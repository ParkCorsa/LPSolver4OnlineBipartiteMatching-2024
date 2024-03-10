Q1

Each vertex has a range of liveness, and it can be matched exactly in this range, so if for some edges two endpoints' liveness doesn't overlap, then even optimal can't select the edge, hence we'll assume the liveness of each edge's endpoints overlaps. We propose a greedy algorithm to postpone the decision as much as possible:

When a vertex is about to pass its deadline, we make an attempt of matching, if fail then we don't match it anymore, if succees we add the matching to the final output.

Now we analyze the performance. Consider the following LP for bipartite matching:
$\max \underset{(u,v)\in E}{\sum}x_{uv}$

$\underset{v\in N(u)}{\sum}x_{uv}\le 1, u\in U$

$\underset{u\in N(v)}{\sum}x_{uv}\le 1, v\in V$

$x_{uv}\ge 0, (u,v)\in E$

And its dual:

$\min \underset{i\in U\cup V}{\sum} y_i$

$y_u+y_v\ge 1,(u,v)\in E$

$y_u \ge 0, u\in U\cup V$

Every time our algorithm matching two vertices $u,v$, we let $y_u=y_v=1, x_{uv}=1$. We claim that all the constrictions are satisfied.

$\underset{v\in N(u)}{\sum}x_{uv}\le 1, u\in U$ and $\underset{u\in N(v)}{\sum}x_{uv}\le 1, v\in V$ are satisfied since one vertex is matched with at most 1 edge. $y_u+y_v\ge 1,(u,v)\in E$ are satisfied because if not, then $y_u=y_v=0$, which means the edge is able to be matched, which is contradictory to our algorithm scheme.

Consider the matching, $\texttt{ALG}=\frac12 \texttt{DUAL}\ge \frac12\texttt{DUAL}_{opt}=\frac12\texttt{PRIMAL}_{opt}\ge\frac12\texttt{ALG}_{opt}$

Where the first equation holds clearly according to our algorithm scheme, the first inequation holds by definition, the second equation holds by complementary slackness, the second inequation holds since IP's optimal is a feasible solution of LP.

Hence the competitve ratio of our algorithm is $\frac12$.

Q2

As before, we assign each vertex a water level. When a vertex is about to expire, let the

vertex 'flow' its water via incident edges.

Suppose $u$ expires before $v$, as before, we assume an monotonically increasing function $g$ and let $x_{u,v}+=\Delta,y_u+=(1-g(w_v))\Delta,y_v+=g(w_v)\Delta$, consider the following two cases:

- If $w_u<1$, then $w_v=1$, $\alpha_u+\alpha_v\ge \int_0^1 g(x)dx$

- If $w_u=1$, then $w_v$ can be any value in $[0,1]$, denote the previous water level of $u$ as $w^p_u$. $\alpha_u+\alpha_v\ge(1-w^p_u)(1-g(w_v))+\int_0^{w_v}g(x)dx+\int_0^{w_u^p}g(x)dx$

So now we try to solve:
$\max_{g}\min_{a,b\in[0,1]}\{(1-b)(1-g(a))+\int_0^ag(x)dx+\int_0^bg(x)dx,\int_0^1g(x)dx\}$

Applying the factor revealing LP technique mentioned in class, we transform the problem to an LP:

$\max r$

$r\le (1-\frac in)(1-g_j)+\sum_{k=0}^{i}\frac1ng_{k}+\sum_{k=0}^{j}\frac1ng_{k},\forall\theta,\space i,j\in[n]$

$g_i\le 1,\sum \frac1ng_i\le1$

$g_i\le g_j,\forall i< j$

$g_i\ge0, r\ge0$

We obtain following results with help of an LP solver mentioned in class:

