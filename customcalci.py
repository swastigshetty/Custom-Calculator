# Importing Tkinter  and customtkinter module 
from tkinter import *
import customtkinter

#  Apply 'dark' theme
customtkinter.set_appearance_mode('dark')

# Configure the size 
cal = customtkinter.CTk()
# img = PhotoImage(file='images.jpg')
# cal.iconphoto(False, img)
cal.iconbitmap("img.ico")
cal.geometry('361x354+423+159')
cal.title('Calculator')
def calcular():
    calcul = output.get('0.0', 'end')
    result = eval(calcul)
    output.delete('0.0', 'end')
    output.insert('0.0', result)

# Textbox to view the numbers
output = customtkinter.CTkTextbox(cal, width=340, height=50,corner_radius=10, border_width=5, border_color='#042940', font=(('Arial', 50)))
output.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

#Buttons
btn1 = customtkinter.CTkButton(cal,text='1', command= lambda:output.insert('end', 1), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn1.grid(row=1, column=0, padx=5, pady=5)

btn2 = customtkinter.CTkButton(cal,text='2', command= lambda:output.insert('end', 2), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn2.grid(row=1, column=1, padx=5, pady=5)

btn3 = customtkinter.CTkButton(cal,text='3', command=lambda:output.insert('end', 3), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn3.grid(row=1, column=2, padx=5, pady=5)

btn4 = customtkinter.CTkButton(cal,text='4', command=lambda:output.insert('end', 4), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn4.grid(row=2, column=0, padx=5, pady=5)

btn5 = customtkinter.CTkButton(cal,text='5', command=lambda:output.insert('end', 5), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn5.grid(row=2, column=1, padx=5, pady=5)

btn6 = customtkinter.CTkButton(cal,text='6', command=lambda:output.insert('end', 6), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn6.grid(row=2, column=2, padx=5, pady=5)

btn7 = customtkinter.CTkButton(cal,text='7', command=lambda:output.insert('end', 7), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn7.grid(row=3, column=0, padx=5, pady=5)

btn8 = customtkinter.CTkButton(cal,text='8', command=lambda:output.insert('end', 8), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn8.grid(row=3, column=1, padx=5, pady=5)

btn9 = customtkinter.CTkButton(cal,text='9', command=lambda:output.insert('end', 9), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn9.grid(row=3, column=2, padx=5, pady=5)

btn0 = customtkinter.CTkButton(cal, text='0', command= lambda:output.insert('end', 0), corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn0.grid(row=4, column=0, padx=5, pady=5)

btn_limpar = customtkinter.CTkButton(cal,text='C', command=lambda:output.delete('0.0', 'end'),fg_color="#808080",hover_color="#5A5A5A",corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_limpar.grid(row=4, column=1, padx=5, pady=5)

btn_calcular = customtkinter.CTkButton(cal,text='=', command=calcular,fg_color="#FF8C00",hover_color="#8B4000", corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_calcular.grid(row=4, column=2, padx=5, pady=5)

btn_somar = customtkinter.CTkButton(cal,text='+', command=lambda:output.insert('end', '+'),fg_color="#FF8C00",hover_color="#8B4000", corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_somar.grid(row=1, column=3, padx=5, pady=5)

btn_subtrair = customtkinter.CTkButton(cal,text='-', command=lambda:output.insert('end', '-'),fg_color="#FF8C00",hover_color="#8B4000", corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_subtrair.grid(row=2, column=3, padx=5, pady=5)

btn_multiplicar = customtkinter.CTkButton(cal,text='x', command=lambda:output.insert('end', '*'),fg_color="#FF8C00",hover_color="#8B4000", corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_multiplicar.grid(row=3, column=3, padx=5, pady=5)

btn_dividir = customtkinter.CTkButton(cal,text='/', command=lambda:output.insert('end', '/'),fg_color="#FF8C00",hover_color="#8B4000", corner_radius=20, width=80, height=55, font=(('arial', 30)))
btn_dividir.grid(row=4, column=3, padx=5, pady=5)

cal.mainloop()