FROM ubuntu:18.04

USER root
WORKDIR /root

COPY ENTRYPOINT.sh /

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    dnsutils \
    ifupdown \
    iproute2 \
    iptables \
    iputils-ping \
    mininet \
    net-tools \
    openvswitch-switch \
    openvswitch-testcontroller \
    tcpdump \
    vim \
    x11-xserver-utils \
    xterm \
 && rm -rf /var/lib/apt/lists/* \
 && touch /etc/network/interfaces \
 && chmod +x /ENTRYPOINT.sh

# Install Python3 and its dependencies along with mininet python library
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-wheel \
 && rm -rf /var/lib/apt/lists/* \
 && pip3 install mininet

# Install and compile OpenFlow reference implementation
RUN apt-get update -y && apt-get install -y autoconf automake libtool make git pkg-config
RUN git clone https://github.com/mininet/openflow.git
RUN cd openflow && ./boot.sh && ./configure && make && make install


EXPOSE 6633 6653 6640

ENTRYPOINT ["/ENTRYPOINT.sh"]