---
layout: post
title: "MS Access Error: Disk or network error."
date: 2005-11-14
categories: [Networking, Windows, Utilities]
---
One of our clients called and reported an issue with a MS Access database. The user was able to open a network based .mdb file, but when they tried to click on a switchboard button they received the following error message: "Disk or network error." There are many resources that deal with this error, but none of them provided the needed solution. The TMP/TEMP directories were set properly, the JET Engine was updated, and the .mdb file was not corrupted (verified on another computer).

Through basic troubleshooting, we determined that this .mdb file had many 'Linked' tables that were using a static network path mapped through drive E:\\. The problem was occurring on a new machine that I quickly noticed did not have a mapped drive 'E:\' because E: was assigned to a secondary CD-R drive. For this machine, access to the network drive was a UNC path.

To remedy the problem, I had to have the MS Office XP disk to install the 'Linked Table Manager'. Once this was installed, I updated all linked tables to use the UNC path and not the static E:\ path. To my relief, it corrected the 'Disk or network error.' problem.

It's amazing how every resource on the Internet didn't help me address the most simple problem :)
