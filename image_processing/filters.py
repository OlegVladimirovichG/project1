from PIL import ImageEnhance, ImageFilter

def apply_filters(image, filter_type):
    """Применяет различные фильтры к изображению."""
    if filter_type == 'sharpen':
        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(2.0)  # Резкость
    elif filter_type == 'brightness':
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(1.5)  # Яркость
    elif filter_type == 'contrast':
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.5)  # Контраст
    elif filter_type == 'blur':
        image = image.filter(ImageFilter.GaussianBlur(radius=2))  # Размытие
    return image
