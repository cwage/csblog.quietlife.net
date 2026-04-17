---
layout: post
title: "Setting up a client site on Heroku"
date: 2011-09-23
author: Daniel Nelson
categories: [Rails, Ruby, Web Development]
---
_Thanks to[Josh Crews](<http://www.joshcrews.com/>) for  
cluing me in on how to set up staging on Heroku last February_

First, add heroku to the development group in the Gemfile and bundle install.

If this is a client site, you will want the client to own the  
application, so we'll sign in as the client from the beginning (you  
can also use "heroku sharing:transfer" to move an app to another user  
later):

`  
$ heroku auth:logout (only if you are already using heroku)  
$ heroku auth:login  
Enter your Heroku credentials.  
Email: client.email@address.com  
Password: client-password  
`

Then create the production and staging apps:

`  
$ heroku create --stack bamboo-mri-1.9.2 mysitename  
$ heroku create --stack bamboo-mri-1.9.2 mysitename-staging  
`

Then add yourself and anyone else on your team to the heroku apps:

`  
$ heroku sharing:add your.email@address.com --app mysitename  
$ heroku sharing:add your.email@address.com --app mysitename-staging  
$ heroku sharing:add team.member@address.com --app mysitename  
$ heroku sharing:add team.member@address.com --app mysitename-staging  
`

Now you can sign out as the client and sign back into your own Heroku account:

`  
$ heroku auth:logout  
$ heroku auth:login  
Enter your Heroku credentials.  
Email: your.email@address.com  
Password: your-password  
`

Next, we need to update project_root/.git/config so that we can deploy  
to the production and staging apps. Do this by copying the "heroku"  
block to a new "staging" block and updating the url to the name of the  
staging app. While you are at it, you might want to change "heroku" to  
"production" so that it is consistent with "staging":

`  
[remote "production"]  
url = git@heroku.com:mysitename.git  
fetch = +refs/heads/*:refs/remotes/heroku/*  
[remote "staging"]  
url = git@heroku.com:mysitename-staging.git  
fetch = +refs/heads/*:refs/remotes/heroku/*  
`

Now, you can push to staging and production separately:

`  
$ git push staging master  
$ git push production master  
`

And to push a branch other than master (such as develop) to staging  
for a beta reveal:

`  
$ git push staging develop:master  
`

Note that for any Heroku commands, you will need to specify the app:

`  
$ heroku rake db:migrate --app mysitename-staging  
`
