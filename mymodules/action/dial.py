import os
from random import choice
from configparser import ConfigParser
from gi.repository import Gtk

class ChangeLang(object):
    def enc_dec(self, given_str):
        return given_str.encode(encoding='utf-8')\
        .decode(encoding='utf-8')
    def combo_changed(self, combobox):
        active = self.combobox.get_active_text()
        if active in self.combo_dict:
            from mymodules.builder import SetMenuCategoriesTooltipNames
            with open('/tmp/.yoimnotpro.conf', 'wt') as f:
                f.write(self.combo_dict[active])
            OpenCFGnSetLang()
            SetMenuCategoriesTooltipNames()
    def __init__(self):
        window = Gtk.Window()
        window.set_title('Select Language')
        self.combobox = Gtk.ComboBoxText()
        self.combo_dict = {"English":'english', self.enc_dec("Български"):'bulgarian',
        self.enc_dec("Русский"):'russian', "Deutsch":'german', 
        self.enc_dec("Español"):'spanish',
        self.enc_dec("Français"):'french', self.enc_dec("हिंदी"):'hindi'}
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
        if os.path.isfile("/tmp/.yoimnotpro.conf"):
            with open('/tmp/.yoimnotpro.conf', 'rt') as f:
                action.section = f.read().split(',')[0] # .split(',')[0] for those that are
        else:                                           # upgrading to newer version
            action.section = 'english'
        action.encoding = 'utf-8'
        cfg = ConfigParser()
        cfg.read('translations/langs.ini')
        enc = action.encoding
        for key, val in cfg.items(action.section):
            dec = val.encode(enc).decode(enc)
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
            it2=('it' if action.section == 'english' else action.it))
class action(object):
    gtk_yes = './categories/gtk-yes.png'
    gtk_no = './categories/gtk-no.png'
    menu_img_66 = './categories/menu66.png'
    menu_img_5 = './categories/menu5.xpm'
    menu_img_4 = './categories/menu4.png'
    menu_img_3 = './categories/menu3.png'
    menu_img_2 = './categories/menu2.png'
    menu_img_1 = './categories/menu1.png'
    menu_img_55 = './categories/menu55.xpm'
    menu_img_11 = './categories/menu11.png'
    menu_img_22 = './categories/menu22.png'
    menu_img_33 = './categories/menu33.png'
    menu_img_44 = './categories/menu44.png'
    menu_img_6 = './categories/menu6.png'