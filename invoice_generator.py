from datetime import datetime

print("=== INVOICE GENERATOR ===")

customer = input("Enter customer name: ")
item = input("Enter item name: ")
price = float(input("Enter price: "))
qty = int(input("Enter quantity: "))

total = price * qty

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

invoice = f"""
-----------------------------
        INVOICE
-----------------------------
Customer : {customer}
Item     : {item}
Price    : {price}
Qty      : {qty}
-----------------------------
TOTAL    : {total}
Date     : {date}
-----------------------------
"""

print(invoice)

# Save invoice
with open("invoice.txt", "w") as f:
    f.write(invoice)

print("Invoice generated successfully!")