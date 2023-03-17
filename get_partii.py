# By: Sr. Esteban
# This program dumps the Miis from a Wii's database.

FILE_DB = "RFL_DB.dat"
EMPTY_PL = b"\x00" * 74
EMPTY_PA = b"\x00" * 64
PADDING_PA = b"\x00" * 10

def main():
    try:
        plaza = getMiis(FILE_DB, 0x4, 74, b"", EMPTY_PL, 100, "PL")
        parade = getMiis(FILE_DB, 0x1F1E0, 64, PADDING_PA, EMPTY_PA, 10_000, "PA")
        input(f"Miis Saved: {plaza} + {parade} = {plaza + parade}")
    except FileNotFoundError: input(f"{FILE_DB} is missing.")
    except PermissionError: input("This folder is read-only.")

def getMiis(source, offset, size, padding, empty, limit, prefix):
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
    return counter

main()