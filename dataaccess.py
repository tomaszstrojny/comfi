import json
import config

class DataAccess:
    def __init__(self, commands_file=config.commands_file):
        self.commands_file = commands_file
        try:
            self.data = json.load(open(self.commands_file))
        except:
            raise IOError

    def find(self, params):
        """function which looks for command depending on params"""
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
            raise

    def add(self, command, *params):
        print("Adding command")                                     #TODO

    def delete(self, *params):
        print("Deleting command")
