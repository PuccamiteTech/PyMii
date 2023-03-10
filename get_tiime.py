# By: Sr. Esteban
# This program calculates and displays a Mii's creation time.

from datetime import datetime, timedelta

def main():
    active = True
    print("\nTo exit the program, input a blank file name."
          "\nMode 0 (default) is for Wii, whereas mode 1 is for Wii U and 3DS.\n")
    while active:
        try:
            mii_data = input("Mii Data File: ").strip()
            if mii_data == "": active = False
            else:
                mode = input("Mode: ").strip()
                mii_sec = getSeconds(mii_data, mode)
                mii_creation = getDateTime(mii_sec, mode)
                print(f"Created: {mii_creation}\n")
        except FileNotFoundError: print(f"{mii_data} does not exist.\n")

def getSeconds(mii_data, mode):
    MULTIPLIER = 2 if mode == "1" else 4
    with open(mii_data, "rb") as infile:
        infile.seek(0xC) if mode == "1" else infile.seek(0x18)
        str_id = infile.read(4).hex()
    int_id = int(str_id[1:], 16)
    return int_id * MULTIPLIER

def getDateTime(mii_sec, mode):
    BASE = datetime(2010, 1, 1) if mode == "1" else datetime(2006, 1, 1)
    shift = timedelta(seconds=mii_sec)
    return BASE + shift

main()