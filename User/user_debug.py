import re
import sys

import sublime
import sublime_plugin


class DebugEvents(sublime_plugin.EventListener):

    def on_activated_async(self, view):
        view.set_status('st_build', 'Build ' + sublime.version())


class ToggleDebugCommand(sublime_plugin.WindowCommand):

    enabled = False

    def description(self):
        return '%s Debug Mode' % ('Disable' if self.enabled else 'Enable')

    def run(self):
        self.enabled = not self.enabled

        sublime.log_build_systems(self.enabled)
        sublime.log_commands(self.enabled)
        # sublime.log_indexing(self.enabled)
        sublime.log_input(self.enabled)
        sublime.log_result_regex(self.enabled)
        if int(sublime.version()) >= 4064:
            sublime.log_control_tree(self.enabled)


class DumpInfoCommand(sublime_plugin.WindowCommand):
    def run(self):
        print('+-------------------')
        print('| Sublime Text version               ', sublime.version())
        print('| Python version                      {}.{}.{} {}{}'.format(
            sys.version_info[0],
            sys.version_info[1],
            sys.version_info[2],
            sys.version_info[3],
            sys.version_info[4]))
        print('| %-35s %s' % ('sys.flags', sys.flags))
        print('| %-35s %s' % ('sys.abiflags', sys.abiflags))
        print('| %-35s %s' % ('sys.path', sys.path))
        print('| %-35s %s' % ('__debug__', __debug__))
        print('| sublime.platform()                 ', sublime.platform())
        print('| sublime.arch()                     ', sublime.arch())
        print('| sublime.channel()                  ', sublime.channel())
        print('| sublime.executable_path()          ', sublime.executable_path())
        print('| sublime.packages_path()            ', sublime.packages_path())
        print('| sublime.installed_packages_path()  ', sublime.installed_packages_path())
        print('| sublime.cache_path():              ', sublime.cache_path())
        print('+')


class DumpScopeCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        scopes = []
        for point in range(view.size()):
            # scope_name() needs to striped due to a bug in ST:
            # See https://github.com/SublimeTextIssues/Core/issues/657.
            scopes.append(view.scope_name(point).strip())

        print(">>>\n".join(scopes) + '<<<')


class DumpViewCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()

        print('>>> *** Dump View ***\n{} [id={}, file={}]'
              '\n buffer_id={: <10}        is_valid={: <10}     is_primary={: <10}   name={: <5}'
              '\n is_dirty={: <10}         is_read_only={: <10} is_scratch={: <10}   encoding={: <5}'
              '\n line_endings={: <10}     is_in_edit={: <10}   change_count={: <10} is_loading={: <5}'
              '\n line_height={: <10}      em_width={: <10}     is_popup_visible={: <10}'
              '\n overwrite_status={: <10} size={: <10}         is_auto_complete_visible={: <10}'
              '\n has_non_empty_selection_region={: <10}'
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
            print('   sel[{}] viewport_position {} {}'.format(i, view.viewport_position(), type(view.viewport_position())))  # noqa: E501
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
        print('<<<')
