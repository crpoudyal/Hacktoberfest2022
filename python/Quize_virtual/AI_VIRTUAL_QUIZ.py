import csv
import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import time
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)

class MCQ():
    def __init__(self, data):
        self.question = data[0]
        self.choice1 = data[1]
        self.choice2 = data[2]
        self.choice3 = data[3]
        self.choice4 = data[4]
        self.answer = int(data[5])

        self.userAns = None

    def update(self, cursor, bboxs):

        for x, bbox in enumerate(bboxs):
            x1, y1, x2, y2 = bbox
            if x1 < cursor[0] < x2 and y1 < cursor[1] < y2:
                self.userAns = x + 1
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)


pathCSV = 'D:\programing\python_programms\download_proggrams\AI_virtual_quiz-game-main\mcq.csv'
with open(pathCSV, newline='\n') as f:
    reader = csv.reader(f)
    dataAll = list(reader)[1:7]
print(len(dataAll))

# Create Object for each MCQ
mcqList = []
for q in dataAll:
    mcqList.append(MCQ(q))

print("Total MCQ Objects Created:", len(mcqList))

qNo = 0
qTotal = len(dataAll)
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands,img = detector.findHands(img,flipType=False)
    if qNo < qTotal:
        mcq = mcqList[qNo]
        img, bbox = cvzone.putTextRect(img, mcq.question, [30, 50], 1, 2, offset=30, border=5)
        img, bbox1 = cvzone.putTextRect(img, mcq.choice1, [30, 200], 2, 3, offset=30, border=5)
        img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [280, 200], 2, 3, offset=30, border=5)
        img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [30, 350], 2, 3, offset=30, border=5)
        img, bbox4 = cvzone.putTextRect(img, mcq.choice4, [280, 350], 2, 3, offset=30, border=5)

        if hands:
            lmList = hands[0]['lmList']
            cursor = lmList[8]
            length, info = detector.findDistance(lmList[8], lmList[12])
            # print(length)
            if length < 35:
                mcq.update(cursor, [bbox1, bbox2, bbox3, bbox4])
                if mcq.userAns is not None:
                    print(mcq.userAns)
                    time.sleep(0.5)
                    qNo += 1
    else:
        score = 0
        for mcq in mcqList:
            if mcq.answer == mcq.userAns:
                score += 1
        score = round((score / qTotal) * 100, 2)
        img, _ = cvzone.putTextRect(img, "Quiz Completed", [150, 100], 2, 2, offset=50, border=5)
        img, _ = cvzone.putTextRect(img, f'Your Score: {score}%', [200, 300], 2, 2, offset=50, border=5)
    barValue = 30 + (530 // qTotal) * qNo
    cv2.rectangle(img,(30,430),(barValue,460),(0,255,0),cv2.FILLED)
    cv2.rectangle(img, (30, 430), (560, 460), (255, 0, 255),5)
    img, _ = cvzone.putTextRect(img, f'{round((qNo / qTotal) * 100)}%', [580, 455], 2, 2, offset=16)
    cv2.imshow("vid", img)
    cv2.waitKey(1)
