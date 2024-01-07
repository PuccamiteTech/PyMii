# By: Sr. Esteban
# This program dumps Miis from supported databases.

from mii_type import MiiType

def main():
    for mii_type in MiiType:
        extract_miis(mii_type)
    
    input()

def extract_miis(mii_type):
    mii_padding = bytearray(mii_type.PADDING)
    empty_mii = bytearray(mii_type.SIZE)
    mii_count = 0
    is_active = True

    try:
        with open(mii_type.SOURCE, "rb") as infile:
            infile.seek(mii_type.OFFSET)

            while is_active:
                mii_data = infile.read(mii_type.SIZE)

                if mii_count == mii_type.LIMIT or mii_data == empty_mii:
                    is_active = False
                else:
                    mii_name = f"{mii_type.PREFIX}{mii_count:05d}.mii"

                    with open(mii_name, "wb") as outfile:
                        outfile.write(mii_data + mii_padding)
                    
                    mii_count += 1
    except FileNotFoundError:
        print(f"{mii_type.PREFIX}: {mii_type.SOURCE} is missing.")
    except PermissionError:
        print(f"{mii_type.PREFIX}: This folder is read-only.")
    finally:
        print(f"Miis Saved ({mii_type.PREFIX}): {mii_count}\n")
        return mii_count

main()
