---
layout: post
title: "iptables firewall"
date: 2005-04-25
author: Chris
categories: [Networking, Linux/BSD]
---
Most of my Linux/BSD servers are convenient located in a network I control, usually behind an [OpenBSD](<http://www.openbsd.org/>) firewall (the only way to fly) that protects it from the big, bad internet. But more and more I have been using servers located in colo facilities in a network I don't control.

For those situations, locking down the box's networking with a simple iptables ruleset is the obvious choice. Naturally, a server should always be thoroughly [locked down](<http://chris.quietlife.net/2003/12/18/securing-a-linux-box-in-the-great-wide-open/>) before you rely on a firewall of any sort, but the iptables rules adds another layer of security.

There are many good hardening toolkits out there like [Bastille](<http://www.bastille-linux.org/>), but frankly I have always found them to be overkill. In addition, I prefer to do things manually, since then I also have the confidence they were done properly. In any event, here is the shell of an iptables script that I use to lock down new servers:

  
`  
!/bin/sh`

# chkconfig: - 60 95  
# description: Starts and stops iptables firewalls

if [ ! -x /sbin/iptables ]; then  
exit 0  
fi  
# See how we were called.  
case "$1" in  
start)

# chain policies  
# set default policies  
/sbin/iptables -P INPUT DROP  
/sbin/iptables -P OUTPUT ACCEPT  
/sbin/iptables -P FORWARD DROP 

# flush tables  
/sbin/iptables -F  
/sbin/iptables -F INPUT  
/sbin/iptables -F OUTPUT  
/sbin/iptables -F FORWARD  
/sbin/iptables -F -t mangle  
/sbin/iptables -X  
/sbin/iptables -F -t nat

# create DUMP table  
/sbin/iptables -N DUMP > /dev/null  
/sbin/iptables -F DUMP  
/sbin/iptables -A DUMP -p tcp -j LOG  
/sbin/iptables -A DUMP -p udp -j LOG  
/sbin/iptables -A DUMP -p tcp -j REJECT -reject-with tcp-reset  
/sbin/iptables -A DUMP -p udp -j REJECT -reject-with icmp-port-unreachable  
/sbin/iptables -A DUMP -j DROP

# Stateful table  
/sbin/iptables -N STATEFUL > /dev/null  
/sbin/iptables -F STATEFUL  
/sbin/iptables -I STATEFUL -m state -state ESTABLISHED,RELATED -j ACCEPT  
/sbin/iptables -A STATEFUL -m state -state NEW -i ! eth0 -j ACCEPT  
/sbin/iptables -A STATEFUL -j DUMP

# loopback rules  
/sbin/iptables -A INPUT -i lo -j ACCEPT  
/sbin/iptables -A OUTPUT -o lo -j ACCEPT

# Allow ICMP requests  
/sbin/iptables -A INPUT -i eth0 -p icmp -icmp-type echo-request -j ACCEPT  
# Allow ICMP type destination unreachable fragmentation-needed to support PMTU  
/sbin/iptables -A INPUT -i eth0 -p icmp -icmp-type fragmentation-needed -j ACCEPT

# Allow ssh from a certain host  
/sbin/iptables -A INPUT -p tcp -i eth0 -s 1.2.3.4/32 -dport 22 -j ACCEPT

# Allow SMTP  
/sbin/iptables -A INPUT -p tcp -i eth0 -dport 25 -j ACCEPT

# Allow HTTP  
/sbin/iptables -A INPUT -p tcp -i eth0 -dport 80 -j ACCEPT

# Allow HTTPS  
/sbin/iptables -A INPUT -p tcp -i eth0 -dport 443 -j ACCEPT

# Allow DNS  
/sbin/iptables -A INPUT -p udp -i eth0 -dport 53 -j ACCEPT

# Allow TCP DNS from AXFR hosts  
/sbin/iptables -A INPUT -p tcp -i eth0 -s 1.2.3.4/32 -dport 53 -j ACCEPT

# Allow IMAP  
/sbin/iptables -A INPUT -p tcp -i eth0 -dport 143 -j ACCEPT

# Allow IMAP/SSL  
/sbin/iptables -A INPUT -p tcp -i eth0 -dport 993 -j ACCEPT

# Don't log route packets coming from routers - too much logging  
/sbin/iptables -A INPUT -p udp -i eth0 -dport 520 -j REJECT

# Don't log smb/windows sharing packets - too much logging  
/sbin/iptables -A INPUT -p tcp -i eth0 -dport 137:139 -j REJECT  
/sbin/iptables -A INPUT -p udp -i eth0 -dport 137:139 -j REJECT

#Don't log auth requests - too much loging  
/sbin/iptables -A INPUT -p tcp -i eth0 -dport 113 -j REJECT -reject-with tcp-reset

# push everything else to state table  
/sbin/iptables -A INPUT -j STATEFUL

;;  
stop)  
echo -n "Shutting down firewall: "

# chain policies  
# set default policies  
/sbin/iptables -P INPUT ACCEPT  
/sbin/iptables -P OUTPUT ACCEPT  
/sbin/iptables -P FORWARD DROP 

# flush tables  
/sbin/iptables -F  
/sbin/iptables -F INPUT  
/sbin/iptables -F OUTPUT  
/sbin/iptables -F FORWARD  
/sbin/iptables -F -t mangle  
/sbin/iptables -X  
/sbin/iptables -F -t nat  
;;  
status)  
status firewall  
;;  
restart|reload)  
$0 stop  
$0 start  
;;  
*)  
echo "Usage: firewall {start|stop|status|restart|reload}"  
exit 1  
esac

exit 0
