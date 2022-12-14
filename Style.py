def color_condition(state):
    if state == 'up':
        color = 'green'
    elif state == 'down':
        color = 'red'
    elif state == 'filtered':
        color = 'yellow'

import streamlit as st
import nmap

scan = nmap.PortScanner()

ip_addy = st.text_input('IP Address', )
scan.scan(ip_addy, arguments='--top-ports 50 -sT')
try:
    if scan[ip_addy]['tcp'].keys() and scan[ip_addy].state():
        for proto in scan[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
        lport = scan[host][proto].keys()
        lport.sort()
        for port in lport:
        print('port : %s\tstate : %s' % (port, scan[host][proto][port]['state'])