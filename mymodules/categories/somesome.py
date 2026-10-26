import os
from copy import deepcopy
from mymodules.buttons_images import Img
from mymodules.builder import Builder
from mymodules.action.install_remove import StartKickingSomeNinjas
from mymodules.action.dial import SetToolTip, action
from mymodules.categories.menu7_button import Menu7

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
            key2 = (key if not len(value) > 3 else value[2])       # [2] menu{Number}, [3] Img.current_menu_category_img
            skyp_or_not = (key2 if not key2 == 'skype' else 'skyp')
            setattr(arg[0], skyp_or_not,
             arg[1].get_object(skyp_or_not))                       # install_remove_button
            setattr(Img, '{}_img'.format(key2),
                arg[1].get_object('{}_img'.format(key2)))          # install_remove_button image
            setattr(arg[0], '{}_icon_tooltip'.format(key2),
                arg[1].get_object('{}_icon_tooltip'.format(key2))) # faenza icon

            #exe_file or path, Img.program_name, Menu.program_name, program_name.capitalize()
            self.deep_copy[key] = (value[0], getattr(Img, '{}_img'.format(key2)), 
                getattr(arg[0], skyp_or_not), value[1])
            getattr(arg[0], '{}_icon_tooltip'.format(key2)).set_tooltip_text(
            (value[2] if not len(value) > 3 else value[3]))        # faenza icon tooltip text

        if not getattr(arg[2], 'first_run'):
            for key, value in local_dict.items():
                key2 = (key if not len(value) > 3 else value[2])
                skyp_or_not = (key2 if not key2 == 'skype' else 'skyp')
                getattr(arg[0], skyp_or_not).connect('clicked', StartKickingSomeNinjas, key)
            setattr(arg[2], 'first_run', 'not first run')

        setattr(action, 'dicti', self.deep_copy)
        self.init_set_file_n_tooltip()
        self.set_grey_menu_icons(arg[3])

    def init_set_file_n_tooltip(self):
        cur_dict = (self.deep_copy if self.deep_copy else self.dicti)
        for val in cur_dict.values():
            if (os.path.isfile(val[0]) if not val[0]
                == "/usr/share/licenses/jre7-openjdk/" else
                os.path.exists(val[0])):
                val[1].set_from_file(action.gtk_yes)
                val[2].set_tooltip_markup(format(SetToolTip(val[3],
                    action.installed, action.remove_it)))
            else:
                val[1].set_from_file(action.gtk_no)
                val[2].set_tooltip_markup(format(SetToolTip(val[3],
                    action.not_here, action.install_it)))
    def __init__(self, dicti):
        self.dicti = dicti
        self.deep_copy = dict()

