

"""
This is a simple shopping list program that allows users to add items to a list and calculate the total value which staff member have added.
Author :- Divya Patel

"""
def  staff_shopping_list():
     staff_list = [] #it is a list that stores values.
     total_price =  0
     while True:
          item = input("Hello employee enter the name of the item (or type 'done' to finish) :")
          if item.lower() == 'done' :
               break
          try:
               price = float(input(f"Enter the price of '{item}': $"))
               staff_list.append((item,price))
               total_price += price
          except ValueError:
               print("Invalid price. Please enter a numeric value for the price.")

     return  staff_list,  total_price # return all the new staff information list by using user information which will inputed by staff employee
def main():
     print("Welcome to the shopping list program")
     staff_list , total_price =  staff_shopping_list()
     if  not staff_list: # condition if list empty
          print("No items were entered")
     else:     
          print("shopping list") 
          # check and print user's all information
          for item , price in staff_list:

               print("item","price:", item , price)
             
               print("total_cost.", total_price)
           
main()
