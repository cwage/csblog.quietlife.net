---
layout: post
title: "New Features in Rails 3"
date: 2010-06-21
author: Travis Roberts
categories: [Web Development]
---
Here at centresource, we're all about following the newest technology in web development. Rails 3 is coming soon, and it promises to be a significant upgrade. With the 4th beta version pushed recently, and a release candidate right around the corner, I thought now would be a good time to go over my two favorite new features.

### All New Router

The router has been completely re-written and borrows heavily from the Merb router, but has a more developed DSL.

**Regular Routes**

Regular routes are more concise, but I'm not sure how I feel about the "controller#action" syntax yet...

**Named Routes**

Very similar to regular routes, just with an extra `:as` variable at the end.

**Restful Routes**

I think restful routes get the biggest improvement. The new syntax is MUCH easier to read than in Rails 2.

### ActiveRecord and ActiveRelation

This is probably my favorite addition to Rails. The new ActiveRecord syntax is very similar to [Doctrine](<http://www.doctrine-project.org/>) (which we use with symfony). Instead of passing options as a hash to your `find()` method, they've created a bunch of new methods you can chain together. 

The best part is that any of the query methods just return a relation instead of running the sql query. That way, you can chain more query methods on the relation later. The actual query doesn't run until you try to access the object(s) (such as with an iterator). This makes fragment caching a lot easier, because you can keep your query call in your action. Even if the cache is hit, it will only create a relation and not actually query the database. You can also force the query to be run at any time by calling `all()`, `first()`, or `last()` on the relation.

I'm very excited for the final release of Rails 3 and can't wait to actually work on a production project with it.
