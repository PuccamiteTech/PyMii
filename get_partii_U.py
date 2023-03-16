# By: Sr. Esteban
# This program dumps the Miis from a Wii U's "O" database.

FILE_DB = "FFL_ODB.dat"
EMPTY = b"\x00" * 92

def main():
    try: maker()
    except FileNotFoundError: input(f"{FILE_DB} is missing.")
    except PermissionError: input("This folder is read-only.")

def maker():
    counter = 0
    with open(FILE_DB, "rb") as infile:
        infile.seek(0x8) # Move to Maker Offset
        active = True
        while active:
            mii_data = infile.read(92)
            if mii_data == EMPTY or counter == 3_000: active = False
            else:
                counter += 1
                mii_name = f"MA{counter:05d}.umii"
                with open(mii_name, "wb") as outfile: outfile.write(mii_data)
    input(f"Maker Miis Saved: {counter}")

main()