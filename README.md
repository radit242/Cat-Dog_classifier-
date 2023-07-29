# Cat-Dog_classifier-

This project presents the development of a sophisticated image classifier capable of distinguishing between cats and dogs. Utilizing the robust Sequential Model, a powerful neural network architecture, the deep learning approach enables precise categorization of images. The project explores the potential of the Sequential Model in the domain of computer vision and image classification.

Using the Keras ImageDataGenerator library, images are fetched from the dataset. At a time, 32 images are retrieved, forming a batch of size 32. The image size is then reshaped to 256x256 pixels.

To ensure proper training, the images are scaled down, normalizing their pixel values to the range of 0 to 1. This preprocessing step is crucial for improving model convergence and performance during training.

Keras Sequential model is used for this project. The model architecture consists of convolutional layers with max-pooling, followed by fully connected (dense) layers. The model starts with a 3x3 convolutional layer with 32 filters, using ReLU activation and valid padding. This is followed by a 2x2 max-pooling layer with a stride of 2. The pattern is repeated for two more convolutional layers, each with 64 and 128 filters, respectively. Finally, the model flattens the output and connects to three dense layers with 128, 64, and 1 neuron(s), respectively. The last layer uses a sigmoid activation function to output binary classification predictions.'adam' is used as an optimizer while for loss we considered using 'binary_crossentropy'.

From the figures below we can clearly see the model is overfitting
![image](https://github.com/radit242/Cat-Dog_classifier-/assets/107355525/48fa6b31-dec1-4b6c-878a-b350aec92adc)

![image](https://github.com/radit242/Cat-Dog_classifier-/assets/107355525/b530972c-9daf-4d2c-8b4f-1b690d8ef38b)

Model1 was intoduced. The same model is being used but this time we have added BatchNormalization and Dropout to reduce overfitting 
Over fitting decreased a bit compared to the previous model

![image](https://github.com/radit242/Cat-Dog_classifier-/assets/107355525/a60e5641-8ae3-422d-a90e-c43b90fe4f7e)

![image](https://github.com/radit242/Cat-Dog_classifier-/assets/107355525/b32e0cf1-de27-415d-a840-98b4f9377dcd)

For the final model, the number of filter layers were changed. (10,20,40,80) is being used while dense layers of (80,40,20,10,1) has been applied to reduce overfitting. This tuning helped to reduce overfitting by a large margin.

![image](https://github.com/radit242/Cat-Dog_classifier-/assets/107355525/c33f8fde-ac77-4dd3-a06d-d3b8c5567a7d)

![image](https://github.com/radit242/Cat-Dog_classifier-/assets/107355525/ca0d1df4-907d-4556-aaa3-c6119cf0eb68)

Now the model is able to evaluate prediction cat and dog accurately.

In conclusion, our image classifier successfully demonstrates the power of deep learning and the Sequential Model in image classification tasks. With further exploration and fine-tuning, it holds potential for broader applications in computer vision and object recognition.

website - https://8xfbtwycperxhsndqopngc.streamlit.app/
