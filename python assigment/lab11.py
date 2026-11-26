#Delete Record & Exit

# def main_part_c():
#     # Sample dictionary for standalone testing of Part C
#     students = {
#         "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
#         "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": "1", "Marks": [74, 80, 82]}
#     }

#     while True:
#         print("\n--- Part C Menu ---")
#         print("6. Delete Student Record")
#         print("7. Exit")
#         choice = input("Enter choice (6 or 7): ").strip()

#         if choice == "6":
#             roll = input("Enter Roll Number to delete: ").strip()
#             # Safely remove record using pop with a default value of None
#             removed = students.pop(roll, None)
#             if removed:
#                 print(f"\n[SUCCESS] Record for '{removed['Name']}' (Roll No: {roll}) deleted successfully.")
#             else:
#                 print(f"\n[ERROR] Student with Roll No {roll} not found.")

#         elif choice == "7":
#             print("\nThank you for using Student Information System. Goodbye!")
#             break
#         else:
#             print("\n[ERROR] Invalid choice! Please enter 6 or 7.")

# if _name_ == "_main_":
#     main_part_c()