import logging
import os
import sys

from sublime import active_window
from sublime import log_build_systems
from sublime import log_commands
from sublime import log_indexing
from sublime import log_input
from sublime import log_result_regex
from sublime import packages_path
from sublime_plugin import ApplicationCommand
from sublime_plugin import WindowCommand
from sublime_plugin import TextCommand


_DEBUG = bool(os.getenv('SUBLIME_DEBUG'))


class ToggleDebugModeCommand(ApplicationCommand):
    def run(self):
        global _DEBUG
        _DEBUG = not _DEBUG
        _sublime_log(_DEBUG)

        file = os.path.join(packages_path(), 'User', '.debug')
        if os.path.isfile(file):
            if not _DEBUG:
                os.remove(file)
        else:
            if _DEBUG:
                with open(file, 'w+', encoding='utf8') as f:
                    f.write('')


class DebugViewToScopeCommand(TextCommand):
    def run(self, edit):
        scopes = []
        for point in range(self.view.size()):
            scopes.append(self.view.scope_name(point).strip())

        print('>>>')
        print("\n".join(scopes))
        print('<<<')


def _sublime_log(flag):
    log_commands(flag)
    log_input(flag)
    log_result_regex(flag)
    # log_indexing(flag)
    log_build_systems(flag)


def plugin_loaded():
    global _DEBUG

    log_indexing(False)  # disable it by default

    file = os.path.join(packages_path(), 'User', '.debug')
    if os.path.isfile(file):
        _DEBUG = True

    if _DEBUG:
        print('DEBUG User: debug is enabled')
        active_window().run_command('show_panel', {'panel': 'console'})
        _sublime_log(True)

        print('DEBUG User: python v{}.{}.{} ({})'.format(
            sys.version_info[0],
            sys.version_info[1],
            sys.version_info[2],
            sys.version_info
        ))

        print('DEBUG User: paths = {}'.format(sys.path))
        print('DEBUG User: abiflags = {}, flags = {}'.format(sys.abiflags, sys.flags))
        print('                       Legend = attribute: flag, debug: -d, inspect: -i, interactive: -i, optimize: -O or -OO, dont_write_bytecode: -B, no_user_site: -s, no_site: -S, ignore_environment: -E, verbose: -v, bytes_warning: -b, quiet: -q, hash_randomization: -R')  # noqa: E501
        print('DEBUG User: platform = {} (Linux: \'linux\', Windows: \'win32\', Windows/Cygwin: \'cygwin\', Mac OS X: \'darwin\')'.format(sys.platform))  # noqa: E501

        window = active_window()
        if not window:
            return

        view = window.active_view()
        if not view:
            return

        settings = view.settings()
        if not settings:
            return

        if not settings.get('user.debug'):
            return

        print('DEBUG User: \'user.debug\' is enabled')

        if settings.get('user.debug.neovintageous'):
            neovintageous_debug_settings = settings.get('user.debug.neovintageous')
            print('DEBUG User: \'user.debug.neovintageous\' =', neovintageous_debug_settings)

            if isinstance(neovintageous_debug_settings, dict):
                if 'level' in neovintageous_debug_settings:
                    logging.getLogger('NeoVintageous').setLevel(getattr(
                        logging,
                        neovintageous_debug_settings['level'].strip().upper(),
                        logging.DEBUG
                    ))


