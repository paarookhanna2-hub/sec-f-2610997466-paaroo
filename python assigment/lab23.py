# School Result Processing

# print("==============================================")
# print("#          SCHOOL RESULT PROCESSING")
# print("==============================================")

# name = input("Enter Student Name: ")
# roll_no = input("Enter Roll Number: ")

# print("--- Enter Marks for 5 Subjects (0-100) ---")

# total = 0
# failed = False

# for i in range(1, 6):
#     marks = float(input("Enter marks for Subject " + str(i) + ": "))

#     if marks < 0 or marks > 100:
#         print("Invalid marks! Marks must be between 0 and 100.")
#         exit()

#     total = total + marks

#     if marks < 40:
#         failed = True

# percentage = (total / 500) * 100

# if failed == True:
#     result = "FAIL"
#     grade = "F"
#     remark = "Failed in one or more subjects"

# elif percentage >= 90:
#     result = "PASS"
#     grade = "A+"
#     remark = "Outstanding"

# elif percentage >= 80:
#     result = "PASS"
#     grade = "A"
#     remark = "Excellent"

# elif percentage >= 70:
#     result = "PASS"
#     grade = "B"
#     remark = "Very Good"

# elif percentage >= 60:
#     result = "PASS"
#     grade = "C"
#     remark = "Good"

# elif percentage >= 50:
#     result = "PASS"
#     grade = "D"
#     remark = "Satisfactory"

# elif percentage >= 40:
#     result = "PASS"
#     grade = "E"
#     remark = "Pass"

# else:
#     result = "FAIL"
#     grade = "F"
#     remark = "Fail"

# print("==============================================")
# print("             STUDENT REPORT CARD")
# print("==============================================")

# print("Student Name :", name)
# print("Roll Number  :", roll_no)

# print("----------------------------------------------")
# print("Total Marks  :", total, "/ 500")
# print("Percentage   :", round(percentage, 2), "%")
# print("Result       :", result)
# print("Grade        :", grade)
# print("Remarks      :", remark)

# print("==============================================")