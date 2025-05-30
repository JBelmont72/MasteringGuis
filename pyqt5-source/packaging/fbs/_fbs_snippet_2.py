from fbs_runtime.application_context.PyQt5 import ApplicationContext


class AppContext(ApplicationContext):

	def __init__(self, *args, _kwargs):
		super().__init__(*args, _kwargs)

		self.window = Window()

    def run(self):
        self.window.show()
        return self.app.exec_()

# ... snip ...
