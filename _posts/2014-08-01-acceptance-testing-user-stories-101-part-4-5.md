---
layout: post
title: "Acceptance Testing (User Stories 101: Part 4 of 5)"
date: 2014-08-01
---
[![User stories 101](http://blog.centresource.com/content/uploads/2014/07/user_stories_101-01-300x194.jpg)](<http://blog.centresource.com/content/uploads/2014/07/user_stories_101-01.jpg>)

In [Part 3](<http://blog.centresource.com/2014/07/29/collecting-user-stories/>) of our "User Stories 101" series, we talked about how **user stories are great placeholders for functionality, but are not all the functional requirements we need**. To go deeper on actually conveying need, we should integrate a series of acceptance tests to confirm that a story is satisfied.

Or, put another way: how do we know when a user story is done?

**A few ground rules** :

  * It's better to write a short story and a longer list of metrics to test.
  * These tests should be written before coding.
  * These tests should not be written by the actual developers.
  * These tests should comprise the QA script for the customer team after coding.



### Writing Acceptance Tests

**Acceptance tests are detailed lists of requirements that accompany a story.** They should be actionable and task oriented, centered around the following thoughts:

  * What does the team need to know about the story?
  * What can go wrong during the story?
  * What am I assuming about how the story will be implemented?



It's a good idea to use a consistent tone and syntax here, too. Our team follows the "Verify That..." approach. The first line of your acceptance tests should begin with that phrase, and what follows can be a simple list of to-do's, essentially. **This allows the developer as well as the QA team to ensure the requirement is met.**

### Behavior Modeling

Another way of explaining detailed functionality is via a **behavior model**. This layout gives another consistently phrased approach to how we handle individual requirements. The syntax is:

_> Given that I am << on a page >> and I have << performed an action >>, I should << see this reaction >>._

This model is also great for QA and bug submissions. Simply add, "Instead, I expect << desired functionality >>." to the end of that line and you've got a really detailed error report that can be submitted to a developer.

I often write these tests on the back of the user story notecard. Again, this limits the amount of detail I can add to a particular card and instead implies that I should break complex stories down into multiple cards or entities

**So now we've got a big pile of well-written, thought-out user stories, and they even have acceptance criteria. Hooray, acceptance testing!**

**Next up, in the final part of our "User Stories 101" series, we'll answer the question: how do we know where to start?**

_Editor's Note: This series was originally drafted by Jon Arnold, but was not published until after he left Centresource for his next adventure as Product Manager at Taonii. You can find Jon on Twitter[@jonarnold](<http://twitter.com/jonarnold>). _

* * *

  * [Development](<http://blog.centresource.com/category/development/>)



[Development](<http://blog.centresource.com/tag/development/>)

![](http://0.gravatar.com/avatar/2152101bbbd6554dcb5b80894835408f?s=120&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D120&r=G)

#### [staff](<http://blog.centresource.com/author/staff/> "Posts by staff")




[ ![Import Drupal Content in Rails \(The Quick and Dirty Way\)](http://blog.centresource.com/content/themes/marroco/assets/img/empty/pixel.png) ](<http://blog.centresource.com/2014/05/09/import-drupal-content-in-rails-the-quick-and-dirty-way/>)

### [Import Drupal Content in Rails (The Quick and Dirty Way)](<http://blog.centresource.com/2014/05/09/import-drupal-content-in-rails-the-quick-and-dirty-way/>)

May 9, 2014 / [Development](<http://blog.centresource.com/category/development/>)

Here in the bucolic surroundings of Centresource, we have many tools at our disposal. We ...

[ ![How the Rules of Improv Made Me a Better Consultant](http://blog.centresource.com/content/themes/marroco/assets/img/empty/pixel.png) ](<http://blog.centresource.com/2014/10/23/rules-improv-made-better-consultant/>)

### [How the Rules of Improv Made Me a Better Consultant](<http://blog.centresource.com/2014/10/23/rules-improv-made-better-consultant/>)

October 23, 2014 / [Development](<http://blog.centresource.com/category/development/>)

It may sound unrelated, but the four basic tenets of improv have influenced how I ...

* * *

# Post navigation

[← Collecting User Stories (User Stories 101: Part 3 of 5)](<http://blog.centresource.com/2014/07/29/collecting-user-stories-user-stories-101-part-3-5/>)

[Prioritizing User Stories (User Stories 101: Part 5 of 5) →](<http://blog.centresource.com/2014/08/05/prioritizing-user-stories-user-stories-101-part-5-5/>)
