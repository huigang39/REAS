def readBVH(fileName):
    with open(fileName) as f:
        lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        if lines[i].startswith("MOTION"):
            frames = int(lines[i].split(" ")[1])
            frameTime = float(lines[i].split(" ")[2])
            break
    for i in range(len(lines)):
        if lines[i].startswith("HIERARCHY"):
            break
    for i in range(len(lines)):
        if lines[i].startswith("ROOT"):
            break
    for i in range(len(lines)):
        if lines[i].startswith("MOTION"):
            break


def main(fileName):
    data = readBVH(fileName)
    data


if __name__ == "__main__":
    fileName = input("Enter the file name: ")
    main(fileName)
