import tkinter as tk
from tkinter import filedialog
import pandas as pd

pairs = []
names1 = []
longs1 = []
lats1 = []
names2 = []
longs2 = []
lats2 = []
precision = None
dtypes = {'Name': str, 'Longitude': float, 'Latitude': float}

# UI Headline

root = tk.Tk()
root.title('Coordinates duplicate search')
headline_name = tk.Label(root, text='Search for potential duplicates of facilities by comparing coordinates')
headline_name.grid(row=0, column=0, padx=10, pady=10)

# UI load first file

file1_dialog = tk.Label(root, text='1. Load first file:')
file1_dialog.grid(row=1, column=0, padx=10, pady=10)


def load_file1():
    file_1 = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"),))
    file1 = pd.read_excel(file_1, dtype=dtypes)
    for index, row in file1.iterrows():
        names1.append(row['Name'])
        longs1.append(row['Longitude'])
        lats1.append(row['Latitude'])
    ok_message = tk.Label(root, text="OK")
    ok_message.grid(row=1, column=4, padx=10, pady=10)


file1_button = tk.Button(root, text="open", command=load_file1)
file1_button.grid(row=1, column=1, padx=10, pady=10)

# UI load second file

file2_dialog = tk.Label(root, text='2. Load second file:')
file2_dialog.grid(row=2, column=0, padx=10, pady=10)


def load_file2():
    file_2 = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"),))
    file2 = pd.read_excel(file_2, dtype=dtypes)
    for index, row in file2.iterrows():
        names2.append(row['Name'])
        longs2.append(row['Longitude'])
        lats2.append(row['Latitude'])
    ok_message = tk.Label(root, text="OK")
    ok_message.grid(row=2, column=4, padx=10, pady=10)


file2_button = tk.Button(root, text="open", command=load_file2)
file2_button.grid(row=2, column=1, padx=10, pady=10)

# UI input Precision

precision_label = tk.Label(root, text="3. Provide digits precision:")
precision_label.grid(row=3, column=0, padx=10, pady=10)


def check_precision():
    value = entry.get()
    try:
        value = int(value)
        if isinstance(value, int):
            ok_message = tk.Label(root, text="OK")  # is an int
            ok_message.grid(row=3, column=4, padx=10, pady=10)
            update_precision()
        else:
            error_message = tk.Label(root, text="!!!")  # not an int
            error_message.grid(row=3, column=4, padx=10, pady=10)
    except ValueError:
        error_message = tk.Label(root, text="!!!")  # not a number
        error_message.grid(row=3, column=4, padx=10, pady=10)


def update_precision():
    precision = entry.get()


entry = tk.Entry(root)
entry.grid(row=3, column=1, padx=10, pady=10)
entry_button = tk.Button(root, text='Update', command=check_precision)
entry_button.grid(row=3, column=2, padx=10, pady=10)

# Compare

for i in longs1:
    round(i, precision)
for i in longs2:
    round(i, precision)
for i in lats1:
    round(i, precision)
for i in lats2:
    round(i, precision)

for i in names1:
    if longs1 == longs2 and lats1 == lats2:
        pairs.append((names1, names2))

df = pd.DataFrame(pairs)


# UI generate file

safe_label = tk.Label(root, text="4. Generate output file:")
safe_label.grid(row=4, column=0, padx=10, pady=10)


def save_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension="*.xlsx", filetypes=(("Excel files", "*.xlsx"),))
    df.to_excel(file_path, index=False)
    ok_message = tk.Label(root, text="OK")
    ok_message.grid(row=4, column=4, padx=10, pady=10)


safe_button = tk.Button(root, text="Generate", command=save_output_file)
safe_button.grid(row=4, column=1, padx=10, pady=10)


# exit program
def exit_program():
    root.destroy()


safe_button = tk.Button(root, text="Exit", command=exit_program)
safe_button.grid(row=5, column=4, padx=10, pady=10)


# UI mainloop

root.mainloop()
