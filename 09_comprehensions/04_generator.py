# generators are used for just saving the memory and processing the data when ever needed

# example 
# this is memory efficient method
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
# if someone ask me to increase the sales of each day by 10% then how to do that


total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)