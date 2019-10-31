import cv2
from io import BytesIO
import tele_interface as tele
from time import sleep
import requests
import jsonpickle


def send_image_to_bot(im, caption):
    im = cv2.imencode('.jpg', im)[1].tostring()
    io = BytesIO(im)
    tele.send_image(io, caption)

def send_image_to_server(im):
    url = 'http://localhost:5000/image'
    _, img_enc = cv2.imencode('.jpg', im)
    response = requests.post(url, data=img_enc.tostring())
    return response.json()

def camera_loop(prev):
    cam = cv2.VideoCapture("http://192.168.43.58:8080/video")
    ret, im = cam.read()

    # send image to server to run face recognition if unknown face,
    res = send_image_to_server(im)
    notify_bot = False if res['code'] == 404 else True
    
    if notify_bot and prev != res['face']:
        # send image to the bot
        caption = res['face'] + ' is here!' if res['code'] == 200 else 'Unknown visitor is here'
        send_image_to_bot(im, caption)
        tele.send_prompt()

    cam.release()
    return res['face']

if __name__ == "__main__":
    prev = ''
    while True:
        prev = camera_loop(prev)
        sleep(1)

