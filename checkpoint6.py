import socket

UDP_IP = "10.248.153.146" # Replace with the Receiver's actual IP
UDP_PORT = 5005
SENDER_ID = "Sender_Sofia"  # Change to 2 and 3 on the other laptops

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Starting UDP Flood ...")
# Send 10,000 packets as fast as possible
for i in range(1, 10001):
    # Include a sequence number in the payload
    message = f"{SENDER_ID} - Packet {i}".encode()
    sock.sendto(message, (UDP_IP, UDP_PORT))

print("Transmission complete.")
sock.close()