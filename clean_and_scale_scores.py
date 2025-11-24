import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    ### Replace with your own code (begin) ###
    array = np.array(scores, dtype=float)
    
    clippedValues = np.clip(array, min_score, max_score)
    
    scaledValues = (clippedValues - min_score) / (max_score - min_score)

    return scaledValues
    pass
    ### Replace with your own code (end)   ###
