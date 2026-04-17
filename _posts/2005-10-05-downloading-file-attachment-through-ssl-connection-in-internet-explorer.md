---
layout: post
title: "Downloading file attachment through SSL connection in Internet Explorer"
date: 2005-10-05
author: Jonathan
categories: [Development]
---
If you are trying to download file attachments from a server with an SSL connection in Internet Explorer you may receive an error like one of these:

> Internet Explorer cannot download file from server.
> 
> Internet Explorer was not able to open this Internet site. The requested site is either unavailable or cannot be found. Please try again later.  
>  -or-  
>  The page cannot be displayed.
> 
> The page you are looking for is currently unavailable. The Web site might be experiencing technical difficulties, or you may need to adjust your browser settings.
> 
> Cannot find server or DNS Error  
>  -or-  
>  Office Application Name cannot open the file. 

The problem only happens if you are using an SSL connection when downloading the file attachment. Internet Explorer requires a specific header forcing it to cache the downloaded file. The problem is internet explorer deletes or never properly caches the files to let you save as or open the file.

The headers that I had to send in order to fix this issue were:

> Pragma: private  
>  Cache-control: private, must-revalidate 

This issue has been documented on the Microsoft Help and Support website. [Click here for the full Microsoft Help File on this issue](<http://support.microsoft.com/default.aspx?scid=kb;en-us;316431>).

Documentation on the issue can also be located in several comments on PHP's header() function documentation located [here](<http://us2.php.net/header>).
