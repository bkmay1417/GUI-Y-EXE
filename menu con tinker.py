import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage

def select_folder1():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder1_entry.delete(0, tk.END)
        folder1_entry.insert(0, folder_selected)

def select_folder2():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder2_entry.delete(0, tk.END)
        folder2_entry.insert(0, folder_selected)

def create_file():
    folder1 = folder1_entry.get()
    folder2 = folder2_entry.get()
    filename = filename_entry.get()
    
    if not folder1 or not folder2 or not filename:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        return
    
    try:
        file_path1 = os.path.join(folder1, filename)
        file_path2 = os.path.join(folder2, filename)
        
        with open(file_path1, 'w') as file:
            file.write("Este es un archivo creado por la aplicación.")
        
        with open(file_path2, 'w') as file:
            file.write("Este es un archivo creado por la aplicación.")
        
        messagebox.showinfo("Éxito", f"Archivo creado en:\n{file_path1}\n{file_path2}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear el archivo: {e}")

app = tk.Tk()
app.title("Crear archivo en dos carpetas")

# Determinar la ruta correcta a la imagen
if hasattr(sys, '_MEIPASS'):
    image_path = os.path.join(sys._MEIPASS, "mnm.png")
else:
    image_path = "mnm.png"  # Reemplaza con la ruta a tu imagen en el directorio de trabajo

# Cargar la imagen PNG y ajustar su tamaño
try:
    img = PhotoImage(file=image_path).subsample(5)  # Subsample a factor de 5 (50/10)
except Exception as e:
    messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")
    img = None

# Folder 1
tk.Label(app, text="Seleccionar carpeta 1:").grid(row=0, column=0, padx=10, pady=10)
folder1_entry = tk.Entry(app, width=50)
folder1_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Buscar", command=select_folder1).grid(row=0, column=2, padx=10, pady=10)

# Folder 2
tk.Label(app, text="Seleccionar carpeta 2:").grid(row=1, column=0, padx=10, pady=10)
folder2_entry = tk.Entry(app, width=50)
folder2_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(app, text="Buscar", command=select_folder2).grid(row=1, column=2, padx=10, pady=10)

# Filename
tk.Label(app, text="Nombre del archivo:").grid(row=2, column=0, padx=10, pady=10)
filename_entry = tk.Entry(app, width=50)
filename_entry.grid(row=2, column=1, padx=10, pady=10)

# Create file button
tk.Button(app, text="Crear archivo", command=create_file).grid(row=3, column=0, columnspan=3, padx=10, pady=20)

# Enlace a una página web
def open_webpage():
    import webbrowser
    webbrowser.open_new("https://www.linkedin.com/in/michael-martinez-8773ab143/")

# Contenedor para la imagen, el enlace y el texto
bottom_frame = tk.Frame(app)
bottom_frame.grid(row=4, column=0, columnspan=3, pady=10)

# Mostrar la imagen en la esquina inferior izquierda si se carga correctamente
if img:
    image_label = tk.Label(bottom_frame, image=img)
    image_label.image = img  # Guardar una referencia al objeto PhotoImage
    image_label.pack(side=tk.LEFT, padx=10)

# Enlace a una página web
link_label = tk.Label(bottom_frame, text="Pueden contactarme aquí", cursor="hand2", fg="blue")
link_label.pack(side=tk.LEFT, padx=10)
link_label.bind("<Button-1>", lambda e: open_webpage())

# Mostrar el texto "By Michael Martinez"
credit_label = tk.Label(bottom_frame, text="By Michael Martinez", font=("Arial", 10, "italic"))
credit_label.pack(side=tk.LEFT, padx=10)

app.mainloop()
