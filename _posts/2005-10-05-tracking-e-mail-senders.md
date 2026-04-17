---
layout: post
title: "Tracking E-mail Senders"
date: 2005-10-05
author: Chris
categories: [Spam]
---
Someone on [this thread](<https://web.archive.org/web/20051013065143/http://blog.centresource.com/2005/08/28/tracking-down-the-source-of-referrer-spam/>) asks the following question:

> Your article was helpful. Thank you very much. I wanted to know how to to track the geo-location from where an email was sent. Is this possible? 

The short answer is "maybe, but probably not".

There are basically two factors playing into whether or not you can track down an e-mail to a **physical** location of origin. The first is "Can I track down the origin IP address that the e-mail originated at?" The second is "Can I associated that IP address with the physical location of the sender?"

So, to answer these questions in order:

**Can I track down the origin IP address that an e-mail message originated at?**

To fully answer this question, some background on how SMTP transfer and e-mail headers is required. When you receive an e-mail message, the process is this:

  1. A mailserver (or a computer in general) connects to your mailserver on port 25
  2. It sends a few initial commands to introduce itself and who the message is sending on behalf of. This is called the "envelope" of the message, and the process in a simplified non-ESTMP session looks like this:  


> 220 mta1.swirbo.net ESMTP Postfix (Debian/GNU)  
>  **HELO domain.com**  
>  250 mta1.swirbo.net  
>  **MAIL FROM: user@domain.com**  
>  250 Ok  
>  **RCPT TO: user@company.com**  
>  250 Ok 

It's important to note that at this stage, we have the following bits of information, only one of which we can actually trust:

     * The IP address (this we can trust, since, barring IP spoofing, we know this address is the one that connected to us).
     * The "envelope From" (MAIL FROM:). This is arbitrary and can be spoofed.
     * The "envelope HELO". This is supposed to contain a FQDN (or IP address literal) of the mail server sending the mail, however this too is arbitrary and can be spoofed.

There are various things a responsible mailserver can do with even these bits of info to verify that it's legit (ensure valid FQDN, etc.) but as far as tracking down the actual sender, there's little to go on here other than the origin IP address.

  3. The receiving mailserver, after sending "250 Ok" and thus indicating it's ready for transmittal of the message, waits for the client to send the "DATA" command followed by the message. For example:  


> **DATA**  
>  354 End data with <CR><LF>.<CR><LF>  
>  **Received: from completely.fake.com (completely.fake.com [123.45.67.8])  
>  by also.fake.com (Postfix) with ESMTP id A22E93A4083  
>  for <user @company.com>; Tue, 4 Oct 2005 14:00:59 -0500 (CDT)  
>  To: user@company.com  
>  Subject: test  
>  MIME-Version: 1.0  
>  From: User <user@domain.com>  
>  Content-Type: text/plain; charset="UTF-8"  
>  Date: Wed, 5 Oct 2005 11:20:14 -0500 (CDT)**
> 
> Hi!  
>  .  
>    
>  250 Ok: queued as 46D393A4083

  4. The receiving mailserver takes this data (the message) and uses the data from step 2) to add a few headers to the message (the "envelope"):  


> **Return-path: user@domain.com  
>  Received: from reverse.for.sender.IP.com (reverse.for.sender.IP.com [1.2.3.4])  
>  by my.mailserver.com (Postfix) with ESMTP id 46D393A4083  
>  for <user @company.com>; Tue, 4 Oct 2005 14:00:59 -0500 (CDT)  
>  **

  5. The entire message is stored in the destination user's mailbox.



So, once this entire process is completed. The resulting message will potentially have a number of "**Received:** " headers, but **the one added by your mailserver is the only one you can trust**. This is the most common mistake that people make when trying to track senders of a particular e-mail message. Often times abuse complains are made to ISPs that have absolutely nothing to do with a particular message, only because their IP address/hostname was listed in forged Received: headers.

Once upon a time, when everyone on the Internet got along quite nicely, and spam was simply an obscure lunch meat, mailservers could all be trusted to add their "Received:" headers for each hop along the way. As a result, back then, you could look at the headers of an e-mail message and get a fair idea of the mailservers it was routed through along the way to you. However these days, with any message you suspect of smelling like spam, you can almost certainly be assured that all the Received: headers other than **the one added by your mailserver** are forged. Why? Think back to step 3) and note that the mailserver accepts all these Received: headers along with the rest of the message on good faith. **They are completely arbitrary.**

So when it's all said and done, the ramifications of this are that for you, as a user reading an e-mail message you suspect to be spam, the only information relevant and useful for you in tracking the source of the message is the **top-most** "Received:" header that was added by your mailserver, and the only information you will be able to glean from it is the IP address of the sender (in our example, 1.2.3.4).

Now, that said, **sometimes** you will still encounter e-mail messages that have useful information in the Received: headers, but you shouldn't rely on it. For example, some webmail services like hotmail do include the IP address of the web browser that sent the message through hotmail in a Received: header. However since this information is completely arbitrary and forgeable, you have to use your best judgement to determine whether or not this information is reliable. In most cases, it is not.

So, now that we understand all that, we are left with the sad conclusion that the only real bit of information we have is the IP address of the client that sent the message. Can we do anything with that?

**"Can I associated that IP address with the physical location of the sender?"**

The answer here again is muddled, but the general answer is "probably not".

There are two ways you can learn information about an IP address: a) WHOIS information for the network from ARIN and b) reverse DNS (if it exists).

However both of these methods are more likely to give you information only about the organization that owns the IP addresses, rather than the actual physical location. The best you can hope for if anything, in these cases, is by observing that it's, say, a Bellsouth IP address, so you know it's in the United States.

Sometimes you will get lucky and reverse DNS on an IP address will be particularly revealing, i.e. you look up "1.2.3.4" and get "1.2.3.4.companyname.com", which gives you a pretty good indication that the sender was at companyname.com.

Further, some ISPs do include some location information in their reverse DNS -- for example, comcast includes a state in their reverse DNS, depending on what state the network is in, i.e. "ca.comcast.net".

Further complicating matters is that there's a good chance the client IP address sending the mail is actually a compromised/abused host, such as an overly permissive open mail relay, a broken web proxy, etc. The "person" actually sending the message may very well be behind several of these proxies, hopping from one to the other before actually contacting your mailserver.

So in conclusion, actually locating the physical location of the person responsible for sending you spam is very difficult, if not impossible. Even when it is possible, it's rarely worth the effort.

The most pragmatic response to e-mail abuse is simply to identify the network source of the message and report the abuse to the ISP responsible for that network. It doesn't matter who originally sent the message if it's an open mail relay being exploited on that ISP's network (which is something they can fix).
