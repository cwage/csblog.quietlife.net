---
layout: post
title: "DKIM/DomainKeys"
date: 2005-06-02
author: Chris
categories: [Spam, News]
---
Yahoo and Cisco have [teamed up](<http://www.eweek.com/article2/0,1759,182>) in the battle against Spam:

> The two companies announced Wednesday that they are combining their two separate authentication proposals into a new specification called DomainKeys Identified Mail, or DKIM, and are planning to propose it as a Web standard. 

[DomainKeys](<https://web.archive.org/web/20050706054113/http://en.wikipedia.org/wiki/DomainKeys>) is a system Yahoo has been touting for a few years now. It's similar to SPF in that it's only a method of identifying the authenticity of a sender. It employs the DomainKeys SMTP header and a record in DNS. Basically, you add a digital signature to every outgoing message and place it in a DomainKeys header. The receiving SMTP server then has the option of looking at the envelope From: address's domain, and looking up the domainkeys record for that domain, which contains the public key (corresponding to the private key used to make the signature). The SMTP server can then verify the signature and thus the authenticity of the sender. The result is that SMTP servers checking Domainkeys will be able to categorize messages into roughly three categories:

  * valid DomainKey signature: authentic
  * invalid or missing DomainKey signature for a domain with the DNS record: forged
  * no DNS record or header: unknown status



It can then use this information to decide what to do with the message.

The idea is a clever one, unfortunately it has a lot of potential problems, some minor, some major:

  * Overhead -- all Mailservers using this system have to introduce cryptographic functionality for every message, which involves heavier computational overhead.
  * Security -- the signing process involves storing the private keys unencrypted on any server that wants to send mail. This introduces the very real possibility that these points will be under constant attack and the keys will frequently be compromised.
  * Authentication only -- This solution will never be the One True Solution to Spam because it's only a form of authentication -- making sure a sender is who they say they are. There's nothing to stop spammers from registering domains and using DomainKeys just like everyone else. After all, in that case, they **are** who they say they are. Proponents of DomainKeys counter this critique by arguing that when we've reached this point it will be much simpler to simply blacklist domains that use domainkeys and that have been caught spamming. At this point, it will basically be a battle of the resources spammers have to constantly register new domains versus the resources of anti-spammers to constantly blacklist them.
  * DNS Spoofing -- The reliance on DNS can be seen as a weakness that grows with the prevalence of DNS spoofing attacks.



It will be interesting to see what comes out of this partnership, because although DomainKeys, like SPF, is an interesting idea, I don't hold out much hope that it will stem the tide of spam.
