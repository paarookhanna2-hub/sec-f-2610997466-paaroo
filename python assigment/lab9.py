# import os

# def write_notes(filename, content):
#     with open(filename, 'w') as file:
#         file.write(content)
#     print(f"[SUCCESS] Notes successfully saved to '{filename}'.")

# def read_notes(filename):
#     if not os.path.exists(filename):
#         return "No notes file found yet."
#     with open(filename, 'r') as file:
#         return file.read()

# def main():
#     filename = "notes.txt"
    
#     while True:
#         print("\n=== STUDENT NOTES MANAGEMENT SYSTEM ===")
#         print("Select an operation:")
#         print("1. Write / Save Notes")
#         print("2. View Saved Notes")
#         print("3. Exit")
        
#         choice = input("Enter choice (1-3): ").strip()
        
#         if choice == '1':
#             content = input("Enter notes to save: ")
#             write_notes(filename, content)
#         elif choice == '2':
#             content = read_notes(filename)
#             print(f"\n--- Notes Content ({filename}) ---")
#             print(content)
#             print("-----------------------------------")
#         elif choice == '3':
#             print("Thank you for using the Notes Management System. Goodbye!")
#             break
#         else:
#             print("[ERROR] Invalid choice. Please choose 1, 2, or 3.")

# if _name_ == "_main_":
#     main()