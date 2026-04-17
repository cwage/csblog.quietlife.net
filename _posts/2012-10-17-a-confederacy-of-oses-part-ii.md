---
layout: post
title: "A Confederacy of OSes, Part II"
date: 2012-10-17
author: Jeremy Holland
categories: [Hardware, Linux/BSD, Miscellaneous, Productivity, Utilities, Web Development, Windows]
---
[Continued from Part I](</2012/10/15/a-confederacy-of-oses-part-i/>)

Due to many factors, setting up Linux turned out to be Hell. Both the kernel and GRUB wouldn't have the ability to recognize the aforementioned pseudo-RAID array as a single disk until later (I'm still not sure if GRUB does), so I first had to effectively wipe the filesystem in its entirety and destroy all partitions; turn off the pseudo-RAID functionality in the BIOS (a miracle they allowed me to do so, considering everything else they expressly hid therefrom), re-partition the two drives as truly separate devices, and reinstall Windows on one disk while setting up Linux on the other. That was a night of my life I'll never get back, and I considered dropping Windows from the lot entirely, but figured it might be handy to have as a last resort / testing platform and so opted to keep it at the last moment.

Finally having completed the installation, I booted up Linux for the first time and went about the standard post-installation rigamarole of bringing in my dotfiles and configuration settings, installing the basic tools I use everyday, etc. There were other problems during the process, but I cannot fairly lay the blame for them at HP's feet. Switchable graphics - as this machine possessed - were still a relatively new and uncommon affair, and the distro kernel hadn't been built to include certain systems associated therewith. So that's  _one_ kernel rebuild right there, and I can assure you there were many more as time went on. Other issues include ACPI issues that  _to this day_ have not been completely resolved and reappear intermittently and seemingly randomly, a total inability to recognize the microphone, and other hardware-related woes. Still, I persisted, expending the elbow grease to fix what I could and resigning to live with the rest. When finished, I had a perfectly usable little hi-res Linux machine upon which to do my development that I could call 100% my own.

I have now used this machine for a year, and have thoroughly enjoyed it... when those issues I said I'd "live with" weren't driving me absolutely insane. Lately, however, I been having doubts about my choice of OS, cataloged as follows:

  1. I had started to miss certain proprietary software that is not made readily available on Linux (Photoshop comes to mind - I need it rarely, but when I do, GIMP simply isn't an adequate substitute). I could run it on Wine, sure, but all my experience with Wine has been less than pleasant, and I didn't want to go through that business again.
  2. I was becoming sick of the desktop quirks. I love Linux, and the developers of the various distros have my absolute and utmost respect; but the unfortunate fact is that drivers for hardware show up there last. Due to its low marketshare among PC OSes vendors have little incentive to develop them themselves, and in many cases, open-source and initially imperfect options are all that is available. That said, give it year or so, and you'll likely see solid drivers made available; but that year is one in which I'm not getting my full money's worth.
  3. Honestly, I was doing a bit of introspection and reexamining my prejudices against Windows. Why do I hate it so? Could it be that I'm not giving it a fair chance, not having used it in nearly 10 years? Windows 7 is purportedly a vast improvement to Vista; maybe it was time to give it a chance.



Because of these and other thoughts, I decided to try an experiment: I would switch back to the Windows 7 installation on my other, nigh-forgotten drive and try it out as my primary desktop for a few weeks, and see how it went. This post is the story of the start of that journey, and how i reached a place where I was at least not anthropomorphizing my machine in the most violent of fashions.

Now, Windows has its problems: certainly it's an absolute crap development environment if you want any real, low-level control of a machine, or if you want to do any development in a language that wasn't pinched off from the Great Golden Sphincter of Redmond. The registry's a horrid design that - despite purportedly being recognized as such by its own engineers - has stubbornly persisted through multiple versions and will almost certainly be there in the next. The built-in command-line interface (cmd) and nearly every third-party one I have yet discovered are all so underpowered as to be little more than curiosities and toys. I won't even get  _started_ about security. However, it does do one thing quite well: provide an ultimately pleasant, consistently usable desktop environment. For everything else - as they say - there's Linux.

[Continued in Part III!](</2012/10/19/a-confederacy-of-oses-part-iii/>)
