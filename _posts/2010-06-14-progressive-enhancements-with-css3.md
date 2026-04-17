---
layout: post
title: "Progressive Enhancements with CSS3"
date: 2010-06-14
author: Travis Roberts
categories: [Web Design]
---
CSS3 is great! The themers and designers here at centresource all love the improvements that are now available to (most) modern browsers. The best part of CSS3 is that the changes are subtle, and a site can still look fantastic without using any of the new styles.

The idea of "progressive enhancement" is to get a site looking the way to want in all of the current browsers, then add some enhancements that most of those browsers can understand. It's kind of like a bonus for the users of the more progressive browsers. Since they are savvy enough to know what browsers are on top, they can reap the rewards of the polish that CSS3 allows for a website.

### Border Radius

**Supported Browsers** : Chrome, Firefox, Safari, IE9

Border-radius is probably the most useful of the CSS3 attributes. It allows you to add rounded corners to any box item. Using this new property saves a lot of time and divs from the old way of achieving rounded corners with background images. The great thing about border-radius is that it works in all of the major browsers (I'm not including Opera in this category) except IE8 and below. So, most likely, the majority of your site visitors will see your snazzy rounded corners.

![border-radius](/wp-content/uploads/2010/06/border-radius.png)

You can also target specific corners.

![border-radius-top-left](/wp-content/uploads/2010/06/border-radius-top-left.png)

Notice that we use the `border-radius` attribute (which will eventually be the standard, and which Chrome already understands), but we also include the proprietary attributes `-moz-border-radius` for Firefox and `-webkit-border-radius` for Safari.

### Text Shadow

**Supported Browsers** : Chrome, Firefox, Opera, Safari

By far my favorite method for adding that last little bit of polish to your site. It's amazing how much better a heading or body text looks with a subtle text-shadow added to it. I think it adds a nice level of depth to the text.

![text shadow example](/wp-content/uploads/2010/06/text-shadow.png)

It's as simple as adding the following line to your CSS:

`text-shadow:1px 1px #ddd;`

### RGBA

**Supported Browsers** : Chrome, Firefox, Opera, Safari, IE9

Another great example of a progressive enhancement that makes a site look great, but one that a user of an old browser won't miss. RGBA just allows to you define a color with an opacity value (between 0.0 and 1.0) for any place you would normally use a regular RGB color (or hex color). It's main uses are for making background or text colors semi-transparent.

![rgba](/wp-content/uploads/2010/06/rgba.png)

### Closing Thoughts

Using CSS3 to add subtle enhancements to your site is a great way to reward your forward-thinking users who are smart enough to run the latest web browsers.
