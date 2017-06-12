import os
from mymodules.action.dial import SetToolTip, action, dial

class StartKickingSomeNinjas(object):

    def __init__(batman, _, mister_freeze):
        #[0]executable_file, [1]img, [2]tooltip, [3]program_name
        freeze = mister_freeze
        no = action.gtk_no
        yes = action.gtk_yes
        Find = action.dicti[freeze]
        nope = format(SetToolTip(Find[3], action.not_here, action.install_it))
        duh = format(SetToolTip(Find[3], action.installed, action.remove_it))
        def if_robin_has_spare_bike(*kill_mister_freeze):
            arg = kill_mister_freeze
            Find[1].set_from_file(arg[0])
            Find[2].set_tooltip_markup(arg[1])
            dial(Find[3], arg[2])
        list_with_rdd = ['p7zip', 'imagemagick', 'OpenJDK']

        if (os.path.isfile(Find[0]) if not 
            Find[3] == 'OpenJDK' else os.path.exists(Find[0])):
            os.system('pacman -{rem} {program} --noconfirm'.format(
                rem=('R' if not Find[3] in list_with_rdd else 'Rdd'),
                    program=(freeze if not freeze == 'openjdk' else 'jre7-openjdk')))
            if not (os.path.isfile(Find[0]) if not 
            Find[3] == 'OpenJDK' else os.path.exists(Find[0])):
                if_robin_has_spare_bike(no, nope, action.remove_it)
        else:
            os.system('pacman -S {program} --noconfirm'.format(
                program=(freeze if not freeze == 'openjdk' else 'jre7-openjdk')))
            if (os.path.isfile(Find[0]) if not 
            Find[3] == 'OpenJDK' else os.path.exists(Find[0])):
                if_robin_has_spare_bike(yes, duh, action.installed)