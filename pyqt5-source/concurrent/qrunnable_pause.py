import sys
import time

from PyQt5.QtCore import (
    QObject,
    QRunnable,
    QThreadPool,
    pyqtSignal,
    pyqtSlot,
)
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QWidget,
)


class WorkerKilledException(Exception):
    pass


class WorkerSignals(QObject):
    progress = pyqtSignal(int)


class JobRunner(QRunnable):
    signals = WorkerSignals()

    def __init__(self):
        super().__init__()

        self.is_paused = False
        self.is_killed = False

    @pyqtSlot()
    def run(self):
        try:
            for n in range(100):
                self.signals.progress.emit(n + 1)
                time.sleep(0.1)

                while self.is_paused:
                    time.sleep(0)  # <1>

                if self.is_killed:
                    raise WorkerKilledException

        except WorkerKilledException:
            pass

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

    def kill(self):
        self.is_killed = True


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Some buttons
        w = QWidget()
        l = QHBoxLayout()
        w.setLayout(l)

        btn_stop = QPushButton("Stop")
        btn_pause = QPushButton("Pause")
        btn_resume = QPushButton("Resume")

        l.addWidget(btn_stop)
        l.addWidget(btn_pause)
        l.addWidget(btn_resume)

        self.setCentralWidget(w)

        # Create a statusbar.
        self.status = self.statusBar()
        self.progress = QProgressBar()
        self.status.addPermanentWidget(self.progress)

        # Thread runner
        self.threadpool = QThreadPool()

        # Create a runner
        self.runner = JobRunner()
        self.runner.signals.progress.connect(self.update_progress)
        self.threadpool.start(self.runner)

        btn_stop.pressed.connect(self.runner.kill)
        btn_pause.pressed.connect(self.runner.pause)
        btn_resume.pressed.connect(self.runner.resume)

    def update_progress(self, n):
        self.progress.setValue(n)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