class DebugViewCommand(TextCommand):

    def run(self, edit=None):
        view = self.view

        print('>>> DEBUG {} [id={}, file={}'
              '\n buffer_id={: <5}        is_valid={: <5}     is_primary={: <5}   name={: <5}'
              '\n is_dirty={: <5}         is_read_only={: <5} is_scratch={: <5}   encoding={: <5}'
              '\n line_endings={: <5}     is_in_edit={: <5}   change_count={: <5} is_loading={: <5}'
              '\n line_height={: <5}      em_width={: <5}     is_popup_visible={: <5}'
              '\n overwrite_status={: <5} size={: <5}         is_auto_complete_visible={: <5}'
              '\n has_non_empty_selection_region={: <5}'
              .format(
                  str(view),
                  str(view.id()), str(view.file_name()),
                  str(view.buffer_id()), str(view.is_valid()), str(view.is_primary()), str(view.name()),
                  str(view.is_dirty()), str(view.is_read_only()), str(view.is_scratch()), str(view.encoding()),
                  str(view.line_endings()), str(view.is_in_edit()), str(view.change_count()), str(view.is_loading()),
                  str(view.line_height()), str(view.em_width()), str(view.is_popup_visible()),
                  str(view.overwrite_status()), str(view.size()), str(view.is_auto_complete_visible()),
                  str(view.has_non_empty_selection_region())))

        print(' sel={}:{}'.format(type(view.sel()), list(view.sel())))

        for i, sel in enumerate(view.sel()):
            print('   sel[{}] {} a = {}, b = {}'.format(i, sel, sel.a, sel.b))
            print('   sel[{}] begin = {}, end = {}, begin substr = "{}", end substr = "{}"'.format(
                i, sel.begin(), sel.end(),
                view.substr(sel.begin()).replace('\n', '\\n'),
                view.substr(sel.end()).replace('\n', '\\n')
            ))
            print('   sel[{}] empty? {}'.format(i, sel.empty()))
            print('   sel[{}] word {} substr >>>{}<<<'.format(
                i, view.word(sel.begin()), view.substr(view.word(sel.begin()))).replace('\n', '\\n'))
            print('   sel[{}] rowcol {} {}'.format(i, view.rowcol(sel.begin()), type(view.rowcol(sel.begin()))))
            print('   sel[{}] visible_region {} {}'.format(i, view.visible_region(), type(view.visible_region())))
            print('   sel[{}] viewport_position {} {}'.format(i, view.viewport_position(), type(view.viewport_position())))
            print('   sel[{}] viewport_extent {} {}'.format(i, view.viewport_extent(), type(view.viewport_extent())))
            print('   sel[{}] layout_extent {} {}'.format(i, view.layout_extent(), type(view.layout_extent())))
            print('   sel[{}] text_to_layout (begin) {} {}'.format(
                i, view.text_to_layout(sel.begin()), type(view.text_to_layout(sel.begin()))))
            # print('    sel[{}] word classify = {}'.format(i, view.classify(sel.begin())))
            # print('    sel[{}] scope name begin = {}'.format(i, view.scope_name(sel.begin())))
            # print('    sel[{}] indentation level begin = {}'.format(i, str(view.indentation_level(sel.begin()))))
            # print('    sel[{}] indented region begin = {}'.format(i, view.indented_region(sel.begin())))
            # print('    sel[{}] indented region begin substr = >>{}<<'.format(
            #   i, view.substr(view.indented_region(sel.begin()))))


class DebugNeovintageousView(TextCommand):

    def run(self, edit):

        keys = [
            '_cmdline_cd',
            '_vintageous_cmdline_cd',
            '_vintageous_glue_until_normal_mode',
            '_vintageous_last_buffer_search',
            '_vintageous_last_buffer_search_command',
            '_vintageous_last_char_search_command',
            '_vintageous_last_character_search',
            '_vintageous_non_interactive',
            '_vintageous_processing_notation',
            '_vintageous_reset_during_init',
            'action',
            'action_count',
            'autoindent',
            'command_mode',
            'ex_data',
            'hlsearch',
            'ignorecase',
            'incsearch',
            'inverse_caret_state',
            'last_buffer_search',
            'linux_shell',
            'magic',
            'mode',
            'motion',
            'motion_count',
            'must_capture_register_name',
            'normal_insert_count',
            'partial_sequence',
            'recording',
            'register',
            'repeat_data',
            'rulers',
            'sequence',
            'showsidebar',
            'vi_editor_setting',
            'vintage',
            'vintageous_action',
            'vintageous_action_count',
            'vintageous_autoindent',
            'vintageous_cmdline_cd',
            'vintageous_command_mode',
            'vintageous_enable_cmdline_mode',
            'vintageous_enable_surround',
            'vintageous_ex_data',
            'vintageous_hlsearch',
            'vintageous_ignorecase',
            'vintageous_ignorecase',
            'vintageous_incsearch',
            'vintageous_inverse_caret_state',
            'vintageous_last_buffer_search',
            'vintageous_linux_shell',
            'vintageous_magic',
            'vintageous_magic',
            'vintageous_mode',
            'vintageous_motion',
            'vintageous_motion_count',
            'vintageous_must_capture_register_name',
            'vintageous_normal_insert_count',
            'vintageous_partial_sequence',
            'vintageous_recording',
            'vintageous_register',
            'vintageous_repeat_data',
            'vintageous_rulers',
            'vintageous_sequence',
            'vintageous_showsidebar',
            'vintageous_surround_spaces',
            'vintageous_use_ctrl_keys',
            'vintageous_use_sys_clipboard',
            'vintageous_vi_editor_setting',
            'VintageousEx_linux_shell',
            'VintageousEx_linux_terminal',
            'VintageousEx_osx_shell',
            'VintageousEx_osx_terminal',
            'visual_bloc',
            'visual_block_direction',
            'visualbell',
            'WrapPlus.include_line_ending',
            'xpos',
        ]

        print('>>> DEBUG NeoVintageous view[id={},file={}]'.format(self.view.id(), self.view.file_name()))

        settings = self.view.settings()
        for key in keys:
            value = settings.get(key)
            if isinstance(value, dict):
                print('  {} {{'.format(key))
                for k, v in value.items():
                    print('    {} = {}'.format(k, v))
                print('  }')
            else:
                print('  {} = {}'.format(key, value))

        print('<<<')
