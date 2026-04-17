---
layout: post
title: "Windows Update Sucks: Error 0x8DDD0007"
date: 2005-09-13
categories: [Windows]
---
At 2AM in the morning, I had a Eureka about the future of computing. As things get easier and easier for users - the art of troubleshooting and problem conveyance (yes, the conveying of errors by software) will diminish!

Today at school, my wife was unexplainably blocked from Internet Access. She contacted the IT department and they told her that she either had a virus, malicious spyware, or needed to upgrade to SP2. Ironic bed-fellows...

After running scans with [Spy-bot](<http://www.safer-networking.org/en/index.html>) and [Ad-aware](<http://www.lavasoft.de/>), I visit Trend Micro's [Housecall ](<https://web.archive.org/web/20050913182441/http://housecall.trendmicro.com/>)(which is fantastic) for a comprehensive scan. Everything checked out ok... Now on to Windows Update for SP2.

While the site is 'Checking for Updates', I get the following message displayed for error 0×8DDD0007:

> "You need to restart your computer to finish installing a program or updates. You cannot view or get other updates from the site until you restart" 

Easy enough... I restart and repeat. Same error. Let's try one more time - hell, its Microsoft. Still no dice!

Naturally, I'll thought I'd find this error code in the Microsoft Knowledge base. No luck there either... both the error code and text search string came up blank.

Save me Obi-Wan-[Google](<https://web.archive.org/web/20050913215954/http://www.google.com/>), you're my only hope! I type the error code into Google and [find the answer](<https://web.archive.org/web/20060130120056/http://www.geekstogo.com/forum/index.php?showtopic=47526>)!

1) Start -> Run -> regedit (Enter)  
2) Navigate to:  
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion  
\WindowsUpdate\Auto Update  
3) The Folder 'RebootRequired' should be visible  
4) Right Click Folder -> Delete

Voila! Windows Update works again!

Wow, how in the hell would anyone know how to fix that? I miss the old days - these newfangled 'easy to use' systems basically leave me with a 10 Digit Obscure error message, don't have any info in the product knowledge base, and force me to delete keys from the most dangerously delicate part of the system...

The part that really pisses me off is that this is the 2nd 'dead-end' type problem I've had with Windows Update. How can Microsoft force everyone to use their 'Active X' driven Update site - but not give alternative methods for updating.

Grrr....
