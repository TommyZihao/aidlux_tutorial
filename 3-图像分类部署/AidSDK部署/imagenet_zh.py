# AidSDK部署-ImageNet1000-摄像头和视频-中文
# 同济子豪兄 2023-8-4

# 导入工具包
import cv2
from cvs import *
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import aidlite_gpu

# 导入中文字体，指定字体大小
font = ImageFont.truetype('SimHei.ttf', 32)

# 载入类别名称与ID映射表
idx_to_labels = np.load('imagenet1000_idx_to_labels_zh.npy', allow_pickle=True).item()

# 载入模型
model_path = 'resnet18_imagenet.tflite'
NUM_CLASS = 1000 # 指定类别个数
aidlite = aidlite_gpu.aidlite()

# 模型路径 输入维度 输出维度 线程数 是否开启NNAPI
# https://docs.aidlux.com/#/intro/ai/ai-aidlite?id=_4fast_annmodel
aidlite.FAST_ANNModel(model_path, [256*256*3*4], [NUM_CLASS*4], 3, 0)

# 初始化摄像头
Camera_ID = 0 # 摄像头ID 0-后置 1-前置
cap = cvs.VideoCapture(Camera_ID)

# 逐帧处理函数
def process_frame(img_bgr):
    
    # 记录该帧开始处理的时间
    start_time = time.time()
    
    ## 预处理
    img_tensor = cv2.resize(img_bgr, (256, 256)) # 尺寸缩放
    mean = (0.485, 0.456, 0.406) # 三通道的均值
    std = (0.229, 0.224, 0.225) # 三通道的标准差
    img_tensor = ((img_tensor / 255) - mean) / std
    img_tensor = img_tensor.astype('float32')
    
    ## 推理预测
    aidlite.setInput_Float32(img_tensor) # 装填数据
    aidlite.invoke() # 推理预测
    result = aidlite.getOutput_Float32() # 获得推理预测结果
    
    ## 解析预测结果
    pred_id = np.argmax(result) # 置信度最高类别 ID
    pred_class = idx_to_labels[pred_id] # 置信度最高类别名称
    
    # 用 pillow写中文
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) # BGR转RGB
    img_pil = Image.fromarray(img_rgb) # array 转 PIL
    draw = ImageDraw.Draw(img_pil)
    draw.text((50, 150), pred_class, font=font, fill=(0, 0, 255, 1))
    img_rgb = np.array(img_pil) # PIL 转 array
    img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR) # RGB转BGR
    
    # 记录该帧处理完毕的时间
    end_time = time.time()
    # 计算每秒处理图像帧数FPS
    FPS = 1/(end_time - start_time)
    # 在画面上写字：图片，字符串，左上角坐标，字体，字体大小，颜色，字体粗细
    FPS_string = 'FPS {:.2f}'.format(FPS) # 写在画面上的字符串
    img_output = cv2.putText(img_bgr, FPS_string, (50, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    return img_output

# 逐帧实时处理手机摄像头拍摄的画面-代码模板
while True:
    img_bgr = cap.read()
    
    if img_bgr is None:
        continue
        
    img_bgr = process_frame(img_bgr)
    
    cvs.imshow(img_bgr)



