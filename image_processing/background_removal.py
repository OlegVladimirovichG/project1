from rembg import remove
from PIL import Image

def remove_background(image: Image):
    """Удаляет фон с изображения."""
    return remove(image)
