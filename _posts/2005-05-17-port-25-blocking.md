---
layout: post
title: "port 25 blocking"
date: 2005-05-17
author: Chris
---
The [debate over ISPs blocking SMTP port 25](<http://www.broadbandreports.com/shownews/63606>) is raging further over at Broadbandreports.

Frankly, it seems a bit silly to me -- ISPs with a spam problem as extensive as Comcast's should not have to think twice about this. Port 25 **outbound** should be blocked except to their mail relays, period. I don't understand why this would be a problem. Anyone running a mailserver can configure it to smarthost to the mailservers provided by the ISP.

The counter to this is that the mailservers provided are not always reliable. This may be true, but alas, that should be a factor in your decision to use Comcast at all -- not in your opinion of whether they should block port 25.

Another concern often cited is privacy -- that by smarthosting your mail through your ISP's mailserver, they have the ability to monitor your e-mail. This, too, is rather silly. SMTP is a plaintext protocol. If you're worried about privacy with e-mail, relaying to your ISP is the least of your problems. You should be using [PGP](<https://web.archive.org/web/20050517083455/http://www.gnupg.org/>).

Lastly, people claim that it will do little good as viruses and spammers get smart enough to use the ISP's mailservers rather than sending directly anyway. This may be true, but something is better than nothing.

I am a big fan of the hands-off unfettered just-the-bandwidth-and-IP-please approach to ISPs, but in this day and age with a network as large as Comcast's, blocking outbound port 25 is the least it can do to be polite to the rest of the Internet that suffers at the hands of the spam resulting from their infected/compromised machines. Simply blocking port 25 reactively is not enough -- by the time an infected machine has been identified, the damage is already done (people have been spammed). It should have never had a chance.
