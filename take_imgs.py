# 从bag文件中提取出某一个索引下的预测分数score、预测类别blade_type。
# 存储到一个txt文件中。


import rosbag
import cv2
import os
import numpy as np
from sensor_msgs.msg import CompressedImage

bag = rosbag.Bag('/home/up2/Desktop/data_big_2023-04-29-23-12-25_0_T61_22.3min_45117.bag')

save_dir = '/home/up2/Desktop/takeout_imgs' 
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

frame_count = 0
output = open("/home/up2/Desktop/raw.txt", "w")
output.truncate()
ans = {}

for topic, msg, t in bag.read_messages(topics=['/cv/blade_type']):
    blade_type = msg.blade_type
    score = msg.score
    output.write(str(frame_count) + "," + str(blade_type) + "," + str(score) + "\n")
    ans[t] = [blade_type, score]
    frame_count += 1

output.close()
print("ans: ", ans)

bag.close()