---
layout: post
title: "window of exposure"
date: 2005-06-06
author: Chris
categories: [Malware, Spam]
---
E-mail filtering company Black Spider [focuses on a "window of exposure"](<https://web.archive.org/web/20050606075547/http://www.theregister.com/2005/06/02/virus_exposure_stats/>) for PCs during the initial spread of a virus:

> More than 295,000 virus-infected emails were sent to companies in the UK in May before anti-virus vendors could issue signature updates, according to email filtering firm BlackSpider Technologies. It's long been known that there is a 'window of exposure' - the interval between when a virus begins spreading and signature updates are issued by anti-virus vendors. BlackSpider has put a figure on this phenomenon in order to back up its argument that there's a high risk of infection during this 'window of exposure' for firms that rely on conventional anti-virus scanners alone. 

This is a huge issue that our clients on [Swirbo](<https://web.archive.org/web/20050522012737/http://www.swirbo.com/>) are shielded from. I myself was spoiled by it. We had a few clients that weren't on Swirbo and during the recent Sober.P outbreak they got hit and hit hard. It took many hours for the various A/V vendors to update their signatures and a few more for the clients to update them. And even then, their inboxes and "virus vaults" were still getting slammed by the incoming messages that have to be filtered and deleted. Resources like bandwidth, processing, and disk space are all still being used. Without an SMTP relay filtering service in place, there wasn't much I could go for them. They weren't in danger of being infected, but the worm was still a big problem for them nonetheless.

> "Blocking at the perimeter alone is dangerous because viruses can spread through variety of methods, such as IM and P2P, as well as email. Users need protection at the heart of their organisation," said Carole Theriault, a security consultant at Sophos.
> 
> Email filtering firms, such as BlackSpider and MessageLabs, counter-argue that their services are needed in addition to conventional anti-virus defences. The ability to recognise and quarantines viruses before patches are issued by anti-virus vendors helps corporate security, they argue. This approach also allows more aggressive filtering. 

Naturally, we couldn't agree more. As we've [noted before](<https://web.archive.org/web/20051125205959/http://blog.centresource.com/2005/05/12/clamav-effectiveness/>), ClamAV's effectiveness thus far is well-established, and during the Sober.P outbreak, clients of Swirbo **never even knew** that there was a new worm going around. We were blocking the virus hours before even the first A/V vendors started updating their signatures. Desktop anti-virus software is a must, but it's only one angle in a comprehensive war against the spread of viruses.
