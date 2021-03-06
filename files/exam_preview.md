# Preview for mid-term exam

### [Poisson process](https://en.wikipedia.org/wiki/Poisson_point_process) (Exponential/Poisson distribution)
* [Prob/Stat review slides](ProbStatsReview.pdf)
* PDF/CDF/expectation of the arrival time t (lambda is arrival rate, i.e., number of events in unit time)?
* How to generate RN for t?
* Credit default swap (CDS)

### Normal RN generation from uniform RN
* [MC method sides](MCmethod.pdf)
* Box-Muller method vs Marsaglia's polar method
* What is the distribution of X_t = B1_t^2 + B2_t^2 (B1_t, B2_t are independent BMs)?
* What is the SDE for X_t and R_t = sqrt(X_t)

### Solving stochastic differential equation (SDE)
* [2016 StoFin Course Note](https://github.com/PHBS/2016.M3.StoFin/blob/master/files/Notes%20Steele.pdf): section 8.5 and 9
* Various solution method from a guess (see below)

### [Ornstein–Uhlenbeck process](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process) and normal model
* Solving SDE (type 1): 
* How to apply forward Euler method from t to t+dt?
* How to derive the distribution at time T? and How do simulate a path from X_s to X_t (s<t)?
* Revisiting normal model for option pricing

### Pricing Asian options
  * [2016 ASP Midterm](2016_ASP_Midterm.pdf) Problem 5, [2016 StoFin Midterm](2016_StoFin_Midterm.pdf) Problem 3

### CEV model (SABR model with no stochastic volatility, i.e. alpha=0)
  * Solving SDE (type 2):
  * [2016 ASP Midterm](2016_ASP_Midterm.pdf) Problem 8, [2016 StoFin Final](2016_StoFin_Final.pdf) problem 5 (CIR)
