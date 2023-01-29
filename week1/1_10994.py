def add_star(stars, repeat):
    if repeat == 0:
        return stars

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

    return add_star(new_stars, repeat - 1)


def main():
    repeat = int(input())
    stars = add_star(["*"], repeat - 1)
    for star in stars:
        print(star)


if __name__ == '__main__':
    main()
