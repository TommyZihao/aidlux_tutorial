# 调用手机摄像头，逐帧实时拍摄+OpenCV图像处理
# 同济子豪兄 2023-7-30

# 导入工具包
import time
import cv2
from cvs import *

# 初始化摄像头
# 摄像头ID 0-后置 1-前置
Camera_ID = 0
cap = cvs.VideoCapture(Camera_ID)

# Canny 边缘检测 - 写 FPS 数值
def process_frame(img_bgr):
    '''输入BGR格式的 numpy array，输出BGR格式的 numpy array'''
    
    # 记录该帧开始处理的时间
    start_time = time.time()
    
    # 逐帧处理操作
    img_bgr = cv2.Canny(img_bgr, 100, 200)
    img_bgr = np.dstack((img_bgr, img_bgr, img_bgr))
    
    # 记录该帧处理完毕的时间
    end_time = time.time()
    # 计算每秒处理图像帧数FPS
    FPS = 1/(end_time - start_time)

    # 在画面上写 FPS 数值
    end_time = time.time()
    FPS = 1/(end_time - start_time) # 计算每秒处理图像帧数FPS
    FPS_string = 'FPS {:.2f}'.format(FPS) # 写在画面上的字符串
    img_bgr = cv2.putText(img_bgr, FPS_string, (25, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (255, 0, 255), 2) # 在画面上写字：图片，字符串，左上角坐标，字体，字体大小，颜色，字体粗细

    return img_bgr

# 逐帧实时处理手机摄像头拍摄的画面-代码模板
while True:
    img_bgr = cap.read()
    
    if img_bgr is None:
        continue
        
    img_bgr = process_frame(img_bgr)
    
    cvs.imshow(img_bgr)


