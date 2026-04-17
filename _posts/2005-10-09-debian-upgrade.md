---
layout: post
title: "Debian Upgrade Issues"
date: 2005-10-09
author: Chris
categories: [Linux/BSD]
---
I had a client call me last week with a problem. They have 3 servers running Debian GNU/Linux. They had had a power failure the evening before, and everything had come back up fine except their Linux servers. All of them!

They all had the exact same problem, he said, "When I boot them up, they get as far as LI...." To even the most casual Linux user, this is a sadly [common problem](<http://home.att.net/~lilo-boot/faq_er.htm#li_only>). I realized that none of these servers had been rebooted since we performed a [Woody](<http://www.us.debian.org/releases/woody/>) to [Sarge](<http://www.us.debian.org/releases/sarge/>) upgrade, and something clearly hosed LILO.

This whole experience raised a number of questions for me:

  1. I fixed the LILO issue by just booting up the Debian install CD, breaking into a shell, and doing the "mount/chroot/lilo" dance, and then installed GRUB. But I wouldn't expect your average user to do this. I know that Debian has (or had, at least) some sort of "rescue" functionality, but I can't find any documentation for it on the web anywhere. Anyone know?
  2. I don't know if this is a bug, or what, but just about every person I have talked to about their Woody to Sarge upgrade has managed to hose their boot sector. I assume this is because somewhere in the installation process, lilo gets upgraded (naturally) but perhaps it's optional to re-run "lilo". In fact, I can imagine people specifically saying **not** to run lilo out of fear of hosing their boot sector. Well, it's burned a lot of people and it looks like it burned us here. Is this is an acknowledged problem?
