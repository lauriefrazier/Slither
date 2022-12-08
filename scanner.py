#-sU for UDP, all udp ports and the service running on them, does not complete the 3 way handshake
#-sT for TCP Scan top 50 ports which most used in TCP
import streamlit as st
import nmap
scanner = nmap.PortScanner()

ip_addr = input()
resp = input()

if st.radio == 'TCP Connect Scan':
    scanner.scan(ip_addr, '--top-ports 50', '-v -sT')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == 'UDP Scan':
    scanner.scan(ip_addr, '--top-ports 50', '-v -sU')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
