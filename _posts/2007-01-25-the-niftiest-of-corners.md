---
layout: post
title: "The Niftiest of Corners"
date: 2007-01-25
---
[Nifty Corners Cube](<http://www.html.it/articoli/niftycube/index.html>) is a javascript library written by Alessandro Fulciniti that enables you to easily implement rounded corners on your page. There are many different utilities out there on the web that do basically the same thing, but you'll be hard pressed to find one that does it any easier.

If you have ever attempted to implement rounded corners in your markup and css, you'll find that your markup quickly becomes riddled with presentational divs, loads of images, and the css seems to be playing the role of a bar bouncer. It's even worse if the content box you have rounded needs to be fluid in any direction.

Nifty Corners Cube solves this for us in just a few lines of Javascript. Here's how easy it is to get it going:

window.onload = function  
{  
**Nifty("#box_to_round", "big top");**  
}

In our example, we assign a window.onload function that will ensure our boxes get rounded every time the page loads/refreshes. The function Nifty(), is where all the work takes place. It takes two parameters. The first parameter points to the id of the element we wish to round (any block level element that takes up space on the page will work). This can be a comma separated list of multiple elements, and it can accept certain CSS selectors. The second parameter is a space delimited list of options that tell Nifty Corners how to round the box. In this example, we used the options 'big', which says to make the corner radius 10 pixels (there is also small(2px), and the default normal(5px)), and we used 'top', which will only round off the top two corners of the box.

There are several other options that allow you to fine tune your boxes. You can assign only one corner of a box to be rounded, and it even has built in support to create columns of rounded boxes. Also, you can call the Nifty() function as many times as you would like for as many elements as you need to. Just be sure to wrap them all in a window.onload (or the included NiftyLoad function).

Recently, we had a design to breakdown that made heavy use of rounded corners. For the first pass, we didn't use Nifty Corners. The markup was laced with tons of nested divs, and the CSS file was accordingly huge. Though the design was functional, it was fragile. Any future redesigns would have required alot of work. We went back and implemented the same design using Nifty Corners, and found that we were able to easily keep the markup lean (and validate XHTML strict), and the CSS file was reduced by nearly 800 lines. This means alot when time is money, and even more should the day come to redesign the site.

There are a couple of improvements I would like to see in future versions of Nifty Corners. Currently, Nifty Corners cannot support borders around your box. You can have a border set, but it will not round off with the rest of the box. Second, I would like to see better support for Safari. We found that it would work on Safari for nearly all applications, but when we attempted to round off a grouping of list elements (which worked in every other browser we tested), it just wasn't happening. Reading up on his site, it seems that support for Safari is new to Nifty Corners, so perhaps it won't be long before all the kinks are worked out.  
We tested Nifty Corners on Firefox 2, IE 7, IE 6, Opera 9, and Safari 2. It faired very well in all browsers (floats and padding couldn't even break it in IE 6!).
