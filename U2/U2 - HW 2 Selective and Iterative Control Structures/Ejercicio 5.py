# INPUT
total_shipping = 0
while True:
    weight_input = input("Enter package weight (kg) or 'exit': ")
    if weight_input.lower() == 'exit':
        break
    
    weight = float(weight_input)
    distance = float(input("Enter distance (km): "))
    
    # PROCESS
    if distance <= 100:
        if weight <= 5:
            cost = 50.00
        else:
            cost = 80.00
    else:
        if weight <= 5:
            cost = 120.00
        else:
            cost = 200.00
        
    total_shipping += cost
    
    # OUTPUT
    print(f"Shipping cost: ${cost:.2f} MXN — Total: ${total_shipping:.2f} MXN")