# main.py

# Import the inventory and user_io modules
import inventory as invent
import user_io as io

# Define a main function that runs the program
def main():
   print("Welcome to the Vending Machine!")
   money = io.get_money()
   # display inventory_list
   for i in range(len(invent.inventory_list)):
      print(f'{i+1}. {invent.inventory_list[i]["name"]} ({invent.inventory_list[i]["price"]}) - {invent.inventory_list[i]["quantity"]} left')
   # display inventory_dict
   index = 1
   for key, value in invent.inventory_dict.items():
      print(f'{index}. {key} ({value[0]}) - {value[1]} left')
      index += 1

   key_list = list(invent.inventory_dict.keys())
   value_list = list(invent.inventory_dict.values())

if __name__ == "__main__":
  main()