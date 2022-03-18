if stock_price < estimated_value:
    print("Buy this stock because it is on sale!")
else:
    print("Don't buy this stock because it is too expensive right now"

    #buy_stock = stock_price < estimated_value

    is_raining = True

if is_raining:
    print("Don't forget to bring your umbrella.")
else:
    print("You will need your sunglasses today!")
#If you type a single equals sign after a new variable, 
# you’re replacing the value for that variable. But if you type 
# a double equals (==), you’re checking whether that variable 
# contains that value. Think of it this way: single equals (=) 
# replace, and double equals (==) verify.

    issue_currency = "USD"
price = 30.0

if issue_currency == "USD":
    print("The price is $", price)
else:
    print("The currency is not in USD.")
    issue_currency = "USD"
price = 30.0

if issue_currency == "USD" and price < 40.0:
    print("The price is $", price)
else:
    print("The currency is not in USD.")