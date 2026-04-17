---
layout: post
title: "Doctrine vs. Propel in symfony..."
date: 2007-04-10
author: Jonathan
---
When we first moved to [symfony](<https://web.archive.org/web/20070406180100/http://www.symfony-project.com/>), my only major concern was [Propel](<https://web.archive.org/web/20080905220453/http://propel.phpdb.org/>). I was pushing to move to Rails, but we gave symfony a shot and ended up absolutely loving it. The two best features of symfony are the plugin architecture and how configurable it is. The only thing we could not live with was Propel. It could not provide the functionality+performance we needed out of our database. Some of the common features like calculated columns, aggregate functions with grouping, etc. are not supported in Propel. Although, a [enhancement ticket](<https://web.archive.org/web/20070418114354/http://propel.phpdb.org/trac/ticket/57>) exists in trac for Propel 2.0.

But we didn't give up on symfony yet, the plugin architecture and Doctrine came together to solve our problems. Since my issues with Propel I have switched to the [Doctrine ORM](<https://web.archive.org/web/20071012100356/http://www.phpdoctrine.org/>) that is implemented by the [sfDoctrinePlugin](<https://web.archive.org/web/20080516144655/http://www.symfony-project.com/trac/wiki/sfDoctrinePlugin>). Supposedly, Doctrine is to be the main ORM for symfony in version 1.1, so do yourself a favor and get a head start by switching to Doctrine now.
