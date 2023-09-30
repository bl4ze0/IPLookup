import whois
import geocoder

print("Welcome to BLZ, an IP Lookup tool made by bl4ze.")
print("Please use it only for educational purposes!")
print("I don't take any responsabilities of the usage of this tool. \n\n")

def get_ip_info(ip_address):
    try:
        domain_info = whois.whois(ip_address)
        
        location = geocoder.ip(ip_address)
        
        print("IP Information:")
        print(f"The IP: {ip_address}")
        print(f"Domain Name: {domain_info.get('domain_name')}")
        print(f"Registrant: {domain_info.get('registrant_name')}")
        print(f"Organization: {domain_info.get('org')}")
        print(f"City: {location.city}")
        print(f"Country: {location.country}")
        print(f"Latitude: {location.latlng[0]}")
        print(f"Longitude: {location.latlng[1]}")
        
    except Exception as e:
        print(f"An Error Occured: {str(e)}")

if __name__ == "__main__":
    ip_address = input("Enter an IP address: ")
    get_ip_info(ip_address)