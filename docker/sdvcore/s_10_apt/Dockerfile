FROM ubuntu:22.04

ARG CMAKE_VERSION=3.24.1

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    PATH="/opt/cmake-${CMAKE_VERSION}/bin:/opt/venv/bin:$PATH"

RUN mkdir -p /opt/open_sdc/ext_apt/

COPY apt_package_list.txt /opt/open_sdc/ext_apt/apt_package_list.txt

# Install core apt packages from list
RUN apt-get update && \
    apt-get install -y perl && \
    apt-get install -y $(perl -ne 'print unless /^(\s*#|\s*$)/' /opt/open_sdc/ext_apt/apt_package_list.txt) && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update -y && \
    apt-get install -y wget && \
    wget https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}-Linux-x86_64.sh \
        -q -O /tmp/cmake-install.sh && \
    chmod +x /tmp/cmake-install.sh && \
    mkdir -p /opt/cmake-${CMAKE_VERSION} && \
    /tmp/cmake-install.sh --skip-license --prefix=/opt/cmake-${CMAKE_VERSION} && \
    rm /tmp/cmake-install.sh && \
    ln -sf /opt/cmake-${CMAKE_VERSION}/bin/* /usr/local/bin

RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install "conan==2.0.17" && \
    conan profile detect
