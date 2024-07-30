import tkinter as tk
from tkinter import filedialog, messagebox

def select_file():
    file_path = filedialog.askopenfilename()
    print("selection file")

def run_program():
    print("run")
    
def graphical_window():
    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Simple File Selector")

    # Label pour afficher le fichier sélectionné
    file_label = tk.Label(root, text="No file selected")
    file_label.pack(pady=10)

    # Bouton pour sélectionner un fichier
    select_button = tk.Button(root, text="Select File", command=select_file)
    select_button.pack(pady=5)

    # Bouton pour lancer le programme
    run_button = tk.Button(root, text="Run Program", command=run_program)
    run_button.pack(pady=5)

    # Exécution de la boucle principale
    root.mainloop()