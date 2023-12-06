import requests
import socket
# class Website_Information:
def get_ip_info(target):
    api_key = "347f37bcee78b6"  # Replace with your ipinfo.io API key (optional but recommended for extended usage)

    try:
        # Check if the target is an IP address or a domain name
        try:
            ip_address = socket.gethostbyname(target)
        except socket.gaierror:
            ip_address = None

        if ip_address:
            api_url = f"http://ipinfo.io/{ip_address}?token={api_key}"
        else:
            api_url = f"http://ipinfo.io/{target}?token={api_key}"
            print(f"Domain '{target}' not found.")

        response = requests.get(api_url)
        data = response.json()

        # Extract relevant information
        ip_address = data.get("ip", "N/A")
        ipv6_address = data.get("ip6", "N/A")
        ip_location = data.get("loc", "N/A")
        reverse_dns = data.get("hostname", "N/A")
        top_level_host_usage = data.get("org", "N/A")
        hosting_company = data.get("org", "N/A")
        hosting_ip_range = data.get("range", "N/A")
        hosting_address = data.get("loc", "N/A")
        hosting_country = data.get("country", "N/A")
        hosting_phone = data.get("phone", "N/A")
        hosting_website = data.get("website", "N/A")
        hosting_cidr = data.get("cidr", "N/A")
        whois_record_created = data.get("created", "N/A")
        whois_record_updated = data.get("updated", "N/A")

        # Print the information if it's not "N/A"
        if ip_address != "N/A":
            print(f"IP Address: {ip_address}")
        if ipv6_address != "N/A":
            print(f"Linked IPv6 Address: {ipv6_address}")
        if ip_location != "N/A":
            print(f"IP Location: {ip_location}")
        if reverse_dns != "N/A":
            print(f"IP Reverse DNS (Host): {reverse_dns}")
        if top_level_host_usage != "N/A":
            print(f"Top Level Host Usage: {top_level_host_usage}")
        if hosting_company != "N/A":
            print(f"Hosting Company: {hosting_company}")
        if hosting_ip_range != "N/A":
            print(f"Hosting IP Range: {hosting_ip_range}")
        if hosting_address != "N/A":
            print(f"Hosting Address: {hosting_address}")
        if hosting_country != "N/A":
            print(f"Hosting Country: {hosting_country}")
        if hosting_phone != "N/A":
            print(f"Hosting Phone: {hosting_phone}")
        if hosting_website != "N/A":
            print(f"Hosting Website: {hosting_website}")
        if hosting_cidr != "N/A":
            print(f"Hosting CIDR: {hosting_cidr}")
        if whois_record_created != "N/A":
            print(f"Whois Record Created: {whois_record_created}")
        if whois_record_updated != "N/A":
            print(f"Whois Record Updated: {whois_record_updated}")

    except Exception as e:
        print(f"Error: {e}")

