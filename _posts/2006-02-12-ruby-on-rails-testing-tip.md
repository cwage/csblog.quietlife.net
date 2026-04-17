---
layout: post
title: "Ruby on Rails Testing Tip"
date: 2006-02-12
author: Chris
categories: [Development, Web design]
---
I have been teaching myself a bit of [Ruby on Rails](<https://web.archive.org/web/20060118112641/http://www.rubyonrails.org/>) lately (a lot more on this to come around here, I am sure).

I was going through the section in the [Agile Web Development with Rails](<https://web.archive.org/web/20060315103940/http://www.pragmaticprogrammer.com/titles/rails/index.html>) book, and ran into a problem. The book says quite clearly:

> Here's the bottom line: even if a test method updates the test database, the database is put back to its default state before the next test method is run. This is important because we don t want tests to become dependent on the results of previous tests. 

Yet nonetheless, when I had test methods that destroyed the object, or modified it in some way, subsequent test assertions were failing because they were still seeing the changed data. Luckily, some googling paid off, and I found [the answer](<https://web.archive.org/web/20070104013043/http://wrath.rubyonrails.org/pipermail/rails/2005-December/005802.html>). It turns out that Rails 1.0 [introduced](<http://www.clarkware.com/cgi/blosxom/2005/10/24#Rails10FastTesting>) some spiffy new stuff for testing, including using transactional fixtures by default. This means that it uses database transactions to rollback changes it makes prior to each subsequent test method. The tables I was using were MySQL MyISAM tables, which don't support transactions.

I merely changed the table types in my test database to use InnoDB with _"alter table products type=InnoDB"_ , though alternatively, you can also simply modify your test class with the following line:

> self.use_transactional_fixtures = false
