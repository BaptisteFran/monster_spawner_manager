import customtkinter as ctk
from core import json_manager

def btn_read_json():
    json_manager.read_json_map("test_map.json")

def init_window():
    app = ctk.CTk()
    app.title("Project Pink Spawn Manager")
    app.geometry("800x600")
    app.grid_columnconfigure(0, weight=1)

    btn_read = ctk.CTkButton(app, text="Read JSON", command=btn_read_json)
    btn_read.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

    app.mainloop()
