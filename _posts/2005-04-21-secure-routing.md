---
layout: post
title: "secure routing"
date: 2005-04-21
author: Chris
categories: [Security, Networking]
---
Geoff Huston over at [Potaroo](<https://web.archive.org/web/20050324014916/http://www.potaroo.net/>) has a [great article](<https://web.archive.org/web/20050403231508/http://www.potaroo.net/ispcol/2005-03/route-sec-2-ispcol.html>) focusing on ways to secure routing transactions with BGP, including using a PKI. Routing protocols are particularly vulnerable to attack, as Geoff notes:

> It's an area where the rewards of mounting a successful attack in the routing system can be very high. It is possible to undertake denial of service, third party traffic inspection and service cloning, and to do so in a manner that can be challenging to detect through deliberate corruption of the information carried in the routing system. For example, by injecting a false route describing a path to an anycast instance of a root server, an attacker can create a network sub-domain where DNS resolution queries are passed to a fake server, who, in turn and manipulate the responses associated with the intended victim, while answering all other queries accurately. Or, more directly, an attacker can create a fake version of an online commerce service, subvert a sub- domain of the internet with false routing information and thereby harvest users' access credentials. Obviously the rewards of attack can be high, whether it's a targeted attack against a single service or a coordinated effort to disrupt the operation of large sections of the network.
