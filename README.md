# Sharescription
> ⚠️ This is a Hackathon entry for UofTHacks VI, and was created in under 36 hours. The code in this repo is likely to be hacky and potentially unstable/insecure, so please be careful if forking this repo. [You can view the project's Devpost page here.](https://devpost.com/software/sharescription)

## Inspiration
We all love leaching off other people's Netflix, but hate it when people do it to us. We wanted to solve the age old issue of sharing subscriptions. There's currently no real easy way to split the bills, as you have to rely on someone paying, and everyone else remembering to pay that person back. We aim to change that.

## What it does
People can register via oAuth Facebook, and then add their bills using the simple web interface. They can then decide to share the bill with other people registered on the platform. Once a month, the service automatically splits the bill between everyone and sends an Interac e-Transfer request to everyone who's agreed to pay the bill. It then generates a one-time use virtual debit card number for them to use at the merchant the bill is for.

## How we built it
The project is lots of different pieces all put together. Our APIs are coded in Node.js via Standard Library, we used Flask and Bootstrap to build our website, and bits of PHP to patch up our knowledge gaps. In terms of APIs, we used the Interac e-Transfer API, Marqeta API for generating card numbers.

## Challenges we ran into
> We had quite a few issues with API documentation (and the lack of it) and things not running quite as they should be. *-Jack*

>  "I was responsible for the backend of the project and we decided to use Flask with Python to handle the login and authentication. Although all of us have experience with Python but learning how to use Flask for the first time was definitely a struggle for all of us. Secondly I had spent a fair amount of time trying to set up the virtual environment in order to get the project up and running." *-Jerry*

> "I am not experienced in coding or website building, so I did have to learn and develop my website. At first it was difficult, however, with my team’s constant support I was able to finish the front-end and deploy it in time." *-Sophia*

> "During the hackathon I found two bugs in Standard Library’s online IDE (case-sensitive usernames not working when sharing code and an error with auto-save overwriting the save files) which took some time away as I sat down with the StdLib sponsors to make sure it was all fixed. There’s a limited supply of documentation on the email parser (SendGrid), and I had to use 3rd party websites to understand how to deploy the app."  *-Iyad*

> Oh my, there was a fair share of challenges, not only did we have to deal with the interact documentation, but even then the website tools rarely ever seemed to work. from there fate decided that the language of choice was going to be one I had not ever used before (node.js) but We still got it working in the end. *-Kevin*


## Accomplishments that we're proud of
> I think we've created a really good project, especially considering how many issues with the APIs we ran into during the development of it. *-Jack*

> "Our project was only 30% done when there was 12 hours left, at that time I didn't expect us to be able to finish the project in time for the demo. However, by some miracles we have managed to pull through and get all of our codes together and to produce this amazing web-app that I am proud to stand behind." *-Jerry*

> "I came into this hackathon with very little coding knowledge, but I worked hard and was able to create a visually pleasing minimum viable product, which impressed myself and the team. I am proud that I was able to learn the language quickly and make a good product." *-Sophia*

> "I came in with another team and a different idea. I thought I was set for this hackathon, however, things didn’t go as planned and I had to find a new team during the hackathon. I’m proud that we were able to create a great product during this weekend, with no prior planning, and with half of us meeting for the first time." *-Iyad*

> To be honest the fact that the proper output is coming out from a range of inputs is a real success for me. to be honest my initial expectations were low, but as time progress, I found more to be proud of in my work. Something about specifically working with the Interac API and starting off with feelings of hopelessness, but then creating something makes it all the more better.*-Kevin*


## What we learned
> I learned all about the weird ways that some payment APIs handle authentication - Marqeta's way of sending data and authenticating yourself was really intuitive, but we got there in the end. I also got to learn about how Flask works, and how to handle authentication using it. *-Jack*

> "I learned how to use Flask and how to deploy a project on to Google App Engine in the past 36 hours. I'm hoping to carry on this skill into creating my personal website." *-Jerry*

> "I learnt how to develop my own website using Html and Bootstrap. I was able to learn a new frontend language that expands my skillset." *-Sophia*

> "I learnt how to integrate three different backend languages into one project. I’m surprised at how seamlessly the codes work together (after hours of debugging). Though not my main focus, I was able to float around the team and help the front end and help out with flask." *-Iyad*

> No doubt I've learnt much about the interact API and why I probably won't use it again, or with the Standard Library and only now starting  to understand what an API is. However what the most important thing I've learnt is to embrace the hackathon spirit, and take on tasks that may not be the easiest, but are cool none the less.  *-Kevin*

## What's next for Sharescription
We built the infrastructure for email parsing, but didn't get quite get around to implementing it as a feature. We'd love to make it so people can just forward their bills to the service and have them automatically appear, as this'd make it a lot easier to add new bills.

We'd also like to add support for more subscriptions, and perhaps use machine learning to recognise new services and add them to the platform.

In terms of business, we think partnering with subscription services to show relevant targeted advertising or rewards/discounts to customers using the service would be a really good way to help monetise it.
