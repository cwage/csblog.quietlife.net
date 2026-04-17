---
layout: post
title: "Symfony Faux Form Serialization"
date: 2009-07-14
author: Brent Shaffer
categories: [Doctrine, PHP, Symfony, Web Development]
---
Recently, I ran into an issue when building a Symfony plugin for Slideshow renderings. When I added the support for multiple libraries, in this case Google Slideshow2 and JQuery Cycle, they had drastically different configuration options. JQuery Cycle allows you to use a list of effects, such as blindX and blindY. These effects are great, and I want the end user to be able to easily select between them. Google Slideshow2 allows the adding of thumbnails and traversing controls. Neither of these settings apply to the other, and this is only two slideshow renderers. What happens when I add another one? Five more? I could create multiple tables for each renderer, such as google_slideshow2_options and jquery_cycle_options. I could also just provide a textarea for key-value pairs (effect=blindX timeout=500) that the user typed in. I did not like either of these options, as the former struck me as over-architecting, and the latter as unusable.

The solution I ended up with was to use something similar to serialization techniques. This allowed me to configure dynamic forms, add options, and keep the whole thing in a single database field. The solution has worked great, and has only required a few extra lines of code to my form. With tweaking, I hope to turn this code into a widget, to allow it to be added quickly to any Symfony form.

If you are interested in implementing this kind of functionality, you can see my code [here](<http://brentertainment.com/2009/07/11/symfony-options-form-faux-form-serialization/>), or you can check out the code for [csDoctrineSlideshowPlugin](<http://www.symfony-project.org/plugins/csDoctrineSlideshowPlugin>) and see it in action.
