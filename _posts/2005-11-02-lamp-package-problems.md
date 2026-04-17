---
layout: post
title: "LAMP Package Problems"
date: 2005-11-02
author: Chris
categories: [Linux/BSD, PHP]
---
My [previous post](</2005/11/02/phplive-best-app-ever/>) on PHP Live! reminded me of a rant I've been meaning to write about the state of some (note: some, not all) LAMP packages and the difficulties in installing and maintaining them. PHP Live! is an example of how easy and painless it can (and should) be. Others, however, suffer from a lot of the same problems:

**1) Convoluted install process.**

[GForge](<https://web.archive.org/web/20051102092117/http://gforge.org/>) is probably the best example of this I've ever encountered. In their case it's understandable, since gforge is a fork of the [sourceforge](<https://web.archive.org/web/20051103010913/http://www.sourceforge.net/>) code, which is obviously a loose amalgamation of stuff to begin with. But at the end of the day, there are no excuses for its installation process. For example, here is a snippet from the "WEB SETUP - MANUAL INSTALLATION" section in the INSTALL file. (You'd think "MANUAL" installation would be as opposed to an automatic one somewhere, but not that I could find):
    
    
    tar -xjf gforge-4.0.2.tar.bz2
    mv gforge-4.0.2 /var/www/
    cd /var/www/
    ln -s gforge-4.0.2 gforge
    mkdir mailman
    mkdir uploads
    mkdir jpgraph
    mkdir scmtarballs
    mkdir scmsnapshots
    mkdir localizationcache
    	
    #project vhost space
    mkdir homedirs
    mkdir /home/groups
    ln -s /home/groups homedirs/groups
    	
    etc...
    

It goes on like this for nearly 2-3 pages.

So, what are the problems with this? First, of course, is that these instructions are meaningless for anyone that doesn't have shell access. Second is that they are meaningless to anyone who isn't familiar with the guts of a UNIX shell in general. But these are forgiveable. The gravest sin is that these instructions are completely meaningless for a server that doesn't match their configuration. Creating random directories in /var/www? Creating random directories in /home/ to support their app? I don't think so. [Debian](<http://www.debian.org/>) follows the [FHS](<http://www.debian.org/doc/packaging-manuals/fhs/>) as closely as possible for a reason, and I am not about to manually unpack all this crap on my server without some way to keep track of it, much less in a slew of non-standard locations.

And these locations differ for any other distribution as well. It's not impossible to translate what the instructions **mean** to say, but regardless, it's a lot of work. I estimated by the full length of those instructions, it would have probably taken me 2 hours to install, and that's if I **didn't** try to translate their directory/setup choices into something more standard, much less try to make a package out of it. 

The icing on the cake here is that gforge requires Register_globals to be "on" for PHP -- which is akin to opening the door to every PHP exploit on the planet.

Conversely, PHP Live! does what I would expect, and what every good web app should do. It wasn't picky about where it was installed, and the instructions were clear and concise:
    
    
    1. gunzip, untar or unzip the application somewhere on the server that
    you can access it with an \"http:\" address.
    2. (UNIX Only) Change the permissions of the \"web/\" directory to be
    write able by the browser.  The \"web/\" directory is located in the root
    unpacked directory of PHP Live!.
    3. Create an empty MySQL database to be used by PHP Live!.  Remember to
    restart your MySQL server if you added a new user.  (Don't create any
    tables, just create an empty database.)
    4. Visit http://www.yourservername.com/phplive/
    5. The setup will walk you through an automated, painless Q&A session.
    Finish the questions till you get to the \"Success\" screen.
    

And that's it. It handles smoothly all the stuff it should -- creating the tables according to its own schema, populating data. It all Just Works, and well within the confines of the directory I set up for the virtualhost in /var/www/support.centresource.com/

**2) Terrible upgrade processes.**

[SugarCRM](<https://web.archive.org/web/20051103025128/http://www.sugarcrm.com/crm/>) wins the award here. The first problem is that SugarCRM requires you to upgrade sequentially through **every single revision** released after the version you are using. I pity anyone that lets their instance of SugarCRM get as out of date as our installation is, since it takes no less than **seven** upgrades to get current.

To make matters worse is the fact that they changed the upgrade method between many versions. Some versions have a "wizard", some require manual steps. And none of the wizards, in my experience, worked much at all -- meaning it was clear that I'd have to take manual steps to fix whatever it was the upgrade "wizard" failed to do. To this day I still haven't upgraded SugarCRM because I simply don't have the time to do everything necessary.

**3) "Smart" packaging**

Perhaps in response to the ease of installation of things in the world of Windows, a lot of LAMP developers have taken to publishing their code in an "all-in-one" type package that includes everything necessary to run their application's **functionality**. [VTiger](<https://web.archive.org/web/20051102094740/http://www.vtiger.com/>) is a great example of this. VTiger is a fork of the SugarCRM code that they have improved and repackaged, along with everything you need to run it: Apache, Postfix, etc. The problem is they have no provision for people that, you know, are **already running** this software. It's nice that they are trying to be accomodating to people that are buying a server, installing an OS and then letting Vtiger do its thing, but here in the real world, applications are usually installed on boxes already in use for other things.

It's not impossible of course to extrapolate their PHP code itself from the "smart" installation package as a whole, but it essentially means doing everything by hand, and fixing everything in their code that incorrectly assumes things about my config and the software I am using.

Not all LAMP packages suffer from the problems highlighted above, naturally, but it's disturbingly common. It's as if they package and release their code without considering that people are actually going to be installing it on servers that **aren't** identical to their own. (Shocker, I know.)
