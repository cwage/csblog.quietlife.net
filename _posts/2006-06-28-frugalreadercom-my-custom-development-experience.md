---
layout: post
title: "FrugalReader.com: My Custom Development Experience"
date: 2006-06-28
---
Gene McCabe, owner of [FrugalReader.com](<http://www.frugalreader.com/>), was kind enough to be a guest blogger this week. He shares his experience in working with a development firm ([CentreSource](<http://www.centresource.com/>)) to develop the latest version of FrugalReader.com. For anyone looking to read an honest, realistic experience about Custom Web Development, I encourage you to read Gene's commentary.  
  


* * *

## Superhighway to Success or   
Long and Winding Dirt Road to Perdition?

**A Client's Perspective on Building a Consumer Web Software Application**

**The Vision**  
[FrugalReader.com](<http://www.frugalreader.com/>) ("FR") is an innovative book sharing website that goes well beyond trading books. It's a venue for book lovers to relate with one another and share opinions, experiences and their passion for reading. FR went live on the Internet on December 12, 2004 and grew nicely over the following six months or so with what I'd describe as basic functionality. With a vision to turn FR into a place for avid readers to deeply connect with one another and share their thoughts on books and life, I began planning to take the website to the next level by adding enhanced functionality and a new graphic design.

**Hire or Contract?**  
With a significant development effort needed, I contemplated hiring a developer or contacting with one for an extended period of time. The primary advantages of this approach are lower development cost and complete control over the development resource. However, the disadvantages are substantial. I engaged a software development firm instead because I needed broader and deeper human resources, skills and tools than a single developer could provide. And since revamping a web application involves much more than writing software, there would be development downtime that would need to be filled with other activities depending upon where we were in the Software Development Life Cycle (SDLC).

**Right Firm**  
Choosing the right software development firm is as much about selling as it is about buying. The software development firm is selling its ability to meet my development and other related needs. I'm selling an exciting project, my vision for future growth (i.e. more business in the future), and my ability to be a great client. Through a mutual contact I met with Nicholas Holland of [CentreSource](<http://www.centresource.com/>) and quickly gained confidence that his firm had the capabilities I needed. There are numerous firms that could build what I needed, so why CentreSource? FR and CentreSource were at about the same place on a similar path. Both were relatively young organizations trying to do something different and better. If our project was a success, we would clearly both help grow each others business.

**Appropriate Engagement**  
There is no simple way and certainly no one right way to engage a software development firm. CentreSource and FR entered into an agreement whereby CentreSource would develop a custom software application per the requirements (detailed in the agreement) defined by FR. Payment was made in stages as work was completed with the final payment made upon delivery of the completed product. Sounds straightforward but as a practical matter the software development process is not nearly as objective as we'd like it to be. The difficulty lies in the requirements. If the requirements are excruciatingly detailed (effectively programming specifications), then it's much more likely that the development firm can accurately estimate the Level Of Effort (LOE), and therefore the cost, to produce the product. But creating such detailed requirements is costly and doing so without the aid of a development team increases the risk of creating a design that's far from optimal from a programming and, more importantly, an end user perspective.

**Build Without a Blueprint**  
A primary reason for hiring CentreSource was to leverage its creative development staff. I needed innovative applications of the latest web software development tools. So we proceeded with relatively high level requirements and worked out application design details during the build phase.

Not surprisingly, as we worked through the development of the application two things happened. First, the development team realized some of the work was more complex than originally estimated. This almost always happens when requirements are at a high level because the software development firm doesn't benefit from overestimating the LOE. Rather, the software development firm benefits from erring on the side of underestimating LOE because the project looks more attractive to the client and the software development firm knows that it will charge for any out of scope work.

Second, in working with the development team several opportunities to improve the product were recognized that were not included in the original scope. Some of these alternative approaches or enhanced feature options were spawned by the development team and presented to me for consideration while others came from me, the client. Regardless of the source, each enhancement was a separate decision with an associated cost if implemented.

**Test, Test, Test**  
The application had more defects coming out of unit testing that I had anticipated. Thus User Acceptance Testing (UAT) was a pretty arduous task and there were added test/code/test cycles. This result is not necessarily bad if you think through the alternative. It'd be relatively expensive to have developers perform more extensive testing. And if the software development firm has a Quality Assurance (QA) team, that too would cost additional money to have them develop and execute thorough test plans. In this case it was more cost effective for me to perform the robust testing.

**Go-Live!**  
The November 28, 2005 cutover was more challenging than when I first brought FR online in December, 2004. We switched to a new ISP which of course required rerouting IP addresses and email. And since the new database had a completely different schema, it was necessary to convert all existing data. We had tightened up the transaction record tracking and data relationships which complicated the conversion and required CentreSource to program around some gaps in the original database structure. The data conversion was a significant challenge, as expected, and despite prior testing we ran into some referential integrity issues. The important problems were immediately addressed and some minor issues impacting a relatively few number of member accounts were left for me to manually clean up. CentreSource stuck with it until I was satisfied we had done everything necessary.

**Post-Implementation**  
One by one we overcame the relatively few technical conversion issues that arose. A good number of FR members understandably found it difficult to adapt to the new design. Several indicated, for various reasons, that they preferred the previous design. This feedback was expected but there were also a small and growing number of members that considered a particular new feature unfair and were quite passionate and vocal in the forums about their discontent. They didn't like the fact that they were unable to request a book within the first 48 hours of it being listed unless they upgraded (at a cost of $25.00/year) their account to Premium. I joined in the discussions, solicited specific feedback and spoke with a few members via telephone to get a better understanding of their concerns, needs and preferences.

After listening to the membership I had CentreSource make a small programming change that had a dramatic impact. I automatically convert each Standard account to Premium (for free) when the respective member ships 2 books that are marked received by the requester. This effectively made all existing member accounts Premium. New members would still need to wait 48 hours after a book was listed before requesting it, but only until proving themselves as legitimate traders by shipping 2 books.

**Outcomes**  
I wasn't surprised by any outcome from the project but some didn't meet my expectations. And some of the outcome variance was a direct result of decisions made by me. So even though there were outcomes that were not necessarily desirable, they were better than the next best alternative. Below are a few of the outcomes worth noting.

1\. The project scope grew significantly, yet with the appropriate client approval at each juncture.  
2\. CentreSource provided value-added functionality input and ideas, and elegant software design solutions. One salient example is FR Trade Groups. This unique feature gives members the autonomy to form and maintain groups of members with similar interests. The feature is being rapidly adopted, especially by members who use the website frequently.  
3\. The application had more defects after unit testing than anticipated.  
4\. Go-live support was very effective and necessarily so for the cutover to be successful.  
5\. There was no opportunity for finger pointing between vendors because I had CentreSource provide all major services: infrastructure setup/maintenance, website graphic design, and software development.  
6\. The project took longer to complete than originally planned, even when taking the additional scope into account.

**Lessons Learned**  
_Here are lessons that I learned, or that were once again reinforced, through the project._

1\. Ask your customers what they want, but give them what they need. Ask all your employees, ask your software development firm - ask anyone with skin in the game what they recommend. Ideas are now the currency of business. Also, review new features and process changes with select hand-picked users before building and deploying them.  
2\. Build a good, but not a great, application in the first release. Software is evolutionary. It needs to be used, understood, and its impact measured for it to be effectively improved.  
3\. Keep it simple. People use web applications and people like software that is straightforward, intuitive and easy to use.  
4\. Work with clear purpose and high energy during the project negotiating and planning phase. The project preparation activities often take longer than necessary to complete and are the greatest opportunity to reduce the overall project time. Don't be overly eager, but do be specific about expectations on follow up and deadlines throughout the project for all but the least important tasks.  
5\. Know who owns the project and confirm that the person is accountable to you. I owned the FR project and therefore managed the project. CentreSource coordinated a lot of activities behind the scenes but I was ultimately responsible for making things happen and ensuring that all the pieces fit together at the right time.  
6\. Partner with people that you trust. At the end of the day, good business comes down to trust. And you don't trust a business, you trust people. If you have an open and trusting relationship with key managers of your business partner you're much more likely to have an economically successful engagement, regardless of how your contracts or other legal agreements are structured.  
7\. Leverage key managers at the software development firm. One of the best value added services CenterSource provides is its CEO, Nicholas Holland. He stayed close to my project and gave me many suggestions and ideas to consider, several of which were business, not technology, oriented. This type of input is a valuable resource and one that the best software development firms will include, to a degree, without charge.  
8\. Beware of lack of regression testing. Regression testing has not reached the level it needs to in software development. Even some large software development shops lack sophisticated regression testing tools and techniques, and rely almost solely on ad hoc testing to ensure that related functionality wasn't broke by new code.  
9\. Software development never ends. Software is merely a means to more effectively perform an activity or process. And activities and processes changes because people change. Your software application will change or it will die. The frequency of change is dependent upon the activities, processes and people who use and rely on it.

Gene J. McCabe  
President, Frugal Concepts  
[genemccabe@yahoo.com](<mailto: genemccabe@yahoo.com>)  
See my FrugalReader.com profile & photo: [http://frugalreader.FrugalReader.com](<http://frugalreader.frugalreader.com/>)
