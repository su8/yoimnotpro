from appcenter import categories, ui
from appcenter.installer import on_app_clicked, show_apps

# popular apps from all categories; names, descriptions and widget ids come from the catalog
APPS = ('geany', 'blender', 'ninja-ide', 'glade', 'audacious', 'gimp', 'evince', 'xfburn', 'flashplugin',
        'openshot', 'chromium', 'deluge', 'liferea', 'htop', 'skype', 'wireshark-gtk', 'virtualbox', 'steam',
        'xchat', 'gedit')
CATALOG = {app: info for category in categories.ALL for app, info in category.apps.items()}


def widget(app):
    """Widget id prefix in ui/start.ui: the category's widget id plus '_'."""
    info = CATALOG[app]
    return (info[1] if len(info) > 2 else app) + '_'


class StartScreen(object):
    """The grid shown at startup."""

    def __init__(self):
        self.builder = ui.builders['start']
        self.grid = self.builder.get_object('apps_grid')
        for app in APPS:
            self.builder.get_object(widget(app) + 'icon_tooltip_').set_tooltip_text(CATALOG[app][-1])
            self.builder.get_object(widget(app)).connect("clicked", on_app_clicked, app)

    def load(self):
        get = self.builder.get_object
        show_apps({app: (get(widget(app) + 'img_'), get(widget(app)), CATALOG[app][0]) for app in APPS})
