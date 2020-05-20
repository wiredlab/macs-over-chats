---
title: Project
permalink: /project
nav_order: 2
---


<!--
<script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


$$\int_1^4 \exp{3}dx$$

$$\frac{1}{2\pi}$$

\\(2\pi \ln asdfa\\)
-->

# Project description
{: .no_toc }


## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


## Narrative

Wireless technologies are an important part of modern life.
By its nature, wireless communications use radio frequencies that are shared among users in the same area.
Radio transmissions from one device are heard by all others in range, whether or not they were the intended recipient.
This "cocktail party effect" makes it difficult to have many "talkers" at the same time and still be able pick out the conversation from the cacophony of sounds.

When in group conversations, humans naturally adapt to talking in groups by using strategies to either have only one speaker at a time or having a small number of side conversations simultaneously that are able to be understood by the participants.
Similar strategies are used for radio communications, such as merely sending when data is ready, stopping if there are simultaneous transmissions, or repeating information that was garbled.
Because radio transmissions have more available _dimensions_ (time, frequency, coding, ...) than human speech, it can be difficult to quickly gain an intuition about how common *channel access* algorithms work.

New concepts and information is most effectively learned when they can be connected to current knowledge and experience.
Even though wireless communication is invisible and inaudible, it is still _communication_ over a shared medium and therefore suffers from the same "cocktail party effect" as many people talking in a room.
This connection is a potential way to connect this life experience with fundamental concepts in wireless technology.


We know that using video chat rooms make it much more difficult to understand someone when more than one person is speaking.
This is because many of the cues our ear-brain system uses to separate talkers is not available, such as stereo direction of arrival, video/audio timing sync, and listener head movement.
Use this disadvantage as a way to make humans better emulate how radio receivers work: 

> Why not have the people learning the concepts actually **be** the transmitters and receivers?
{: .text-beta .italic}


This raises several questions:

* What strategies to people actually use when talking in large groups?
* Which algorithms for wireless channel access are possible to emulate with people?
* How do the data and error rate curves compare?
* Does participating in a human communication system affect learning the related wireless concepts?


If we create the instructions and an easy (web) way to collect data, then literally anyone with a microphone, speaker, and a web browser can participate.
Social isolation may actually be a _good_ time to develop these questions!


There are several requirements to accomplish this:

* Create a set of procedures and the support tools for people to simulate channel-access using video/audio chat rooms.

* Collect the raw data from trials.

* Create plots summarizing the rates of data transmission and errors.

* Invite others across the Internet to participate in our trials and provide
  feedback.


## Goals

1. Develop a framework for participants to learn about channel access methods by becoming the transmitters and receivers themselves.

1. Simulate the throughput versus traffic load performance curves for simple shared-channel access methods by using people instead of code.

1. Document the procedures so that others can run trials to replicate the results.

1. Build tools to guide participants during a trial session and collect data.

    * Printable templates for manual tracking.
    * Website to manage trials and collect the results.



## Objectives

1. Identify and describe channel access methods including:

    * [ALOHA](https://en.wikipedia.org/wiki/ALOHAnet) pure and slotted
    * [CSMA](https://en.wikipedia.org/wiki/Carrier-sense_multiple_access) and variants

1. Use [GitHub](github.com) for workflow and project management using:

    * Issues
    * Pull requests
    * Web page content using Markdown syntax
    * Version control using `git`

1. Design procedures and instructions for trial participants to implement particular channel access methods.

1. Use tools such as spreadsheets and scripting languages to analyze raw data from trials.

1. Create plots and other graphics showing the performance characteristics of channel access methods such as transmission and error rates.

1. Compare theoretical performance curves with experimental results.

1. Create a website that documents the project for others to perform their own trials.

1. Invite others across the Internet to participate in trials, provide feedback, and collect more data.



## Schedule

### Week 1

* [ ] Obtain a [GitHub](github.com) account and send Prof. White your username for access to the [https://github.com/wiredlab/macs-over-chats repository](https://github.com/wiredlab/macs-over-chats) repository.

* [ ] Read about ALOHA and other channel access methods.

* [ ] Write a draft procedure for emulating radios with packets to send using people.  Post to the GitHub repository.

* [ ] Chat session to try sending/receiving random information to each other.


### Week 2

* [ ] 


### Week 3

* [ ] 


### Week 4

* [ ] 


### Week 5

* [ ] 





## ECE 499 credit info

Optional: register for 1 credit of ECE 499 Undergraduate Research.

**Title:** MACs over Chats

**Substance of Project:**
Study common channel access methods for shared media as used in wireless communications.
Develop a set of procedures and tools that uses people in chat rooms to simulate the collision and throughput rates of simple protocols.

**Method of Evaluation:**
Written content for a project website and post-trial reports.



<!--
 vim: tw=0
 -->
