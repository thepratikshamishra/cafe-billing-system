
Menu={
"soup" : 100  ,
"chai"  : 60  ,
"fries" : 75   ,
"pizza" : 10   ,
"milkshake" : 150  , 
"juice" : 200  ,
"salad" : 500  ,
"coffee": 600  ,
"pasta" : 700  ,
"noodles": 900 ,
"water" : 200  ,
}    
print("💖welcome to my cafe💖 \n👇Here is our menu👇")

for item, price in Menu.items():
    print(f"{item:<10} {price:<6}")

name = (input("May I have your name please? :  "))
print(f"Hello,{name} Welcome to our cafe🙏🙏")

your_food = input("Please enter the food you want to eat (seperate with space) : ")
quantity = input("Enter the qty of food: ")
qty = [int(q) for q in quantity.split()]
food = your_food.split()


total_price= [Menu[item] * q for item, q in zip(food, qty) if item in Menu]
total_bill = sum(total_price)



price = [Menu[key] for key in food if key in Menu]


print()
print("Order Summary")
for s in range (0,40):
    print("-",end="")
print()   

print(f"{"Item":<10}{"Qty":<8}{"Price/item":<15}{"Total":<8}")  

for i , a, e, n, in zip (food , qty , price , total_price ):
    print(f"{i:<10}{a:<8}{e:<15}{n:<8}")
      
for s in range (0,40):
    print("-",end="")
print()   

print("Your total bill is:   ₹",total_bill)

print()

print("Thank you for choosing my cafe !! hope you enjoyed your meal😛😌 see you soon !!")