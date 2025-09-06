import customtkinter as ctk
from core import json_manager

def btn_read_json():
    json_manager.read_json_map("test_map.json")

def init_window():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Project Pink Spawn Manager")
    app.geometry("800x600")

    btn_read = ctk.CTkButton(
        app,
        text="Read JSON",
        command=btn_read_json,
        width=140,
        height=28,
        fg_color="blue",
        text_color="white"
    )
    btn_read.pack(side="top", fill="x", padx=20, pady=20)

    app.update()
    app.mainloop()