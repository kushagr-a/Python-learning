chai_type = "Ginger_chai"
customer_name = "John Doe"

print(f"Hello {customer_name}, your order for {chai_type} is being prepared.")

# indexing and slicing
chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:8]}")  # Slicing the first 7 characters andf 2 is the step size
print(f"Last word: {chai_description[12:]}")  # Slicing from index 12 to the end
print(f"Reversed: {chai_description[::-1]}")