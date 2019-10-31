import face_recognition as fr
from glob import glob
import numpy as np
import cv2

photo_paths = glob('faces/*.jpg')
photos = [cv2.imread(f)[:, :, ::-1] for f in photo_paths]
names = [name.split('/')[1][:-4] for name in photo_paths]

def detect_faces(img):

    img_enc = fr.face_encodings(img)

    if len(img_enc) == 0:
        return (-1, 'no face')
    else:
        img_enc = img_enc[0]

    photos_enc = [fr.face_encodings(im)[0] for im in photos]
    
    matches = fr.compare_faces(photos_enc, img_enc)
    matches = np.array(matches)

    if not matches.any():
        return (0, 'unknown face')
    else:
        match = matches.argmax()
        return (match, names[match])
