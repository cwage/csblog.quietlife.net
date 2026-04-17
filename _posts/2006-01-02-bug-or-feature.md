---
layout: post
title: "bug or feature?"
date: 2006-01-02
author: Chris
categories: [Malware, News]
---
F-secure has some [interesting commentary](<http://www.f-secure.com/weblog/#00000761>) on the latest [Windows WMF vulnerability](<https://web.archive.org/web/20060103101643/http://www.microsoft.com/technet/security/advisory/912840.mspx>):

> The feature now in the limelight is known as the [Escape()](<http://msdn.microsoft.com/library/default.asp?url=/library/en-us/gdi/prntspol_0d6b.asp>) function and especially the [SetAbortProc](<http://msdn.microsoft.com/library/default.asp?url=/library/en-us/gdi/prntspol_0883.asp>) subfunction.
> 
> This function was designed to be called by Windows if a print job needed to be canceled during spooling. 
> 
> This really means two things:  
>  1) There are probably other vulnerable functions in WMF files in addition to SetAbortProc  
>  2) This bug seems to affect all versions of Windows, starting from Windows 3.0 - shipped in 1990! 
> 
> "The WMF vulnerability" probably affects more computers than any other security vulnerability, ever. 

Impressive, and scary. Update those virus signatures, kids.
