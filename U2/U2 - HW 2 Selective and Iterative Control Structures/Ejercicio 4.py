# INPUT / PROCESS
while True:
    month_input = input("Enter month number (1-12) or 'exit': ")
    if month_input.lower() == 'exit':
        break
    
    # PROCESS
    month = int(month_input)
    if month < 1 or month > 12:
        print("Invalid month. Please enter a number between 1 and 12.")
        continue
        
    if month in [12, 1, 2]:
        season = "Winter"
    elif month in [3, 4, 5]:
        season = "Spring"
    elif month in [6, 7, 8]:
        season = "Summer"
    else:
        season = "Fall"
        
    # OUTPUT
    print(season)