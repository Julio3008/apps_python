import customtkinter 
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root=customtkinter.CTk()
root.geometry('350x300')
def login():
    print("Bienvenido")

frame=customtkinter.CTkFrame(master=root)

frame.pack(pady=20,padx=60,fill="both",expand=True)

label=customtkinter.CTkLabel(master=frame,text="Login")
label.pack(pady=12,padx=10)
entry1=customtkinter.CTkEntry(master=frame,placeholder_text="Usuario")
entry1.pack(pady=12,padx=10)

entry2=customtkinter.CTkEntry(master=frame,placeholder_text="Contraseña", show="*")
entry2.pack(pady=12,padx=10)

button=customtkinter.CTkButton(master=frame,text="Login",command=login)
button.pack(pady=12,padx=10)

root.mainloop()