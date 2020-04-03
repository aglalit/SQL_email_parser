import os
import re

if not os.path.exists("/Users/marat/Desktop/output.txt"):
    os.mknod("/Users/marat/Desktop/output.txt")

output_file = open("/Users/marat/Desktop/output.txt", "w")
file = open("/Users/marat/Desktop/School_of_advanced_studies_2020_03_13_1584079498_78019a3_wpdb.sql", "r")
file_opened = file.read()

match = re.findall(r'mailto:[\w\.-]+@[\w\.-]+\.\w+', file_opened)
stripped = [x[7:] for x in match]

print(stripped)

output_file.write('\n'.join(stripped))

file.close()
output_file.close()
