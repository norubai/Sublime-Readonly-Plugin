import sublime
import sublime_plugin

###############################################################################
# Makes the view editable
class ClearPepperCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        filePath = self.view.file_name().split('/')
        fileName = filePath[-1]
        view.set_read_only(False)
        sublime.message_dialog(fileName + ' is editable')
        view.set_status('pepper_stat', '')

###############################################################################
# Makes the view read-only
class SetPepperCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        filePath = self.view.file_name().split('/')
        fileName = filePath[-1]
        view.set_read_only(True)
        sublime.message_dialog(fileName + ' is read only')
        view.set_status('pepper_stat', 'Read-Only')

###############################################################################
# Toggles the view's read only attribute
class TogglePepperCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        if view.is_read_only():
            view.run_command('clear_pepper')
        else:
            view.run_command('set_pepper')
    def is_checked(self):
        return self.view.is_read_only()


## TODO: add settings so that files become readonly by default when theyre opened