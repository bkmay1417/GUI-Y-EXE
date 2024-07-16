# GUI-Y-EXE
<div style="display: flex; align-items: center;">
    <img src="https://img.shields.io/badge/STATUS-FINALIZADO-blue" />
    <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/bkmay1417/GUI-Y-EXE"/>
</div>

Creo una Interfaz Básica con Tkinter y Convertir un Archivo .py a .exe

## Requisitos
Para ejecutar este código, necesitas tener instalado Python y la biblioteca Tkinter (que viene incluida con Python).


### Explicación Paso a Paso

1. **Importación de Bibliotecas**
    ```python
    import os
    import tkinter as tk
    from tkinter import filedialog, messagebox
    ```
    - `os`: Biblioteca estándar de Python para interactuar con el sistema operativo.
    - `tkinter`: Biblioteca para crear interfaces gráficas.
    - `filedialog`: Módulo de `tkinter` para abrir cuadros de diálogo.
    - `messagebox`: Módulo de `tkinter` para mostrar mensajes emergentes.

2. **Definición de Funciones**
    - **Función `select_folder1`**
        ```python
        def select_folder1():
            folder_selected = filedialog.askdirectory()
            if folder_selected:
                folder1_entry.delete(0, tk.END)
                folder1_entry.insert(0, folder_selected)
        ```
        - Abre un cuadro de diálogo para seleccionar una carpeta.
        - Si se selecciona una carpeta, la ruta se muestra en un cuadro de texto en la interfaz.

    - **Función `select_folder2`**
        ```python
        def select_folder2():
            folder_selected = filedialog.askdirectory()
            if folder_selected:
                folder2_entry.delete(0, tk.END)
                folder2_entry.insert(0, folder_selected)
        ```
        - Similar a `select_folder1`, pero para la segunda carpeta.

    - **Función `create_file`**
        ```python
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
        ```
        - Obtiene las rutas de las carpetas y el nombre del archivo desde los cuadros de texto.
        - Verifica que todos los campos estén completos.
        - Crea el archivo en ambas carpetas seleccionadas y escribe un texto simple en ellos.
        - Muestra un mensaje de éxito o error según corresponda.

3. **Creación de la Interfaz Gráfica**
    - **Configuración de la ventana principal**
        ```python
        app = tk.Tk()
        app.title("Crear archivo en dos carpetas")
        ```
        - Crea la ventana principal de la aplicación y establece su título.

    - **Elementos de la Interfaz**
        - **Selección de la primera carpeta**
            ```python
            tk.Label(app, text="Seleccionar carpeta 1:").grid(row=0, column=0, padx=10, pady=10)
            folder1_entry = tk.Entry(app, width=50)
            folder1_entry.grid(row=0, column=1, padx=10, pady=10)
            tk.Button(app, text="Buscar", command=select_folder1).grid(row=0, column=2, padx=10, pady=10)
            ```
            - Etiqueta: "Seleccionar carpeta 1".
            - Cuadro de texto: Para mostrar la ruta de la carpeta seleccionada.
            - Botón: Abre el cuadro de diálogo para seleccionar la primera carpeta.

        - **Selección de la segunda carpeta**
            ```python
            tk.Label(app, text="Seleccionar carpeta 2:").grid(row=1, column=0, padx=10, pady=10)
            folder2_entry = tk.Entry(app, width=50)
            folder2_entry.grid(row=1, column=1, padx=10, pady=10)
            tk.Button(app, text="Buscar", command=select_folder2).grid(row=1, column=2, padx=10, pady=10)
            ```
            - Similar a la selección de la primera carpeta, pero para la segunda carpeta.

        - **Nombre del archivo**
            ```python
            tk.Label(app, text="Nombre del archivo:").grid(row=2, column=0, padx=10, pady=10)
            filename_entry = tk.Entry(app, width=50)
            filename_entry.grid(row=2, column=1, padx=10, pady=10)
            ```
            - Etiqueta: "Nombre del archivo".
            - Cuadro de texto: Para ingresar el nombre del archivo a crear.

        - **Botón para crear el archivo**
            ```python
            tk.Button(app, text="Crear archivo", command=create_file).grid(row=3, column=0, columnspan=3, padx=10, pady=20)
            ```
            - Botón: Llama a la función `create_file` cuando se hace clic en él.

    - **Inicio del bucle principal**
        ```python
        app.mainloop()
        ```
        - Inicia el bucle principal de la aplicación, lo que permite que la interfaz gráfica permanezca abierta y funcione hasta que el usuario la cierre.

