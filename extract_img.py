import rosbag
import cv2
import os
import numpy as np
from sensor_msgs.msg import CompressedImage

base_path = "/home/up2/Downloads"
for file in os.listdir(base_path):
    bag = rosbag.Bag('/home/up2/Downloads/' + file)

    save_dir = '/home/up2/Desktop/takeout_imgs/' + file[:-4] 
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # frame_count = 0
    frame_count = 0
    output = open("/home/up2/Desktop/takeout_imgs/" + file[:-4]  + "/raw.txt", "w")
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

    frame_count = 0
    for topic, msg, t in bag.read_messages(topics=['/camera/live_view/compressed']):

        # if frame_count > 3000 and frame_count < 5000:
            
        compressed_img = msg

        np_arr = np.frombuffer(compressed_img.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)


        save_path = save_dir + "/" + str(frame_count) + ".jpg"


        cv2.imwrite(save_path, cv_image)
        


        frame_count += 1


    bag.close()