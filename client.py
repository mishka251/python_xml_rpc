from xmlrpc.client import ServerProxy
import base64
from PIL import Image

host = input('Введите host сервера к которому подключаемся(например localhost)')
port = input('Введите порт сервера к которому подключаемся(например 9000)')

url = f'http://{host}:{port}'
proxy = ServerProxy(url)

response = proxy.get_b64_screenshot()
content = str(response)

_image = base64.b64decode(content)

filename = 'screenshot2.png'

with open(filename, 'wb') as file:
    file.write(_image)

image = Image.open(filename)
image.show()
