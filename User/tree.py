from functools import partial
import os
import shutil

from sublime import ENCODED_POSITION
from sublime import error_message
from sublime import Region
from sublime import set_timeout_async
import sublime_plugin


def _error_message(msg):
    print('Tree:', msg)
    error_message(msg)


class TreeMoveCommand(sublime_plugin.WindowCommand):

    def is_visible(self, files):
        return len(files) == 1

    def run(self, files):
        if len(files) != 1:
            return

        if not os.path.isfile(files[0]):
            _error_message('Unable to move: invalid file')
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
        input_panel.sel().add(Region(len(head) + 1, (len(head) + 1 + len(root))))

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
            _error_message('Unable to move: ' + str(e))


class TreeDuplicateCommand(sublime_plugin.WindowCommand):

    def is_visible(self, files):
        return len(files) == 1

    def run(self, files):
        if len(files) != 1:
            return

        if not os.path.isfile(files[0]):
            return _error_message('Unable to duplicate: invalid file')

        file = files[0]
        head, tail = os.path.split(file)
        root, ext = os.path.splitext(tail)
        new_tail = root + ' (Copy)' + ext
        duplicate_file = os.path.join(head, new_tail)

        input_panel = self.window.show_input_panel(
            'Duplicate:',
            duplicate_file,
            partial(self.on_done, file),
            None,
            None)

        sel = input_panel.sel()
        sel.clear()
        sel.add(Region(len(head) + 1, len(duplicate_file) - (len(ext))))

    def on_done(self, file, duplicate_file):
        try:
            duplicate_file_dirname = os.path.dirname(duplicate_file)
            if not os.path.exists(duplicate_file_dirname):
                os.makedirs(duplicate_file_dirname)

            if os.path.exists(duplicate_file):
                raise OSError('file already exists')

            shutil.copy2(file, duplicate_file)

            self.window.open_file(duplicate_file)

        except Exception as e:
            _error_message('Unable to duplicate: ' + str(e))


class NewFileMixin():

    extension = None
    content = ''

    def is_visible(self, dirs=None):
        return True if dirs is None else len(dirs) == 1

    def init(self):
        pass

    def run(self, dirs=None):
        if dirs is None:
            view = self.window.active_view()
            if not view:
                raise ValueError('expected view')

            file_name = view.file_name()
            if not file_name:
                raise ValueError('expected file name')

            dirs = [os.path.dirname(file_name)]

        if len(dirs) != 1:
            raise ValueError('one directory is required')

        self.init()

        if self.extension and '.' not in self.extension:
            initial_text = '.' + self.extension
        else:
            initial_text = ''

        input_panel = self.window.show_input_panel(
            'New File:',
            initial_text,
            partial(self.on_done, dirs[0]),
            None,
            None)

        sel = input_panel.sel()
        sel.clear()
        sel.add(Region(0, len(initial_text) - (len(initial_text))))

    def on_done(self, dir, file):
        file = os.path.join(dir, file)

        file_directory = os.path.dirname(file)
        if not os.path.exists(file_directory):
            os.makedirs(file_directory)

        if os.path.exists(file):
            _error_message('Unable to create file, file or folder exists.')
            return

        with open(file, 'w+', encoding='utf8') as f:
            f.write(str(self.content))

        view = self.window.open_file(file + ':99:99', ENCODED_POSITION)
        view.run_command('_enter_insert_mode')

        def _insert_best_completion_async():
            # no idea why this needs to be async but won't work otherwise
            view.run_command('insert_best_completion')

        set_timeout_async(lambda: _insert_best_completion_async())


class TreeNewFileCommand(NewFileMixin, sublime_plugin.WindowCommand):
    pass


class TreeNewHtmlFileCommand(NewFileMixin, sublime_plugin.WindowCommand):
    def init(self):
        self.extension = 'html'


class TreeNewMarkdownFileCommand(NewFileMixin, sublime_plugin.WindowCommand):
    def init(self):
        self.extension = 'md'


class TreeNewPhpFileCommand(NewFileMixin, sublime_plugin.WindowCommand):
    def init(self):
        self.extension = 'php'
        self.content = '<?php\n\n'


class TreeNewPhpunitTestCaseFileCommand(NewFileMixin, sublime_plugin.WindowCommand):
    def init(self):
        self.extension = 'Test.php'
        self.content = 'testcase'


class TreeNewPhtmlFileCommand(NewFileMixin, sublime_plugin.WindowCommand):
    def init(self):
        self.extension = 'phtml'


class TreeNewPythonFileCommand(NewFileMixin, sublime_plugin.WindowCommand):
    def init(self):
        self.extension = 'py'
