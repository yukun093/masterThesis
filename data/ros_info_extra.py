#coding:utf-8

import roslib
import rosbag
import rospy
import cv2
from sensor_msg.msg import Image
from cv_bridge import CvBridgeError

path = '/home/yukun/Documents/Master_Thesis/masterThesis/output/ros1_bagimage_output' # path to store images
class ImageCreatror():
    def __init__(self):
        self.bridge = CvBridge()
        with rosbag.Bag('2ndroll.bag', 'r') as bag:   #要读取的bag文件；
            for topic,msg,t in bag.read_messages():
                if topic == "/spot/camera/back/image":  #图像的topic；
                        try:
                            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                        except CvBridgeError as e:
                            print(e)
                        timestr = "%.6f" %  msg.header.stamp.to_sec()
                        #%.6f表示小数点后带有6位，可根据精确度需要修改；
                        image_name = timestr+ ".jpg" #图像命名：时间戳.jpg
                        cv2.imwrite(path+image_name, cv_image)  #保存;

if __name__ == '__main__':
    image_creator = ImageCreator()