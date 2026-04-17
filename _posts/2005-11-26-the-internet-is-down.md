---
layout: post
title: "The Internet is Down!"
date: 2005-11-26
author: Chris
categories: [Miscellaneous, Networking]
---
Nearly everyone that has worked in tech support before (or even those that haven't) has a joke or story about some naive end-user calling about a routine problem but describing it as "the Internet is down!" -- when really all they needed to do was reboot or something. It's funny, and we nerds all get a laugh, but what happens when it's true and you have to explain it to a customer?

This happened to me a few months ago. We had a customer calling to ask why they were being flooded with calls from their users about their web application (which we host) was down.

At first, I was perplexed, because I was on their server via SSH and also logged into the web application with no problems. No latency, no bandwidth problems, no load. Nothing. Then I remembered the news I had read that week. Cogent and Level3 were in the midst of a [billing spat](<http://www.computerworld.com/managementtopics/outsourcing/isptelecom/story/0,10801,105210,00.html>), and as a result, they were dropping eachothers' peering connections.

So, we got some of the people complaining on the phone and got their IP address, and a few traceroutes later, sure enough, we verified that they were going through Level3 to get to us and were being dropped off the face of the earth.

So, the explanation in this scenario was, more or less, "the Internet is down". Well, not exactly, but you can imagine how difficult it was to explain in this situation how the problem really was a systemic one of "The Internet's" and not anything I could have any control over.

The Internet is a rather remarkable feat of engineering. We sometimes take for granted that it always Just Works, which can make it rather troublesome when it doesn't!
