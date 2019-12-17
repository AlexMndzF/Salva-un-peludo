from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, InputLayer
from keras.models import Model, Sequential,load_model
from keras.callbacks import ModelCheckpoint
from keras import backend as K
from src.costants import BATCH_SIZE,EPOCH,IMG_NUM
from src.photo import createnp


input_img = (220, 220,3)


def build_autoencoder():
    input_img = (220, 220,3)  # adapt this if using `channels_first` image data format
    encoder = Sequential()
    encoder.add(InputLayer(input_img))
    encoder.add(Conv2D(16, (3, 3), activation='relu', padding='same'))
    encoder.add(MaxPooling2D((2, 2), padding='same'))
    encoder.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
    encoder.add(MaxPooling2D((2, 2), padding='same'))
    encoder.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
    encoder.add(MaxPooling2D((2, 2), padding='same'))

     # at this point the representation is (4, 4, 8) i.e. 128-dimensional
    vector_size = (28, 28, 8)
    decoder = Sequential()
    decoder.add(InputLayer(vector_size))
    decoder.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
    decoder.add(UpSampling2D((2, 2)))
    decoder.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
    decoder.add(UpSampling2D((2, 2)))
    decoder.add(Conv2D(16, (3, 3), activation='relu'))
    decoder.add(UpSampling2D((2, 2)))
    decoder.add(Conv2D(3, (3, 3), activation='sigmoid', padding='same'))
    return encoder

X = createnp('Dogs/*/*')
X_train, X_test = X,X

encoder, decoder = build_autoencoder()
inp = Input(input_img)
code = encoder(inp)
reconstruction = decoder(code)

autoencoder = Model(inp,reconstruction)
autoencoder.compile(optimizer='adamax', loss='mse', metrics=['accuracy'])


filepath='Checkpoint_{epoch:02d}_{val_loss:.2f}'
checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

from keras.callbacks import TensorBoard
model = autoencoder.fit_generator(generator=X_train,
                                  steps_per_epoch=IMG_NUM//BATCH_SIZE,
                                  validation_data=X_test,
                                  validation_steps=IMG_NUM//BATCH_SIZE,
                                  epochs=60,
                                  shuffle=True,
                                  use_multiprocessing=True,
                                  callbacks=callbacks_list
                                  )


model = build_autoencoder()
model.load_weights('../Encoder_81.h5')

