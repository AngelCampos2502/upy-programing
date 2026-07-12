# INPUT
grades = []
while True:
    user_input = input("Enter grade or 'done': ")
    if user_input.lower() == 'done':
        break
    # PROCESS
    grades.append(float(user_input))

# PROCESS & OUTPUT
if len(grades) == 0:
    print("No grades entered. Please enter at least one grade.")
else:
    average = sum(grades) / len(grades)
    # OUTPUT
    print(f"Average: {average:.2f} — {'Passed' if average >= 7.0 else 'Failed'}")