
Active conda environment, ros_visuals

Create conda environment with python=3.10
pip install rosbag-to-dataframe
pip install pandas rosbags
conda install notebook ipykernel Pillow pyparsing matplotlib

VSCode Extensions:
- Data Wrangler

Use ros2 bag info /bagpath to see what topics there are.
ros2 interface show sensor_msgs/msg/Imu (the type of message)
    - Shows you the fields inside the topic

Why not Bagpy?
- Bagpy is great, but only compatible with ROS1.