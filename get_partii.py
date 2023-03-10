# By: Sr. Esteban
# This program dumps the Miis from a Wii's database.

FILE_DB = "RFL_DB.dat"
EMPTY_PL = b"\x00" * 74
EMPTY_PA = b"\x00" * 64
PADDING = b"\x00" * 10

def main():
    try:
        counter1 = plaza()
        counter2 = parade()
        input(f"Total Miis Saved: {counter1 + counter2}")
    except FileNotFoundError: input(f"{FILE_DB} is missing.")
    except PermissionError: input("This folder is read-only.")

def plaza():
    counter = 0
    with open(FILE_DB, "rb") as infile:
        infile.seek(0x4) # Move to Plaza Offset
        active = True
        while active:
            mii_data = infile.read(74)
            if mii_data == EMPTY_PL or counter == 100: active = False
            else:
                counter += 1
                mii_name = f"PL{counter:05d}.mii"
                with open(mii_name, "wb") as outfile: outfile.write(mii_data)
    print(f"Plaza Miis Saved: {counter}")
    return counter

def parade():
    counter = 0
    with open(FILE_DB, "rb") as infile:
        infile.seek(0x1F1E0) # Move to Parade Offset
        active = True
        while active:
            mii_data = infile.read(64)
            if mii_data == EMPTY_PA or counter == 10_000: active = False
            else:
                counter += 1
                mii_name = f"PA{counter:05d}.mii"
                with open(mii_name, "wb") as outfile: outfile.write(mii_data + PADDING)
    print(f"Parade Miis Saved: {counter}")
    return counter

main()