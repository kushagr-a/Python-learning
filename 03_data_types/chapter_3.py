# Interger

black_tea_grm = 14;
ginger_grams = 3;

total_grams = black_tea_grm + ginger_grams;
print (f"total grams: {total_grams}") # here f used for formatting the string and {} used for variable substitution

remaining_grams = black_tea_grm - ginger_grams;
print (f"remaining grams: {remaining_grams}")

milk_liters = 7;
servings = 4; 
milk_per_serving = milk_liters / servings;
print (f"milk per serving: {milk_per_serving}")

total_tea_bags = 7;
pots = 4;
bags_per_pot = total_tea_bags // pots; # here // used for floor division
print (f"bags per pot: {bags_per_pot}")

total_cadamons_pods = 10;
pods_per_cup = 3;
remaining_cadamons_pods = total_cadamons_pods % pods_per_cup; # % this is modulus operator which gives the remainder of the division
print (f"remaining cadamons pods: {remaining_cadamons_pods}");

# improve a readability
total_tea_leaves_harvested = 1_000_000_000_000; # here _ used for improving the readability of the number
print (f"total tea leaves harvested: {total_tea_leaves_harvested}")

base_flavor_strength = 2;
scale_factor = 3;
poweer_flavor_strength = base_flavor_strength ** scale_factor; # here ** used for power operation
print (f"power flavor strength: {poweer_flavor_strength}")