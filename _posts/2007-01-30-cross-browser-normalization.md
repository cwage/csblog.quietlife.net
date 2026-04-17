---
layout: post
title: "Cross-Browser Normalization"
date: 2007-01-30
---
If you work in a web design or development firm, then you are probably already very (if not too) familiar with the various idiosyncrancies across the major browsers. Even before you start to apply the stylesheets you can spot noticable differences in the way the browsers render the html. This is because the major browsers come with a default stylesheet they use to render html when nothing else is available. It is a very simple stylesheet, mainly affecting paragraphs, headings, links, and fonts. This is why, without any styling, unvisited links appear blue with an underline, among other things. While using links is a trivial example, small differences in font sizes and paragraph margins can become a headache and can cause you to start adding unnecessary fluff to your well crafted stylesheets. There are some techniques you can utilize to minimize the damage, or what we in the industry refer to as browser normalization.

First, I recommend you head on over to Yahoo Develper Network. The good people there have already taken most of the hard work out of browser normalization for you. There are two stylesheets you can download. The first is called reset.css. It sets defaults values for paragraph margins, body tag margins and padding, and headings among other things. The next stylesheet you need to download is fonts.css. This does the same thing as reset.css, but for fonts.

These two files should be the first stylesheets you call in your html. This way, you are provided with a relatively clean slate across all browsers to begin working on your own stylesheet. The first time I tried this technique out, I started without the normalizing stylesheets and viewed my page in Firefox, IE 7, IE 6, and Opera. I rapidly switched between the browsers to spot the differences. Some were very noticable, others not so much. I then applied my reset.css and fonts.css and repeated the same process. The result was very pleasing. Now, I was hard pressed to spot any differences.

BTW - While your visiting Yahoo, be sure to peek around. There are a ton of web designer and developer goodies up for grabs, as well as lots of literature to peruse.

The next thing I would recommend is getting in the habit of always using a DOCTYPE in your html. This is not only a good practice, but it is the standards compliant way of writing markup. Having a DOCTYPE tells your browser how to parse your markup. Without it, the browser reverts to it's own methods. In IE 6, it goes into what is known as 'quirks' mode. Not only is this non-standard, but who wants IE acting any more quirky than it already does? When you add a DOCTYPE, IE goes in to "strict" mode, which is more predictable for web design and development.

Of equal importance, is that when you have a DOCTYPE, you can now run your markup through a validator. If you are not familiar with validating your markup, you should start to consider making it one of the most utilized tools in your web development arsenal. Running your markup through a validator allows you to quickly catch syntax errors you would have otherwise spent hours looking for. It also insures that your markup is keeping up to standards. There are several types of DOCTYPES to choose from, the most common today being XHTML Transitional, and the holy grail of all - XHTML Strict. Having markup that validates XHTML Strict is not only a badge of pride, but it also means that your markup is accessible and well formed. As with everything, the caveat here is that the validator is not smart enough to analyze your content, just the markup. So, once your html is validating, it is your job to make sure your markup is meaningful and the content is ordered properly to be accessible to those with text-only browsers, screen readers, and mobile devices.

### Resources:

**Yahoo Developer Network:**  
[http://developer.yahoo.com](<https://web.archive.org/web/20070127182318/http://developer.yahoo.com/>)

**reset.css:**  
<https://web.archive.org/web/20070130/http://developer.yahoo.com/yui/reset/>

**font.css:**  
<https://web.archive.org/web/20070130/http://developer.yahoo.com/yui/fonts/>

**W3C HTML validator:**  
<https://web.archive.org/web/20070130/http://validator.w3.org/>

**W3C CSS validator:**  
<https://web.archive.org/web/20070130/http://jigsaw.w3.org/css-validator/>

**IE - quirks and strict modes:**  
<https://web.archive.org/web/20070130/http://www.quirksmode.org/css/quirksmode.html>

**Other good resources for DOCTYPES:**  
<https://web.archive.org/web/20070130/http://www.w3.org/QA/2002/04/valid-dtd-list.html>  
<https://web.archive.org/web/20070130/http://alistapart.com/stories/doctype/>  
<https://web.archive.org/web/20070130/http://www.oreillynet.com/pub/a/javascript/synd/2001/08/28/doctype.html>
