import pytesseract
from PIL import ImageGrab
import cv2
import numpy as np
import re
# Configura la ruta de Tesseract si es necesario
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Cambia según tu ruta de instalación

# Función para hacer la captura de pantalla
def capture_screen():
    # Captura la pantalla completa
    screen = ImageGrab.grab()
    return np.array(screen)

# Función para recortar la parte superior de la imagen
def crop_image(image, crop_y_low,crop_y_high,crop_x_low,crop_x_high  ):
    # Recortar la imagen para que solo incluya la región de interés (ajusta según el área específica)
    return image[crop_y_low:crop_y_high, crop_x_low:crop_x_high]

def crop_red_gold(image):
    # Recortar la imagen para que solo incluya la región de interés (ajusta según el área específica)
    return image[22:52,  1470:1540]

# Función para invertir la imagen (mejorar contraste del texto rojo)
def invert_image(image):
    # Invertir los colores de la imagen
    return cv2.bitwise_not(image)

# Función para preprocesar la imagen (canal rojo)
def preprocess_image(image):

    # Invertir la imagen para que el texto rojo se vuelva blanco sobre fondo oscuro
    inverted_image = invert_image(image)

    # Aplicar umbral binario para mejorar el contraste
    _, threshold_image = cv2.threshold(inverted_image, 120, 255, cv2.THRESH_BINARY)

    return threshold_image

# Función para detectar y extraer los números en el área recortada
def extract_number_from_image(image):
    # Preprocesa la imagen
    processed_image = preprocess_image(image)

    # Usa pytesseract para extraer el texto de la imagen (optimizado para dígitos)
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=.,k0123456789'  # Permite números y decimales
    extracted_text = pytesseract.image_to_string(processed_image, config=custom_config)

    # Utiliza una expresión regular para extraer números, incluyendo decimales
    numbers = re.findall(r'\d+[.,]\d+k', extracted_text)

    if numbers:
        return numbers[0]  # Devuelve el primer número detectado
    else:
        print("LOG WARN: {}".format(extracted_text))
        return None  # Si no se encuentra ningún número
def get_gold(crop_y_low,crop_y_high,crop_x_low,crop_x_high  ):
    # Captura la pantalla
    screen_image = capture_screen()

    # Recorta la parte superior de la imagen (solo los primeros píxeles de interés)
    cropped_blue_gold = crop_image(screen_image, crop_y_low,crop_y_high,crop_x_low,crop_x_high )

    # Extrae el número de la imagen recortada
    return extract_number_from_image(cropped_blue_gold)
