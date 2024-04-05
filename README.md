# CS399 Module 7: Exploring Neural Word Embeddings with Python

This repo contains the code for my CS 399 course assignment 7. This assignment
involves determining an outlier in a series of words based on a distributed
vector word model - this program was designed using a subset of the GloVe
Common Crawl 840b token 300 dimension model, found here;
https://nlp.stanford.edu/data/glove.840B.300d.zip

Various GloVe models can be found here: https://nlp.stanford.edu/projects/glove/

The repository has 2 options for using this tool. `main.py` contains the
`remove_outliers` function and the loading of the GloVe model. `ui.py` uses
Streamlit to create a web UI for interacting with the tool.

**NOTE:** This repository does not include any text files containing model
data. You will have to download your preferred model and create a text file
containing the model data (without headers) and place it in the file
`model.txt` in the same directory as the scripts.
