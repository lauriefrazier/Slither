import streamlit as st
import nmap
scan = nmap.PortScanner()
import pandas as pd

st.title('Slither')
st.subheader('INF 601 -  Advanced Programming with Python Final Project')
st.caption('Slither uses a NMAP API and displays an interactive '
           'table with easy visuals crossing over multiple IP addresses'
           ' under a SYN ACK, UDP or a Comprehensive Scan.'
           ' Slither runs a scan through a IP address given by the user and runs it '
           'through the top 50 ports being used.')
ip_addy = st.text_input('IP Address', )
protocol = st.radio("Chose an Option", ['TCP Connect Scan', 'UDP Scan'], horizontal=True)

st.write('IP status: ', scan[ip_addy].state())


if protocol == 'TCP Connect Scan':

    scan.scan(ip_addy, '--top-ports 50', '-v -sT')

    tdf = pd.DataFrame({"Open Ports: ", scan[ip_addy]['tcp'].keys(),
                        'State', [scan[ip_addy].state()]})
    tdf.style.applymap(color_condition)
    st.table(tdf)


elif protocol == 'UDP Scan':
    udf = pd.DataFrame({'Port': [20, 28],
                        'Service': [11, 8],
                        'Version': [8, 2]}, )
    udf.style.applymap(color_condition)
    st.table(udf)

else:
    st.write('Please')
