---
layout: post
title: "Comcast is Not a Business ISP"
date: 2007-06-28
author: Chris
---
Recently we had one of our regular (every couple of months) Comcast Nightmares. These happen now and again, and by now our entire company is fairly used to the "Comcast is down -- go work from home or a coffee shop" routine. This time, however, I wanted to detail a bit of what we experienced, and talk about what it means for us. First, a rough timeline of our original problems:

### Thursday 6/07

4PM -- Our comcast cable goes down hard. We reboot the modem and lights sync up fine, but we have no access to the internet. One of our employees called Comcast and they dispatched for the following morning (Friday 6/08)

### Friday morning 6/08

10AM -- Comcast tech arrives on-site. He checks the signal and it's fine, and then proceeds to replace the old SMC modem with a Netgear "business IP gateway". Unfortunately this didn't get us back up.

11AM -- After an hour or so of phone calls, he managed to get a laptop online via NAT from the router. This is good because it means whatever originally went wrong has been fixed, but he had no explanation for what originally caused it.

11:05AM -- Comcast tech looks satisfied and starts hinting that we're good to go and I ask about the static IP configuration and remind him that we're down until we get the static IP configuration. He clearly has no idea what this even means, so I have to convince him that he's not done, since he was arguing at first that "the static IP is something y'all have to do, we don't do that".

11:30AM -- After I convince him that we need the static IP (i nearly whiteboarded a network diagram to try to explain it to him, but he had no TCP/IP/routing/networking knowledge at all whatsoever), he called 2 different Comcast numbers, eventually getting someone. He wouldn't let me just talk to them, so I had to relay word-for-word what I needed, which he relayed to them: "They.. they're saying they .. they need a static.. static? right, static IP? a static IP configuration?"

11:40AM -- After finally relaying this to the woman he was talking to, she informs him that "We don't provide the static IP -- that's something the client has to provide.." As politely as I could, I let them know that I don't even know what that means. We pay for a static IP. They give us the IP, route it, and we assign it to our firewall. Pretty simple. We've had it that way for 2 years.

12:30PM -- Finally, they get the static IP config built and pushed to the new modem. At long last, we're back up and running. I pack up and head home.

2:30PM -- I get alerts from Nagios that our Comcast has gone down. Again. I venture into the office to check on it, and verify via troubleshooting that it appears our new modem has simply "lost" the static IP configuration again. (I know this because I can get online via NAT through the modem itself). I call comcast support, and an hour later, I finally get to a tech that knows what I am talking about, and they get the static IP re-pushed. I head home again.

3:30PM -- I get alerts from Nagios that our Comcast has gone down again. I head back into the office. Same thing. I call Comcast, same song and dance. This time, I again ask what could be causing this that the modem would simply "lose" its config so often. He doesn't seem to know, and asks if anyone "hard reset" the modem. No progress on that front, but he got us back up and running again.

