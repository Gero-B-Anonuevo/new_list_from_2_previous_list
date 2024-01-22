first_list = [10, 53, 70, 90, 37]
second_list = [56, 54, 33, 11, 97]
product_list = []

for number in first_list:
    if number%2 != 0:
        product_list.append(number)

for number in second_list:
    if number%2 == 0:
        product_list.append(number)

print("Resulting list: ", product_list)