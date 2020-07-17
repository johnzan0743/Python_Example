import os
import glob


direction ='C:/Python-Example/AUXXX/Therapeutic Massage Parlours/VIC/Western Suburb/'
file_name = glob.glob(direction+'*')
new_file_name = [x.encode("ascii", "ignore") for x in file_name]
# remove all non-ASCII characters from a string

for i in range(len(file_name)):
    os.rename(file_name[i],new_file_name[i])