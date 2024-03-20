# user_io.py

# A function that gets the user's input of money and validates it
def get_money():
    money = input("Please enter the amount of money you have: $")
    try:
      money = float(money)
      return money
    except Exception as e:
      return get_money()

# A function that displays the list of items and gets the user's choice of item
def get_choice(inventory):
  choice = int(input("Please enter the number of the item you wish to purchase:"))
  if choice in range(1,5):
    return choice
  else:
    print("Invalid selection, please select again (1-4):")
    return get_choice(inventory)