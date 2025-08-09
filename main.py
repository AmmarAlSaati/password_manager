from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=logo_img)
canvas.grid(column=1, row=0, columnspan=2)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="W")
website_entry = Entry(width=45)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="W")
email_entry = Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="W")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=46)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
