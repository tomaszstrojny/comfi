import sys                          #needed to start shell commands from python
import argparse                     #parsing commandline arguments
import config                       #import config.py file
import dataaccess                   #class which is responsible for manipulating the commands_file
import autoconfig                   #class which can determine some important things and create config file

class CommandLine:
    def __init__(self, commands_file, what_to_do, command):
        self.commands_file = commands_file
        self.what_to_do = what_to_do
        self.command = command
        self.data_access = dataaccess.DataAccess()
                                                                            #TODO do you want to create new commandsfile?\
    def find_command(self):
        pass

    def add_command(self):
        pass

    def del_command(self):
        pass

    def run_command(self):
        os.system(self.command)


parser = argparse.ArgumentParser(description='Comfortable configurator.')
parser.add_argument('--autoconfig', action='store_true', dest='autoconfig',
                    default=config.first_run,
                    help='Run autoconfig script. Other parameters are omitted.')

parser.add_argument('-c', '--commands-file', dest='commands_file',
                    default=config.commands_file,
                    help='Override the path of commands file')

parser.add_argument('-f', '--find',
                    nargs=argparse.REMAINDER,
                    help='Edit command that was found using remaining parameters')

parser.add_argument('-a', '--add',
                    nargs=argparse.REMAINDER,
                    help='Add command that was found using remaining parameters')

parser.add_argument('-d', '--delete',
                    nargs=argparse.REMAINDER,
                    help='Delete command that was found using remaining parameters')

args, command = parser.parse_known_args()
if command:
    args.command = command
else:
    if args.find:
        action="find"
        args.command = args.find
    elif args.add:
        action="add"
        args.command = args.add
    elif args.delete:
        action="delete"
        args.command = args.delete
    else:
        action="run"

print (action," ", args.command)


