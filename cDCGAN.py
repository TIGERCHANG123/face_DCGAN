import tensorflow as tf
from tensorflow.keras import layers

class generator(tf.keras.Model):
  def __init__(self, noise_shape, img_shape):
    super(generator, self).__init__()
    self.noise_shape = noise_shape
    self.img_shape = img_shape

    self.model = tf.keras.Sequential()
    self.model.add(layers.Dense(4 * 4 * 512, use_bias=False, input_shape=noise_shape))
    self.model.add(layers.BatchNormalization())
    self.model.add(layers.ReLU())
    self.model.add(layers.Reshape((4, 4, 512)))

    self.model.add(layers.Conv2DTranspose(256, (5, 5), strides=2, padding='same', use_bias=False))
    self.model.add(layers.BatchNormalization())
    self.model.add(layers.ReLU())

    self.model.add(layers.Conv2DTranspose(128, (5, 5), strides=2, padding='same', use_bias=False))
    self.model.add(layers.BatchNormalization())
    self.model.add(layers.ReLU())

    self.model.add(layers.Conv2DTranspose(64, (5, 5), strides=2, padding='same', use_bias=False))
    self.model.add(layers.BatchNormalization())
    self.model.add(layers.ReLU())

    self.model.add(layers.Conv2DTranspose(3, (5, 5), strides=1, padding='same', use_bias=False))
    self.model.add(layers.Activation(activation='tanh'))
  def call(self, x):
    return self.model(x)

class discriminator(tf.keras.Model):
  def __init__(self, img_shape=[32, 32, 3]):
    super(discriminator, self).__init__()
    self.img_shape=img_shape

    self.model = tf.keras.Sequential()

    self.model.add(tf.keras.layers.Conv2D(64, kernel_size=5, strides=2, input_shape=self.img_shape, padding="same"))
    self.model.add(tf.keras.layers.LeakyReLU(alpha=0.2))
    self.model.add(tf.keras.layers.Dropout(0.25))

    self.model.add(tf.keras.layers.Conv2D(128, kernel_size=5, strides=2, padding="same"))
    self.model.add(tf.keras.layers.BatchNormalization(momentum=0.8))
    self.model.add(tf.keras.layers.LeakyReLU(alpha=0.2))
    self.model.add(tf.keras.layers.Dropout(0.25))

    self.model.add(tf.keras.layers.Conv2D(256, kernel_size=5, strides=1, padding="same"))
    self.model.add(tf.keras.layers.BatchNormalization(momentum=0.8))
    self.model.add(tf.keras.layers.LeakyReLU(alpha=0.2))
    self.model.add(tf.keras.layers.Dropout(0.25))

    self.model.add(tf.keras.layers.Flatten())
    self.model.add(tf.keras.layers.Dense(1))

  def call(self, x):

    return self.model(x)

def get_gan(noise_shape, img_shape):
    Generator = generator(noise_shape, img_shape)
    Discriminator = discriminator(img_shape)
    gen_name = 'c_dc_gan'
    return Generator, Discriminator, gen_name
