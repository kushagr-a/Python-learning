# zip used to combine two list into one list of tuples and then we can iterate over it using for loop

names = ['Aman', 'Atul', 'Kushagra', "Rohit", "Ramesh", "Suresh"]

bills = [100, 200, 300, 400, 500, 600]

for name, bill in zip(names, bills):
    print(f"serving chai to {name} and bill is {bill}")