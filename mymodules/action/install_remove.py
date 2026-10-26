import subprocess
from mymodules.action import pkg
from mymodules.action.dial import SetToolTip, action, dial


def show_state(img, button, name, installed):
    img.set_from_file(action.gtk_yes if installed else action.gtk_no)
    button.set_tooltip_markup(format(SetToolTip(name, action.installed, action.remove_it)
        if installed else SetToolTip(name, action.not_here, action.install_it)))


class StartKickingSomeNinjas(object):

    def __init__(self, _, app):
        img, button, name = action.dicti[app]
        remove = pkg.is_installed(app, pkg.installed_packages())
        subprocess.run(pkg.command(app, remove), stdin=subprocess.DEVNULL, env=pkg.ENV)
        if pkg.is_installed(app, pkg.installed_packages()) != remove:
            show_state(img, button, name, not remove)
            dial(name, action.remove_it if remove else action.installed)