```tex
Optimize a model with 10246402 rows, 6403 columns and 40969603 nonzeros
Model fingerprint: 0xcce2d273
Coefficient statistics:
  Matrix range     [3e-04, 2e+00]
  Objective range  [1e+00, 1e+00]
  Bounds range     [1e+00, 1e+00]
  RHS range        [3e-04, 1e+00]
Presolve removed 1 rows and 1 columns (presolve time = 5s) ...
Presolve removed 3 rows and 3 columns (presolve time = 10s) ...
Presolve removed 3 rows and 3 columns (presolve time = 16s) ...
Presolve removed 3 rows and 3 columns
Presolve time: 43.22s
Presolved: 6401 rows, 10249605 columns, 40966406 nonzeros

Concurrent LP optimizer: primal simplex, dual simplex, and barrier
Showing barrier log only...

Ordering time: 1.69s

Barrier statistics:
 Free vars  : 3198
 AA' NZ     : 1.536e+07
 Factor NZ  : 1.567e+07 (roughly 4.0 GB of memory)
 Factor Ops : 4.568e+10 (roughly 1 second per iteration)
 Threads    : 14

                  Objective                Residual
Iter       Primal          Dual         Primal    Dual     Compl     Time
   0   1.39919409e+04  1.61342003e-03  1.72e+02 4.87e-03  2.97e-02    70s
   1   8.87778282e+03 -1.01056356e-02  1.00e+02 2.14e-01  1.83e-02    73s
   2   8.56776900e+03 -8.85706596e-03  9.55e+01 2.25e-01  1.76e-02    76s
   3   7.74087079e+03 -8.25434546e-03  7.68e+01 2.23e-01  1.58e-02    79s
   4   5.26468417e+03 -9.21978594e-03  4.32e+01 1.68e-01  9.64e-03    83s
   5   4.65021137e+03 -4.29011102e-03  3.55e+01 1.54e-01  8.32e-03    87s
   6   2.81887967e+03 -6.46613160e-03  1.60e+01 1.14e-01  4.55e-03    90s
   7   1.09996787e+03 -4.92230872e-03  2.83e+00 8.69e-02  1.56e-03    96s
   8   8.59136696e+02 -4.35256040e-03  1.88e+00 7.68e-02  1.16e-03   101s
   9   8.57603640e+02 -3.36649116e-03  1.88e+00 5.95e-02  1.08e-03   104s
  10   3.03800296e+02 -1.91813336e-03  4.99e-01 3.39e-02  3.36e-04   107s
  11   4.63096631e+01 -1.42722156e-03  5.01e-02 2.52e-02  4.78e-05   110s
  12   2.25790562e+01 -7.19282710e-04  2.00e-02 1.28e-02  2.14e-05   113s
  13   9.23394141e+00 -3.37502262e-04  7.64e-03 6.02e-03  8.42e-06   116s
  14   8.39665756e+00 -1.82746346e-04  6.91e-03 3.30e-03  7.48e-06   118s
  15   7.02899145e+00 -1.08300710e-04  5.73e-03 1.98e-03  6.20e-06   121s
  16   2.93391269e+00 -5.00452262e-05  2.34e-03 9.69e-04  2.57e-06   124s
  17   1.96529207e+00 -6.57027693e-07  1.54e-03 1.51e-04  1.72e-06   126s
  18   7.50506973e-01  1.25176619e-05  5.76e-04 5.79e-05  6.56e-07   129s
  19   7.79599813e-01  6.02294994e-02  5.01e-04 5.38e-05  6.16e-07   132s
  20   7.09402886e-01  9.47951369e-02  4.11e-04 4.74e-05  5.22e-07   134s
  21   6.99005775e-01  1.48291708e-01  3.70e-04 4.18e-05  4.65e-07   137s
  22   6.86899026e-01  2.29737976e-01  3.15e-04 3.33e-05  3.81e-07   140s
  23   6.66236776e-01  2.66129147e-01  2.60e-04 2.96e-05  3.33e-07   143s
  24   6.60477268e-01  2.89521838e-01  2.41e-04 2.74e-05  3.08e-07   147s
  25   6.47434432e-01  4.44339355e-01  1.72e-04 1.49e-05  1.69e-07   152s
  26   6.33704554e-01  5.62185088e-01  1.17e-04 3.25e-06  5.78e-08   158s
  27   6.27931121e-01  5.72575415e-01  9.72e-05 2.21e-06  4.46e-08   164s
  28   6.18264651e-01  5.79797693e-01  6.87e-05 1.43e-06  3.09e-08   169s
  29   6.07236718e-01  5.84295116e-01  4.35e-05 5.90e-07  1.84e-08   173s
  30   6.06104071e-01  5.84633742e-01  4.11e-05 4.76e-07  1.72e-08   177s
  31   6.03328058e-01  5.84837434e-01  3.53e-05 3.31e-07  1.48e-08   179s
  32   5.97298486e-01  5.85093308e-01  2.29e-05 1.88e-07  9.74e-09   182s
  33   5.95219394e-01  5.85262352e-01  1.88e-05 1.12e-07  7.94e-09   185s
  34   5.93574121e-01  5.85294925e-01  1.56e-05 9.01e-08  6.60e-09   188s
  35   5.92725704e-01  5.85354590e-01  1.39e-05 7.74e-08  5.88e-09   190s
  36   5.91827944e-01  5.85380136e-01  1.21e-05 7.90e-08  5.14e-09   193s
  37   5.89745867e-01  5.85391553e-01  8.15e-06 7.77e-08  3.47e-09   196s
  38   5.88626491e-01  5.85385865e-01  5.98e-06 6.47e-08  2.58e-09   199s
  39   5.87942414e-01  5.85404155e-01  4.70e-06 5.02e-08  2.02e-09   201s
  40   5.87255611e-01  5.85403862e-01  3.42e-06 5.23e-08  1.48e-09   204s
  41   5.86141237e-01  5.85405961e-01  1.34e-06 3.99e-08  5.86e-10   207s
  42   5.86121791e-01  5.85406679e-01  1.31e-06 3.71e-08  5.70e-10   210s
  43   5.85653731e-01  5.85408862e-01  4.44e-07 2.28e-08  1.95e-10   213s
  44   5.85581909e-01  5.85409275e-01  3.13e-07 1.27e-08  1.38e-10   215s
  45   5.85470330e-01  5.85409393e-01  1.10e-07 1.44e-08  4.86e-11   218s
  46   5.85425039e-01  5.85409409e-01  2.80e-08 7.37e-09  1.25e-11   221s
  47   5.85413343e-01  5.85409436e-01  6.98e-09 3.24e-09  3.12e-12   224s
  48   5.85409981e-01  5.85409439e-01  9.68e-10 2.07e-09  4.33e-13   226s
  49   5.85409461e-01  5.85409440e-01  3.82e-11 7.53e-10  1.72e-14   229s
  50   5.85409440e-01  5.85409440e-01  1.45e-12 7.37e-11  6.82e-17   232s

Barrier solved model in 50 iterations and 232.21 seconds (156.11 work units)
Optimal objective 5.85409440e-01

Crossover log...

    1329 DPushes remaining with DInf 0.0000000e+00               235s
    1328 DPushes remaining with DInf 0.0000000e+00               235s
    1209 DPushes remaining with DInf 0.0000000e+00               248s
    1089 DPushes remaining with DInf 0.0000000e+00               262s

Solved with primal simplex
Iteration    Objective       Primal Inf.    Dual Inf.      Time
  339236    5.8540947e-01   0.000000e+00   0.000000e+00    278s

Solved in 339236 iterations and 278.38 seconds (174.47 work units)
Optimal objective  5.854094707e-01
Optimal solution found!
Objective value:  0.5854094707422357
```

By solving the optimization problem by an numerical LP method, we could give a $\ge0.5854094707422357$ competitive ratio.
