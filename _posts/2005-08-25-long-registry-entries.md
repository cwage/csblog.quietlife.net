---
layout: post
title: "long registry entries"
date: 2005-08-25
author: Chris
categories: [News, Alerts]
---
A rather nasty bug in Windows has a [rather unfortunate result](<http://isc.sans.org/diary.php?date=2005-08-24>):

> What started like a nice and quiet day ended with the potential for lots of nasty surprises. A reader alerted us to a vulnerability note published by [Secunia](<http://secunia.com/advisories/16560/>) that on first sight did not appear to be overly scary. Once we started to play with it, though, the nastiness became apparent: An overly long registry entry can be added, but won't be shown by regedit and regedt32. Even better, all registry entries that get added afterward under the same key, even if not overly long, will be hidden as well. 
> 
> [Pause, to give your wheels some time to spin] 
> 
> Yes. This allows to add hidden entries under the famous HKLM\Software\MS\Windows\CV\Run. Entries that you can't see with regedit, but that will just as faithfully get run at startup. 

More info [here](<http://isc.sans.org/diary.php?date=2005-08-25>).
