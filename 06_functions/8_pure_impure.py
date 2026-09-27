# Types of functions in Python
# Pure Vs Impure Functions
# Recursive Functions
# Lambdas (Anonymous Functions)

# Pure functions are those functions that do not have any side effects and always produce the same output for the same input. They do not modify any external state or variables.
def pure_chai(cups):
    return cups * 10

total_chai = 0


#  not recommended
def impure_chai(cups):
    global total_chai  # referring to the global variable
    total_chai += cups * 10  # updating the global variable

# A function called itself is called a recursive function
def pour_chai(n):
    print(f"Pouring chai for cup {n}")
    if n == 0:
        return "No chai left"
    return pour_chai(n - 1) + "Pouring chai\n"  # recursive function calling itself

print(pour_chai(5))  # Output: Pouring chai\nPouring chai\nPouring chai\nPouring chai\nPouring chai\nNo chai left


# Lambda functions are anonymous functions that can have any number of arguments but only one expression. They are often used for short, simple functions that are not reused elsewhere in the code.
chai_types = ["light", "medium", "strong"]

strong_chai = list(filter(lambda chai: chai == "strong", chai_types))  # using lambda function to filter strong chai
print(strong_chai)  # Output: ['strong']