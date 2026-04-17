---
layout: post
title: "dh-make-perl"
date: 2005-06-20
author: Chris
---
My friend Chris (no relation) has a [good post](<https://web.archive.org/web/20060925230457/http://utcc.utoronto.ca/~cks/space/blog/sysadmin/CPANProblem>) on the problem with CPAN for Perl modules, and other systems like it: namely, that they are a packaging system on top of the OS's existing packaging system. I have frequently been annoyed by this, and I feel silly now, because his post also points out the obvious solution that has been in Debian the whole time: dh-make-perl:

> Description: Create debian packages from perl modules dh-make-perl will create the files required to build a debian source package out of a perl package. This works for most simple packages and is also useful for getting started with packaging perl modules. Given a perl package name, it can also automatically download it from CPAN.
