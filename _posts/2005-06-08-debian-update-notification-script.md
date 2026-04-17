---
layout: post
title: "debian update notification script"
date: 2005-06-08
author: Chris
---
I realized I [mentioned](<https://csblog.quietlife.net/2005/04/28/run-parts/>) this script previously, but never got around to actually posting it.

This is a handy shell script you can use on your Debian system (woody or sarge, or anything that uses apt, really) to check for security (or any other) updates as per whatever repositories you have in your _/etc/apt/sources.list_. I run it from cron nightly. It basically does an "apt-get update", and if there are updates available, it downloads them (but doesn't install), and mails you with the changelogs. If you are satisfied it won't make your server explode, you can simply login to do "sudo apt-get upgrade" to actually install them. It's very handy if you manage a number of servers. The script itself isn't pretty, but what shell script is? Note: it requires apt-listchanges (_apt-get install apt-listchanges_) to do the changelog mailing.

The [source can be found here](<https://csblog.quietlife.net/wp-content/check-apt.txt>).

`  
#!/bin/sh  
#  
# This script checks for updates via apt. If any are found, it does the  
# following:  
#  
# 1) Downloads the packages (but does not install)  
# 2) Pulls the latest from the changelog using apt-listchanges  
# 3) E-mails the results to the address(es) listed in $CONTACT`

CONTACT="your@email.com"  
DATE=`date`  
MACHINE=`hostname`  
HEADER="Debian Package Update\n--------------\nDate: $DATE\nHost: $MACHINE\n\nThe following packages have been updated on the debian.org mirrors and require an update:\n  
"  
FOOTER="The packages have been downloaded locally, but not installed. Please login and run \"apt-get upgrade\" to complete the upgrade."

# First, we update our package lists  
apt-get -qq update 

# If there are new packages, we get them in $NEWPKG. If not, do nothing.  
if apt-get -qq -s upgrade | grep 'Inst' > /dev/null;  
then  
NEWPKG=`apt-get -qq -s upgrade | awk '$1 ~ /Inst/ { print $2}'`  
# This is ugly, so sue me. All output goes to $MESSAGE For ease of  
# e-mailing  
MESSAGE=`  
echo -e $HEADER  
# Only download (-d) new packages very quietly (-qq)  
apt-get -qq -y -d upgrade  
# List the latest change and presumably the reason for upgrading  
for package in $NEWPKG  
do  
apt-listchanges -f text /var/cache/apt/archives/$package* 2>/dev/null  
done  
echo $FOOTER  
`  
IFS=  
# Mail it!  
echo $MESSAGE | mail -s "Debian updates on $MACHINE" $CONTACT  
fi
