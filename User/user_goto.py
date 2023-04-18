# import os

# import sublime_plugin


# class GotoResultCommand(sublime_plugin.WindowCommand):

#     def run(self, action):
#         exec_panel = self.window.find_output_panel('exec')
#         if not exec_panel:
#             return

#         if exec_panel.sel()[-1].end() == exec_panel.size():
#             exec_panel.run_command("move_to", {"to": "bof"})

#         if action == 'next':
#             self.window.run_command('next_result')
#         else:
#             self.window.run_command('prev_result')
