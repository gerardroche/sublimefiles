import os

from sublime import load_settings
from sublime import packages_path
from sublime import save_settings
import sublime_plugin

from Default.fold import FoldCommand as DefaultFoldCommand
from Default.fold import UnfoldCommand as DefaultUnfoldCommand


# When you see something you like and would like to use it, open an issue about
# abstracting it out into a reusable package, possibly installable via Package
# Control.

# TODO RenameFile() command

# TODO ExtractVariable() command

# TODO InlineVariable() command

# TODO OpenChangedFiles() command

# TODO SelectaFile("name") command


def _find_in_open_folders(window, interactive=True, default_filter=False):
    view = window.active_view()
    region = view.sel()[0]
    word = view.word(region)
    view.sel().clear()
    view.sel().add(word)

    def get_default_filter():
        include_filters = []

        file_name = view.file_name()
        if file_name:
            include_filters.append('*' + os.path.splitext(file_name)[1])

        if include_filters:
            return ',' + ','.join(include_filters)
        else:
            return ''

    window.run_command('show_panel', {
        'panel': 'find_in_files',
        'where': '<open folders>' + get_default_filter() if default_filter else '',
        'whole_word': True,
        'case_sensitive': False,
        'regex': False,
        'use_buffer': True,
        'show_context': True
    })

    view.sel().clear()
    view.sel().add(region)

    if not interactive:
        window.run_command('find_all', {
            'close_panel': True
        })


def _post_fold_command_fixes(view):
    # Reset cursors to begining and start of
    # lines and clear any visual selections.
    sels = []
    for sel in view.sel():
        sels.append(view.text_point(view.rowcol(sel.begin())[0], 0))

    if sels:
        view.sel().clear()
        view.sel().add_all(sels)


# TODO Cleanup and submit a PR for this to be added to SublimeLinter core.
class LintersCommand(sublime_plugin.WindowCommand):
    def run(self, action):
        settings = load_settings('SublimeLinter.sublime-settings')

        if action == 'toggle_mode':
            lint_mode = settings.get('lint_mode')
            if lint_mode:
                if lint_mode != 'load_save':
                    lint_mode = 'load_save'
                else:
                    lint_mode = 'background'

            settings.set('lint_mode', lint_mode)
            save_settings('SublimeLinter.sublime-settings')

            return

        # TODO How to get a real list of installed linters?
        linters = settings.get('linters')

        items = []
        for linter, linter_settings in linters.items():
            is_disabled = linter_settings.get('disable', False)

            if action == 'disable':
                if not is_disabled:
                    items.append(linter)
            elif action == 'enable':
                if is_disabled:
                    items.append(linter)
            elif action == 'toggle':
                items.append(linter)
            else:
                raise RuntimeError('unknown action')

        def on_done(index):
            if index >= 0:
                linter = items[index]

                if action == 'disable':
                    disable = True
                elif action == 'enable':
                    disable = False
                elif action == 'toggle':
                    if 'disable' in linters[linter]:
                        disable = not linters[linter]['disable']
                    else:
                        disable = True

                linters[linter]['disable'] = disable
                settings.set('linters', linters)
                save_settings('SublimeLinter.sublime-settings')

        self.window.show_quick_panel(items, on_done)


class FindInOpenFoldersCommand(sublime_plugin.WindowCommand):
    def run(self, interactive=True, default_filter=False):
        _find_in_open_folders(self.window, interactive, default_filter)


class TaskListCommand(sublime_plugin.WindowCommand):
    def run(self, interactive=True):
        self.window.run_command('show_panel', {
            'panel': 'find_in_files',
            'where': '<open folders>,-.srcpath/,-.buildpath/,-vendor/,-res/doc/',
            'whole_word': False,
            'case_sensitive': False,
            'preserve_case': False,
            'regex': True,
            'use_buffer': False,
            'show_context': False,
        })

        self.window.run_command('insert', {'characters': '(#|//)\\s*(TODO|FIXME|XXX|IMPORTANT|DEPRECATED)'})

        if not interactive:
            self.window.run_command('find_all', {'close_panel': True})


