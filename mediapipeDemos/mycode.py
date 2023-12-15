import argparse  # 导入参数解析模块
import cv2  # 导入OpenCV模块
import sys  # 导入sys模块
import numpy as np  # 导入NumPy模块
import insightface  # 导入insightface模块
from insightface.app import FaceAnalysis  # 从insightface.app中导入FaceAnalysis类
from insightface.data import get_image as ins_get_image  # 从insightface.data中导入get_image函数
import time
assert insightface.__version__>='0.3'  # 断言版本不低于0.3
import os
import mediapipe as mp
def handdetect(img):
    handimformation=[]
    list=[]
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
                for i in result.multi_hand_landmarks:
                    hand_landmarks = i  # 仅取第一个检测到的手
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
                    txt=''
                    if finger[0] and (not finger[1] and not finger[2] and not finger[3] and not finger[4]):
                        txt='good'
                    if finger[1] and finger[2] and (not finger[0] and not finger[3] and not finger[4]):
                        txt='yeah'
                    handimformation.append([list[0][1],list[0][2],txt])
                    for j in range(21):
                        list.pop(0)
    return handimformation
def judge(boxa,boxb):
    if boxa[0]<boxb[0]:
        return False
    if boxa[1]<boxb[1]:
        return False
    if boxa[2]>boxb[2]:
        return False
    if boxa[3]>boxb[3]:
        return False
    return True
def draw_on(img, face, text):
    dimg = img.copy()
    box = face.bbox.astype(int)
    color = (0, 0, 255)
    p=False
    for (x, y, w, h) in bodies:
        if judge(box,[x,y,x+w,y+h]):
            cv2.rectangle(dimg, (x, y), (x+w, 640), color, 2)
            p=True
            for i in handimformation:
                if judge([i[0],i[1],i[0],i[1]],[x+w/2-40,0,x+w/2+40,640]):
                    text+=':'+i[2]
    if not p:
        cv2.rectangle(dimg, (box[0], box[1]), (box[2], box[3]), color, 2)
        for i in handimformation:
            if judge([i[0],i[1],i[0],i[1]],[box[0]-10,0,box[2]+10,640]):
                text+=':'+i[2]
    imgsave=dimg[box[1]:box[3],box[0]:box[2],:]
    cv2.imwrite('./'+path+'/'+text+'/'+text+'.jpg',imgsave)
    '''
    if face.kps is not None:
        kps = face.kps.astype(int)
        for l in range(kps.shape[0]):
            color = (0, 0, 255)
            if l == 0 or l == 3:
                color = (0, 255, 0)
            cv2.circle(dimg, (kps[l][0], kps[l][1]), 1, color,2)
    '''
    cv2.putText(dimg, text, (box[0]-1, box[1]-4),cv2.FONT_HERSHEY_COMPLEX,1.2,(0,255,0),1)
    return dimg

path='face_data'
cascade_classifier = cv2.CascadeClassifier('./model/haarcascade_upperbody.xml')
parser = argparse.ArgumentParser(description='insightface app test')  # 创建参数解析器，设置描述为'insightface app test'
parser.add_argument('--ctx', default=0, type=int, help='ctx id, <0 means using cpu')  # 添加参数'--ctx'，默认值为0，类型为整数，帮助信息为'ctx id, <0 means using cpu'
parser.add_argument('--det-size', default=640, type=int, help='detection size')  # 添加参数'--det-size'，默认值为640，类型为整数，帮助信息为'detection size'
args = parser.parse_args()  # 解析参数
app = FaceAnalysis()  # 创建FaceAnalysis实例
app.prepare(ctx_id=args.ctx, det_size=(args.det_size,args.det_size))  # 准备分析器，设置ctx_id和det_size
data_source='data_package'
name_store=[]
land=[]
mpHands = mp.solutions.hands  # 使用mediapipe 手部模型
hands = mpHands.Hands()
drawmp = mp.solutions.drawing_utils  # 画线
topIds = [4, 8, 12, 16, 20]
for file in os.listdir('data_package'):
    name_store.append(file.split('.')[0])
    filename=os.path.join(data_source,file)
    img=cv2.imread(filename)
    img=cv2.resize(img,(480,640),interpolation=cv2.INTER_LINEAR)
    faces=app.get(img)
    land.append(faces[0].normed_embedding)
land = np.array(land, dtype=np.float32)  # 将feats转换为NumPy数组，数据类型为np.float32
def euclidean_distance(landmarks1, landmarks2):
    # 计算两组特征点之间的距离
    distances = np.sqrt(np.sum((landmarks1 - landmarks2)**2, axis=1))
    # 返回平均距离作为匹配度
    return np.mean(distances)
# 计算欧氏距禮以进行人脸比对
cap=cv2.VideoCapture(0)
while True:
    flag, img=cap.read()
    handimformation=handdetect(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bodies = cascade_classifier.detectMultiScale(gray, 1.1, 1)
    rimg = img.copy()
    faces=app.get(img)
    landnew = []
    for face in faces:
        landnew.append(face.normed_embedding)
    landnew = np.array(landnew, dtype=np.float32)
    dist_matrix = np.zeros((len(land), len(landnew)))
    if len(landnew)!=0:
        dist_matrix = np.dot(land,landnew.T)
    for i in range(len(land)):
        for j in range(len(landnew)):
            if dist_matrix[i, j]>0.35:
                rimg=draw_on(rimg,faces[j],name_store[i])
            print(dist_matrix)
    cv2.imshow('test',rimg)
    cv2.waitKey(5)
