---
layout: post
title: "Joys of IRC Help"
date: 2005-11-30
author: Chris
categories: [Miscellaneous]
---
There's an old saying: "If you don't have anything nice to say, don't say anything at all."

There should be a similar addendum for IRC support channels: "If you don't have anything useful to add, don't say anything at all."

IRC support channels can be an extremely useful resource -- if someone is available and is able to help you out. Conversely, they can also be very frustrating, because you get someone who is incapable of helping you but feels compelled to offer advice or just berate you. The following is an actual conversation I just had on #mysql on OPN (the names have been changed to protect the unhelpful):

> 22:01 <cwage> if you do a select * from table; without any order by, how does  
>  mysql decide on what order to pull the rows by?  
>  22:02 <CaptainUnhelpful> cwage: undefined. don't rely on it. always specify order by if  
>  you want it. mysql will optimise it away if it's the same  
>  order it got the rows in (like it used an index to retrieve  
>  and you order on the same index field)  
>  22:02 <CaptainUnhelpful> cwage: rows have no order.  
>  22:02 <cwage> ok  
>  22:02 <cwage> is it just a matter of optimizing the read from the backend bdb  
>  or whatever as far as how it decides?  
>  22:03 <CaptainUnhelpful> cwage: is what a matter of what?  
>  22:03 <CaptainUnhelpful> cwage: it's, basically, none of the user's concern. and it's  
>  definitely not something you can rely on. if the server  
>  decides to do things differently, it can. rows have no  
>  implicit order in relational dbs.  
>  22:04 <cwage> i wasn't asking because i wanted to rely on it.. I was asking  
>  because I was curious  
>  22:05 <CaptainUnhelpful> cwage: You don't want to. it makes no sense. there is no speed  
>  advantage. if mysql doesn't need to sort, it won't. so why  
>  would you?  
>  22:05 <cwage> CaptainUnhelpful: why would I be curious about something?  
>  22:05 <CaptainUnhelpful> cwage: no, why mess with it. considering my explanation.  
>  22:05 <cwage> CaptainUnhelpful: are you reading the words I am saying, or are you just  
>  talking? 

This went on for a while, partially because I have a penchant for masochism. You can see here that this guy clearly has no answer to my actual question, but evidently just really loves to hear himself talk. But my post was not just to complain -- I do have a point. There are a lot of frustrating people on IRC (understatement of the century), but IRC can be a true godsend for assistance in your hour of need. But it can also irritating when you need it and it doesn't come through. Here are a few tips for getting help on IRC:

  * Use the IRC channels on [Freenode](<http://www.freenode.org/>). This network of IRC servers is designed to facilitate open-source projects, and contains the defacto IRC channel for just about every major open-source project. The signal-to-noise ratio is much higher, and there are fewer jacka$$es out to flex their geek muscles without actually answering your question (although there are some, as evidenced above).
  * Ask your question clearly and directly. Don't say "can I ask a question?" or "anyone here?" or "Anyone have any experience with _____?" You'll just get a snarky response in return. If someone has an answer for what you need, they'll pipe up whether or not you preface it with anything. IRC channels are busy places, so the regulars are understandably annoyed by lengthy exposition before a question.
  * Don't paste errors into the channel unless they are relatively short. Most channels have a pastebin that you can use to paste and get a URL instead.
  * And perhaps most importantly: be patient. There's nothing more frustrating than running up against a particularly frustrating and time-sensitive problem and getting nothing from the IRC channel but digital crickets chirping in the background. It's best not to get too worked up about this. Ask your question and wait. You'd be amazed how many times I've asked a question and just idled over night and had an answer in the morning. I've also had conversations with less than 3-4 clarifying questions over the period of a few days. Yes, it makes me wonder why I am not just using the mailing list, but c'est la vie. This brings me to:
  * Consider other avenues of support. IRC is convenient because it's realtime and immediate, but if you find yourself idling in the channel and asking "can anyone help me?" over and over. The digital crickets are trying to tell you something. In these situations it is wise to hedge your bets (or cut your losses, depending on how you look at it) and send mail to the devel/user mailing list for the project you need help with. It's often not much more trouble than using IRC and you will be communicating with a bigger and probably more experienced/devoted userbase. It may take longer for a result, but it may be a much better one.
