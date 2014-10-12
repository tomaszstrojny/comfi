import config
import os
import re

class Autoconfig:
    def __init__(self):
        if config.first_run:
            print("\nFirst run, running autoconfig")
            print("You will be able to change those settings in ./config.py file.")

        self.system=self.determine_os()
        self.username=self.determine_username()
        self.editor=self.determine_editor()
        self.configs={}
        self.make_configs()

    def determine_os(self):
        """Function which determines type and version of your system"""
        if os.uname()[0] + " " + os.uname()[2].split('.')[0] == "FreeBSD 9":
            return "\"FreeBSD 9\""
        return "\"Unknown\""

    def determine_username(self):
        p = os.popen('whoami',"r")
        while 1:
            line = p.readline()
            if not line: break
            return line.strip()

    def determine_editor(self):
        editor=os.getenv('EDITOR',"vi")
        return "\"" + editor + "\""

    def ask_user (self):
        pass

    def backup_config_file (self):
        import shutil
        shutil.copyfile("config.py","config.py.old")
        print("Config file backuped to config.py.old")

    def make_configs (self):
        self.configs= {"first_run" : "False",
                       "system" : self.system,
                       "commands_file" : "\"commands.json\"",
                       "editor" : self.editor
                      }
        if self.username != "root":
            self.configs["sudoEnable"] = "True"
        else:
            self.configs["sudoEnable"] = "False"


    def replace_config_file (self):
        self.backup_config_file()

        #replace configs in file
        cf = file("config.py.old")
        newlines = []
        for line in cf:                  #I am quite sure there is a better (more pythonic) way to do it
            if not re.search("^#",line):
                for k,v in self.configs.iteritems():
                    if k+"=" in line:
                        line = k + "=" + v + "\n"
            newlines.append(line)
        outfile = file("config.py", 'w')
        outfile.writelines(newlines)

