# By: Sr. Esteban
# This program calculates and displays Mii creation times.

from os import path, scandir
from datetime import datetime, timedelta

def main():
    total_times = 0

    for entry in scandir("."):
        if entry.is_file() and not entry.name.endswith(".py") and "mii" in entry.name:
            with open(entry.name, "rb") as infile:
                try:
                    is_wii_mii = get_mode(entry.name, path.getsize(entry.name))
                    seconds = get_seconds(infile, is_wii_mii)
                    creation_time = get_datetime(seconds, is_wii_mii)
                    print(f"{entry.name}: {creation_time}")
                    total_times += 1
                except Exception as err:
                    print(err)
    
    input(f"Times Calculated: {total_times}")

def get_mode(filename, length):
    if length == 74:
        return True
    elif length == 92:
        return False
    else:
        raise ValueError(f"{filename}'s format is unknown.")

def get_seconds(file, is_wii_mii):
    MULTIPLIER = 4 if is_wii_mii else 2
    file.seek(0x18) if is_wii_mii else file.seek(0xC)
    str_id = file.read(4).hex()
    int_id = int(str_id[1:], 16)
    return int_id * MULTIPLIER

def get_datetime(seconds, is_wii_mii):
    BASE = datetime(2006, 1, 1) if is_wii_mii else datetime(2010, 1, 1)
    shift = timedelta(seconds=seconds)
    return BASE + shift

main()
