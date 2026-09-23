# bollean

is_boiling = True
stri_count = 5;
total_actions = stri_count + is_boiling; # upcasting of boolean to integer, True is converted to 1 and False is converted to 0 
print (f"total actions: {total_actions}")

milk_present = 0;
print (f"milk present: {bool(milk_present)}") # here 0 is converted to False and any non zero value is converted to True

# logical operaton :- and(&), or(|), not(~)
water_hot = True;
tea_added = True;

can_server = water_hot and tea_added; # here and(&) operator is used to check both conditions are True or not
print (f"can server: {can_server}")

