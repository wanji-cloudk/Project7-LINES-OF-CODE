import sys
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line argument")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line argument")
    file_name = sys.argv[1]
    if not file_name.endswith(".py"):
        sys.exit("Not a python file")
    line_count = get_lines(file_name)
    print(f"{line_count}")

def get_lines(file):
    try:
        file = open(file)
        lines = file.readlines()
        return line_count(lines)
    except FileNotFoundError:
        sys.exit("file does not exist")

def line_count(lines):
    new_lines = []
    for line in lines:
        clean_line = line.strip()
        if clean_line.lstrip() == "":
            continue
        elif clean_line.startswith("#"):
            continue
        else:
            new_lines.append(clean_line)
    return len(new_lines)

if __name__ == "__main__":
    main()

