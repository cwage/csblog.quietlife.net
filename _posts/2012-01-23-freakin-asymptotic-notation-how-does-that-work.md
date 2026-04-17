---
layout: post
title: "Freakin' asymptotic notation: How does that work?"
date: 2012-01-23
author: Jeremy Holland
categories: [Miscellaneous, Theory, Web Development]
---
OK, I'll be the first to admit it - math is my favorite subject. I know that makes me weird - even among fellow working software engineers - but it's the truth. It's also the truth that while they may be boring to many, knowing even a little bit about the numbers of computer science can help make you a better software engineer. Today, we're going to look at a little piece of applied discrete math - the analysis of algorithms - and how we can empirically describe the performance of one algorithm with respect to another using something called "asymptotic notation". If you already know what this is and how to read the various sub-notations, skip the rest of this post: it's old news. If you do not know what this is, and would like to, read on! If you do not know what this is and don't care, read on anyway - I promise you it'll be worth it.

Now, while I'm totally guilty of bandying around big scary terms like "asymptotic notation" (I'm a notorious stickler for nomenclature), what this boils down to is the following mathematical notation (and its related brothers, which we'll get to later):

![O\(g\(n\)\) ](/wordpress/wp-content/plugins/latex/cache/tex_86170f0037842246df67f90ab032cf23.gif)

Most typically, you'll see this used and referred to not as ![O\(g\(n\)\) ](/wordpress/wp-content/plugins/latex/cache/tex_86170f0037842246df67f90ab032cf23.gif), which doesn't serve much purpose unless we know already what ![g\(n\) ](/wordpress/wp-content/plugins/latex/cache/tex_9a4aa4746e3b82145ff1af2052b1325f.gif) is, but rather in terms of a **specific** ![g\(n\) ](/wordpress/wp-content/plugins/latex/cache/tex_9a4aa4746e3b82145ff1af2052b1325f.gif), say, ![n^2 ](/wordpress/wp-content/plugins/latex/cache/tex_3ac3bd4c4c1f66111feb1ef16babaad6.gif):

![O\(n^2\) ](/wordpress/wp-content/plugins/latex/cache/tex_14fd02f6323f8a36e2bb5abc3af32923.gif)

Moreover, for the purposes of this discussion, we're going to look primarily at the following notation style:

![f\(n\) = O\(n^2\) ](/wordpress/wp-content/plugins/latex/cache/tex_f7dd4a60bc10c04a4c3da54cb9742773.gif)

So what on earth does this mean? Well, let's think about algorithms. What is an algorithm? Simply a series of instructions for performing some task, right? In computing specifically an algorithm is implemented as an actual, written program in your language of choice. But under the hood, mathematically, an algorithm is a **function** (sometimes pure, sometimes not): it takes some input(s) and delivers some output. In the above block o' math, let us equate ![f\(n\) ](/wordpress/wp-content/plugins/latex/cache/tex_996cb805d9bfdfe8d06fed3a6f842841.gif) with some algorithm we would like to implement, say, sorting an array of integers from least to greatest. With an algorithm such as that, you would give it an array of dubiously sorted values, and it would give you back an array containing exactly the same elements but in sorted order. Represented mathematically, we have:

![s\(a\) ](/wordpress/wp-content/plugins/latex/cache/tex_a37aa991945fb7f4c4d9ce2a2485a695.gif)

where ![s ](/wordpress/wp-content/plugins/latex/cache/tex_ff705f1b6f527fe2038d5ad152f64769.gif) is the algorithm function itself, and ![a ](/wordpress/wp-content/plugins/latex/cache/tex_99020cb24bd13238d907c65cc2b57c03.gif) is the array to be sorted. Now, let's keep in mind that there are many different ways of going about sorting an array - naturally, we would like to pick the fastest one for the task at hand. So in order to know anything about the _performance_ of an algorithm, we should probably come up with some way to represent how long it takes to run. To wit:

![T\(s\(a\)\) ](/wordpress/wp-content/plugins/latex/cache/tex_c9e5188fdbbb8ce19aecbcebe72f2bd9.gif)

represents the "time" ![T ](/wordpress/wp-content/plugins/latex/cache/tex_3b85a149146b36ea27855e7e05656385.gif) it takes to run algorithm ![s ](/wordpress/wp-content/plugins/latex/cache/tex_ff705f1b6f527fe2038d5ad152f64769.gif) on input ![a ](/wordpress/wp-content/plugins/latex/cache/tex_99020cb24bd13238d907c65cc2b57c03.gif). OK. So, how can we begin to reason about what the range of this function might be? Actually, perhaps that's jumping the gun - what would really be the _domain_ of this function? What measurement of your general work-a-day sorting algorithm would dictate how long it takes to run? The answer, my friend, is the size of the input: it should make sense to anybody who's actually had to do it that sorting a 10-element array is a heck of a lot faster than sorting a 10,000,000-element array. So, really, our ![T ](/wordpress/wp-content/plugins/latex/cache/tex_3b85a149146b36ea27855e7e05656385.gif) function can be abstracted further as a function of ![n ](/wordpress/wp-content/plugins/latex/cache/tex_6fa45c22bd311a4aa532cffb668d86a0.gif), where ![n ](/wordpress/wp-content/plugins/latex/cache/tex_6fa45c22bd311a4aa532cffb668d86a0.gif) is the size of the array to be sorted:

![T\(n\) ](/wordpress/wp-content/plugins/latex/cache/tex_4df613dbccbdf85fc2a66aca70969a9c.gif)

Since the value of ![T\(n\) ](/wordpress/wp-content/plugins/latex/cache/tex_4df613dbccbdf85fc2a66aca70969a9c.gif) will grow as ![n ](/wordpress/wp-content/plugins/latex/cache/tex_6fa45c22bd311a4aa532cffb668d86a0.gif) grows (presumably), this seems like a solid footing to start our thinking upon.

Alrighty. Now that we've got some notation to start thinking about how we'll build this bad boy, let's actually pick a real, concrete algorithm and think through it. For the purposes of simplicity and succinctness (cue laughter), I'm going to go with [Bubble Sort](<http://en.wikipedia.org/wiki/Bubble_sort>). If you want to learn more about the actual algorithm, I suggest you read the wikipedia article linked to above, because I'm gonna skip over a fat exposition on what it actually does and how it does it in favor of thinking about how long it _takes_ to do it, and specifically how long it takes to do it to the worse possible case of input: an array that's already been sorted, but reversed. Please note I have copied the following pseudocode directly from wikipedia, and credit therefor is due directly to the author of the page linked to above.

![c_{1} ](/wordpress/wp-content/plugins/latex/cache/tex_f5a8dc2100232317501798aef2136fce.gif)  
![c_{2} ](/wordpress/wp-content/plugins/latex/cache/tex_46a0953f49dc908f517f7b8e3599ce0f.gif)  
![c_{3}n ](/wordpress/wp-content/plugins/latex/cache/tex_34e67db8f2efedeb7c00cc787613a2b2.gif)  
![c_{4}n ](/wordpress/wp-content/plugins/latex/cache/tex_56bc9141c4b140d44b8cb4ffc44b593f.gif)  
![c_{5}n\(n-1\) ](/wordpress/wp-content/plugins/latex/cache/tex_29fbc20da3471cfac95817e174c6508f.gif)  
![c_{6}n\(n-1\) ](/wordpress/wp-content/plugins/latex/cache/tex_114f1abc3d8cb8ac60905e49c99f9460.gif)  
![c_{7}n\(n-1\) ](/wordpress/wp-content/plugins/latex/cache/tex_bb8bbb4afe68d6c721e7ff95e3a86d88.gif)

![c_{8}n ](/wordpress/wp-content/plugins/latex/cache/tex_83e966c8380f5364e394ea832dbeb3be.gif)

procedure bubbleSort( A : list of sortable items )  
repeat  
swapped = false  
for i = 1 to length(A) - 1 inclusive do:  
if A[i-1] > A[i] then  
swap( A[i-1], A[i] )  
swapped = true  
end if  
end for  
until not swapped  
end procedure

OK, so that's the algorithm from wikipedia - but what's all that nasty-looking business on the right? Put quite simply, that's our best guess as to how long that line of code takes to execute! Note that each line is some function of ![n ](/wordpress/wp-content/plugins/latex/cache/tex_6fa45c22bd311a4aa532cffb668d86a0.gif) and some constant ![c_{i} ](/wordpress/wp-content/plugins/latex/cache/tex_270988921d2d88e2bf292f4caccb0845.gif). Now if we wanted to figure out _exactly_ how long this algorithm takes to run, we'd need to know the value of those contants, e.g. ![c_{1} = 12.2ms ](/wordpress/wp-content/plugins/latex/cache/tex_c4fa814f77f2a12b7f5dc261feae338f.gif) or something. You'll notice that some lines _only_ seem to take a constant time to run; that's because those lines are only executed once _regardless of how big the input is_. Other lines are the associated constant multiplied by ![n ](/wordpress/wp-content/plugins/latex/cache/tex_6fa45c22bd311a4aa532cffb668d86a0.gif) \- those lines will execute once for every unit of input. Still others are multiplied by ![n\(n-1\) ](/wordpress/wp-content/plugins/latex/cache/tex_3098b1083ac981b7c728533cfa4fbafe.gif) \- these lines are executed ![n-1 ](/wordpress/wp-content/plugins/latex/cache/tex_41c82d523ef9895c903eca0ccbda03bc.gif) times for each input. Now, handily, we can figure out our overall formula by just adding all these things together:

![T\(n\) = c_{1} + c_{2} + c_{3}n + c_{4}n + c_{5}n\(n-1\) + c_{6}n\(n-1\) + c_{7}n\(n-1\) + c_{8}n ](/wordpress/wp-content/plugins/latex/cache/tex_dbca013708a4a9a62f6fff5fae63721f.gif)

  


![T\(n\) = c_{1} + c_{2} + c_{3}n + c_{4}n + c_{5}n^{2}-n + c_{6}n^{2}-n + c_{7}n^{2}-n + c_{8}n ](/wordpress/wp-content/plugins/latex/cache/tex_6a84257bf25f7279d5f2a62b4aec3b37.gif)

  


![T\(n\) = \(c_{5} + c_{6} + c_{7}\)n^{2} + \(c_{3} + c_{4} + c_{8} - 3\)n + \(c_{1} + c_{2}\) ](/wordpress/wp-content/plugins/latex/cache/tex_321d1916a4318ce2b9b4d098602b0aa5.gif)

But it turns out that the precise value of each constant is practically useless - the constants in question represent such complex matters and concrete facts of the real world as language of implementation, hardware specs, how many other processes are fighting for CPU time, etc. Remember that we only really care about the performance of the _algorithm_ \- not the performance of the hardware or implementation thereof, which is not affected by the algorithm itself. So we can happily simplify our job by just getting rid of all those pesky constants!

![T\(n\) = n^{2} + n ](/wordpress/wp-content/plugins/latex/cache/tex_13db7c457bd0320380dc18ee50d7d8da.gif)

Wow, much nicer! But guess what: it gets even simpler. Since, for large enough inputs, the contribution of the lower-order term ![n ](/wordpress/wp-content/plugins/latex/cache/tex_6fa45c22bd311a4aa532cffb668d86a0.gif) makes virtually no difference to the output number, we can happily drop that too:

![T\(n\) = n^{2} ](/wordpress/wp-content/plugins/latex/cache/tex_bd661977b23acf8fe0e1efc93d998a6e.gif)

And voilá! Unfortunately, we've boiled this timing function down so far and stripped so much from it that we can't really say that ![T\(n\) ](/wordpress/wp-content/plugins/latex/cache/tex_4df613dbccbdf85fc2a66aca70969a9c.gif) is _exactly_ ![n^{2} ](/wordpress/wp-content/plugins/latex/cache/tex_093456214537de9bf72aac04b00c55b7.gif), just that (in the worst case) it follows a similar curve. More precisely, we have virtually guaranteed that, for large enough inputs, it can never be bigger than some constant ![c ](/wordpress/wp-content/plugins/latex/cache/tex_9400ebf223f50ff8fccb32ed13ea819e.gif) _times_ ![n^{2} ](/wordpress/wp-content/plugins/latex/cache/tex_093456214537de9bf72aac04b00c55b7.gif). This is the crux of asymptotic notation - specifically what is referred to as "Big-O notation". As such, when we say that:

![T\(n\) = O\(n^{2}\) ](/wordpress/wp-content/plugins/latex/cache/tex_133e9f1515189423e9a2e5248a7dba57.gif)

What we mean is that there are some constants ![c ](/wordpress/wp-content/plugins/latex/cache/tex_9400ebf223f50ff8fccb32ed13ea819e.gif) and ![a ](/wordpress/wp-content/plugins/latex/cache/tex_99020cb24bd13238d907c65cc2b57c03.gif), such that for all ![n ](/wordpress/wp-content/plugins/latex/cache/tex_6fa45c22bd311a4aa532cffb668d86a0.gif) where ![0 \\le a < n ](/wordpress/wp-content/plugins/latex/cache/tex_3f4a026870b81ff5de38c54fe0096ccd.gif), we know that ![T\(n\) \\le cn^{2} ](/wordpress/wp-content/plugins/latex/cache/tex_0c92d598ba6c40ec0c8c9ab004de2b93.gif).

It should also be pointed out that the notation's use of the "equals sign" is a little unusual - we're not saying that ![T\(n\) ](/wordpress/wp-content/plugins/latex/cache/tex_4df613dbccbdf85fc2a66aca70969a9c.gif) _is equal to_ ![O\(n^{2}\) ](/wordpress/wp-content/plugins/latex/cache/tex_3306139fad2e84214191fb8212060c4c.gif), but that it is of equal or lesser _order_ to ![n^{2} ](/wordpress/wp-content/plugins/latex/cache/tex_093456214537de9bf72aac04b00c55b7.gif). This might be a bit of a trick to wrap your head around at first (it certainly was to me). If I'd have written the notation myself, I'd have tried to use some symbol that didn't already carry all the connotations and denotations the "equals sign" itself does; but c'est la vie - this is the way it's done. Another way (in fact, the proper way) to think of it is to think of ![O\(n^{2}\) ](/wordpress/wp-content/plugins/latex/cache/tex_3306139fad2e84214191fb8212060c4c.gif) being some set of functions that follow the above definition, and for the notation

![T\(n\) = O\(n^{2}\) ](/wordpress/wp-content/plugins/latex/cache/tex_133e9f1515189423e9a2e5248a7dba57.gif)

to in fact mean

![T\(n\) \\in O\(n^{2}\) ](/wordpress/wp-content/plugins/latex/cache/tex_00f8df56f1fe095f524dbdc010c4ea05.gif)

i.e. that ![T\(n\) ](/wordpress/wp-content/plugins/latex/cache/tex_4df613dbccbdf85fc2a66aca70969a9c.gif) is an _element_ of the set ![O\(n^{2}\) ](/wordpress/wp-content/plugins/latex/cache/tex_3306139fad2e84214191fb8212060c4c.gif).

OK, so we've been able to put an upper bound on some hypothetical order of our function ![T\(n\) ](/wordpress/wp-content/plugins/latex/cache/tex_4df613dbccbdf85fc2a66aca70969a9c.gif), but what does that really tell us? Not a whole lot, in isolation. But it really comes into play when you consider other algorithms, such as, say [Merge Sort](<http://en.wikipedia.org/wiki/Merge_Sort>), which is bounded on top not by ![O\(n^{2}\) ](/wordpress/wp-content/plugins/latex/cache/tex_3306139fad2e84214191fb8212060c4c.gif), but by ![O\(n\\log_{2}n\) ](/wordpress/wp-content/plugins/latex/cache/tex_6683d14c695737b36b0b60968b56c04e.gif)! Graph those two functions and here's what you get (![n^{2} ](/wordpress/wp-content/plugins/latex/cache/tex_093456214537de9bf72aac04b00c55b7.gif) is in black, ![n\\log_{2}n ](/wordpress/wp-content/plugins/latex/cache/tex_d5c3a3002b4a1a4c546caea68a7a6bcd.gif) is in red):

[![](/wp-content/uploads/2012/01/graph-e1327292808431-300x173.png)](</wp-content/uploads/2012/01/graph-e1327292605398.png> "graph")

This is a bit of an oversimplification, but sufficient to demonstrate the idea - notice that very quickly, ![n^{2} ](/wordpress/wp-content/plugins/latex/cache/tex_093456214537de9bf72aac04b00c55b7.gif) begins to overtake ![n\\log_{2}n ](/wordpress/wp-content/plugins/latex/cache/tex_d5c3a3002b4a1a4c546caea68a7a6bcd.gif), and continues to do so, the gap getting ever wider as n gets ever bigger; and just like in golf, the lower score is the one you want.

So, in what I hope was nutshell-ish if not perfectly so, that's the basics of asymptotic notation! There are other, related notations like "Big Theta" ![\\Theta\(g\(n\)\) ](/wordpress/wp-content/plugins/latex/cache/tex_70cf58380aa0dadd0aefb858fa5f925f.gif), "Big Omega" ![\\Omega\(g\(n\)\) ](/wordpress/wp-content/plugins/latex/cache/tex_aa0884f77bfcfdcaf1f0c8477a1d2dc2.gif), and the lower-case versions of omega and o, but I'll leave those to you to explore.

Finally, as a disclaimer, I have tried to make the math herein as simple as possible for the purposes of the demonstration, and I could easily have borked something up terribly (I'm still getting the hang of LaTeX). If you spot an error, comment and I'll see that it's corrected. Thanks!
