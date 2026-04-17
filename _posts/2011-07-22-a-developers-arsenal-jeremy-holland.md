---
layout: post
title: "A Developer's Arsenal: Jeremy Holland"
date: 2011-07-22
author: Jeremy Holland
categories: [Miscellaneous, Productivity, Software, Utilities, Web Development]
---
So I'm reading all our designers' "Trapper Keeper" posts, and I figure, "why should they get to have all the fun? Developers have stuff to say as well!" In that spirit, here is my attempt to start a similar series for the development department here at CentreSource.
    
    
    class DeveloperArsenal < Programmers::Toolset
      include CentreSource::JeremyHolland
    end

**1\. What tools do you use daily in the course of your development, and why those tools in particular?**

1\. [MacVim](<http://http//code.google.com/p/macvim/>) The more-or-less canonical port of the fantastic Vim text editor (itself an extension of the vi editor). While the benefits the GUI MacVim offers over and above the native CLI vim are minimal for an experienced user, I wholeheartedly recommend MacVim for beginners new to the editor; you'll still retain use of your mouse and all the classic OS X key shortcuts (cmd-s, cmd-w, etc) so you can stay productive while learning the new paradigm. Yehuda Katz has [a great blog post on just this subject](<http://yehudakatz.com/2010/07/29/everyone-who-tried-to-convince-me-to-use-vim-was-wrong/>).  
2\. [iTerm2](<http://www.iterm2.com/#/section/home>) Hands-down beats the native OS X terminal application. The features I particularly like are automatic copy-to-clipboard on mouse selection of text, true fullscreen, the ability to split a single pane both vertically and horizontally so as to keep multiple shells open and visible simultaneously (even in the aforementioned fullscreen mode), and a number of other little perks and pluses.  
3\. [Sequel Pro](<http://www.sequelpro.com/>) Holy smokes, I cannot say enough good things about this product. It is a shining example of doing one thing and doing it **incredibly** well - which is providing a simple, beautiful, and easily usable interface that just plain old _shows you the data in your database_. No crazy-ass graphical query builders, no wonky schema fiddling screens or massively over-complicated index-generation wizards, none of that crap. Everything provides all the functionality I need in what is likely the best possible interface with which said functionality could be represented. My only complaint is that it's MySQL-only, though myself and others are crossing our fingers for PostgreSQL and SQLite support down the road a ways.  
4\. [Google Chrome](<http://www.google.com/chrome>) Simply the best, fastest browser out there. I used to be a Firefox man, but that browser's javascript engine needs to get off its behind and catch up to the rest of the world.

**2\. How did you get into development/programming/engineering, and what keeps you in it?**

I've always kind of been intrigued by software development. I started with BASIC on my family's Apple IIGS (10 PRINT "_[redacted - ed.]_ "; 20 GOTO 10;), though I obviously didn't publish any world-changing papers based on my experience therewith. I had tooled around with HTML while I was still in high school, back in the SGML-esque days when tag names and attributes were still written in all caps, and even started studying computer science at college. Of course, college being college, I promptly decided to go be a bohemian and make no money. Subsequently, real life being real life and lack of money being a serious impediment to the living thereof, it wasn't long before I took up the programming mantle once more, fell back in love with it, and made it the focus of my career. So here I am today!

**3\. Who is another programmer or developer you admire, and why?**

Martin Fowler. His books and experiences have contributed a great deal to my own understanding of object-oriented programming, and they remain among the first volumes I reach for when I'm facing down a particularly difficult modeling problem. When called upon to train new developers, I put [Patterns of Enterprise Application Architecture](<http://www.amazon.com/Patterns-Enterprise-Application-Architecture-Martin/dp/0321127420>) on their required reading list, especially since a great many patterns comprising the Ruby on Rails framework are implemented directly from the book in question.

**4\. How do you keep yourself up-to-date with the latest technologies and what new or upcoming tech are you excited about?**

I never stop being a programmer, and I never stop learning new things. While I definitely don't subscribe to umpteen-thousand RSS feeds, I **have** amassed quite a library during my career (of which I am quite proud - picture below), and am constantly reading a book at least somewhat related to the subject. As far as getting excited about new tech goes, it takes a lot to impress me, so said excitement is pretty rare nowadays. Still, if I had to say something, I'd say graph databases: still in their infancy, but I think a decade or so down the line we might be seeing some awesome implementations and uses for same.

[![](https://csblog.quietlife.net/wp-content/uploads/2011/07/2011-07-22_18-08-28_802-300x169.jpg)](<https://csblog.quietlife.net/wp-content/uploads/2011/07/2011-07-22_18-08-28_802.jpg> "2011-07-22_18-08-28_802")

A few aren't mine, but it's good to have our developer bookshelf in one place.

**5\. What's your favorite language of the moment? Why?**

Ruby, for its flexibility and power; Erlang is a close second, because I'm a lambda calculus nerd.

**6\. Do you have any advice for nascent developers?**

Get yo' math on, read like your life depends on it (it does), and most importantly **don't cop an attitude**. Help your fellow developers when they need it, and accept the help of the same when offered. The quality of our work always goes up when we work as a team (e.g. Pair Programming, which I also recommend you participate in early and often).
