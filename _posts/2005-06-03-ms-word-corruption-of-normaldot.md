---
layout: post
title: "MS Word: Corruption of Normal.dot"
date: 2005-06-03
categories: [Miscellaneous, Windows, Productivity]
---
For years, MS Office users somehow find a way to 'mess up' their office installation in a manner that prevents them efficiently working. Typically, I've seen users corrupt their Normal.dot file by creating macros, migration profiles, or trying to create custom templates which accidentally overwrite the Normal.dot file.

Before I give the advice, you should know that Normal.dot is the Microsoft Template file that is the basis for all the new word files you create. Only advanced users should manipulate it...

The main issue is what to do if you find your Normal.dot corrupted. Today, I experienced this and it inspired my post to help other users fix the problem.

I am not entirely sure what happened, but I believe it occurred when I was using a letterhead template. Somehow, the Normal.dot was manipulated - thus every new word doc I created had margins that were VERY wrong.

Here's the easiest way to fix the Normal.dot file. You'll need someone with the same version of office to send you a version of their file.

**Before we begin, Note:** You must have hidden/protected files showing in your file viewer. To do this, open up Explorer (not Internet Explorer), select:

1) File -> Tools -> Folder Options  
2) Click the View Tab  
3) Show Hidden files & Uncheck the two Hide Options

**On to restoring the file:**  
1) Open up Explorer and navigate to:

C: / Documents and settings /  / Application Data / Microsoft / Templates

2) Take the file that was emailed to you and copy/paste (Yes - replace the current version)  
3)**Voila! You're done**

**If you cannot get someone to send you the file from the same version of Office as you have... You can create a new profile on your computer. This will create a new user under the 'Application Data' path and you can get the Normal.dot file there.**
