# import sublime_plugin


# # When you see something you like and would like to use it, open an issue about
# # abstracting it out into a reusable package, possibly installable via Package
# # Control.


# # Use cases
# #
# # CTRL-k CTRL-b (TSB)
# #
# # When the sidebar loses focus it auto close.
# #
# # Examples:
# #
# # * TSB then CTRL-1 or CTRL-n (puts focus on view n)
# # * TSB then openning the Command palette or overlay e.g. CTRL-p
# # * TSB then mouse click on a view
# # * TSB then mouse click on the sidebar (which should focus the sidebar)
# # * TSB then CTRL-0 (which will focus the sidebar) followed by any of the
# #   actions describe above.
# #
# # When the sidebar should no auto close:
# #
# # * TSB then mouse click on the sidebar (which should focus the sidebar)


# _DEBUG = False


# class AutoHideSideBarEvents(sublime_plugin.EventListener):

#     _queue_skip = False

#     def on_activated_async(self, view):
#         if _DEBUG:
#             print('AutoHideSideBarEvents *** on_activated_async ***')
#             print('AutoHideSideBarEvents on_activated_async VIEW =', view, view.file_name(), view.id())
#         if not view.settings().get('auto_hide_side_bar'):
#             return

#         window = view.window()
#         if _DEBUG:
#             print('AutoHideSideBarEvents on_activated_async WINDOW =', window)

#         if window and window.is_sidebar_visible() and not self._queue_skip:
#             window.set_sidebar_visible(False)

#         self._queue_skip = False

#     def on_post_text_command(self, view, command, args):
#         if command == 'drag_select':
#             if _DEBUG:
#                 print('AutoHideSideBarEvents *** on_post_text_command ***', view, view.file_name(), view.id())
#             self.on_activated_async(view)

#     def on_post_window_command(self, window, command, args):
#         if command == 'focus_side_bar':
#             if window.is_sidebar_visible():
#                 self._queue_skip = True
#         elif command == 'focus_group':
#             self._queue_skip = False
