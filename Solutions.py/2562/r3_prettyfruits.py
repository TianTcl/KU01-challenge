fruit_count = int(input())
fruit_price = 0
for specific_fruit in range(fruit_count):
    fruit_info = input()
    fruit_length = int(fruit_info.split(" ")[0])
    fruit_width = int(fruit_info.split(" ")[1])
    if fruit_length*75/100 >= fruit_width:
        fruit_price += 5
    else:
        fruit_price += 3
print(fruit_price)
#passed