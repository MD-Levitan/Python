'''
Created on Dec 1, 2016

@author:  
Adopted from CS231n
'''

import numpy as np
import progressbar
import sys
import math


def choose_mean(labels):
    """
    Calculates the average value among labels, if average has rest part = 0.5, chooses the nearest value to first
    element in list.
    :param labels: list.
    :return: average value.
    """
    average = sum(labels)/float(len(labels))
    average_rest, average_int = math.modf(average)
    if average_rest < 0.5:
        return int(average_int)
    if average_rest > 0.5:
        return int(average_int+1)
    if average_rest == 0.5:
        if average_int < labels[0]:
            return int(average_int+1)
        return int(average)


def predict_decorator(distance_method):
    def wrapper(self, X, k=1):
        """ X is N x D where each row is an example we wish to predict label for """
        num_test = X.shape[0]
        bar = progressbar.ProgressBar(maxval=num_test, widgets=[progressbar.Bar('=', '[', ']'), ' ',
                                                                progressbar.Percentage()]).start()
        # lets make sure that the output type matches the input type
        Ypred = np.zeros(num_test, dtype=self.ytr.dtype)

        # loop over all test rows
        for i in xrange(num_test):
            # find the nearest training image to the i'th test image
            # using the L1 distance (sum of absolute value differences)
            distances = distance_method(self.xtr - X[i, :])
            min_index_set = []

            for counter in xrange(0, k):
                min_index = np.argmin(distances)  # get the index with smallest distance
                min_index_set.append(min_index)
                distances[min_index] = sys.maxint

            nearest_labels = [self.ytr[val] for val in min_index_set]
            Ypred[i] = choose_mean(nearest_labels)  # predict the label of the nearest example
            bar.update(i + 1)
        bar.finish()

        return Ypred

    return wrapper


class NearestNeighborClass(object):
    def __init__(self):
        self.xtr = None
        self.ytr = None
        pass

    def train(self, x, y):
        """ X is N x D where each row is an example. Y is 1-dimension of size N """
        # the nearest neighbor classifier simply remembers all the training data
        self.xtr = x
        self.ytr = y

    def cross_validation(self, number=3, max_value=100):
        if self.xtr is None or self.ytr is None:
            raise Exception("Error. Training data is missing.")
        length_folder = len(self.xtr) / number
        folders = [self.xtr[length_folder*i:length_folder*i+length_folder] for i in xrange(number-1)]
        label_folders = [self.ytr[length_folder * i:length_folder * i + length_folder] for i in xrange(number-1)]
        folders.append(self.xtr[(number-1)*length_folder:])
        label_folders.append(self.ytr[(number-1)*length_folder:])
        accuracy_values = []
        for k in range(1, max_value):
            accuracy = []
            for folder_counter in xrange(number):
                nn = NearestNeighborClass()
                X = None
                Y = None
                for x in xrange(number):
                    if x != folder_counter:
                        if X is None:
                            X = folders[x]
                            Y = label_folders[x]
                        else:
                            X = np.concatenate((X, folders[x]))
                            Y = np.concatenate((Y, label_folders[x]))

                nn.train(X, Y)
                labels_predict = nn.predictL2(folders[folder_counter], k=k)
                accuracy.append(np.mean(labels_predict == label_folders[folder_counter]))
                print(accuracy)
            accuracy_values.append(accuracy)
        print accuracy_values

    @predict_decorator
    def predictL1(y):
        distances = np.sum(np.abs(y), axis=1)
        return distances

    @predict_decorator
    def predictL2(y):
        distances = np.sqrt(np.sum(np.power(y, 2), axis=1))
        return distances

    # Usual way, but it can be faster than using decorator.
    # def predictL1(self, X, k=1):
    #     """ X is N x D where each row is an example we wish to predict label for """
    #     num_test = X.shape[0]
    #     bar = progressbar.ProgressBar(maxval=num_test,
    #                                   widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()
    #     # lets make sure that the output type matches the input type
    #     Ypred = np.zeros(num_test, dtype=self.ytr.dtype)
    #
    #     # loop over all test rows
    #     for i in xrange(num_test):
    #         # find the nearest training image to the i'th test image
    #         # using the L1 distance (sum of absolute value differences)
    #         distances = np.sum(np.abs(self.xtr - X[i, :]), axis=1)
    #         min_index_set = []
    #
    #         for counter in xrange(0, k):
    #             min_index = np.argmin(distances)  # get the index with smallest distance
    #             min_index_set.append(min_index)
    #             distances[min_index] = sys.maxint
    #
    #         nearest_labels = [self.ytr[val] for val in min_index_set]
    #         Ypred[i] = math.ceil(sum(nearest_labels) / k)  # predict the label of the nearest example
    #         bar.update(i + 1)
    #     bar.finish()
    #
    #     return Ypred
    #
    # def predictL2(self, X, k=1):
    #     """ X is N x D where each row is an example we wish to predict label for """
    #     num_test = X.shape[0]
    #     bar = progressbar.ProgressBar(maxval=num_test,
    #                                   widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()
    #     # lets make sure that the output type matches the input type
    #     Ypred = np.zeros(num_test, dtype=self.ytr.dtype)
    #
    #     # loop over all test rows
    #     for i in xrange(num_test):
    #         # find the nearest training image to the i'th test image
    #         # using the L2 distance
    #         distances = np.sqrt(np.sum(np.power(self.xtr - X[i, :], 2), axis=1))
    #         min_index_set = []
    #
    #         for counter in xrange(0, k):
    #             min_index = np.argmin(distances)  # get the index with smallest distance
    #             min_index_set.append(min_index)
    #             distances[min_index] = sys.maxint
    #
    #         nearest_labels = [self.ytr[val] for val in min_index_set]
    #         Ypred[i] = math.ceil(sum(nearest_labels) / k)  # predict the label of the nearest example
    #         bar.update(i + 1)
    #     bar.finish()
    #
    #     return Ypred
