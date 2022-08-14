the data comes from the following link: https://www.kaggle.com/rmisra/news-category-dataset. 

Overall the dataset contains over 200K headlines from the Huffington Post between 2012 and 2018. The dataset has six columns that capture the category, headlines, author, link, description, and date the article was published. Overall there are 40 different categories ranging from politics to education. In general the top categories are politics, wellness, and entertainment. For the purposes of this notebook we won't be using the other columnns but it is worthy noting that each date may have more than one headline. More information about the data can be found below this abstract.

The goal of the notebook will be to take the headline column and use topic modeling to recreate the categories. Since we already have hand-labeled category information it will be interesting to see if our models match the ground truth data that we have. To accomplish this we will use non-negative matrix factorization (NMF) to 1) choose the optimal number of topics and 2) associate documents/terms with those topics. NMF is explained in further detail below, but basically it decomposes a document-term matrix into factors by which you can parse document/topics and document/terms from. 

The project will happen in multiple stages consisting of 1) preprocess the text, 2) create a document-term matrix using tf-idf 3) create the NMF model using the doc-term matrix  4) select the optimal number of topics using word2vec and calculate topic coherence 5) based on the optimal k topics print out top terms, documents and compare to original labels for accuracy.

references/inspiration:<br>
-Benedek Rozemberczaki's boosted factorization: https://github.com/benedekrozemberczki/BoostedFactorization <br>
-Derek Greene's excellent github & papers: https://github.com/derekgreene 

![Alt text](/bokeh_plot.png?raw=true "image of corpus SVD")