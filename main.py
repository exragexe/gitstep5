
#
z=int(input("Введіть висоту прямокутника: "))
y=int(input("Введіть ширину прямокутника: "))
for i in range(z):
    for j in range(y):
        print(f"*", end="")
    print()