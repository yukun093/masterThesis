# import rosbag
# import time

# bag = rosbag.Bag('2021-02-24-17-27-26.bag')
# for topic, msg, t in bag.read_messages(topics=['/spot/odometry']):
#     time.sleep(1)
#     f = open("bagpy_test.txt", 'a')
#     print(type(msg))
#     # f.write(string(msg))
# bag.close()


import bagpy
from bagpy import bagreader
import pandas as pd
 
bag = bagreader('test.bag')

# replace the topic name
spot_odometry = bag.message_by_topic('/spot/odometry')
spot_odometry = pd.read_csv(spot_odometry)

# two format, one is csv, and the another is vc
# then the (x,y,z) of odometry can be read
print(spot_odometry) # prints laser data in the form of pandas dataframe

"""
continue later when using the real rosbag in ros2
"""
