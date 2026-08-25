products = {
    101: {
        "pname": "Laptop",
        "category": "Electronics",
        "price": 55000,
        "stock": 10
    },
    102: {
        "pname": "Mouse",
        "category": "Electronics",
        "price": 800,
        "stock": 25
    },
    103: {
        "pname": "Keyboard",
        "category": "Electronics",
        "price": 1500,
        "stock": 15
    },
    104: {
        "pname": "Monitor",
        "category": "Electronics",
        "price": 12000,
        "stock": 8
    }
}

orders = {}

def add_order():
    order_id = int(input("Enter Order ID: "))
    customer_name = input("Enter Customer Name: ")

    order_product = {}

    print("AVAILABLE PRODUCTS")

    for key, value in products.items():
        if value["stock"] > 0:
            print(
                key,
                value["pname"],
                value["category"],
                value["price"],
                value["stock"]
            )

    while True:
        product_id = int(input("Enter Product ID: "))

        if product_id in products:
            print("Product found")

            quantity = int(input("Enter Quantity: "))

            if quantity <= products[product_id]["stock"]:
                order_product[product_id] = quantity
                products[product_id]["stock"] -= quantity
                print("Product added successfully")
            else:
                print("Insufficient stock")

        else:
            print("Product not found")

        choice = input("Do you want to add another product? yes/no: ")

        if choice.lower() == "no":
            break

    orders[order_id] = {
        "customer_name": customer_name,
        "products": order_product
    }

    print("Order added successfully")
              
def cancel_order():
    order_id = int(input("Enter Order ID: "))

    if order_id in orders:
        print("Order found")

        order = orders[order_id]

        for product_id, quantity in order["products"].items():
            products[product_id]["stock"] += quantity

        del orders[order_id]

        print("Order cancelled successfully")

    else:
        print("Order not found")   
      
def generate_bill():
    order_id = int(input("Enter Order ID: "))

    if order_id in orders:
        order = orders[order_id]

        print("\n----- BILL -----")
        print("Customer:", order["customer_name"])

        total = 0

        for product_id, quantity in order["products"].items():
            product = products[product_id]

            price = product["price"]
            amount = price * quantity

            print(
                product["pname"],
                "Qty:", quantity,
                "Price:", price,
                "Amount:", amount
            )

            total += amount

        print("Total:", total)

        if total > 10000:
            discount = total * 0.05
            final_amount = total - discount

            print("Discount:", discount)
            print("Final Amount:", final_amount)

        else:
            print("Final Amount:", total)

    else:
        print("Order not found")                   
        
def search_order():
    order_id = int(input("Enter Order ID: "))

    if order_id in orders:
        order = orders[order_id]

        print("Order ID:", order_id)
        print("Customer Name:", order["customer_name"])

        print("Products:")

        for product_id, quantity in order["products"].items():
            print(
                product_id,
                "-->",
                products[product_id]["pname"],
                "Quantity:",
                quantity
            )

    else:
        print("Order not found") 
        
def display_orders():

    if not orders:
        print("No orders found")
        return

    for order_id, order in orders.items():

        print("Order ID:", order_id)
        print("Customer Name:", order["customer_name"])

        print("Products:")

        for product_id, quantity in order["products"].items():
            print(
                product_id,
                "-->",
                products[product_id]["pname"],
                "Quantity:",
                quantity
            )

        print("----------------------")       
        
        
while True:

    print("\n===== ORDER MANAGEMENT SYSTEM =====")
    print("1. Add Order")
    print("2. Cancel Order")
    print("3. Generate Bill")
    print("4. Search Order")
    print("5. Display All Orders")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_order()

    elif choice == 2:
        cancel_order()

    elif choice == 3:
        generate_bill()

    elif choice == 4:
        search_order()

    elif choice == 5:
        display_orders()

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice")                