Title: Check DNS et IP
Date: 2023-06-09 11:13
Category: Python
Lang: fr
Tags: dns, check


# Prerequis
 * python3
 * module python `nslookup`
 * un dossiern results pour stocker les résultats
 
 Le script Lit un csv en entrée et eécrit les résultats au fur et à mesure.
 
# Script
 
```python
import os
import csv
from nslookup import Nslookup
dns_query = Nslookup()


def ping_ko( ip ):
    response = os.popen(f"ping -c 4 {ip} ").read()
    for line in  response.splitlines():
        print(line)
        if "Request timed out." in line:
            return True
        if "unreachable" in line:
            return True
        if "4 packets transmitted, 0 received" in line:
            return True
    return False

def main( csv_file, host_field = "host" ):
    with open( csv_file ) as csv_open:
        reader = csv.DictReader( csv_open )
        for row in reader:
            ips_record = dns_query.dns_lookup(row[host_field])
            print( row[host_field], ips_record.response_full, ips_record.answer )
            if not ips_record.answer:
                DNS_KO = open( "results/dns_ko.txt", "a" )
                DNS_KO.write( f"{row[host_field]}\n" )
                DNS_KO.close()
                continue
            if ping_ko( ips_record.answer[0] ):
                PING_KO = open( "results/ping_ko.txt", "a" )
                PING_KO.write( f"{row[host_field]}\n" )
                PING_KO.close()
            else:
                PING_OK = open( "results/ping_ok.txt", "a" )
                PING_OK.write( f"{row[host_field]}\n" )
                PING_OK.close()


if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser(description = 'Test DNS reachable servers')
    parser.add_argument('csv', help='List of servers given by Splunk csv file')
    parser.add_argument('--host', help='Name of the host column', default="host")
    args = parser.parse_args()

    main( args.csv, host_field=args.host )
```
