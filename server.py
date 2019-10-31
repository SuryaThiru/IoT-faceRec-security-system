from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
from facerec import detect_faces

# Initialize the Flask application
app = Flask(__name__)
app.debug = True

# route http posts to this method
@app.route('/image', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # recognize faces
    res = detect_faces(img[:, :, ::-1])

    if res[0] == -1: # no face
        response = {
            'face': '',
            'code': 404
        }
    elif res[0] == 0:
        response = {
            'face': 'unknown',
            'code': 201
        }
    else:
        response = {
            'face': res[1],
            'code': 200
        }

    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


# start flask app
app.run(host="0.0.0.0", port=5000)
