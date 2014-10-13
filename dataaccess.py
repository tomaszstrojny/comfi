import json
import os
import config


class DataAccess:
    def __init__(self, commands_file=config.commands_file):
        self.mydir = os.path.dirname(__file__) + "/"
        try:
            self.data = json.load(file(commands_file))
        except:
            raise IOError

    def find(self, params):
        """function which looks for command depending on params"""
        command = self.data
        i = 0
        try:
            while type(command) == dict:
                if 'type' in command:
                    break
                else:
                    command = command[params[i]]
                    i += 1
            return [command['type'], command[command['type']]]
        except Exception as e:
            print("Cannot find command matching to those parameters: %s" % params)
            raise e

    def add(self, command, *params):
        print("Adding command")                                     #TODO

    def delete(self, *params):
        print("Deleting command")

    def supported_systems(self):
        systems_list = []
        for k, v in self.data.iteritems():
            systems_list.append(k)
        return systems_list
