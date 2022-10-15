
#
try:
    user = int(input("Введіть розмір сторони квадрата: "))
    for i in range(user):
        for j in range(user):
            if i == 0 or i == user-1:
                print("* ", end=" ")
            else:
                if j == 0 or j == user-1:
                    print("* ", end=" ")
                else:
                    print("  ", end=" ")
        print()



except Exception as ex:
    print(ex)






