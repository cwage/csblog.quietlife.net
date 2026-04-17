---
layout: post
title: "Tools That Make My Job Easier"
date: 2010-01-04
author: Travis Roberts
categories: [Doctrine, Drupal, PHP, Symfony, Web Development]
---
### Bash Aliases

Working on a Mac, I spend a lot of my time in Terminal (the command-line utility). This is where I do all of my interaction with my local databases, the central Subversion repository, and issue various system commands. Some of these commands can get quite long and are time consuming to type out. That's where aliases come to the rescue!

On a Mac, you can simply edit a file in your home directory called either `.bash_profile` or `.bash_login` (this is a hidden file, so you'll have to edit it from the command line). Adding an alias is simple. Let's say you have a long command like `php symfony doctrine:build --all --and-load=data/fixtures/` (this is the command to build/rebuild the ORM components of a symfony site). That's a long command, and one I don't want to type out every time I have to run it. The solution, add the following alias:

`alias dbal="php symfony doctrine:build --all --and-load=data/fixtures/"`

Now, instead of typing out that long statement, you only have to type `dbal` as it is now aliased to the command. 

### Textmate Snippets

I do all of my coding in Textmate, which is the absolute best text editor if you are on a Mac (apologies to the `vim` fanboys). Textmate snippets work much in the same way as the aliases I mentioned above. They are shortcuts for pasting in a block of code or performing some function, and there are a LOT of them. I'm constantly finding new shortcuts that I didn't know about. 

All snippets are kept in what Textmate refers to as "bundles". You can get an HTML bundle, a Subversion bundle, even a Haskell bundle. The textmate Subversion repository houses all of these bundles, which you can peruse and download at your leisure at <http://svn.textmate.org/trunk/Bundles/>

### VMware Fusion

Fusion is a Mac application that lets you run Microsoft Windows (or Linux) on your Mac. It's great for cross-browser testing, because I can have multiple Windows instances. I have an instance for Internet Explorer 6 testing, and a separate instance for testing with Internet Explorer 7 and 8. This is a big time-saver over having to use a completely different computer or several computers to do cross-browser testing of Web sites. 

### Apple Spaces

Apple added the Spaces application for creating virtual desktops to the Leopard version of their Mac OS X operating system. It was one of the changes that I most looked forward to. Basically, this allows you to group application windows onto different virtual "desktops". I have five desktops: one for chat windows (Adium, IRC, Yammer), one for browsing, one for coding, one for email, and one for Photoshop or VMware Fusion. Having only one or two windows on each desktop drastically cuts down on the clutter and helps me navigate between applications much easier. 

### Google and Stack Overflow

You may think Google is a no-brainer but I mentioned it because, while it is helpful for finding information, you really need to know HOW to search to get what you want. That might be a topic for a whole separate blog post, but it makes a big difference in the information that is returned. While keywords are important for the search. Also try searching for your entire question (like "how to add symfony form validation"). Chances are, someone has already asked that exact same question, and you can find the post where it was answered. 

Stack Overflow ([stackoverflow.com](<http://stackoverflow.com/>)) is another great resource for programming questions. It's a forum for asking technical questions and getting answers from other members. If you can't find an existing answer to you question, you can ask the masses and usually receive at least one answer within a few hours. I've used this site several times, and the quality of the answers I've received have always been very high.
