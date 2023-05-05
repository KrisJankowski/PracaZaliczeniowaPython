import tkinter as tk
from tkinter import filedialog
import pandas as pd

pairs = []

# UI Headline

root = tk.Tk()
root.title('My application')
headline_name = tk.Label(root, text='Search for potential duplicates of facilities by comparing coordinates')
headline_name.grid(row=0, column=0, padx=10, pady=10)

# UI load first file

file1_dialog = tk.Label(root, text='1. Load first file:')
file1_dialog.grid(row=1, column=0, padx=10, pady=10)


def load_file1():
    file_1 = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"),))
    file1 = pd.read_excel(file_1)
    for index, row in file1.iterrows():
        global name1, lon1, lat1
        name1 = row['Name']
        lon1 = row['Longitude']
        lat1 = row['Latitude']


file1_button = tk.Button(root, text="open", command=load_file1)
file1_button.grid(row=1, column=1, padx=10, pady=10)

# UI load second file

file2_dialog = tk.Label(root, text='2. Load second file:')
file2_dialog.grid(row=2, column=0, padx=10, pady=10)


def load_file2():
    file_2 = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"),))
    file2 = pd.read_excel(file_2)
    for index, row in file2.iterrows():
        global name2, lon2, lat2
        name2 = row['Name']
        lon2 = row['Longitude']
        lat2 = row['Latitude']


file2_button = tk.Button(root, text="open", command=load_file2)
file2_button.grid(row=2, column=1, padx=10, pady=10)

# UI input Precision

precision_label = tk.Label(root, text="3. Provide number of digits precision:")
precision_label.grid(row=3, column=0, padx=10, pady=10)
precision = tk.Entry(root)
precision.grid(row=3, column=1, padx=10, pady=10)


# Compare

if round(lon1, precision.get()) == round(lon2, precision.get()) and \
        round(lat1, precision.get()) == round(lat2, precision.get()):
    pairs.append((name1, name2))
df = pd.DataFrame(pairs)
# UI generate file

safe_label = tk.Label(root, text="4. Generate output file:")
safe_label.grid(row=4, column=0, padx=10, pady=10)


def save_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension="*.xlsx", filetypes=(("Excel files", "*.xlsx"),))
    df.to_excel(file_path, index=False)


safe_button = tk.Button(root, text="Generate", command=save_output_file)
safe_button.grid(row=4, column=1, padx=10, pady=10)

# UI mainloop
root.mainloop()
