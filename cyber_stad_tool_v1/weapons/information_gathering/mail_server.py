import dns.resolver

def find_mx_records(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        print(f"Domain name for MX records: {domain}\n")

        for mx_record in mx_records:
            print(f"MX: {mx_record.exchange} (Priority: {mx_record.preference})")

    except dns.resolver.NXDOMAIN:
        print(f"Domain '{domain}' not found.")
    except dns.resolver.NoAnswer:
        print(f"No MX records found for '{domain}'.")
    except dns.exception.DNSException as e:
        print(f"Error: {e}")

