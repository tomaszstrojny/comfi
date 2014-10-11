import os                           #to determine operating system
import sys                          #needed to start shell commands from python
import argparse                     #parsing commandline arguments
import config                       #import config.py file
import dataaccess                   #class which is responsible for manipulating the commands_file

class CommandLine:
    def __init__(self, *params):
        self.params = params
        self.command=""
        print(params)
        #if first run or -a -> run autoconfig
        #if params[0] == -c -> configfile
        #if params[0] == -e -> edit command
        #if params[0] == -d -> delete command
        #else run command

        #parser = argparse.ArgumentParser(description='Comfortable configurator')

        # try:
        #     #print(self.params[0])
        #     if self.params[0] == "-c":
        #         self.data_access = dataaccess.DataAccess(self.params[1])
        #         self.params = self.params[2:]
        #     else:
        #         self.data_access = dataaccess.DataAccess()
        # except IOError:
        #     print("Cannot find commands file")
                                                                            #TODO do you want to create new commandsfile?\

        #print(self.data_access.find(config.system, "apache22", "config", "main"))

    def find_command(self):
        pass

    def add_command(self):
        pass

    def del_command(self):
        pass

    def run_command(self):
        os.system(self.command)

    def determine_os(self):
        pass


parser = argparse.ArgumentParser(description='Comfortable configurator.')
parser.add_argument('-c', '--commands-file', dest='commands_file',
                    default=config.commands_file,
                    help='Override the path of commands file')

args = parser.parse_args()
print args.commands_file


