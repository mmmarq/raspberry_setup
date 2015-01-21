#!/bin/bash
set -e

# Raspberry Pi dnsmasq script
# Stephen Wood
# www.heystephenwood.com
#
# Usage: $ sudo ./dnsmasq_install
#
# Net install:
#   $ curl https://raw.github.com/stephendotexe/raspberrypi/master/roles/dnsmasq_server | sudo sh

# Must be run as root
if [[ `whoami` != "root" ]]
then
  echo "This install must be run as root or with sudo."
  exit
fi

apt-get install -y dnsmasq

cat - > /etc/dnsmasq.conf <<DNSMASQCONF
# Dnsmasq.conf for raspberry pi
# By Stephen Wood heystephenwood.com
# Full examples found here:
# http://www.thekelleys.org.uk/dnsmasq/docs/dnsmasq.conf.example

# Set up your local domain here
domain=raspberry.local
resolv-file=/etc/resolv.dnsmasq
min-port=4096
server=8.8.8.8
server=8.8.4.4

# Max cache size dnsmasq can give us, and we want all of it!
cache-size=10000

# Below are settings for dhcp. Comment them out if you dont want
# dnsmasq to serve up dhcpd requests.
# dhcp-range=192.168.0.100,192.168.0.149,255.255.255.0,1440m
# dhcp-option=3,192.168.0.1
# dhcp-authoritative

DNSMASQCONF

service dnsmasq restart

echo "Testing dns performance with random urls"

# We'll generate a list of urls that we're moderately certain doesn't exist in our cache to get a good base line for speed increases.
URLS=`for i in {1..50}; do echo www.$RANDOM.com;done`

# Make the requests in parallel
echo $URLS | xargs -I^ -P50 dig @127.0.0.1 grep time | awk /time/'{sum+=$4} END { print "average response = ", sum/NR,"ms"}'
echo $URLS | xargs -I^ -P50 dig @127.0.0.1 grep time | awk /time/'{sum+=$4} END { print "average response = ", sum/NR,"ms"}'
echo $URLS | xargs -I^ -P50 dig @127.0.0.1 grep time | awk /time/'{sum+=$4} END { print "average response = ", sum/NR,"ms"}'

echo 'Installation complete. Enjoy!'
