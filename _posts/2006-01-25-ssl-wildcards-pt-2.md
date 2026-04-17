---
layout: post
title: "SSL Wildcards pt. 2"
date: 2006-01-25
author: Chris
---
While researching the situation with [SSL Wildcards](<http://blog.centresource.com/2006/01/24/ssl-wildcards/>) that i mentioned yesterday, the plot seems to have thickened a bit.

Here's the situation as I see it so far. First, here's all I can find about what [the HTTP/TLS RFC](<http://www.ietf.org/rfc/rfc2818.txt>) says:

> Names may contain the wildcard character * which is considered to match any single domain name component or component fragment. E.g., *.a.com matches foo.a.com but not bar.foo.a.com. f*.com matches foo.com but not bar.com. 

This is rather vague, but it doesn't seem to prevent what we want to do. That said, here is the actual behaviour I am seeing:

Certificate specifies CN: *.domain.com:
    

  * Browser visits domain.com: yields a warning that the hostname does not match the certificate name in all browsers. **(Normal as per the RFC)**
  * Browser visits foo.domain.com: yields no warning in any browser. **(Normal as per the RFC)**
  * Browser visits foo.bar.blah.domain.com: yields a warning that the hostname does not match the certificate name _only in IE_. No warning in other browsers. **(Normal as per the RFC)**


Certificate specifies *.*.*.domain.com:
    

  * Browser visits domain.com: yields a warning that the hostname does not match the certificate name in all browsers. **(Normal as per the RFC)**
  * Browser visits foo.domain.com: yields a warning that the hostname does not match the certificate name in all browsers. **(Normal as per the RFC)**
  * Browser visits foo.bar.blah.domain.com: yields a warning that the hostname does not match the certificate name _only in IE_ **(Behaviour not specified by the RFC as near as I can tell)**. No warning in any other browsers.



So, the last one there is the real mystery to me. Why does IE think that foo.bar.blah.domain.com doesn't match "*.*.*.domain.com". A friend of mine speculated that wildcard matching in domain names used PCRE before IE came along, which would be nice. Verisign and rapidssl both claim that using anything other than "*.domain.com" is not possible, which seems flat-out wrong.

Does anyone have any input on this or a reference to an authoritative spec that would cover this? The RFC seems too vague, and sadly it's been left to the browsers to implement, but I can't find a reference for how IE handles domainname matching. (I'd just go look at the source, but...)
