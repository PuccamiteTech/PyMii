# By: Sr. Esteban
# This module defines common PyMii functions.

def get_miis(source, offset, size, padding, empty, limit, prefix):
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

if __name__ == "__main__": input("This file is a module, not a script.")