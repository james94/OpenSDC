FROM s_ros_humble

RUN mkdir -p /opt/open_sdc/ext_entry/

COPY entrypoint.py /opt/open_sdc/ext_entry/entrypoint.py
COPY setup_ros2.py /opt/open_sdc/ext_entry/setup_ros2.py

# Set up ROS2
ENV ROS_DOMAIN_ID=0

ENTRYPOINT ["python3", "/opt/open_sdc/ext_entry/entrypoint.py"]
