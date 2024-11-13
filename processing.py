import numpy as np
import pandas as pd

import tensorflow as tf
from keras.models import load_model

model = tf.keras.models.load_model('lr_model.keras')

def process(a, b, c, d):
    x = pd.DataFrame([np.array([a, b, c, d])])
    res = model.predict(x)
    return float(res[0,0]), float(res[0,1])
