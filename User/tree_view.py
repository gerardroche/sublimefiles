from functools import partial
import os
import shutil


import sublime
import sublime_plugin


class TreeViewMoveCommand(sublime_plugin.WindowCommand):

    def is_visible(self, files):
        return len(files) == 1

    def run(self, files):
        if len(files) != 1:
            return

        if not os.path.isfile(files[0]):
            sublime.error_message('Unable to move: invalid file')
            return

        file = files[0]

        head, tail = os.path.split(file)
        root, ext = os.path.splitext(tail)

        input_panel = self.window.show_input_panel(
            'Move:',
            file,
            partial(self.on_done, file),
            None,
            None
        )

        input_panel.sel().clear()
        input_panel.sel().add(sublime.Region(len(head) + 1, (len(head) + 1 + len(root))))

    def on_done(self, file, new_file):
        try:
            if os.path.exists(new_file):
                raise OSError('file already exists')

            new_dir = os.path.split(new_file)[0]
            if not os.path.isdir(new_dir):
                os.makedirs(new_dir)

            os.rename(file, new_file)

            v = self.window.find_open_file(file)
            if v:
                v.retarget(new_file)

        except Exception as e:
            sublime.error_message('Unable to move: ' + str(e))
            return


class TreeViewDuplicateCommand(sublime_plugin.WindowCommand):

    def is_visible(self, files):
        return len(files) == 1

    def run(self, files):
        if len(files) != 1:
            return

        if not os.path.isfile(files[0]):
            sublime.error_message('Unable to duplicate: invalid file')
            return

        file = files[0]

        head, tail = os.path.split(file)
        root, ext = os.path.splitext(tail)
        new_tail = root + ' (Copy)' + ext

        input_panel = self.window.show_input_panel(
            'Duplicate:',
            new_tail,
            partial(self.on_done, file, head),
            None,
            None
        )

        input_panel.sel().clear()
        input_panel.sel().add(sublime.Region(0, len(new_tail) - (len(ext))))

    def on_done(self, file, new_head, new_tail):
        new_file = os.path.join(new_head, new_tail)

        try:
            if os.path.exists(new_file):
                raise OSError('file already exists')

            shutil.copy2(file, new_file)

        except Exception as e:
            sublime.error_message('Unable to duplicate: ' + str(e))
            return


class NewFileMixin():

    extension = None
    content = ''

    def is_visible(self, dirs):
        return len(dirs) == 1

    def run(self, dirs):
        if len(dirs) != 1:
            return

        self.configure()

        extension = self.extension

        if extension is None:
            raise ValueError('extension is required')

        if '.' not in extension:
            extension = '.' + extension

        initial_text = extension

        input_panel = self.window.show_input_panel(
            'New File:',
            initial_text,
            partial(self.on_done, dirs[0]),
            None,
            None
        )

        input_panel.sel().clear()
        input_panel.sel().add(sublime.Region(0, len(initial_text) - (len(initial_text))))

    def on_done(self, dir, file):
        file = os.path.join(dir, file)
        if os.path.exists(file):
            sublime.error_message('Unable to create file, file or folder exists.')
            return

        with open(file, 'w+', encoding='utf8') as f:
            f.write(str(self.content))

        view = self.window.open_file(file + ':99:99', sublime.ENCODED_POSITION)
        view.run_command('_enter_insert_mode')

        def insert_best_completion_async():
            # no idea why this needs to be async but won't work otherwise
            view.run_command('insert_best_completion')

        sublime.set_timeout_async(lambda: insert_best_completion_async())


class TreeViewNewPhpFileCommand(NewFileMixin, sublime_plugin.WindowCommand):

    def configure(self):
        self.extension = 'php'
        self.content = '<?php\n\n'


class TreeViewNewPythonFileCommand(NewFileMixin, sublime_plugin.WindowCommand):

    def configure(self):
        self.extension = 'py'


class TreeViewNewPhtmlFileCommand(NewFileMixin, sublime_plugin.WindowCommand):

    def configure(self):
        self.extension = 'phtml'


class TreeViewNewPhpunitTestCaseFileCommand(NewFileMixin, sublime_plugin.WindowCommand):

    def configure(self):
        self.extension = 'Test.php'
        self.content = 'testcase'