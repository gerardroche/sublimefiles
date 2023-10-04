from contextlib import contextmanager

from sublime import decode_value
from sublime import load_resource
from sublime import load_settings
from sublime import save_settings


def decode_resource(name: str):
    return decode_value(load_resource(name))


@contextmanager
def save_preferences():
    yield load_settings('Preferences.sublime-settings')
    save_settings('Preferences.sublime-settings')
