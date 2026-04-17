---
layout: post
title: "PHP Session Lifetime: An Adventure"
date: 2006-05-23
author: Chris
---
We had a bit of a sticky situation here at the Centresource stomping grounds this past couple of weeks. We have a server with a multitude of environments served via our Apache webserver. It's a fairly simple setup: we have a virtualhost devoted to development environments for all of our software developers, and then a plethora of virtualhosts for the various web-based applications we use: some home-brewed, some OSS web applications we use for various business functions (CMS, CRM, Groupware, etc..).

The mystery started when sessions started mysteriously expiring prematurely on two of our most popular web applications: [DekkoTime](<http://app.dekkotime.com/>), and our internal CRM/groupware application. It started about two weeks ago, with no discernable changes to our configuration that could be responsible.

So to understand what was necessary to track down this problem, we have to explore a little bit about how PHP session data storage and expiration works:

When PHP creates a session with session_start(), it dumps a file in a particular path. This is governed by the _session.save_path_ parameter in php.ini -- /tmp by default. But naturally, as sessions go idle or are abandoned, they need to be cleaned up, so that our save_path isn't overwhelmed with old session data before it has a chanced to be cleaned (usually on reboot, in the case of /tmp). Enter garbage collection.

Garbage collection in PHP is, from what I gather, piggybacked on invocations of the PHP interpreter itself. When (if) it runs, it deletes any session files in the save_path that haven't been accessed in a certain amount of time, governed by another php.ini setting: session.gc_maxlifetime. There are other parameters that dictate the probability/frequency with which the garbage collection routine runs, but they are irrelevant to this discussion.

So, naturally, the first thing I checked to see why our sessions were expiring was session.gc_maxlifetime in our php.ini:
    
    
    session.gc_maxlifetime = 72000
    

72000 seconds -- that's 20 hours. So, no problem there. It appeared from our experience that sessions were expiring between 45 minutes to an hour -- far less than 20 hours. I roughly verified the time that sessions were disappearing by initiating a new session and doing this:
    
    
    date; while true;
    do
    if [ ! -f sess_235f09d44d5288554cf7a55fdfbc6df7 ];
    then echo "session has disappeared" | mail cwage@centresource.com;
    break;
    fi;
    sleep 1;
    done
    

That way, I'd get mailed when the session disappeared. Pretty sick, I know. This verified that sessions were disappearing after around 45 minutes of idle time. I could not find an explanation for this: session.gc_maxlifetime was set to 72000 in our php.ini. Maybe it was being overridden in that particular php environment? "print_r(ini_get("session.gc_maxlifetime"))" bore the same result: 72000. No problem there.

Here I took a slight detour in wondering if there was something else diligently cleaning up an admittedly messy and full /tmp directory (~500 days of uptime will do that). So I started looking for some sort of utility that would let me monitor a file and see what process was responsible for unlinking it (the session file, that is). Sadly, there's no utility that can accomplish this with a stock kernel in Linux: [fwatch](<http://www.fwatch.org/>) appears to accomplish this, but I wasn't about to install a kernel module labelled as an alpha release just to track this down. Eventually I convinced myself, anyway, that the likelihood of some rogue process cleaning up /tmp was pretty unlikely, even for Linux.

So, I resorted to just googling my little heart out. Here's where things get interesting.

Naturally, any application can override _session.gc_maxlifetime_ to whatever pleases it -- in fact, most OSS PHP applications do just this, in order to enforce its own particular idea of a sensible session expiration time. But here's where things get sticky. If you override _session.gc_maxlifetime_ in one particular environment, how does it know which sessions are its own, as opposed to others that should be adhering to the global setting?

Well, apparently, it doesn't. When the PHP garbage collection routine runs, as far as I can tell, it blindly removes sessions from _session.save_path_ that haven't been accessed in longer than _session.gc_maxlifetime_ -- **period**. So, as it happens, what changed two weeks ago? We started playing with a number of PHP applications: [Joomla!](<http://www.joomla.org/>) and [Zen-Cart](<https://web.archive.org/web/20060515102305/http://www.zen-cart.com/>), both of whom (among others), take it upon themselves to override _session.gc_maxlifetime_ to a smaller value, which appears to have been, drumroll please: around 45 minutes. So, every time the PHP interpreter was invoked in this environment, it obliterated sessions for all our other applications if they had been idle for 45 minutes or more. Harsh.

I am not sure what the preferred solution to this is supposed to be, and I'm also surprised that this isn't a more common problem -- overriding _session.gc_maxlifetime_ is a fairly common thing for PHP applications to do these days. I am surprised these unexpected results would go unnoticed. In any event, my solution was just to create a hierarchy of per-application directories inside _/tmp/php_ (owned by www-data, so Apache can write to them), and then adding a line to my Apache virtualhost config for each one, for example:
    
    
    php_admin_value session.save_path /tmp/php4/dekko
    

In this way, the save_path is isolated for each application, so an overridden _session.gc_maxlifetime_ for another codebase won't affect it.

Phew.
