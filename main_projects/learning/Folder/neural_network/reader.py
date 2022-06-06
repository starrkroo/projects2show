#!/usr/bin/env python3

import tensorflow as tf

new_model = tf.keras.models.load_model('epic_num_reader.model')
predictions = new_model.predict([x_test])
print(predictions)
import numpy as np
print(np.argmax(predictions[0])) # x_test[0]
plt.imshow(x_test[0])
plt.show()