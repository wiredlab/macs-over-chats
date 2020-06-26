---
title: Math analysis
permalink: /math
nav_order: 2
---


<script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


<!--
$$\int_1^4 \exp{3}dx$$

$$\frac{1}{2\pi}$$

\\(2\pi \ln asdfa\\)
-->

# Mathematical analysis
{: .no_toc }


## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}



## Pure ALOHA assumptions and analysis

Assumptions:

* All frames have the same length.
* Stations only generates a new frame after a successful transmission ACK.
* The (aggregate) population of stations transmits according to a Poisson distribution.
* Stations transmit a frame when data is ready, regardless of whether the channel is busy or not.
* If a station does not receive an acknoledgement, the frame is retransmitted after a random delay.


Definitions:

$$T$$
: Time required to send one frame

$$G$$
: Poisson distribution mean number of frame arrivals in a certain interval of length $$T$$.


The Poisson distribution is discrete -- the probability of *k* events occurring in a fixed time interval if the events have a constant mean rate and are independent of the time since the last event.


\\(
f_{\text{Poisson}}(k; G)= \Pr(X = k)= \dfrac{G^k e^{-G}}{k!}
\\)




Exponential distribution has mean of $$\mu = 1/\lambda$$

\\(
f_{\text{exp}}(x;\lambda) = \begin{cases}
\lambda e^{-\lambda x} & x \ge 0, \\
0 & x < 0.
\end{cases}
\\)

The Erlang distribution $$(k, \lambda)$$ is the sum of $$k$$ independent exponential variables with mean $$1/\lambda$$ each.
It is a continuous distribution with a mean of $$k/\lambda$$

\\(
f_{\text{Erlang}}(x; k,\mu)=\dfrac{ x^{k-1} e^{-\frac{x}{\mu}} }{\mu^k (k-1)!}\quad\mbox{for }x, \mu \geq 0
\\)

**PROBLEM:** what is probability density function of delays for an individual client that yields a Poisson distribution for number of packets arriving in a time interval $$T$$?



