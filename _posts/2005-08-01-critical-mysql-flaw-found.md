---
layout: post
title: "Critical MySQL Flaw Found"
date: 2005-08-01
categories: [Linux/BSD, Development]
---
Attention LAMP developers, MySQL has a critical vulnerability...

> A "highly critical" flaw has been reported in MySQL that can be exploited to cause a DoS (Denial of Service) or to execute arbitrary code on the open-source database, according to security alerts aggregator Secunia Inc.
> 
> The vulnerability lies in the fact that MySQL uses a vulnerable zlib library. Zlib is a data compression library used to support the compressed protocol and the COMPRESS/UNCOMPRESS functions under Windows.
> 
> The error occurs in "inftrees.c" when handling corrupted compressed data streams.
> 
> According to Secunia's alert, the flaw can be exploited to crash any application that uses the zlib library. Alternatively, malicious users can execute arbitrary code with privileges of the vulnerable application. 

[Critical MySQL Flaw Found](<http://www.eweek.com/article2/0,1895,1840146,00.asp>)
