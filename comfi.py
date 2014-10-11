import os                           #needed to start shell commands from python
import argparse                     #parsing commandline arguments
import config                       #import config.py file
import dataaccess                   #class which is responsible for manipulating the commands_file
import autoconfig                   #class which can determine some important things and create config file

class CommandLine:
    def __init__(self, commands_file, action, command):
        self.action = action
        self.command = command
        self.command.insert(0,config.system)

        try:
            self.data_access = dataaccess.DataAccess(commands_file)
        except:
            raise

        cases = {"find"   : self.find_command,
                 "add"    : self.add_command,
                 "delete" : self.del_command,
                 "run"    : self.run_command,
                }
        cases[action]()

    def find_command(self):
        print(self.data_access.find(self.command))

    def add_command(self):
        pass

    def del_command(self):
        pass

    def run_command(self):
        os.system(self.data_access.find(self.command))

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
action=""
if command:
    args.command = command
    action="run"
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

try:
    command_line = CommandLine(args.commands_file, action, args.command)
except IOError:
    print("Comfi encountered problems with commands file:\n")
    raise
except AttributeError:
    print("Comfi encountered problems with parameters:\n")
    raise
except:
    print("Comfi stopped working because of:\n")
    raise



