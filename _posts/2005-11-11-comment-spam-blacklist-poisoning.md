---
layout: post
title: "Comment Spam Blacklist Poisoning"
date: 2005-11-11
author: Chris
categories: [Spam]
---
A new trend in comment/referer spam is on the rise -- or on the low, I should say, since it is low indeed.

Typically, when I get a comment spam that slips through our .htaccess checks and [wpblacklist](<https://web.archive.org/web/20051109215608/http://sm.farook.org/WPBlacklist.htm>), I usually have to go to the wpblacklist options area and manually search for the URL they spammed and add the offending IP, host regex, etc.

However, a few months ago, I noticed a URL being spammed that didn't look like your average "htp://free-blackjack-poker.info" type spam URLs. This was an innocuous URL that actually appeared to be legit. So on a lark, I loaded it, and indeed, it was a legit post, by a legitimate blog. The content, however, was still your standard "Get free rolexes/v1agra/etc" type message.

I have seen this more and more. It appears to be a concerted effort by the comment/referer spammers to intersperse legitimate URLs along with the actual spam URLs. Presumably, the point is to get these legitimate URLs into blacklist databases and as a result diminish their reliability for not inducing false-positives. "Poisoning the well", so to speak. In the e-mail spam world, this is referred to as a [Joe-Job](<https://web.archive.org/web/20051124165005/http://en.wikipedia.org/wiki/Joe_job>).

So far the volume hasn't been high enough that I haven't been able to tell right off the bat that a particular attempt is a joe-job attempt, and in those cases I've just deleted the comment and added the IP to the blacklist but not the URL. But I suspect this new technique may make blacklisting even more difficult in the near future.

On [this thread](<https://web.archive.org/web/20051102022429/http://blog.centresource.com/2005/08/28/tracking-down-the-source-of-referrer-spam/#comment-1374>), I suspected at first that we were the victim of such an attempt, as someone reported being referrer spammed with our URL. However, upon further investigation it appears to have merely been a [lame attempt at revenge](<https://web.archive.org/web/20051102022429/http://blog.centresource.com/2005/08/28/tracking-down-the-source-of-referrer-spam/#comment-1381>) by our favorite referrer spammer himself, Jackie Zhao.
