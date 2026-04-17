---
layout: post
title: "SSL Introduction"
date: 2005-05-17
author: Chris
---
We have received a number of questions from people asking why [Swirbo](<http://www.swirbo.com/>)'s e-mail management website prompts them about an "unrecognized certificate"?

There's a good reason for this with a slightly long answer. Read on for a brief (as possible) introduction to how SSL works:

SSL utilizes two different types of encryption in the process of securing a connection -- [symmetric](<http://en.wikipedia.org/wiki/Symmetric_key>) and [public key cryptography](<http://en.wikipedia.org/wiki/Public_key_cryptography>). The difference between these two types of encryption is in how keys are used. It' s a bit complicated. but briefly:

  * Symmetric encryption involves picking **one key** and encrypting the data with this key. The recipient that wants to decrypt this data must have the **same key**.
  * Public key encryption involves picking a **pair of keys** -- one "public" and one "private". Information encrypted with the private key can only be decrypted with the public key and vice versa. In this way, the "public" key can be distributed far and wide without concern for security. Things encrypted with the public key can only be decrypted with the **private** key, kept safe and secure by the recipient.



Public key cryptography is very cool, but it's not very practical for speed reasons to use exclusively in communicating with a webserver. It would take too long to encrypt/decrypt all the data with this method. So, regular old symmetric encryption is our optimum method of securing the communication.

The browser wants to talk to the server with symmetrically encrypted data, for which it needs to pick a shared key (the "session key") to encrypt with. However, it can't just transmit the key in clear-text to the server, since anyone (a "man in the middle") could intercept that and access the subsequent encrypted data. 

This is where public key cryptography comes in: the browser generates a session key and encrypts it with the "public" key and sends it to the server, which has the "private" key -- the only key that can decrypt that data. With SSL, this public key is called the "server certificate". Once the server has the key safely and securely, the browser can begin encrypting the session with the session key, which the server now has as well, and all is well. 

In the world of public-key cryptography, trust is communicated via the process of "signing" public keys. This is a process by which someone else (another organization) uses their private key to "sign" the public key of someone else. It's a way of vouching that this public key represents what it says it does. It prevents malicious third parties from claiming to be an organization they are not by using a fake public key. Anyone with the public key of the signer can verify that the signature of the signer is valid, which increases their level of trust in that public key. The creation of this sort of trust is important.

In the world of SSL for web traffic, this is done by the creation and use of signing authorities -- organizations that are (theoretically) big and stable enough to be trusted to be a clearinghouse for public keys, to verify that they are all who they say they are. These organizations sign the keys to vouch that they can be trusted to represent who they claim to represent.

So, to bring this all back home, if you want to offer secure data via your website, you first have to generate a certificate. Then, it has to be signed. You can either do this yourself (a "self-signed" certificate), or you can send it to a signing authority. The signing authority then signs the certificate and gives it back to you. 

Now you can imagine that a browser connects to a webserver to initiate a secure connection. It gets a certificate signed by abccompany.com, "ABC Company, Inc.". Well, how does the browser know that it can trust this particular company? How is it different from any other company? What makes it an "authority"?

The answer is that most browsers ship with a list of signing authorities that they trust by default. However, you can add others (more on this later).

This gets to the meat of the issue with Swirbo's certificate. Unfortunately, the criteria for being listed as a default signing authority in the most prevalent browser, Internet Explorer, has become increasingly less stringent security-wise and increasingly more expensive.

It is, in effect, a racket. The only real criteria for a signing authority to get listed in IE's browser is paying a very large amount of money for their "security review" process.

As a result, there are a number of large signing authorities in IE's default list which, in turn, charge a significant (but varying) amount of money to sign certificates. They charge a hefty fee to sign a certificate for one host (foo.domain.com) but they charge a truly exorbitant fee for "wildcard" certificates -- ones that will work for any host on a domain (i.e. *.domain.com). Why? Because they can.

To get to the point (finally) we at CentreSource and Swirbo believe in cryptography and security but we don't believe it should be something you have to pay for.

Thus we have used a signing authority that also adheres to this philosophy: [CACert](<http://www.cacert.org/>).

They are an organization that offers free certificate signing and is actively campaigning to get included in the default list of signing authorities in several browsers -- cost being the primary obstacle to getting listed with Microsoft.

We are using them both because we don't feel it's necessary to pay exorbitant fees for certificate signing and we also want to support this organization in its endeavor.

If you want to inherently trust CACert in the future, you can opt to go to [this page](<http://www.cacert.org/index.php?id=3>) and install their root certificate into your browser. By doing this, you will no longer get warnings when you visit sites using certificates signed by CACert.
