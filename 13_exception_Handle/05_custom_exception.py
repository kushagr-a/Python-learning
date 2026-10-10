# this is our example of custom exception where we are raising our own exception

def bre_chai(flavor):
    if flavor not in ["masala", "ginger", "elachi"]:
        raise ValueError("Unserved chai flavor")
    else:
        print(f"here is your {flavor} chai")

try:
    bre_chai("cardmom")
except ValueError as e:
    print(e)

#output -> Unserved chai flavor
        