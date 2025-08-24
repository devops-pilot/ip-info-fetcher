#!/usr/bin/env python3

import requests

def get_ip_info():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()

        if data["status"] == "success":
            print(f"🌐 IP Address: {data['query']}")
            print(f"📍 Location  : {data['city']}, {data['regionName']}, {data['country']}")
            print(f"🏢 Internet service provider       : {data['isp']}")
            print(f"🛰️  Lat/Lon  : {data['lat']}, {data['lon']}")
        else:
            print("Failed to fetch IP info.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_ip_info()
