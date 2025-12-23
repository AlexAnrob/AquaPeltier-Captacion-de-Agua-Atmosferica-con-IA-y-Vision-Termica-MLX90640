import time
import board
import busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def initialize_sensor():
    i2c = busio.I2C(board.SCL, board.SDA)
    mlx = adafruit_mlx90640.MLX90640(i2c)
    mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_4_HZ
    return mlx

def setup_plot():
    fig, ax = plt.subplots(figsize=(12, 7))
    therm1 = ax.imshow(np.zeros((24, 32)), vmin=0, vmax=60, cmap='jet', interpolation='bilinear')  # Usando 'jet'
    cbar = fig.colorbar(therm1)
    cbar.set_label('Temperature [°C]', fontsize=14)
    plt.title('Thermal Image')
    return fig, ax, therm1

def update_display(canvas, therm1, data_array):
    therm1.set_data(np.fliplr(data_array))
    therm1.set_clim(vmin=np.min(data_array), vmax=np.max(data_array))
    canvas.draw()

def save_image(fig, count):
    filename = f'capture_{count}.png'
    fig.savefig(filename)
    print(f'Imagen guardada: {filename}')
 
def main():
    mlx = initialize_sensor()
    fig, ax, therm1 = setup_plot()

    # Inicialización de la ventana Tkinter
    root = tk.Tk()
    root.wm_title("Thermal Camera")

    # Integrar Matplotlib con Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    frame = np.zeros((24*32,))
    t_array = []
    max_retries = 5

    last_save_time = time.monotonic()  # Para controlar cuando guardar imágenes
    image_counter = 0  # Contador para el nombre de los archivos de imagen

    while True:
        t1 = time.monotonic()
        retry_count = 0
        while retry_count < max_retries:
            try:
                mlx.getFrame(frame)
                data_array = np.reshape(frame, (24, 32))
                update_display(canvas, therm1, data_array)
                t_array.append(time.monotonic() - t1)
                print('Sample Rate: {0:2.1f}fps'.format(len(t_array) / np.sum(t_array)))
                break
            except ValueError:
                retry_count += 1
            except RuntimeError as e:
                retry_count += 1
                if retry_count >= max_retries:
                    print(f"Failed after {max_retries} retries with error: {e}")
                    break
        
        current_time = time.monotonic()
        if current_time - last_save_time >= 10:
            save_image(fig, image_counter)
            last_save_time = current_time
            image_counter += 1
        
        root.update_idletasks()  # Para actualizar la interfaz de Tkinter
        root.update()  # Para mantener la interfaz responsiva

if __name__ == '__main__':
    main()