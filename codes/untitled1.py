# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 20:08:03 2017

@author: yuchen
"""

import tensorflow as tf

# Create TensorFlow object called hello_constant
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)