dishes={
    "кофе": 20.00,
    "чай": 10.00,
    "булочка": 5.00,
    "салат": 30.40,
    "пирожное": 45.50
}
x=input("блюдо: ")

for name in dishes:
    if name ==x:
        print("сумма: ", dishes[name])

