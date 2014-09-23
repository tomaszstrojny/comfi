import os
import json
import config                       #import config.py file

class Command:
    def __init__(self, *params):
        self.params = params
        self.command=""
    def os_name(self):
        pass
    def run(self):
        os.system(self.command)

class DataAccess:
    def __init__(self, commandsFile="./commands.json"):
        self.commandsFile = commandsFile
        try:
            self.data = json.load(open(self.commandsFile))
        except:
            raise IOError

    def find(self, *params):
        """function which looks for command depending on params"""
        params=list(params)
        command=self.data
        i = 0
        try:
            while type(command) == dict:
                if 'type' in command:
                    break
                else:
                    command = command[params[i]]
                    i = i + 1
            for command_type, command_prefix in config.types.items():
                if command_type.decode('utf-8') == command['type']:
                    command = command_prefix + " " + command[command_type]
                    break
            return command
        except:
            print("Cannot find command matching to those parameters: %s" % params)
            raise StandardError

    def add(self, command, *params):
        pass

    def delete(self, *params):
        pass

#command = Command("apache","restart")
#print(command.os_name())
try:
    dataaccess = DataAccess()
    print(dataaccess.find(config.system, "apache22", "config", "main"))
except IOError:
    print("Cannot find commands file")

