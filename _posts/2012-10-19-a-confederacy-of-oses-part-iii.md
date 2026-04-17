---
layout: post
title: "A Confederacy of OSes, Part III"
date: 2012-10-19
author: Jeremy Holland
categories: [Hardware, Linux/BSD, Miscellaneous, Productivity, Utilities, Web Development, Windows]
---
Read [Part I](<https://csblog.quietlife.net/2012/10/15/a-confederacy-of-oses-part-i/>) and [Part II](<https://csblog.quietlife.net/2012/10/17/a-confederacy-of-oses-part-ii/>)

So my strategy is as follows: I use Windows to run web browsers, the odd desktop app like Photoshop, handy GUI utilities like calculators, media playback, and the like. On top of all this, I have installed VirtualBox and the easy-to-install Windows version of Vagrant, running a VM with the Ubuntu server distribution (I have no need of the gnome or any other GUI therein.. yet. That may change when I need to start running Selenium-based tests, but it'll do for now). I use two PuTTY windows - one on each monitor - to connect to the VM, which is configured to startup at boot. I forward the necessary ports from the host to the guest (made easily configurable by Vagrant) and provision the whole affair with Chef.

Internally, I use tmux, vim, and all the usual CLI tools of the trade to ply my own. Servers, databases, services and the like all run internally to the VM, and the only crosstalk I've yet needed to make use of is accessing guest-hosted websites with my host-based browser, a feat easily enabled by Vagrant's port forwarding. RDBMS GUIs will likely be needed soon enough, and the same solution will presumably apply thereto.

So, how has it been? So far, the experience has actually been pretty pleasant. After getting the VM's hardware and the general translation and keyboard layout bells & whistles configured to my liking, I feel for the most part that I'm back in my native Linux land when developing. No issues arising from the system being a VM have yet reared their heads, and aside from the MS chrome peeking around the corners of my terminals, I could almost be convinced that I'd never left. As far as the desktop bit goes, I'm still acclimating. However, the fact that the sound, the graphics, the power management - all the hardware in general - works perfectly without my having to tweak arcane configuration settings is a very great improvement over my earlier experience; and not having to forcefully implement hacky workarounds is a weight off of my shoulders.

That all said, I do have a few qualms. If you know of an acceptable solution to any of these, please comment and share!

  1. PuTTY is the best SSH client out of all those I've tried, and it's not that great. It's profile saving/loading system is nightmarish from a UX standpoint, the built-in fonts are fugly (though I can presumably use others once installed on the OS), but the thing that irks me the most is that I can't go fullscreen! I have absolutely no need to see any of that garish MS chrome on the edges of my screen, and having it present detracts from the real estate available to me for tasks of actual importance, as well as simply clashing aesthetically.
  2. The price of the full-featured Windows is prohibitive. There are certain features available only in the Professional or Business or whatever-they're-called versions of Windows 7 that I would've found quite useful, but that I don't really count as being worth the extra few hundred I'd have to lay out so to acquire (group policy editing comes to mind).
  3. No real shell script to speak of. Sure, there's VBScript and whatever that trash is that passes for a shell in cmd, but these simply don't possess the power and terseness of bash.
  4. The godforsaken automatic restart after update. I understand that Windows needs to update itself frequently in order for the boys in Redmond to have the slightest hope of plugging security leaks as fast as they're discovered, but I do not at all appreciate having my viewing of some video on Hulu interrupted without discernible warning by my computer suddenly rebooting itself. Turning this trash off is apparently one of the features they reserved for the "Professional" users, and I quite frankly don't see how this isn't a bigger issue among Windows users at large. I understand they'll "fix" this garbage in Windows 8, but for now, it is pretty off-putting.



Anyway, those rants aside, all in all my experience has not been unsatisfactory. Neither, however, has it been revelatory, and I believe I'll need more time to make a decision one way or the other. I'll keep you all posted!
