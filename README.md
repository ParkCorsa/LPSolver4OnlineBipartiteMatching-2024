# LPSolver4OnlineBipartiteMatching-2024
## Online Bipartite Matching: with Release Time and Deadline
Initially, there is no vertex in the bipartite graph. At each time, one of the following event happens:

Vertex $x$ releases: all edges between $x$ and previously-released vertices are revealed.
Vertex $x$ expires: vertex $x$ meets its deadline, and it is the last chance to match $x$. It can be shown that you can postpone your matching decision to a deadline, so in other words, if $x$ is currently not matched: you can match $x$ irrevocably with $y\in N(x)$ who is currently not matched, or leave $x$ unmatched forever.
You can assume that the graph is always bipartite, and the vertices are given with their attributions to $U$ or $V$. The target is to maximize the $\sum_{(u,v)\text{ is matched}}1$.

1. Analyze a GREEDY algorithm to the problem: present the algorithm, and justify the competitive ratio.
2. Consider the fractional version of the problem, like what discussed in lecture: you can match fractionally, and the sum of each vertex participating in matching does not exceed 1. Give an analysis of WATER-FILLING like algorithm, whose ratio should be better than 0.5. (You can solve a closed form of the ratio or use an LP solver).
