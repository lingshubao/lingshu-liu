"""author:youngkun;date:20180608;function:裁剪照片的黑边"""

import cv2
import os
import datetime

def change_size(read_file):
    image=cv2.imread(read_file,1) #读取图片 image_name应该是变量

    b=cv2.threshold(image,15,255,cv2.THRESH_BINARY)          #调整裁剪效果
    binary_image=b[1]               #二值图--具有三通道
    binary_image=cv2.cvtColor(binary_image,cv2.COLOR_BGR2GRAY)
    print(binary_image.shape)       #改为单通道

    x=binary_image.shape[0]
    print("高度x=",x)
    y=binary_image.shape[1]
    print("宽度y=",y)
    edges_x=[]
    edges_y=[]
    for i in range(x):
        for j in range(y):
            if binary_image[i][j] == 255:
             edges_x.append(i)
             edges_y.append(j)
    left=min(edges_x)
    right=max(edges_x)
    width=right-left
    bottom=min(edges_y)
    top=max(edges_y)
    height=top-bottom
    pre1_picture=image[left:left+width,bottom:bottom+height]
    return pre1_picture

source_path="./test_dir/lichenification_score 3/"                                    #图片来源路径
save_path="./cut_test_dir/lichenification_score 3/"                                     #图片修改后的保存路径

if not os.path.exists(save_path):
    os.mkdir(save_path)

file_names=os.listdir(source_path)

starttime=datetime.datetime.now()
for i in range(len(file_names)):
    x=change_size(source_path + file_names[i])        #得到文件名
    cv2.imwrite(save_path+file_names[i],x)
    print("裁剪：",file_names[i])
    print("裁剪数量:",i)
    while(i==2600):
        break


print("裁剪完毕")
endtime = datetime.datetime.now()#记录结束时间
endtime = (endtime-starttime).seconds
print("裁剪总用时",endtime)

