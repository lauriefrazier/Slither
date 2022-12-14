
        try:
            if scan[ip_addy]['tcp'].keys() and scan[ip_addy].state():
                state = st.write('State: ', scan[ip_addy].state())
                st.write(scan[ip_addy]['tcp'][1-1024]['state'])
                tdf = pd.DataFrame({'Open Ports', scan[ip_addy]['tcp'].keys(),
                                    'Service', scan[ip_addy].service()})
                # tdf.style.applymap(color_condition)
                st.table(tdf)
            else:
                st.write("Nothing found!")
        except:
            st.write("Nothing found!")