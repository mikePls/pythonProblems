# implement a custom decision tree algorithms

import pandas as pd
import numpy as np

# Get test data
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
data = pd.read_csv('dataset_iris.xls')

# implement the Node class
class Node():
    def __init__(self, feature_index=None, threshold=None, left=None, right=None, info_gain=None, value=None):
        """ Class constructor """
        # decision node block
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right
        self.info_gain = info_gain

        # leaf node reference
        self.value = value

# Implement the tree class
class DecisionTreeClassifier:
    def __init__(self, min_samples_split=2, max_depth=2):
        """ Class constructor """

        # initialise root node
        self.root = None

        # termination conditions
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth

    def build_tree(self, dataset, curr_depth=0):
        """ recursive method for building a tree"""
        X, Y = dataset[:,:-1], dataset[:,-1] # considering the dataset includes the target column
        num_samples, num_features = np.shape(X)

        # split the data until termination conditions are met
        if num_samples >= self.min_samples_split and curr_depth >= self.max_depth:
            # search for the best split
            best_split = self.get_best_split(dataset, num_samples, num_features)
            # evaluate information gain
            if best_split["info_gain"]>0:
                # recur left
                left_subtree = self.build_tree(best_split["dataset_left"], curr_depth+1)
                # recur right
                right_subtree = self.build_tree(best_split["dataset_right"], curr_depth+1)
                # return decision node
                return Node(best_split["feature_index"], best_split["threshold"],
                            left_subtree, right_subtree, best_split["info_gain"])

        # compute leaf node
        leaf_value = self.calculate_leaf_value(Y)
        # return leaf node
        return Node(value=leaf_value)

    def get_best_split(self, dataset, num_samples, num_features)->dict:
        """ method that finds and returns the best split in a dataset """

        # dictionary to store the best split
        best_split = {}
        # max info ref
        max_info_gain = -float("inf")

        # loop over all available features
        for feature_index in range(num_features):
            feature_values = dataset[:, feature_index]
            possible_thresholds = np.unique(feature_values)
            # loop all feature values in the data
            for threshold in possible_thresholds:
                # get current split
                dataset_left, dataset_right = self.split(dataset, feature_index, threshold)
                # check that child are not null
                if len(dataset_left)>0 and len(dataset_right)>0:
                    y, left_y, right_y = dataset[:, -1], dataset_left[:, -1], dataset_right[:,-1]
                    # calculate information gain
                    curr_info_gain = self.information_gain(y, left_y, right_y, "gini")
                    # update best split
                    if curr_info_gain>max_info_gain:
                        best_split["feature_index"] = feature_index
                        best_split["threshold"] = threshold
                        best_split["dataset_left"] = dataset_left
                        best_split["dataset_right"] = dataset_right
                        best_split["info_gain"] = curr_info_gain
                        max_info_gain = curr_info_gain

        #return best split
        return best_split

    def split(self, dataset, feature_index, threshold):
        """ Method to split the dataset. Returns a tuple with two arrays of the original data"""

        dataset_left = np.array([row for row in dataset if row[feature_index] <= threshold])
        dataset_right = np.array([row for row in dataset if row[feature_index] > threshold])

        return dataset_left, dataset_right

    def information_gain(self, parent, l_child, r_child, mode="entropy"):
        """ method that computes information gain """

        weight_l = len(l_child) / len(parent)
        weight_r = len(r_child / len(parent))
        if mode == "gini":
            return self.gini_index(parent) - (weight_l*self.gini_index(l_child) + weight_r*self.mini_index(r_child))
        else:
            return self.entropy(parent) - (weight_l*self.entropy(l_child) + weight_r*self.entropy(r_child))

    def entropy(self, y):
        """ method that calculates and returns entropy """

        class_labels = np.unique(y)
        entropy = 0
        for cls in class_labels:
            p_cls = len(y[y == cls]) / len(y)
            entropy += -p_cls * np.log2(p_cls)

        return entropy

    def gini_index(self, y):
        """ method that calculates and returns gini index"""

        class_labels = np.unique(y)
        gini = 0
        for cls in class_labels:
            p_cls = len(y[y == cls]) / len(y)
            gini += -p_cls**2

        return gini

    def calculate_leaf_value(self, y):
        """ method to compute leaf node"""
        y = list(y)
        return max(y, key=y.count)

    def print_tree(self, tree=None, indent=" "):
        """ method to print the tree"""

        if not tree:
            tree = self.root

        if tree.value is not None:
            print(tree.value)
        else:
            print("X_"+str(tree.feature_index), "<=", tree.threshold, "?", tree.info_gain)
            print("%sleft:" % indent, end="")
            self.print_tree(tree.left, indent + indent)
            print("%right:" % indent, end="")
            self.print_tree(tree.right, indent + indent)

    def fit(self, X, Y):
        """ method to train the tree"""

        dataset = np.concatenate((X, Y), axis=1)
        self.root = self.build_tree(dataset)

    def predict(self, X):
        """ method to predict new dataset """
        predictions = [self.make_prediction(x, self.root) for x in X]
        return predictions

    def make_prediction(self, x, tree):
        """ method that predicts a single data point """

        if tree.value is not None:
            return tree.value
        feature_val = x[tree.feature_index]
        if feature_val <= tree.threshold:
            return self.make_prediction(x, tree.left)
        else:
            return self.make_prediction(x, tree.right)


# Train-Test split
from sklearn.model_selection import train_test_split
X = data.iloc[:, :-1]
Y = data.iloc[:, -1].values.reshape(-1,1)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.3)

dt = DecisionTreeClassifier(min_samples_split=3, max_depth=3)
dt.fit(X_train, Y_train)

dt.print_tree()





