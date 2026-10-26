import subprocess
import threading
from random import choice
from appcenter import packages, ui
from appcenter.i18n import app_tooltip, text
from gi.repository import GLib, Gtk

shown_apps = {}  # app: (status image, install/remove button, display name) of the visible grid


def show_state(img, button, name, installed):
    img.set_from_file(ui.INSTALLED_ICON if installed else ui.NOT_INSTALLED_ICON)
    button.set_tooltip_markup(app_tooltip(name, installed))


def show_apps(apps):
    """Make apps the visible ones and show whether each is installed or not available."""
    shown_apps.clear()
    shown_apps.update(apps)
    installed = packages.installed_packages()
    for app, (img, button, name) in apps.items():
        available = packages.package(app) is not None
        button.set_sensitive(available)
        if available:
            show_state(img, button, name, packages.is_installed(app, installed))
        else:
            img.set_from_file(ui.NOT_INSTALLED_ICON)
            button.set_tooltip_markup(text.not_available.format(
                name=name, system=packages.NAMES[packages.SYSTEM]))


def show_success(name, removed):
    moods = ((text.how_dare_you, text.pitty_to_see_it_go, '>:-(', text.was_douchebag, 'LMAO', 'LOL',
              text.damn_you_bro) if removed else
             (text.good_choice, text.thats_my_boy, text.i_like_it_too, text.cheers, '>:-)', text.eyecandy))
    dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
        '{} {} {} {}.'.format(name, text.was, text.removed if removed else text.installed, text.successfully),
        title='{} {}'.format(name, choice(moods)))
    dialog.run()
    dialog.destroy()


def on_app_clicked(_, app):
    """Install the app, or remove it if it is installed."""
    img, button, name = shown_apps[app]
    remove = packages.is_installed(app, packages.installed_packages())
    cmd = packages.command(app, remove)
    window = button.get_toplevel()
    window.set_sensitive(False)  # one package manager run at a time

    def done(result):
        window.set_sensitive(True)
        if result.returncode:
            error = Gtk.MessageDialog(transient_for=window, message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.OK, text='{} failed'.format(' '.join(cmd)))
            error.format_secondary_text(result.stderr.strip()[-2000:])
            error.run()
            error.destroy()
        else:
            show_state(img, button, name, not remove)
            show_success(name, remove)

    # run in a thread so the window keeps redrawing during long installs
    threading.Thread(target=lambda: GLib.idle_add(done, subprocess.run(cmd,
        stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
        text=True, errors='replace', env=packages.ENV)), daemon=True).start()
