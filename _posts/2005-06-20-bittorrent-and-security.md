---
layout: post
title: "bittorrent and security"
date: 2005-06-20
author: Chris
categories: [Malware, Software]
---
A few weeks ago, as I downloaded the enormity of XP SP2 to burn to CD, it occurred to me that it seems silly that Microsoft didn't leverage the power of [bittorrent](<https://web.archive.org/web/20050621013916/http://www.bittorrent.com/>) to distribute this update, and their patches in general. Imagine my dismay to discover that someone tried, and was [promptly shut down](<https://web.archive.org/web/20050621005400/http://sp2torrent.com/>) using the DMCA. I guess I shouldn't be too surprised, but evidently Microsoft claims to be working on a similar "alternative" to bittorrent, which the creator of bittorrent is dismissing as [nothing but vaporware](<https://web.archive.org/web/20050622024659/http://www.livejournal.com/users/bramcohen/20140.html>).

But, further in this line of logic, why don't Anti-virus and anti-spyware vendors use it as well -- that is, build the bittorrent client right into the client's update code? These thoughts came home to roost a few days ago when the [Mytob infections](</2005/06/20/mytob-mania/>) were running rampant, and as a result, AVG's free update site was overwhelmed and largely inaccessible all day. Something like bittorrent would never fall prey to this, and instead the result of the massive traffic load would be a benefit for everyone looking for this particular data. It's the perfect distribution method for these very time-sensitive spike-prone updates.

Naturally, security measures would have to be taken to prevent rogue bittorrent seeds posing as authoritative sources to inject bogus code/updates. Is PKI a viable answer to this? Are there any other pitfalls to using bittorrent to distribute these sorts of very sensitive updates?
