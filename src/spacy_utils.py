import json
import numpy as np
import pandas as pd

def import_label_studio_data(filename):
    """
    This function imports the data from Label Studio JSON file and returns the data in the format required for training.
    It also allows selecting specific labels to train the model on with the "label" argument.

    Args:
        filename (str): The path to the JSON file.
        label (list): The list of labels to train the model on.

    Returns:
        A list of tuples containing (text, {"entities": entities}).
    """
    TRAIN_DATA = []
    with open(filename,'rb') as fp:
        training_data = json.load(fp)
    for text in training_data:
        entities = []
        info = text.get('text')
        entities = []
        if text.get('label') is not None:
            list_ = []
            for label in text.get('label'):
                list_.append([label.get('start'), label.get('end')])
            a = np.array(list_)
            overlap_ind =[]
            for i in range(0,len(a[:,0])):
                a_comp = a[i]
                x = np.delete(a, (i), axis=0)
                overlap_flag = any([a_comp[0] in range(j[0], j[1]+1) for j in x])
                if overlap_flag:
                    overlap_ind.append(i)
                    
            for ind, label in enumerate(text.get('label')):
                if ind in overlap_ind:
                    iop=0
                else:
                    if label.get('labels') is not None:
                        entities.append((label.get('start'), label.get('end') ,label.get('labels')[0]))
        TRAIN_DATA.append((info, {"entities" : entities}))
    return TRAIN_DATA

def spacy_to_dataframe(data):
    """
    This function takes the data in the format returned by the import_label_studio_data function and returns a pandas dataframe of two columns: text and label.

    Args:
        data: The data in the format returned by the import_label_studio_data function.

    Returns:
        A pandas dataframe of two columns: text and label.
    """
    text_data = [text for text, _ in data]
    labels = [label for _, label in data]

    df = pd.DataFrame({'text': text_data, 'label': labels})
    return df