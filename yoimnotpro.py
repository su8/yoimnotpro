#!/usr/bin/env python3
import os
import sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ui/, translations/ etc. are relative paths
from appcenter.i18n import LanguagePicker, load_language, text
from appcenter import categories, packages, ui
from appcenter.start_screen import StartScreen
import cairo
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk

class AppCenter(object):

    def show(self, view):
        view.load()
        self.content.remove(self.current.grid)
        self.current = view
        self.content.add(view.grid)

    def on_category_clicked(self, button):
        self.show(self.category_of_button[button])

    def on_about_clicked(self, button):
        aboutdialog = Gtk.AboutDialog()
        aboutdialog.set_program_name(text.program_name)
        aboutdialog.set_version("1.8")
        aboutdialog.set_logo(GdkPixbuf.Pixbuf.new_from_file("ui/yoimnotpro_icon.png"))
        aboutdialog.set_comments(text.program_description)
        aboutdialog.set_website("http://linux.sytes.net/")
        aboutdialog.set_website_label(text.dev_website)
        aboutdialog.set_authors(["Aaron Caffrey\nhttp://linux.sytes.net/",\
         "\n{Suggestions}:\nexcalibur1234\nKorrode\ntetrahderon\nAyceman\nAJ1000".format(Suggestions=text.suggestions), \
         "\n{Comments}:\nRichad\ndrumBE\nVerandert2.0\nLukimya\naaditya\nHardyH\ndcell\nrfkill 2.0".format(Comments=text.comments)])
        aboutdialog.set_copyright('{License}: GPLv3 - http://www.gnu.org/licenses/gpl.html'.format(License=text.license))
        aboutdialog.run()
        aboutdialog.destroy()

    def on_language_clicked(self, button):
        LanguagePicker(on_change=ui.set_category_tooltips)
        self.current.load()

    def draw_transparency(self, widget, cr):
        cr.set_source_rgba(.1, .1, .1, 0.8)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)

    def __init__(self):
        ui.main.connect_signals(self)
        self.category_of_button = {ui.main.get_object(c.name + '_button'): c for c in categories.ALL}
        self.current = StartScreen()
        self.window = ui.main.get_object("main_window")

        # holds the sidebar and, next to it, the grid of the shown category
        self.content = ui.main.get_object("content_box")
        self.content.add(self.current.grid)

        # transparency
        screen = self.window.get_screen()
        visual = screen.get_rgba_visual()
        if visual is not None and screen.is_composited():
            self.window.set_visual(visual)
        self.window.set_app_paintable(True)
        self.window.connect("draw", self.draw_transparency)

        css = Gtk.CssProvider()
        css.load_from_path('ui/style.css')
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), css, Gtk.STYLE_PROVIDER_PRIORITY_USER)

        load_language()
        self.current.load()
        ui.set_category_tooltips()

        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show_all()

if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('yoimnotpro installs packages, so run it as root, e.g. with sudo -E or doas')
    if packages.SYSTEM is None:
        sys.exit('yoimnotpro supports Arch Linux (pacman), Debian (apt) and OpenBSD (pkg_add).')
    AppCenter()
    Gtk.main()
