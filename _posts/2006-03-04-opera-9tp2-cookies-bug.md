---
layout: post
title: "Opera 9TP2 Cookies bug"
date: 2006-03-04
author: Chris
---
The problem I alluded to in my [brief review](<https://csblog.quietlife.net/2006/03/04/opera-90-tp2/>) of Opera 9.0 TP2 is simple: In the site-specific preferences, if you set the default to "Never accept cookies" -- it does just that, ignoring your site-specific exclusions. This appears to be because although the option to honor your site-specific prefs is still there, they just .. forgot to let you select it in the UI.

So, as [discussed here](<https://web.archive.org/web/20060507090010/http://my.opera.com/community/forums/topic.dml?id=123132>), all you have to do is manually edit your opera6.ini to set your cookie preferences how you want them and leave it alone. The table of values for "Enable Cookies" can be [found here](<https://web.archive.org/web/20080725151926/http://my.opera.com/burnout426/homes/files/cookietable.html>).

Naturally, this won't be an issue in the official release, but for all you bleeding-edgers like myself, this tip may come in handy until the bug is fixed.
