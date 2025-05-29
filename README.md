# Extract Data from ROSBAG into Pandas DataFrame
Code provides example of how to extract data from a ROSBAG in ROS2 to a Pandas dataframe, including ROS2 example ROSBAGs from data collected onboard a BlueROV2 as Blue Grotto Dive Resort.

Data visualized with Matplotlib.

## Setup
I recommend using a conda environment. I named mine ros_visuals.
1) Create conda environment with python=3.10
2) Activate conda environment
3) Install the following packages
- ``pip install rosbag-to-dataframe rosbags``
- ``conda install pandas matplotlib notebook ipykernel Pillow pyparsing``
4) Install ROS2 binaries for your computer if you have not already. See ROS2 documentation for details.
    - Note: ros2 is only needed if you need to work with the ROSBAGs (AKA view their topics and play them back. Otherwise, it is not needed.)

### Recommended Installs:
VSCode Extensions:
- Data Wrangler

## Using ROS2 for working with ROSBAG data
The most important thing is the ability to see what is in your bag (AKA know what topics and fields are available to you).
- Use ```ros2 bag info /bagpath``` to see what topics there are.
- ```ros2 interface show sensor_msgs/msg/Imu``` (the type of message)
    - Shows you the fields inside the topic


## Why not use Bagpy instead?
- Bagpy is great, but only compatible with ROS1.