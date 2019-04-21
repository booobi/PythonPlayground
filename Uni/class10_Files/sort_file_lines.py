import sys

try:
    source_file_name = sys.argv[1]
    target_file_name = sys.argv[2]
except IndexError:
    print "Please supply the source and target file names as script parameters."
    raise

source_file = open(source_file_name, "r")
try:
    lines = source_file.readlines()
except:
    "Problem with opening file"
    raise
finally:
    source_file.close()

lines.sort()

target_file = open(target_file_name, "w")
try:
    target_file.writelines(lines)
finally:
    target_file.close()