class menu7(Inherit):
    pass
    @staticmethod
    def load():
        men7 = menu7({
        "gedit": ("/usr/bin/gedit", Img.gedit__img, Menu7.gedit_, "Gedit"),
        "blender": ("/usr/bin/blender", Img.blender__img, Menu7.blender_, "Blender"),
        "geany": ("/usr/bin/geany", Img.geany__img, Menu7.geany_, "Geany"),
        "glade": ("/usr/bin/glade", Img.glade__img, Menu7.glade_, 'Glade'),
        "ninja-ide": ("/usr/bin/ninja-ide", Img.ninja_ide__img, Menu7.ninja_ide_, 'Ninja-IDE'),
        "evince": ("/usr/bin/evince", Img.evince__img, Menu7.evince_, 'Evince'),
        "gimp": ("/usr/bin/gimp", Img.gimp__img, Menu7.gimp_, 'GIMP'),
        "chromium": ("/usr/bin/chromium", Img.chromium__img, Menu7.chromium_, 'Chromium'),
        "deluge": ("/usr/bin/deluge", Img.deluge__img, Menu7.deluge_, 'Deluge'),
        "xchat": ("/usr/bin/xchat", Img.xchat__img, Menu7.xchat_, 'Xchat'),
        "liferea": ("/usr/bin/liferea", Img.liferea__img, Menu7.liferea_, 'Liferea'),
        "skype": ("/usr/bin/skype", Img.skype__img, Menu7.skype_, 'Skype'),
        "steam": ("/usr/bin/steam", Img.steam__img, Menu7.steam_, 'Steam'),
        "audacious": ("/usr/bin/audacious", Img.audacious__img, Menu7.audacious_, 'Audacious'),
        "openshot": ("/usr/bin/openshot", Img.openshot__img, Menu7.openshot_, 'Openshot'),
        "flashplugin": ("/usr/bin/flash-player-properties", Img.flashplayer__img,
            Menu7.flashplayer_, 'Adobe Flashplayer'),
        "xfburn": ("/usr/bin/xfburn", Img.xfburn__img, Menu7.xfburn_, 'Xfburn'),
        "htop": ("/usr/bin/htop", Img.htop__img, Menu7.htop_, 'Htop'),
        "virtualbox": ("/usr/bin/virtualbox", Img.virtualbox__img, Menu7.virtualbox_, 'Virtualbox'),
        "wireshark-gtk": ("/usr/bin/wireshark", Img.wireshark__img, Menu7.wireshark_, 'Wireshark')})
        attr = getattr(men7, 'dicti')
        men7.init_set_file_n_tooltip()
        setattr(action, 'dicti', attr)

class menu6(Inherit):
    first_run = str()
    @staticmethod
    def load():
        Img.image6.set_from_file(action.menu_img_66)
        local_dict = {
        "docky": ("/usr/bin/docky", "Docky", "Docky is an advanced shortcut bar that sits at the edges of your screen."),
        "emacs": ("/usr/bin/emacs", "Emacs", "Emacs is a text editor."),
        "vim": ("/usr/bin/vim", "Vim", "Vim is a text editor"),
        "galculator": ("/usr/bin/galculator", "Galculator", "Galculator is an open source scientific calculator with a modern GUI."),
        "gedit": ("/usr/bin/gedit", "Gedit", "Gedit is lightweight text editor."),
        "gloobus-preview": ("/usr/bin/gloobus-preview", "Gloobus", 'gloobus', "Gloobus Preview is a program designed to preview the contents of a file or folder on Linux OS"),
        "leafpad": ("/usr/bin/leafpad", "Leafpad", "Leafpad is a text editor"),
        "scribes": ("/usr/bin/scribes", "Scribes", "Simple, slim and sleek, yet powerful text editor."),
        "tomboy": ("/usr/bin/tomboy", "Tomboy", "Tomboy is a desktop note-taking application"),
        "tuxcards": ("/usr/bin/tuxcards", "Tuxcards", "TuxCards is a hierarical notebook."),
        "imagewriter": ("/usr/bin/imagewriter", "Imagewriter", "This tool is used for writing images to USB sticks."),
        "p7zip": ("/usr/bin/7zFM", "7zip", 'sevenzip', "7-Zip is an open source file archiver")}
        men6 = menu6(local_dict)
        men6.set_attr_on_the_fly(Menu6, Builder.builder7, menu6, Img.image6)

