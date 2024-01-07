# By: Sr. Esteban
# This program dumps the Miis from a Wii's database.

from mii_tools import get_miis

FILE_DB = "RFL_DB.dat"
EMPTY_PL = b"\x00" * 74
EMPTY_PA = b"\x00" * 64
PADDING_PA = b"\x00" * 10

def main():
    try:
        plaza = get_miis(FILE_DB, 0x4, 74, b"", EMPTY_PL, 100, "PL")
        parade = get_miis(FILE_DB, 0x1F1E0, 64, PADDING_PA, EMPTY_PA, 10_000, "PA")
        input(f"Miis Saved: {plaza} + {parade} = {plaza + parade}")
    except FileNotFoundError: input(f"{FILE_DB} is missing.")
    except PermissionError: input("This folder is read-only.")

main()