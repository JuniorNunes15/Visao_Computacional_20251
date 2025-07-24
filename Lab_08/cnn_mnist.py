"""
Based on:
https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py
"""

import sys
import numpy as np
import keras
from keras import layers
import matplotlib.pyplot as plt


"""
## Prepare the data
"""

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# Load the data and split it between train and test sets
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")


# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

"""
## Build the model
"""

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(8, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Dropout(0.3),
        layers.Conv2D(16, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(name='flatten'),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)


model.summary()
"""
## Train the model
"""

batch_size = 128
epochs = 5
validation_split = 0.1
loss_function = keras.losses.categorical_crossentropy
optimizer = keras.optimizers.Adam()
metrics = ["accuracy", "mse"]



model.compile(loss=loss_function, optimizer=optimizer, metrics=metrics)

history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=validation_split)



"""
## Evaluate the trained model
"""

score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])
print("Test mse:", score[2])


# Função para visualizar as curvas do treinamento
def plot_curves(history):
    plt.figure(figsize=(8, 6))
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.plot(history.history['mse'], label='Training MSE')
    plt.plot(history.history['val_mse'], label='Validation MSE')
    plt.plot(history.history['accuracy'], label='Training accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation accuracy')

    plt.title('Training and Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

# plot_curves(history)

# Função para visualizar previsões
def plot_image(i, predictions_array, true_label, img):
    correct_label, img = np.argmax(true_label[i]), img[i].squeeze()
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img)#, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == correct_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(predicted_label,
                                         100*np.max(predictions_array),
                                         true_label),
                                         color=color)

# Fazer previsões
predictions = model.predict(x_test)

# Visualizar as primeiras 15 imagens, previsões e classes verdadeiras
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions[i], y_test, x_test)
plt.tight_layout()
plt.show()



# Função para visualizar feature maps
def display_feature_maps(seq_model,col_size, layer_index):

    # cria um modelo intermediário
    layer_outputs = [layer.output for layer in model.layers[:layer_index+1]]
    mid_layer_outputs = keras.models.Model(inputs=seq_model.inputs, outputs=layer_outputs)
    mid_layer_outputs.summary()

    # Executa a previsao com o modelo intermediário
    test_image = np.expand_dims(x_test[7], axis=0)
    activations = mid_layer_outputs.predict(test_image)

    activation = activations[layer_index]
    num_filters = activation.shape[-1]
    size = activation.shape[1]
    nrows = num_filters // col_size
    ncols = col_size
    display_grid = np.zeros((size * nrows, size * ncols))

    for i in range(nrows):
        for j in range(ncols):
            x = activation[0, :, :, i * ncols + j]
            x -= x.mean()
            x /= x.std() + 1e-5
            x *= 64
            x += 128
            x = np.clip(x, 0, 255).astype('uint8')
            display_grid[i * size: (i + 1) * size,
            j * size: (j + 1) * size] = x
    scale = 1. / size
    plt.figure(figsize=(scale * display_grid.shape[1],
                        scale * display_grid.shape[0]))
    plt.title(model.layers[layer_index].name)
    plt.grid(False)
    plt.imshow(display_grid, aspect='auto', cmap='viridis')




# Visualizar os feature maps
display_feature_maps(model, col_size=8, layer_index=len(model.layers)-6)

display_feature_maps(model, col_size=8, layer_index=len(model.layers)-5)

display_feature_maps(model, col_size=8, layer_index=len(model.layers)-4)

plt.show()