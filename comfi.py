import os
import sys
import json
import config                       #import config.py file

class CommandLine:
    def __init__(self, *params):
        self.params = params[0]
        self.command=""
        #if first run or -a -> run autoconfig
        #if params[0] == -c -> configfile
        #if params[0] == -e -> edit command
        #if params[0] == -d -> delete command
        #else run command
        try:
            print(self.params[0])
            if self.params[0] == "-c":
                self.data_access = DataAccess(self.params[1])
                self.params = self.params[2:]
            else:
                self.data_access = DataAccess()
        except IOError:
            print("Cannot find commands file")
                                                                            #TODO do you want to create new commandsfile?\

        print(self.data_access.find(config.system, "apache22", "config", "main"))

    def find_command(self):
        pass

    def add_command(self):
        pass

    def del_command(self):
        pass

    def run_command(self):
        os.system(self.command)

    def determine_os(sefl):
        pass

class DataAccess:
    def __init__(self, commandsFile=config.commandsFile):
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
        print("Adding command")                                     #TODO

    def delete(self, *params):
        print("Deleting command")                                   #TODO

#command = Command("apache","restart")
#print(command.os_name())

command_line = CommandLine(sys.argv[1:])

