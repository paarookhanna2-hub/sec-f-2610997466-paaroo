 Lab 14 - Library Book Collection

# books = [
#     ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
#     ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
#     ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
#     ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
# ]

# library_categories = set()

# for book in books:
#     library_categories.add(book[3])

# student_wishlist = {
#     "AI",
#     "Cloud Computing",
#     "Robotics",
#     "Cybersecurity"
# }

# while True:
#     print("========================================")
#     print("      LIBRARY BOOK & CATEGORY MANAGER")
#     print("========================================")

#     print("Select an operation:")
#     print("1. View Cataloged Books")
#     print("2. Add New Book Record")
#     print("3. View Unique Library Categories")
#     print("4. Add Category to Student Wishlist")
#     print("5. Run Category Gap Analysis")
#     print("6. Exit")

#     choice = input("Enter your choice (1-6): ")

#     if choice == "1":
#         print("--- Current Library Catalog ---")

#         for i in range(len(books)):
#             title, author, year, category = books[i]

#             print(str(i + 1) + ".", title)
#             print("   Author:", author)
#             print("   Year:", year)
#             print("   Genre:", category)

#         print("Total Books:", len(books))

#     elif choice == "2":
#         print("--- Add New Book Record ---")

#         title = input("Enter book title: ")
#         author = input("Enter author name: ")
#         year = input("Enter publication year: ")
#         category = input("Enter category/genre: ")

#         new_book = (title, author, year, category)

#         books.append(new_book)
#         library_categories.add(category)

#         print('[SUCCESS] "' + title + '" added to the catalog.')
#         print('[INFO] Category set updated with:', category)

#     elif choice == "3":
#         print("\n--- Unique Library Categories ---")

#         for category in sorted(library_categories):
#             print("-", category)

#         print("Total Unique Genres:", len(library_categories))

#     elif choice == "4":
#         print("--- Add to Student Wishlist ---")

#         category = input("Enter requested category: ")

#         student_wishlist.add(category)

#         print('[SUCCESS] "' + category + '" added to student wishlist.')

#     elif choice == "5":
#         print("========== CATEGORY GAP ANALYSIS ==========")

#         print("Library Holdings:", library_categories)
#         print("Student Wishlist:", student_wishlist)

#         available = library_categories & student_wishlist
#         needed = student_wishlist - library_categories
#         combined = library_categories | student_wishlist

#         print("1. Already in Stock (Intersection):")
#         print(sorted(available))

#         print("2. Purchase Order Needed (Difference):")
#         print(sorted(needed))

#         print("3. Full Combined Genre Coverage (Union):")
#         print(sorted(combined))

#     elif choice == "6":
#         print("Thank you for using the Library Manager.")
#         print("Goodbye!")
#         break

#     else:
#         print("Invalid choice! Please enter a number from 1 to 6.")