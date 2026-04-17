---
layout: post
title: "Simulating the ENUM MySQL Column Type in Rails"
date: 2011-06-22
author: Jeremy Holland
categories: [Rails, Ruby, Web Development]
---
Today I was speccing out a handful of models that had "enumerable" attributes - i.e. attributes that are stored as strings, but whose possible values are limited to being a single element of a finite set of predefined strings.

Think something along the lines of, say, the attribute "color": valid values for "color" might include "red", "blue", or "chartreuse"; while it's certainly a large set, it's still finite in the sense that there are not an infinite number of values that would satisfy the condition of being a color, and in that the valid values have no common regularity - i.e. the validity of any string cannot be determined by a regular expression match as said validity is determined purely by semantics, with no discernable extrusion into syntactical space (at least in English and most other germanic and romance languages).

Now, MySQL handily supplies a column type specifically for this purpose: ENUM. When defining an ENUM column in MySQL, one must define along with it a list of its possible values. In the event that one attempts to store a value not in this list in the column in question, the database throws an error, thus handily preventing invalid values from entering the dataset and corrupting the state of the database.

However, when using a database abstraction layer in order to maintain database portability, we unfortunately lose this capability as it is more or less unique to MySQL in the base column-type implementation. PostGRESQL has the ability to create new column types which are predefined as ENUM (via a wholly different paradigm), but both Oracle and SQL Server lack the capability completely.

Given the above, it has been the habit of Rails developers to enforce ENUM-style behavior at the application level via (at least) a call to validates_inclusion_of, and often an overriding of the attribute accessor methods to allow the assignment and retrieval of the values as ruby symbols while still actually persisting them to the database as strings. An example follows:
    
    
    class Paint < ActiveRecord::Base
      validates_presence_of :color, :in => [:red, :blue, :chartreuse]
    
      def color
        read_attribute(:color).to_sym
      end
    
      def color=(value)
        write_attribute(:color,value.to_s)
      end
    end
    

Now, while this is a relatively small quantity of code, it has been my personal experience that the need for an application-enforced ENUM pops up often enough that it becomes somewhat tedious to repeat this pattern over and over and again for different attributes. As such, we at Centresource have just released the enum_simulator plugin for Rails 3+, available under the MIT license at [our github repo](<http://github.com/centresource/enum_simulator>). It isn't much, but once installed, the code above can be condensed to:
    
    
    class Paint < ActiveRecord::Base
      enum :color, [:red, :blue, :chartreuse]
    end
    

The validates_inclusion_of and symbol<->string typecasting are defined by the plugin, so we can shorten everything down to one call to the class method enum, wherein the first argument is the attribute in question, and the second is an array of possible values. Install and enjoy!
