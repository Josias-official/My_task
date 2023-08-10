#let's create a list call menu
menu = ['bread','thea','spaghetti','egg']
#print(menu)
#let's create a dictionary called stock which should contains value of each items
dictionary_stock = {"bread": 20,
                    "thea": 23,
                    "spaghetti": 40,
                    "egg": 90}

#let's create a dictionary called price which should contains price of each items
dictionary_price = {"bread": 150,
                    "thea": 170,
                    "spaghetti": 250,
                    "egg": 180}

# Calculate total stock worth
total_stock = 0
for item in menu:
    item_value = (dictionary_stock[item] * dictionary_price[item])
    total_stock += item_value

# Print total stock worth
print(f'The total stock worth in the cafe is ${total_stock:.2f}')