import sublime_plugin


class KitchenSinkDumpSettings(sublime_plugin.WindowCommand):

    def run(self, prefixes=None):
        print('\n\n')
        print('----- Dump Settings -----')
        print('\n\n')

        view = self.window.active_view()
        settings = view.settings().to_dict()

        for name, value in settings.items():
            display = False if prefixes else True
            if not display:
                for prefix in prefixes:
                    if name.startswith(prefix):
                        display = True
                        continue

            if display:
                print('  ', name, '=>', value)

        print('\n\n')
