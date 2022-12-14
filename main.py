# INF601 - Advanced Programming in Python
# Laurie Frazier
# Final Project
# -sU for UDP, all udp ports and the service running on them, does not complete the 3 way handshake
# -sT for TCP Scan top 50 ports which most used in TCP
import streamlit as st
import nmap
import pandas as pd
import numpy as np

scan = nmap.PortScanner()
st.title('Slither')
st.subheader('INF 601 -  Advanced Programming with Python Final Project')
st.caption('Slither uses a NMAP API and displays an interactive '
           'table with easy visuals crossing over multiple IP addresses'
           ' under a SYN ACK, UDP or a Comprehensive Scan.'
           ' Slither runs a scan through a IP address given by the user and runs it '
           'through the top 50 ports being used.')
col1, col2 = st.columns([2, 2])
with col1:
    ip_addy = st.text_input('IP Address', )
with col2:
    protocol = st.radio("Chose an Option", ['TCP Connect Scan', 'UDP Scan'], horizontal=True)

if st.button('Run Scan'):
    if protocol == 'TCP Connect Scan':
        scan.scan(ip_addy, arguments='--top-ports 50 -sT')
        # Dataframe for TCP, in columns, port and state, followed by the scan run of keys and state
        try:
            if scan[ip_addy]['tcp'].keys() and scan[ip_addy].state():
                state = st.write('State: ', scan[ip_addy].state())
                key = scan[ip_addy]['tcp'].keys()
                tdf = pd.DataFrame({'Port', scan[ip_addy]['tcp'].keys(),
                                    'State', scan[ip_addy].state(),
                                    'Service', scan[ip_addy].service()})
                # tdf.style.applymap(color_condition)
                st.dataframe(tdf)
            else:
                st.write("Nothing found!")
        except:
            st.write("Nothing found!")

    elif protocol == 'UDP Scan':
        scan.scan(ip_addy, arguments='--top-ports 50 -sU')
        # Dataframe for TCP, in columns, port and state, followed by the scan run of keys and state
        try:
            if scan[ip_addy]['udp'].keys() and scan[ip_addy].state():
                state = st.write('State: ', scan[ip_addy].state())
                # st.write(scan[ip_addy]['udp'][1 - 1024]['state'])
                # st.write(scan[ip_addy]['udp'].keys())
                df = pd.DataFrame(
                    np.random.randn(50, 20),
                    columns=('col %d' % i for i in range(20)))
                # tdf = pd.DataFrame({'Open Ports', scan[ip_addy]['udp'].keys(),
                # 'Service', scan[ip_addy].service()})
                # tdf.style.applymap(color_condition)
                st.dataframe(df)
            else:
                st.write("Nothing found!")
        except:
            st.write("Nothing found!")

# Run for TCP Scan
