import whois
from datetime import datetime
from components import loading

def format_date(date_str):
    if isinstance(date_str, list):
        # If the date is a list, format each item in the list
        return [format_date(item) for item in date_str]
    try:
        if isinstance(date_str, datetime):
            # If the date is already a datetime object, format it directly
            formatted_date = date_str.strftime("%Y-%m-%d %H:%M:%S")
        else:
            # Convert the date string to a datetime object
            date_object = datetime.strptime(str(date_str), "%Y-%m-%d %H:%M:%S")
            # Format the datetime object as a string
            formatted_date = date_object.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_date
    except ValueError:
        return date_str

def get_whois_info(domain):
    try:
        whois_info = whois.whois(domain)
        return whois_info
    except whois.exceptions.FailedParsingWhoisOutput as e:
        if "Domain not found" in str(e):
            return f"Error: Domain not found - {domain}"
        else:
            return f"Error: {e}"

def whios_scan(domain_name):
    loading.loading_animation()
    print(f"\nScanning domain: {domain_name}\n")
    whois_info = get_whois_info(domain_name)

    if isinstance(whois_info, dict):
        for key, value in whois_info.items():
            if key in ['updated_date', 'creation_date', 'expiration_date']:
                formatted_date = format_date(value) if value else "N/A"
                print(f"[+] {key}: {formatted_date}")
            elif key == 'name_servers':
                if isinstance(value, (list, tuple)):
                    print(f"[+] {key}: {', '.join(value)}")
                else:
                    print(f"[+] {key}: {value}")
            else:
                print(f"[+] {key}: {value}")
    else:
        print(whois_info)
