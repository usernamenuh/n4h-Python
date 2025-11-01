import nmap


scanner = nmap.PortScanner()

scanner.scan('192.168.100.13', '1-1024', '-v -sT')

print(scanner.scaninfo())
print(scanner.all_hosts())
print(scanner['192.168.100.13'].hostname())
print(scanner['192.168.100.13'].state())
print(scanner['192.168.100.13'].all_protocols())


