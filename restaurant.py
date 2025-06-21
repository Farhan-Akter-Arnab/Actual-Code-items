import tkinter as tk
from tkinter import ttk, messagebox
class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.menu.items = {
            "Meat Broth": 5,
            "Barley bread": 3,
            "Camel milk": 2,
            "Date dessert": 4,
            "Lamb kebab": 7,
            "Drinks": 1
        }
        self.exchange_root = 121.80
        self.setup_background(root)
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ttk.label(frame, text="Restaurant Order Management", font=("Times New Roman", 20, "bold")).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.menu_labels = {}
        self.menu_quantities = {}
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame, text=f"{item} (${price}):", font=("Times New Roman", 12))
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry
            self.currency_var = tk.StringVar()
            ttk.Label(frame, text="Currency: ", font=("Times New Roman", 12)).grid(row=len(self.menu_items)+1, column=0, padx=10, pady=5)
            currency_dropdown = ttk.Combobox(frame, textvariable=self.currency_var, state="readonly", width=18, values=('USD', 'BDT'))
            currency_dropdown.grid(row=len(self.menu_items)+1, column=1, padx=10, pady=5)
            currency_dropdown.current(0)
            self.currency_var.trace("w", self.update_menu_prices)
            order_button = ttk.Button(frame, text="Place Order", command=self.place_order)
            order_button.grid(row=len(self.menu_items)+2, column=0, columnspan=3, padx=10, pady=10)
            def setup_background(self, root):
                bg_width, bg_height = 824, 624
                canvas = tk.Canvas(root, width=bg_width, height=bg_height)
                canvas.pack()
                original_image = tk.PhotoImage(file="restaurant_background.png")