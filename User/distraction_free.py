from sublime_plugin import WindowCommand


class ToggleTrueFullScreenCommand(WindowCommand):
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


class ToggleTrueDistractionFreeCommand(WindowCommand):
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
