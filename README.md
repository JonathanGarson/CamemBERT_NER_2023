# CamemBERT_NER_2023

This repo is part of project developped for the DARES (French Ministry of Labor) and Alpha (French private company) to extract informations about wage variations in public business agreements. To extract we tried several approaches, the one contained in this repo is based on CamemBERT ([French trained BERT](https://huggingface.co/docs/transformers/model_doc/camembert)). All the data, and most importantly the training datas, are available in the repo.

*****

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    |   ├── external       <- External datasets
    │   ├── intermediate   <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   |── raw            <- The original, immutable data dump.
    |   └── text           <- Texts used for training.
    |       ├── docx       <- docx documents
    |       └── txt        <- txt documents used for traning (converted from docx documents).
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details *Not used*
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries *Not used*
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials. *Not used*
    │
    ├── reports            <- Generated analysis as txt, HTML, PDF, LaTeX, etc. Contain informations about model performances. *Not used*
    │   └── figures        <- Generated graphics and figures to be used in reporting. Mostly the matrix of confusion. *Not used*
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │                    predictions *Not used*
    │   │  
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations *Not used*
    │   
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

## How to run the code

To generate the data run the code "download.py" it will automatically retrieve the data from Legifrance website. It is a webscrapping method, then it is subject to potential firewall interuptions, and download the documents in word format in the folder data/text/docx. I discovered latter that most of the data are available through an API, it is probably a faster and safer way of downloading a consequent amount of data.

Once the data are downloaded, use "convert_txt.py" to convert the docx to txt format. Once it is done clean the texts of their eventual accents or wildcard by using "clean_txt.py". The output folder of the cleaned texts is ./data/texts/txt.

To generate those data, please refer to the "prepare_data.ipynb" notebook. First, it will store the txt in csv file and match it with the txt their compagny name and ID. It generates a new dataframe named "text_for_training.csv". After there is a manual part of shortening and labelling data manually. To shorten them we worked collaboratively on Google Sheet, to reduce the texts to 2800 characters, and then imported them on [Label Studio](https://labelstud.io/). This aspect was *crucial* to train [BERT](https://github.com/JonathanGarson/CamemBERT_NER_2023). Though it provided shorter and easier texts to analyse which certainly improved the model performances. Henceforth, I *strongly recommand* working on this aspect of text shortening, for both performance and pratical reasons. Note that the datasets included in the repo allow to train out-of-the-shell a model to do so. I didn't have time to do it, but please feel free to contribute.

We exported from Label Studio three files: data449.json (contains the labelled data), data449F.json (full data, allows to start labelling directly where we stopped in LS), and data_449_cats.csv, csv file containing the labelled data. The notebook prepare_data.ipynb has generated for this a csv file in data/processed named data449_text.csv, it only contains the training txt.

Then to train the models please run the notebook : bert_finetuning_multilabel.ipynb and bert_finetuning_unilabel.ipynb (other textbooks/scripts can do the same, but they are the most efficient ones). It will automatically generate the folder where the models are stored and trained.

We haven't go further so far. I recommand for this job to focus on few shots approaches with LLM. For this please see my [GPT repository](https://github.com/JonathanGarson/gpt_2023)

Thanks for reading, and good luck!
 
<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
