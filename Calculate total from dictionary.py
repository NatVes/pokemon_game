#q1: Create a program that stores 3 fruits and their prices in a dictionary.
#Example:apple → 2, banana → 1, orange → 3
#Then print all fruits and their prices.

fruit_prices = {
    "apple": 2,
    "banana": 1,
    "orange": 3
}
print(fruit_prices)
for fruit in fruit_prices:
    print(fruit, fruit_prices[fruit])
#{'apple': 2, 'banana': 1, 'orange': 3}
#apple 2
#banana 1
#orange 3

#q2: Using the same dictionary, calculate the total price of all fruits.
total = 0
for price in fruit_prices.values():
    total += price
print("Total price:", total)

#{'apple': 2, 'banana': 1, 'orange': 3}
#apple 2
#banana 1
#orange 3
#Total price: 6