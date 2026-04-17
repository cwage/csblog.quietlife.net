---
layout: post
title: "obfuscated perl"
date: 2005-06-29
author: Chris
---
[This](<http://perl.plover.com/obfuscated/bestever.pl>) is the best bit of obfuscated perl I have ever seen. It's pretty obfuscated for perl as is. What makes this amazing is that it's also valid postscript. Go ahead, try printing it out:

> /;{}def/#{def}def/$_={/Times-Bold exch selectfont}#/_{rmoveto}#/"{dup}#/*/!/$  
>  ;/q{exch}#/x ; {/J q #}#/.{/T q #}#{stringwidth}#{}#{}# 14 string dup dup dup  
>  260 40 moveto 90 rotate ; %/}};$0='"\e[7m \e[0m"';@ARGV=split//,reverse  
>  q(ThePerl). q(Journal) x 220 ; q ; 0 T putinterval exch 7 J putinterval ;  
>  ; $_= q /m$ pop T($*!$"=!$ " )pop " * true% ? $ " $!" " !! !! % !" !" !  
>  ! charpath {!"""}pop $ pop{""!}pop ! neg{!#}pop 220 ! neg _{!!}pop J false %T  
>  charpath clip " pop 0 " moveto 6{!!}pop $_= 105{!!}pop {$ ! $ " ! #! ##}  
>  pop{dup dup $ ! " pop pop q{"}pop 22{dup show}repeat {"}pop q 22 mul{$ "} pop  
>  neg{!#! $ "}pop ! 8 .65 mul{$ # # $}pop ! neg{"}pop _ pop{"}pop } repeat pop  
>  " { $ " ! ! ! $ " ! !" "#" #"!"""""! #" " # "m/;@ARGV=(@ARGV[-14..-1])x50;q}  
>  0 "%};s/m[ou]|[-\dA-ln-z.\n_{}]|\$_=//gx;s/(.)(?{$*=''})/('$*.='.(++$#  
>  %2?'':"$0;").'pop;')x(ord($1)-31).'$*'/gee;s/((.(\e\\[.m)*|.){77})/$1\n/g;print  
>  ; sub showpage {}
