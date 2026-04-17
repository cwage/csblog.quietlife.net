---
layout: post
title: "Windows File Deletion"
date: 2005-10-19
author: Chris
categories: [Windows]
---
I have not been keeping up my rep as a bonafide Microsoft-hater lately, so here come some gripes with a few things that bug me in Microsoft software.

First up is a dangerous inconsistency in how Microsoft Windows handles file deletion. On your average workstation, when you "delete" a file, it's not actually deleted, but rather just relocated to the Recycling Bin. However, when you delete a file or files from a share on a server, these files are not copied to the Recycling Bin. They are in fact just deleted. This is probably because Windows engineers figured it wouldn't be practical to transfer all that data over the network to the workstation Recycling Bin (I guess). Why they didn't just have the deleted files be relocated to a recycling bin on the server is beyond me.

In any event, the ramifications are that users in Windows are generally not overly-cautious in deleting files because they generally have the safety net of the Recycling Bin. This dependency is dangerous when they encounter shared files because that safety net disappears. I just had a client call me with precisely this situation -- he had deleted (accidentally) an entire folder from a share and was asking why it wasn't in his Recycling Bin. Naturally we could retrieve it from a backup, but not everyone is so lucky.

At first I thought there was something I was overlooking here -- surely Windows wouldn't leave people hanging in such an obvious way, but alas, as some quick research [has confirmed](<https://web.archive.org/web/20051222125935/http://discuss.fogcreek.com/joelonsoftware/default.asp?cmd=show&ixPost=22273>) that this it's true.

One of the many ways in which [Samba](<https://web.archive.org/web/20051024000744/http://www.samba.org/>) has a leg up on Windows for filesharing is that Samba allows you to account for this problem by using the "recycle" vfs object so that files are never deleted, but are instead moved to a directory. Example config:

> [RecycleShare]  
>  comment = Share with Recycling  
>  path = /var/lib/samba/share/  
>  vfs objects = recycle  
>  recycle: repository = .recycle/%U  
>  recycle: versions=True  
>  recycle: keeptree=True  
>  recycle: exclude = *.TMP *.tmp *.temp *.cache ~$*.doc  
>  recycle: maxsize = 0
