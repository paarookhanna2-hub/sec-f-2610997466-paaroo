# import os

# def append_entry(filename, entry):
#     with open(filename, 'a') as file:
#         file.write(entry + '\n')
#     print(f"[SUCCESS] New entry logged to '{filename}'.")

# def display_log(filename):
#     if not os.path.exists(filename):
#         print("\nNo log file found yet.")
#         return
#     print("\n--- DAILY LOG BOOK ---")
#     count = 0
#     with open(filename, 'r') as file:
#         for line in file:
#             print(line.strip())
#             count += 1
#     print("----------------------")
#     print(f"Total logged entries: {count}")

# def main():
#     filename = "daily_log.txt"
    
#     while True:
#         print("\n=== OFFICE DAILY LOG BOOK ===")
#         print("Select an operation:")
#         print("1. Add Log Entry")
#         print("2. Display Complete Log")
#         print("3. Exit")
        
#         choice = input("Enter choice (1-3): ").strip()
        
#         if choice == '1':
#             entry = input("Enter log entry: ").strip()
#             if entry:
#                 append_entry(filename, entry)
#             else:
#                 print("[ERROR] Log entry cannot be empty.")
#         elif choice == '2':
#             display_log(filename)
#         elif choice == '3':
#             print("Thank you for using the Daily Log Book. Goodbye!")
#             break
#         else:
#             print("[ERROR] Invalid choice. Please choose 1, 2, or 3.")

# if _name_ == "_main_":
#     main()