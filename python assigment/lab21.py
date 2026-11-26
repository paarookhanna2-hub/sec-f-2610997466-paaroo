# import os

# --- Modular Function Definitions ---

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error: Division by zero!"
#     return a / b

# def modulo(a, b):
#     if b == 0:
#         return "Error: Division by zero!"
#     return a % b

# def power(base, exponent=2):
#     return base ** exponent

# def main():
#     history = []
    
#     while True:
#         print("\n=== ADVANCED MODULAR UTILITY CALCULATOR ===")
#         print("Select an operation:")
#         print("1. Addition (+)")
#         print("2. Subtraction (-)")
#         print("3. Multiplication (*)")
#         print("4. Division (/)")
#         print("5. Modulo / Remainder (%)")
#         print("6. Power / Exponentiation (Default: exponent=2)")
#         print("7. View Calculation History")
#         print("8. Exit")
        
#         choice = input("Enter your choice (1-8): ").strip()
        
#         if choice == '8':
#             print("Thank you for using the Utility Calculator. Goodbye!")
#             break
            
#         elif choice == '7':
#             print("\n--- Calculation History ---")
#             if not history:
#                 print("No calculations performed yet.")
#             else:
#                 for record in history:
#                     print(record)
#             print("---------------------------")
#             continue
            
#         elif choice in ['1', '2', '3', '4', '5', '6']:
#             try:
#                 first_num = float(input("Enter first number: "))
                
#                 if choice == '6':
#                     exp_input = input("Enter exponent (press Enter for default 2): ").strip()
#                     if exp_input == "":
#                         result = power(first_num)
#                         op_str = f"{first_num} ** 2 = {result}"
#                     else:
#                         exponent = float(exp_input)
#                         result = power(first_num, exponent)
#                         op_str = f"{first_num} ** {exponent} = {result}"
#                 else:
#                     second_num = float(input("Enter second number: "))
                    
#                     if choice == '1':
#                         result = add(first_num, second_num)
#                         op_str = f"{first_num} + {second_num} = {result}"
#                     elif choice == '2':
#                         result = subtract(first_num, second_num)
#                         op_str = f"{first_num} - {second_num} = {result}"
#                     elif choice == '3':
#                         result = multiply(first_num, second_num)
#                         op_str = f"{first_num} * {second_num} = {result}"
#                     elif choice == '4':
#                         result = divide(first_num, second_num)
#                         op_str = f"{first_num} / {second_num} = {result}"
#                     elif choice == '5':
#                         result = modulo(first_num, second_num)
#                         op_str = f"{first_num} % {second_num} = {result}"
                
#                 print(f"[RESULT] {op_str}")
#                 history.append(op_str)
                
#             except ValueError:
#                 print("[ERROR] Invalid numeric input. Please enter valid numbers.")
#         else:
#             print("[ERROR] Invalid choice. Please select an option between 1 and 8.")

# if _name_ == "_main_":
#     main()