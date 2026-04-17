---
layout: post
title: "Referrer and Comment Spam: A Primer"
date: 2005-04-30
author: Chris
categories: [Spam, Networking]
---
### Introduction

There is a growing nuisance for users and administrators of sites that run web servers, and, particularly, blogs like this one: Comment, trackback and referer spam. I figured I'd take this lazy Saturday afternoon as an opportunity to try to lay out the various issues and attempts to combat this increasingly costly problem.

Table of contents

  1. [Introduction](<http://blog.centresource.com/2005/04/30/referrercomment-spam/#s-Introduction>)
  2. [First, a Note on Spelling](<http://blog.centresource.com/2005/04/30/referrercomment-spam/#s-First,-a-Note-on-Spelling>)
  3. [What is HTTP Referer?](<http://blog.centresource.com/2005/04/30/referrercomment-spam/#s-What-is-HTTP-Referer?>)
  4. [OK, What is Referer Spam?](<http://blog.centresource.com/2005/04/30/referrercomment-spam/#s-OK,-What-is-Referer-Spam?>)
  5. [Why Referer Spam?](<http://blog.centresource.com/2005/04/30/referrercomment-spam/#s-Why-Referer-Spam?>)
  6. [What is Comment/Trackback Spam?](<http://blog.centresource.com/2005/04/30/referrercomment-spam/#s-What-is-Comment/Trackback-Spam?>)
  7. [Consequences](<http://blog.centresource.com/2005/04/30/referrercomment-spam/#s-Consequences>)
  8. [Solutions (and Non-Solutions)](<http://blog.centresource.com/2005/04/30/referrercomment-spam/#s-Solutions-\(and-Non-Solutions\)>)
  9. [Conclusion](<http://blog.centresource.com/2005/04/30/referrercomment-spam/#s-Conclusion>)
  10. [Links](<http://blog.centresource.com/2005/04/30/referrercomment-spam/#s-Links>)



### First, a Note on Spelling

Referrer or referer? "Referer" is, in fact, a [misspelling](<http://www.m-w.com/cgi-bin/dictionary?book=Dictionary&va=referer>). A common misspelling, however -- so common that it made it into the [HTTP/1.1 spec](<http://www.ietf.org/rfc/rfc2616.txt>). This is funny, but annoying. For the purposes of this article and others, we will resist being pedantic and simply refer (ha!) to it as "referer" spam, simply because it refers to the "Referer" header. We'll use the proper spelling when referring to the actual referrer (the HTTP client in question).

### What is HTTP Referer?

The [HTTP 1.1 RFC](<http://www.ietf.org/rfc/rfc2616.txt>) defines the "Referer" header as:

> The Referer[sic] request-header field allows the client to specify,  
>  for the server's benefit, the address (URI) of the resource from  
>  which the Request-URI was obtained (the "referrer", although the  
>  header field is misspelled.) 

Essentially, it's a way for an HTTP client to send in the HTTP headers the URI of the page that sent them there. For example, when I search for "centreblog" in google and click on the link to our blog, my web browser sends the following header:

`  
Referer: http://www.google.com/search?num=100&hl=en&lr=&q=centreblog&btnG=Search  
`

This is handy, because it gives the site administrator some insight into where the traffic on his webserver is coming from. Further, many of the most popular webserver log analyzers also depend on this info to provide statistics on the most common referrers. Not every web browser and HTTP client sends the Referer: header, however, so it should not be depended upon in any sort of web programming or analysis. Some web browsers, for example [Opera](<http://www.opera.com/>), give you the ability to turn off the sending of the Referer. While this improves your privacy as a web browser, it can impair your web-browsing because many websites check the Referer: header on requests for images, movies, and other forms of media likely to be "stolen" -- i.e. accessed directly rather than through the website hosting it.

### OK, What is Referer Spam?

While the HTTP Referer: header is very useful, it's also completely arbitrary. There's nothing to stop a web browser or HTTP client from sending a forged Referer: header with any request to a web server. You can even do it by hand:
    
    
    $ telnet blog.centresource.com 80
    Trying 70.84.100.10...
    Connected to picasso.centresource.com.
    Escape character is '^]'.
    GET / HTTP/1.0
    Host: blog.centresource.com
    Referer: http://whitehouse.gov/
    	
    HTTP/1.1 200 OK
    

It's that easy. And, much like spammers have taken advantage of the fact that there is no provision for authentication in SMTP, they have also clued in on this openness, using specially crafted requests with their websites in the Referer: header.

### Why Referer Spam?

You're probably thinking to yourself "Okay, I understand how Referer: spam works, but why would someone bother spamming something only the site administrator will see in the logs?"

That's a good question, and others have [speculated at length](<http://the.taoofmac.com/space/blog/2004-12-10>) on the various motivations. But, briefly, the reasons are generally:

  1. an attempt at boosting search engine rankings
  2. simply to show up in any stats published by the site. That is, if the site being spammed runs Webalizer, AWStats or some other webserver log-analyzing software, the spammer can get their URL in the "top referers" section.



There are probably other reasons, but we won't waste our time psychoanalyzing the degenerate mind of the spammer.

### What is Comment/Trackback Spam?

Comment spam and [trackback](<http://en.wikipedia.org/wiki/Trackback>) spam is a much more direct method that spammers have discovered. As the popularity of blogs has grown exponentially, so has their popularity grown with spammers. Initially, most blogging software (Movable Type, Wordpress, etc.) and most blogging sites (blogger.com, livejournal.com, etc) had very little restrictions against who could post a comment. There is simply an HTML form that POSTs to a CGI script which accepts and displays the comment.

Of course it takes very little technical knowledge to see that this is easily exploited by spammers who want to get their goods in front of people's eyes. These spammers have automated tools that are constantly searching for blogs that allow comments/trackback, and spam them with POST requests containing generic comments with their URLs. Sometimes the URL is in the body of the comment, the "URL" field of the comment, or both.

### Consequences

There are many consequences for those of us trying to use the Internet and the WWW in a reasonably productive way as a result of these two new methods of spamming.

**Tragedy of the Commons**

The first and most obvious is that comments on blogs have been overwhelmed by hundreds of comments advertising "c1al1s", "v1agra" and other wonderful things. Many blog operators have simply given up and disabled comments and trackback, delivering a serious blow to one of the most powerful aspects of blogging -- the network of communication and relationships built between people and blogging communities.

**Bandwidth, Bot-nets and DoS**

A more serious consequence is that the process of comment, trackback and Referer: spam is often performed via an HTTP "GET" or "POST request, which retrieves the entire body of the document being spammed. For example, if a spammer is sending "GET /index.html" to send his Referer: header, and index.html is a 30k document, all 30k is transferred across your Internet pipe. The ever-optimizing engineer in me feels compelled to point out to the spammers that they could simply issue a "HEAD" request and accomplish the same thing without wasting my bandwidth, but I don't want to encourage them.

Anyways, this all results in quite a bit of traffic on your webserver, and bandwidth is not cheap.

Further complicating the situation is the increasing prevalence of [botnets](<http://en.wikipedia.org/wiki/Botnet>) on the Internet. These massive networks of compromised computers are being used more and more to distribute the process of comment/trackback spam. This means that the potential for bandwidth usage increased exponentially. It also means that the comment spamming attacks can actually result in an effective [Denial of Service](<http://en.wikipedia.org/wiki/Denial_of_service>) attack.

While CentreBlog is relatively new and hasn't had much problem with comment/Referer spam, my personal blog at [chris.quietlife.net](<http://chris.quietlife.net/>) has been in operation for around 4 years now. I'd estimate that roughly 70-80% of the traffic on my site is Comment/Referer: spam. My Wordpress blacklist plugin blocks, on average, around 500-600 comment spams a day (more on prevention techniques later). On at least 4 or 5 different occasions my website was entirely shut down by comment/referer spam attacks. In the past I had been able to simply firewall off the offending IP addresses, but these were attacks by bot-nets, meaning they were massively distributed and impossible to block -- each request comes from a different IP address.

I simply had to shut down apache (my HTTP server) and wait it out. It was quite infuriating, because there was nothing I could do.

### Solutions (and Non-Solutions)

So, what's a webserver administrator to do? Here are a list of some of the prevention methods and their effectiveness:

**Firewalling**

Simply noticing an attack and simply firewalling it off is effective against the occasional limited attack, but in general this is a losing battle, and with the advent of bot-net attacks, has been rendered impotent.

**.htaccess**

By and large, this is also an unwinnable battle, but you can blacklist certain referers in .htaccess. For example, [this one](<http://underscorebleach.net/jotsheet/supplementary/block_referrer_spam_htaccess.txt>).

The ease with which spammers register thousands of domains and rotate them as quickly as they are blacklisted has rendered this ineffective as well.

**Comment/Trackback Blacklisting**

This is a largely effective technique to prevent comment spammers from wreaking too much havoc on your blog/website. It will do nothing to prevent a large-scale bot-net attack from bringing down your webserver (or eating up your bandwidth), however.

For Wordpress, I have had great luck with Fahim Farook's [WPBlacklist](<http://sm.farook.org/WPBlacklist.htm>) plugin.

For Movable Type, there's the ubiquitous [MT-Blacklist](<http://www.jayallen.org/projects/mt-blacklist/>) written by Jay Allen.

These plugins simply check comments/trackbacks against certain blacklisted URLs, IP addresses, etc. and denies the request if there's a match. This prevents the site from being overwhelmed but it still uses bandwidth and system resources.

As mentioned before, my personal blog gets around 500 per day, and the WPBlacklist plugin catches most of them.

**DNSBL checks**

A newer but more difficult technique to stop the bot-net attacks is by using [DNS Blacklists](<http://en.wikipedia.org/wiki/DNSBL>) to check requests to a webserver.

I've outlined the process by which you can use mod_access_rbl in apache to accomplish this in [this article](<http://chris.quietlife.net/2005/01/16/referrer-b-gone/>). The technique involves checking each web request against many of the popular DNS blacklists typically used to fight E-mail spam. This can help mitigate the success of attacks by bot-nets, since these compromised computers are often in blacklisted IP space, or IP space at least flagged as dynamic/dial-up/broadband IP space. You have to be careful with this, though, because networks that will be blacklisted from sending e-mail are not always suitable for blocking web access -- that is, you may inadvertantly cut off legitimate users of your site.

### Conclusion

This sort of spamming is a growing problem. As the popularity of standards for blogging interaction increase, so do the opportunities for spammers to use it to pollute the web. Further, the rise of bot-nets does not seem to be abating, contributing to the difficulty in reining in this problem. Like the problem of E-mail spam, this is a tricky problem to deal with (but not impossible *cough*cough*[Swirbo](<http://www.swirbo.com/>)*cough*). We will continue to keep this blog updated with the latest developments and tactics in fighting this growing problem.

### Links

  * [Tom Sherman's Summary and Proposal for combatting referer spam](<http://underscorebleach.net/jotsheet/2005/01/referrer-spam-proposal>)
  * Wikipedia's [entry on referer spam](<http://en.wikipedia.org/wiki/Referer_spam>)
  * An old entry on kuro5hin.org that provides a window into the early [origins](<http://www.kuro5hin.org/story/2001/5/30/22341/3757>) of this problem.
