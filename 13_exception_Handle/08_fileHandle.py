# Here we are seeing about how to handle the error related to file operations

# used for opening the file or creating the file
# file = open("text.txt", "w", encoding="utf-8")

# try:
#     file.write("Masala chai 2- cups 40₹\n")
#     file.write("Ginger chai 2- cups 30₹\n")
#     file.write("Elachi chai 2- cups 20₹\n")
# finally:
#     file.close() --> file.__exit__ -> call automatically

# another way
with open("text.txt", "w", encoding="utf-8") as file:
    file.write("Masala chai 2- cups 40₹\n")
