with open("plan_vol.txt", "r") as truc:
    l = truc.readlines()
    for ligne in range(len(l)):
        l[ligne] = l[ligne]
    print(l)