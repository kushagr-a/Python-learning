# key value pair
tea_prices_inr = {
    "Masala chai": 15,
    "Green tea": 20,
    "Black tea": 25,
    "Iced Americano": 30,
    "Green tea": 35,
    "Black tea": 40,
    "Latte": 45,
    "Dalgona Coffee": 50,
    "Cold Brew": 55
}

chai_Price_USD = {tea:price / 80  for tea, price in tea_prices_inr.items()}
print(chai_Price_USD)
