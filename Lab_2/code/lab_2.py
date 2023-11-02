import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import exposure
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

def linear_contrast(image):
    # Получение минимального и максимального значения яркости изображения
    min_val = np.min(image)
    max_val = np.max(image)

    # Применение линейного контрастирования к изображению с использованием реального диапазона яркостей
    contrasted_image = exposure.rescale_intensity(image, in_range=(min_val, max_val))

    return contrasted_image

def add_constant(image, constant):
    # Поэлементное сложение изображения с константой
    tmp = image + constant
    result = np.uint8(tmp)
    return result

def negative(image):
    # Преобразование изображения в негатив
    tmp = np.uint8(255 - image)
    result = np.uint8(tmp)
    return result

def multiply_constant(image, constant):
    # Поэлементное умножение изображения на константу
    tmp = image * constant
    result = np.uint8(tmp)
    return result

def power_transform(image, constant):
    # Возведение в степень
    tmp = np.power(image, constant)
    tmp = np.clip(tmp, 0, 255)
    result = np.uint8(tmp)
    return result

def logarithmic_transform(image):
    # Логарифмическое преобразование изображения
    tmp = np.log(1 + image)
    tmp = tmp / np.max(tmp) * 255
    result = np.uint8(tmp)
    return result

def otsu_thresholding(image):
    # Применение метода Отсу для глобальной пороговой обработки
    _, thresholded_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresholded_image

def global_thresholding_with_histogram(image):
    # Вычисление гистограммы изображения
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])

    # Выбор порога на основе гистограммы
    total_pixels = image.shape[0] * image.shape[1]
    sum_intensity = np.sum(np.arange(256) * hist)

    max_between_class_variance = 0
    optimal_threshold = 0

    for t in range(256):
        foreground_pixels = np.sum(hist[:t])
        background_pixels = total_pixels - foreground_pixels

        if foreground_pixels == 0 or background_pixels == 0:
            continue

        sum_foreground = np.sum(np.arange(t) * hist[:t])
        sum_background = sum_intensity - sum_foreground

        mean_foreground = sum_foreground / foreground_pixels
        mean_background = sum_background / background_pixels

        between_class_variance = (foreground_pixels / total_pixels) * (background_pixels / total_pixels) * \
                                 ((mean_foreground - mean_background) ** 2)

        if between_class_variance > max_between_class_variance:
            max_between_class_variance = between_class_variance
            optimal_threshold = t

    # Применение пороговой обработки на основе выбранного порога
    _, thresholded_image = cv2.threshold(image, optimal_threshold, 255, cv2.THRESH_BINARY)

    return thresholded_image

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        thresholded_image = global_thresholding_with_histogram(image)
        show_images(image, thresholded_image)

def show_images(image, new_image, text):
    cv2.imshow("original image", image)
    cv2.imshow(text, new_image)

def show_images_hist(image, threshholded_image, text):
    cv2.imshow("original image", image)
    draw_histogram(image)
    cv2.imshow(text, threshholded_image)

def draw_histogram(image):
    # Вычисление гистограммы изображения
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Нормализация гистограммы для визуализации
    hist_normalized = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX)

    # Создание пустого холста для рисования гистограммы
    histogram_canvas = np.zeros((256, 256), dtype=np.uint8)

    # Рисование графика гистограммы
    for i in range(256):
        cv2.line(histogram_canvas, (i, 255), (i, 255 - int(hist_normalized[i])), 255)

    return histogram_canvas

