---
layout: post
title: "microsoft rolls sender-ID"
date: 2005-06-23
author: Chris
---
Despite the fact that talks to agree on a standard more or less fizzled, evidently Microsoft has decided to [implement sender-ID checking](<http://www.broadbandreports.com/shownews/64851>) for Hotmail/MSN mail, effectively junking any message from a domain not implementing sender-ID.

Seeing as how sender-ID has very little adoption so far, this bodes poorly for the number of false positives they will see as a result. Whatever you think of sender-ID/SPF, this move seems extremely premature. I have a feeling Microsoft will regret this little episode of arrogance.

**UPDATE:** I guess a little background might be helpful. Sender-ID is Microsoft's **patented** implementation of a system similar to SPF/Domainkeys, which I have [discussed](<http://blog.centresource.com/2005/06/02/dkimdomainkeys/>) the up/downsides of in the past. The key here is that talks fizzed because of Microsoft's patent claims on the particular details of Sender-ID, effectively making it un-implementable for any open-source software or distribution with a license that forbids it. You can see now perhaps how this move is extremely bizarre, to say the least. I have to say that Microsoft can sometimes be arrogant or downright evil, but they are rarely stupid. What gives?
