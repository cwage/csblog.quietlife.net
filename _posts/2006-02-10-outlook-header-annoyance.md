---
layout: post
title: "Outlook Header Annoyance"
date: 2006-02-10
author: Chris
categories: [Software, Windows]
---
One of the worst thing Microsoft Outlook ever did for the Internet was decide that when someone forwards a message, they don't need to include any of the SMTP headers along with it.

This, of course, renders the message useless to any poor administrator trying to track down a problem that a user is reporting. When someone, for example, forwards a message and says "Hey, I keep getting this spam message -- can you do something about it?", this is what it looks like from Outlook:
    
    
    -----Original Message-----
    From: Michelle Spitzer [mailto:Michelle.Spitzer@ptassoc.com]
    Sent: Thursday, February 09, 2006 10:00 PM
    To: undisclosed-recipients:
    Subject: Live webcast: Customer Relationship Management (CRM) for
    Associations
    

Can anything be done based on this? Nope. There is approximately zero information of value for any troubleshooting in this. The result is that helpdesks have to resort to convoluted instructions, for example [here](<https://web.archive.org/web/20060111175151/http://micro.uoregon.edu/fullheaders/>), where they have a simple _7 step process_ for the user to dig up the headers from the bowels of the Outlook menus, copy them, and manually paste into a message to report.

It was really a silly decision on behalf of Microsoft. There was no reason to _remove_ the headers -- they could have at least merely _hidden_ them. But hey, I guess Microsoft figured we'd all be using [MAPI](<https://web.archive.org/web/20051215000000/http://en.wikipedia.org/wiki/MAPI>) by now rather than that pesky open standard, SMTP, anyway, right?
