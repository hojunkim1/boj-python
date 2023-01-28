def add_star(stars):
    height = len(stars)
    new_stars = []

    new_string1 = ""
    new_string2 = ""

    for _ in range(height + 4):
        new_string1 = new_string1 + "*"
    for _ in range(height + 2):
        new_string2 = new_string2 + " "

    new_stars.append(new_string1)
    new_stars.append("*" + new_string2 + "*")

    for i in range(height):
        new_string = "* " + stars[i] + " *"
        new_stars.append(new_string)

    new_stars.append("*" + new_string2 + "*")
    new_stars.append(new_string1)

    return new_stars


def star(repeat):
    new_stars = ["*"]
    for _ in range(repeat - 1):
        new_stars = add_star(new_stars)
    return new_stars


def main():
    repeat = int(input())
    stars = star(repeat)
    for s in stars:
        print(s)


if __name__ == '__main__':
    main()
