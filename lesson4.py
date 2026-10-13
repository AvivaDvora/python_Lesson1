# 1

import csv


def My_reade(url):
    with open(url, "r") as file:
        text = file.read()
        c = text.count(' ')
    return c + 1


print(My_reade("a.txt"))


# 2


def My_write(people):
    with open("people.csv", "a") as file:
        writer = csv.writer(file)
        for p in people:
            writer.writerow({p[0], p[1], p[2], p[3]})


pepole = [["Aviva", "Pinski", 19, "MI"], ["Leah", "Ben horin", 20, "MI"], ["Ayala", "Pintz", 19, "MI"]]
My_write(pepole)
