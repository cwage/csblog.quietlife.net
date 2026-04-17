---
layout: post
title: "Tracking down the source of Referrer Spam"
date: 2005-08-28
categories: [Miscellaneous, Spam, Security]
---
Referrer Spam is the bane of any blogger's statistic tracking. These low-life people attempt to trick bloggers into 'clicking' their URLs because the blog software lists them as the top referrers to the blog. This, as with other types of spam, causes grief because it exists purely to deceive and ultimately wastes time.

In the CentreBlog, our top 10 referrers are all Spammers - primarily split between online casinos and generic directories with hundreds of links. Given that its a Sunday afternoon and I some free time, I decided to go against the crowd and NOT IGNORE IT.

My hunt starts off by trying to figure out who the referrers actually are. I start off with a basic WHOIS search ([http://www.whois.sc](<https://web.archive.org/web/20050719235654/http://www.whois.sc/>)) on the #1 entry, thebenjamingate.com.  
_For the record,[Internic.net](<https://web.archive.org/web/20050828232308/http://www.internic.net/>) \- once known for their usefulness - is practically worthless in a WHOIS search._

Here are the results:
    
    
    Website Title: 	Gamble and Casino Content Provider
    Meta Description: Gamble and Casino
    Meta Keywords: Gamble and Casino
    Response Code: 200
    SSL Cert: No valid SSL on this Host, Get Secure
    Website Status: Active
    Reverse IP: Web server hosts 108 websites
    Server Type: Apache/1.3.33 (Unix)
    IP Address: 70.84.113.250 (ARIN & RIPE IP search)
    IP Location: - Texas - Dallas - Theplanet.com Internet Services Inc
    Blacklist Status: Clear
    Cached Whois: 2005-08-28
    Whois History: 2 records stored
    Oldest: 2001-03-01
    Newest: 2005-08-28
    Record Type: Domain Name
    Name Server: NS1.SERVERMATRIX.COM
    ICANN Registrar: NETWORK SOLUTIONS, LLC.
    Created: 2000-05-10
    Expires: 2006-05-10
    Status: REGISTRAR-LOCK
    

So now I know that:  
1) This domain has been registered for a long time (since April 10, 2000). This person is probably no novice when it comes to the Internet. Also, they have probably left a trail somewhere...  
2) The web server hosts 108 sites. I bet they are all Referrer Spam sites. If I can get this person stopped, I may make a small difference on the Internet!  
3) **The most important data:** I know they are hosted at [ServerMatrix](<http://www.servermatrix.com/>) (a division of [The Planet](<https://web.archive.org/web/20050828225454/http://www.theplanet.com/>)) and I know the IP address (70.84.113.250).

The WHOIS Site also returns the following contact info:
    
    
    	
    Registrant:
    Zhao, Jackie
       82-36 Grand Ave.
       null
       Elmhurst, NY 11373
       US
    	
       Domain Name: THEBENJAMINGATE.COM
    	
       Administrative Contact, Technical Contact:
          Zhao, Jackie
          82-36 Grand Ave.
          null
          Elmhurst, NY 11373
          US
          8008358336 fax: null
          jackie586@gmail.com
    	
       Record expires on 10-May-2006.
       Record created on 10-May-2000.
    	
       Domain servers in listed order:
    	
       NS1.SERVERMATRIX.COM         216.185.111.10
       NS2.SERVERMATRIX.COM         69.56.222.10
    	

Upon reading this info, I am doubtful that any of it is true. Even if it is, I highly doubt that anyone with the last name Zhao will have a real first name of 'Jackie'. When I see the phone number, I am immediately suspicious... Who has an (800) number? Nevertheless, I try calling it first... _SURPRISE, SURPRISE!_ It's a '**Sex Hotline** ' asking for my CC#. This guy is a real stand up fella. I bet his kids will turn out great...

Since that isn't his real number, I try to see if I can find him via [Reverse Phone Number](<https://web.archive.org/web/20050829002255/http://www.reversephonedirectory.com/>) lookup and address hunting. No dice - imagine that.

All I have left is his email address... so I decide to send him an email.

> Hello Jackie,
> 
> You have been spamming people's blogs/websites with 'Referrer Spam' - mine included. Why are you doing this? Its very hurtful to the Internet community and you put yourself and your family in the spotlight by doing this. Do you really want someone tracking you down in person to confront you about this? While the Internet is vast and complex, we live in a small world - I ask that you stop your spam attacks and earn your living in an honest manner.
> 
> Sincerely,
> 
> Nicholas Holland  
>  CEO / President  
>  CentreSource Inc.  
>  Nashville, TN 37210 

Before I contact ServerMatrix, I remember [a great article about a guy tracking down Spyware](<https://web.archive.org/web/20050921042049/http://blog.centresource.com/2005/05/04/why-make-spyware/>) and its affiliates. He brought up a good point - follow the money. So I go back to the culprit's website and identify who is paying the slime-ball his money.

On the page (beyond all the links to gambling), I notice 'Webmasters, remember to join our Casino Affiliate Program'. Here's the kicker, the link is:  
**adv.casinoblasters.com/index.php?JackyZhao**

So his name is not Jackie, but Jacky. So I go to Google and type in " _Jacky Zhao_ " for all exact matches. **EUREKA!** I find one 'Jacky Zhao' [offering to sell a domain](<https://web.archive.org/web/20051221043657/http://www.searchengineforums.com/apps/webmaster.forums/forum::buy-my-website/thread::1086441304/action::thread/>) (xjoke.net) and listing all of the page impressions it gets per month. Even more interesting, his name is listed in the actual text message as Jackie Zhao. So I hurriedly go back to the WHOIS site to see who owns xjoke.net.

Heeeeere's Jackie! But I am not 100% sure it's him - this Jackie is from China and the site now belongs to Andy Su. I try to visit the site, but the site won't resolve. What I am really looking for is the smoking gun - a site tied to this Jackie that shows up on the original casino site server.
    
    
    	
    Jackie Zhao
               Jackie Zhao
               No. 117 Dongda Road
               Fuzhou Fujian 350001
               China
               tel: 86 591 7510052
               contact@mp3cdsoft.com
    	

So I keep reading his posts on the SEO site, and I find another one where he is trying to sell a 'popular' software website with 300K impressions per month. I remember that his contact address for xjoke.net was ' _mp3cdsoft.com_ ' and I realize which one he is trying to sell. I pull up the site **AND IT ACTUALLY HAS A CASINO ANIMATED GIF AT THE BOTTOM**. Now I'm practically sure its the same Jacky/ie. Also, I see that the 'contact' address for the mp3cdsoft.com website is the same as the Admin Contact for the XJoke.net - located in China.

I conduct a tracert (trace-route command in DOS), but I don't get the smoking gun I was looking for - but close. The website, mp3cdsoft.com is hosted at ServerMatrix too - but on a different IP address. I conduct the normal WHOIS search on it, but all the contact info is blocked. It seems that a service called NameCheap.com will keep spammers info protected. My suspicions were confirmed when I saw the WHOIS database showed them as being listed as Spammers.

> Blacklist Status: Listed - Cached Today ([details](<https://web.archive.org/web/20050719235654/http://www.whois.sc/rbl/?ip=67.18.111.42>)) 

On a hunch, I decide to check other domains listed in our Referrer Spam list. I choose one, innerspacerecords.com, and launch a WHOIS on it. **BINGO - WE HAVE A WINNER!** Its listed at ServerMatrix, has Jackie Zhao as the Contact, and has the IP address 67.18.111.42 - the very same IP for mp3cdsoft.com. Its 100% confirmed, we now know it was the right Jacky.

At this point, I decide that my lack of Chinese will keep me from tracking him down. There are many entries in Google for a Jackie Zhao (including a blog!) but they are all in Chinese. Since my email to him wasn't rejected, I can only hope that it was a legitimate address and he'll read it.

Now, on to the prevention...

So I visit CasinoBlasters.com (remember the URL with good 'ole JackyZhao in the string) and send them an email:

> Greetings,
> 
> One of your affiliates is participating in 'Referrer Spamming' and his actions are causing a great deal of grief for honest Internet users. We are actively tracking the person and wanted to know if your organization supported this type of promotion and if not, would you assist us in stopping this person's activities.
> 
> Here is their affiliate string:  
>  http://adv.casinoblasters.com/index.php?JackyZhao
> 
> I look forward to your response. If we do not hear from you, we will assume you support this method of promotion and will include your service/company in our report.
> 
> Thank you,
> 
> Nicholas L. Holland  
>  CEO / President  
>  CentreSource Inc.  
>  Nashville, TN 37210 

It may be a while until we hear from them, so next I contacted The Planet / ServerMatrix. I called their 'abuse' phone at +1-214-782-7802 & their tech 'Chris' was quick to defer me to their abuse email: abuse@theplanet.com. I filed the following email:

> We've identified a Comment/Referrer spammer on your network with the following information:
> 
> **Name:**  
>  Jackie / Jacky Zhao
> 
> **Domains:**  
>  http://www.thebenjamingate.com  
>  http://www.ninetwork.com  
>  http://www.redsquirreldesign.com  
>  http://www.innerspacerecords.com  
>  ** Many more **
> 
> **Identified IPs:**  
>  67.18.111.42  
>  70.84.113.253
> 
> **Abuse Items:**  
>  Referrer / Comment Spam (logs can be provided)  
>  Fraudulent Domain Admin Contact  
>  ** Contact number is a Sex-Hotline
> 
> Thank you for your assistance. We (CentreSource) are also clients of ServerMatrix and want to ensure that service remains free of spammers and illegal/fraudulent operations.
> 
> Nicholas L. Holland  
>  CEO / President  
>  CentreSource Inc.  
>  Nashville, TN 37210 

At this point, we've accomplished the following:  
1) Identified the culprit  
2) Sent him communications asking him to stop his activities  
3) Alerted those that fund him  
4) Reported his abuse to the servers hosting his activities  
5) Mentioned his name (Jackie Zhao, Jacky Zhao) so that it shows up in the search engines and possibly shames him into better behavior.

If I get a response to any of the emails, I'll post them for everyone to read...

**Update 08/29/2005**

Jackie actually responded... although he ignored my original question of why he spammed in the first place. I responded back - here's the string:

> Our URL is http://blog.centresource.com. Why are you spamming blogs? That is not very nice and it upsets many people. I already reported the activity to your Casino Affiliate (Casino Blaster) and ServerMatrix. I ask that you stop this abusive practice.
> 
> NLH
> 
> Jackie Zhao wrote:  
>  > Hi  
>  >  
>  > What is your url? We will remove your website. We're sorry for the  
>  > inconvenience it may have caused to you.  
>  >  
>  > Thank you.  
>  >  
>  > Best regards  
>  >  
>  > Jackie 

**Casino Blasters also wrote back:**

> Dear Nicholas,
> 
> Thank you for informing us of this incident. Please note that we are very strict about our NO SPAMMING policy and the affiliate mentioned has been contacted about this.
> 
> Thank you again,
> 
> Jackie  
>  Affiliate Manager  
>  Customer Relations  
>  1-866-225-6909 

**And finally, the last note from 'ole Jackie**

> Hi
> 
> I have stopped it a few days ago.
> 
> Thank you.
> 
> Best regards
> 
> Jackie Zhao
