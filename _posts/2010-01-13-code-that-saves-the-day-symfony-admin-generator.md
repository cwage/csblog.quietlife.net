---
layout: post
title: "Code That Saves The Day: Symfony Admin Generator"
date: 2010-01-13
author: Brent Shaffer
categories: [PHP, Symfony, Web Development]
---
Every day at CentreSource brings with it a new challenge. With every challenge comes the opportunity to try a unique approach. We all know sailing the interweb can be stormy at best. But if you keep your eyes open, you will find code that can be a lighthouse to your sinking ship. Today's Code that Saves the Day™:**The Symfony Admin Generator!**

For those who don't know, [Symfony](<https://web.archive.org/web/20100112184910/http://www.symfony-project.org/>) is an MVC web framework built on PHP. Symfony is a great tool to use for custom development, and is very similar to the als0-opensource MVC framework Ruby on Rails. The [Symfony Admin Generator](<https://web.archive.org/web/20100115222158/http://www.symfony-project.org/screencast/admin-generator>) is a tool connected to a command-line task that allows you to easily spin up editable interfaces for your website's administrators. Do you have a table for contacts in your database? Type a single command into your terminal...

> `$: php symfony doctrine:generate-admin backend Contacts`

...and presto! Your users can filter, sort, view, edit, and create new contacts! Yes, it really is that simple. There are a variety of customizations available (some of which could use healthier documentation, which extends beyond the scope of this post), and you can read about those [here](<https://web.archive.org/web/20100112231844/http://www.symfony-project.org/book/1_2/14-Generators>).

### Problem: Client demands additional functionality for administrative purposes.

_example:_ "We want to easily export data from the tables in our database. We want to customize exported fields per export, change column labels, and make other fields unable to be exported".

### Mediocre Solution: Override the generated admin module with code to export.

_explanation:_ While not a terrible alternative, this is certainly not the best one. The admin generator places most of the generated code in cache, so a good way to customize it is to override the generated files. This is great for small customizations, but _not optimal for potentially reusable code!_ Allowing for any table in your application to be exported is a pretty tempting solution, yes? Think about it. What if you could do this?

> `$: php symfony doctrine:generate-admin backend Contacts --theme=export`

And have a fully generated export interface at your disposal? Pretty slick, I'd say. Which brings us to the:

### Better Solution: Customize the admin generator itself (as opposed to the generated code).

That's right! We get to write code that writes code! Nervous? Scared? Envisioning tiny software bugs slowly infecting every part of your application? Don't be! It's easy. Now I know you're salivating. 

The admin generator is contained in Symfony core. I used the doctrine version, because we're pulling directly from the database. In the `sfDoctrinePlugin`, copy the files in `data/generator/sfDoctrineModule/admin` into your own data directory (I used the path `[data/generator/sfDoctrineModule/export](<https://csblog.quietlife.net/wp-content/uploads/2010/01/Screen-shot-2010-01-11-at-9.35.40-AM.png> "The proper path for your custom admin generator theme in your Symfony project")` in my project's root directory. The directory after `sfDoctrineModule` is the name of your theme). There are three directories: parts, skeleton, and templates. _Skeleton_ is what gets generated outside of cache into the project itself. _Template_ is what is generated INTO cache. _Parts_ contains all your files you do NOT want to copy over into cache or the project, but you need for organizational purposes.

I chose to override the `sfModelGeneratorConfiguration` class to give myself more flexibility when customizing. The `sfModelGeneratorConfiguration` class parses the `generator.yml` file, which is what allows the developers to tweak the generated code to their specifications without having to copy over/write new code. In my admin generator, a user can[ customize their export fields](<https://csblog.quietlife.net/wp-content/uploads/2010/01/Screen-shot-2010-01-11-at-9.46.08-AM.png> "generator.yml configuration for export admin generator") via the generator.yml file.

We now have a flexible admin generator on demand that not only exports the fields of a database table, but allows our user to customize which fields are appropriate to show to the end user. On top of this, the system allows the user to declare fields to export that _don't even exist on the object!_ Lets say we want to have a field exported called "timespan", which symbolizes the duration the user has been in the system. This is going to be a calculation of the current date minus the date the user was added to the system. All we need to do is add "timespan" to the _fields_ option in `generator.yml`, and add a method to our Contact model called `getTimespan()` that returns the appropriate string. If you still haven't salivated, then maybe this will help: The export interface feeds off the sorting/filtering applied by the user in the main view, _and_ allows the users to rename columns and deselect unwanted columns appropriately for their export.

We now have an out-of-the-box exporting solution for the following deliverables for our end-user:

  * Filtering for Export result set
  * Sorting for Export result set
  * Exported column naming
  * Exported column selection



And the following deliverables for our developers:

  * Customization of available fields for exporting
  * Customizing of filters/sorting capability (pulls from existing admin-generator functionality)
  * Addition of non-real export fields
  * Easy extension of the admin generator 
  * _all of this functionality is object-oriented, normalized, and easily overridden or extended._
  * Extended admin generator functionality  
_The export admin generator adds several helpful methods such as` hasExport` and `isFiltered` to the classic admin generator. It also adds a flash message "Your results are currently filtered, click HERE to unfilter them" to any list view._



You can find all of this code [here](<https://web.archive.org/web/20100129114446/http://github.com/bshaffer/Symfony-Snippets/tree/master/AdminGeneratorExport>). Now go forth, and [EXTEND THY ADMIN GENERATOR](<https://web.archive.org/web/20100106112701/http://www.strangebuzz.com/index.php/2008/04/03/31-symfony-10-tutorial-extending-the-admin-generator>)!!
