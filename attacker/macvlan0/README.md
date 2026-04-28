# Create a macvlan interface(macvlan0) to bridge attacker containers to the victim subnet:

```bash
sudo ip link add macvlan0 link eth1 type macvlan mode bridge
sudo ip addr add 192.168.100.254/24 dev macvlan0
sudo ip link set macvlan0 up

