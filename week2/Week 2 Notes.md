# Week 2 Notes: Probability

## Probability
2 ways to define:
* Frequency
* Degree of Belief (Bayesian)

## Bayes
$P(A|B) = \frac{P(B|A) P(A)}{P(B)}$
posterior = likelihood * prior / evidence

Disjoint parameters if $P(A \text{ and } B) = 0$
So $P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B) = P(A) + P(B)$

Independent parameters if $P(A, B) = P(A)P(B)$
So $P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B) = P(A) + P(B) - P(A)P(B)$

## Chain Rule