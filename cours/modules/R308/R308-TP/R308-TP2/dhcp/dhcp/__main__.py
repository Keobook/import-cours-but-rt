import re

class Host:
    """ Classe représentant une machine"""
    def __init__(self, hostname:str, attributes):
        self.hostname = hostname
        self.attributes = attributes
          
    def __repr__(self):
        return f"DHCP::Host(hostname={self.hostname} attributes={self.attributes}"

class Database:
    """Classe relative au DHCP """
    def __init__(self):
        self.pattern={
            "host": r"(\w[a-zA-Z]*-*[a-zA-Z]*)"
        }
        self.hosts=[]

    def addPattern(self, key: str, pattern: str):
        """ Méthode d'ajout d'une mac ou d'une IP """
        self.pattern[key] = pattern

    def dump(self):
        """Affichage de l'entrée hôte"""
        for host in self.hosts:
            print(host)

    def load(self,filename):
        """Chargement du fichier DHCP"""
        with open(filename, "rt", encoding="utf-8") as fin:
            if fin.readable():
                rfin = fin.readlines()
                for line in rfin:
                    curr_attributes = {
                        "ip": "",
                        "mac": ""
                    }

                    host = re.findall(self.pattern["host"], line)[1]
                    mac = re.findall(self.pattern["mac"], line)[0].strip().replace(";", "")
                    ip = re.findall(self.pattern["ip"], line)

                    ### Let's set the attributes dict
                    curr_attributes.update({
                        "ip": "".join(ip).strip().replace(";", ""),
                        "mac": mac
                    })

                    self.hosts.append(Host(host, curr_attributes))

def test():
  chemin="./src/dhcpd_hosts.txt"
  db = Database()
  db.addPattern( "mac", r'hardware\s+ethernet\s+(\S+)' )
  db.addPattern( "ip",  r'fixed-address\s+(\S+)'       )
  db.load(chemin)
  db.dump()

if __name__ == "__main__":
    test()