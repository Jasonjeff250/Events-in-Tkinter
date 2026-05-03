#tkinter code for converting quantities and values between different units of measurement
from tkinter import *
from tkinter import ttk
def convert():
    try:
        value=float(entry.get())
        from_unit=from_unit_var.get()
        to_unit=to_unit_var.get()
        if from_unit=="Meters":
            if to_unit=="Kilometers":
                result=value/1000
            elif to_unit=="Feet":
                result=value*3.28084
            elif to_unit=="Inches":
                result=value*39.3701
            else:
                result=value
        elif from_unit=="Kilometers":
            if to_unit=="Meters":
                result=value*1000
            elif to_unit=="Feet":
                result=value*3280.84
            elif to_unit=="Inches":
                result=value*39370.1
            else:
                result=value
        elif from_unit=="Feet":
            if to_unit=="Meters":
                result=value/3.28084
            elif to_unit=="Kilometers":
                result=value/3280.84
            elif to_unit=="Inches":
                result=value*12
            else:
                result=value
        elif from_unit=="Inches":
            if to_unit=="Meters":
                result=value/39.3701
            elif to_unit=="Kilometers":
                result=value/39370.1
            elif to_unit=="Feet":
                result=value/12
            else:
                result=value
        output_label.config(text=f"{value} {from_unit} = {result:.4f} {to_unit}")
    except ValueError:
        output_label.config(text="Please enter a valid number.")
root=Tk()
root.title("Unit Converter")
root.geometry("400x200")
#Input field
# Unit selection
from_unit_var=StringVar(value="Meters")
to_unit_var=StringVar(value="Kilometers")
units=["Meters","Kilometers","Feet","Inches"]
entry=Entry(root).pack(pady=10)
from_unit_menu=OptionMenu(root,from_unit_var,*units).pack(pady=5)
to_unit_menu=OptionMenu(root,to_unit_var,*units).pack(pady=5)
Button(root,text="Convert",command=convert).pack(pady=10)
output_label=Label(root,text="").pack(pady=10)
root.mainloop()  