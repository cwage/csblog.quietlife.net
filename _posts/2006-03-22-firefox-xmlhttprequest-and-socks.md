---
layout: post
title: "Firefox XMLHttpRequest and SOCKS"
date: 2006-03-22
author: Chris
---
A friend of mine pointed me at this site: <https://web.archive.org/web/20060322/http://www.mapable.com/>. A neat, but forgettable site. It uses the Google Maps API to display a map with real-time chatting between people on .. the map. It uses the client IP address to extrapolate geolocation and display it on the map, so they can talk in tiny width-restricted fields. Example:

> Person in Algeria: So, you're in Canada, eh?  
>  Person in Canada: Yep  
>  Person in Algeria: Soo..  
>  Person in Canada: Can you see anything I write longer than 50 charact  
>  Person in Alergia: Nope. 

Okay, so the interface needs a little work. Okay, well, it's just not terribly useful at all -- except, as it turns out, for identifying Firefox bugs. Being the fiendish nerd that I am, the first thing I tried to do was fake out the site by redirecting my traffic through an anonymous proxy -- in this case, [tor](<https://web.archive.org/web/20060408185824/http://tor.eff.org/>), running a SOCKS daemon. Oddly, though, even though I told Firefox to use the SOCKS proxy, it still pinpointed my location as Nashville. Perplexed, I cleared my cookies and tried again. Nope, still located in Nashville. "Wow," I thought, "These guys are good." 

But if there's one thing I know, it's TCP, DNS, and HTTP. They couldn't get my location from HTTP, because all the requests are going through SOCKS, which is redirecting to somewhere in New Jersey, which I verified by visits to other places on the web. DNS is rather impossible as well, since they have no way of knowing which DNS requests match to which HTTP requests. There was no other possibility, except .. AJAX. This is a fancy site using AJAX stuff, including XMLHttpRequest. The only other option was that Firefox was just not tunneling XMLHttpRequest calls through the SOCKS proxy. A quick _tcpflow -c host www.mapable.com_ verified this to be the case:

> 010.010.015.002.34046-068.178.163.109.04000: <?xml version="1.0" encoding="utf-8" ?><broadcast senderName="Guest 1917" channelName="mapablemain" wolf="true"><l>test</l></broadcast>

Sure enough, Firefox is ignoring the SOCKS proxy for XMLHttpRequest calls and sending it straight through to the website. I am assuming this is a bug, and I'll be reporting it as such, if I can ever work up the motivation to try to fight through Mozilla's bugzilla interface. I hope no one in the meantime is trying to hide anonymously using SOCKS on an AJAX page!
