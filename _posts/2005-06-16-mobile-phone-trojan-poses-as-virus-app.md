---
layout: post
title: "Mobile phone Trojan poses as Virus App"
date: 2005-06-16
---
Will the fun ever end? I continue to marvel at the extent to which security (or lack thereof) affects our lives. Now our mobile phones are not safe...

[eWeek's writeup](<http://www.eweek.com/article2/0,1759,1827394,00.asp>) states:

> The latest mutant, identified as Skulls.L, pretends to be a pirated copy of the F-Secure Mobile Anti-Virus application, a sign that virus writers targeting cell-phone users are borrowing well-known replication tactics from computer viruses.
> 
> According to an advisory from F-Secure, Skulls.L provides a new twist on previous versions by masquerading as a mobile protection installation package. The Trojan, which arrives as a SIS file, also displays dialog text that reads: "F-Secure Antivirus protect you against the virus. And don't forget to update this!" 

The worst part of this Virus/Trojan is its payload - the Cabir worm. This worm attempts to spread itself via Bluetooth.

> Cabir, originally detected last June, uses the Bluetooth wireless peer protocol to propagate, copying itself to other Bluetooth devices as far as 30 feet away, depending on the environment.
> 
> According to Niemela, the two Cabir variants dropped by the Trojan do not activate automatically, and will not activate on reboot. He said the worms will activate only if the infected user goes to the icon of the dropped Cabir file and runs it from there. 

_Where there's a will, there's a security hole..._
