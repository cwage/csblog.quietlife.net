---
layout: post
title: "OpenBSD 3.7 Release"
date: 2005-05-02
author: Chris
categories: [Linux/BSD]
---
Undeadly is [reporting](<https://web.archive.org/web/20060427145131/http://undeadly.org/cgi?action=article&sid=20050502152347>) that [OpenBSD 3.7](<https://web.archive.org/web/20050507063400/http://www.openbsd.org/37.html#new>) CDs have begun arriving. Among the new features are some interesting ones:

New iwi(4) driver for Intel PRO/Wireless 2200BG/2225BG/2915ABG IEEE 802.11a/b/g wireless network adapters.
    There goes one excuse for me to not to be running OpenBSD on my laptop..
ospfd(8), implementing the OSPFv2 routing protocol.
    This is great news. Previously OpenBSD only was capable of doing RIP, RIP-2 and BGP so this is welcome news. The only alternative is using [GNU Zebra](<http://www.zebra.org/>), which is nice, but clunky.
In-kernel pppoe(4) support.
    This good news for me, as I use OpenBSD as my firewall and I'm thinking about moving to [butler.net](<https://web.archive.org/web/20050407072207/http://www.butler.net/>)'s 3Mbps/384Kbps service, which requires PPPoE

There are also a bunch of improvements to pf, CARP, isakmpd, spamd and lots of other goodies. Check it out!
