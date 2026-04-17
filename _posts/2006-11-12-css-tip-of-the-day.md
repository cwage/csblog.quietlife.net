---
layout: post
title: "CSS Cross-Browser Tricks"
date: 2006-11-12
---
Anyone that has written HTML and CSS has undoubtedly, at one time or another, faced a major headache attempting to acheive crossbrowser display uniformity. It's a problem that's not going to go away anytime soon, so we all just have to live with it for the time being.

I've noticed over the years, that everyone has a different approach to tackling this issue. Some prefer to use multiple stylesheets, one always for IE, the other for everyone else. Some code one stylesheet, but forsake uniformity for subtle, sometimes unnoticable, differences. I myself have used both of these techniques in the past. Not that there is anything wrong with either method; the end goal is to have a webpage that looks roughly the same in all the major browsers (IE 5-6, Firefox, Opera, Safari), and most importantly, without using tables for layout.

Recently, I discovered a technique that takes a little bit off the edge of that crossbrowser headache. It allows you to use a single stylesheet for the two big browsers (IE, Firefox), and not have to resort to 'hacks' to get IE to cooperate. I've noticed that the standard is starting to lean towards a 'design in Firefox - tweak for IE' mentality. This technique allows us to handle both browsers at the same time, without having to go back later and run in to the inevitable issues that crop up.

Enough talk. Let's see some code.

We'll start with an HTML snippet:
    
    
    <div id="green">What color is this?</div>

Simple enough. Now, let's style it so that our text is actually green on the page.
    
    
    #green { color: #00ff00; }

Ok. Now, if we viewed this in any browser, the text 'What color is this?' will be green. But what if we wanted the text to be blue in Internet Explorer, but stay green in Firefox? Hmm...do we use two stylesheets? Not anymore. Check this CSS out:
    
    
    #green { color: #0000ff; } /* make it blue for internet explorer */
    
    
    body>#green { color: #00ff00; }  /* make it green for firefox */

What's happening here? Well, when Internet Explorer is parsing through this stylesheet, it comes to the first #green tag. Nothing out of the ordinary here, so it parses it just fine. Then it comes to the next tag, body>#green. Internet Explorer 6 and below does not recognize the '>' selector (which is referred to as the child selector), so it doesn't parse it. But Firefox and Opera support the child selector, so following the rules of cascading, Firefox would render the tag correctly, while IE only renders the first tag. Cool, huh?

Of course, my example is trivial. This really comes in handy when dealing with positioning issues such as the differences between how IE and Firefox handle the box model, padding, margins, and floats.

There are some rules to follow when using this technique:

1- The IE element should come first in the stylesheet (they don't call it cascading stylesheets for nothing!)

2- There should be no white space surrounding the child selector:
    
    
    #container > #green { color: #00ff00; } /* This won't work! */
    
    #container>#green { color: #00ff00; } /* This will! */

3- When using the child selector (>), the element on the left should be the direct parent of the element you wish to effect.

For example, if we had had the following html in our earlier example:
    
    
    <div id="container">
    
    <div id="green">What color is this?</div>
    
    
    </div>

We would have wanted our stylesheet to look like this:
    
    
    #green { color: #0000ff; }  /* blue for IE */
    #container>#green { color: #00ff00; } /* #container is the direct parent of #green */

That's it. No other rules needed. I find that this technique really saves me time now when it comes to doing css layout. I can handle positioning an element in both browsers at the same time, instead of coming back to it later to tweak.Of note: IE7 now supports the use of child selectors. So, when your coding your css, keep in mind that IE6 and below won't understand the selector, but IE7 will. Also, IE7 won't support the old "star hack" that many a css designer have used in the past to hide styles from IE.

For more information on crossbrowser CSS, as well as the discussed techniques and 'star hack' visit these links:

<http://www.quirksmode.org/css/contents.html>

<http://www.webcredible.co.uk/user-friendly-resources/css/internet-explorer-7.shtml>
