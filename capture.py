#!/usr/bin/python3

from scapy.all import *

interfaces = ["eth0", "lo"]
capture = sniff (iface = interfaces, count = 100)
wrpcap("capturestocker.pcap", capture)

