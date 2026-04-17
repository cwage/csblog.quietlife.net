---
layout: post
title: "mock trial"
date: 2005-06-08
author: Chris
categories: [Security]
---
I don't know where these people found time to [hold a mock trial](<http://www.infoworld.com/article/05/06/07/HNispsinnocent_1.html?source=rss&url=http://www.infoworld.com/article/05/06/07/HNispsinnocent_1.html>) with all the real ones going on in the industry, but they did, and it looks pretty interesting:

> ISPs (Internet service providers) were put on "trial" Tuesday, with hundreds of IT security professionals serving as jurors, for not doing enough to keep subscribers' computers from being compromised and used as tools in attacks on corporate networks.
> 
> The plaintiffs, a couple of fictional companies hit by denial of service attacks, argued that ISPs could do more to prevent "zombie" machines used in attacks by scanning subscribers' computers, monitoring traffic and shutting down suspicious network uses. "ISPs are in the best position to take reasonable steps to diminish the threat," argued real-life cybersecurity lawyer Ben Wright, during a mock trial at the Gartner IT Security Summit in Washington, D.C. "It's very difficult to go out and find the hackers who are responsible for these attacks." 
> 
> But defense lawyer Stewart Baker, a partner in the Washington office of Steptoe and Johnson LLP, argued that it would be a violation of privacy for ISPs to check subscribers' computers. It would be nearly impossible for ISPs to distinguish between legitimate Internet traffic, such as a subscriber's browser updating a weather map every few seconds, and a computer being used in a denial of service attack, added Baker, representing a group of fictional ISPs. 

This is a fascinating debate. In the past, when I've mentioned [port 25 blocking](<https://csblog.quietlife.net/2005/05/17/port-25-blocking/>), good points were raised about the fact that most ISPs see this as a slippery slope insofar as:

  1. Being perceived as having rigid usage policies, and:
  2. Being held liable for lapses in their protection



These are interesting points, but I respectfully disagree that they are grounds for ISPs do to nothing at all. After all, the idea of a "slippery slope" argument is not an argument at all, but rather a fallacy. I agree that ISPs with draconian limits on what you can and can't do with your connectivity are annoying. That's why I enjoy [butler.net](<https://web.archive.org/web/20050612003417/http://www.butler.net/>)'s service so much. He gives you the DSL and is, by and large, hands-off after that. But I think to some extent we're in a different world, these days, and with spam being the problem it already is, and [botnets](<https://web.archive.org/web/20050609075057/http://www.honeynet.org/papers/bots/>) becoming one of the more prevalent threats on the internet, I think the bigger ISPs have an obligation to do something.

In the grand scheme of things, and particularly in light to the benefit to the Internet as a whole of being a **good neighbor** , ISPs bliocking outbound SMTP and monitoring usage patterns more carefully to identify, isolate and block obviously infected/compromised Windows "bot" PCs is a small price to pay. Until solid solutions are implemented to the problems with SMTP and the problems with Windows security, something must be done, and ISPs are in a position to help.

The legal angle is interesting, and I'm no lawyer -- can any of our readers speculate on the precedent for liability if a company (an ISP) provides a measure of protection to the community at large (blocking outbound port SMTP) and this protection fails, and there is some negative effect (say, furthering the spread of a worm)?
