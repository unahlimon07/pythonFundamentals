

# product name, category, price, quantity sold for the month of June, quantity sold for the month of July
data = [
    {"item": "Fish", "category": "Food", "subcategory": "Seafood", "price": 120, "qt_sold_june": 400, "qt_sold_july": 425},
    {"item": "Beef", "category": "Food", "subcategory": "Meat", "price": 400, "qt_sold_june": 250, "qt_sold_july": 300},
    {"item": "Egg", "category": "Food", "subcategory": "Dairy & Eggs", "price": 10, "qt_sold_june": 4125, "qt_sold_july": 4500},
    {"item": "Chicken", "category": "Food", "subcategory": "Meat", "price": 220, "qt_sold_june": 350, "qt_sold_july": 300},
    {"item": "Shrimp", "category": "Food", "subcategory": "Seafood", "price": 300, "qt_sold_june": 180, "qt_sold_july": 150},
    {"item": "Canned Tuna", "category": "Food", "subcategory": "Packaged", "price": 90, "qt_sold_june": 200, "qt_sold_july": 180},
    {"item": "Instant Noodles", "category": "Food", "subcategory": "Packaged", "price": 20, "qt_sold_june": 500, "qt_sold_july": 470},
    {"item": "Milk", "category": "Food", "subcategory": "Dairy & Eggs", "price": 90, "qt_sold_june": 500, "qt_sold_july": 450},
    {"item": "Cheese", "category": "Food", "subcategory": "Dairy & Eggs", "price": 150, "qt_sold_june": 200, "qt_sold_july": 175},
    {"item": "Apple", "category": "Food", "subcategory": "Fruits", "price": 35, "qt_sold_june": 600, "qt_sold_july": 520},
    {"item": "Banana", "category": "Food", "subcategory": "Fruits", "price": 20, "qt_sold_june": 700, "qt_sold_july": 650},
    {"item": "Carrot", "category": "Food", "subcategory": "Vegetables", "price": 25, "qt_sold_june": 550, "qt_sold_july": 490},
    {"item": "Pen", "category": "Non-Food", "subcategory": "Stationery", "price": 20, "qt_sold_june": 312, "qt_sold_july": 401},
    {"item": "Eraser", "category": "Non-Food", "subcategory": "Stationery", "price": 5, "qt_sold_june": 252, "qt_sold_july": 201},
    {"item": "Sharpener", "category": "Non-Food", "subcategory": "Stationery", "price": 10, "qt_sold_june": 372, "qt_sold_july": 297},
    {"item": "Notebook", "category": "Non-Food", "subcategory": "Stationery", "price": 45, "qt_sold_june": 200, "qt_sold_july": 180},
    {"item": "Stapler", "category": "Non-Food", "subcategory": "Office Supplies", "price": 120, "qt_sold_june": 80, "qt_sold_july": 60},
    {"item": "Tape", "category": "Non-Food", "subcategory": "Office Supplies", "price": 35, "qt_sold_june": 150, "qt_sold_july": 120},
    {"item": "Plastic Cup", "category": "Non-Food", "subcategory": "Household", "price": 15, "qt_sold_june": 500, "qt_sold_july": 420},
    {"item": "Dish Soap", "category": "Non-Food", "subcategory": "Household", "price": 75, "qt_sold_june": 220, "qt_sold_july": 200},
    {"item": "Broom", "category": "Non-Food", "subcategory": "Household", "price": 180, "qt_sold_june": 90, "qt_sold_july": 70},
    {"item": "Light Bulb", "category": "Non-Food", "subcategory": "Electrical", "price": 60, "qt_sold_june": 140, "qt_sold_july": 110},
    {"item": "Paper Plates", "category": "Non-Food", "subcategory": "Packaged", "price": 45, "qt_sold_june": 300, "qt_sold_july": 250},
    {"item": "Plastic Cups", "category": "Non-Food", "subcategory": "Packaged", "price": 35, "qt_sold_june": 280, "qt_sold_july": 210}
]



# [1] Item 1
# loop through data and print the names part only all caps
print('-----------------[1]------------------')

#type code here





# Expected output:

# FISH
# BEEF
# EGG
# CHICKEN
# SHRIMP
# CANNED TUNA
# INSTANT NOODLES
# MILK
# CHEESE
# ...










# [2] Item 2
print('-----------------[2]------------------')
# print only food products with their price

#type code here





# Expected output:

# Fish :  120
# Beef :  400
# Egg :  10
# Chicken :  220
# Shrimp :  300
# Canned Tuna :  90
# Instant Noodles :  20
# Milk :  90
# Cheese :  150
# Apple :  35
# Banana :  20
# Carrot :  25






# [3] Item 3
print('-----------------[3]------------------')
# print only 'Food' and 'Packaged' products with their price

#type code here





# Expected output:

# Canned Tuna :  90
# Instant Noodles :  20






# [4] Item 4
# print all unique categories in the data
print('-----------------[4]------------------')
set1 = set()

# dont brute force it by hardcoding the categories. use set to get unique categories
# use for loop to loop through data and add category to set
# use for loop to loop through set and print each category







# Expected output:
# Non-Food
# Food





print('-----------------[5]------------------')
# total sales for the month of June of food products. (price * qt_sold_june)
total_sales_june = 0

for item in data:
    pass


print(total_sales_june)


# Expected output:
# 472000