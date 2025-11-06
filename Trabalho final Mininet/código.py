from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info


class CustomTopo(Topo):
    def build(self):

        # Adiciona os switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Adiciona os hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')

        # Conecta os hosts aos switches
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s3)
        self.addLink(h5, s3)

        # Conecta os switches entre si
        self.addLink(s1, s2)
        self.addLink(s2, s3)


def run():
    "Executa a rede"
    topo = CustomTopo()
    net = Mininet(topo=topo, switch=OVSSwitch, controller=None,
                  link=TCLink, autoSetMacs=True)

    net.start()
    info('\n### Rede inicializada ###\n')
    info('### Testando conectividade inicial com pingall ###\n')
    net.pingAll()

    # Abrir CLI para comandos manuais
    CLI(net)

    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
