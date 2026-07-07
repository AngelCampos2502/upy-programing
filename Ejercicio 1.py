year = int(input("Enter a year"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
 print (f"lap year {year}")
else:
 print ("Nain")
  
  
num = int(input("Ingresa un numero entero: "))
rango = 10 <= num <= 15
print (rango)
  
letra = input("Ingresa una letra:")
  vocal = letra.lower() in "aeiou"
  print (vocal)
  
  
