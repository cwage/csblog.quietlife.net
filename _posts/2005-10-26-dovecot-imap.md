---
layout: post
title: "dovecot IMAP"
date: 2005-10-26
author: Chris
categories: [Software]
---
As a followup to [this post](<https://csblog.quietlife.net/2005/10/14/imapvnew/>), I should note that [dovecot](<https://web.archive.org/web/20051101214522/http://www.dovecot.org/>), an IMAP daemon I've been meaning to check out for a while now, does indeed suport server-side indexing to aid searching for mail.

I haven't found any good answer to the problem of compressing and archiving mail server-side, however (although they have [discussed it](<https://web.archive.org/web/20051226004515/http://dovecot.org/list/dovecot/2005-June/thread.html#7684>) on the dovecot dev list). Probably because this requires cooperation on behalf of both the MDA (i.e. the MTA or something like procmail) and the mail-reading protocol (IMAP, et al) to both agree to read/write gzipped/bzipped data.

One hack I do think would be relatively easy to append to the IMAP RFC would be something similar to HTTP's "Accept-Encoding" header. It would be trivial for an IMAP client to hack in gzip/bzip support and send "Accept-encoding: gzip" and likewise trivial for any IMAP servers to recognize it and deliver gzipped data. This wouldn't help the problem of storing uncompressed data, but it would help sending it over bandwidth-constrained paths.
