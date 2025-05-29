from rosbag_to_dataframe import extract_data_from_bag
import pandas as pd

import numpy as np

bag_files = ['waterlinked_dvl_05132025_1250']  # List of ROS bag files
topic1 = '/rov/imu'  # Topic to extract data from
fields1 = [ 'orientation']  # List of fields to extract from the message

dataframe1 = extract_data_from_bag(bag_files, topic1, fields1)

# Expand orientation column into separate x, y, z, w columns
orientation_df = dataframe1['orientation'].apply(lambda q: pd.Series({
    'orientation_x': q.x,
    'orientation_y': q.y,
    'orientation_z': q.z,
    'orientation_w': q.w,
}))

# Combine with original DataFrame
dataframe = pd.concat([dataframe1.drop(columns=['orientation']), orientation_df], axis=1)

print(dataframe1.head())

###################################################################
bag_files = ['waterlinked_dvl_05132025_1250']  # List of ROS bag files
topic2 = '/waterlinked_dvl_driver/odom'  # Topic to extract data from
fields2 = ['pose']  # List of fields to extract from the message

dataframe2 = extract_data_from_bag(bag_files, topic2, fields2)

print(dataframe2.head())
# print(dataframe2.columns)
# print(type(dataframe2.iloc[0][topic2]))  # Or whatever the column name is
