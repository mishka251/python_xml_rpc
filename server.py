import pyautogui
from PIL.Image import Image
import base64
from xmlrpc.server import SimpleXMLRPCServer
import logging

host = input('Введите host запускаемого сервера(например localhost)')
port = int(input('Введите порт запускаемого сервера(например 9000)'))


def get_screenshot() -> Image:
    image: Image = pyautogui.screenshot()
    return image


def get_b64_screenshot() -> bytes:
    image = get_screenshot()
    filename = 'screenshot.png'
    with open(filename, 'wb') as file:
        image.save(file)
    with open(filename, 'rb')as file:
        _image = file.read()

    b64 = base64.b64encode(_image)

    return b64


logging.basicConfig(level=logging.DEBUG)

server = SimpleXMLRPCServer((host, port), logRequests=True)

server.register_function(get_b64_screenshot)

try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
