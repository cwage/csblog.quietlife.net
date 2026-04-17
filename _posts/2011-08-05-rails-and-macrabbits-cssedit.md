---
layout: post
title: "Rails and MacRabbit's CSSEdit"
date: 2011-08-05
author: Jeremy Holland
categories: [Miscellaneous, Productivity, Rails, Ruby, Software, Web Design, Web Development]
---
Just a real quick tip for other Rails developers out there who enjoy the benefits of MacRabbit's excellent software [CSSEdit](<http://macrabbit.com/cssedit/>). Due to the fact that Rails applies a timestamp to every asset (stylesheet, javascript, and/or image) included in a view via the appropriate helper in order to allow the user to use the Expires header with said asset (full explanation [here](<http://api.rubyonrails.org/classes/ActionView/Helpers/AssetTagHelper.html>)), and because CSSEdit overrides stylesheets based on the full URL _including the query string_ , attempting to use the CSSEdit override functionality with a default Rails installation is nigh-impossible. Here's how to get around it:

In your development environment file at /config/environments/development.rb, place the following command in the <Your App>::Application.configure block
    
    
    ENV["RAILS_ASSET_ID"] = ''

Voilá! Timestamps gone in development.
