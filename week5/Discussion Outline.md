* Introduction
	* Basic linear
	* Widest street or widest margin
	* Support vectors
	* softening the margin for non clean datasets
* Non-linear SVC
	* Polynomial
	* Gaussian
	* Similarity Features
* Moons Example and Summary
	* Moons Example in notebook
	* Pros and Cons

Summary

Pros
* One of the biggest advantages is that once you train and create a model, they are very compact. They only depend on the support vectors to define, so storing the model itself takes very little memory.
* Similarly, making a prediction is also very fast. You just calculate which side of the model your point falls on.
* Since the models depend only on points that are near the margin, SVMs work well with data that is high dimensions. This can be challenging for other algorithms, but for SVMs, they only need to be trained with points near the margin.
* Kernels extend this method to work with a wide variety of data

Cons
* Computation time can be prohibitive for some cases, scaling as O(N^3) at worst or O(N^2) at best. So large training sets can make computing a model difficult
* The results depend strongly on a softening parameter C. This has to be carefully chosen, via cross-validation and can further slow down computation for large data sets.
* When you get a result, you don't get a probabilistic value for that result, unlike other methods (e.g. Naive Bayes). You can try to get a probability by internal cross validation, but this also can make things slow.

In general, used when other simpler, faster, and less fine-tuning models are insufficient. Can take a lot of computational time to train, but have several advantages once trained or for different types of datasets.