### Cómo Usar el Programa

1. Ejecuta el código en un entorno Python.
2. Aparecerá una ventana con la interfaz gráfica.
3. Haz clic en "Buscar" junto a "Seleccionar carpeta 1" para seleccionar la primera carpeta.
4. Haz clic en "Buscar" junto a "Seleccionar carpeta 2" para seleccionar la segunda carpeta.
5. Escribe el nombre del archivo en el cuadro de texto "Nombre del archivo".
6. Haz clic en "Crear archivo".
7. El programa creará el archivo en ambas carpetas seleccionadas y mostrará un mensaje de éxito.



## Explicación Paso a Paso para Convertir un Archivo .py a .exe Usando Auto Py to Exe

1. **Instalación de auto-py-to-exe**

    - Para convertir un archivo .py a .exe usaremos la herramienta auto-py-to-exe, que facilita este proceso mediante una interfaz gráfica. Primero, asegúrate de tener pip instalado y luego ejecuta el siguiente comando en tu terminal para instalar auto-py-to-exe:
       ```
        pip install auto-py-to-exe
       ```

2. **Ejecutar auto-py-to-exe**
    - Una vez instalado, ejecuta auto-py-to-exe con el siguiente comando:
      ```
      auto-py-to-exe
      ```
    - Esto abrirá la interfaz gráfica de la herramienta.

4. **Seleccionar el archivo .py**

    - En la interfaz gráfica, verás una opción para seleccionar el archivo .py que deseas convertir. Haz clic en el botón "Browse" junto a "Script Location" y selecciona tu archivo .py.
      
    - Elegir el tipo de archivo ejecutable
      
5. **Tienes dos opciones principales:**
      
    - One File: Genera un único archivo .exe. Marca esta opción si quieres un solo archivo ejecutable.
    - One Directory: Genera una carpeta con el archivo .exe y las dependencias necesarias. Elige esta opción si prefieres mantener las dependencias separadas.
      
6. **Opciones adicionales**

    - Console Window: Selecciona "Console Based" si tu programa necesita una ventana de consola para funcionar. Si no es necesario, elige "Window Based" para ocultar la consola.
    - Additional Files: Si tu script depende de otros archivos (por ejemplo, imágenes o archivos de datos), puedes incluirlos aquí. Haz clic en "Add Files" y selecciona los archivos adicionales.

7. **Configuraciones avanzadas (opcional)**

      - Icon: Puedes personalizar el ícono de tu archivo .exe haciendo clic en "Icon" y seleccionando un archivo .ico.
      - Advanced: Aquí puedes agregar comandos adicionales para personalizar aún más la conversión. Por ejemplo, puedes agregar opciones de PyInstaller si tienes experiencia con ellas.

8. **Generar el archivo .exe**

      - Una vez configuradas todas las opciones, haz clic en el botón "Convert .py to .exe". La herramienta comenzará a trabajar y, después de unos momentos, tu archivo ejecutable estará listo.

9. **Resultado**

    - La ruta del archivo .exe generado se mostrará en la interfaz. Puedes encontrar tu ejecutable en la carpeta que especificaste.

### Resumen de las Opciones Importantes

1. **Script Location**: Selecciona el archivo `.py` que deseas convertir.
2. **One File/One Directory**: Elige si quieres un solo archivo `.exe` o una carpeta con las dependencias.
3. **Console Window**: Decide si tu programa necesita una ventana de consola.
4. **Additional Files**: Incluye archivos adicionales necesarios para tu script.
5. **Icon**: Personaliza el ícono de tu archivo ejecutable.
6. **Advanced**: Opciones avanzadas para usuarios con experiencia en PyInstaller.

### Cómo Usar el Programa

1. Instala `auto-py-to-exe` usando `pip`.
2. Ejecuta `auto-py-to-exe` para abrir la interfaz gráfica.
3. Selecciona tu archivo `.py`.
4. Configura las opciones según tus necesidades.
5. Haz clic en "Convert .py to .exe".
6. Encuentra tu archivo `.exe` en la carpeta especificada.

## Desarrolladores

| [<img src="https://avatars.githubusercontent.com/u/163685041?v=4" width=115><br><sub>Michael Martinez</sub>](https://github.com/bkmay1417) |
| :---: |

Copyright (c) 2024 [Michael Martinez] yam8991@gmail.com
