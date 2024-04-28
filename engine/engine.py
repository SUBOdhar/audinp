import data.data as dt
import unicode.unicode as uc
import tensorflow as tf
import numpy as np

model =tf.keras.sequential([...])
optimizer =tf.keras.optimizer.SGD()
while True:
    predection=model(x)
    with tf.GradientTape() as tape:
        loss=compute_loss(y,predection)
    grads=tape.gradient(loss,model.trainable_variables)
    optimizer.apply_gradients(zip(grads,model.trainable_variables))