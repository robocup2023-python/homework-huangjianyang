import cv2
if __name__ == '__main__':
    # 加载Haar级联分类器模型
    cascade_classifier = cv2.CascadeClassifier('./model/haarcascade_upperbody.xml')
 
    # 加载视频
    video_capture = cv2.VideoCapture(0)
    while True:
        # 获取视频的一帧
        ret, frame = video_capture.read()
 
        # 转换为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
        # 检测人体
        bodies = cascade_classifier.detectMultiScale(gray, 1.1, 4)
 
        # 在图像上绘制人体框并显示
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
        cv2.imshow('image', frame)
        cv2.waitKey(5)
 
    # 释放资源
    cv2.destroyAllWindows()
