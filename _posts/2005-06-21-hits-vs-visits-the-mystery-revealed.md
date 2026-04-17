---
layout: post
title: "Hits vs. Visits - The mystery revealed"
date: 2005-06-21
categories: [Operations, Development]
---
The question often arises: _When viewing a web log, what is the difference between Hits & Visits._ This is a great question for those who are truly interested in the traffic going to their site. However, website operators must realize that this is an imprecise science and that many factors (including the actual software you use to record web statistics) can affect the actual numbers.

Here is a high-level explanation of important web log statistics:

1) Visits: Visits represent the number of times your website had someone access it. Visits are independent of the actual number of pages viewed (see 'Pages Viewed per Visit' below), the length of time the person stayed on your site, and does NOT represent the total number of unique visitors.

2) Hits: This number, often used by companies to tout the popularity of their website, represents the number of 'requests' for web page elements your website fulfilled. Images, javascript, Cascading Style Sheets, embedded objects, and other website elements all contribute to the 'Hits' count. A great example is that a single page with 30 images, 1 javascript file, and a style sheet would be 33 hits (you have to include the page as a hit in the total count). 1 visit, 33 hits.  
**Note:** _Hits are great for tracking your bandwidth usage needs_

Many stats program are now providing more useful statistics such as 'Unique Visitors' and 'Pages Viewed per Visit'. These are much better for tracking the popularity of your website.

  * 'Unique Visitors' attempts to track visits that originate from a unique IP address. This number is rarely accurate since many companies have a single public IP address shared by many internal users. It is, however, a great number to watch because it can provide a baseline estimate for the number of unique visitors to your site.
  * 'Pages Viewed per Visit' shows how sticky/interesting your website is. Each time a visitor views a page, this number is increased. Its important to note that this number is not limited only to unique visitors, but by all visits - including return/repeat visitors!



Webstats are not a precise science - especially when you introduce things like private networking, dynamic IP addresses (via dial ups), hits, visits, unique visits, page views, content aggregators, cookies, search engine bots, etc, etc. That being said, they are a great way to get a 'feel' for how popular your site is - and how sticky your content proves to be.

Some great web stats packages are:  
<http://www.mrunix.net/webalizer/>  
<http://awstats.sourceforge.net/>
