---
layout: post
title: "PHP Code Generator"
date: 2005-12-27
author: Jackson
categories: [Miscellaneous, Utilities, Productivity, Development, PHP]
---
I just spent some time playing with [PHP Object Generator](<https://web.archive.org/web/20051228051046/http://www.phpobjectgenerator.com/>) and thought I would share my thoughts.

I should mention that I think needing code generation is an indication of poor design. The reason is that in order for code generation to work there has to be enough code that is duplicated that the process of creating the code can be scripted. 

I will take it a step further too and say that if you need code generation it is an indication that the duplicated code it too complicated as well.

The developer then has to maintain the generated code, which is full of duplication and complexity.

As for PHP Object Generator specifically, I think it does a very poor job of creating database classes. Right off the bat I notice that it is lacking error checking and reporting. (It does check for Exceptions in the PHP 5 code, but it is incredibly ungraceful)

It also does not handle null values gracefully.

It lacks the ability to handle multi-part keys.

There is nothing for relational data.

It asks for data types, and then does not use them. There is nothing for date columns. This is particularly a problem for timestamp columns that should update to NOW() on every update. With the classes that PHP Object Generator creates the timestamp columns must be explicitly set on every update by the developer.

Then there is the problem of getting data based on multiple fields that are not primary keys. A good example might be finding blog articles by author and date. I don't see a way to accomplish that.

I guess my thoughts can be summed to say that I think it is "clever", but not really useful.
