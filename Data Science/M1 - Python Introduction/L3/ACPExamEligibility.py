total_days = int(input("Enter total number of working days: "))
absent_days = int(input("Enter total number of days absent: "))

# Calculating days attended
attended_days = total_days - absent_days

# Calculating percentage
percentage = (attended_days / total_days) * 100

print(f"\nTotal Attendance: {percentage:.2f}%")

# Eligibility check
if percentage >= 75:
    print("Status: Eligible. The student is allowed to sit in the exam.")
else:
    print("Status: Ineligible. The student cannot sit in the exam due to low attendance.")