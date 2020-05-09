# CityClassifier
A City Image Classifier that can be accessed through a simple web app.
I worked on this for the [fast.ai course](https://course.fast.ai/index.html) for Lesson 1&2.
Therefore my Notebook is mainly drawn from there.
## How to reproduce
1. To produce the City Dataset, have a look at [this notebook](https://github.com/fastai/course-v3/blob/master/nbs/dl1/lesson2-download.ipynb) and follow sections 'Get a list of URLs' and 'Download images'. It is quite straightforward! And don't worry yet about images being misfits! We will later try to discover bad images in our notebook.
2. Now we can train on the data in the train.ipynb Notebook. The model will be saved in the end as 'export.pkl'.
3. Inference is also done at the end of the train.ipynb Notebook.

## How to use the web app
1. Run `pip install -r requirements.txt` in the terminal to install Flask and fastai.
2. Run `python3 app.py`.
3. Now in order to use the classifier, you can either enter an image URL like this *http://127.0.0.1:5000/classify?url=YOUR_URL_HERE* or you can simply submit the URL in the form at the main page. The page will return probabilities for the cities that are currently represented in the model.
