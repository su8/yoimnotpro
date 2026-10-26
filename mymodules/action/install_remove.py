import subprocess
import threading
from mymodules.action import pkg
from mymodules.action.dial import SetToolTip, action, dial
from gi.repository import GLib, Gtk


def show_state(img, button, name, installed):
    img.set_from_file(action.gtk_yes if installed else action.gtk_no)
    button.set_tooltip_markup(format(SetToolTip(name, action.installed, action.remove_it)
        if installed else SetToolTip(name, action.not_here, action.install_it)))


class StartKickingSomeNinjas(object):

    def __init__(self, _, app):
        img, button, name = action.dicti[app]
        remove = pkg.is_installed(app, pkg.installed_packages())
        cmd = pkg.command(app, remove)
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
                dial(name, action.remove_it if remove else action.installed)

        # run in a thread so the window keeps redrawing during long installs
        threading.Thread(target=lambda: GLib.idle_add(done, subprocess.run(cmd,
            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
            text=True, errors='replace', env=pkg.ENV)), daemon=True).start()
