#!/usr/bin/env python3

import requests
import sys
import json

def lookup_ip(ip_address):
    try:
        
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        data = response.json()
        
        
        print("\nIP Information:")
        print("-" * 50)
        print(f"IP Address: {data.get('ip', 'N/A')}")
        print(f"Hostname: {data.get('hostname', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Location: {data.get('loc', 'N/A')}")
        print(f"Organization: {data.get('org', 'N/A')}")
        print(f"Postal Code: {data.get('postal', 'N/A')}")
        print(f"Timezone: {data.get('timezone', 'N/A')}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not fetch IP information - {e}")
    except json.JSONDecodeError:
        print("Error: Invalid response from the server")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <ip_address>")
        sys.exit(1)
    
    ip_address = sys.argv[1]
    lookup_ip(ip_address)

if __name__ == "__main__":
    main()
