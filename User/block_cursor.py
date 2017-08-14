# import sublime

# from sublime_plugin import EventListener


# _DEBUG = False


# class UserBlockCursor(EventListener):

#     def on_activated(self, view):
#         if _DEBUG: print('=> CURSOR.on_activated()', view.file_name())  # noqa
#         self._redraw(view)

#     def on_deactivated(self, view):
#         if _DEBUG: print('=> CURSOR.on_deactivated()', view.file_name())  # noqa
#         if _DEBUG: print('=> CURSOR.on_deactivated() ERASE INSERT CURSOR!')  # noqa
#         view.erase_regions('InsertModeCursor')

#     def on_post_save(self, view):
#         if _DEBUG: print('=> CURSOR.on_post_save()', view.file_name())  # noqa
#         if view.window().active_view().id() != view.id():
#             if _DEBUG: print('=> CURSOR.on_post_save() ERASE INSERT CURSOR!', view.file_name())  # noqa
#             view.erase_regions('InsertModeCursor')

#     def on_selection_modified(self, view):
#         if _DEBUG: print('=> CURSOR.on_selection_modified()', view.file_name())  # noqa
#         self._redraw(view)

#     def on_text_command(self, view, command, args):
#         if _DEBUG: print('=> CURSOR.on_text_command()', 'command=', command, 'view=', view.file_name())  # noqa
#         if command == '_enter_insert_mode':
#             self._redraw(view, True)
#         elif command == '_enter_normal_mode':
#             if _DEBUG: print('=> CURSOR.on_text_command() ERASE INSERT CURSOR!')  # noqa
#             view.erase_regions('InsertModeCursor')

#     def _redraw(self, view, force=False):
#         if _DEBUG: print('=> CURSOR._redraw()', 'force=', force, 'view=', view.file_name())  # noqa
#         if _DEBUG: print('=> CURSOR._redraw() ERASE INSERT CURSOR!')  # noqa
#         view.erase_regions('InsertModeCursor')

#         regions = []
#         if force or (not view.settings().get('command_mode') and not view.settings().get('is_widget')):
#             for sel in view.sel():
#                 if sel.begin() != sel.end():
#                     continue
#                 regions.append(sublime.Region(sel.begin(), sel.begin() + 0))

#         if regions:
#             if _DEBUG: print('ADD INSERT CURSOR!')  # noqa
#             view.add_regions('InsertModeCursor', regions, 'insert_mode_cursor', '', sublime.DRAW_EMPTY)
