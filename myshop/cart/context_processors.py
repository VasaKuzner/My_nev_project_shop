

from .cart import Cart

def cart(request):
    """Як видно, контекстний процесор — це функція, яка отримує
    об'єкт запиту як параметр і повертає словник об'єктів, які будуть
    доступні для всіх шаблонів, що візуалізуються за допомогою"""

    return {'cart': Cart(request)}