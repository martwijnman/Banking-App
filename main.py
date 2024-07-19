from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
import pandas as pd
import os

# Sample CSV filename
csv_filename = "data.csv"
if os.path.exists(csv_filename):
    dataFrame = pd.read_csv(csv_filename)
    dataset = dataFrame.values.tolist()
else:
    dataset = []
# Function to write data to CSV file
def write_to_csv(data):
    file_exists = os.path.isfile(csv_filename)
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Product", "Code", "Price", "DebitCredit"])
        writer.writerow(data)


csvFile = open("data.txt", "r")
reader = csv.DictReader(csvFile)
dataset2 = list(reader)

bgcolor = "#1c1c1c"  # Background color
fgcolor = "#ffffff"  # Text color
buttonbg = "#007acc"  # Button background color
buttonfg = "#ffffff"  # Button text color






root = Tk()
root.title("Login UI")
root.geometry("400x300")
root.configure(bg=bgcolor)
loginframe = tk.Frame(root, bg=bgcolor)
loginframe.pack(expand=True, pady=20)
header = tk.Label(loginframe, text="Accountancy Login", fg=fgcolor, bg=bgcolor,font=("Arial", 24, "bold"))
header.pack(pady=20)
name = tk.Label(loginframe, text="Name:", bg=bgcolor, fg=fgcolor)
name.pack(pady=5)
UIname = Entry(loginframe)
UIname.pack()
passwordLabel = tk.Label(loginframe, text="Password:", bg=bgcolor, fg=fgcolor)
passwordLabel.pack(pady=5)

UIpassword = Entry(loginframe)
UIpassword.pack()

def loginUI():
    username = UIname.get()
    password = UIpassword.get()
    if username == "jack" and password == "hoi":
        messagebox.showinfo("Login Status", "Login succeeded")
        showNewPage()
    else:
        messagebox.showerror("Login Status", "Invalid credentials")
def showNewPage():

    def addListFile():
        def addListProduct():
            nextpage2frame.pack_forget()
            showNewPage()
            UIlist = (UIproduct.get(), float(UIprice.get()), UIcode.get(), "Debit")
            dataset.append(UIlist)
            write_to_csv(UIlist)

        nextpageframe.pack_forget()
        nextpage2frame = ttk.Frame(root)
        nextpage2frame.pack(expand=True, fill="both")
        name = tk.Label(nextpage2frame, text="Name:", bg=bgcolor, fg=fgcolor)
        name.pack(pady=5)
        UIproduct = Entry(nextpage2frame)
        UIproduct.pack()
        price = tk.Label(nextpage2frame, text="Price:", bg=bgcolor, fg=fgcolor)
        price.pack(pady=5)
        UIprice = Entry(nextpage2frame)
        UIprice.pack()
        code = tk.Label(nextpage2frame, text="Code:", bg=bgcolor, fg=fgcolor)
        code.pack(pady=5)
        UIcode = Entry(nextpage2frame)
        UIcode.pack()
        removebutton = ttk.Button(nextpage2frame, text="add new product", command=addListProduct)
        removebutton.pack(pady=20)
    def removeListFile():
        def addListProduct():
            nextpage2frame.pack_forget()
            showNewPage()
            UIlist = (UIproduct.get(), -float(UIprice.get()), UIcode.get(), "Credit")
            dataset.append(UIlist)
            write_to_csv(UIlist)

        nextpageframe.pack_forget()
        nextpage2frame = ttk.Frame(root)
        nextpage2frame.pack(expand=True, fill="both")
        name = tk.Label(nextpage2frame, text="Name:", bg=bgcolor, fg=fgcolor)
        name.pack(pady=5)
        UIproduct = Entry(nextpage2frame)
        UIproduct.pack()
        price = tk.Label(nextpage2frame, text="Price:", bg=bgcolor, fg=fgcolor)
        price.pack(pady=5)
        UIprice = Entry(nextpage2frame)
        UIprice.pack()
        code = tk.Label(nextpage2frame, text="Code:", bg=bgcolor, fg=fgcolor)
        code.pack(pady=5)
        UIcode = Entry(nextpage2frame)
        UIcode.pack()
        name = tk.Label(nextpage2frame, text="Name:", bg=bgcolor, fg=fgcolor)
        removebutton = ttk.Button(nextpage2frame, text="add new product", command=addListProduct)
        removebutton.pack(pady=20)

    loginframe.pack_forget()
    nextpageframe = ttk.Frame(root)
    nextpageframe.pack(expand=True, fill="both")

    # Define the columns, including 'DebitCredit'
    columns = ("Product", "Code", "Price", "DebitCredit")

    # Create the Treeview
    tree = ttk.Treeview(nextpageframe, columns=columns, show="headings")

    # Define the column headers
    tree.heading("Product", text="Product")
    tree.heading("Code", text="Code")
    tree.heading("Price", text="Price")
    tree.heading("DebitCredit", text="DebitCredit")

    # Add the Treeview to the frame and make it expandable
    tree.pack(expand=True, fill="both")

    # Add a vertical scrollbar to the Treeview
    scrollbar = ttk.Scrollbar(nextpageframe, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Add data to the Treeview
    data = [
        ("ijsje", "fkdj1", 2.2, "Credit"),
        ("tshirt", "ts134", 900.30, "Credit"),
        ("stocks", "et322", 3000.30, "Credit")
    ]

    # Ensure each row is inserted correctly
    #for product, code, price, debit_credit in dataset:
     #   print(f"Inserting row: {product, code, price, debit_credit}")  # Debugging statement
      #  tree.insert("", "end", values=(product, code, price, debit_credit))

    def refreshtreeview():

        # Clear the existing items in the Treeview
        for item in tree.get_children():
            tree.delete(item)
        # Insert items from dataset into the Treeview
        for product, code, price, debitcredit in dataset:
            tree.insert("", "end", values=(product, code, price, debitcredit))

    refreshtreeview()

    #dataFrame = pd.read_csv("data.csv")
    #for _, row in dataFrame.iterrows():
     #   tree.insert("", "end", values=(row["Product"], row["Code"], row["Price"], row["DebitCredit"]))
        # Add buttons to the frame
    addbutton = ttk.Button(nextpageframe, text="Add Data Page", command=addListFile)
    addbutton.pack(pady=20)

    removebutton = ttk.Button(nextpageframe, text="Remove Data Page", command=removeListFile)
    removebutton.pack(pady=20)












login = Button(loginframe, text="login", padx=42, command=loginUI, bg=buttonbg, fg=buttonfg, font=("Arial", 10, "bold"))

login.pack(pady=10)




root.mainloop()