class menu5(Inherit):
    first_run = str()
    @staticmethod
    def load():
        Img.image5.set_from_file(action.menu_img_55)
        local_dict = {
        "gparted": ("/usr/bin/gparted", 'Gparted', "GParted is a free partition editor for graphically managing your disk partitions. "),
        "guake": ("/usr/bin/guake", 'Guake', "Guake is a drop-down terminal."),
        "hardinfo": ("/usr/bin/hardinfo", 'Hardinfo', "Hardinfo provides comprehensive details of your PC's software and hardware and allows you to benchmark its performance."),
        "htop": ("/usr/bin/htop", 'Htop', "Htop is an interactive process viewer."),
        "keepassx": ("/usr/bin/keepassx", 'KeepassX', "KeePassX is an application for people with extremly high demands on secure personal data management."),
        "playonlinux": ("/usr/bin/playonlinux", 'PlayOnLinux', "PlayOnLinux will allow you to play your favorite games on Linux easily."),
        "terminator": ("/usr/bin/terminator", 'Terminator', "Terminator is a cross-platform GPL terminal emulator with advanced features not yet found elsewhere."),
        "thunar": ("/usr/bin/thunar", 'Thunar', "Thunar is a file manager."),
        "truecrypt": ("/usr/bin/truecrypt", 'Truecrypt', "TrueCrypt is free open-source disk encryption software."),
        "unetbootin": ("/usr/bin/unetbootin", 'Unetbootin', "UNetbootin allows you to create bootable Live USB drives for GNU/Linux distributions without burning a CD"),
        "virtualbox": ("/usr/bin/virtualbox", 'Virtualbox', "VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.\nThe program is similar to Virtual PC."),
        "wine": ("/usr/bin/wine", 'Wine', "Wine is a compatibility layer for running windows applications on GNU/Linux."),
        "wireshark-gtk": ("/usr/bin/wireshark", 'Wireshark', 'wireshark', "Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis,\nsoftware and communications protocol development."),
        "xbmc": ("/usr/bin/xbmc", 'XBMC', "XBMC Media Center is a free cross-platform media player software and entertainment system application framework."),
        "gufw": ("/usr/bin/gufw", 'Gufw', "One of the easiest firewalls in the world!"),
        "octopi": ("/usr/bin/octopi", 'Octopi', "Octopi is a powerful tool to manage (Arch | Manjaro) Linux packages."),
        "pamac": ("/usr/bin/pamac-manager", 'Pamac', "Pamac - simple graphical package manager for Manjaro Linux."),
        "gnome-system-monitor": ("/usr/bin/gnome-system-monitor", 
            'Gnome System Monitor', 'gnome_system_monitor', "Gnome System Monitor is a GNOME process viewer and system monitor with a nice easy-to-use interface")}
        men5 = menu5(local_dict)
        men5.set_attr_on_the_fly(Menu5, Builder.builder6, menu5, Img.image5)

class menu4(Inherit):
    first_run = str()
    @staticmethod
    def load():
        Img.image4.set_from_file(action.menu_img_44)
        local_dict = {
        "amarok": ("/usr/bin/amarok", 'Amarok', "Amarok is a cross-platform free and open source music player."),
        "audacious": ("/usr/bin/audacious", 'Audacious', 'Audacious is a free and open source audio player.'),
        "banshee": ("/usr/bin/banshee", 'Banshee', 'Banshee is a cross-platform open-source media player.'),
        "cheese": ("/usr/bin/cheese", 'Cheese', 'Cheese uses your webcam to take photos and videos, applies fancy special effects, and lets you share the fun with others.'),
        "clementine": ("/usr/bin/clementine", 'Clementine', 'Clementine is a cross-platform free and open source music player and library organizer.'),
        "flashplugin": ("/usr/bin/flash-player-properties", 'Adobe Flashplayer', 'flashplayer', 'Cross-platform plugin plays animations, videos and sound files.'),
        "gtk-recordmydesktop": ("/usr/bin/gtk-recordMyDesktop", 'RecordMyDesktop', 'recordmydesktop', 'RecordMyDesktop is a desktop session recorder.'),
        "guayadeque": ("/usr/bin/guayadeque", 'Guayadeque', 'Guayadeque is a music management program designed for all music enthusiasts.'),
        "mplayer": ("/usr/bin/mplayer", 'Mplayer', 'Mplayer is a free software and open source media player.'),
        "openshot": ("/usr/bin/openshot", 'Openshot', 'A simple, powerful, and free open-source video editor for Linux with a focus on usability, flexibility, and style.'),
        "pitivi": ("/usr/bin/pitivi", 'PiTiVi', 'Pitivi is an open source, non-linear video editor.'),
        "rhythmbox": ("/usr/bin/rhythmbox", 'Rhythmbox', 'Rhythmbox is an integrated music management application, originally inspired by Apple\'s iTunes.'),
        "soundconverter": ("/usr/bin/soundconverter", 'SoundConverter', 'SoundConverter is the leading audio file converter.'),
        "totem": ("/usr/bin/totem", 'Totem', 'Totem is a media player.'),
        "vlc": ("/usr/bin/vlc", 'VLC', 'VLC is a multimedia player for various audio and video formats.'),
        "winff": ("/usr/bin/winff", 'Winff', 'WinFF is a video converter.'),
        "xfburn": ("/usr/bin/xfburn", 'Xfburn', 'Xfburn is a simple CD/DVD burning tool.'),
        "kdenlive": ("/usr/bin/kdenlive", 'Kdenlive', 'Kdenlive (KDE Non-Linear Video Editor) is an open source video editing software'),
        "simplescreenrecorder": ("/usr/bin/simplescreenrecorder", 'Simple Screen Recorder', 'SimpleScreenRecorder is capable of recording video from full-screen and window-size captures of Opengl applications(and games).'),
        "vokoscreen": ("/usr/bin/vokoscreen", 'Vokoscreen', 'Vokoscreen is an easy to use screencast creator to record educational videos, live recordings of browser, installation, videoconferences, etc.')}
        men4 = menu4(local_dict)
        men4.set_attr_on_the_fly(Menu4, Builder.builder5, menu4, Img.image4)

