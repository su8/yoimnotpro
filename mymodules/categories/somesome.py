from copy import deepcopy
from mymodules.buttons_images import Img
from mymodules.builder import Builder
from mymodules.action import pkg
from mymodules.action.install_remove import StartKickingSomeNinjas, show_state
from mymodules.action.dial import action
from mymodules.categories.menu7_button import APPS

class Menu6(object):
    pass
class Menu5(object):
    pass
class Menu2(object):
    pass
class Menu4(object):
    pass
class Menu3(object):
    pass
class Menu1(object):
    pass
class Inherit(object):
    def set_grey_menu_icons(self, given_img):
        img_list = [(action.menu_img_1, Img.image1),
        (action.menu_img_2, Img.image2),
        (action.menu_img_3, Img.image3),
        (action.menu_img_4, Img.image4),
        (action.menu_img_5, Img.image5),
        (action.menu_img_6, Img.image6)]
        for x in img_list:
            if not x[1] == given_img:
                x[1].set_from_file(x[0])
    def set_attr_on_the_fly(self, *arg):
        local_dict = self.dicti
        self.deep_copy = deepcopy(local_dict)
        for key, value in local_dict.items():                      # args: [0] Menu{Number}, [1] Builder.builder{Number}
            key2 = (key if not len(value) > 2 else value[1])       # [2] menu{Number}, [3] Img.current_menu_category_img
            skyp_or_not = (key2 if not key2 == 'skype' else 'skyp')
            setattr(arg[0], skyp_or_not,
             arg[1].get_object(skyp_or_not))                       # install_remove_button
            setattr(Img, '{}_img'.format(key2),
                arg[1].get_object('{}_img'.format(key2)))          # install_remove_button image
            setattr(arg[0], '{}_icon_tooltip'.format(key2),
                arg[1].get_object('{}_icon_tooltip'.format(key2))) # faenza icon

            # Img.program_name, Menu.program_name, program_name.capitalize()
            self.deep_copy[key] = (getattr(Img, '{}_img'.format(key2)),
                getattr(arg[0], skyp_or_not), value[0])
            getattr(arg[0], '{}_icon_tooltip'.format(key2)).set_tooltip_text(
                value[-1])                                         # faenza icon tooltip text

        if not getattr(arg[2], 'first_run'):
            for key, value in local_dict.items():
                key2 = (key if not len(value) > 2 else value[1])
                skyp_or_not = (key2 if not key2 == 'skype' else 'skyp')
                getattr(arg[0], skyp_or_not).connect('clicked', StartKickingSomeNinjas, key)
            setattr(arg[2], 'first_run', 'not first run')

        setattr(action, 'dicti', self.deep_copy)
        self.init_set_file_n_tooltip()
        self.set_grey_menu_icons(arg[3])

    def init_set_file_n_tooltip(self):
        installed = pkg.installed_packages()
        for app, (img, button, name) in (self.deep_copy or self.dicti).items():
            available = pkg.package(app) is not None
            button.set_sensitive(available)
            if available:
                show_state(img, button, name, pkg.is_installed(app, installed))
            else:
                img.set_from_file(action.gtk_no)
                button.set_tooltip_markup(action.not_available.format(
                    name=name, distro=pkg.NAMES[pkg.SYSTEM]))
    def __init__(self, dicti):
        self.dicti = dicti
        self.deep_copy = dict()

class menu7(Inherit):
    @staticmethod
    def load():
        get = Builder.builder8.get_object
        men7 = menu7({key: (get(prefix + '_img_'), get(prefix + '_'), name)
            for key, (prefix, name, _) in APPS.items()})
        men7.init_set_file_n_tooltip()
        setattr(action, 'dicti', men7.dicti)

class menu6(Inherit):
    first_run = str()
    @staticmethod
    def load():
        Img.image6.set_from_file(action.menu_img_66)
        local_dict = {
        "docky": ("Docky", "Docky is an advanced shortcut bar that sits at the edges of your screen."),
        "emacs": ("Emacs", "Emacs is a text editor."),
        "vim": ("Vim", "Vim is a text editor"),
        "galculator": ("Galculator", "Galculator is an open source scientific calculator with a modern GUI."),
        "gedit": ("Gedit", "Gedit is lightweight text editor."),
        "gloobus-preview": ("Gloobus", 'gloobus', "Gloobus Preview is a program designed to preview the contents of a file or folder on Linux OS"),
        "leafpad": ("Leafpad", "Leafpad is a text editor"),
        "scribes": ("Scribes", "Simple, slim and sleek, yet powerful text editor."),
        "tomboy": ("Tomboy", "Tomboy is a desktop note-taking application"),
        "tuxcards": ("Tuxcards", "TuxCards is a hierarical notebook."),
        "imagewriter": ("Imagewriter", "This tool is used for writing images to USB sticks."),
        "p7zip": ("7zip", 'sevenzip', "7-Zip is an open source file archiver")}
        men6 = menu6(local_dict)
        men6.set_attr_on_the_fly(Menu6, Builder.builder7, menu6, Img.image6)

