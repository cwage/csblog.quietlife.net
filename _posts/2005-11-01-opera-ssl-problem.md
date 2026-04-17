---
layout: post
title: "Opera SSL Problem"
date: 2005-11-01
author: Chris
categories: [Software]
---
More and more I've encountered a weird issue with Opera and some HTTPS sites, where it would return an error trying to connect:

> Could not connect to remote server
> 
> You tried to access the address https://products.geotrust.com/ssl/starterssl.do?ref=freessl, which is currently unavailable. Please make sure that the Web address (URL) is correctly spelled and punctuated, then try reloading the page. 

The same site would work fine in IE or Firefox. I consulted the [almighty oracle Google](<http://groups.google.com/group/opera.general/browse_thread/thread/e3efc4912f694513/582a6a2753fb6aa3?lnk=st&q=%22You+tried+to+access+the+address+https%22&rnum=2#582a6a2753fb6aa3>) and discovered it's because Opera 8.5 (and perhaps others) evidently turns on TLS 1.1 by default (either that or I somehow turned it on). This is forward-thinking of them, but as it turns out a lot of sites don't support TLS 1.1 yet.

You can disable this by going to Preferences -> Advanced -> Security -> Security Protocols and unchecking the box next to TLS 1.1.

Voila! No more weird SSL errors!
