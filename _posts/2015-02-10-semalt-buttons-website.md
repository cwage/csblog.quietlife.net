---
layout: post
title: "What is semalt? What is buttons-for-website?"
date: 2015-02-10
---
![Semalt](http://blog.centresource.com/content/uploads/2015/02/semalt-300x172.jpg)If you keep an eye on your Google Analytics referral sources, you've probably noticed a growing number of referrals from semalt.com and buttons-for-website.com. Aside from your referral sources in analytics, you've probably never heard of these sites, and you're curious why you're getting so much traffic from them.

In short, these sites are employing a tactic known as '[referrer spam](<http://en.wikipedia.org/wiki/Referer_spam>).' The concept is to generate a whole ton of links to a website by creating a bunch of traffic that appears to be coming from a particular site that they wish to promote. These 'referrals' then appear in access logs which are crawled by search engines. The massive quantity of links that point back to the spammer's site then improve their own SEO scores. The added side benefit is that astute observers like yourself are curious about this site that keeps showing up in your analytics, and you go and look up the site, and they've now brought in a new potential customer for their SEO services.

The good news is that this doesn't pose any real threat to your website. The bad news is that it messes up your analytics numbers and doesn't provide a true picture of what's happening on your site, since this traffic typically has a 100% bounce rate, and a time on site of zero.

So, what to do? If you want to have a more realistic picture of what users are doing on your site, you'll need to block these referral spammer numbers from your analytics reports. Many other articles published about the semalt scourge tout the solution of using Google Analytics' relatively new "[Bot Filtering](<https://plus.google.com/+GoogleAnalytics/posts/2tJ79CkfnZk>)". If you're unfamiliar with it, it's a simple checkbox that Analytics added within a site's View Settings. Unfortunately, in our experience, the checkbox doesn't actually filter out semalt and buttons-for-website referrals. Thus, to weed out this junk traffic from your analytics, you'll likely need to add a custom filter. Here's how to do that:

  1. Within Analytics, click on Admin.
  2. On the right column, under View, select Create New View. (We always suggest creating a new view when adding a filter so that you always keep one view that is completely unfiltered, since filters can't ever be undone.)
  3. Name the new view. (Maybe something like Filtering Bots)
  4. Click Filters.
  5. Click + New Filter.
  6. Make sure Create new Filter is the selected option, and name the filter. (Something like Semalt Filter)
  7. Choose Custom as the Filter Type.
  8. Under Exclude, change the Filter Field to Referral and enter "semalt.com" (without quotes) in the Filter Pattern box.
  9. Click Save.



Repeat from step 5, replacing semalt.com with buttons-for-website.com to include filtering for that site.

Note that views and filters are not retroactive, so you'll only start seeing the data within this view moving forward from when it was created.

* * *

  * [Interactive Strategy](<http://blog.centresource.com/category/interactive-strategy-2/>)
  * [Marketing](<http://blog.centresource.com/category/marketing/>)



[google analytics](<http://blog.centresource.com/tag/google-analytics/>)

![](http://1.gravatar.com/avatar/58a8d7bffbe9b1c52860e08219d64d8b?s=120&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D120&r=G)

#### [Shaun Jackson](<http://blog.centresource.com/author/sjackson/> "Posts by Shaun Jackson")

Shaun is one of the few centresourcerers (yeah, that's right) that came to us as a client first. Shaun was a long-time centresource client and friend of the firm -- we worked closely with Shaun as our client contact at Warner Bros. Records, where he managed all things web and interactive for a large roster...




[ ![Great Stats and Facts Picked Up at the Google Partners Connect Event](http://blog.centresource.com/content/themes/marroco/assets/img/empty/pixel.png) ](<http://blog.centresource.com/2014/05/27/great-stats-and-facts-picked-up-at-the-google-partners-connect-event/>)

### [Great Stats and Facts Picked Up at the Google Partners Connect Event](<http://blog.centresource.com/2014/05/27/great-stats-and-facts-picked-up-at-the-google-partners-connect-event/>)

May 27, 2014 / [Marketing](<http://blog.centresource.com/category/marketing/>)

Last week, we hosted a Google Partners Connect simulcast event at the Centresource Lab. We ...

[ ![The Lean UX Canvas](http://blog.centresource.com/content/themes/marroco/assets/img/empty/pixel.png) ](<http://blog.centresource.com/2014/09/18/lean-ux-canvas/>)

### [The Lean UX Canvas](<http://blog.centresource.com/2014/09/18/lean-ux-canvas/>)

September 18, 2014 / [Interactive Strategy](<http://blog.centresource.com/category/interactive-strategy-2/>), [UX-Design](<http://blog.centresource.com/category/uxdesign/>)

We work with a lot of companies in varying states of maturity. Some prospective clients ...

* * *

# Post navigation

[← 6 Easy Ways to Know if Your Site Has a UX Problem](<http://blog.centresource.com/2015/02/05/6-easy-ways-know-site-ux-problem/>)

[3 Essentials That Make a City Great for Startups →](<http://blog.centresource.com/2015/02/13/3-essentials-make-city-great-place-startups/>)