class menu3(Inherit):
    first_run = str()
    @staticmethod
    def load():
        Img.image3.set_from_file(action.menu_img_33)
        local_dict = {
        "chromium": ("/usr/bin/chromium", 'Chromium', "Chromium is the open source web browser project from which Google Chrome draws its source code."),
        "deluge": ("/usr/bin/deluge", 'Deluge', "Open source, cross-platform BitTorrent client."),
        "evolution": ("/usr/bin/evolution", 'Evolution', "Evolution is a fully featured open source powerful, flexible and generally great email client."),
        "filezilla": ("/usr/bin/filezilla", 'Filezilla', "Open-source FTP client."),
        "firefox": ("/usr/bin/firefox", 'Firefox', "Firefox is a free and open-source web browser"),
        "google-chrome": ("/usr/bin/google-chrome-stable", 'Google Chrome', 'chrome', "Google Chrome is a browser that combines a minimal design with sophisticated technology to make the web faster, safer and easier."),
        "xchat": ("/usr/bin/xchat", 'Xchat', "XChat is a popular Internet Relay Chat (IRC) client."),
        "liferea": ("/usr/bin/liferea", 'Liferea', "Liferea is an abbreviation for Linux Feed Reader, a news aggregator for online news feeds."),
        "midori": ("/usr/bin/midori", 'Midori', "Midori is a lightweight Webkit-based web browser."),
        "minitube": ("/usr/bin/minitube", 'MiniTube', "Minitube is a native YouTube client. With it you can watch YouTube videos in a new way."),
        "opera": ("/usr/bin/opera", 'Opera', "Opera is a web browser."),
        "pidgin": ("/usr/bin/pidgin", 'Pidgin', "Pidgin is universal chat client."),
        "skype": ("/usr/bin/skype", 'Skype', "Skype is a freemium voice-over-IP service and instant messaging client."),
        "steam": ("/usr/bin/steam", 'Steam', "Steam is a digital distribution, digital rights management, multiplayer, and communications platform developed by\nValve Corporation. It is used to distribute games and related media online, from small independent developers to larger software houses."),
        "thunderbird": ("/usr/bin/thunderbird", 'ThunderBird', "Thunderbird is an email program."),
        "transmission-gtk": ("/usr/bin/transmission-gtk", 'Transmission', 'transmission', "Transmission is a BitTorrent client."),
        "linuxdcpp": ("/usr/bin/linuxdcpp", 'Linuxdcpp', "A port of DC++ to GNU/Linux")}
        men3 = menu3(local_dict)
        men3.set_attr_on_the_fly(Menu3, Builder.builder4, menu3, Img.image3)
        
