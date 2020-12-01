
######################################################################
# Part 1

# Read the file contents to a string
expense_file = open("elves_expense_report.txt", "r")
content = expense_file.read()
expense_file.close()

# Split each line into a separate entry and convert to int
expenses = [int(entry) for entry in content.split("\n")]
 
first = 0
second = 0
product = 0

# Iterate through the list for each item and check if the sum is 2020
# for two entries in the list
# Calculate the product of these two items.
for i in range(len(expenses)):
    for j in range(len(expenses[i:])):
        if expenses[i]+expenses[j] == 2020:
            first = expenses[i]
            second = expenses[j]
            product = first * second  

print(f"{first} * {second} = {product}")
print(f"{first} + {second} = {first+second}")

######################################################################
# Part 2

# Read the file contents to a string
expense_file = open("elves_expense_report.txt", "r")
content = expense_file.read()
expense_file.close()

# Split each line into a separate entry and convert to int
expenses = [int(entry) for entry in content.split("\n")]
 
first = 0
second = 0
third = 0
product = 0

# Iterate through the list for each item and check if the sum is 2020
# for three entries in the list
# Calculate the product of these three items.
for i in range(len(expenses)):
    for j in range(i,len(expenses)):
        for k in range(j, len(expenses)):    
            if expenses[i]+expenses[j]+expenses[k] == 2020:
                first = expenses[i]
                second = expenses[j]
                third = expenses[k]
                product = first * second * third  

print(f"{first} * {second} * {third} = {product}")
print(f"{first} + {second} + {third} = {first+second+third}")

######################################################################