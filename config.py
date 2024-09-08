import os

# Конфигурации приложения
class Config:
    STRIPE_API_KEY = os.getenv('STRIPE_API_KEY', 'your_stripe_api_key')

# Для других конфигураций можно использовать дополнительные классы
