
# Website Legal Details Extractor

This Python script extracts publicly available legal and technical details from any website. 

It gathers the following information:
- IP Address
- Host details
- WHOIS data (Creation and Last Update dates)
- SSL Certificate details
- HTTP headers
- Website status (up/down)

## Prerequisites

- Python 3.x
- Required libraries: `requests`, `python-whois`, `pyOpenSSL`

## Installation

1. Install Python on Termux (or any other system):

   ```bash
   pkg update && pkg upgrade
   pkg install python
   ```

2. Install required libraries:

   ```bash
   pip install requests python-whois pyOpenSSL
   ```

## Usage

1. Download or clone this repository.

2. Save the Python script file as `website_legal_details.py`.

3. Run the script with the following command:

   ```bash
   python website_legal_details.py
   ```

4. When prompted, enter the website URL to fetch the details.

## Example Output:

```
Enter the website URL: https://example.com
Website Details for: https://example.com
----------------------------------------
IP Address: 93.184.216.34
Host: example.com
Creation Date: 1995-08-04 04:00:00
Last Update: 2023-07-15 12:15:32
SSL Certificate: {'Subject': '<subject_details>', 'Issuer': '<issuer_details>', 'Not Before': '2023-01-01', 'Not After': '2024-01-01'}
HTTP Headers: {'Content-Type': 'text/html; charset=UTF-8', 'Server': 'nginx', ...}
Status Code: 200
Website is Up: Yes
----------------------------------------
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

