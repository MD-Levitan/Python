'''
Created on Dec 1, 2016

@author: eao
'''
import numpy as np
import matplotlib.pyplot as plt
from NearestNeighbor import *
from Backpropagation import *

print("Hello World:)\n")
ds=DataSet()
util=Utilities()

util.test()

Train, Valid, Test = ds.load_MNIST() 
Train_images=Train[0]
Train_labels=Train[1]
Valid_images=Valid[0]
Valid_labels=Valid[1]

def PlotSample(ARR_im, ARR_lb,num):
    util.exit_with_error("COMPLETE THE FUNCTION ACCORDING TO LABSPEC!!\n")

    return
def AnalyseData(ARR_im):
    util.exit_with_error("COMPLETE THE FUNCTION ACCORDING TO LABSPEC!!\n")
    
    return



# nn=NearestNeighborClass()
# nn.train(Train_images, Train_labels) # train the classifier on the training images and labels
# Labels_predict = nn.predict(Valid_images) # predict labels on the test images
# # and now print the classification accuracy, which is the average number
# # of examples that are correctly predicted (i.e. label matches)
# print 'accuracy: %f' % ( np.mean(Labels_predict == Valid_labels) )

PlotSample(Train_images, Train_labels, 2)

AnalyseData(Train_images)

def prepare_for_backprop(batch_size, Train_images, Train_labels, Valid_images, Valid_labels):
    
    print "Creating data..."
    batched_train_data, batched_train_labels = util.create_batches(Train_images, Train_labels,
                                              batch_size,
                                              create_bit_vector=True)
    batched_valid_data, batched_valid_labels = util.create_batches(Valid_images, Valid_labels,
                                              batch_size,
                                              create_bit_vector=True)
    print "Done!"


    return batched_train_data, batched_train_labels,  batched_valid_data, batched_valid_labels

batch_size=100;

train_data, train_labels, valid_data, valid_labels=prepare_for_backprop(batch_size, Train_images, Train_labels, Valid_images, Valid_labels)

mlp = MultiLayerPerceptron(layer_config=[784, 100, 100, 10], batch_size=batch_size)

mlp.evaluate(train_data, train_labels, valid_data, valid_labels,
             eval_train=True)

print("Done:)\n")
    
