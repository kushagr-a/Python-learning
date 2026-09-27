def chai_flavour(flavour = "masala"):
   """This function returns the flavour of the chai."""
   return flavour

# __doc__ is called dunderdoc :- used to access the docstring of a function
print(chai_flavour.__doc__)  # Output: This function returns the flavour of the chai.
print(chai_flavour.__name__)  # Output: chai_flavour