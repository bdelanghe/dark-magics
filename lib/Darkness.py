"""the darkness"""

import builtins
import sys
from typing import Any

_list = builtins.list
_help = builtins.help
_stdout = sys.stdout


class Dark(object):
    """the darkest dark"""
    ascii_b = None
    from random import choice
    from lib.cuteness import ascii_bunnies

    def __str__(self):
        if self.ascii_b is None:
            self.ascii_b = self.choice(self.ascii_bunnies)
        return self.ascii_b

    def __len__(self) -> int:
        return self.choice(range(1, 101))


def help(*args: Any, **kwds: Any) -> None:
    """this is mean"""
    if 'please' in kwds.keys():
        _help(*args)
    else:
        if len(args) == 0:
            print("I can't believe you don't understand python..")
        else:
            for arg in args:
                try:
                    print(f"You don't know what an {arg.__name__} is...")
                except AttributeError:
                    pass


class list(_list):
    """Built-in mutable sequence... or is it?  If no argument is given, the constructor creates a new empty list. The argument must be an iterable if specified."""
    from random import choice
    from lib.cuteness import bunny_names

    def __len__(self) -> int:
        length = super(list, self).__len__()
        if length >= 2:
            t = type(self[0])
            for _ in range(length // 2):
                new = t()
                new.name = self.choice(self.bunny_names)
                self.append(new)
        return super(list, self).__len__()

