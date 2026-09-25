# using enumerate()

menu = ['samosa', 'chai', 'pakora', 'burger']

# printing out these numbers using enumerate() function and get back list like := [(0, 'samosa'), (1, 'chai'), (2, 'pakora'), (3, 'burger')]
for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai")