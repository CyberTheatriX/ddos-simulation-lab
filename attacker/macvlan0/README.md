# Create a macvlan interface(macvlan0) to bridge attacker containers to the victim subnet:

```bash
sudo ip link add macvlan0 link eth1 type macvlan mode bridge
sudo ip addr add 192.168.100.254/24 dev macvlan0
sudo ip link set macvlan0 up
```
# Enable IP Forwarding

```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```
## To make it persistent across reboots, add to /etc/sysctl.conf

```bash
net.ipv4.ip_forward=1
```
##and apply

```sudo sysctl -p
```
# Enable Proxy ARP

```bash
echo 1 > /proc/sys/net/ipv4/conf/macvlan0/proxy_arp
echo 1 > /proc/sys/net/ipv4/conf/eth1/proxy_arp
```
## To persist across reboots, add to /etc/sysctl.conf

```bash
net.ipv4.conf.macvlan0.proxy_arp=1
net.ipv4.conf.eth1.proxy_arp=1
```
#Enable Promiscuous Mode

```bash
sudo ip link set macvlan0 promisc on
sudo ip link set eth1 promisc on
```
