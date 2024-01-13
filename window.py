import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("App GUI")

label = tk.Label(root,text="Hello World", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial',16))
textbox.pack(padx=10, pady=10)

button = tk.Button(root, text="Click me!", font=('Arial',18))
button.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial',18))

root.mainloop()
