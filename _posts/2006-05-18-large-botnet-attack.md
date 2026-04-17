---
layout: post
title: "Large Botnet Attack"
date: 2006-05-18
author: Chris
---
So, the inspiration for writing [this script](<https://web.archive.org/web/20060615075533/http://blog.centresource.com/2006/05/18/simplegraph/>) was so that I could quickly and effortlessly visualize some of the stats from my webserver logs on the fly. The reason was that I have noticed a huge influx of comment-spam attempts on my personal blog, this blog, and the [Nashville Metblog](<https://web.archive.org/web/20060516180305/http://nashville.metblogs.com/>).

I have access to the logs on the first two, and it was obvious from casual inspection that each attempt was coming from a different IP and network: i.e., it is coming from a botnet. I suspected that the spam influx on all these hosts was from the **same** botnet, and it appears that I was right. Out of 3-400 unique IP addresses making the spam attempts on those first two sites, around [200 of them](<https://web.archive.org/web/20060615101812/http://blog.centresource.com/wp-content/botnet_ips.txt>) had hit both servers. And lest there was any doubt, compare these two graphs of the comment-spam attempts per hour:

![centresource spam attempt graph](https://web.archive.org/web/20070102020149/http://blog.centresource.com/wp-content/centresource-spam.png)

![quietlife spam attempt graph](https://web.archive.org/web/20070102020430/http://blog.centresource.com/wp-content/quietlife-spam.png)

Note the same spikes, where you can see the botnet being flipped on and off. The volume of spam here relative to comment-spam spikes I've seen in the past is not really that large, but what's striking is how widespread the targets of the botnet is.
