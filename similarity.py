import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub  # contains USE4
from numpy.linalg import norm

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4" #Model is imported from this URL
model = hub.load(module_url)
def embed(input):
  return model(input)
def similarity(text1,text2):
    message = [text1,text2]
    message_embeddings = embed(message)
                             
    a = tf.make_ndarray(tf.make_tensor_proto(message_embeddings))
    cos_sim = np.dot(a[0], a[1])/(norm(a[0])*norm(a[1]))             
    return cos_sim