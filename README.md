# Friends-Script-Generator
Generate a whole Friends using a neural network.

In order to get the data set run the python script `getDataset.py` to get all text from multiple webpages, and write the text to a file.

**Current State:** Training works fine, and generates data after it's done. Currently working to add tensorboard support.

To train a model, run this bat file:

`train.bat` or `python model.py train`

To generate text data, run this bat file:

`generate.bat` or `python model.py generate --weights="model.h5"`


