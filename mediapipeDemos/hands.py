import cv2
import mediapipe as mp
import time
cap = cv2.VideoCapture(0)  # 调用镜头
mpHands = mp.solutions.hands  # 使用mediapipe 手部模型
hands = mpHands.Hands()
drawmp = mp.solutions.drawing_utils  # 画线
topIds = [4, 8, 12, 16, 20]
while True:
    success, img = cap.read()  # cap.read()会返回两个值：Ture或False 和 帧
    if success:
        list = []
        # opencv调用相机拍摄的图像格式是BGR,得转化为RGB格式便于图像处理
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)
        # print(result.multi_hand_landmarks) #打印手部21个点的坐标信息
        if result.multi_hand_landmarks:
            for handlm in result.multi_hand_landmarks:
                # print(landmarks) #打印坐标信息
                drawmp.draw_landmarks(img, handlm, mpHands.HAND_CONNECTIONS)
                for id, lm in enumerate(handlm.landmark):
                    h, w, c = img.shape  # 图像的长、宽、通道
                    cx, cy = int(lm.x * w), int(lm.y * h)  # 将坐标数值转为整数
                    list.append([id, cx, cy])
            if len(list) != 0:
                finger = []
                # 判断左右手
                if result.multi_hand_landmarks:
                    hand_landmarks = result.multi_hand_landmarks[0]  # 仅取第一个检测到的手
                    # 大拇指
                    if list[5][2]<list[0][2] and list[0][2]>list[17][2]+10:
                        if hand_landmarks.landmark[mpHands.HandLandmark.WRIST].x < hand_landmarks.landmark[
                            mpHands.HandLandmark.THUMB_TIP].x:
                            if list[topIds[0]][1] > list[topIds[0] - 1][1]:
                                finger.append(1)
                            else:
                                finger.append(0)
                        else:
                            if list[topIds[0]][1] < list[topIds[0] - 1][1]:
                                finger.append(1)
                            else:
                                finger.append(0)
                        for id in range(1, 5):
                            if list[topIds[id]][2] < list[topIds[id] - 2][2]:
                                finger.append(1)
                            else:
                                finger.append(0)
                    else:
                        if list[4][2]<list[3][2]:
                            finger.append(1)
                        else:
                            finger.append(0)
                        if hand_landmarks.landmark[mpHands.HandLandmark.WRIST].x < hand_landmarks.landmark[
                            mpHands.HandLandmark.THUMB_TIP].x:
                            for id in range(1, 5):
                                if list[topIds[id]][1] > list[topIds[id] - 2][1]:
                                    finger.append(1)
                                else:
                                    finger.append(0)
                        else:
                            for id in range(1, 5):
                                if list[topIds[id]][1] < list[topIds[id] - 2][1]:
                                    finger.append(1)
                                else:
                                    finger.append(0)
                print(finger)
                txt=''
                if finger[0] and (not finger[1] and not finger[2] and not finger[3] and not finger[4]):
                    txt='good'
                if finger[1] and finger[2] and (not finger[0] and not finger[3] and not finger[4]):
                    txt='yeah'
            cv2.putText(img, txt, (40, 350), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
    cv2.imshow("images", img)
    cv2.waitKey(1)
