---
layout: post
title: "hostile profiling"
date: 2005-05-24
author: Chris
---
Techweb [surveys](<http://www.techweb.com/wire/security/163700240>) a technique that phishers/spammers/cretins are using to "hostilely" profile users using simple registration/password reminder processes on popular websites:

> In a registration attack, a spammer tries to register large numbers of e-mail addresses -- using automated scripts somewhat similar to those used in directory harvest attacks -- with a variety of Web sites. Because sites typically return errors on addresses already in use -- Reshef said his research showed a majority of sites do this -- spammers and phishers can determine not only which addresses are valid, but match an address with a Web site.
> 
> ...
> 
> A password reminder attack is similar, but takes advantage of the habit of most Web sites to inform users that an address is either in use or not registered when someone requests a password reminder for that address. If the address has been registered, the spammer is usually told that the password has been sent, essentially validating the address. 

[Ebay](<http://www.ebay.com/>) gets a gold star for evidently thwarting the password reminder attempt, using a practice that all web programmers should consider using as well:

> Few sites use the simple techniques that can stymie such attacks. eBay seems to be one of them. When TechWeb tried the password reminder technique at eBay, and used the bogus address "john@invalid.com," eBay responded with "eBay just sent your User ID to john@invalid.com. Check your email to get your User ID." It didn't verify that the address was in use on the site or not.
