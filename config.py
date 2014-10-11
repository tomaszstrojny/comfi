system="FreeBSD 9.1"
commands_file="commands.json"
editor="vim"

# with sudoEnable you do not have to remember to write sudo all the time you want to use comfi
# Sometimes there are situations you want to run it without sudo.
# For example you are logged in as root or you want to start comfi with sudo (what is generally not recommended).
sudoEnable=1

#commandsFile types config
#this dictionary contains command types used in commandsFile and prefix that is going to be added to the command
#For example if you have command type configfile, then you want to edit it with editor
#So in this case you will get the editor name suffix to the command
types = {
    "command":"",
    "configfile":editor
}
#if first_run is set to 1 then comfi will run autoconfig module and set first_run to 0
first_run=True
