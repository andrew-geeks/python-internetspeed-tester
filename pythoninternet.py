import speedtest

st = speedtest.Speedtest()
#all results will be shown in mbps

print('Download Speed:',st.download()) #download speed
print('Upload Speed:',st.upload()) #upload speed

snames = []
st.get_servers(snames)
print('Ping:',st.results.ping) #ping
