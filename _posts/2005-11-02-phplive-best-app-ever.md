---
layout: post
title: "PHPLive: Best App Ever"
date: 2005-11-02
author: Chris
categories: [Software, PHP]
---
No, I'm not on [PHP Live!](<http://www.phplivesupport.com/>)'s payroll. However, I am truly impressed with their product.

We had needed some sort of web-based live chat system for sales and support for a long time, and we found the answer in PHP Live's product. I demoed it on their site and was impressed. However you have to take demonstrations with a grain of salt if they are hosted on the company's website. Often times what you'll find is that a demo of software works great on the company's webserver, but completely breaks down when you try to use it, or even just to install it. This is usually because the demo webserver is of course finely honed and tweaked to accomodate the product, masking bugs and/or problems that might arise in a more standard or variable environment.

PHP Live!, though, worked great -- right out of the box, with a minimum of work to install. (It took me around 3 minutes to install).

This product costs $100 ($69/yr renewal), which may sound like a lot, but for the gap it fills in our company, it's well worth the money -- there is no open-source product I have seen that can compete.

One feature addition I would like to see added is the ability to interface web-chat requests to support technicians via Jabber. The web interface they have built is very nice, however it's still web-based, requiring the technicians to keep this browser window open while they are logged in. It would be nice if they bridged this to something people already use -- an IM client. XMPP is a protocol that is about as extensible as you can get (heck, it's in the name!). This way I could field requests for chats via jabber rather than having to be logged into a website. There is a [Jabber class for PHP](<http://cjphp.netflint.net/>) well in the works, and it doesn't seem like it would be too difficult to implement (says the guy that doesn't have to develop it).
