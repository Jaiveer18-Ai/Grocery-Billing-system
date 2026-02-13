total={"Rice":50,"Sugar":50,"Oil":50,"Water bottle":50,"Maggie":50}
cart=[]
while True:
    print("=====what you want to choose:=====")
    print("1.show all products")
    print("2.Add an item to cart")
    print("3.Show Cart")
    print("4.Generate Bill")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        print("=====Available products=====")
        for items,price in total.items():
            print(items,"-",price)
    elif choice == 2:
        item = input("Enter name of the item: ").title()

        if item in total:
            cart.append(item)
            print("✅ Item added to cart")
        else:
            print("❌ Item not found!")
    elif choice == 3:
        print("=====Your cart=====")
        if cart:
            for item in cart:
                print(item)
        else:
            print("Cart is empty")
    elif choice == 4:
        if not cart:
            print("Your cart is empty mate")
        else:
            print("=====BILL=====")
            total_amount=0
        for item in cart:
            price=total[item]
            total_amount+=price
            print(f"{item} → ₹{price}")
        print("---------------------------------")
        print(f"Total Amount → ₹{total_amount}")
        print("=================================")
        break
    elif choice == 5:
        print("👋 Thank you for your patience...")
        break
    else:
        print("Invalid")