class menu2(Inherit):
    first_run = str()
    @staticmethod
    def load():
        Img.image2.set_from_file(action.menu_img_22)
        local_dict = {
        "evince": ("/usr/bin/evince", 'Evince', "Evince is a document viewer for multiple document formats."),
        "f-spot": ("/usr/bin/f-spot", 'F-spot', "f_spot", "F-Spot is a full-featured personal photo management application."),
        "gimp": ("/usr/bin/gimp", 'GIMP', "GIMP is an image retouching and editing tool, similar to Photoshop."),
        "gwenview": ("/usr/bin/gwenview", 'Gwenview', "Gwenview is an image viewer."),
        "inkscape": ("/usr/bin/inkscape", 'Inkscape', "Inkscape is an open source vector graphics editor."),
        "mypaint": ("/usr/bin/mypaint", 'MyPaint', "MyPaint is a fast and easy open-source graphics application for digital painters."),
        "pinta": ("/usr/bin/pinta", 'Pinta', "Pinta is an open-source, cross-platform bitmap image drawing and editing program inspired by Paint.NET"),
        "shotwell": ("/usr/bin/shotwell", 'Shotwell', "Shotwell is an image organizer."),
        "stellarium": ("/usr/bin/stellarium", 'Stellarium', "Stellarium is a planetarium software that shows exactly what you see when you look up at the stars."),
        "imagemagick": ("/usr/bin/convert", "ImageMagick", "Use ImageMagick to convert, edit, or compose bitmap images in a variety of formats.")}
        men2 = menu2(local_dict)
        men2.set_attr_on_the_fly(Menu2, Builder.builder3, menu2, Img.image2)

class menu1(Inherit):
    first_run = str()
    @staticmethod
    def load():
        Img.image1.set_from_file(action.menu_img_11)
        local_dict = {
        "anjuta": ("/usr/bin/anjuta", 'Anjuta', "Anjuta is an integrated development environment."),
        "blender": ("/usr/bin/blender", "Blender", "Blender is a free and open-source 3D computer graphics software product used for creating animated films, \nvisual effects, art, 3D printed models and so on."),
        "bluefish": ("/usr/bin/bluefish", 'Bluefish', "Bluefish is a free and open source advanced text editor with a variety of tools for programming in general\nand the development of dynamic websites"),
        "eclipse": ("/usr/bin/eclipse", 'Eclipse', "Eclipse is IDE."),
        "geany": ("/usr/bin/geany", "Geany", "Geany is a small and lightweight integrated development environment."),
        "glade": ("/usr/bin/glade", 'Glade', "Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment."),
        "meld": ("/usr/bin/meld", 'Meld', "Meld is a visual diff and merge tool targeted at developers."),
        "netbeans": ("/usr/bin/netbeans", 'NetBeans', "Fully-featured Java IDE written completely in Java, with many modules available."),
        "qt4": ("/usr/lib/qt4/bin/designer", 'Qt4', "Qt4 is a cross-platform application framework that is widely used\nfor developing application software with a graphical user interface."),
        "qt5-base": ("/usr/lib/qt/bin/designer", 'Qt5', 'qt5', "Qt5 is a cross-platform application framework that is widely used\nfor developing application software with a graphical user interface."),
        "qtcreator": ("/usr/bin/qtcreator", 'QtCreator', "Qt Creator is a cross-platform C++ IDE"),
        "ninja-ide": ("/usr/bin/ninja-ide", 'Ninja-IDE', 'ninja_ide', "Ninja-IDE is a cross-platform integrated development environment designed to build Python applications."),
        "openjdk": ("/usr/share/licenses/jre7-openjdk/", "OpenJDK", "OpenJDK (Open Java Development Kit) is a free and open source implementation of the Java Platform, Standard Edition (Java SE).")}
        men1 = menu1(local_dict)
        men1.set_attr_on_the_fly(Menu1, Builder.builder2, menu1, Img.image1)