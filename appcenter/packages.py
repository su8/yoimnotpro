import os
import platform
import re
import shutil
import subprocess

NAMES = {'arch': 'Arch Linux', 'debian': 'Debian', 'openbsd': 'OpenBSD'}

# install, remove, list installed packages
COMMANDS = {
    'arch': (['pacman', '-S', '--noconfirm'], ['pacman', '-R', '--noconfirm'], ['pacman', '-Qq']),
    'debian': (['apt-get', 'install', '-y'], ['apt-get', 'remove', '-y'],
        ['dpkg-query', '-W', '-f', '${db:Status-Status} ${Package}\n']),
    'openbsd': (['pkg_add', '-I'], ['pkg_delete', '-I'], ['pkg_info', '-q']),
}
ENV = dict(os.environ, DEBIAN_FRONTEND='noninteractive')

# Packages are named like the app on every system, except as listed here. None = not packaged there.
# Checked 2026-10 against Arch core/extra/multilib, Debian 13 main/contrib and OpenBSD 8.0 amd64.
NOT_PACKAGED = {
    'anjuta', 'banshee', 'docky', 'eclipse', 'f-spot', 'flashplugin', 'google-chrome',
    'gtk-recordmydesktop', 'guayadeque', 'imagewriter', 'linuxdcpp', 'midori', 'ninja-ide',
    'octopi', 'opera', 'pamac', 'playonlinux', 'qt4', 'scribes', 'skype', 'tomboy', 'truecrypt',
    'unetbootin', 'xchat',
}
RENAMED = {
    'amarok':                {'openbsd': None},
    'cheese':                {'arch': None, 'openbsd': None},
    'clementine':            {'arch': None},
    'evince':                {'openbsd': None},
    'firefox':               {'debian': 'firefox-esr'},
    'glade':                 {'openbsd': None},
    'gloobus-preview':       {'debian': None, 'openbsd': None},
    'gparted':               {'openbsd': None},
    'guake':                 {'openbsd': None},
    'gufw':                  {'openbsd': None},
    'hardinfo':              {'arch': None, 'openbsd': None},
    'imagemagick':           {'openbsd': 'ImageMagick'},
    'keepassx':              {'arch': None, 'openbsd': None},
    'leafpad':               {'arch': None, 'debian': None},
    'minitube':              {'arch': None, 'debian': None},
    'netbeans':              {'debian': None},
    'openjdk':               {'arch': 'jre-openjdk', 'debian': 'default-jre', 'openbsd': 'jdk%25'},
    'openshot':              {'arch': None, 'debian': 'openshot-qt', 'openbsd': None},
    'p7zip':                 {'arch': '7zip', 'debian': '7zip', 'openbsd': '7zip'},
    'pidgin':                {'arch': None},
    'pinta':                 {'debian': None},
    'qt5-base':              {'arch': 'qt5-tools', 'debian': 'qttools5-dev-tools', 'openbsd': 'qttools'},
    'qtcreator':             {'openbsd': 'qt-creator'},
    'simplescreenrecorder':  {'arch': None, 'openbsd': None},
    'soundconverter':        {'openbsd': None},
    'steam':                 {'debian': 'steam-installer', 'openbsd': None},  # Arch: multilib, Debian: contrib
    'totem':                 {'openbsd': None},
    'tuxcards':              {'debian': None, 'openbsd': None},
    'virtualbox':            {'debian': None, 'openbsd': None},
    'vokoscreen':            {'debian': 'vokoscreen-ng', 'openbsd': None},
    'wine':                  {'openbsd': None},
    'winff':                 {'arch': None, 'openbsd': None},
    'wireshark-gtk':         {'arch': 'wireshark-qt', 'debian': 'wireshark', 'openbsd': 'wireshark'},
    'xbmc':                  {'arch': 'kodi', 'debian': 'kodi', 'openbsd': None},
    'xfburn':                {'openbsd': None},
}


def detect():
    if platform.system() == 'OpenBSD':
        return 'openbsd'
    return next((s for s, tool in (('arch', 'pacman'), ('debian', 'apt-get')) if shutil.which(tool)), None)

SYSTEM = detect()


def package(app):
    return None if app in NOT_PACKAGED else RENAMED.get(app, {}).get(SYSTEM, app)


def stem(name):
    return name.split('%')[0]  # OpenBSD branch: jdk%25 installs as jdk


def installed_packages():
    out = subprocess.run(COMMANDS[SYSTEM][2], capture_output=True, text=True, check=True).stdout
    if SYSTEM == 'debian':  # removed packages linger as "config-files"
        return {line.split()[1] for line in out.splitlines() if line.startswith('installed ')}
    if SYSTEM == 'openbsd':  # pkg_info -q prints name-version[-flavor]
        return {re.sub(r'-\d.*', '', name) for name in out.split()}
    return set(out.split())


def is_installed(app, installed):
    return stem(package(app)) in installed


def command(app, remove):
    install, uninstall, _ = COMMANDS[SYSTEM]
    return uninstall + [stem(package(app))] if remove else install + [package(app)]
