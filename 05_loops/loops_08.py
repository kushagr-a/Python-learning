# Study about for else

staff = [
    ("Aman", 22),
    ("Atul", 23),
    ("Kushagra", 24),
    ("Rohit", 15),
    ("Ramesh", 16),
    ("Suresh", 17),
]

# here fall back logics we are used
for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible for driving license")
        break
else:
    print(f"{name} is not eligible for driving license")