def select_image(button_index):
    # Opening the file selection dialog
    file_path = filedialog.askopenfilename()

    if file_path:
        # Loading the image
        image = Image.open(file_path)

        # Converting the image to a Tkinter-compatible format
        tk_image = ImageTk.PhotoImage(image)
        

        """# Updating the image on the corresponding button
        image_buttons[button_index].config(image=tk_image)
        image_buttons[button_index].image = tk_image"""

        # Displaying the selected image
        selected_image_labels[button_index].config(image=tk_image)
        selected_image_labels[button_index].image = tk_image
        processed_image = image.copy()
        # Processing the selected image
        if button_index == 0:
            processed_image = linear_contrast(np.array(image))
        elif button_index == 1:
            # Getting the value from the corresponding entry widget
            constant = int(spinbox_widgets[0].get())
            processed_image = add_constant(np.array(image), constant)
        elif button_index == 2:
            processed_image = negative(np.array(image))
        elif button_index == 3:
            # Getting the value from the corresponding entry widget
            constant = int(spinbox_widgets[1].get())
            processed_image = multiply_constant(np.array(image), constant)
        elif button_index == 4:
            # Getting the value from the corresponding entry widget
            constant = int(spinbox_widgets[2].get())
            processed_image = power_transform(np.array(image), constant)
        elif button_index == 5:
            processed_image = logarithmic_transform(np.array(image))
        elif button_index == 6:
            processed_image = otsu_thresholding(np.array(image.convert('L')))
        elif button_index == 7:
            processed_image = global_thresholding_with_histogram(np.array(image))

        # Converting the processed image to a Tkinter-compatible format
        processed_tk_image = ImageTk.PhotoImage(Image.fromarray(processed_image))

        # Displaying the processed image
        processed_image_labels[button_index].config(image=processed_tk_image)
        processed_image_labels[button_index].image = processed_tk_image

# Creating the application window
window = tk.Tk()
window.title("Image Selection and Processing")

# Configuring the style for the notebook
style = ttk.Style()
style.configure("TNotebook.Tab", padding=[30, 10])  # Increasing the padding to enlarge the tabs

# Creating tabs
notebook = ttk.Notebook(window, style="TNotebook")

# Creating a list of image selection buttons, selected image labels, and processed image labels
image_buttons = []
selected_image_labels = []
processed_image_labels = []
spinbox_widgets = []
tab_names = ["linear","add","neg","mul","pow","log","otsu","glob_hist"]
for i in range(8):
    # Creating a tab
    tab = ttk.Frame(notebook)

    # Creating the image selection button on the tab
    button = tk.Button(tab, text="Select Image", command=lambda i=i: select_image(i))
    button.pack(pady=10)
    image_buttons.append(button)
    
    # Adding a scale widget for the second, third, and fourth tabs
    if i == 1 or i == 2 or i == 3:
        spinbox_label = tk.Label(tab)
        spinbox_label.pack(pady=5)

        spinbox_widget = tk.Spinbox(from_=0, to=100)
        spinbox_widget.pack(pady=5)

        spinbox_widgets.append(spinbox_widget)

    # Creating labels to display the selected image and processed image on the tab
    selected_image_label = tk.Label(tab)
    selected_image_label.pack(pady=10)
    selected_image_labels.append(selected_image_label)

    processed_image_label = tk.Label(tab)
    processed_image_label.pack(pady=10)
    processed_image_labels.append(processed_image_label)

    # Adding the tab to the notebook
    notebook.add(tab, text=f"{tab_names[i]}")

# Placing the notebook on the window
notebook.pack()

# Running the main event loop
window.mainloop()

# Загрузка изображения
"""image = cv2.imread('E://Low-contrast-image.png', 0)  # Загрузка в оттенках серого

root = tk.Tk()
root.title("Image Thresholding")

# Создание кнопки "Открыть файл"
open_button = tk.Button(root, text="Открыть файл", command=open_file)
open_button.pack()

root.mainloop()

# Применение линейного контрастирования к изображению
lc_image = linear_contrast(np.array(image))
add_image = add_constant(np.array(image), 50)
neg_image = negative(np.array(image))
mul_image = multiply_constant(np.array(image), 2)
pow_image = power_transform(np.array(image), 1.5)
log_image = logarithmic_transform(np.array(image))
otsu_image = otsu_thresholding(image)
hist_image = global_thresholding_with_histogram(image)
# Отображение исходного и контрастированного изображений
cv2.imshow('Original Image', image)
cv2.imshow('Contrast Adjusted Image', lc_image)
cv2.imshow('Added Constant Image', add_image)
cv2.imshow('Negative Image', neg_image)
cv2.imshow('Multioly Image', mul_image)
cv2.imshow('Power Image', pow_image)
cv2.imshow('Logarithmic Image', log_image)
cv2.imshow('Otsu threshholding', otsu_image)
cv2.imshow('Histogram threshholding', hist_image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""