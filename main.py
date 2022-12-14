# INF601 - Advanced Programming in Python
# Laurie Frazier
# Final Project
# -sU for UDP, all udp ports and the service running on them, does not complete the 3 way handshake
# -sT for TCP Scan top 50 ports which most used in TCP
import streamlit as st
import nmap
scan = nmap.PortScanner()
st.title('Slither')
st.subheader('INF 601 -  Advanced Programming with Python Final Project')
st.caption('Slither uses a NMAP API and displays an interactive '
           'table with easy visuals crossing over multiple IP addresses'
           ' under a SYN ACK, UDP or a Comprehensive Scan.'
           ' Slither runs a scan through a IP address given by the user and runs it '
           'through the top 50 ports being used.')
# Created columns within the frame to create better visuals
col1, col2 = st.columns([2, 2])
with col1:
    ip_addy = st.text_input('IP Address', )
with col2:
    protocol = st.radio("Chose an Option", ['TCP Connect Scan', 'UDP Scan'], horizontal=True)

# Committing button for scan with Run Scan
if st.button('Run Scan'):
    if protocol == 'TCP Connect Scan':
        scan.scan(ip_addy, arguments='--top-ports 50 -sT')
        # If statement, if it passes with both keys and live state, run the loop
        if scan[ip_addy]['tcp'].keys() and scan[ip_addy].state():
            state = st.write('Host State: ', scan[ip_addy].state())
            ports = list(scan[ip_addy]['tcp'].keys())
            ports.sort()
            st.write(f"Host: {ip_addy}")
            st.write(f"Available Ports:")
            col1, col2, col3 = st.columns([1, 1, 2])
            # Created columns for data to be run.
            with col1:
                st.write(f"Port")
            with col2:
                st.write(f"State")
            with col3:
                st.write(f"Service")
            for port in ports:
                with col1:
                    st.write(f"{port}")
                with col2:
                    st.write(f"{scan[ip_addy]['tcp'][port]['state']}")
                with col3:
                    st.write(f"{scan[ip_addy]['tcp'][port]['name']}")

    elif protocol == 'UDP Scan':
        scan.scan(ip_addy, arguments='--top-ports 50 -sU')
        # Copy of loop for UDP Scan instead, same properties
        if scan[ip_addy]['udp'].keys() and scan[ip_addy].state():
            state = st.write('Host State: ', scan[ip_addy].state())
            ports = list(scan[ip_addy]['udp'].keys())
            ports.sort()
            st.write(f"Host: {ip_addy}")
            st.write(f"Available Ports:")
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                st.write(f"Port")
            with col2:
                st.write(f"State")
            with col3:
                st.write(f"Service")
            for port in ports:
                with col1:
                    st.write(f"{port}")
                with col2:
                    st.write(f"{scan[ip_addy]['udp'][port]['state']}")
                with col3:
                    st.write(f"{scan[ip_addy]['tudp'][port]['name']}")
    else:
        st.write('Nothing Found!')
