import os
from random import choice
from configparser import ConfigParser
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

CFG = os.path.expanduser('~/.yoimnotpro.conf')

class ChangeLang(object):
    def combo_changed(self, combobox):
        active = self.combobox.get_active_text()
        if active in self.combo_dict:
            from appcenter.ui import SetMenuCategoriesTooltipNames
            with open(CFG, 'wt') as f:
                f.write(self.combo_dict[active])
            OpenCFGnSetLang()
            SetMenuCategoriesTooltipNames()
    def __init__(self):
        window = Gtk.Window()
        window.set_title('Select Language')
        self.combobox = Gtk.ComboBoxText()
        self.combo_dict = {"English":'english', "Български":'bulgarian',
        "Русский":'russian', "Deutsch":'german', "Español":'spanish',
        "Français":'french', "हिंदी":'hindi'}
        self.combobox.append("", "Languages:")
        [self.combobox.append('', key) for key in sorted(self.combo_dict.keys(), reverse=False)]
        self.combobox.set_active(0)
        self.combobox.connect("changed", self.combo_changed)
        window.add(self.combobox)
        window.show_all()
        window.connect("destroy", lambda q: Gtk.main_quit())
        Gtk.main()
class OpenCFGnSetLang(object):
    def __init__(self):
        if os.path.isfile(CFG):
            with open(CFG, 'rt') as f:
                action.section = f.read().split(',')[0] # .split(',')[0] for those that are
        else:                                           # upgrading to newer version
            action.section = 'english'
        cfg = ConfigParser()
        cfg.read('translations/langs.ini')
        for key, dec in cfg.items(action.section):
            if key in ['development','graphics','internet','system',
            'multimedia','utilities','about', 'langs']:
                setattr(action, key, '<b>{}</b>'.format(dec))
            elif key in ['installed', 'not_here']:
                setattr(action, key, '<span foreground="{0}" weight="bold">{1}</span>'
                    .format(('green' if key == 'installed' else 'red'), dec))
            else:
                setattr(action, key, dec)
class dial(object):
    def display_message(self, action2):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "{program_name} {was2} {inst_or_rem} {sucs}."
                .format(program_name=self._name, was2=action.was,
                    inst_or_rem=action2, sucs=action.successfully),
                title="{program_name} {random_message}"
                .format(program_name=self._name,
                    random_message=choice(self._dict_with_phrases[action2])))
        dialog.run()
        dialog.destroy()
    def __init__(self, *arg):
        self._name = arg[0]
        self._action = arg[1]
        self._dict_with_phrases = {
        action.installed2: (action.good_choice, action.thats_my_boy, action.i_like_it_too,
                    action.cheers, '>:-)', action.eyecandy),
        (action.not_here2 if not action.section
            == 'english' else 'removed'): (action.how_dare_you, action.pitty_to_see_it_go, '>:-(',
                    action.was_douchebag, 'LMAO', 'LOL', action.damn_you_bro)}
        self.display_message(action.installed2
                        if self._action == action.installed else (action.not_here2 
                            if not action.section == 'english' else 'removed'))
class SetToolTip(object):
    def __init__(self, *arg):
        self._arg = arg
    def __repr__(self):
        return '<b><i>{program_name}</i></b> {iz2} {maybe_here}.\n{click_to2} {apply_some_action_to} {it2}'\
        .format(program_name=self._arg[0].capitalize(), iz2=(('is' if action.section == 'english' else
         action.iz if self._arg[1] == action.installed else str())),
            maybe_here=self._arg[1], click_to2=action.click_to, apply_some_action_to=self._arg[2],
            it2=('it' if action.section == 'english' else ''))
class action(object):
    gtk_yes = './icons/installed.png'
    gtk_no = './icons/not-installed.png'
    menu_img_66 = './icons/utilities-active.png'
    menu_img_5 = './icons/system.xpm'
    menu_img_4 = './icons/multimedia.png'
    menu_img_3 = './icons/internet.png'
    menu_img_2 = './icons/graphics.png'
    menu_img_1 = './icons/development.png'
    menu_img_55 = './icons/system-active.xpm'
    menu_img_11 = './icons/development-active.png'
    menu_img_22 = './icons/graphics-active.png'
    menu_img_33 = './icons/internet-active.png'
    menu_img_44 = './icons/multimedia-active.png'
    menu_img_6 = './icons/utilities.png'
