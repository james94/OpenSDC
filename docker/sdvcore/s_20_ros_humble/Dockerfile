FROM s_apt

RUN mkdir -p /opt/open_sdc/ext_ros/

COPY ros_humble_package_list.txt /opt/open_sdc/ext_ros/ros_humble_package_list.txt

# Set up locale
RUN locale-gen en_US en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

# Set up ROS2
ENV ROS_DISTRO=humble

# Setup sources and keys for ROS2 Humble
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key | apt-key add - && \
    echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list

# Install ROS2 Humble packages from list
RUN apt-get update && \
    apt-get install -y perl && \
    apt-get install -y $(perl -ne 'print unless /^(\s*#|\s*$)/' /opt/open_sdc/ext_ros/ros_humble_package_list.txt) && \
    rm -rf /var/lib/apt/lists/*
