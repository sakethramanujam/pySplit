import sys

filename = sys.argv[1]
lines_per_file = sys.argv[2]

def splitter(filename,lines_per_file):
    lines_per_file = int(lines_per_file)
    file = open(filename)
    smallfile = None
    for lineno, line in enumerate(file):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = filename[:-4]+'-part-{}.txt'.format(int((lineno + lines_per_file)/lines_per_file))
            smallfile = open(small_filename, "w")
            print("Writing",small_filename)
        smallfile.write(line)
    if smallfile:
        smallfile.close()

splitter(filename,lines_per_file)
