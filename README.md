# finalCapstone

Final Capstone Project from HyperionDev Bootcamp.

Table of Contents

- [finalCapstone](#finalcapstone)
  * [Introduction](#introduction)
  * [Requirements for the DS (Data Science) T21 Semantic Similarity (NLP)](#requirements-for-the-ds-data-science-t21-semantic-similarity-nlp)
    + [Compulsory Task 1](#compulsory-task-1)
    + [Compulsory Task 2](#compulsory-task-2)
    + [Usage](#usage)
  * [Requirements for the DS (Data Science) T22 Capstone Project](#requirements-for-the-ds-data-science-t22-capstone-project)
    + [Compulsory Task 3](#compulsory-task-3)
    + [Compulsory Task 4](#compulsory-task-4)



## Introduction
This project demonstrates an understanding of Natural Language Processing (NLP) and its applications.
It is divided into two sections: Task 21 and Task 22. The first section focuses on building a system that
can recommend what to watch next based on the word vector similarity of the description of the movies.
The second part is descriptive and focuses on natural language processing applications, such as text 
classification and sentiment analysis.


## Requirements for the DS (Data Science) T21 Semantic Similarity (NLP)

### Compulsory Task 1
Follow these steps:
- Create a file called **semantic.py** and run all the code extracts above.
- Write a note about what you found interesting about the similarities
between cat, monkey and banana and think of an example of your own.
- Run the example file with the simpler language model `en_core_web_sm` and
write a note on what you notice is different from the model `en_core_web_md`.

### Compulsory Task 2
Let us build a system that will tell you what to watch next based on the word
vector similarity of the description of movies.
- Create a file called `watch_next.py`
- Read in the `movies.txt` file. Each separate line is a description of a different
movie.
- Your task is to create a function to return which movies a user would watch
next if they have watched Planet Hulk with the description “Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
planet Sakaar where he is sold into slavery and trained as a gladiator.”
- The function should take in the description as a parameter and return the
title of the most similar movie.

Note: Please make sure when running `watch_next.py`, that the `movies.txt` file is in the same folder.

### Usage

In order to use the `semantic.py` and `watch_next.py` programs, please make sure you have the SpaCy library
installed as well as the specific language models. Please follow the instructions to add SpaCy and english 
language models.

SpaCy is a Python NLP library specifically designed with the goal of being a useful
library for implementing production-ready systems. It is particularly fast and
intuitive, making it a top contender for beginners in NLP. Before doing anything,
you need to have spaCy installed, as well as its English language model.
Type the following commands in the command line to install spaCy:


```bash
pip3 install spacy
```


Please keep in mind that Python 2 is now deprecated. If your system does not
recognise 'python' in the next step or if you have a macOS, please use 'python3'.
To confirm that spacy is properly installed, get into the Python console by typing
the following:
```python
# get into python console
python
import spacy
```

If you receive no error, this means that spaCy was installed correctly!

## Requirements for the DS (Data Science) T22 Capstone Project

### Compulsory Task 3
- In a file called `nlp_1.pdf`, categorize which type of NLP application applies for each of the following use cases:
(Use the categories we have discussed on this boot camp so far)
  - A model that allocates which mail folder an email should be sent to (work, friends, promotions, important), like Gmail’s inbox tabs.
  - A model that helps decide what grade to award to an essay question. This can be used by a university professor who grades a lot of classes or essay competitions.
  - A model that provides assistive technology for doctors to provide their diagnosis. Remember, doctors ask questions, so the model will use the patients’ answers to provide probable diagnosis for the doctor to weigh and make decisions.


### Compulsory Task 4
- Read up on any innovative technology using NLP (by companies such as Google or IBM, for instance) and write a brief summary about the technology, what it achieves/does, and an overview of how it works (250 - 500 words).
To take an example, you may have noticed Gmail’s auto-response suggestions on your incoming emails. If I send an email to your Gmail address asking for an appointment, on opening the mail you would notice Gmail’s automatically suggested response options such as “Yes, that works for me” and “Sorry, I’m not available at that time.”
- Save your answer in a file called `nlp_2.pdf`.
