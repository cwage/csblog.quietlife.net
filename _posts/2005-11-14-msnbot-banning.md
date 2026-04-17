---
layout: post
title: "MSNbot Banning"
date: 2005-11-14
author: Chris
categories: [Miscellaneous]
---
Chris has a very informative [post](<http://utcc.utoronto.ca/~cks/space/blog/web/BanningMSNBot>) about why he's banned Microsoft's indexing robot, elaborating on some of the problems:

>   * repeatedly fetches large binary files, including 500 megabyte ISO images, that are properly served as binary files and have not changed in some time; 21 fetches for 4 files accounting for 3.7 gigabytes of transfers this week. (See [MSNbotBinariesProblem](<http://utcc.utoronto.ca/~cks/space/blog/web/MSNbotBinariesProblem>))
>   * aggressively fetching syndication feeds, many of them unchanging; 1,615 fetches of 329 feeds amounting to 45 megabytes of transfers this week. Half of the top 10 requested feeds have not changed within the past week, yet were requested 12 times or more. (See [MSNbotCrazyRSSBehavior](<http://utcc.utoronto.ca/~cks/space/blog/web/MSNbotCrazyRSSBehavior>))
>   * never uses conditional GET, even when aggressively fetching syndication feeds. (See [AtomReadersAndCondGet](<http://utcc.utoronto.ca/~cks/space/blog/web/AtomReadersAndCondGet>))
>   * aggressively recrawls unchanging content and error pages, while neglecting changed content, although this is better than it used to be. (See [CrazyMSNCrawler](<http://utcc.utoronto.ca/~cks/space/blog/web/CrazyMSNCrawler>))
> 


I too have noticed the odd behaviour of MSN's crawler, although I don't host the amount of binary data that would make it particularly bothersome to me (repeated hits on an RSS feed or two, versus pulling down huge ISOs), however I can appreciate why this is a huge problem. I find myself wondering why Microsoft hasn't responded or fixed the issue?