4:45PM -- I get alerts from Nagios that our connection has gone down again. This time, however, just as I arrive at the office, it comes back up. It appears that this perhaps was just a "normal" outage. (The fact that I consider outages like these to be "normal" is an indication of the quality of Comcast's service.)

### Saturday and Sunday (6/09 and 6/10)

During these two weekend days, our cable went up and down around 3 or 4 times, for 15-20 minutes at a time. Though it concerned me, it never does any good to call Comcast support to "let them know" that it went down, so if it comes back up at all, we consider ourselves lucky.

### Monday (6/10)

Thinking that everything seems peachy keen, our employees arrived at the office fresh and ready for a productive day's work for a change. Unfortunately, looks can be deceiving. Not long into the day, we started to realize that something is wrong -- the re-emergence of a problem we had around 6 months ago that subsequently mysteriously disappeared.

The problem was that TCP sessions would timeout during inactivity. I knew this wasn't an issue with our firewall, because of the following reasons:

  * Our firewall config hasn't changed or been touched substantially in over 2 years.
  * The problem came and went (usually corresponding with Comcast needing to re-push the static IP config) while no changes were made to our firewall
  * While the problem is occurring, I could still see a connection in the pf state table (our firewall is OpenBSD running on a Soekris box).
  * I was able to reproduce the problem by setting up a laptop with the static IP and plugging it straight into the modem.



The problem was tolerable in the past, but this time it was much worse -- connections were timing out after around 5 minutes of inactivity. This doesn't sound like a big deal, but when you consider the amount of traffic we have that requires a persistent TCP connection, and how poorly some software deals with timeouts (*cough*Outlook*cough*), you can imagine how rough things were for us. Instant Messaging (AOL, MSN or Jabber) would stop working. E-mail (IMAP) would stop working. FTP control connections would stop working, etc.

Making matters worse, from a technical perspective, was that these connections didn't merely "time out" -- there was no RST or FIN packets sent to terminate the connection. It just disappeared. Traffic goes out, nothing comes back.

I will spare you the blow-by-blow of the troubleshooting for this problem, but you can probably imagine that a company with tech support that can barely understand and support the basic services they provide (i.e. our static IP configuration problems), getting them to understand a slightly esoteric (but devestating) TCP problem was a nightmare. Attempts were made to deflect the issue back to us were made at every turn. Every call was a new call -- no one was able to stay familiar with the problem, and no one every seemed to be working on the issue. I eventually managed to get is escalated to "tier two", who then said he was forwarding it on to their networking team, but I never heard anything from them ever again.

The only resolution came, **a week later** when I finally got a tier 1 tech to dispatch someone to try replacing the Netgear modem with an SMC modem similar to the one we originally had. This was scheduled for Thursday (6/13) between 10-12, unfortunately no one ever showed up. I got a phone call at 5PM from a dispatch tech saying he "had the wrong modem, could we reschedule?" So, Friday comes, and finally, around noon, he shows up with the modem and replaces it. After the usual phone-call song-and-dance he gets a tech that can push the config, and we're back up and runing. Problem solved -- no more timeouts. I don't know if it's a configuration issue, or if it's an issue with Netgear, or what.

I do know that Comcast surely doesn't know either -- but what's worse, is they don't care. Our entire company was forced to work at home for a grand total of **7 business days** due to these issues. To this date, no one has ever followed up on the original ticket(s) we filed about either issue to ask if it was resolved. I'm afraid to call, because as often as Comcast tech support fixes something, they break something else.

The important thing to realize about this story is that it's not unique. It's not a one-off experience. We've faced these difficulties every step of the way with Comcast, in multiple locations. They advertise their "business cable" as a business-grade Internet connection. It's not. You get more bandwidth, but that's it. No SLAs. No accountability. No customer service. Nothing.

Further, what I've learned about Comcast is that they are truly too big for their own good. They have so many different departments that even their employees don't seem to understand it all. Dispatched techs often make 2-3 phone calls before they even get the right person. Tech support never knows whether or not someone is actually being dispatched. If you've ever heard the expression _"the left hand isn't talking to the right"_ , that perfectly describes Comcast, except Comcast is a multi-armed Shiva, and none of the hands are talking to eachother. At one point, a tier-1 tech actually transferred me to Gateway. No joke. I wish I could make this up. He said that "he thinks the problem is with our internet gateway, so he needs to transfer me to Gateway @home support" (or something like that). Next thing you know, I was on hold with Gateway computers. Naturally, I had to hang up and try again.

I know that after I post this, I'm sure I'll get the standard "well, we have Comcast and it works fine!" comments. That's great. I'm not saying there's anything wrong with cable technology. It's wonderful. The problem is with Comcast's business practices and size. If you have no problems, generally, you're good to go. But good luck if you ever have any problems. We're moving to a new building this fall, and I can assure you, I won't even remotely consider Comcast as an option. The ramifications of this is that our ISP cost will easily double or triple. Painful, right? Not really. Not when you factor in the cost of the downtime we've suffered at the hands of Comcast. It's not a business-grade ISP. Period. It's a no-brainer for us.
