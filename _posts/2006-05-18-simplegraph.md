---
layout: post
title: "Simplegraph"
date: 2006-05-18
author: Chris
---
I use command-line utilities to do data-mining on logs compulsively -- often in sick and twisted ways. There are many times in which I perform a tortuous serious of grep/perl/awk commands which wind up being fed to "sort | uniq -c | sort -nr" or something similar.

Those of you familiar with those commands already know that the result is a list of unique values added up and displayed with a total, e.g.:
    
    
       289 text1
       134 text2
       134 text3
    

This is pretty handy for visualizing statistics. The next step for visualization of course is graphing it. [GNUPlot](<http://www.gnuplot.info/>) is the reigning king of open-source graphing applications, but in this case, I wanted something simpler. I wanted something to which I could simply pipe the output of my various shell concoctions and get a graph on STDOUT. Unable to find anything, I wrote a simple perl script to do it. It expects the output of "uniq -c" on stdin or in a file given as an argument, and it spits out an image on stdout. That's pretty much all there is to it. The image is PNG by default, and the width of the image is 10 pixels * [num of rows] -- so if you have a lot of rows, you will get a very wide image, although you can constrain the image using the "-width" option.

You can find a copy of the script here: [simplegraph.pl](<http://blog.centresource.com/wp-content/simplegraph.txt>)

Let me know if you find any problems with it -- it was a quick and dirty hack job. Happy graphing!
