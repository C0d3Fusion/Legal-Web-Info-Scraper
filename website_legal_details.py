
import socket
import requests
import whois
import ssl
import datetime
from urllib.parse import urlparse
from OpenSSL import SSL

# Function to get the IP address of the website
def get_ip_address(url):
    try:
        ip = socket.gethostbyname(urlparse(url).hostname)
        return ip
    except Exception as e:
        return f"Error: {e}"

# Function to get the website's host details
def get_host_details(url):
    try:
        host = urlparse(url).hostname
        return host
    except Exception as e:
        return f"Error: {e}"

# Function to get the website's WHOIS data (including creation date and last update)
def get_whois_details(url):
    try:
        domain = whois.whois(url)
        creation_date = domain.creation_date
        last_update = domain.updated_date
        return creation_date, last_update
    except Exception as e:
        return f"Error: {e}"

# Function to get SSL certificate details
def get_ssl_details(url):
    try:
        context = SSL.Context(SSL.SSLv23_METHOD)
        connection = SSL.Connection(context, socket.socket())
        connection.connect((urlparse(url).hostname, 443))
        connection.set_tlsext_host_name(urlparse(url).hostname.encode())
        connection.do_handshake()
        cert = connection.get_peer_certificate()
        cert_info = {
            "Subject": cert.get_subject(),
            "Issuer": cert.get_issuer(),
            "Not Before": cert.get_notBefore().decode(),
            "Not After": cert.get_notAfter().decode(),
        }
        return cert_info
    except Exception as e:
        return f"Error: {e}"

# Function to get HTTP headers
def get_http_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        return headers
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Function to get the website's details and check for bugs
def get_website_details(url):
    details = {}
    
    # Get IP address
    details['IP Address'] = get_ip_address(url)
    
    # Get host details
    details['Host'] = get_host_details(url)
    
    # Get WHOIS details
    creation_date, last_update = get_whois_details(url)
    details['Creation Date'] = creation_date if creation_date else "N/A"
    details['Last Update'] = last_update if last_update else "N/A"
    
    # Get SSL certificate details
    details['SSL Certificate'] = get_ssl_details(url)
    
    # Get HTTP headers
    details['HTTP Headers'] = get_http_headers(url)
    
    # Get status code of the website
    try:
        response = requests.get(url)
        details['Status Code'] = response.status_code
        details['Website is Up'] = 'Yes' if response.status_code == 200 else 'No'
    except requests.exceptions.RequestException as e:
        details['Status Code'] = "Error"
        details['Website is Up'] = 'No'
        details['Error Message'] = str(e)
    
    return details

# Function to display the website's details
def display_website_details(url):
    print(f"Website Details for: {url}")
    print("-" * 40)
    details = get_website_details(url)
    
    for key, value in details.items():
        print(f"{key}: {value}")
    print("-" * 40)

# Main function
def main():
    url = input("Enter the website URL: ")
    display_website_details(url)

if __name__ == "__main__":
    main()
