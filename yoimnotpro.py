#!/usr/bin/env python3
import os
import sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ui/, translations/ etc. are relative paths
from appcenter.ui import Builder, SetMenuCategoriesTooltipNames
from appcenter.start_screen import InitConnectMeSignals
import appcenter.categories as somesome
from appcenter import packages as pkg
from appcenter.i18n import action, OpenCFGnSetLang, ChangeLang
import cairo
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk

class iod(object):

    def on_category_clicked(self, widget):
        grid = self.grid_of_button[widget]
        self.cur_menu_dict[grid].load()
        self.vbox.remove(self.current_category)
        self.current_category = grid
        self.vbox.add(grid)

    def on_button7_clicked(self, widget):
        aboutdialog = Gtk.AboutDialog()
        aboutdialog.set_program_name(action.program_name)
        aboutdialog.set_version("1.8")
        aboutdialog.set_logo(GdkPixbuf.Pixbuf.new_from_file("ui/yoimnotpro_icon.png"))
        aboutdialog.set_comments(action.program_description)
        aboutdialog.set_website("http://linux.sytes.net/")
        aboutdialog.set_website_label(action.dev_website)
        aboutdialog.set_authors(["Aaron Caffrey\nhttp://linux.sytes.net/",\
         "\n{Suggestions}:\nexcalibur1234\nKorrode\ntetrahderon\nAyceman\nAJ1000".format(Suggestions=action.suggestions), \
         "\n{Comments}:\nRichad\ndrumBE\nVerandert2.0\nLukimya\naaditya\nHardyH\ndcell\nrfkill 2.0".format(Comments=action.comments)])
        aboutdialog.set_copyright('{License}: GPLv3 - http://www.gnu.org/licenses/gpl.html'.format(License=action.license))
        aboutdialog.run()
        aboutdialog.destroy()

    def on_button8_clicked(self, widget):
        ChangeLang()
        self.cur_menu_dict[self.current_category].load()

    def draw_transparency(self, widget, cr):
        cr.set_source_rgba(.1, .1, .1, 0.8)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)

    def __init__(self):
        Builder.builder.connect_signals(self)

        self.current_category = Builder.grid_custom
        self.cur_menu_dict = {Builder.grid_development: somesome.menu1,
        Builder.grid_graphics: somesome.menu2,
        Builder.grid_internet: somesome.menu3,
        Builder.grid_multimedia: somesome.menu4,Builder.grid_system: 
        somesome.menu5,Builder.grid_utilities: somesome.menu6,
        Builder.grid_custom: somesome.menu7}
        self.grid_of_button = {Builder.button1: Builder.grid_development,
        Builder.button2: Builder.grid_graphics,
        Builder.button3: Builder.grid_internet,
        Builder.button4: Builder.grid_multimedia,
        Builder.button5: Builder.grid_system,
        Builder.button6: Builder.grid_utilities}

        self.window = Builder.builder.get_object("window1")

        # it's horizontal box, separating the menu buttons from the ui files
        self.vbox = Builder.builder.get_object("box1")
        self.vbox.add(Builder.grid_custom)

        # transparancy
        self.window.screen = self.window.get_screen()
        self.window.visual = self.window.screen.get_rgba_visual()
        if self.window.visual is not None and self.window.screen.is_composited():
            self.window.set_visual(self.window.visual)
        self.window.set_app_paintable(True)
        self.window.connect("draw", self.draw_transparency)

        # css
        self.screen = Gdk.Screen.get_default()
        self.css_provider = Gtk.CssProvider()
        self.css_provider.load_from_path('ui/style.css')
        self.priority = Gtk.STYLE_PROVIDER_PRIORITY_USER
        self.context = Gtk.StyleContext()
        self.context.add_provider_for_screen(self.screen, self.css_provider, self.priority)

        OpenCFGnSetLang()
        InitConnectMeSignals()
        somesome.menu7.load()
        SetMenuCategoriesTooltipNames()

        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show_all()

if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('yoimnotpro installs packages, so run it as root, e.g. with sudo -E or doas')
    if pkg.SYSTEM is None:
        sys.exit('yoimnotpro supports Arch Linux (pacman), Debian (apt) and OpenBSD (pkg_add).')
    iod()
    Gtk.main()
