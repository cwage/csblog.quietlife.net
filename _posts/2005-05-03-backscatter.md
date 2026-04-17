---
layout: post
title: "backscatter"
date: 2005-05-03
author: Chris
categories: [Spam]
---
Nick highlighted some of the disadvantages of E-mail handshaking as a spam prevention method (or "challenge/response" for the technical term) in [this post](</2005/05/03/100-accurate-spam-protection-is-a-lie/>). Yet another disadvantage is a little understood, highly problematic and confusing problem called "backscatter". What is backscatter exactly? To explain backscatter, we need to start with how mailservers dealt with unknown users in the past:

### Mailservers and NDRs

Once upon a time, in a magical far-off land, it was still safe to run a mailserver on the Internet relatively unfettered without fear of things like spam, viruses and other nasty problems clogging up your mailserver. Back in these days, a mailserver would generally accept mail for any domain it hosted (and sometimes others as well -- making it a dreaded "open relay", which didn't use to be quite the mortal sin it is now.) Once it accepted and queued the message, it would figure out what to do with it -- either relay it, or deliver it to a local recipient.

But, what if the recipient was an unknown user? The mailserver would simply generate a message to the sender of the original message with an error message saying, basically, "Sorry, I couldn't find this user." These messages are called NDRs for "Non-Delivery Receipt" (or sometimes DSN for "Delivery Status Notification"). The legitimate user that originally sent the message would receive this NDR and realize they sent their message to an unknown user -- perhaps because of a typo.

### Backscatter Defined

However, times have changed and mailservers have to be leaner -- and meaner. Why? Imagine, if you will, how these NDRs might behave in the face of a typical spammer's dictionary attack. A dictionary attack is when you attempt to use brute-force through a sequence of plausible strings (in this case, e-mail addresses) that have a chance of matching. Spammers (and viruses) will often use this technique to spam a domain by simply trying to deliver mail over and over to every conceivable username on a domain. The problem this creates with respect to NDRs from a receiving mailserver is twofold:

  1. Resource/Bandwidth utilization -- simply put, it takes a **lot** of resources to handle these completely illegitimate messages. Aside from the fact that they are spam, they are for users that **don't even exist**. The mailserver is forced to accept, queue, process, and re-deliver a message in response to every single message.
  2. More importantly, spammers and viruses are rarely so polite as to actually include a legitimate sender e-mail address. Instead, more likely, the from address is often forged entirely. Many viruses, when they propagate, simply snag two addresses from the infected user's addressbook for sending: one for the sender and one for the recipient. The result, when a mailserver receives this forged message containing a virus or spam to an unknown user, diligently crafts a NDR to send to the (forged) sender. The sender then receives a mystifying NDR for a message they never sent.



### Exploitation

This is a serious problem -- it confuses users and it overloads mailservers. It's very difficult to explain to your average user what these messages are and why they got them -- their instinct is to panic, thinking they did something wrong or in fact have a virus themselves. However, the problem doesn't end with mere annoyance. Spammers have discovered this weakness in mailservers and exploited it to their advantage. Why waste time trying to find an open relay when a spammer can simply find a mailserver configured to send NDRs for unknown users? They can simply craft messages to unknown users with **forged senders** that they want to get their message. The result is that the middle-man mailserver is effectively used like a mirror to literally "bounce" the spam to the hapless user who receives a message that is not only spam, but has a slightly increased change of being read because it appears to be a legitimate error message.

### Consequences

The end result of this is that a growing number of unsuspecting users are being plagued by torrents of these NDRs about mail they never sent, usually from spammers and viruses forging mail. But it's not just spammers. Unfortunately, some of the good guys have even gotten in on the act. For a long time, [Barracuda](<https://web.archive.org/web/20050507133954/http://www.barracudanetworks.com/>), makers of a popular anti-spam firewall, raised the ire of the anti-spam community by shipping their firewall out of the box to deliver NDRs -- it would notify the sender e-mail address of any message that was blocked containing a virus or a blocked attachment. People had to post [instructions](<https://web.archive.org/web/20050308174410/http://postmaster.gtcs.com/CudaFix.php>) on how to disable this very rude default behavior, and in fact [spamhaus](<https://web.archive.org/web/20050507024152/http://www.spamhaus.org/>) went as far as to start blacklisting spam filters like Barracuda that were misconfigured in this way, much to the relief of beleaguered mailserver administrators everywhere being overwhelmed with forged NDRs. Norton Anti-Virus for Exchange and many others exhibited to this unsavory default behavior for a while as well.

### Solutions

Fortunately, more people are being made aware of this growing problem, and unlike the thornier issue of spam in general, it's one that can be prevented fairly easily by mail server administrators everywhere, by simply configuring your mailserver to **reject** mail for unknown users right off the bat at the SMTP "RCPT TO" command, rather than accepting, queueing and generating NDRs. Any modern mailserver (as well as qmail and sendmail) will let you configure it in this way, and there's an excellent list of resources for doing this on many mailservers that you can find [here](<https://web.archive.org/web/20050526115516/http://spamlinks.net/prevent-secure-backscatter.htm#reject>).

This has no effect on legitimate errors, of course -- if a delivery attempt is made to an unknown user on a properly configured mailserver, the sending mailserver is able to see the reject message and deliver an error message to the sender on its own, while the receiving mailserver is spared the trouble of accepting the "DATA" command, queueing, processing, and sending an NDR. It's a win-win situation.

### Challenge/Response: Just Say No

And, to finally tie it all back in with what reminded me to post this at all: Challenge/Response systems are a very clever system for defeating spam. They do a great job protecting the user (with the exceptions that Nick laid out). Unfortunately, they are rather rude to the rest of the Internet -- suffering the same flaw that mailservers sending NDRs does. Every "challenge" sent in response to a forged piece of spam or a virus is yet another message flooding some hapless user's inbox. This can be inadvertent, or it can be intentionally used to spam people in the forged sender.

For this reason, Swirbo does not and will not ever considering implementing a Challenge/Response spam-defeating mechanism
