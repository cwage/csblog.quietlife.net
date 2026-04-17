---
layout: post
title: "sober.p/q spam backscatter"
date: 2005-05-16
author: Chris
categories: [Spam]
---
Filtering the spam being sent from sober.p/q is fairly easy as the bayesian/DCC type checks begin to catch it more and more accurately. In addition, someone has provided some convenient [rules](<https://web.archive.org/web/20050517010505/http://mailscanner.prolocation.net/german.cf>) to catch the spam directly in spamassassin.

But a particularly annoying problem is blocking the [backscatter](</2005/05/03/backscatter/>) that results from this Sober.P spam. Blocking backscatter consistently is much tougher. In general, filtering backscatter consistently is difficult, because it's tricky to identify the the backscatter spam from the legitimate NDRs -- and simply not accepting mail with a null return path (MAIL FROM: <>) is [against the RFC](<https://web.archive.org/web/20050602074731/http://www.rfc-ignorant.org/policy-dsn.php>) (all NDRs are sent with a null return path).

So, unfortunately, the best way to filter backscatter from a worm/virus going around is sadly on a case-by-case basis. For the backscatter from this latest Sober.P worm, you may want to add some spamassassin rules like these to kill the backscatter, as a complement to the normal [rules](<https://web.archive.org/web/20050517010505/http://mailscanner.prolocation.net/german.cf>) mentioned above. Naturally you will need to add a score for each of these rules as well:

> body SOBERQ_BACKSCATTER1 /Subject:.*Volk wird nur zum zahlen/  
>  describe SOBERQ_BACKSCATTER1 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER2 /Subject:.*Armenian Genocide Plagues Ankara/  
>  describe SOBERQ_BACKSCATTER2 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER3 /Subject:.*Augen auf/  
>  describe SOBERQ_BACKSCATTER3 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER4 /Subject:.*Auslaender bevorzugt/  
>  describe SOBERQ_BACKSCATTER4 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER5 /Subject:.*Auslaenderpolitik/  
>  describe SOBERQ_BACKSCATTER5 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER6 /Subject:.*Blutige Selbstjustiz/  
>  describe SOBERQ_BACKSCATTER6 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER7 /Subject:.*Can you believe this still happens today/  
>  describe SOBERQ_BACKSCATTER7 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER8 /Subject:.*Deutsche Buerger/  
>  describe SOBERQ_BACKSCATTER8 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER9 /Subject:.*Deutsche werden kuenftig beim/  
>  describe SOBERQ_BACKSCATTER9 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER10 /Subject:.*Dresden 1945 /  
>  describe SOBERQ_BACKSCATTER10 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER11 /Subject:.*Dresden Bombing Is To Be Regretted Enormously/  
>  describe SOBERQ_BACKSCATTER11 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER12 /Subject:.*Du wirst ausspioniert/  
>  describe SOBERQ_BACKSCATTER12 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER13 /Subject:.*Du wirst zum Sklaven gemacht/  
>  describe SOBERQ_BACKSCATTER13 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER14 /Subject:.*Gegen das Vergessen/  
>  describe SOBERQ_BACKSCATTER14 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER15 /Subject:.*Graeberschaendung auf bundesdeutsche/  
>  describe SOBERQ_BACKSCATTER15 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER16 /Subject:.*Hier sind wir Lehrer die einzigen Auslaender/  
>  describe SOBERQ_BACKSCATTER16 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER17 /Subject:.*Jahre Befreiung/  
>  describe SOBERQ_BACKSCATTER17 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER18 /Subject:.*Massenhafter Steuerbetrug durch auslaendische/  
>  describe SOBERQ_BACKSCATTER18 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER19 /Subject:.*Multi\\-Kulturell/  
>  describe SOBERQ_BACKSCATTER19 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER20 /Subject:.*Osteuropaeer durch Fischer-Volmer Erlass/  
>  describe SOBERQ_BACKSCATTER20 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER21 /Subject:.*Paranoider Deutschenmoerder kommt/  
>  describe SOBERQ_BACKSCATTER21 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER22 /Subject:.*Polizei schlaegt Alarm/  
>  describe SOBERQ_BACKSCATTER22 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER23 /Subject:.*Schily ueber Deutschland/  
>  describe SOBERQ_BACKSCATTER23 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER24 /Subject:.*Transparenz ist das Mindeste/  
>  describe SOBERQ_BACKSCATTER24 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER25 /Subject:.*Trotz Stellenabbau/  
>  describe SOBERQ_BACKSCATTER25 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER26 /Subject:.*Tuerkei in die/  
>  describe SOBERQ_BACKSCATTER26 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER27 /Subject:.*Turkish Tabloid Enrages Germany with Nazi Comparisons/  
>  describe SOBERQ_BACKSCATTER27 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER28 /Subject:.*Verbrechen der deutschen Frau/  
>  describe SOBERQ_BACKSCATTER28 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER29 /Subject:.*Volk wird nur zum zahlen/  
>  describe SOBERQ_BACKSCATTER29 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER30 /Subject:.*Vorbildliche Aktion/  
>  describe SOBERQ_BACKSCATTER30 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER31 /Subject:.*Whore Lived Like a German/  
>  describe SOBERQ_BACKSCATTER31 Backscatter from Sober.Q spam
> 
> body SOBERQ_BACKSCATTER32 /Subject:.*wirst ausspioniert/  
>  describe SOBERQ_BACKSCATTER32 Backscatter from Sober.Q spam
