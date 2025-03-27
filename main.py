from tkinter import *
from tkinter import ttk

temperature = 0.0
current_unit = ''
requested_unit = ''

# when convert button press
def convert_button_press():
    try :
        # receive values from e1, combo_box1 and combo_box2
        temperature, current_unit, requested_unit = float(e1.get()), combo_box1.get(), combo_box2.get()
        if current_unit == 'C' and requested_unit == 'F' :
            result =  (temperature * (9/5)) + 32
        elif current_unit == 'F' and requested_unit == 'C' :
            result = (temperature - 32) * (5/9)
        elif current_unit == 'C' and requested_unit == 'K' :
            result = temperature + 273.15
        elif current_unit == 'K' and requested_unit == 'C' :
            result = temperature - 273.15
        elif current_unit == 'F' and requested_unit == 'K' :
            result = (temperature - 32) * (5/9) + 273.15
        elif current_unit == 'K' and requested_unit == 'F' :
            result = (temperature - 273.15) * (9/5) + 32
        else :
            result = "invalid"
        label_result.config(text= f" result : {result:.2f}")
    except ValueError:
        label_result.config(text= "invalid input")


# create a window
root = Tk()
root.geometry("235x200")
root.title("temperature")
# temperature
lable_1 = Label(root, text= "temperature : ").grid(row= 0, column= 0)
e1 = Entry(root)
e1.grid(row= 0, column= 1)
# current unit
label2 = Label(root, text="current unit   : ").place(x= 0, y= 30)
combo_box1 = ttk.Combobox(root, values=["F", "K", "C"], width= 5)
combo_box1.place(x= 80, y= 30)
# requested unit
label3 = Label(root, text="requested unit : ").place(x= 0, y= 60)
combo_box2 = ttk.Combobox(root, values=["F", "K", "C"], width= 5)
combo_box2.place(x= 90, y= 60)
# convert button
button1 = Button(root, text='convert', width= 30, command= convert_button_press)
button1.place(x= 6, y= 95)
# show result
label_result = Label(root, text= "result : --- ")
label_result.place(x= 70, y= 125)
# close button
button2 = Button(root, text= "Done", width= 30, command= root.destroy)
button2.place(x= 6, y=160)

root.mainloop()