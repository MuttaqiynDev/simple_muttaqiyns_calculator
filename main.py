import tkinter as tk

root = tk.Tk()
root.title('Kalkulyator')
root.geometry('320x430')
root.resizable(False, False)

equation = tk.StringVar()

display = tk.Entry(root, textvariable=equation, font=("Arial", 20), bg="#f5f5f5", border=0, justify="right")
display.pack(fill="both", ipadx=8, ipady=15, pady=(10, 0), padx=10)

def press(num):
    '''raqamlar bosilganda ularni display qilish uchun function'''
    current = equation.get()
    equation.set(current + str(num))

def equalpress(): 
    '''= bosilganda bu function ishlaydi'''
    try:
        natija = str(eval(equation.get()))
        equation.set(natija)
    except:
        equation.set('Xato')

def clear():
    ''' c bosilganda ko'rinib turgan barcha sonlarni o'chirib yuboradi'''
    equation.set('')

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# tugmalarni yaratamiz
tugmalar = [
    ['7', '8', '9', 'c'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['0', '.', '+', '/']
]

for qator in tugmalar:
    frame_row = tk.Frame(frame)
    frame_row.pack(expand=True, fill='both')
    for tgm_matni in qator:
        tgm = tk.Button(frame_row,
            text=tgm_matni,
            font=("Arial", 18),
            height=2,
            width=5,
            bg="#f0f0f0",
            activebackground="#dcdcdc",
            command=lambda x=tgm_matni: clear() if x == 'c' else press(x))
        tgm.pack(side='left', fill="both", expand=True)

equal_tgm = tk.Button(root, text='=', font=('Arial', 18), bg='#ff5252', fg='white', height=2, width=5, command=equalpress)
equal_tgm.pack(pady=(5, 10))

root.mainloop()

