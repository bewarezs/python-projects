import requests

ip = input("Enter the IP address to track: ")
response = requests.get(f"http://ip-api.com/json/{ip}")

data = response.json()
print("IP:", data["query"])
print("country:", data["country"])
print("city:", data["city"])
print("ISP:", data["isp"])  
print("region:", data["region"])
print("cordinates:", f"{data['lat']}, {data['lon']}")

