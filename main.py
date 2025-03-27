from tkinter import *
from tkinter import ttk

temperature = ''
current_unit = ''
requested_unit = ''

root = Tk()
root.geometry("235x150")
root.title("temperature")
# temperature
lable_1 = Label(root, text= "temperature : ").grid(row= 0, column= 0)
e1 = Entry(root).grid(row= 0, column= 1)
# current unit
label2 = Label(root, text="current unit   : ").place(x= 0, y= 30)
combo_box1 = ttk.Combobox(root, values=["F", "K", "C"], width= 5).place(x= 80, y= 30)
# requested unit
label3 = Label(root, text="requested unit : ").place(x= 0, y= 60)
combo_box2 = ttk.Combobox(root, values=["F", "K", "C"], width= 5).place(x= 90, y= 60)
# convert button
button1 = Button(root, text='convert', width= 15, command= root.destroy).place(x= 110, y= 95)
# show result
label2 = Label(root, text= "Hello").place(x= 117, y= 130)

root.mainloop()

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