class menu5(Inherit):
    first_run = str()
    @staticmethod
    def load():
        Img.image5.set_from_file(action.menu_img_55)
        local_dict = {
        "gparted": ('Gparted', "GParted is a free partition editor for graphically managing your disk partitions. "),
        "guake": ('Guake', "Guake is a drop-down terminal."),
        "hardinfo": ('Hardinfo', "Hardinfo provides comprehensive details of your PC's software and hardware and allows you to benchmark its performance."),
        "htop": ('Htop', "Htop is an interactive process viewer."),
        "keepassx": ('KeepassX', "KeePassX is an application for people with extremly high demands on secure personal data management."),
        "playonlinux": ('PlayOnLinux', "PlayOnLinux will allow you to play your favorite games on Linux easily."),
        "terminator": ('Terminator', "Terminator is a cross-platform GPL terminal emulator with advanced features not yet found elsewhere."),
        "thunar": ('Thunar', "Thunar is a file manager."),
        "truecrypt": ('Truecrypt', "TrueCrypt is free open-source disk encryption software."),
        "unetbootin": ('Unetbootin', "UNetbootin allows you to create bootable Live USB drives for GNU/Linux distributions without burning a CD"),
        "virtualbox": ('Virtualbox', "VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.\nThe program is similar to Virtual PC."),
        "wine": ('Wine', "Wine is a compatibility layer for running windows applications on GNU/Linux."),
        "wireshark-gtk": ('Wireshark', 'wireshark', "Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis,\nsoftware and communications protocol development."),
        "xbmc": ('XBMC', "XBMC Media Center is a free cross-platform media player software and entertainment system application framework."),
        "gufw": ('Gufw', "One of the easiest firewalls in the world!"),
        "octopi": ('Octopi', "Octopi is a powerful tool to manage (Arch | Manjaro) Linux packages."),
        "pamac": ('Pamac', "Pamac - simple graphical package manager for Manjaro Linux."),
        "gnome-system-monitor": ('Gnome System Monitor', 'gnome_system_monitor', "Gnome System Monitor is a GNOME process viewer and system monitor with a nice easy-to-use interface")}
        men5 = menu5(local_dict)
        men5.set_attr_on_the_fly(Menu5, Builder.builder6, menu5, Img.image5)

class menu4(Inherit):
    first_run = str()
    @staticmethod
    def load():
        Img.image4.set_from_file(action.menu_img_44)
        local_dict = {
        "amarok": ('Amarok', "Amarok is a cross-platform free and open source music player."),
        "audacious": ('Audacious', 'Audacious is a free and open source audio player.'),
        "banshee": ('Banshee', 'Banshee is a cross-platform open-source media player.'),
        "cheese": ('Cheese', 'Cheese uses your webcam to take photos and videos, applies fancy special effects, and lets you share the fun with others.'),
        "clementine": ('Clementine', 'Clementine is a cross-platform free and open source music player and library organizer.'),
        "flashplugin": ('Adobe Flashplayer', 'flashplayer', 'Cross-platform plugin plays animations, videos and sound files.'),
        "gtk-recordmydesktop": ('RecordMyDesktop', 'recordmydesktop', 'RecordMyDesktop is a desktop session recorder.'),
        "guayadeque": ('Guayadeque', 'Guayadeque is a music management program designed for all music enthusiasts.'),
        "mplayer": ('Mplayer', 'Mplayer is a free software and open source media player.'),
        "openshot": ('Openshot', 'A simple, powerful, and free open-source video editor for Linux with a focus on usability, flexibility, and style.'),
        "pitivi": ('PiTiVi', 'Pitivi is an open source, non-linear video editor.'),
        "rhythmbox": ('Rhythmbox', 'Rhythmbox is an integrated music management application, originally inspired by Apple\'s iTunes.'),
        "soundconverter": ('SoundConverter', 'SoundConverter is the leading audio file converter.'),
        "totem": ('Totem', 'Totem is a media player.'),
        "vlc": ('VLC', 'VLC is a multimedia player for various audio and video formats.'),
        "winff": ('Winff', 'WinFF is a video converter.'),
        "xfburn": ('Xfburn', 'Xfburn is a simple CD/DVD burning tool.'),
        "kdenlive": ('Kdenlive', 'Kdenlive (KDE Non-Linear Video Editor) is an open source video editing software'),
        "simplescreenrecorder": ('Simple Screen Recorder', 'SimpleScreenRecorder is capable of recording video from full-screen and window-size captures of Opengl applications(and games).'),
        "vokoscreen": ('Vokoscreen', 'Vokoscreen is an easy to use screencast creator to record educational videos, live recordings of browser, installation, videoconferences, etc.')}
        men4 = menu4(local_dict)
        men4.set_attr_on_the_fly(Menu4, Builder.builder5, menu4, Img.image4)

