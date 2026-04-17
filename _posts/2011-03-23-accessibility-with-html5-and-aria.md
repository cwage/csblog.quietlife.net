---
layout: post
title: "Accessibility with HTML5 and ARIA"
date: 2011-03-23
author: Joshua Stauter
categories: [Usability, Web Design, Web Development]
---
When designing markup for a website or a web app, it's important to keep in mind that what others see is not necessarily what meets your own eye. Accessible design means that page elements are encoded with information about the structure and content of the document, so that screen readers and assistive devices can make sense of them, lacking the visual faculties that most of us take for granted. And while accessibility generally refers to non-sighted human users, machine users (like search engine crawlers) will also greatly appreciate your consideration.

[HTML5](<http://en.wikipedia.org/wiki/HTML5>) and [ARIA](<http://en.wikipedia.org/wiki/WAI-ARIA>) are two standards that both take steps to address this issue and, conveniently for designers and developers, dovetail quite nicely as we'll see. Following is a chart of content roles that each defines:

**HTML5** | **ARIA** | **Description**  
---|---|---  
header | banner | Content that describes the site, like a logo  
nav | navigation | A set of links for navigating within the site  
section | main | Okay, I fudged a little on this one. "Section" is for a section of a document. "Main" is for the main content piece of a document. We'll use them together, but they aren't a one-to-one match.  
aside | complementary | Content outside of the main content of the document.  
footer | contentinfo | Information about the document, like copyright.  
  
Importantly, none of these define any sort of visual style whatsoever-they are purely semantic.

### Putting it all together

HTML5 allows ARIA roles to be declared using the role attribute. Let's go into "HTML mode" and see how this is done:
    
    
    <!DOCTYPE html>
    <html>
    <head>
      <title>Accessibility is Easy!</title>
    </head>
    <body>
    
    <header role="banner">
      <img src="a_cool_logo.png" alt="Always provide alt text for accessibility ;-)" />
    </header>
    
    <nav role="navigation">
      <a href="">This could be a link for getting around the site.</a>
    </nav>
    
    <section role="main">
      <h1>Doesn't this look simple?</h1>
      <p>As you can see, every element on this mock HTML page is semantic--it describes the content it contains.</p>
      <p>Also, all the typical areas of an HTML document are covered--no DIVs necessary!</p>
    </section>
    
    <aside role="complementary">
      <p>This is a sidebar that illustrates how we could declare secondary content.</p>
    </aside>
    
    <footer role="contentinfo">
      <p>copyright 2011, centresource interactive agency</p>
    </footer>
    
    </body>
    </html>

Easy, right? Feel free to use the above as a template for beginning your own HTML5 project. It's valid HTML5 and works in current versions of all major browsers.

### ADDENDUM: Internet Explorer

"But, but!" you cry, "Internet Explorer doesn't recognize HTML5!"

Sadly, it's true. The maverick of the browser world won't render our meaningful HTML5 elements. But the fix is simple. Using Javascript, call the createElement method on each HTML5 element you use.
    
    
    <script type="text/javascript">
    document.createElement('header');
    document.createElement('nav');
    document.createElement('section');
    document.createElement('aside');
    document.createElement('footer');
    </script>

Alternately, you can use a library like [HTML5 Shiv](<http://code.google.com/p/html5shiv/>) or [Modernizr](<http://www.modernizr.com/>), which will take care of it for you.

Have feelings about accessibility? Web 3.0? The rise of the machines? Leave a comment.
