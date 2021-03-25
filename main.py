import tkinter as tk
import hemming

window = tk.Tk()

window.rowconfigure([0,1,2,3,4,5,6,7,8], minsize=20, weight=1)
window.columnconfigure([0, 1, 2], minsize=20, weight=1)
window.title("Menu principal")
window.geometry("500x500")



b_hamming = tk.Button(master=window, text="Hamming",width=50, command=hemming.start, bg="grey")
b_hamming.grid(row=1,column=1)


window.mainloop()