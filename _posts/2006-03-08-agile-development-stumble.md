---
layout: post
title: "Agile Development Stumble"
date: 2006-03-08
author: Chris
---
I am going through the [Agile Web Development with Rails](<http://pragmaticprogrammer.com/titles/rails/index.html>) book, and in their tutorial, there's a slight stumbling block I ran into. I figure if anyone else has this problem and is anything like me, they'll google for it, so maybe this will help someone out there. A description of the issue and solution follows:

On page 145, it takes you through building some test cases for the shopping cart in the "depot" app we're learning with.

In "products.yml", the book has you create a few example records, for example:

> version_control_book:  
>  id: 1  
>  title: Pragmatic Version Control  
>  description: How to use version control  
>  image_url: http://.../sk_svn_small.jpg  
>  price: 29.95  
>  date_available: 2005-01-26 00:00:00 

The book then refers to this object as @version_control_book. This wasn't working for me, however. I kept getting errors like this using the same examples they had:

> 1) Error:  
>  test_add_unique_products(CartTest):  
>  NoMethodError: You have a nil object when you didn't expect it!  
>  The error occured while evaluating nil.price  
>  /var/www/cwage/rails/depot/config/../app/models/line_item.rb:9:in `for_product'  
>  /var/www/cwage/rails/depot/config/../app/models/cart.rb:15:in `add_product'  
>  cart_test.rb:11:in `test_add_unique_products' 

After scratching my head for a while, I discovered it's because in "test_helper.rb", "self.use_instantiated_fixtures" was set to false. In order for the test methods to instantiate the objects by name from the YML files, this needs to be set to true. The book seems to be operating on the assumption that it's set to true by default, but in the version of rails I was using, it wasn't.

So, after setting "self.use_instantiated_fixtures = true" in test_helper.rb, I was good to go.
