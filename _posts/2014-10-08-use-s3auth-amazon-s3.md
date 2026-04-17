---
layout: post
title: "How To Use S3Auth With Amazon S3"
date: 2014-10-08
---
Here at Centresource, we create new projects for clients all the time. There is a lot of information to keep organized and up-to-date. We have tried a lot of solutions in the past, but much of the information becomes scattered across [Trello](<http://trello.com/>), [Redmine](<http://redmine.org/>), [Invision](<http://invisionapp.com/>), [Google Drive](<http://drive.google.com/>) and [Dropbox](<http://dropbox.com/>). With filenames like `ClientA-Wireframes-Interior1-Rev3A.format`, your storage becomes cluttered and difficult to interpret. Additionally, it is difficult to share this information with the client in a presentable format if they don't have our same proprietary applications like [Pages](<https://www.apple.com/mac/pages/>), [Keynote](<https://www.apple.com/mac/keynote/>), [Omnigraffle](<https://www.omnigroup.com/omnigraffle>) or [Photoshop](<http://www.photoshop.com/>).

![s3auth_logo](/content/uploads/2014/08/s3auth_logo-300x52.png)

This is why we've decided on a web-based solution that is viewable to anybody with a browser that just uses basic HTML/CSS/JS. More specifically, we've decided to us [Jekyll](<http://jekyllrb.com/>) that is deployed to an S3 bucket. In order to keep this site/bucket secure we are leveraging [S3Auth](<http://s3auth.com/>) to put HTTP Basic Authentication in front of our client's S3 bucket. I'll show you how we do that.

Here's example project information that I'll be referencing throughout this tutorial.

View the code on [Gist](<https://gist.github.com/3f545432ebfb69af9f6a>).

Here are the instructions I followed to get s3auth.com to work with my s3 bucket.

  1. Create a basic Jekyll website. Feel free to use our own tool, [generator-playbook](<https://github.com/centresource/generator-playbook>). Go ahead and deploy your site to S3 to make sure all that works. Make sure gzip is turned off. s3auth does not support gzipped assets.
  2. Follow the Instructions from S3Auth.com 
     1. Login to your DNS provider and create a CNAME that points to `relay.s3auth.com`.
     2. Create a new Amazon IAM user with the following policy



View the code on [Gist](<https://gist.github.com/1989409704b0838eacd7>).

3\. Register with s3auth.com and submit the form on their site. Here is the information I would provide based on the project info provided earlier:

View the code on [Gist](<https://gist.github.com/449593a0cea532a67a68>).

4\. Generate .htpasswd file in [Apache HTTP Server format](<http://httpd.apache.org/docs/2.2/misc/password_encryptions.html>) using [htpasswd](<http://httpd.apache.org/docs/2.2/programs/htpasswd.html>) tool:

htpasswd -nbs user password

5\. Upload it to the root of your bucket. It is very important to put it in the root. [Currently, S3Auth does not support nested paths](<https://github.com/yegor256/s3auth/issues/203>).

6\. Now when you access your files at goliath.example.com, you should be prompted with an HTTP Basic Auth dialog. Enter the credentials from step 4 with `user` as your username and `password` as your password. You should now have access.

Let me know if you run into any problems with any of these steps. You can let me know in the comments below or DM me on [Twitter](<https://twitter.com/rianrainey>). I'd love to hear your feedback. Does this help or just make your more confused?

* * *

  * [Development](</category/development/>)



![](http://0.gravatar.com/avatar/e950a70038b437c6604caa4826641a60?s=120&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D120&r=G)

#### [Rian Rainey](</author/rrainey/> "Posts by Rian Rainey")




[ ![Acceptance Testing \(User Stories 101: Part 4 of 5\)](/content/themes/marroco/assets/img/empty/pixel.png) ](</2014/08/01/acceptance-testing-user-stories-101-part-4-5/>)

### [Acceptance Testing (User Stories 101: Part 4 of 5)](</2014/08/01/acceptance-testing-user-stories-101-part-4-5/>)

August 1, 2014 / [Development](</category/development/>)

In Part 3 of our "User Stories 101" series, we talked about how user stories are great ...

[ ![5 Reasons To Choose a Digital Agency Over a Unicorn](/content/themes/marroco/assets/img/empty/pixel.png) ](</2014/06/06/5-reasons-choose-digital-agency-unicorn/>)

### [5 Reasons To Choose a Digital Agency Over a Unicorn](</2014/06/06/5-reasons-choose-digital-agency-unicorn/>)

June 6, 2014 / [Development](</category/development/>)

So here's the scenario: you have a product you want to build, but like most people ...

* * *

# Post navigation

[← Welcome to the team, Erick Pennington!](</2014/10/02/welcome-team-erick-pennington/>)

[Do I Really Need a CMS? →](</2014/10/10/really-need-cms/>)
