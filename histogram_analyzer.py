import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def procesar_y_mostrar_imagen():
    """
    Selecciona una imagen, la muestra junto con su histograma,
    imprime las frecuencias, la ecualiza, muestra la imagen ecualizada
    y su histograma, e imprime las frecuencias ecualizadas.
    """
    # --- 1. Selección de Archivo ---
    root = tk.Tk()
    root.withdraw()
    ruta_imagen = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Archivos de Imagen", "*.jpg *.jpeg *.png *.bmp *.tiff *.gif"),
                   ("Todos los archivos", "*.*")]
    )

    if not ruta_imagen:
        print("No se seleccionó ninguna imagen.")
        return

    # --- 2. Cargar la Imagen Original ---
    imagen_original = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)

    if imagen_original is None:
        print(f"Error: No se pudo cargar la imagen desde '{ruta_imagen}'")
        print("Asegúrate de que el archivo es una imagen válida y la ruta es correcta.")
        return

    # --- 3. Calcular Histograma Original ---
    hist_original = cv2.calcHist([imagen_original], [0], None, [256], [0, 256])

    # --- 4. Ecualizar la Imagen ---
    imagen_ecualizada = cv2.equalizeHist(imagen_original)

    # --- 5. Calcular Histograma Ecualizado ---
    hist_ecualizado = cv2.calcHist([imagen_ecualizada], [0], None, [256], [0, 256])

    # --- 5.5 Imprimir Frecuencias en la Consola ---
    print("-" * 40)
    print(" Frecuencias del Histograma Original")
    print("-" * 40)
    for i in range(256):
        # hist_original[i] devuelve una lista con un elemento, por eso [0]
        # Lo convertimos a entero para una impresión más limpia
        frecuencia = int(hist_original[i][0])
        print(f"Intensidad {i}: {frecuencia}")
    print("-" * 40)

    print("\n" + "-" * 40)
    print(" Frecuencias del Histograma Ecualizado")
    print("-" * 40)
    for i in range(256):
        frecuencia = int(hist_ecualizado[i][0])
        print(f"Intensidad {i}: {frecuencia}")
    print("-" * 40)
    print("\nMostrando gráficos...") # Indicador antes de que aparezca la ventana

    # --- 6. Mostrar Resultados Gráficos ---
    plt.figure(figsize=(12, 8)) # Tamaño de la ventana de visualización

    # Subplot 1: Imagen Original
    plt.subplot(2, 2, 1)
    plt.imshow(imagen_original, cmap='gray')
    plt.title('Imagen Original')
    plt.axis('off')

    # Subplot 2: Histograma Original
    plt.subplot(2, 2, 2)
    plt.plot(hist_original, color='black')
    plt.title('Histograma Original')
    plt.xlabel('Intensidad de Píxel')
    plt.ylabel('Número de Píxeles (Frecuencia)')
    plt.xlim([0, 256])

    # Subplot 3: Imagen Ecualizada
    plt.subplot(2, 2, 3)
    plt.imshow(imagen_ecualizada, cmap='gray')
    plt.title('Imagen Ecualizada')
    plt.axis('off')

    # Subplot 4: Histograma Ecualizado
    plt.subplot(2, 2, 4)
    plt.plot(hist_ecualizado, color='black')
    plt.title('Histograma Ecualizado')
    plt.xlabel('Intensidad de Píxel')
    plt.ylabel('Número de Píxeles (Frecuencia)')
    plt.xlim([0, 256])

    plt.tight_layout()
    plt.show() # La ejecución se detiene aquí hasta que cierres la ventana

# --- Ejecutar la función principal ---
if __name__ == "__main__":
    print("Iniciando selector de imagen...")
    procesar_y_mostrar_imagen()
    help(cv2.calcHist)
    print("Proceso terminado.")
