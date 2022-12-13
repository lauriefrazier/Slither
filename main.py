# INF601 - Advanced Programming in Python
# Laurie Frazier
# Final Project
# -sU for UDP, all udp ports and the service running on them, does not complete the 3 way handshake
# -sT for TCP Scan top 50 ports which most used in TCP
import streamlit as st
import nmap
import pandas as pd
scan = nmap.PortScanner()
st.title('Slither')
st.subheader('INF 601 -  Advanced Programming with Python Final Project')
st.caption('Slither uses a NMAP API and displays an interactive '
           'table with easy visuals crossing over multiple IP addresses'
           ' under a SYN ACK, UDP or a Comprehensive Scan.'
           ' Slither runs a scan through a IP address given by the user and runs it '
           'through the top 50 ports being used.')
ip_addy = st.text_input('IP Address', )
protocol = st.radio("Chose an Option", ['TCP Connect Scan', 'UDP Scan'], horizontal=True)
# Created for state recognization on the top of the scan
st.write('IP status: ', scan[ip_addy,'--top-ports 50'].state())

# Run for TCP Scan
if protocol == 'TCP Connect Scan':
    scan.scan(ip_addy, '--top-ports 50', '-sT')
    # Dataframe for TCP, in columns, port and state, followed by the scan run of keys and state
    tdf = pd.DataFrame({"Open Ports", scan[ip_addy]['tcp'].keys(),
                        'State', scan[ip_addy].state()})
    # tdf.style.applymap(color_condition)
    st.table(tdf)


elif protocol == 'UDP Scan':
    scan.scan(ip_addy, '--top-ports 50', '-sU')
    # Dataframe for TCP, in columns, port and state, followed by the scan run of keys and state
    udf = pd.DataFrame({'Port', scan[ip_addy]['udp'].keys(),
                        'Service', scan[ip_addy].service(),
                        'Version', scan[ip_addy].version()})
    # udf.style.applymap(color_condition)
    st.table(udf)

else:
    st.write('Please')
