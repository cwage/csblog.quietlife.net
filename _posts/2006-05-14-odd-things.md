---
layout: post
title: "Odd Things"
date: 2006-05-14
author: Chris
---
My personal webserver has been getting slammed with requests for "/robots.txt", by what appears to be a botnet -- over 234 unique IP addresses so far, over the last week. But appearances can be deceiving. Here's where things get weird: All of the IP addresses have reverse DNS that has "planetlab" in it, which even resolves backwards to the correct IP. A smattering of examples:

> 14.1.31.128.in-addr.arpa domain name pointer planetlab4.csail.mit.edu.  
>  15.1.31.128.in-addr.arpa domain name pointer planetlab5.csail.mit.edu.  
>  16.1.31.128.in-addr.arpa domain name pointer planetlab6.csail.mit.edu.  
>  17.1.31.128.in-addr.arpa domain name pointer planetlab7.csail.mit.edu.  
>  12.36.4.128.in-addr.arpa domain name pointer planetlab2.pc.cis.udel.edu.  
>  143.6.42.128.in-addr.arpa domain name pointer ricepl-1.cs.rice.edu.  
>  145.6.42.128.in-addr.arpa domain name pointer ricepl-3.cs.rice.edu.  
>  200.67.59.128.in-addr.arpa domain name pointer planetlab1.comet.columbia.edu.  
>  201.67.59.128.in-addr.arpa domain name pointer planetlab2.comet.columbia.edu.  
>  202.67.59.128.in-addr.arpa domain name pointer planetlab3.comet.columbia.edu. 

And so on and so forth. They all appear to be universities. Does anyone have any idea what this is?

**UPDATE:**

A friend of mine did some digging and found the [culprit, planet-lab.org](<https://web.archive.org/web/20060428025648/http://www.planet-lab.org/>). Here is the response from support@planet-lab.org:

> Hello,
> 
> Apologies about the burst of web traffic. We are running an experiment  
>  to map the core of the Internet. Such a map will be extremely useful  
>  in understanding large scale Internet behavior and future Internet  
>  engineering projects. We have done everything we can think of to limit  
>  the load and intrusiveness of our experiments, for example, using the  
>  smallest file we can request (i.e., robots.txt) and limiting our request  
>  rate. A combination of software and human error has made our experiment  
>  appear less innocuous than intended, and we appreciate your understanding.
> 
> The http requests for robot.txt is what allows us to map the path from  
>  planetlab node into the core of the network. So while they appear  
>  useless, they actually provide a good bit of data about the underlying  
>  network. In any case, I have completed my scanning, so you won't see  
>  this problem again.
