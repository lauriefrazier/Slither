import streamlit as st
import nmap
scanner = nmap.PortScanner()

st.title('Slither')
st.subheader('INF 601 -  Advanced Programming with Python Final Project')
st.caption('Slither uses a NMAP API and displays an interactive '
           'table with easy visuals crossing over multiple IP addresses'
           ' under a SYN ACK, UDP or a Comprehensive Scan.'
           ' Slither runs a scan through a IP address given by the user and runs it '
           'through the top 50 ports being used.')
ip_addy = st.text_input('IP Address', )
st.radio("Chose an Option", ['TCP Connect Scan', 'UDP Scan'], horizontal=True)
st.write('IP status: ', scanner[ip_addy].state())



