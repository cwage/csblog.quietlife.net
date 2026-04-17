---
layout: post
title: "Apple xServe: dscl, dsimport and web services aka fun!"
date: 2008-04-04
author: Jonathan Wage
categories: [Miscellaneous, PHP, Web Development]
---
So, recently here at CentreSource we've been working on a project which is using the brand spanking new xServe from Apple. First, let me say the server is pretty slick, but like any other software it has issues. The reason we went with the xServe was because we needed the ability to have web applications which have central authentication and calendaring data. Open Directory, CalDAV, PHP, Apache, and MySQL are just ready to go with xServe, so it made sense!Our usage is that we have these web applications on the net which will use the [PHP LDAP Functions](<http://us3.php.net/ldap>) to authenticate our users on Open Directory from our PHP web applications, we also communicate to Open Directory whenever adding or changing users passwords to keep things up-to-date. To accomplish this I have written a small web service which lives on the xServe and runs under Apache and PHP. This code talks to Open Directory via the dscl and dsimport command line utilities provided by Apple. I use dsimport for adding the initial working records, and I then use dscl to change passwords. So essentially this web service is just a web service wrapped around those two commands.

Now, on to the issues. I first was using dscl by generating a temporary file named commands.txt which I then piped to the dscl command. It did a few things, it authenticated with the open directory admin, changed to the users directory, authenticated to that node, then issued the command to change a users password. Below are the exact steps I took to reproduce the issue, and essentially this is the core of what my web service does. This is just a manual representation of it.

-------------

> 1.) Add the user dsimport -g jon.txt /LDAPv3/127.0.0.1 O -u opendiradmin -p password -y applexserveaddress.com -yrnm opendiradmin -yrpwd passwordContents of jon.txt 0×0A 0×5C 0×3A 0×2C dsRecTypeStandard:Users 6 RecordName AuthMethod Password UniqueID PrimaryGroupID RealName jon:dsAuthMethodStandard\:dsAuthClearText:password:2004:20:Jonathan H. Wage
> 
> 2.) Testing authentication with dirt server:Users jwage$ dirt -u jon -p password
> 
> Call to dsGetRecordList returned count = 1 with Status : eDSNoErr : (0)
> 
> Call to checkpw(): Success
> 
> path: /LDAPv3/127.0.0.1 Username: jon Password: password Success
> 
> 3.) Testing authentication with ldap binding' Using this PHP script: http://pastie.textmate.org/171856 Note: This is the method of authentication I will use to in my web applications.
> 
> This script shows "Success"...
> 
> 4.) Changing Password with dscl
> 
> Contents of commands.txt
> 
> cd /LDAPv3/127.0.0.1 auth opendiradmin password passwd Users/jon newpass
> 
> Command used to change password
> 
> cat commands.txt | dscl -u opendiradmin -P password applexserveaddress.com
> 
> 5.) Testing old password with dirt dirt -u jon -p password
> 
> Call to dsGetRecordList returned count = 1 with Status : eDSNoErr : (0)
> 
> Call to checkpw(): Bad Password
> 
> path: /LDAPv3/127.0.0.1 Username: jon Password: password Error : eDSAuthFailed : (-14090)
> 
> 6.) Testing new password with dirt
> 
> dirt -u jon -p newpass Call to dsGetRecordList returned count = 1 with Status : eDSNoErr : (0)
> 
> Call to checkpw(): Bad Password
> 
> path: /LDAPv3/127.0.0.1 Username: jon Password: newpass Error : eDSAuthFailed : (-14090)
> 
> 7.) Testing new password with: http://pastie.textmate.org/171856 Changed "password" to "newpass" in the PHP script linked to above.
> 
> This script shows "Failure"...
> 
> Attached is a file named jon.txt produced by the following command dscl /LDAPv3/127.0.0.1 read /Users/jon > ~/jon.txt  
>  <br/> Contents of jon.txt ------------- dsAttrTypeNative:apple-generateduid: A4891049-44B3-466E-B38A-49190A57EEFC dsAttrTypeNative:authAuthority: ;ApplePasswordServer;0×47ec5cb02b82fcae0000001700000017,1024 35 165460696124814462411611436492354879433092038102783905389795105675339122350613168014994644237932552198395261589394442778231023754518789840462560068601355183790356702635800277892727080147503108118694113781754703058183613068520410434810818614704517699376740702860179744461656638410687251764916990406937612551307 root@applexserveaddress.com:208.65.156.21 ;Kerberosv5;0×47ec5cb02b82fcae0000001700000017;jon@SERVER.SOUTHWESTERNEDGE.COM;SERVER.SOUTHWESTERNEDGE.COM;1024 35 165460696124814462411611436492354879433092038102783905389795105675339122350613168014994644237932552198395261589394442778231023754518789840462560068601355183790356702635800277892727080147503108118694113781754703058183613068520410434810818614704517699376740702860179744461656638410687251764916990406937612551307 root@applexserveaddress.com dsAttrTypeNative:cn: Jonathan H. Wage dsAttrTypeNative:gidNumber: 20 dsAttrTypeNative:homeDirectory: 99 dsAttrTypeNative:objectClass: inetOrgPerson posixAccount shadowAccount apple-user extensibleObject organizationalPerson top person dsAttrTypeNative:sn: 99 dsAttrTypeNative:uid: jon dsAttrTypeNative:uidNumber: 2004 dsAttrTypeNative:userPassword: ******** AppleMetaNodeLocation: /LDAPv3/127.0.0.1 AuthenticationAuthority: ;ApplePasswordServer;0×47ec5cb02b82fcae0000001700000017,1024 35 165460696124814462411611436492354879433092038102783905389795105675339122350613168014994644237932552198395261589394442778231023754518789840462560068601355183790356702635800277892727080147503108118694113781754703058183613068520410434810818614704517699376740702860179744461656638410687251764916990406937612551307 root@applexserveaddress.com:208.65.156.21 ;Kerberosv5;0×47ec5cb02b82fcae0000001700000017;jon@SERVER.SOUTHWESTERNEDGE.COM;SERVER.SOUTHWESTERNEDGE.COM;1024 35 165460696124814462411611436492354879433092038102783905389795105675339122350613168014994644237932552198395261589394442778231023754518789840462560068601355183790356702635800277892727080147503108118694113781754703058183613068520410434810818614704517699376740702860179744461656638410687251764916990406937612551307 root@applexserveaddress.com GeneratedUID: A4891049-44B3-466E-B38A-49190A57EEFC LastName: 99 NFSHomeDirectory: 99 Password: ******** PrimaryGroupID: 20 RealName: Jonathan H. Wage RecordName: jon Jonathan H. Wage RecordType: dsRecTypeStandard:Users UniqueID: 2004

Now as you can see above, piping the commands.txt directly to dscl does not change the password correctly and breaks, but entering the commands one at a time interactively via the terminal does work.

Below you can find the first draft of the web service which adds and edits username/passwords in apples open directory. Note, this code is beta and currently does not do any checking to verify things, and the delete functionality is not written yet. This is the first working draft we were able to produce. Hopefully this will help someone else get started with using this software in the same way.

It took an $800 dollars apple enterprise support contract for me to verify that I was not doing something wrong, and that it in fact was a bug. I was not too happy when the tech support guy told me that it was a bug and that I had to pay another 800 dollars for him to come up with a work around or for him to report it to the engineers. So, thanks Apple. I reported the bug myself and came up with a work around.

[Open Directory Manager](<http://blog2.centresource.com/wp-content/uploads/2009/01/open_directory_manager.zip>)
