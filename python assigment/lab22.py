# Lab 11 - Online Account Registration

# print("========================================")
# print("      ONLINE ACCOUNT REGISTRATION")
# print("========================================")

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# print("========================================")
# print("       PASSWORD VALIDATION REPORT")
# print("========================================")

# print("Username:", username)
# print("Password:", "*" * len(password))

# print("--- Validation Rules ---")

# if len(password) >= 8:
#     print("[PASS] Minimum 8 characters")
#     length_valid = True
# else:
#     print("[FAIL] Minimum 8 characters")
#     length_valid = False

# digit_valid = False

# for ch in password:
#     if ch >= '0' and ch <= '9':
#         digit_valid = True

# if digit_valid:
#     print("[PASS] At least one digit")
# else:
#     print("[FAIL] At least one digit")

# uppercase_valid = False

# for ch in password:
#     if ch >= 'A' and ch <= 'Z':
#         uppercase_valid = True

# if uppercase_valid:
#     print("[PASS] At least one uppercase letter")
# else:
#     print("[FAIL] At least one uppercase letter")

# print("--- Result ---")

# if length_valid and digit_valid and uppercase_valid:
#     print("Password is VALID!")
#     print("Account created successfully for", username + "!")
# else:
#     print("Password is INVALID")

# print("========================================")