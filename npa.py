from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {proto}")

print("Starting packet capture... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=0)


