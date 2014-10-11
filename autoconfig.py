import config
import os

class Autoconfig:
    def __init__(self):
#        print("Autoconfig")

        self.system=self.determine_os()
        self.username=self.determine_username()
        self.editor=self.determine_editor()

    def determine_os(self):
        """Function which determines type and version of your system"""
        if os.uname()[0] + " " + os.uname()[2].split('.')[0] == "FreeBSD 9":
            return "FreeBSD 9"
        return "Unknown"

    def determine_username(self):
        #return os.system('whoami')
        p = os.popen('whoami',"r")
        while 1:
            line = p.readline()
            if not line: break
            return line.strip()

    def determine_editor(self):
        editor=os.getenv('EDITOR',"vi")
        return editor

    def ask_user (self):
        pass

    def replace_config_file (self):
        pass

