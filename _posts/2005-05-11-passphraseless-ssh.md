---
layout: post
title: "passphraseless ssh"
date: 2005-05-11
author: Chris
---
I have written [articles](<http://chris.quietlife.net/2003/10/23/security-part-iii/>) in the past about ways to use passphraseless SSH keys in a secure manner, by using the the "command" parameter in the _authorized_keys_ file. The one inconvenience with this method is that it only lets you specify one command.

What if you want an account to be able to execute, say, two or three varying commands using the same key? For example, today I was setting up a script to rsync data using ssh. The process involved the command "rsync", but with varying parameters. The answer, it seems, is to write a wrapper script. SSH makes the command passed available to whatever command you execute via the $SSH_ORIGINAL_COMMAND environment variable. Thus you can pretty easily write a wrapper script that checks $SSH_ORIGINAL_COMMAND against some pre-defined allowed commands and only execute certain ones.

I wrote a quick script to do this, and I had intended on making a post here detailing the process. However, as is usually the case, after I wrote the script, I realized I had largely reinvented the wheel. My friend Richard pointed me at some [similar scripts](<http://www.ucar.edu/csac/ssh-unattended-file-transfers/restrictrsync/>) he had written, including a great [introduction and howto](<http://www.ucar.edu/csac/ssh-unattended-file-transfers/>). So, I will simply link to his excellent work.

This is a great method for utilizing the convenience of passphraseless ssh keys without allow blanket access to the remote host in question if the key is compromised.
