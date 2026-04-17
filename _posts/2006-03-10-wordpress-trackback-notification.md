---
layout: post
title: "Wordpress Trackback Notification"
date: 2006-03-10
author: Chris
---
Last month, I [posted](<https://csblog.quietlife.net/2006/02/01/eliminating-most-trackback-spam/>) about the methods we use to block comment and trackback spam. As I noted then, we hadn't had one single successful comment/trackback spam then, or since. However there was still one tremendous annoyance. Dan Sandler's [trackback validator](<https://web.archive.org/web/20060209033008/http://idli.cs.rice.edu/~dsandler/trackback/trackback-validator-plugin/>) plugin effectively eliminates the trackback spam, however Wordpress was still stubbornly e-mailing me about every single one.

My personal blog is currently getting slammed by a botnet of around 270+ computers so far, continually spamming it all day long, so you can imagine how this was quite an annoyance.

Finally, I've figured out why: in wp-trackback.php, there's this bit of code:

> wp_new_comment($commentdata);
> 
> do_action('trackback_post', $wpdb->insert_id); 

The "trackback_post" action is where the trackback validator has the chance to do its magic -- including dying entirely on failure to validate (something which I may have hacked into the plugin myself, come to think of it). But note that before that, it goes ahead and calls wp_new_comment() regardless of the result of the "trackback_post" action. This is why I was getting the e-mail notification even though the trackbacks were not successfully posted.

A simple solution appears to be to simply reverse the order:

> do_action('trackback_post', $wpdb->insert_id);  
>  wp_new_comment($commentdata); 

There doesn't **appear** to be any adverse effects from doing this. The trackback/comment action hooks could use a little consolidation/cleanup. They seem to share functionality in places they shouldn't and differ in places where they ought to be the same.

In any event, I am no longer getting any e-mail about these, and am finally, truly, enjoying a spam-free existence. (Okay, I'd be lying if I said seeing the POSTs fly by in the access log didn't still bother me, but until we cure The Botnet Problem, this is not going away).
