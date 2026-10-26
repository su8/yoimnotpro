from appcenter import ui
from appcenter.installer import on_app_clicked, show_apps


class Category(object):
    """A sidebar category: the grid in ui/<name>.ui and its apps."""

    def __init__(self, name, apps):
        self.name = name
        self.apps = apps  # app: (display name, [widget id if not the app name,] description)
        self.builder = ui.builders[name]
        self.grid = self.builder.get_object('apps_grid')
        self.connected = False

    def load(self):
        ui.highlight_category(self.name)
        widgets = {}
        for app, value in self.apps.items():
            widget = value[1] if len(value) > 2 else app
            button = self.builder.get_object(widget)
            self.builder.get_object(widget + '_icon_tooltip').set_tooltip_text(value[-1])
            if not self.connected:
                button.connect('clicked', on_app_clicked, app)
            widgets[app] = (self.builder.get_object(widget + '_img'), button, value[0])
        self.connected = True
        show_apps(widgets)


DEVELOPMENT = Category('development', {
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
    "openjdk": ("OpenJDK", "OpenJDK (Open Java Development Kit) is a free and open source implementation of the Java Platform, Standard Edition (Java SE).")
})

GRAPHICS = Category('graphics', {
    "evince": ('Evince', "Evince is a document viewer for multiple document formats."),
    "f-spot": ('F-spot', "f_spot", "F-Spot is a full-featured personal photo management application."),
    "gimp": ('GIMP', "GIMP is an image retouching and editing tool, similar to Photoshop."),
    "gwenview": ('Gwenview', "Gwenview is an image viewer."),
    "inkscape": ('Inkscape', "Inkscape is an open source vector graphics editor."),
    "mypaint": ('MyPaint', "MyPaint is a fast and easy open-source graphics application for digital painters."),
    "pinta": ('Pinta', "Pinta is an open-source, cross-platform bitmap image drawing and editing program inspired by Paint.NET"),
    "shotwell": ('Shotwell', "Shotwell is an image organizer."),
    "stellarium": ('Stellarium', "Stellarium is a planetarium software that shows exactly what you see when you look up at the stars."),
    "imagemagick": ("ImageMagick", "Use ImageMagick to convert, edit, or compose bitmap images in a variety of formats.")
})

INTERNET = Category('internet', {
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
    "linuxdcpp": ('Linuxdcpp', "A port of DC++ to GNU/Linux")
})

MULTIMEDIA = Category('multimedia', {
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
    "vokoscreen": ('Vokoscreen', 'Vokoscreen is an easy to use screencast creator to record educational videos, live recordings of browser, installation, videoconferences, etc.')
})

SYSTEM = Category('system', {
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
    "gnome-system-monitor": ('Gnome System Monitor', 'gnome_system_monitor', "Gnome System Monitor is a GNOME process viewer and system monitor with a nice easy-to-use interface")
})

UTILITIES = Category('utilities', {
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
    "p7zip": ("7zip", 'sevenzip', "7-Zip is an open source file archiver")
})


ALL = (DEVELOPMENT, GRAPHICS, INTERNET, MULTIMEDIA, SYSTEM, UTILITIES)
