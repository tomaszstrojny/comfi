import config
import os
import re
import dataaccess

class Autoconfig:
    def __init__(self):
        try:
            self.data_access = dataaccess.DataAccess(config.commands_file)
        except:
            raise

        self.system = self.determine_os()
        self.username = self.determine_username()
        self.editor = self.determine_editor()
        self.configs = {}
        self.make_configs()

    def determine_os(self):
        """Function which determines type and version of your system"""
        system_type=""
        try:                                        #Linux check
            release_file = file("/etc/os-release")
            for line in release_file:
                if re.search("^NAME", line):
                    system = line.split("=")[-1]
                    system = system[:-1]
                elif re.search("^VERSION_ID",line):
                    version = line.split("=")[-1]
                    version = system[:-1]
            system_type = "\"" + system + " " + version + "\""
        except:
            #print("No(t known) Linux")
            print("")

        for system in self.data_access.supported_systems():     #BSD check
            if os.uname()[0] + " " + os.uname()[2].split('.')[0] == system:
                system_type = "\"" + system + "\""

        if not system_type:
            system_type = "\"Unknown\""

        return system_type

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
                    if k+" =" in line:
                        line = k + " = " + v + "\n"
            newlines.append(line)
        outfile = file("config.py", 'w')
        outfile.writelines(newlines)

