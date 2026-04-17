---
layout: post
title: "Blog Layout"
date: 2005-10-05
author: Chris
categories: [Miscellaneous]
---
There are two common types of blog layouts as far as handling "permalinks" to individual entries:

  * Type 1 is one HTML "page" per article, i.e. as is the case with this blog.
  * Type 2 is one long page with multiple updates, where permanent links are handled with anchors. (for the non web-geeks, an "anchor" is a tag added to the end of a URL to mark a "spot" in the page to scroll to automatically -- i.e. loading http://www.blah.com/index.html#foo loads index.html and then scrolls to the "foo" anchor.



I loathe the latter Type 2 layouts. The reason should be simple and apparent to anyone that has read such a blog. It's that some browsers (including Opera) do not scroll to anchor tags until it has fully loaded the page (and hence can render it). This is because it has to know the layout of all the elements of a page (images, etc) before it can scroll the right amount of pixels down to the anchor. Firefox doesn't appear to do this, and I am assuming it just makes a "best guess" as to where that anchor will end up in the text, which makes it slightly more convenient -- but also annoying, because from what I can see, it sometimes gets it wrong, and the top of your browser winds up in some place slightly off from where the article actually starts, which is jarring and confusing.

What's worse is that in browsers like Opera, you have to wait for the entire page to load until it scrolls to the anchor at all (i.e. to read the entry that you clicked to read to begin with). And, invariably, the blogs with this format also tend to be ones **loaded** with sidebar ads, images, and other included content that takes **forever** to load. I always end up manually scrolling to find what I was looking for while the 8,000 images load in the background.

So there's one trivial but very annoying reason why I vastly prefer the first page-per-article layout. It's fast and efficient. You don't have to wait for an archive page of 2,000 articles to load just to read a 50 word post.
