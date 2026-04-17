---
layout: post
title: "weird SMTP flood"
date: 2005-05-12
author: Chris
---
A little weirdness this morning: Swirbo got hit with a few IPs just endlessly connecting and disconnecting as follows:

> 066.240.006.125.24775-067.019.187.050.00025: EHLO DSEXCH.DebtShield.net
> 
> 067.019.187.050.00025-066.240.006.125.24775: 250-mta1.swirbo.net  
>  250-PIPELINING  
>  250-SIZE 30720000  
>  250-VRFY  
>  250-ETRN  
>  250 8BITMIME
> 
> 066.240.006.125.24775-067.019.187.050.00025: QUIT
> 
> 067.019.187.050.00025-066.240.006.125.24775: 221 Bye 

63.243.57.99 was the same, except it sent "EHLO dc1admin.admin.tecnicocorp.com".

The two IPs were:

63.243.57.99/32 (Tecnico TEC42186 (NET-63-243-57-96-1))  
66.240.6.125/32 (Optical Capital Group CMA1-OPTICALC-1 (NET-66-240-6-112-1))

Anyone run into this before? Can anyone think of a misconfiguration this would be a symptom of? If it was a DoS attempt it sure wasn't a very good one.
