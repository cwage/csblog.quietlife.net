---
layout: post
title: "mysql FULLTEXT search length"
date: 2005-06-09
author: Chris
---
I discovered something interesting today. We couldn't figure out why our internal documentation wiki (which uses [mediawiki](<http://wikipedia.sourceforge.net/>)) seemed to search so poorly. i.e., if you searched for "ftp", you got no results, even though there were tons of entries with "FTP" in them.

I suspected it had to do with length limitations, and I was right -- but it has nothing to do with mediawiki. It's MySQL's FULLTEXT searching, which is limited to 4+ characters minimum by default. Luckily, it's customizable. In our case, I simply added this line to /etc/mysql/my.cnf in the [mysqld] section:

> ft_min_word_len=3 

You then have to rebuild the indexes on the tables being FULLTEXT searched. In mediawiki's case, this required:

> mysql> repair table searchindex quick; 

Voila! Now searches for "FTP" actually returned useful results. Happy searching!
