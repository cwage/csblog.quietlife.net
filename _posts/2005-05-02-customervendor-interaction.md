---
layout: post
title: "customer/vendor interaction"
date: 2005-05-02
author: Chris
---
Just a quick note here. In this industry, we deal with a **lot** of different, varied technical vendors. This involves calling tech support and customer service often about problems or complications with the vendor. Because I am often in the position they are, it's important that we pay attention to that interaction and learn from it.

I have one piece of advice along these lines. When addressing/troubleshooting a problem with a customer, never, ever, **ever** let these words cross your lips:

> "Huh. I don't know. Works fine for me!"

That may sound like common sense, but it's easier to let slip with a comment like this than you realize. As an engineer, I know that it's easy to get defensive of your servers/systems. They're your "babies" -- and you might sometimes feel inclined to defend them irrationally. But saying something like this to a customer that is having problems is the absolute worst thing you can do -- it's absolutely infuriating. It also has the potential to make you look quite foolish in the event that there is a real problem. It's condescending, dismissive and rude. Don't do it -- even if you're right.

I was reminded of this because of a bit of interaction I just had with [ValueWeb](<http://www.valueweb.com/>). A customer was trying to get Valueweb to send me e-mail with a security code so that I could relay it to him so that he could change the contact info. However, I hadn't gotten the e-mail, so I called to clarify. After a bit of troubleshooting, it became obvious that their mail to me was being rejected by [Swirbo](<http://www.swirbo.com/>) because their mailserver was misconfigured:

> May 2 10:46:10 mta2 postfix/smtpd[3678]: NOQUEUE: reject: RCPT from pool78.mis.valueweb.com[216.219.249.78]: 504 <lotusnotes>: Helo command rejected: need fully-qualified hostname; from=<XXXXXX@valueweb.com> to=<cwage @centresource.com> proto=ESMTP helo=<lotusnotes>

This of course has nothing to do with spam-filtering per se and more to do with their mailserver being misconfigured and sending "HELO lotusnotes", which is an egregious violation of the [SMTP RFC ](<http://www.faqs.org/rfcs/rfc2821.html>)which specifies that you should send a FQDN (or a valid IP address) in the HELO command.

I told him, politely, that my mail system was rejecting his mail because his mailserver appeared to be misconfigured. His response was to laugh, and say "Well, that's the mailserver we use for all customer communication, so if something was wrong I think I would have heard about it by now."

This is a perfect example of what not to say. It infuriates the customer (me) and does nothing to solve the problem at hand -- is he accusing me of lying? I told him I didn't know what to tell him, short of reading off the RFC to him. Luckily, our Mexican standoff ended when he was able to send the message through a mailserver that was not misconfigured.

I tried to defuse the tension at the end of the conversation by politely explaining what the issue was -- and why most mailservers will accept mail from a server misconfigured as theirs is, but that with spammers on the rise, more and more mailservers are restricting their communication in this way1, and that that's the reason one server worked and the other didn't.

His response was "OK, thanks for calling." Oh well, that's what you get for trying to be helpful!

1 (This reminds me, there's an interesting point to be made about how the advent of spam and network abuse has forced concessions to the mantra coined by Jon Postel for protocol design: "Be liberal in what you accept, and conservative in what you send", making it no longer as practical. There's probably a lengthier article in here somewhere.)
