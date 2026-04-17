---
layout: post
title: "Open Source Groupware & Project Management"
date: 2005-12-11
categories: [Operations, PHP]
---
For the past week, we have been searching for a new web-based platform that can help consolidate our various back-end applications. We currently use [SugarCRM](<https://web.archive.org/web/20080828023214/http://www.sugarcrm.com/>) for Contact & Sales Management, [phpCollab](<https://web.archive.org/web/20041212030532/http://www.php-collab.org/>) for Project Management, Media Wiki for Documentation & Knowledgebase, and have weakly attempted to use Mantis for Bug Tracking. We also utilize [DekkoTime](<https://web.archive.org/web/20051220142927/http://www.dekkotime.com/>) for Time Tracking, phpLive for online Chat, and IMAP email. Needless to say, we have a real need for consolidation :)

Our main goal was to find a system that combined Groupware & Project Management - something that allows the team to not only manage their project work loads, but also non-project related tasks & events. What made our situation unique is our need for external parties to have access (moderated) to our systems. phpCollab is great because we can communicate effectively with our clients while working on their projects. This little feature proved to be the undoing of most of our viable candidates.

We also really wanted our new platform to have a Trouble Ticket system & a Knowledge Base. Various platforms had one or the other, but rarely had both. All in all, we simply couldn't find a system that met our requirements... Every single one was deficient in some way. This made it increasingly difficult to choose since every path was a trade-off.

Here are some of the platforms that made it to the final round (they are all worthy applications):

[http://www.sugarcrm.com](<https://web.archive.org/web/20080828023214/http://www.sugarcrm.com/>) \- The new version has some definite improvements, especially the newly added project mgmt section. Unfortuantely, it doesn't allow for 'users' to view items in the projects.

[http://www.dotproject.org](<https://web.archive.org/web/20051211015623/http://www.dotproject.org/>) \- Inadequate Permission structure for working with external clients. Clients can see everything if given access. Also doesn't handle the CRM piece.

http://www.open-project.org - No CRM features and their demo didn't allow for ADMIN testing. The overall system is very 'clunky' and didn't instill great confidence (although, it did make it to the final round!)

[http://www.moregroupware.org](<https://web.archive.org/web/20040726040816/http://www.moregroupware.org/>) \- This appeared to be a viable candidate until we saw that their permission structure didn't allow clients to see specific projects. All or nothing.

[http://www.opengroupware.org](<https://web.archive.org/web/20051211144410/http://www.opengroupware.org/>) \- Looks to be a great product, but I couldn't test because they do not provide an online demo. Such a shame.

[http://www.egroupware.org](<http://www.egroupware.org/>) \- We had previous experience with eGroupware, but their overly-complicated Project Mgmt module made us avoid them. We were lucky to check on them again - the new project manager is great! Overall, this application is far superior to anything we tested!

At this point, it appears that eGroupware is the clear winner. We are going to proceed with full testing and will migrate to the platform if all things go well. This jewel is web-based, has project mgmt, groupware, trouble tickets, and one of the best Knowledge Base apps I've seen.

Stay tuned for how things progress!
