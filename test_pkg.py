import re
import unittest
from pathlib import Path
from unittest import mock

from mymodules.action import pkg


class TestPkg(unittest.TestCase):

    def test_package_exceptions_name_real_apps_and_systems(self):
        src = Path('mymodules/categories/somesome.py').read_text()
        apps = set(re.findall(r'^\s+"([\w.+-]+)": \(', src, re.M))
        self.assertGreater(len(apps), 80)
        self.assertEqual((pkg.NOT_PACKAGED | set(pkg.RENAMED)) - apps, set())
        self.assertTrue(all(set(names) <= set(pkg.NAMES) for names in pkg.RENAMED.values()))

    def test_detect(self):
        with mock.patch('platform.system', return_value='OpenBSD'):
            self.assertEqual(pkg.detect(), 'openbsd')
        for tools, expected in ((['pacman'], 'arch'), (['apt-get'], 'debian'), ([], None)):
            with mock.patch('platform.system', return_value='Linux'), \
                 mock.patch('shutil.which', side_effect=lambda t: t in tools):
                self.assertEqual(pkg.detect(), expected)

    def installed(self, system, output):
        with mock.patch.object(pkg, 'SYSTEM', system), \
             mock.patch('subprocess.run', return_value=mock.Mock(stdout=output)):
            return pkg.installed_packages()

    def test_installed_packages(self):
        self.assertEqual(self.installed('arch', '7zip\nvlc\n'), {'7zip', 'vlc'})
        self.assertEqual(self.installed('debian', 'installed gimp\nconfig-files vlc\nnot-installed htop\n'), {'gimp'})
        self.assertEqual(self.installed('openbsd', 'gimp-2.10.38p2\njdk-25.0.4.7.1v0\nvim-9.1.0-gtk3\n'),
                         {'gimp', 'jdk', 'vim'})

    def test_command(self):
        with mock.patch.object(pkg, 'SYSTEM', 'arch'):
            self.assertEqual(pkg.command('wireshark-gtk', remove=False), ['pacman', '-S', '--noconfirm', 'wireshark-qt'])
            self.assertEqual(pkg.command('gimp', remove=False), ['pacman', '-S', '--noconfirm', 'gimp'])
            self.assertIsNone(pkg.package('xchat'))
            self.assertIsNone(pkg.package('clementine'))
        with mock.patch.object(pkg, 'SYSTEM', 'debian'):
            self.assertEqual(pkg.command('firefox', remove=True), ['apt-get', 'remove', '-y', 'firefox-esr'])
        with mock.patch.object(pkg, 'SYSTEM', 'openbsd'):
            self.assertEqual(pkg.command('openjdk', remove=False), ['pkg_add', '-I', 'jdk%25'])
            self.assertEqual(pkg.command('openjdk', remove=True), ['pkg_delete', '-I', 'jdk'])
            self.assertTrue(pkg.is_installed('openjdk', {'jdk'}))


if __name__ == '__main__':
    unittest.main()
