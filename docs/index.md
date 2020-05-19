---
title: Home
permalink: /
nav_order: 1
---

# MACs over Chats
{: .no_toc }

2020 Summer

<img src="{{ 'image/logo.svg' | absolute_url }}" width="200"/>


## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


## Summer project goals

## For-credit

### Substance of Project

Study common channel access methods for shared media as used in wireless
communications.
Develop a set of procedures and tools that uses people in chat rooms to simulate the collision and throughput rates of simple protocols.


### Method of Evaluation

Written content for a project website and post-trial reports.




## Learning objectives

**TODO**




You will:

Learn about channel access methods used by wireless and other shared-channel communications systems.


We will: 

* Create a set of procedures and the support tools for people to simulate channel-access using video/audio chat rooms.

* Invite others across the Internet to participate in our trials and provide
  feedback.

* Collect the raw data from trials.

* Create plots summarizing the rates of data transmission and errors.

Goal:  Simulate the throughput versus traffic load performance curves for simple shared-channel access methods by using people instead of code.

The "answers" for these curves are already known, and in most cases have closed form equations for various sets of assumptions.

Why?

Developing an intuition about the advantages and disadvantages for each method can be difficult.

Humans talking to each other in groups naturally use some of the strategies for reliable communication that is used in radio systems.

The only resources needed to conduct this sort of simulation is a set of rules for participants, a clock, and paper/notepad.

Perhaps the simulation works even better over an online chat since it is more difficult to understand multiple speakers at once.

Questions:

Tasks:

Develop an easy to learn and follow set of instructions for participants which emulates each sort of channel access method.

Compare the results of trials against the expected theoretical results.

Create support tools for:

Generating data to send

Recording data during a trial

Assisting participants in following the given protocol

Collecting and analyzing the results of a trial



https://lastminuteengineers.com/nrf24l01-arduino-wireless-communication/



## Background

Communications is the transfer of information.  You may think of using a transmitter to send bits to a receiver.  This transfer may take place over space (here to there) or time (store and retrieve a file) or any combination.  Information is used here in both the technical sense of Shannon's definition of P(x) * log(1/P(x)) and the generic sense of bits and bytes as sent over a radio or stored in a file, though this second category is more properly called symbols.
One last distinction we will make is the "s" at the end of communications.  The difference is that communication is concerned with meaning and content while communications is only concerned with the error-free transfer of bits of information, we don't care what the data actually represents or means.


Figure 1 from A Mathematical Theory of Communication by Claude Shannon.

The small central rectangle in Figure 1 represents the medium over which the signal travels, called the channel.  This channel can be many things, such as the wiring connecting the transmitter to the receiver or the space between two antennas.
In addition to the fundamental theory from Shannon showing what is possible, there i




// vim: tw=0
