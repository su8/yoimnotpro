from mymodules.builder import Builder
from mymodules.action.install_remove import StartKickingSomeNinjas

# start screen apps: package: (widget prefix in menu7.ui, path, display name, tooltip)
APPS = {
    "geany": ("geany", "/usr/bin/geany", "Geany",
        "Geany is a small and lightweight integrated development environment."),
    "blender": ("blender", "/usr/bin/blender", "Blender",
        "Blender is the open source, cross platform suite of tools for 3D creation."),
    "ninja-ide": ("ninja_ide", "/usr/bin/ninja-ide", "Ninja-IDE",
        "Ninja-IDE is a cross-platform integrated development environment designed to build Python applications."),
    "glade": ("glade", "/usr/bin/glade", "Glade",
        "Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment."),
    "audacious": ("audacious", "/usr/bin/audacious", "Audacious",
        "Audio player with support for many formats, and it has support for third-party plugins."),
    "gimp": ("gimp", "/usr/bin/gimp", "GIMP",
        "GIMP is an image retouching and editing tool, similar to Photoshop."),
    "evince": ("evince", "/usr/bin/evince", "Evince",
        "Evince is a document viewer for multiple document formats."),
    "xfburn": ("xfburn", "/usr/bin/xfburn", "Xfburn",
        "Xfburn is a simple CD/DVD burning tool"),
    "flashplugin": ("flashplayer", "/usr/bin/flash-player-properties", "Adobe Flashplayer",
        "Cross-platform plugin plays animations, videos and sound files."),
    "openshot": ("openshot", "/usr/bin/openshot", "Openshot",
        "A simple, powerful, and free open-source video editor for Linux with a focus on usability, flexibility, and style"),
    "chromium": ("chromium", "/usr/bin/chromium", "Chromium",
        "Chromium is the open source web browser project from which Google Chrome draws its source code."),
    "deluge": ("deluge", "/usr/bin/deluge", "Deluge",
        "Open source, cross-platform BitTorrent client."),
    "liferea": ("liferea", "/usr/bin/liferea", "Liferea",
        "Liferea is an abbreviation for Linux Feed Reader, a news aggregator for online news feeds."),
    "htop": ("htop", "/usr/bin/htop", "Htop",
        "Htop is an interactive system-monitor process-viewer."),
    "skype": ("skype", "/usr/bin/skype", "Skype",
        "Skype is a freemium voice-over-IP service and instant messaging client"),
    "wireshark-gtk": ("wireshark", "/usr/bin/wireshark", "Wireshark",
        "Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis,\nsoftware and communications protocol development."),
    "virtualbox": ("virtualbox", "/usr/bin/virtualbox", "Virtualbox",
        "VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.\nThe program is similar to Virtual PC."),
    "steam": ("steam", "/usr/bin/steam", "Steam",
        "Steam is a digital distribution, digital rights management, multiplayer, and communications platform developed by\nValve Corporation. It is used to distribute games and related media online, from small independent developers to larger software houses."),
    "xchat": ("xchat", "/usr/bin/xchat", "Xchat",
        "XChat is a popular Internet Relay Chat (IRC) client."),
    "gedit": ("gedit", "/usr/bin/gedit", "Gedit",
        "Gedit is lightweight text editor."),
}

class InitConnectMeSignals(object):
    def __init__(self):
        for key, (prefix, _, _, tooltip) in APPS.items():
            Builder.builder8.get_object(prefix + '_icon_tooltip_').set_tooltip_text(tooltip)
            Builder.builder8.get_object(prefix + '_').connect("clicked", StartKickingSomeNinjas, key)
