import tkinter as tk
from tkinter import ttk



root = tk.Tk()
root.geometry('600x400')

main = ttk.Frame(root)
main.pack(side='top', fill='both', expand=True)

rectangle_1 = tk.Label(main, text='Rectangle 1', bg='gray', fg='black')
rectangle_1.pack(side='top', ipadx=10, ipady=10, padx=2, fill='x')

rectangle_2 = tk.Label(main, text='Rectangle 2', bg='gray', fg='black')
rectangle_2.pack(side='left', ipadx=10, ipady=10, padx=2,fill='x')

rectangle_2 = tk.Label(main, text='Rectangle 2', bg='gray', fg='black')
rectangle_2.pack(side='left', ipadx=10, ipady=10, padx=2,fill='x')

rectangle_2 = tk.Label(main, text='Rectangle 2', bg='gray', fg='black')
rectangle_2.pack(side='left', ipadx=10, ipady=10, padx=2,fill='x')

quit_button = ttk.Button(root, text='Sair', command=root.destroy)
quit_button.pack(side='bottom', fill='both', expand=True)

root.mainloop()