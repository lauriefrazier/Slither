# INF 601 Advanced Programming with Python
# Laurie Frazier
# Final Project: Slither


### Please commit these before you start:
````
pip install -r
````
### To run the program, in the terminal please run. This will load a link to use on the local URL on localhost:8502 or on a network url ending in 8502. 8520 is Streamlit's platform for web deployment.
````
streamlit run main.py
````
### Please also insure you have NMAP installed into your PATH on your device. You will also need to be hardwired into your internet in order for the scans to work. If you need to install NMAP, please [click here](https://nmap.org/download).
## Purpose of Project
Slither uses a NMAP API and displays your TCP Connect Scan or UDP Scan in a easy visual to understand quickly what your network has. 
Slither runs a scan through a IP address given by the user and runs it through the top 50 ports being used on your device.