# this is mutable data type
# mutable data types are those data types whose value can be changed after they are created.

spice_mix = set()
print (f"initial spice mix id: {id(spice_mix)}")

spice_mix.add("cumin")
print (f"spice mix after adding cumin id: {id(spice_mix)}")