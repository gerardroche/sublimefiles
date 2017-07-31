from sublime import load_settings
from sublime import save_settings
from sublime import status_message
from sublime_plugin import ApplicationCommand


class ToggleNeovintageousArrowKeysCommand(ApplicationCommand):
    def run(self):
        settings = load_settings('Preferences.sublime-settings')

        flag = not settings.get('neovintageous_disable_arrow_keys', False)
        settings.set('neovintageous_disable_arrow_keys', flag)

        save_settings('Preferences.sublime-settings')

        status = 'enabled' if flag else 'disabled'
        status_message('NeoVintageous hard time is {}'.format(status))
