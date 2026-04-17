---
layout: post
title: "Blacksheep: a new Firesheep Prophylactic"
date: 2010-11-20
author: Chris Wage
categories: [Miscellaneous]
---
Just a quick update: [Last month](</2010/10/27/firesheep-and-web-security/>), I posted about the threat of [firesheep](<http://codebutler.github.com/firesheep/>), and some countermeasures you can take.

There's a new tool on the block called [BlackSheep](<http://research.zscaler.com/2010/11/blacksheep-tool-to-detect-firesheep.html>). It's pretty clever -- it's a modified version of the firesheep codebase that makes fake HTTP requests of the sort that Firesheep would normally intercept and hijack, and detects the subsequent hijacking attempts. It won't do anything to prevent the attack, but it will help verify your suspicions of the nerdy guy with the thinkgeek t-shirt in the back of the coffee shop who hasn't ordered anything in a while.
