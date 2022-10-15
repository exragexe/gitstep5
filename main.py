
#
try:
    dovzh = int(input("Введіть довжину прямокутника: "))
    shir = int(input("Введіть ширину прямокутника: "))
    for i in range(dovzh):
        for j in range(shir):
            if i == 0 or i == dovzh-1:
                print("* ", end=" ")
            else:
                if j == 0 or j == shir-1:
                    print("* ", end=" ")
                else:
                    print("  ", end=" ")
        print()



except Exception as ex:
    print(ex)
