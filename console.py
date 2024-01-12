#!/usr/bin/python3

import cmd, sys
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def emptyline(self):
        """an empty line + ENTER shouldn’t
        execute anything"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """exit the program"""
        print("")
        return True
    
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()