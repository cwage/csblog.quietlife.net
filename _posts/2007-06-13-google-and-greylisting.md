---
layout: post
title: "Google and Greylisting"
date: 2007-06-13
author: Chris
---
We'd have a recent spat of complaints from our [Swirbo](<http://www.swirbo.com/>) customers regarding their inability to receive mail from certain [Google](<https://web.archive.org/web/20070614025949/http://www.google.com/>) apps -- i.e. if you invite someone to view a blog, or docs.google.com document. Today I got an example of the actual error they are getting:

> Technical details of permanent failure:  
>  TEMP_FAILURE: SMTP Error (state 13): 450 : Recipient  
>  address rejected: Greylisted for 5 minutes  
> 

Anyone see a problem? The error we returned was 450, yet Google seems to think it was a permanent failure. Here's a bit from the SMTP RFC (2821):

> 4yz Transient Negative Completion reply  
>  The command was not accepted, and the requested action did not  
>  occur. However, the error condition is temporary and the action  
>  may be requested again. The sender should return to the beginning  
>  of the command sequence (if any). It is difficult to assign a  
>  meaning to "transient" when two different sites (receiver- and  
>  sender-SMTP agents) must agree on the interpretation. Each reply  
>  in this category might have a different time value, but the SMTP  
>  client is encouraged to try again. A rule of thumb to determine  
>  whether a reply fits into the 4yz or the 5yz category (see below)  
>  is that replies are 4yz if they can be successful if repeated  
>  without any change in command form or in properties of the sender  
>  or receiver (that is, the command is repeated identically and the  
>  receiver does not put up a new implementation.) 

SMTP 4xx errors are temporary and typically represent transient errors. An SMTP client, upon receiving an error like this, **should** (i.e. is encouraged to) try again. Greylisting is a spam-filtering technique that takes advantage of this fact by issuing temporary rejections to new clients, in effect filtering out mail sent by software not smart enough to retry (as any proper mailserver would). Google should be queueing and retrying these messages. Anyone else running into this?
