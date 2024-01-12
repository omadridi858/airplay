from zeroconf import Zeroconf, ServiceInfo,ServiceBrowser
import socket
import requests
import ee

def advertise_airplay_services():
    # Replace the following values with your own information
    server_name = "DESKTOP-RJEVN3N."
    port = 7000

    # Replace with the actual IP address of your PC
    pc_ip_address = "192.168.1.12"

    # Create a Zeroconf instance
    zeroconf = Zeroconf()

    

    # Advertise Apple TV 3 service
    service_type_atv3 = "_airplay._tcp.local."
    service_name_atv3 = "AppleTV3"
    properties_atv3 = {
        'deviceid': '4D:4F:6C:2B:28:46',

'features':' 0xFFFFFFFF'

    }
    service_info_atv3 = ServiceInfo(
        service_type_atv3,
        f"{service_name_atv3}._airplay._tcp.local.",
        addresses=[socket.inet_aton(pc_ip_address)],
        port=port,
        properties=properties_atv3,
        server=server_name,
    )
    zeroconf.register_service(service_info_atv3)
    print(f"Advertising AirPlay service: {service_name_atv3} on {pc_ip_address}:{port} with server {server_name}")
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
    discover_bonjour_services()
class MyListener:
    def remove_service(self, zeroconf, type, name):
        print(f"Service {name} removed")

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info:
            ip_address = ".".join(map(str, info.parsed_addresses()[0]))
            print(ip_address)
            c = 0
            new_ip_address = ""

            for char in ip_address:
                if char!= '.':

                    new_ip_address += char
                else:
                    c += 1
                    new_ip_address += ''
                    if c == 3:

                        new_ip_address += '.'
                    if c>=3:
                        c = 0


                
            port = info.port
            print(f"{new_ip_address}:{port}")
            ee.g(port)

    def update_service(self, zeroconf, type, name):
        pass  # Empty method to avoid FutureWarning

def discover_bonjour_services():
    zeroconf = Zeroconf()
    listener = MyListener()

    print("Scanning for Bonjour services. Press Ctrl+C to stop.")

    browser_raop = ServiceBrowser(zeroconf, "_dacp._tcp.local.", listener)

    try:
        input("Press Enter to stop scanning...\n")
    except KeyboardInterrupt:
        pass
    finally:
        zeroconf.close()




if __name__ == "__main__":
    # Run the function to advertise the AirPlay services
    advertise_airplay_services()
