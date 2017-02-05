
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math
import struct
from PIL import Image, ImageDraw

from NearestNeighbor import *
from Backpropagation import *

print("Hello World:)\n")
ds = DataSet()
util = Utilities()

util.test()

Train, Valid, Test = ds.load_MNIST() 
Train_images = Train[0]
Train_labels = Train[1]
Valid_images = Valid[0]
Valid_labels = Valid[1]

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

def float_to_RGB(f):
    value= str(float_to_hex(f))[2:]
    lv = len(value)
    if value == "0":
        return (0, 0, 0)
    return tuple(int(value[i:i + lv / 3], 16) for i in range(0, lv, lv / 3))


def PlotSample(ARR_im, ARR_lb, num=None):
    if num is None:
        num = len(ARR_im)
    # for i in xrange(len(ARR_im)):
    #     new_img = Image.new("RGB", (28, 28))
    #     new_img.putdata([float_to_RGB(c) for c in ARR_im[i]])
    #     draw = ImageDraw.Draw(new_img)
    #     draw.text((0, 0), str(ARR_lb[i]))
    #     del draw
    #     new_img.save("images/out{0}.png".format(i))
    # Create folder with images

    figure = plt.figure()
    for i in range(0, num):
        new_img = Image.new("RGB", (28, 28))
        new_img.putdata([float_to_RGB(c) for c in ARR_im[i]])
        draw = ImageDraw.Draw(new_img)
        draw.text((0, 0), str(ARR_lb[i]))
        del draw
        figure.add_subplot(math.floor(math.sqrt(num))+1, math.floor(math.sqrt(num))+1, i+1)
        plt.axis("off")
        plt.imshow(new_img)
    # new_img.save("images/out{0}.png".format(i))
    plt.tight_layout(-1, -1, -7)
    plt.savefig("collage.png", fmt='png')
    #plt.show()
    return

def AnalyseData(ARR_im):
    num = len(ARR_im)
    maxvalue = [max([ARR_im[i][j] for i in xrange(num)]) for j in xrange(len(ARR_im[0]))]
    minvalue = [min([ARR_im[i][j] for i in xrange(num)]) for j in xrange(len(ARR_im[0]))]
    meanvalue = [float(sum([ARR_im[i][j] for i in xrange(num)]))/max(num, 1) for j in xrange(len(ARR_im[0]))]
    stdvalue =  [math.sqrt(sum([(ARR_im[i][j]-meanvalue[j])**2
                                 for i in xrange(num)]))/max(num, 1) for j in xrange(len(ARR_im[0]))]

    new_img = Image.new("RGB", (28, 28))

    new_img.putdata([float_to_RGB(c) for c in minvalue])
    new_img.save("out_minvalue.png".format(i))

    new_img.putdata([float_to_RGB(c) for c in maxvalue])
    new_img.save("out_maxvalue.png".format(i))

    new_img.putdata([float_to_RGB(c) for c in meanvalue])
    new_img.save("out_meanvalue.png".format(i))

    new_img.putdata([float_to_RGB(c) for c in stdvalue])
    new_img.save("out_stdvalue.png".format(i))
    return


nn = NearestNeighborClass()
nn.train(Train_images, Train_labels)  # train the classifier on the training images and labels
nn.cross_validation(number=3, max_value=50)

#Labels_predict = nn.predictL2(Valid_images) # predict labels on the test images
# and now print the classification accuracy, which is the average number
# of examples that are correctly predicted (i.e. label matches)
#print 'accuracy: %f' % (np.mean(Labels_predict == Valid_labels))

#PlotSample(Train_images, Train_labels)

#AnalyseData(Train_images)

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
    
