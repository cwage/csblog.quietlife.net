---
layout: post
title: "Search Engine Loop"
date: 2006-03-08
author: Chris
---
My [previous post](<http://blog.centresource.com/2006/03/08/on-tagging/>) on tags reminded me that I wanted to mention something amusing I ran into when I first installed [Ultimate Tag Warrior](<http://www.neato.co.nz/ultimate-tag-warrior/>) on my personal blog.

This plugin gives you the natural ability to limit posts by multiple tags, for example, <http://blog.centresource.com/tag/linux+software> gives you all the posts tagged with "linux" and "software". Conversely, you can also do <http://blog.centresource.com/tag/linux|software> to get all posts tagged with "linux" OR "software".

However, it's convenient to have some way to construct these URLs in the actual interface. UTW gives you a formatting option, for example "andcommalist", which puts + and | next to tags. That way, if you're viewing <http://blog.centresource.com/tag/linux>, and a post was also tagged with "software", the "software" will have + and | next to it -- both links which allow you to add a restriction of "AND software" and "OR software", respectively.

This is pretty cool, but it has an interesting effect. I turned it on on my website, but over the course of a week, I started to notice the search engines that crawl my site behaving erratically (well, more erratically than normal, anyway). They seemed to be hitting the same URLs over and over again.

Eventually I realized what it was. UTW isn't smart enough to notice if you are already viewing, say, <http://blog.centresource.com/tag/linux>, and not to put the + and | next to the "linux" tag in the list. The result is that you can keep clicking the + next to "linux" and wind up viewing <http://blog.centresource.com/tag/linux+linux+linux+linux>. Anyone want to take a stab at what happens when a search engine crawler gets ahold of a page doing this? That's right, infinite-loop city.

An interesting unintended side-effect. I have disabled this feature, but I'd like to re-enable it once this is fixed.
