 def factorial(n):
#     # Base case
#     if n == 0 or n == 1:
#         return 1
#     # Recursive step
#     return n * factorial(n - 1)

# def fibonacci(n):
#     # Base case
#     if n <= 1:
#         return n
#     # Recursive step
#     return fibonacci(n - 1) + fibonacci(n - 2)

# def main():
#     while True:
#         print("\n=== MATHEMATICS LEARNING TOOL ===")
#         print("Select an operation:")
#         print("1. Calculate Factorial")
#         print("2. Generate Fibonacci Series")
#         print("3. Exit")
        
#         choice = input("Enter choice (1-3): ").strip()
        
#         if choice == '1':
#             try:
#                 n = int(input("Enter a non-negative integer: "))
#                 if n < 0:
#                     print("[ERROR] Factorial is not defined for negative numbers.")
#                 else:
#                     result = factorial(n)
#                     print(f"[RESULT] Factorial of {n} ({n}!) = {result}")
#             except ValueError:
#                 print("[ERROR] Please enter a valid integer.")
                
#         elif choice == '2':
#             try:
#                 n_terms = int(input("Enter number of terms to generate: "))
#                 if n_terms <= 0:
#                     print("[ERROR] Please enter a positive integer for the number of terms.")
#                 else:
#                     fib_series = [fibonacci(i) for i in range(n_terms)]
#                     print(f"[RESULT] Fibonacci series ({n_terms} terms): {fib_series}")
#             except ValueError:
#                 print("[ERROR] Please enter a valid integer.")
                
#         elif choice == '3':
#             print("Thank you for using the Mathematics Learning Tool. Goodbye!")
#             break
#         else:
#             print("[ERROR] Invalid choice. Please choose 1, 2, or 3.")

# if _name_ == "_main_":
#     main()