---
layout: post
title: "Eliminating (Most) Trackback Spam"
date: 2006-02-01
author: Chris
---
Well, [wordverify](<http://chris.quietlife.net/wordverify>) has taken care of almost all comment spam, except for [human spammers](<http://blog.centresource.com/2006/01/27/advantage-consulting-services-spammers/>), of course.

However, trackback spam, since it is by definition automated when working properly, cannot be eliminated with that method. I had the simple idea to write a plugin that, upon receiving a trackback ping, would snag the referring URL and make sure it actually links. If not, the trackback would be rejected. This is slightly in opposition to the spirit of trackbacks, according to some, since some people believe you should be able to send a trackback without actually linking. I am not necessarily in agreement, but I think the elimination of this possibility is a small price to pay to eliminate spam.

Well, seeing as how this idea is so simple, I assumed rightly that I wasn't the first to have it. Indeed, Dan Sandler has already written a [fine plugin](<http://idli.cs.rice.edu/~dsandler/trackback/trackback-validator-plugin/>) for Wordpress which does this exact thing.

With this plugin installed, along with wordverify, I am finally looking at a near spam-free existence in my blogging. I hope it lasts.
