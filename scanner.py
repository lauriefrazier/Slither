#-sU for UDP, all udp ports and the service running on them, does not complete the 3 way handshake
#-sT for TCP Scan top 50 ports which most used in TCP
import streamlit as st
import nmap
scanner = nmap.PortScanner()
import pandas as pd

ip_addy = input()

if st.radio == 'TCP Connect Scan':
    scanner.scan(ip_addy, '--top-ports 50', '-v -sT')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_addy].state())
    print(scanner[ip_addy].all_protocols())
    print("Open Ports: ", scanner[ip_addy]['tcp'].keys())


    df = pd.DataFrame({'Open Port': [scanner[ip_addy]['tcp'].keys()],
                       ''})
elif st.radio == 'UDP Scan':
    scanner.scan(ip_addy, '--top-ports 50', '-v -sU')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_addy].state())
    print(scanner[ip_addy].all_protocols())
    print("Open Ports: ", scanner[ip_addy]['udp'].keys())


