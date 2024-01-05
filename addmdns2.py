from zeroconf import Zeroconf, ServiceInfo
import socket

def advertise_airplay_service():
    # Replace the following values with your own information
    service_type = "_airplay._tcp.local."
    base_service_name = "iphone"
    server_name = "DESKTOP-RJEVN3N."
    port = 7000
    properties = {'deviceid':'4D:4F:6C:2B:28:46','flags': '0x44','model': 'AppleTV3,2C','ch': 2,
   'pk': 'fffff1844ff7f31f456fff253af654fffffffea','features': '0x5A7FFFF7,0x1E','srcvers': 220.68
    }

    # Replace with the actual IP address of your PC
    pc_ip_address = "192.168.1.12"

    # Create a Zeroconf instance
    zeroconf = Zeroconf()

    # Advertise multiple services with different names
    
    service_name = f"{base_service_name}._airplay._tcp.local."
    service_info = ServiceInfo(
        service_type,
        service_name,
        addresses=[socket.inet_aton(pc_ip_address)],
        port=port,
        properties=properties,
        server=server_name,
    )
    # Print information about the advertised service
    print(f"Advertising AirPlay service: {service_name} on {pc_ip_address}:{port} with server {server_name}")
    # Register the service
    zeroconf.register_service(service_info)
    service_type = "_raop._tcp.local."
    base_service_name = "4d4f6c2b2846@iphone"
    server_name = "DESKTOP-RJEVN3N."
    port = 7000
    properties = {'vs': 220.68,'sf': '0x44','et': '0,3,5','ft': '0x5A7FFFF7,0x1E',
    'pk': 'fffff1844ff7f31f456fff253af654fffffffea','vv': 2,'am': 'AppleTV3,2C',
    'cn': '0,1,2,3','md': '0,1,2', 'vn': 65537, 'da': 'true', 'tp': 'UDP',
    }

    # Replace with the actual IP address of your PC
    pc_ip_address = "192.168.1.12"

    # Create a Zeroconf instance
    zeroconf = Zeroconf()

    # Advertise multiple services with different names
    service_name = f"{base_service_name}._raop._tcp.local."
    service_info = ServiceInfo(
        service_type,
        service_name,
        addresses=[socket.inet_aton(pc_ip_address)],
        port=port,
        properties=properties,
        server=server_name,
    )
    # Print information about the advertised service
    print(f"Advertising AirPlay service: {service_name} on {pc_ip_address}:{port} with server {server_name}")
    # Register the service
    zeroconf.register_service(service_info)

    try:
        # Wait for user input to stop advertising
        input("Press Enter to stop advertising the AirPlay services...\n")
    finally:
        # Unregister the services and close the Zeroconf instance
        zeroconf.close()

if __name__ == "__main__":
    # Run the function to advertise the AirPlay services
    advertise_airplay_service()
