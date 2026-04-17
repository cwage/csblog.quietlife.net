---
layout: post
title: "SSL Wildcards"
date: 2006-01-24
author: Chris
---
Today's lesson for the day: SSL wildcards are just that: wildcards.

We have a client that needed an SSL certificate for websites that will be running on some wildcard zones, so for example:

https://foo.bar.blah.domain.com/  
https://bar.bar.blah.domain.com/  
etc...

When you register an SSL certificate, you have to set the "CN" (Common Name) to the hostname you want the certificate to match. I set the hostname to *.domain.com, my regex-training betraying me into think the * would match **anything** before .blah.com. That is not the case, however, and the [RFC for HTTP over TLS](<https://web.archive.org/web/20060126225959/http://www.ietf.org/rfc/rfc2818.txt>) is quite clear about it:

> Names may contain the wildcard character * which is considered to match any single domain name component or component fragment. E.g., *.a.com matches foo.a.com but not bar.foo.a.com. f*.com matches foo.com but not bar.com. 

So what I should have specified is a hostname of *.*.*.domain.com. That means that foo.bar.blah.domain.com matches, however a downside is that bar.blah.domain.com, blah.domain.com or even domain.com **do not** match.

**UPDATE:** I have spoken to people at both rapidssl and Verisign that say that specifying *.*.*.domain.com in a CN for an SSL CSR is not even possible. However, testing on my own with a self-signed certificate seems to indicate otherwise. Does anyone have any insight on this? Is there some reason this wouldn't work, or are they just trying to upsell me (both people tried to sell me an "enterprise" solution)?
