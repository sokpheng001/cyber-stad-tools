import re

def is_valid_domain_name(domain)-> bool:
    # Regular expression for a simple check on a domain name
    domain_regex = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Use re.match to check if the string matches the regular expression
    match = re.match(domain_regex, domain)
    
    # check if the domain
    if match is not None:
        return match is not None;
    else:
        return False;
    
    # If match is not None, the string is a valid domain name
    # 
    # return match is not None

# Test the function
