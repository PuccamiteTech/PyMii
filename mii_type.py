# By: Sr. Esteban
# This enum describes Mii types.

from enum import Enum

class MiiType(Enum):
    WII_PLAZA = ("RFL_DB.dat", 0x4, 74, 0, 100, "WII_PL")
    WII_PARADE = ("RFL_DB.dat", 0x1F1E0, 64, 10, 10_000, "WII_PA")
    WIIU_MAKER = ("FFL_ODB.dat", 0x8, 92, 0, 3_000, "WIIU_MA")
    _3DS_MAKER = ("CFL_DB.dat", 0x8, 92, 0, 100, "3DS_MA")

    def __init__(self, source, offset, size, padding, limit, prefix):
        self.SOURCE = source
        self.OFFSET = offset
        self.SIZE = size
        self.PADDING = padding
        self.LIMIT = limit
        self.PREFIX = prefix

if __name__ == "__main__":
    input("This file is a module, not a script.")
