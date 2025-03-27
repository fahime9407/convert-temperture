temperature = float(input("Enter temperature : "))
current_unit = input("Enter current unit : ")
requested_unit = input("Eneter the unit you want : ")

if current_unit == 'C' and requested_unit == 'F' :
    converted_unit =  (temperature * (9/5)) + 32
elif current_unit == 'F' and requested_unit == 'C' :
    converted_unit = (temperature - 32) * (5/9)
elif current_unit == 'C' and requested_unit == 'K' :
    converted_unit = temperature + 273.15
elif current_unit == 'K' and requested_unit == 'C' :
    converted_unit = temperature - 273.15
elif current_unit == 'F' and requested_unit == 'K' :
    converted_unit = (temperature - 32) * (5/9) + 273.15
elif current_unit == 'K' and requested_unit == 'F' :
    converted_unit = (temperature - 273.15) * (9/5) + 32
else :
    converted_unit = 'invalid value!'

print(converted_unit)