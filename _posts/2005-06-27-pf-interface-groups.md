---
layout: post
title: "pf interface groups"
date: 2005-06-27
author: Chris
---
Some [cool additions](<http://marc.theaimsgroup.com/?l=openbsd-misc&m=111894940807554&w=2>) to OpenBSD's pf:

> An interface group, is, well, a group of interfaces (surprised,  
>  anyone?). Interfaces can join and leave interface groups any time, and  
>  can be member in an arbitary number of groups. The join and leave is  
>  done via ifconfig:  
>  ifconfig sk1 group dmz  
>  makes sk1 join the group dmz, and  
>  ifconfig sk1 -group dmz  
>  removes sk1 from that group again. A group is removed when it does not  
>  have any members any more and pf does not refer to it.  
>  So far, so good.  
>  Now, pf can use interface groups instead of interfaces basically  
>  everywhere now. Sounds simple, but is quite powerful.  
>  For example, you can (ab-)use interface groups as a kind of aliasing.  
>  Just a group with one member, and refer to that. For example, hang your  
>  dmz of an interface group called "dmz" - if you do this in a consistent  
>  manner, your ruleset is entirely independent from the underlying  
>  hardware, you make interfaces join the groups in their respective  
>  hostname.if files which are machine dependent anyway.
