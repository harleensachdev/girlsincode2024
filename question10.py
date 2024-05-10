import shutil

with open("03LunarData.txt", "rb") as sourcefile:
    with open("AllLunarData.txt", "ab") as destinationfile:
        shutil.copyfileobj(sourcefile, destinationfile)
