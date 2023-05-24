from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topo import Topo
from visualize import visualize_topology

class MyTopo(Topo):
    def __init__(self, num_hosts=20):
        super(MyTopo, self).__init__()

        # Add switches
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')

        # Add hosts and connect them to switches
        num_switches = 2
        for i in range(1, num_hosts + 1):
            host = self.addHost(f'h{i}')
            switch = switch1 if i % num_switches == 1 else switch2
            self.addLink(host, switch)

        # Add link between switches
        self.addLink(switch1, switch2)

def create_midsize_organization_topology():
    my_topo = MyTopo()  # Create an instance of your custom topology class
    net = Mininet(topo=my_topo, controller=Controller, switch=OVSKernelSwitch)  # Pass the topology to the Mininet constructor

    visualize_topology(net.topo)  # Add this line

    net.start() # Start the network
    CLI(net) # Start CLI
    net.stop() # Stop the network

if __name__ == '__main__':
    setLogLevel('info')
    create_midsize_organization_topology()
