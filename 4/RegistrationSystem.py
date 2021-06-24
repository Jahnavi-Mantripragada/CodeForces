database = dict()


def reg_system(name):
    if name not in database:
        database[name] = 0
        return "OK"
    database[name] += 1
    return "{}{}".format(name, database[name])


n = int(input())
for i in range(n):
    name = input()
    print(reg_system(name))
