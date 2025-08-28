menu ={"Tea":20,
        "Dosa":50,
       "Idli": 30,
       "Uttapa": 50,
       "Sambar Wada": 40,
       "Pakoda":20,
       "wadapao": 15,
       "Poha":20}

cart = []
total = 0

print("---------MENU----------")
for key, value in menu.items():
     print(f"{key:12} :Rs {value: .2f}")

print("------------------------------")
while True:
    Food=input("Pls enter what would you like to have Today (Q to Quit)----").title()
    if Food == "Q" :
       break
    elif menu.get(Food) is not None :
        cart.append(Food)
    else:
        print("sorry item not available")

print("\nYou ordered:")
for Food in cart:
    total += menu.get(Food)
    print(Food, end=" ")

print(f"\nYour Total is Rs {total}")




























