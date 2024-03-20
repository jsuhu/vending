# main.py

# Import the inventory and user_io modules
import inventory as invent
import user_io as io

# Define a main function that runs the program
def main():
   print("Welcome to the Vending Machine!")
   money = io.get_money()
   # display inventory_list
   print('Here is a list of items you can purchase:')
   for i in range(len(invent.inventory_list)):
      print(f'{i+1}. {invent.inventory_list[i]["name"]} ({invent.inventory_list[i]["price"]}) - {invent.inventory_list[i]["quantity"]} left')
   
   choice = io.get_choice(invent.inventory_list)
   product = invent.inventory_list[choice - 1]['name']
   price = invent.inventory_list[choice - 1]['price']
   print(f'You have selected a {product}. The price is ${price}.')

   if money >= price:
      change = money - price
      print(f'You have inserted ${money}. Your change is ${change}')

   # display inventory_dict
   index = 1
   for key, value in invent.inventory_dict.items():
      print(f'{index}. {key} ({value[0]}) - {value[1]} left')
      index += 1

   key_list = list(invent.inventory_dict.keys())
   value_list = list(invent.inventory_dict.values())
   product1 = key_list[choice - 1]
   price1 = value_list[choice - 1][0]
   print(f'You have selected a {product1}. The price is ${price1}.')

   if money >= price1:
      change = money - price1
      print(f'You have inserted ${money}. Your change is ${change}')

   print(f'Thank you for your purchase! Enjoy your {product1}!')

if __name__ == "__main__":
  main()