class FocusUnitTestingPanelCommand(sublime_plugin.WindowCommand):
    def run(self):
        name = 'output.UnitTesting'
        self.window.run_command('show_panel', {'panel': name})

        name = 'UnitTesting'
        self.window.focus_view(self.window.find_output_panel(name))


class FoldCommand(DefaultFoldCommand):
    def run(self, edit):
        super().run(edit)
        _post_fold_command_fixes(self.view)


class GotoSymbolInFileCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('show_overlay', {
            'overlay': 'goto',
            'text': '@'
        })


class HidePhantoms(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('exec', {
            'hide_phantoms_only': True
        })


class OpenPreferencesCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('open_file', {
            'file': os.path.join(
                packages_path(),
                'User',
                'Preferences.sublime-settings'
            )
        })


class RulersCommand(sublime_plugin.TextCommand):
    def run(self, edit, action):
        col = self.view.rowcol(self.view.sel()[0].begin())[1]
        if col > 0:
            queue_save = False
            settings = self.view.settings()
            rulers = settings.get('rulers')

            if action == 'add':
                if col not in rulers:
                    rulers.append(col)
                    queue_save = True
            elif action == 'remove':
                if col in rulers:
                    rulers.remove(col)
                    queue_save = True
            elif action == 'clear':
                if rulers != []:
                    rulers = []
                    queue_save = True
            else:
                raise Exception('unknown action')

            if queue_save:
                rulers.sort()
                if rulers:
                    settings.set('rulers', rulers)
                else:
                    settings.erase('rulers')


class ShowCommandPaletteCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('show_overlay', {
            'overlay': 'command_palette'
        })


class ShowFindInFilesCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('show_panel', {
            'panel': 'find_in_files'
        })


class ShowFindResultsCommand(sublime_plugin.WindowCommand):
    def run(self):
        for view in self.window.views():
            if view.name() == 'Find Results':
                # Clear any visual selection.
                sel = view.sel()[0].begin()
                view.sel().clear()
                view.sel().add(sel)

                return self.window.focus_view(view)


class ToggleDistractionFreeCommand(sublime_plugin.WindowCommand):
    _is_active = False
    _original_is_menu_visible = False

    def run(self):
        self.window.run_command('toggle_distraction_free')

        if self._is_active:
            self.window.set_menu_visible(self._original_is_menu_visible)
            self._is_active = False
        else:
            self._original_is_menu_visible = self.window.is_menu_visible()
            self.window.set_menu_visible(False)
            self._is_active = True


class ToggleFullScreenCommand(sublime_plugin.WindowCommand):
    _is_active = False
    _original_is_menu_visible = False

    def run(self):
        self.window.run_command('toggle_full_screen')

        if self._is_active:
            self.window.set_menu_visible(self._original_is_menu_visible)
            self._is_active = False
        else:
            self._original_is_menu_visible = self.window.is_menu_visible()
            self.window.set_menu_visible(False)
            self._is_active = True


class ToggleTemporaryFolderCommand(sublime_plugin.WindowCommand):
    def run(self):
        preferences = load_settings('Preferences.sublime-settings')

        folder_exclude_patterns = preferences.get('folder_exclude_patterns', [])

        if 'tmp' not in folder_exclude_patterns:
            folder_exclude_patterns.append('tmp')
        else:
            folder_exclude_patterns.remove('tmp')

        folder_exclude_patterns.sort()
        preferences.set('folder_exclude_patterns', folder_exclude_patterns)

        save_settings('Preferences.sublime-settings')


class UnfoldCommand(DefaultUnfoldCommand):
    def run(self, edit):
        super().run(edit)
        _post_fold_command_fixes(self.view)
