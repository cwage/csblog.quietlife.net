---
layout: post
title: "6 Tips and Tricks for Designing with the 960 Grid System"
date: 2009-06-15
author: Jason O'Brien
categories: [Web Design]
---
If you're not familiar with CSS frameworks, you should be. They create a baseline from which designers and themers can create websites, standardizing basic layout options with a common toolset and language. I was passionately opposed to them for the longest time because I feared we would lose the art and beauty of designing and XHTML/CSS coding. My opinion changed once I discovered the 960 Grid System.

As soon as you hit the 960.gs homepage, you see actual screenshots of websites using the framework with an option to overlay the 12 or 16 column grid template. The first link you see on the site is an option to download templates for Photoshop, Illustrator, and OmniGraffle -- oh, and the framework itself is included as well. Finally, a framework for designers! I'm getting verklempt just thinking about it.

I'm no developer, but I felt right at home with 960 from the beginning. Instead of wasting time setting up guides in Photoshop and worrying about proportional structure, I can focus on bigger, more important issues such as what I want a user to focus on, how to get them to a conversion page, or what color scheme might make the most sense. For those just getting started or interested in learning it, I give you six of my favorite tips and tricks for designing with the 960 grid system.

### 1\. Use your background space effectively

As the background of a website can exist outside of the 960 pixel container, it's a wonderful place to experiment with unique visual elements and horizons, as seen on Bryan Veloso's avalonstar. Designers now have some rote options for working with backgrounds, such as repeating horizontally a la Drupalcon 2009, highlighting your content by making an elegant centered background like on the Bellingham Real Estate site, or using a full photographic background like on Housing Works.

  * [![avalonstar's grungy background texture](http://blog.centresource.com/wp-content/uploads/2009/06/thumb_avalon1.jpg)](<http://avalonstar.com/>)avalonstar's grungy background texture
  * [![DrupalCon 2009's repeating city background](http://blog.centresource.com/wp-content/uploads/2009/06/thumb_drupal.jpg)](<http://dc2009.drupalcon.org/>)The DrupalCon cityscape background
  * [![Large photographic background on Housing Works](http://blog.centresource.com/wp-content/uploads/2009/06/thumb_housingworks1.jpg)](<http://www.housingworks.org/>)Large photography on Housing Works



The background is truly a freeform canvas. You don't have to worry about browser widths or how it might work with dynamic content, so go to town.

### 2\. Pull or push outside the grid

It's hard to deny the cold and inescapable reality of the pink columns if you sit and stare at them long enough. But fear not! With the power of CSS positioning, it's no problem to break out of those constraints.

![Popcorn Thumbnail](http://blog.centresource.com/wp-content/uploads/2009/06/thumb_popcorn.jpg)

In this example, I've moved the logo about 25 pixels outside the left edge of the grid container to help the design feel a little more free and flowing. It's often helpful to limit the width of an element you are pushing or pulling to a specific number of columns. I measured the logo out to be about 9 columns in width (out of 16 available columns), which means a front-end designer can apply a grid_9 class to the logo and then position it outside of the grid using CSS. Easy for them, easy for me.

Being able to push and pull things can lead to some extraordinary things and helps you remember that you're not as boxed in as you might think.

### 3\. Mix 12 and 16 column grids in the same design

While the default 12 column grid template is fine for most projects, some designs might require the additional flexibility and finer control of 16 columns. Newspaper and magazine styles can benefit the most from the extra grid control, especially when you might need to nest multiple small columns. But there's no rule that you can't use BOTH the 12 and 16 column grid in the same design.

![12_16_mix](http://blog.centresource.com/wp-content/uploads/2009/06/12_16_mix.jpg)

In this example I have a simple layout that utilizes both grid templates. The top section is more open and simple and worked well with just 12 columns. The bottom section gets a bit trickier. I really wanted 4 columns and some specific layout tricks that would have been more difficult using the default grid template. As you can see, it's as simple as placing the 16 column grid in the design and having at it.

### 4\. Rotate the template for a poor man's baseline grid

Since the 960 grid has 20 pixels of margin between each column, you can rotate the grid template 90 degrees and get a nice vertical grid to work with. While the common baseline grid is based on 18 pixels, I find working with a 20 pixel vertical margin helps keep the overall structure standardized and clean.

![baseline](http://blog.centresource.com/wp-content/uploads/2009/06/baseline.jpg)

I've modified the 12 and 16 column template that comes with 960 to include this baseline grid to have it readily available.

### 5\. Perfect your proportions

One of the biggest benefits of using 960 when designing is there's no guesswork over the general size of content areas. The most commonly used format for the web is 2/3 of the overall page width for the main content and 1/3 for sidebar content. In 960, that's as simple as fitting your main content inside 8 columns and your sidebar content inside the remaining 4 columns. Easy!

![proportions](http://blog.centresource.com/wp-content/uploads/2009/06/proportions.jpg)

Obtaining complex layouts without grids can be painful because alignments need to be acutely defined. Imagine having to deal with a complex 6 column layout and working through issues of a section being 230 pixels versus 235 pixels wide, and how that 5 pixel difference might affect everything else on the page. 960 takes away a lot of the guesswork and tedium and allows you to focus on information flow and overall look and feel.

### 6\. Ditch the grid

That's right, one of my favorite things to do when designing with 960 is to turn the damn thing off. The template is great for setting up the general size of your content areas and for lining things up, but you shouldn't get into a habit of leaving it on while you design. Those columns can literally start boxing you in, so ditch them and feel free to get curvy.

### In Conclusion

If you've never designed with a pre-built grid and framework, now's the time to give it a try. I've found the 960 Grid System to be a valid answer to shrinking budgets and timelines. Even though I was previously a spokesperson against frameworks, I now find them to be useful in many situations.

I'd love to hear what other people think, so leave your comments below. Is designing with a grid helpful or a hinderance?
