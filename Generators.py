
def get_names(fname):
    with open(fname, 'r') as file:
        lines = []
        for line in file:
            lines.append(line.rstrip("\n")) # rstrip is because we don't want \n to be read from the file
        return lines


names = get_names("Names.txt")


print(names)

-------------------------- instead -----------------------


def get_names(fname):
    with open(fname, 'r') as file:
        for line in file:
            yield line

names = get_names("Names.txt")

print(next(names))

