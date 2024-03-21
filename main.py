from tkinter import *
import pandas as pd
from tkinter import messagebox
# import os

mini_font = ("arail", 16, "bold")


def delete_product_function(product_name, view_window):
    df = pd.read_excel('products.xlsx')

    # Delete the row from the dataframe
    df = df[df['Name'] != product_name]

    # Update the Excel file with the modified dataframe
    df.to_excel('products.xlsx', index=False)

    # Optionally, you can provide feedback to the user
    messagebox.showinfo("Success", f"Product with Name: {product_name} deleted successfully.")

    view_window.destroy()


# name, price, product description, qrcode, trader, company name, weight, expiration date, production date,........


def view_product_function(product_index, product_name, product_price, view_window):
    # You can implement the logic to delete the product with the given ID from the dataframe or database
    # For demonstration purposes, let's assume you have a dataframe 'df' and you want to delete a row with the given ID
    df = pd.read_excel('products.xlsx')
    product_old_name = ''
    for index, row in df.iterrows():
        if index == product_index:
            product_old_name = row['Name']

    # Delete the row from the dataframe
    df = df[df['Name'] != product_old_name]

    df.loc[len(df)] = [product_name, product_price]

    df.to_excel('products.xlsx', index=False)

    # Optionally, you can provide feedback to the user
    messagebox.showinfo("Success", f"Product at index: {product_index} Updated successfully.")

    # Optionally, you can update the view window or close it after deletion
    # For example, you can update a listbox or tree view widget displaying the products
    # or you can simply close the window
    view_window.destroy()


def view_btn_pressed():
    print("View Button Pressed")
    view_window = Tk()
    view_window.geometry("700x650+350+0")
    mini_window.configure(bg="#362657")

    df = pd.read_excel('products.xlsx')

    delete_label = Label(view_window, text="Item to Delete", font=mini_font)
    delete_label.place(x=100, y=25)
    delete_text = Text(view_window, bg="white", font=my_font)
    delete_text.place(x=280, y=20, width=220, height=50)
    delete_product_btn = Button(view_window, text="Delete", font=12, bg='red',
                                command=lambda: delete_product_function(delete_text.get("1.0", "end-1c"),
                                                                        view_window))
    delete_product_btn.place(x=550, y=20)
    #
    # update_label = Label(view_window, text="Item to update", font=mini_font)
    # update_label.place(x=0, y=60)
    # update_index = Text(view_window, bg="white", font=my_font)
    # update_index.place(x=180, y=60, width=100, height=50)
    # update_name = Text(view_window, bg="white", font=my_font)
    # update_name.place(x=300, y=60, width=200, height=50)
    # update_price = Text(view_window, bg="white", font=my_font)
    # update_price.place(x=550, y=60, width=200, height=50)
    #
    # update_product_btn = Button(view_window, text="update", font=12, bg='red',
    #                             command=lambda: view_product_function(int(update_index.get("1.0", "end-1c")),
    #                                                                     update_name.get("1.0", "end-1c"),
    #                                                                     update_price.get("1.0", "end-1c"),
    #                                                                     view_window))
    # update_product_btn.place(x=450, y=60)

    for index, row in df.iterrows():
        # print(f'Row index: {index}')
        # print(f"Row values: {row['Name']}")
        # print("Product Name: "+row['Name'], "Product price: "+str(row['Price']))
        # print(df['Name'][0])
        product_number_label = Label(view_window, text=str(index), font=mini_font)
        product_number_label.place(x=0, y=100 + 50 * index)

        product_name_label = Label(view_window, text="Product Name: " + row['Name'], font=mini_font)
        product_name_label.place(x=70, y=100 + 50 * index)

        product_price_label = Label(view_window, text="Product price: " + str(row['Price']), font=mini_font)
        product_price_label.place(x=400, y=100 + 50 * index)

    view_window.mainloop()


def add_product_function(product_name, product_price, mini_window):
    print(product_name.get("1.0", "end-1c"), product_price.get("1.0", "end-1c"))

    df = pd.read_excel('products.xlsx')

    print(df)

    # Directly assigning values to a new row
    df.loc[len(df)] = [product_name.get("1.0", "end-1c"), product_price.get("1.0", "end-1c")]
    print(df)

    df.to_excel('products.xlsx', index=False, sheet_name='Product')
    messagebox.showinfo("Success", "Product Added Successfully")
    mini_window.destroy()
    # if os.name == 'nt':  # For Windows
    #     os.system(f'start products.xlsx')


def add_btn_pressed():
    print("Add Button Pressed")
    mini_window = Tk()
    mini_window.geometry("400x400+350+70")
    mini_window.configure(bg="#362657")

    product_name_label = Label(mini_window, text="Product Name", font=mini_font)
    product_name_label.place(x=0, y=50)
    product_name = Text(mini_window, bg="white", font=mini_font)
    product_name.place(x=180, y=50, width=200, height=50)

    product_price_label = Label(mini_window, text="Product Price", font=mini_font)
    product_price_label.place(x=0, y=150)
    product_price = Text(mini_window, bg="white", font=mini_font)
    product_price.place(x=180, y=150, width=200, height=50)

    add_product = Button(mini_window, text="Add Product", font=mini_font,
                         command=lambda: add_product_function(product_name, product_price, mini_window))
    add_product.place(x=110, y=250)

    mini_window.mainloop()


window = Tk()

window.title("Store App")

window.geometry("400x400+200+20")

window.configure(bg="#4b7296")

my_font = ('arial', 28, 'bold')

add_image = PhotoImage(file="images/add-product.png")
add_image = add_image.subsample(4)
add_btn = Button(text="Add", font=my_font, compound=TOP, image=add_image, command=add_btn_pressed)
add_btn.place(x=50, y=100)

view_image = PhotoImage(file="images/view.png")
view_image = view_image.subsample(4)
view_btn = Button(text="View", font=my_font, compound=TOP, image=view_image, command=view_btn_pressed)
view_btn.place(x=230, y=130)

window.mainloop()
