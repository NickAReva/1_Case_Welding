import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import pandas as pd
import numpy as np

import tensorflow as tf
tf.get_logger().setLevel('ERROR')
import keras
from keras.models import load_model

model_load = load_model('lr_model.h5')

X_test = pd.DataFrame([np.array([46, 141, 10, 80])], columns=['IW', 'IF', 'VW', 'FP'])
print(model_load.predict(X_test))