'''
Created on Dec 1, 2016

@author: eao
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import struct
from PIL import Image

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

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

def float_to_RGB(f):
    value= str(float_to_hex(f))[2:]
    lv = len(value)
    if value == "0":
        return (0, 0, 0)
    return tuple(int(value[i:i + lv / 3], 16) for i in range(0, lv, lv / 3))


def PlotSample(ARR_im, ARR_lb,num):
    for i in xrange(len(ARR_im)):
        new_img = Image.new("RGB", (28, 28))
        new_img.putdata([float_to_RGB(c) for c in ARR_im[i]])
        new_img.save("images/out{0}.png".format(i))

    fig = plt.figure()
     
    ax1 = plt.subplot2grid((2, 2), (0, 0))
    ax2 = plt.subplot2grid((2, 2), (0, 1))
    ax3 = plt.subplot2grid((2, 2), (1, 0))
    ax4 = plt.subplot2grid((2, 2), (1, 1))


    i = -1
    jj = [0, 0, 1, 1]
    kk = [0, 1, 0, 1]
    for ax in fig.axes:
        i += 1
        stext = 'ax%d - %d, %d' % (i + 1, jj[i], kk[i])
        ax.text(0.4, 0.5, stext, color='b')
        ax.grid(True)

    save('pic_7_4_1', fmt='png')
    save('pic_7_4_1', fmt='pdf')

    plt.show()

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
    
