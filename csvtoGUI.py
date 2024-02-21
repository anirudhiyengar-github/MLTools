import tkinter as tk
from tkinter import filedialog
import pandas as pd
from pandastable import Table, TableModel

def load_csv_data():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        data = pd.read_csv(file_path)
        display_data(data)

def display_data(data):
    top = tk.Toplevel(root)
    top.title("CSV Data")
    frame = tk.Frame(top)
    frame.pack(fill="both", expand=True)
    model = TableModel(dataframe=data)
    table = Table(frame, model=model)
    table.show()

root = tk.Tk()
root.title("CSV to Tabular Data Converter")
root.geometry("400x200")

load_button = tk.Button(root, text="Load CSV", command=load_csv_data)
load_button.pack(pady=20)

root.mainloop()
