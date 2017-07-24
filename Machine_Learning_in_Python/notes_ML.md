# Machine Learning
## Intro to SciKit Learn

#### What is Machine Learning?
	
- The study of computer programs(algorithms) that can learn by example
- ML algorithms can generalize from existing examples of a task
- Examples:
	- Speech Recognition
	- after seeing a training set of labeled images, an image classifier can figure out how to apply labels accurately to new, previously unseen images
	
##### Machine learning models can learn by example (called training data)
- Algorithms learn rules from labelled examples
- A set of labelled examples used for learning is called training data
- The learned rules should also be able to generalize to correctly recognize or predict new examples not in the training set

##### The basic problem of machine learning is to explore how computers can program themselves to perform a task, and to improve their performance automatically as they gain more experience

##### Machine Learning models learn from experience
- Labeled examples( Email spam detection)
- User feedback (clicks on a search page)
- Surrounding environment (self-driving cars)

##### Machine Learning brings together statistics, computer science, and more...
- Statistical methods
	- infer conclusions from data
	- Estimate reliability of predictions
- Computer science
	- large-scale computing architectures
	- Algorithms for capturing, manipulating, indexing, combining, retrieving and performing predictions on data
	- Software pipelines that manage the complexity of multiple subtasks
- Economics, biology, psychology


### Key types of Machine Learning problems
1. #### Supervised machine learning: Learn to predict target values from labelled data.
##### goal is to predict some output variable that's associated with each input item.
	- Classification (target values are discrete classes. output is a **category** a finite number of possibilities such as a fraudulent or not fraudulent prediction for a credit card transaction. Or maybe it's the English word associated with an audio signal for speech recognition. We call this a classification problem within supervised learning, and the function that we learn is called the *classifier*) 
	- Regression (target values are continuous values. The output is **not a category** but **a real valued number**(the amount of time in seconds) *regression function*)

	－ training labels are typically provided by human judges
	
2. #### Unsupervised machine learning:Find structure in unlabeled data
	- Find groups of similar instances in the data(clustering)
	- Finding unusual patterns(outlier detection)
	
#### A basic Machine learning workflow
representation -> evaluation ->optimization -> (may need to go back to)evaluation

1. convert the problem into a representation (that a computer can deal with)

	- convert each input object, which we often call a sample into a set of features that describe the object
	- pick a learning model, typically the type of classifier that you want the system to learn
	
2. choose the type of classifier that;s appropriate for the problem


### Python Tools for Machine Learning
- scikit-learn
- SciPy
- NumPy
- pandas
- matplotlib

#### data used for training cannot be used for test (examples in the data that we use to train the classifier, we can't also use that same fruit sample later as a test sample to also evaluate the classifier. )

##### 75% - 25% split is a pretty standard relative split 

－ capital X, which is typically a two dimensional array or data frame. 
－ lowercase y, which is usually a one dimensional array, or a scalar. 
－ When using the training set and the test set, we'll then use X_train that holds the training instances to train the classifier, and X_test to evaluate the classifier after it's been trained




 