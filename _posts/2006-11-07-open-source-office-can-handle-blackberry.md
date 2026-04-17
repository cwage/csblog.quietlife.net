---
layout: post
title: "Open Source Office can handle Blackberry"
date: 2006-11-07
---
CentreSource has jumped on the Blackberry bandwagon! After complaining for months that I spend too much time with email, I gave up trying to avoid the problem and simply decided to further my addiction :) We purchased three new Blackberry 8703e's and have now started the painful process of getting them to work in our Open Source environment. That's right, Blackberries in a world without Outlook and Exchange. The verdict? It works, but not great.  


So, here's our setup:

1) **Email** : This actually works really well. We use IMAP and the Blackberry (through Sprint) has a nice service that allows us to connect to our IMAP server. The Blackberry checks the IMAP Server every 15 minutes and alerts me to the new messages. I set my blackberry up to be the master and it reconciles every 15 minutes. WARNING: This means that my blackberry is actually deleting messages from my IMAP (and to be literal, it is expunging them - so they aren't even in my trash folder). I chose this option so I don't have hundreds of emails waiting on me when I get back to the office. Remember, I can't sync (but that comes later).

2) **Local PIM (personal information management)** : This includes contacts, calendar, tasks, and notes. Simply put, forget about using them. We have two issues that we're up against. First, we use Thunderbird - so we don't have a good option for calendar, tasks, and notes. I hope their progress with [Sunbird and Lightning](<https://web.archive.org/web/20061128142335/http://www.mozilla.org/projects/calendar/>) continues! The calendar isn't as hopeless as Tasks/Notes since the Blackberry can sync with iCal formatted calendars. If you use an iCal compatible Calendar, then you can have your events.

As for locally stored contacts, I couldn't find an easy solution to sync to the Blackberry. The best idea I had was to use [Plaxo's Thunderbird client](<https://web.archive.org/web/20061106071408/http://www.plaxo.com/downloads/tbird>) and access via the web ([premium service](<https://web.archive.org/web/20061106071408/http://www.plaxo.com/premium?src=corp_nav>))

3) **Groupware Server:** If you are using an OpenSource Groupware product, there are more options available for syncing the blackberry. For basic calendars & tasks, the Blackberry will sync with any iCal formatted calendar. To do this, you will need an application like PocketMac.

For a more robust solution, the best option is to setup a Groupware solution that is compatible with a [SyncML server like funambol](<https://web.archive.org/web/20061105193338/http://www.funambol.com/opensource/downloads.html>). There are many solutions available (and even some services like [Zyb](<https://web.archive.org/web/20060816213110/https://zyb.com//>)). We use [eGroupware](<https://web.archive.org/web/20061106200522/http://www.egroupware.org/>) and it [integrates with SyncML](<https://web.archive.org/web/20061010231600/http://www.egroupware.org/index.php?page_name=sync&wikipage=SyncMLFunambol>). For the Blackberry, [SyncBerry [$29.95]](<http://www.handango.com/blackberry/PlatformProductDetail.jsp?siteId=1181&osId=824&jid=F874566CD4856D63E4127X59B1X3AD7A&platformId=5&productType=2&productId=180473&sectionId=0&catalog=40&topSectionId=-1>) provides Over-The-Air (OTA) synchronization with Contacts, Calendar, and Tasks (InfoLog). Once the SyncML server is setup, there are two options for syncing Thunderbird. One is an community supported [Mozilla extension of funambol](<https://web.archive.org/web/20061029175126/http://sourceforge.net/projects/sync4jmozilla>) and the other is a ['beta' application called TSync](<http://www.topologilinux.com/syncml/>). This ensures that the Blackberry & Thunderbird are both sync'd to the corporate groupware package/service.

_Note: I'm writing this article as I research these solutions. We haven't implemented the SyncML server, so I can't vouch for the success of this piece._

4) **Internet Access (Phone)** : This is my favorite part! First, the 8703e has a beautiful screen and it is very easy to access web pages. For our company, we disabled images & their placeholders to increase load speeds. Since we haven't implemented SyncML, everyone simply accesses eGroupware via the phone's web browser. It isn't pretty, but it's functional (especially if you make the calendar display in list view).

**** BONUS****  
This phone actually acts as a wireless Modem on the Sprint Network!!! All of the research I've conducted has been through the phone - connected via a USB cable. The 8703e on Sprint's EDVO network is getting an average of 340kbps - easily enough for basic web usage.

All in all, I think the Blackberry will be a fantastic solution once we have eGroupware+SyncML+SyncBerry+Thunderbird/funambol. In fact, CentreSource will begin providing Nashville clients with installations of the OpenSource combination upon successful implementation.

Until then, it is a great tool for checking IMAP email and accessing the web (via the phone and as a modem).
