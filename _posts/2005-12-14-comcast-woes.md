---
layout: post
title: "comcast woes"
date: 2005-12-14
author: Chris
categories: [Networking]
---
Well, we were and are giving Comcast a shot for our new office's internet access. While I am personally averse to Comcast's service and reputation, their product offering of 8Mbps/1Mbps throughput with a static IP is too much to resist. That is, it would be if we were actually seeing that. We've only had our firewall up for 6 hours, and here are the speeds I am seeing to our server in Dallas:
    
    
    ------------------------------------------------------------
    Server listening on TCP port 5001
    TCP window size: 85.3 KByte (default)
    ------------------------------------------------------------
    ------------------------------------------------------------
    Client connecting to picasso.centresource.com, TCP port 5001
    TCP window size: 16.0 KByte (default)
    ------------------------------------------------------------
    [  6] local 192.168.1.3 port 32820 connected with 1.2.3.4 port 5001
    [  6]  0.0-10.1 sec    216 KBytes    175 Kbits/sec
    [  6] local 192.168.1.3 port 5001 connected with 1.2.3.4 port 60231
    [  6]  0.0-10.3 sec  1.41 MBytes  1.15 Mbits/sec
    

Yes, you read that right. Our throughput is 1.15M/175Kbps up/down. Worse than our ADSL was. I am hoping this is just a problem on Comcast's end and not just normal congestion during the day, or we will be quickly moving to a T1.

**UPDATE:** This update comes with my tail between my legs. Those speeds we were getting look almost exactly like ADSL speeds, huh? Maybe that's because .. I left bandwidth throttling on our firewall at 1.5M/256Kbps. Woops. We're getting around 4Mbps/1Mbps now.
