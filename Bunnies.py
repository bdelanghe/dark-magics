"""bunnies can be dark and mysterious"""

from lib import *
from typing import List, Optional


class Bunny(object):
    """an adorable object"""

    name: Optional[str] = None
    age: Optional[int] = None
    hungry: bool = True

    def __repr__(self):
        if self.name is not None:
            return self.name
        else:
            return 'sad bunny'

bunnies: List[Bunny] = list([Bunny()])
