---
layout: post
title: "Subqueries in MySQL 4.1+"
date: 2006-02-01
author: Chip
categories: [Development, PHP, Web design]
---
Today I came across a problem where I needed to find all of the threads in a forum, along with the first post and last post information. The easy (but inefficient) way is to find all of the initial posts, and then based on that result set, find all of the replies for each post.

`SELECT post.*, user.nickname  
FROM post, user  
WHERE post.parent_post_id = 0  
AND post.user_id = user.user_id  
AND post.forum_id = $forum_id  
GROUP BY post.post_id  
`

This will return all of the initial post info, as well as the nickname of the user who posted it. Now, with that result set, we do another query to find the replies to each post ($parent_post_id):

`SELECT post.*, user.nickname,  
count(post.post_id) AS num_replies  
FROM post, user  
WHERE post.parent_post_id = $parent_post_id  
AND post.user_id = user.user_id  
GROUP BY post.post_id  
ORDER BY post.created_on  
`

Now while this is the most logical way to do it, it can grow to be completely inefficient. For each row returned from the initial query, at least one more query most be performed -- that can grow really big really fast.

The better way? Subqueries, introduced by MySQL in version 4.1. Subqueries allow you to call select statements within another select statement. 

`SELECT * FROM t1 WHERE column1 = (SELECT column1 FROM t2);`

From the [MySQL Manual](<https://web.archive.org/web/20060203064706/http://dev.mysql.com/doc/refman/4.1/en/subqueries.html>):

> The main advantages of subqueries are:
> 
>   * They allow queries that are structured so that it is possible to isolate each part of a statement.
>   * They provide alternative ways to perform operations that would otherwise require complex joins and unions.
>   * They are, in many people's opinion, readable. Indeed, it was the innovation of subqueries that gave people the original idea of calling the early SQL "Structured Query Language."
> 


So how can the earlier problem be solved with subqueries? Keep in mind that the information needed from this query is: the subject for the post, the number of replies, the first post date and user, and the last post date and user.

`SELECT first_post.*, first_post_user.nickname,  
count(allposts.post_id) AS num_replies,  
last_post.post_id as last_post_id,  
last_post.created_on as last_post_date,  
last_post_user.nickname as last_post_user  
FROM post first_post,  
user first_post_user,  
post allposts,  
post last_post,  
user last_post_user  
WHERE last_post.post_id = (SELECT post.post_id  
FROM post  
WHERE post.forum_id = '$forumVO->forum_id'  
AND post.parent_post_id = first_post.post_id  
ORDER BY created_on DESC LIMIT 1)  
AND last_post.user_id = last_post_user.user_id  
AND first_post.user_id = user.user_id  
AND first_post.parent_post_id = 0  
AND first_post.forum_id = '$forumVO->forum_id'  
AND allposts.parent_post_id = p1.post_id  
GROUP BY first_post.post_id  
`

That's it! All of the necessary information in one easy MySQL query. One thing to note is that you can reference a table & column that's outside of the subquery which is necessary in a case like this (" _AND post.parent_post_id = first_post.post_id_ "). This creates a correlation between the main query and the subquery that is similar to doing two separate queries.

There's a lot more to subqueries that I look forward to learning about -- instead of setting a column equal to a subquery (like I did in this example), you can set a column to be **IN** a subquery, or **ALL** of the results of a subquery, etc.

Check out the [MySQL manual](<https://web.archive.org/web/20060203064706/http://dev.mysql.com/doc/refman/4.1/en/subqueries.html>) on everything you can do, and share your success stories below!
