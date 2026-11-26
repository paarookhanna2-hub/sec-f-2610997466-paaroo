#Lab 13 - Inventory Control System

# inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

# while True:
#     print("========================================")
#     print("        INVENTORY CONTROL SYSTEM")
#     print("========================================")

#     print("Select an operation:")
#     print("1. View Inventory")
#     print("2. Add Item")
#     print("3. Remove Item")
#     print("4. Sort Inventory")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     if choice == "1":
#         print("--- Current Inventory ---")

#         if len(inventory) == 0:
#             print("Inventory is empty.")
#         else:
#             for i in range(len(inventory)):
#                 print(str(i + 1) + ".", inventory[i])

#     elif choice == "2":
#         item = input("Enter item name to add: ")

#         inventory.append(item)

#         print('[SUCCESS] "' + item + '" added to inventory.')

#     elif choice == "3":
#         item = input("Enter item name to remove: ")

#         if item in inventory:
#             inventory.remove(item)
#             print('[SUCCESS] "' + item + '" removed from inventory.')
#         else:
#             print("[ERROR] Item not found in inventory.")

#     elif choice == "4":
#         inventory.sort()

#         print("[SUCCESS] Inventory sorted alphabetically.")
#         print("Updated Inventory:")

#         for i in range(len(inventory)):
#             print(str(i + 1) + ".", inventory[i])

#     elif choice == "5":
#         print("Thank you for using Inventory Control System.")
#         print("Goodbye!")
#         break

#     else:
#         print("Invalid choice! Please enter a number from 1 to 5.")