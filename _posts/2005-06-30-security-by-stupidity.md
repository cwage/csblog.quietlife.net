---
layout: post
title: "security by stupidity"
date: 2005-06-30
author: Chris
categories: [Miscellaneous, Development]
---
I originally switched to Suntrust primarily because I was fed up with First Tennessee's online banking system and Suntrust's was much better.

They have made a lot of changes recently, and I am considering switching again, namely because Suntrust's site has gone from bad to worse over the last year, both in matters of web-design and in security (or lack thereof). Among my problems:

  1. Usernames are actually your social security number.
  2. Passwords have a 6-character length **limit**. **6 characters!**. After all, we don't want **too** much security.
  3. The login-page has javascript that **won't even submit** the form if the password attempted is not between 4 and 6 characters. This, as far as I can tell, is to hand the password lengths on a platter to anyone wanting to brute-force crack them.
  4. Their online bill-pay is now IE-only.
  5. Even with IE, their bill-pay system is like a case-study in bad UI design. This is a screenshot of the section where I manage the payments for a particular vendor, which works only in IE, mind you. I had to fire up VMWare just to get this screenshot. In this case, my auto-payment to [butler.net](<https://web.archive.org/web/20050615002449/http://www.butler.net/>):  
[![Suntrust Billpay Interface](http://blog.centresource.com/wp-content/thumb-suntrust.png)](<http://blog.centresource.com/wp-content/suntrust.png>)  
Note the convenient items for "Payment 1" -- what exactly is "Payment 1"? Who knows. But you can delete it! 



The discrepancies between the rest of Suntrust's site and this new bill-pay section make it obvious they paid/hired a different contractor to do this billpay section, and it seems to be a case-study in what happens when you try to get web-development on the cheap. It's **terrible**. Non-standard, non-functional, and inaccessible.
