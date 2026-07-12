# INPUT / PROCESS
while True:
    weight_input = input("Enter weight (kg) or 'exit': ")
    if weight_input.lower() == 'exit':
        break
    weight = float(weight_input)
    height = float(input("Enter height (m): "))
    
    # PROCESS
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi <= 24.9:
        category = "Normal"
    elif bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"
        
    # OUTPUT
    print(f"BMI: {bmi:.2f} — {category}")