import math

print("==============================================")
print("         ENGINEERING CALCULATION TOOL         ")
print("==============================================")

value = float(input("Enter a numerical value: "))
exponent = float(input("Enter an exponent: "))
decimal_val = float(input("Enter a decimal measurement: "))

power_result = math.pow(value, exponent)
sqrt_result = math.sqrt(value)
ceil_result = math.ceil(decimal_val)
floor_result = math.floor(decimal_val)

print("\n--- Results ---")
print(f"{'Value':<20}: {value}")
print(f"{'Exponent':<20}: {exponent}")
print(f"{'Power (pow)':<20}: {power_result}")
print(f"{'Square Root (sqrt)':<20}: {sqrt_result:.4f}")
print(f"{'Decimal Value':<20}: {decimal_val}")
print(f"{'Ceil Value':<20}: {ceil_result}")
print(f"{'Floor Value':<20}: {floor_result}")
print("==============================================")