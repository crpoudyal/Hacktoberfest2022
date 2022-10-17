'''

@author: Ayush Shete

'''

import cv2
import numpy as np
from fer import FER

scr = cv2.VideoCapture(0) 
scr.set(3, 640)
scr.set(4, 480)

detector = FER(mtcnn=True)

while True:

    ret,frame = scr.read()
    emotion, score = detector.top_emotion(frame)

    print(emotion,score)
    if emotion == 'angry':
        emoj = cv2.imread('https://i.ibb.co/QN0gqNH/angry.png')
    elif emotion == 'disgust':
        emoj = cv2.imread('https://i.ibb.co/tJDxrhD/disgust.png')
    elif emotion == 'fear':
        emoj = cv2.imread('https://i.ibb.co/yBczSFB/fear.png')
    elif emotion == 'happy':
        emoj = cv2.imread('https://i.ibb.co/g6DW0Cf/happy.png')
    elif emotion == 'sad':
        emoj = cv2.imread('https://i.ibb.co/NyF0sDq/sad.png')
    elif emotion == 'surprise':
        emoj = cv2.imread('https://i.ibb.co/D4rDyfM/surprise.png')
    elif emotion == 'neutral':
        emoj = cv2.imread('https://i.ibb.co/KX7VSjh/neutral.png')
    else:
        emoj = cv2.imread('https://i.ibb.co/LdnS9nL/none.png')

    size = 150
    emoj = cv2.resize(emoj, (size, size))

    img2gray = cv2.cvtColor(emoj, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

    roi = frame[-size-20:-20, -size-20:-20]
    roi[np.where(mask)] = 0
    roi += emoj

    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (40, 210)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    cv2.putText(frame,emotion, org, font, fontScale, color, thickness, cv2.LINE_AA)
    
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

scr.release()

cv2.destroyAllWindows()
