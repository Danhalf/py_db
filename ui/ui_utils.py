# ui_utils.py
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk 
from db.db_utils import get_records, add_record  

def create_main_window(conn):
    root = tk.Tk()
    root.title("Tech Controller")
    root.geometry("1400x1000")

    tree = ttk.Treeview(root, columns=('id', 'name', 'number', 'owner', 'status', 'notes'), show='headings')
    tree.heading('id', text='ID')
    tree.heading('name', text='Tech Name')
    tree.heading('number', text='Tech Number')
    tree.heading('owner', text='Owner')
    tree.heading('status', text='Status')
    tree.heading('notes', text='Notes')

    tree.pack(fill='both', expand=True, pady=20)

    def update_table():
        for row in tree.get_children():
            tree.delete(row)
        
        records = get_records(conn)
        for record in records:
            tree.insert('', 'end', values=record)

    form_frame = tk.Frame(root)
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Tech Name").grid(row=0, column=0)
    name_entry = tk.Entry(form_frame)
    name_entry.grid(row=0, column=1)

    tk.Label(form_frame, text="Tech Number").grid(row=1, column=0)
    number_entry = tk.Entry(form_frame)
    number_entry.grid(row=1, column=1)

    tk.Label(form_frame, text="Owner").grid(row=2, column=0)
    owner_entry = tk.Entry(form_frame)
    owner_entry.grid(row=2, column=1)

    tk.Label(form_frame, text="Status").grid(row=3, column=0)
    status_entry = tk.Entry(form_frame)
    status_entry.grid(row=3, column=1)

    tk.Label(form_frame, text="Notes").grid(row=4, column=0)
    notes_entry = tk.Entry(form_frame)
    notes_entry.grid(row=4, column=1)

    def add_new_record():
        name = name_entry.get()
        number = number_entry.get()
        owner = owner_entry.get()
        status = status_entry.get()
        notes = notes_entry.get()

        add_record(conn, name, number, owner, status, notes)
        update_table() 

    add_button = tk.Button(root, text="Add Record", command=add_new_record)
    add_button.pack(pady=10)

    update_table()

    return root
