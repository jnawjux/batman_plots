# Batman Plot Generator
#### <em>Fun with Batman plots, using GPT-2</em>

* [Scraping Process (Jupyter Notebook)](https://github.com/jnawjux/batman_plots/blob/master/scraping.ipynb)

* [Model building through Collaboratory (Jupyter Notebook)](https://github.com/jnawjux/batman_plots/blob/master/Finetuning_GPT_2_w_Batman_Plot_summaries.ipynb)

* [Local model testing (Jupyter Notebook)](https://github.com/jnawjux/batman_plots/blob/master/text_generation_local.ipynb)

* [Presentation (Google Slides)](https://docs.google.com/presentation/d/1PKpglW9tL4CzkSmBj6t2vb6LN9jmImE4T9bI4usBroI/edit?usp=sharing)


### Overview
This project builds on some resent work I did with NLP using neural networks, [discussed further here.](https://towardsdatascience.com/the-next-greatest-batman-story-generated-d58cf6753607) As a homage to one of the greatest fictional crime fighters, I explored methods of text generation.  Though previously working with a different set of data and neural network tools, the goal of this was to work with finetuning [GPT-2](https://github.com/openai/gpt-2) to create an interactive tool to play with creating new plots for Batman stories. The finished product I am working on will be a web app where a user can write sentences, have the model fill in a couple sentences, and then pass back off to the user again to continue. This could be used as just a fun creative tool for all ages to experiment with and celebrate the joy of Batman.

### Data used
I scraped the [Batman Wikia on Fandom](https://batman.fandom.com/wiki/Batman_Wiki) for all the plot summaries written for the Batman TV series (1966-1968).  The total corpus is around 15k words long. See the scraping notebook for further information on how it was gathered and processed. After extracting and some cleaning, the corpus was exported to the text file included.

### GPT-2 Fine-tuning process
For fine-tuning, I used the `gpt-2-simple` module, [found here.](https://github.com/minimaxir/gpt-2-simple) This module made working with GPT-2 very intuitive. Due to the amount of processing power needed to build the model, I relied on using Google Collaboratory notebooks to harness their GPU power which added some complication to the workflow, but was incredibly powerful in processing the model efficiently.  

### Testing the model locally
Once created, I was able to download the model to my local repo and test out in a seperate Jupyter notebook.  My ultimate goal being an interactive tool which would repeatedly take input and update with user input, I also began some work in the notebook exploring the type of text manipulation necessary to return only complete sentences and continue to return text with each iteration. 

### Flask web app (in development)
Though I have a model working, I am still developing the web app portion of this project. Currently, the Flask app has the ability to return one new chunk of text from a user input. The model file is fairly large (.5 GB), so it is currently just stored locally, but will work to get it shared remotely so that the project will be able to work as a live website.