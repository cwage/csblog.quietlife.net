---
layout: post
title: "debian volatile"
date: 2005-06-07
author: Chris
---
One of the nicer developments with the release of Debian 3.1 is that they have also introduced the concept of ["volatile" packages](<http://volatile.debian.net/>) (for both woody and sarge):

> Some packages aim at fast moving targets like spam filtering and virus scanning, and even via using updated virus patterns, this doesn't really work for the full time of a stable release. The main issue of volatile is to allow system administrators to update their systems in a nice, consistent way without getting the drawbacks of using unstable, even without getting the drawback for the selected packages. 

It should be noted, though, that this is **not** just another place for "backports" -- presumably (hopefully!) [backports.org](<http://www.backports.org/>) will soon pick up where it left off for sarge updates as it did for woody eventually. The idea behind the volatile mirrors is a place for packages that contain "volatile" data by their very nature. ClamAV is a great example -- frequently, changes to the signature database require updated clamav binaries to maintain 100% functionality.

So, how do you use it? For example, on my laptop I have various clamav packages installed:

> $ dpkg -l | grep clamav  
>  ii clamav 0.84-2 antivirus scanner for Unix  
>  ii clamav-base 0.84-2 base package for clamav, an anti-virus utili  
>  ii clamav-freshcl 0.84-2 downloads clamav virus databases from the In  
>  ii libclamav1 0.84-2 virus scanner library 

By adding the volatile mirrors (See their [mirrors list](<http://volatile.debian.net/mirrors.html>)) to my /etc/apt/sources.list:

> deb http://ftp2.de.debian.org/debian-volatile sarge/volatile main  
>  deb-src http://ftp2.de.debian.org/debian-volatile sarge/volatile main 

and performing "apt-get -s upgrade" I see that it gives me more recent clamav packages:

> # apt-get -s upgrade  
>  Reading Package Lists... Done  
>  Building Dependency Tree... Done  
>  The following packages will be upgraded:  
>  clamav clamav-base clamav-freshclam libclamav1  
>  4 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.  
>  Inst libclamav1 [0.84-2] (0.85.1-0volatile1 debian-volatile:sarge)  
>  Inst clamav-freshclam [0.84-2] (0.85.1-0volatile1 debian-volatile:sarge) []  
>  Inst clamav-base [0.84-2] (0.85.1-0volatile1 debian-volatile:sarge)  
>  Inst clamav [0.84-2] (0.85.1-0volatile1 debian-volatile:sarge)  
>  Conf libclamav1 (0.85.1-0volatile1 debian-volatile:sarge)  
>  Conf clamav-base (0.85.1-0volatile1 debian-volatile:sarge)  
>  Conf clamav-freshclam (0.85.1-0volatile1 debian-volatile:sarge)  
>  Conf clamav (0.85.1-0volatile1 debian-volatile:sarge) 

Pretty cool! One side note: it appears that "stable" still points at "woody" on some of the volatile mirrors, so be aware of that and explicitly pick either "sarge" or "woody" depending on what you want.
