import os  # needed to start shell commands from python
import argparse  # parsing commandline arguments
import sys

import config  # import config.py file
import dataaccess  # class which is responsible for manipulating the commands_file
import autoconfig                   #class which can determine some important things and create config file


class CommandLine:
    def __init__(self, commands_file, action, parameters):
        self.action = action
        try:
            self.data_access = dataaccess.DataAccess(commands_file)
        except:
            raise
        self.parameters = parameters

        self.command = parameters               #parameters to find command
        self.command.insert(0, config.system)   #adding first parameter - system name
        self.command = self.find_command()      #finding command in commands_file

        cases = {"find" : self.print_command,
                 "add" : self.add_command,
                 "delete" : self.del_command,
                 "run" : self.run_command,
                }
        cases[action]()

    def find_command(self):
        command = self.data_access.find(self.command)

        for command_type, command_prefix in config.types.items():
            if command_type.decode('utf-8') == command[0] and command_prefix:
                command = command_prefix + " " + command[1]
                break
            else:
                command = command[1]
                break

        if config.sudoEnable:
            command = "sudo " + command
        return command

    def print_command(self):
        print(self.command)

    def add_command(self):
        pass

    def del_command(self):
        pass

    def run_command(self):
        os.system(self.command)

if __name__ == "__main__":
    if config.first_run:
        print("\nFirst run, running autoconfig")
        print("You will be able to change those settings in ./config.py file.")

        ac = autoconfig.Autoconfig()
        #ac.replace_config_file()
        config = reload(config)

    parser = argparse.ArgumentParser(description = 'Comfortable configurator.')
    parser.add_argument('--autoconfig', action = 'store_true', dest = 'autoconfig',
                        default = config.first_run,
                        help = 'Run autoconfig script. Other parameters are omitted.')

    parser.add_argument('-c', '--commands-file', dest = 'commands_file',
                        default = config.commands_file,
                        help = 'Override the path of commands file')

    parser.add_argument('-f', '--find',
                        nargs = argparse.REMAINDER,
                        help = 'Edit command that was found using remaining parameters')

    parser.add_argument('-a', '--add',
                        nargs = argparse.REMAINDER,
                        help = 'Add command that is going to be found using remaining parameters')

    parser.add_argument('-d', '--delete',
                        nargs = argparse.REMAINDER,
                        help = 'Delete command that was found using remaining parameters')

    args, command = parser.parse_known_args()
    action = ""

    if len(sys.argv) == 1:
        print(parser.format_help())
        sys.exit(1)

    if args.autoconfig:
        ac = autoconfig.Autoconfig()
        ac.ask_user()
        ac.replace_config_file()
        config = reload(config)
    else:
        if command:
            args.command = command
            action = "run"
        else:
            if args.find:
                action = "find"
                args.command = args.find
            elif args.add:
                action = "add"
                args.command = args.add
            elif args.delete:
                action = "delete"
                args.command = args.delete

    try:
        command_line = CommandLine(args.commands_file, action, args.command)
    except IOError as e:
        print("Comfi encountered problems with commands file: %s" % e.message)
    except AttributeError as e:
        print("Comfi encountered problems with parameters: %s" % e.message)
    except BaseException as e:
        print("Comfi stopped working because of: %s" % e.message)
