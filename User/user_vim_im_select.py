import sublime_plugin


def is_normal_view(view) -> bool:
    return view and view.element() is None


def is_command_mode(view) -> bool:
    return is_normal_view(view) and view.settings().get('command_mode')


# class ImSelectEvents(sublime_plugin.EventListener):

#     def on_post_text_command(self, view, command_name, args):
#         if is_command_mode(view):
#             print('in NORMAL mode')
#         else:
#             print('in INSERT mode')
