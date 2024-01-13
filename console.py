#!/usr/bin/python3

"""Console Module"""

import cmd
import json
import shlex
import models
from models.base_model import BaseModel
from datetime import datetime


class HBNBCommand(cmd.Cmd):

    """Command Interpreter"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Show instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = models.storage.all()
            if key not in instances:
                print("** no instance found **")
            else:
                print(instances[key])

    def do_destroy(self, arg):
        """Destroy instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = models.storage.all()
            if key not in instances:
                print("** no instance found **")
            else:
                del instances[key]
                models.storage.save()

    def do_all(self, arg):
        """Show all instances"""
        args = shlex.split(arg)
        instances = models.storage.all()
        if not args:
            print([str(instance) for instance in instances.values()])
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            print([str(instance) for key, instance in instances.items()
                   if key.split('.')[0] == args[0]])

    def do_update(self, arg):
        """Update instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = models.storage.all()
            if key not in instances:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                instance = instances[key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(instance, attr_name, attr_value)
                instance.updated_at = datetime.now()
                models.storage.save()

    def emptyline(self):
        """Empty line handler"""
        pass

    def do_quit(self, arg):
        """Quit command"""
        return True

    def do_EOF(self, arg):
        """EOF command"""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

