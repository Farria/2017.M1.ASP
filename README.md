# Applied Stochastic Processes (FIN 514, 2017-18 Module 1)

## Announcements
* Please create your GitHub account for homework/project. Make sure to add your full name (not only ID). Then, click the classroom invidation link I sent to email.

* I set up class mailing list phbs.asp@allmail.net and sent out the first email. __If you're not in the list, please contact me.__ I sent the invitation link for GitHub classroom for uploading homework.

* See this wikipage for [python install](https://github.com/PHBS/2017.M1.ASP/wiki/Python-Resources) and [downloading github desktop install file](https://github.com/PHBS/2017.M1.ASP/wiki/Github-Desktop-Download). The Github install files are now in [CMS for this course](http://cms.phbs.pku.edu.cn/claroline/document/document.php?cidReset=true&cidReq=FIN514).

## Lectures:

* __06 [NEW]__ (09/20 Wed): Stochastic process review. ([Course note]( https://github.com/PHBS/2016.M3.StoFin/blob/master/files/Notes%20Steele.pdf) from stochastic finance course)
* __05__ (09/18 Mon): Implied volatility([Slides](files/ImpVol.pdf), [Py demo](py/ImpliedVolatility.ipynb)), RN generation for correlated normals.
* __04__ (09/14 Thu): Random number generation continued: Box-Muller/Marsaglia method. [Normal model](files/NormalModel.pdf).
* __03__ (09/11 Mon): Python crash course ([Cheatsheet](py/Cheatsheet_Derek_Banas.ipynb), [Black-Scholes implementation](py/BlackScholes_FunctionVsClass.ipynb) in notebook)
* __02__ (09/07 Thu): Scientific computing, Monte Carlo method, Random number generation ([Slides](files/MCmethod.pdf), [Py demo](py/MC_Demo.ipynb)). [Grouping for HW/projects, Software installation]
* __01__ (09/04 Mon): Course overview ([Syllabus](files/syllabus.pdf)), Probability Statistics Review ([Slides](files/ProbStatsReview.pdf))

## Homeworks:

### [NEW] __Set 2__ [Due by 9/29 Fri 11 PM, Group]:

Write code for Black-Scholes-Merton and Normal model: vanilla option (call/put) price, delta, vega, CDF (digital), and price from Monte-Carlo. Implement them using python class. I am going to provide the base code from which you can build your own.

### __Set 1__ [Due by 9.18 Mon 11 PM, Individual]: 

Assume that you keep throwing a coin (H/T probabilitly p/q=1-p) __until you get two heads in a row__? Write a python function to compute this expected number of coin throw using __Monte Carlo__ method. Get one answer by averaging N simulations, and obtain M answers. Get the mean and standard deviation increasing N with fixed M (e.g. say N=100,200,400,800 and M=1000). Run the same experiment for p = 0.5, 0.25, 0.05. __Please comment on your codes so that I can understand what your code does.__

You can find the true answer for p=q=0.5 in the [HW answer](https://github.com/PHBS/2016.M3.StoFin/blob/master/files/StoFin_HW_Solution.pdf) of Stochastic finance course. You can easily generalize for general p/q.



## Classes: 
* Lectures: Monday & Thursday 1:30 – 3:20 PM
* Venue: PHBS Building, Room 313

## Instructor: [Jaehyuk Choi](http://www.jaehyukchoi.net/phbs_en)
* Office: PHBS Building, Room 755
* Phone: 86-755-2603-0568
* Email: jaehyuk@phbs.pku.edu.cn
* Office Hour: Monday & Thursday 11 – 12AM or by appointment

## Course overview: 
Applied Stochastic Processes (ASP) is intended for the students who are
seeking advanced knowledge in stochastic calculus and are eventually interested in the jobs in
financial engineering. As the name indicates, the course will emphasis on applications such as
numerical calculation and programming. On completion of this course, the students will learn
how financial observations (e.g. stock prices and FX rate) are modelled with stochastic
processes and how they can be computed using analytics or computer simulations.

## Prerequisites: 
Undergraduate-level knowledge in probability, statistics, linear algebra and
programming skill (R recommended) are highly recommended. [Stochastic Finance](https://github.com/PHBS/2016.M3.StoFin) (FIN 519),
a year 1 required course for quantitative finance program, is also highly recommended as it
provides theoretical background. However these are not mandatory prerequisites. The
students without these recommended prerequisites are still encouraged to take this course if
interested, but are expected to take extra efforts.

##  Textbooks and Reading Materials
* Monte Carlo Methods in Finance by Peter Jaeckel
* Option Valuation Under Stochastic Volatility by Alan Lewis
* [Stochastic Calculus and Financial Applications](http://www-stat.wharton.upenn.edu/~steele/StochasticCalculus.html) by J. Michael Steele
([Stochastic finance course notes](https://github.com/PHBS/2016.M3.StoFin/blob/master/files/Notes%20Steele.pdf))

## HW/Final project
During the course, students will be asked to 4~5 homeworks in mini-project styles individually or in group:

* Black-Scholes-Merton (lognormal) vs Bachelier (normal) option pricing model
* Spread/Basket (multi-asset) option pricing
* Stochastic volatility model
* Pricing equity-linked-notes (knock-out)

One of the HWs can be chosen as __a final project topic__ and students will do an in-depth research on the topic. Majority of the HW/project will be coding in Python/Jupyter notebook. (Submission of HW/project is uploading the codes to github.)

## Assessment/Grading Details
Attendance 20%, Mid-term Exam 25%, Assignments 25%, Course Project 30%
(Mid-term exam will be taken on Oct 23 in the 7th week. There will be no final exam.)
