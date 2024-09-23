
def get_names(fname):
    with open(fname, 'r') as file:
        lines = []
        for line in file:
            lines.append(line)
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

