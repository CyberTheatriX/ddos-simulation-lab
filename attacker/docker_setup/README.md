# Create Dockerfile

```bash
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    apache2-utils \
    iputils-ping \
    curl \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

CMD ["bash"]
```

# build attacker-image

```bash
sudo docker build -t attacker-image .
```

# run docker-compose.yml

```bash
version: '3.8'

services:
  attacker10:
    image: attacker-image
    container_name: attacker10
    networks:
      attacker_net:
        ipv4_address: 192.168.100.10

  attacker11:
    image: attacker-image
    container_name: attacker11
    networks:
      attacker_net:
        ipv4_address: 192.168.100.11

  attacker12:
    image: attacker-image
    container_name: attacker12
    networks:
      attacker_net:
        ipv4_address: 192.168.100.12

  attacker13:
    image: attacker-image
    container_name: attacker13
    networks:
      attacker_net:
        ipv4_address: 192.168.100.13

  attacker14:
    image: attacker-image
    container_name: attacker14
    networks:
      attacker_net:
        ipv4_address: 192.168.100.14

  attacker15:
    image: attacker-image
    container_name: attacker15
    networks:
      attacker_net:
        ipv4_address: 192.168.100.15

  attacker16:
    image: attacker-image
    container_name: attacker16
    networks:
      attacker_net:
        ipv4_address: 192.168.100.16

  attacker17:
    image: attacker-image
    container_name: attacker17
    networks:
      attacker_net:
        ipv4_address: 192.168.100.17

  attacker18:
    image: attacker-image
    container_name: attacker18
    networks:
      attacker_net:
        ipv4_address: 192.168.100.18

  attacker19:
    image: attacker-image
    container_name: attacker19
    networks:
      attacker_net:
        ipv4_address: 192.168.100.19

networks:
  attacker_net:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.100.0/24
 
```
# launch containers

```bash
sudo docker-compose up -d
```

# start containers after reboot

```bash
for i in $(seq 10 19); do
    sudo docker start attacker$i                                              
done
```
# execute simultaneous attack

```bash
sudo bash -c 'for i in $(seq 10 19); do docker exec attacker$i ab -n 50 -c 3 http://192.168.56.12/ & done; wait'
```
# to trigger threshold rule 

```bash
sudo bash -c 'for i in $(seq 10 19); do docker exec attacker$i ab -n 500 -c 20 http://192.168.56.12/ & done; wait'
```
