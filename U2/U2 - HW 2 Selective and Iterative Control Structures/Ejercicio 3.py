# INPUT
total_accumulated = 0
while True:
    consumption_input = input("Enter consumed m3 or 'exit': ")
    if consumption_input.lower() == 'exit':
        break
    
    # PROCESS
    m3 = float(consumption_input)
    if m3 <= 10:
        charge = m3 * 8.00
    elif m3 <= 20:
        charge = m3 * 12.00
    else:
        charge = m3 * 18.00
        
    total_accumulated += charge
    
    # OUTPUT
    print(f"Month charge: ${charge:.2f} MXN — Total: ${total_accumulated:.2f} MXN")