class menu3(Inherit):
    first_run = str()
    @staticmethod
    def load():
        Img.image3.set_from_file(action.menu_img_33)
        local_dict = {
        "chromium": ('Chromium', "Chromium is the open source web browser project from which Google Chrome draws its source code."),
        "deluge": ('Deluge', "Open source, cross-platform BitTorrent client."),
        "evolution": ('Evolution', "Evolution is a fully featured open source powerful, flexible and generally great email client."),
        "filezilla": ('Filezilla', "Open-source FTP client."),
        "firefox": ('Firefox', "Firefox is a free and open-source web browser"),
        "google-chrome": ('Google Chrome', 'chrome', "Google Chrome is a browser that combines a minimal design with sophisticated technology to make the web faster, safer and easier."),
        "xchat": ('Xchat', "XChat is a popular Internet Relay Chat (IRC) client."),
        "liferea": ('Liferea', "Liferea is an abbreviation for Linux Feed Reader, a news aggregator for online news feeds."),
        "midori": ('Midori', "Midori is a lightweight Webkit-based web browser."),
        "minitube": ('MiniTube', "Minitube is a native YouTube client. With it you can watch YouTube videos in a new way."),
        "opera": ('Opera', "Opera is a web browser."),
        "pidgin": ('Pidgin', "Pidgin is universal chat client."),
        "skype": ('Skype', "Skype is a freemium voice-over-IP service and instant messaging client."),
        "steam": ('Steam', "Steam is a digital distribution, digital rights management, multiplayer, and communications platform developed by\nValve Corporation. It is used to distribute games and related media online, from small independent developers to larger software houses."),
        "thunderbird": ('ThunderBird', "Thunderbird is an email program."),
        "transmission-gtk": ('Transmission', 'transmission', "Transmission is a BitTorrent client."),
        "linuxdcpp": ('Linuxdcpp', "A port of DC++ to GNU/Linux")}
        men3 = menu3(local_dict)
        men3.set_attr_on_the_fly(Menu3, Builder.builder4, menu3, Img.image3)
        
class menu2(Inherit):
    first_run = str()
    @staticmethod
    def load():
        Img.image2.set_from_file(action.menu_img_22)
        local_dict = {
        "evince": ('Evince', "Evince is a document viewer for multiple document formats."),
        "f-spot": ('F-spot', "f_spot", "F-Spot is a full-featured personal photo management application."),
        "gimp": ('GIMP', "GIMP is an image retouching and editing tool, similar to Photoshop."),
        "gwenview": ('Gwenview', "Gwenview is an image viewer."),
        "inkscape": ('Inkscape', "Inkscape is an open source vector graphics editor."),
        "mypaint": ('MyPaint', "MyPaint is a fast and easy open-source graphics application for digital painters."),
        "pinta": ('Pinta', "Pinta is an open-source, cross-platform bitmap image drawing and editing program inspired by Paint.NET"),
        "shotwell": ('Shotwell', "Shotwell is an image organizer."),
        "stellarium": ('Stellarium', "Stellarium is a planetarium software that shows exactly what you see when you look up at the stars."),
        "imagemagick": ("ImageMagick", "Use ImageMagick to convert, edit, or compose bitmap images in a variety of formats.")}
        men2 = menu2(local_dict)
        men2.set_attr_on_the_fly(Menu2, Builder.builder3, menu2, Img.image2)

class menu1(Inherit):
    first_run = str()
    @staticmethod
    def load():
        Img.image1.set_from_file(action.menu_img_11)
        local_dict = {
        "anjuta": ('Anjuta', "Anjuta is an integrated development environment."),
        "blender": ("Blender", "Blender is a free and open-source 3D computer graphics software product used for creating animated films, \nvisual effects, art, 3D printed models and so on."),
        "bluefish": ('Bluefish', "Bluefish is a free and open source advanced text editor with a variety of tools for programming in general\nand the development of dynamic websites"),
        "eclipse": ('Eclipse', "Eclipse is IDE."),
        "geany": ("Geany", "Geany is a small and lightweight integrated development environment."),
        "glade": ('Glade', "Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment."),
        "meld": ('Meld', "Meld is a visual diff and merge tool targeted at developers."),
        "netbeans": ('NetBeans', "Fully-featured Java IDE written completely in Java, with many modules available."),
        "qt4": ('Qt4', "Qt4 is a cross-platform application framework that is widely used\nfor developing application software with a graphical user interface."),
        "qt5-base": ('Qt5', 'qt5', "Qt5 is a cross-platform application framework that is widely used\nfor developing application software with a graphical user interface."),
        "qtcreator": ('QtCreator', "Qt Creator is a cross-platform C++ IDE"),
        "ninja-ide": ('Ninja-IDE', 'ninja_ide', "Ninja-IDE is a cross-platform integrated development environment designed to build Python applications."),
        "openjdk": ("OpenJDK", "OpenJDK (Open Java Development Kit) is a free and open source implementation of the Java Platform, Standard Edition (Java SE).")}
        men1 = menu1(local_dict)
        men1.set_attr_on_the_fly(Menu1, Builder.builder2, menu1, Img.image1)