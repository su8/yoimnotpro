import os
from configparser import ConfigParser
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

SETTINGS = os.path.expanduser('~/.yoimnotpro.conf')
LANGUAGES = {"English": 'english', "Български": 'bulgarian', "Русский": 'russian', "Deutsch": 'german',
    "Español": 'spanish', "Français": 'french', "हिंदी": 'hindi'}


class text(object):
    """Strings of the current language, filled in by load_language()."""
    language = 'english'


def load_language():
    if os.path.isfile(SETTINGS):
        with open(SETTINGS, 'rt') as f:
            text.language = f.read().split(',')[0]  # older versions saved "language,encoding"
    else:
        text.language = 'english'
    translations = ConfigParser()
    translations.read('translations/langs.ini')
    for key, value in translations.items(text.language):
        if key in ['development', 'graphics', 'internet', 'system',
                   'multimedia', 'utilities', 'about', 'language']:
            value = '<b>{}</b>'.format(value)
        elif key in ['status_installed', 'status_not_installed']:
            value = '<span foreground="{}" weight="bold">{}</span>'.format(
                'green' if key == 'status_installed' else 'red', value)
        setattr(text, key, value)


def app_tooltip(name, installed):
    """Tooltip of an app's install/remove button."""
    english = text.language == 'english'
    return '<b><i>{}</i></b> {} {}.\n{} {} {}'.format(
        name.capitalize(),
        'is' if english else (text.is_ if installed else ''),
        text.status_installed if installed else text.status_not_installed,
        text.click_to,
        text.remove_it if installed else text.install_it,
        'it' if english else '')


class LanguagePicker(object):
    """Window with a language list; picking one saves it, reloads the strings and calls on_change()."""

    def __init__(self, on_change):
        self.on_change = on_change
        window = Gtk.Window()
        window.set_title('Select Language')
        self.combobox = Gtk.ComboBoxText()
        self.combobox.append("", "Languages:")
        for name in sorted(LANGUAGES):
            self.combobox.append('', name)
        self.combobox.set_active(0)
        self.combobox.connect("changed", self.on_changed)
        window.add(self.combobox)
        window.show_all()
        window.connect("destroy", lambda window: Gtk.main_quit())
        Gtk.main()

    def on_changed(self, combobox):
        name = self.combobox.get_active_text()
        if name in LANGUAGES:
            with open(SETTINGS, 'wt') as f:
                f.write(LANGUAGES[name])
            load_language()
            self.on_change()
