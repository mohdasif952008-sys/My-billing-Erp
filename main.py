import customtkinter as ctk
import sqlite3
import tkinter as tk
from tkinter import messagebox

# Theme Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ERPSystem(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Professional ERP - Integrated Dashboard")
        self.geometry("1300x850")

        # Database ko start karein
        self.init_db()

        # Layout Design
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- LEFT SIDEBAR (MENU) ---
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(self.sidebar, text="GEMINI ERP", font=("Arial", 24, "bold")).pack(pady=40)

        # Menu Buttons
        self.btn_dash = ctk.CTkButton(self.sidebar, text="DASHBOARD", command=self.show_dashboard, height=40)
        self.btn_dash.pack(pady=10, padx=20)

        self.btn_cust = ctk.CTkButton(self.sidebar, text="CUSTOMER MASTER", command=self.show_customer_master, height=40)
        self.btn_cust.pack(pady=10, padx=20)

        self.btn_exit = ctk.CTkButton(self.sidebar, text="EXIT APP", fg_color="#922b21", command=self.quit, height=40)
        self.btn_exit.pack(side="bottom", pady=20, padx=20)

        # --- RIGHT CONTENT PANEL ---
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        self.show_dashboard() # Shuruat mein Dashboard dikhayega

    def init_db(self):
        conn = sqlite3.connect('master_data.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS customers 
                      (sn INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, code TEXT, address TEXT, 
                       contact TEXT, balance TEXT, bal_type TEXT, email TEXT, firm_name TEXT, 
                       country TEXT, state TEXT, city TEXT, pincode TEXT, bank_name TEXT, 
                       bank_acc TEXT, bank_ifsc TEXT)''')
        conn.commit()
        conn.close()

    def show_dashboard(self):
        for w in self.container.winfo_children(): w.destroy()
        
        # Dashboard Heading
        ctk.CTkLabel(self.container, text="WELCOME TO ERP DASHBOARD", font=("Arial", 32, "bold")).pack(pady=40)
        
        # Simple Stats Cards
        stats_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        stats_frame.pack(fill="x", padx=50)
        
        self.create_card(stats_frame, "TOTAL CUSTOMERS", "25", "#1f538d").pack(side="left", padx=20)
        self.create_card(stats_frame, "TODAY'S SALES", "₹ 15,200", "#1e8449").pack(side="left", padx=20)

    def create_card(self, master, title, val, color):
        card = ctk.CTkFrame(master, width=280, height=160, fg_color=color, corner_radius=15)
        card.pack_propagate(False)
        ctk.CTkLabel(card, text=title, font=("Arial", 16)).pack(pady=(30, 5))
        ctk.CTkLabel(card, text=val, font=("Arial", 28, "bold")).pack()
        return card

    def show_customer_master(self):
        # Yahan par Dashboard ke andar Customer Master load hoga
        for w in self.container.winfo_children(): w.destroy()
        
        ctk.CTkLabel(self.container, text="CUSTOMER MASTER", font=("Arial", 26, "bold")).pack(pady=10)
        
        # Simple button to confirm navigation
        ctk.CTkButton(self.container, text="+ ADD CUSTOMER", command=lambda: messagebox.showinfo("Alert", "Form Coming Soon!")).pack(pady=20)
        ctk.CTkLabel(self.container, text="(Yahan aapki customer list aur form aayega)").pack()

if __name__ == "__main__":
    app = ERPSystem()
    app.mainloop()