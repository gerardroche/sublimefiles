from functools import partial
import os


import sublime
import sublime_plugin


def new_file(window, dirs, suffix, content=''):
    if len(dirs) != 1:
        return

    initial_text = suffix

    def on_done(dir, file):
        file = os.path.join(dir, file)
        if os.path.exists(file):
            return sublime.error_message(
                'Unable to create file, file or folder exists.')

        with open(file, 'w+', encoding='utf8') as f:
            f.write(str(content))

        view = window.open_file(file + ':99:99', sublime.ENCODED_POSITION)
        view.run_command('_enter_insert_mode')

        def needs_to_be_async_no_idea_why():
            view.run_command('insert_best_completion')
        sublime.set_timeout_async(lambda: needs_to_be_async_no_idea_why())

    input_panel = window.show_input_panel(
        'File:',
        initial_text,
        partial(on_done, dirs[0]),
        None,
        None
    )

    input_panel.sel().clear()
    region = sublime.Region(0, len(initial_text) - (len(initial_text)))
    input_panel.sel().add(region)


class NewFileByExtension:

    def extension(self):
        return None

    def content(self):
        return ''

    def is_visible(self, dirs = []):
        return len(dirs) == 1

    def run(self, dirs):

        extension = self.extension()

        if extension is None:
            raise ValueError('extension is required')

        if '.' not in extension:
            extension = '.' + extension

        content = self.content()

        new_file(self.window, dirs, extension, content)


class NewPhpFile(NewFileByExtension, sublime_plugin.WindowCommand):

    def extension(self):
        return 'php'

    def content(self):
        return '<?php\n\n'

class NewPythonFile(NewFileByExtension, sublime_plugin.WindowCommand):
    def extension(self):
        return 'py'


class NewPhtmlFile(NewFileByExtension, sublime_plugin.WindowCommand):
    def extension(self):
        return 'phtml'


class NewPhpunitTestCaseFile(NewFileByExtension, sublime_plugin.WindowCommand):

    def extension(self):
        return 'Test.php'

    def content(self):
        return 'testcase'
