def server_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError
        else:
            print("Here is your chai")
    except ValueError:
        print("Please select a valid chai")
    finally: # it will always execute / runs
        print("I'll be back")

server_chai("ginger")
server_chai("unknown")

# Output ->
# Preparing ginger chai...
# Here is your chai
# I'll be back
# Preparing unknown chai...
# Please select a valid chai
# I'll be back