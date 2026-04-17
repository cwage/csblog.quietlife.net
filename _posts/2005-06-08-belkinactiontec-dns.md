---
layout: post
title: "belkin/actiontec DNS"
date: 2005-06-08
author: Chris
---
A friend of mine was doing a woody -> sarge update and he kept getting a mysterious error:

> 0% [Connecting to security.debian.org (1.0.0.0)] 

It appeared that for some reason apt-get was resolving security.debian.or to 1.0.0.0, although when he pinged it, it resolved fine.

I had [read about this before](<http://www.mepis.org/node/3221>). Apparently crappier DSL modem/routers like Belkin and Actiontec (which is what he had) provide its IP (i.e. 192.168.0.1 or what have you) for DNS and proxy it to the ISP's DNS servers rather than just giving those out directly. Which is nice and all, except the proxy they use is terrible. As I suspected, the router proxy was barfing on the repeated requests from apt-get and handing out 1.0.0.0 instead.

Changing his nameservers in /etc/resolv.conf fixed it. So, if you run into this problem on a Debian upgrade, now you know what to do!
