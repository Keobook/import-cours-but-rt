from dhcp import Database

chemin="./src/dhcpd_hosts.txt"

db = Database()
db.addPattern("mac", 'hardware\s+ethernet\s+(\S+)' )
db.addPattern("ip",  'fixed-address\s+(\S+)'       )
db.load(chemin)
db.dump()