---
layout: post
title: "siteground's braindead spam-filtering"
date: 2007-06-29
author: Chris
---
We have a customer of ours who pays us both for e-mail/web hosting as well as our anti-spam/anti-virus relay service, [Swirbo](<https://web.archive.org/web/20070628164348/http://www.swirbo.com/>). Swirbo is a service that filters mail by having mail for a domain sent to it first, via MX records, and then relayed to its final destination.

Recently, this customer began reporting that she was unable to receive e-mail from certain people. Some investigation yielded this information from Swirbo, while attempting to deliver a legit e-mail message from someone on aol.com:

> Jun 14 10:50:10 mta1 postfix/smtp[5285]: 90D0D834038: to=, relay=redacteddomain.com[1.2.3.4], delay=3, status=bounced (host redacteddomain.com[1.2.3.4] said: 550 SITEGROUND Faked AOL, so you must be spam. (in reply to RCPT TO command))  
> 

This error message was not exactly clear, so I was forced to contact Siteground to try to determine why they were blocking this mail. Unfortunately, Siteground has no support number to call, or e-mail address to e-mail. So, I attempted to file a ticket, however even this requires 30 minutes of trudging/fighting through obscure attempts to deflect actual contact with support via their "knowledge base" and a barely-functionining java applet that tries to detect obvious problems first. Once I made it through this and obtained the customer's password (which is required for some reason to even file a ticket), I managed to file a ticket asking them for an explanation.

This was their response, after which they immediately closed the ticket (which I can't re-open to respond):

> I carefully investigated your case and I noticed that your domain is using an mail exchange server as it's MX records point to 
> 
> redacteddomain.com. 14400 IN MX 10 mta1.swirbo.net.  
>  redacteddomain.com. 14400 IN MX 10 mta2.swirbo.net. 
> 
> Due to this fact the email messages are coming to our server from email address redacteduser@aol.com and hostname mta2.swirbo.net. due to the fact that mta2.swirbo.net. is relaying them to us. 
> 
> Our spam prevention filters are checking if the email address domain and the host which the emails come from are the same and if they find a mismatch the email is rejected with the message that it must be fake mail. 
> 
> My advice is to contact your mail exchanger support team and present them with this information in order to solve the issue more effectively.
> 
> Please do not hesitate to contact us if you have any further questions or comments. 
> 
> Best Regards, 
> 
> Andrey  
>  Support Team  
>  SiteGround.com 

So, aside from their hideous customer service and refusal to give me a chance to respond to a support inquiry, we have what appears to be a very braindead attempt at spam-filtering by Siteground. What they seem to be saying is that when they receive an SMTP connection, they check the reverse-DNS for the IP, and if the domain name in the resulting A record doesn't match the sender's domain, they reject it. This makes no sense, and contravenes any number of standard practices involving SMTP relays. I'm assuming they only do this for certain larger domains (AOL, Yahoo, etc.), otherwise it's hard to imagine how their customers get any mail at all. The potential here for false-positives is huge.

Similar problems as this emerge with [SPF](<https://web.archive.org/web/20071012125810/http://en.wikipedia.org/wiki/Sender_Policy_Framework>), but this is above and beyond even that.

Unfortunately, due to Siteground's complete lack of support, broken e-mail, and inability to address this problem, we'll probably be migrating what few accounts we have with them somewhere else.
