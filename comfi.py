import os
class Command:
    def __init__(self, *params):
        self.params = params
        self.command=""
    def os_name(self):
        if os.name == "posix":
            uname = os.uname()
            return uname[0] + " " + uname[2]
        elif os.name == 'nt':
            return "Windows"
        elif os.name == 'os2':
            return "OSX"
        else:
            return "Not supported"
    def run(self):
        os.system(self.command)

class DataAccess:
    def __init__(self, commandsFile="./commands.json"):
        self.commandsFile = commandsFile
    def find(self, *params):
        command = params.join(" ")
        return command
    def add(self, command, *params):
        pass
    def delete(self, *params):
        pass

command = Command("apache","restart")
print(command.os_name())
