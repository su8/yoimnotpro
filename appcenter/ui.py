from appcenter.i18n import text
from gi.repository import Gtk

CATEGORIES = ('development', 'graphics', 'internet', 'multimedia', 'system', 'utilities')
INSTALLED_ICON = './icons/installed.png'
NOT_INSTALLED_ICON = './icons/not-installed.png'


def load(path):
    builder = Gtk.Builder()
    builder.add_from_file(path)
    return builder

main = load('./ui/main.ui')
builders = {name: load('./ui/{}.ui'.format(name)) for name in CATEGORIES + ('start',)}


def highlight_category(category):
    """Show the active icon on this category's sidebar button and the plain one on the others."""
    for name in CATEGORIES:
        extension = 'xpm' if name == 'system' else 'png'
        main.get_object(name + '_icon').set_from_file('./icons/{}{}.{}'.format(
            name, '-active' if name == category else '', extension))


def set_category_tooltips():
    for name in CATEGORIES + ('about', 'language'):
        main.get_object(name + '_button').set_tooltip_markup(getattr(text, name))
