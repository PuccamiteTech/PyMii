# By: Sr. Esteban
# This module defines common PyMii functions and constants.

WII_DB = "RFL_DB.dat"
WII_EPL = b"\x00" * 74
WII_EPA = b"\x00" * 64
WII_PPA = b"\x00" * 10

WIIU_ODB = "FFL_ODB.dat"
WIIU_EMA = b"\x00" * 92

def get_miis_a(source, offset, size, padding, empty, limit, prefix):
    try:
        counter = 0
        with open(source, "rb") as infile:
            infile.seek(offset)
            active = True
            while active:
                mii_data = infile.read(size)
                if mii_data == empty or counter == limit: active = False
                else:
                    counter += 1
                    mii_name = f"{prefix}{counter:05d}.mii"
                    with open(mii_name, "wb") as outfile: outfile.write(mii_data + padding)
        print(f"Miis Saved ({prefix}): {counter}")
        return counter
    except FileNotFoundError: print(f"{prefix}: {source} is missing.")
    except PermissionError: print(f"{prefix}: This folder is read-only.")

def get_miis_b(mode): # if-elif-else used for compatibility
    if mode == 0: # Wii
        get_miis_a(WII_DB, 0x4, 74, b"", WII_EPL, 100, "WII_PL")
        get_miis_a(WII_DB, 0x1F1E0, 64, WII_PPA, WII_EPA, 10_000, "WII_PA")
    elif mode == 1: # 3DS
        print("3DS not implemented")
    elif mode == 2: # Wii U
        get_miis_a(WIIU_ODB, 0x8, 92, b"", WIIU_EMA, 3_000, "WIIU_MA")
    elif mode == 3: # Switch
        print("Switch not implemented")
    else: print(f"Mode {mode} is invalid.")

if __name__ == "__main__": input("This file is a module, not a script.")