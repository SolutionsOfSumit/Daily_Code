string = """
25-Jul-2025 (11:10- 12:10)
Period Attendance
25-Jul-2025 (12:10- 13:10)
Period Attendance
17-Jul-2025 (09:00- 10:00)
Period Attendance




"""
Dates = string.split("Period Attendance")

ActualString = ""
for i in Dates:
    ActualString.append(i)

print(ActualString)