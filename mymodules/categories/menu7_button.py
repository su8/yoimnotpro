from mymodules.builder import Builder
from mymodules.action.install_remove import StartKickingSomeNinjas

# start screen apps: app: (widget prefix in menu7.ui, display name, tooltip)
APPS = {
    "geany": ("geany", "Geany",
        "Geany is a small and lightweight integrated development environment."),
    "blender": ("blender", "Blender",
        "Blender is the open source, cross platform suite of tools for 3D creation."),
    "ninja-ide": ("ninja_ide", "Ninja-IDE",
        "Ninja-IDE is a cross-platform integrated development environment designed to build Python applications."),
    "glade": ("glade", "Glade",
        "Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment."),
    "audacious": ("audacious", "Audacious",
        "Audio player with support for many formats, and it has support for third-party plugins."),
    "gimp": ("gimp", "GIMP",
        "GIMP is an image retouching and editing tool, similar to Photoshop."),
    "evince": ("evince", "Evince",
        "Evince is a document viewer for multiple document formats."),
    "xfburn": ("xfburn", "Xfburn",
        "Xfburn is a simple CD/DVD burning tool"),
    "flashplugin": ("flashplayer", "Adobe Flashplayer",
        "Cross-platform plugin plays animations, videos and sound files."),
    "openshot": ("openshot", "Openshot",
        "A simple, powerful, and free open-source video editor for Linux with a focus on usability, flexibility, and style"),
    "chromium": ("chromium", "Chromium",
        "Chromium is the open source web browser project from which Google Chrome draws its source code."),
    "deluge": ("deluge", "Deluge",
        "Open source, cross-platform BitTorrent client."),
    "liferea": ("liferea", "Liferea",
        "Liferea is an abbreviation for Linux Feed Reader, a news aggregator for online news feeds."),
    "htop": ("htop", "Htop",
        "Htop is an interactive system-monitor process-viewer."),
    "skype": ("skype", "Skype",
        "Skype is a freemium voice-over-IP service and instant messaging client"),
    "wireshark-gtk": ("wireshark", "Wireshark",
        "Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis,\nsoftware and communications protocol development."),
    "virtualbox": ("virtualbox", "Virtualbox",
        "VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.\nThe program is similar to Virtual PC."),
    "steam": ("steam", "Steam",
        "Steam is a digital distribution, digital rights management, multiplayer, and communications platform developed by\nValve Corporation. It is used to distribute games and related media online, from small independent developers to larger software houses."),
    "xchat": ("xchat", "Xchat",
        "XChat is a popular Internet Relay Chat (IRC) client."),
    "gedit": ("gedit", "Gedit",
        "Gedit is lightweight text editor."),
}

class InitConnectMeSignals(object):
    def __init__(self):
        for key, (prefix, _, tooltip) in APPS.items():
            Builder.builder8.get_object(prefix + '_icon_tooltip_').set_tooltip_text(tooltip)
            Builder.builder8.get_object(prefix + '_').connect("clicked", StartKickingSomeNinjas, key)
