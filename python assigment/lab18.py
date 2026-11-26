# import os

# def search_keyword(filename, keyword):
#     if not os.path.exists(filename):
#         print(f"\n[ERROR] File '{filename}' not found.")
#         return
        
#     print(f"\n--- Search Results for '{keyword}' ---")
#     match_count = 0
#     keyword_lower = keyword.lower()
    
#     with open(filename, 'r') as file:
#         for line_num, line in enumerate(file, 1):
#             if keyword_lower in line.lower():
#                 print(f"Line {line_num} (1 match): {line.strip()}")
#                 match_count += 1
                
#     print(f"\n[FOUND] Total occurrences of '{keyword}': {match_count}")
#     print("---------------------------------------")

# def display_document(filename):
#     if not os.path.exists(filename):
#         print(f"\n[ERROR] File '{filename}' not found.")
#         return
        
#     print(f"\n--- Full Report Document ({filename}) ---")
#     with open(filename, 'r') as file:
#         for line_num, line in enumerate(file, 1):
#             print(f"{line_num} | {line.strip()}")
#     print("------------------------------------------")

# def main():
#     filename = "report.txt"
    
#     while True:
#         print("\n=== KEYWORD SEARCH UTILITY ===")
#         print("Select an operation:")
#         print("1. Search Keyword in Document")
#         print("2. View Full Document")
#         print("3. Exit")
        
#         choice = input("Enter choice (1-3): ").strip()
        
#         if choice == '1':
#             keyword = input("Enter keyword to search: ").strip()
#             if keyword:
#                 search_keyword(filename, keyword)
#             else:
#                 print("[ERROR] Keyword cannot be empty.")
#         elif choice == '2':
#             display_document(filename)
#         elif choice == '3':
#             print("Thank you for using Keyword Search Utility. Goodbye!")
#             break
#         else:
#             print("[ERROR] Invalid choice. Please choose 1, 2, or 3.")

# if _name_ == "_main_":
#     main()