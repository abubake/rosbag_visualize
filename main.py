from rosbag_to_dataframe import extract_data_from_bag

bag_files = ['/path/to/your/bagfile1.bag', '/path/to/your/bagfile2.bag']  # List of ROS bag files
topic = '/your_topic'  # Topic to extract data from
fields = ['field1', 'field2']  # List of fields to extract from the message

dataframe = extract_data_from_bag(bag_files, topic, fields)