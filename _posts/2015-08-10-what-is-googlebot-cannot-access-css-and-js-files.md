---
layout: post
title: "What is \"Googlebot cannot access CSS and JS files?\""
date: 2015-08-10
---
![Blocked CSS and JS](http://blog.centresource.com/wp-content/uploads/2015/08/blockedcss-300x226.png)I recently received an email from a client that included a message they had received from Google with an ominous warning in the subject line that "Googlebot cannot access CSS and JS files" on the client's website. The body of the email warned us that "Googlebot cannot access your JavaScript and/or CSS files because of restrictions in your robots.txt file." So, just what does that mean, wondered my client.

The message arrives from the Google Search Console ([formerly Google Webmaster Tools](<http://googlewebmastercentral.blogspot.com/2015/05/announcing-google-search-console-new.html>)) and after doing more digging, I found that this is a new push by Google to inform website owners that blocking these important files can hinder Google's ranking of your site.

Ok, cut through the tech jargon. What does this mean? In short, CSS and JS files are files on your server that make sure your website displays as intended, and functions properly. Since these files are basically computer code, it doesn't make a whole lot of sense to the average person, and many web developers put a line in their code (specifically, in a file called robots.txt) that tells search engines to ignore the CSS and JS files, so they don't end up showing up in search results.

Since we're telling search engines to ignore these pages, that means that when Google looks at your website, it scans the homepage, and sees that in order to display the page properly, it needs to also load these JS and CSS files, but then Google sees that it is being told to ignore those files. That leaves Google with an incomplete picture of what your site looks like. It still can read and index the content on your site, which is the most important thing, but Google is now wanting a more complete view of your site, including how things are displayed on the page. In order for that to happen, it needs to be given permission to view those CSS and JS files.

So, if you're ready to unblock these files, or want to see if you currently are:

  1. Make sure you have your [site set up with Google Search Console](<https://support.google.com/webmasters/answer/6001104?hl=en>)
  2. Within Search Console, on the left click on Crawl -> Fetch as Google
  3. Leave the URL space blank to fetch your homepage, and click on Fetch and Render
  4. After the fetch is complete, click on the results to see the rendering. This will show you how Google sees your page vs. how a visitor to your site sees it. Below the rendering, you'll see a list of any blocked items.
  5. If your CSS and/or JS files are being blocked, you'll need to edit the robots.txt file. (You will probably want to get a developer to do this.) Here's what you'll need to add to your robots.txt file: 
     * User-Agent: Googlebot  
Allow: .js  
Allow: .css



That should solve the issue and now Google will be able to fully render and understand the appearance and structure of your website.

* * *

  * [Marketing](<http://blog.centresource.com/category/marketing/>)



[google](<http://blog.centresource.com/tag/google/>)[SEO](<http://blog.centresource.com/tag/seo/>)[webmaster-tools](<http://blog.centresource.com/tag/webmaster-tools/>)

![](http://1.gravatar.com/avatar/58a8d7bffbe9b1c52860e08219d64d8b?s=120&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D120&r=G)

#### [Shaun Jackson](<http://blog.centresource.com/author/sjackson/> "Posts by Shaun Jackson")

SHAUN is incredibly laid back, exuding a level of calm that does not at all line up with his serious caffeine intake. He loves Nashville's musical and artistic atmosphere, but even more so, loves the weather. Shaun has a surprising level of disdain for snow, considering he hails from the Great White North (born and raised in Ottawa Canada). He went to college in New York and obtained a Bachelors in Marketing, and later received his MBA. Whenever possible, Shaun loves to hit the road on his motorcycle to discover new sites and coffee shops and ride off into the sunset. Or something.




[ ![SEA Summit 14: The Thing No One Is Talking About](http://blog.centresource.com/wp-content/themes/marroco/assets/img/empty/pixel.png) ](<http://blog.centresource.com/2014/04/16/sea-summit-14-the-thing-no-one-is-talking-about/>)

### [SEA Summit 14: The Thing No One Is Talking About](<http://blog.centresource.com/2014/04/16/sea-summit-14-the-thing-no-one-is-talking-about/>)

April 16, 2014 / [Marketing](<http://blog.centresource.com/category/marketing/>)

There have been countless keynote sessions and workshops that have piqued my interest at the ...

[ ![Your Website Performance Reality Check](http://blog.centresource.com/wp-content/themes/marroco/assets/img/empty/pixel.png) ](<http://blog.centresource.com/2015/08/17/your-website-performance-reality-check/>)

### [Your Website Performance Reality Check](<http://blog.centresource.com/2015/08/17/your-website-performance-reality-check/>)

August 17, 2015 / [Marketing](<http://blog.centresource.com/category/marketing/>)

Did you know that Amazon found that for every 100 milliseconds more in page load ...

* * *

# Post navigation

[← Learning Product Management From... Fruit Salad?](<http://blog.centresource.com/2015/08/04/learning-product-management-from-fruit-salad/>)

[Your Website Performance Reality Check →](<http://blog.centresource.com/2015/08/17/your-website-performance-reality-check/>)
