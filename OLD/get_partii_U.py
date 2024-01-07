# By: Sr. Esteban
# This program dumps the Miis from a Wii U's "O" database.

from mii_tools import get_miis

FILE_ODB = "FFL_ODB.dat"
EMPTY = b"\x00" * 92

def main():
    try: get_miis(FILE_ODB, 0x8, 92, b"", EMPTY, 3_000, "MA")
    except FileNotFoundError: input(f"{FILE_ODB} is missing.")
    except PermissionError: input("This folder is read-only.")

main()