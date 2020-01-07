############################################################################
#                              Cv.hw1                                      #  
#                        Arthor: Wet-ting Cao.                             #   
#                             2019.10.24                                   #
############################################################################

import sys
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsView, QGraphicsScene
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from app import Ui_Dialog
import cv2 as cv
import numpy as np  

import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F
from torch import nn, optim
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle
import math

global pt
pt = []

# MainWindow -> button implementation.
class MainWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # Q1.
        self.disparity.clicked.connect(self.disp)
        
        # Q2.
        self.ncc.clicked.connect(self.NCC)
        
        # Q3.
        self.keypoints.clicked.connect(self.key)
        self.keypoints2.clicked.connect(self.matchKey)
        
    def disp(self):
        imgL = cv.imread('images/imL.png', 0)
        imgR = cv.imread('images/imR.png', 0)
        stereo = cv.StereoBM_create(numDisparities = 64, blockSize = 9)
        dis = stereo.compute(imgL, imgR)
        plt.figure(), plt.title('Without L-R Disparity Check'), plt.axis('off'), plt.imshow(dis, 'gray')
        plt.show()
    
    def NCC(self):
        img_ncc_rgb = cv.imread('images/ncc_img.jpg')
        img_ncc = cv.imread('images/ncc_img.jpg', 0)
        img_tem = cv.imread('images/ncc_template.jpg', 0)
        
        w, h = img_tem.shape[::-1]
        tem = cv.matchTemplate(img_ncc, img_tem, cv.TM_CCORR_NORMED)
        
        threshold = 0.999
        loc = np.where(tem >= threshold)
        
        for p in zip(*loc[::-1]):
            cv.rectangle(img_ncc_rgb, p, (p[0] + w, p[1] + h), 0, 2)
        
        plt.figure()
        plt.subplot(121), plt.imshow(cv.cvtColor(img_ncc_rgb, cv.COLOR_BGR2RGB)), plt.title('ncc_img.jpg'), plt.axis('off')
        plt.subplot(122), plt.imshow(tem, 'gray'), plt.title('Template matching feature'), plt.axis('off')
        plt.show()
               
    def key(self):
    
        def getMatch(matches, ratio):
            mask = [[0, 0] for i in range(len(matches))]
            num = 0
            for i, (m, n) in enumerate(matches):
                if m.distance < ratio * n.distance:
                    mask[i] = [1, 0]
                    num += 1  
                    pt
                if num == 6:
                    break
            return num, mask, good1, good2
        
        img1 = cv.imread('images/Aerial1.jpg', 0)
        img2 = cv.imread('images/Aerial2.jpg', 0)
        
        sift = cv.xfeatures2d.SIFT_create(nfeatures = 200)
        kp1, des1 = sift.detectAndCompute(img1, None)
        kp2, des2 = sift.detectAndCompute(img2, None)
               
        FLANN_INDEX_KDTREE = 0
        indexParams = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        searchParams = dict(checks = 6)
        flann = cv.FlannBasedMatcher(indexParams, searchParams)

        matches = flann.knnMatch(des1, des2, k = 2)
        mask = [[0, 0] for i in range(len(matches))]
        best = 0
        for i, (m, n) in enumerate(matches):
            if m.distance < 0.4 * n.distance:
                mask[i] = [1, 0]
                pt1 = kp1[m.queryIdx].pt
                pt2 = kp2[m.trainIdx].pt
                print(i, pt1, pt2, best)
                if best < 6:
                    cv.circle(img1, (int(pt1[0]), int(pt1[1])), 6, (255, 255, 255), -1)
                    cv.circle(img2, (int(pt2[0]), int(pt2[1])), 6, (255, 255, 255), -1)
                    best += 1
                else:
                    break
                    
        cv.imshow('FeatureAerial1.jpg', img1)
        cv.imshow('FeatureAerial2.jpg', img2)
        
        cv.imwrite('FeatureAerial1.jpg', img1)
        cv.imwrite('FeatureAerial2.jpg', img2)
        
        print('save image')
    
    def matchKey(self):
    
        def getMatch(matches, ratio):
            mask = [[0, 0] for i in range(len(matches))]
            num = 0
            for i, (m, n) in enumerate(matches):
                if m.distance < ratio * n.distance:
                    mask[i] = [1, 0]
                    num += 1    
                if num == 6:
                    break
            return num, mask
            
        img1 = cv.imread('images/Aerial1.jpg', 0)
        img2 = cv.imread('images/Aerial2.jpg', 0)
        
        sift = cv.xfeatures2d.SIFT_create(nfeatures = 200)
        kp1, des1 = sift.detectAndCompute(img1, None)
        kp2, des2 = sift.detectAndCompute(img2, None)
               
        FLANN_INDEX_KDTREE = 0
        indexParams = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        searchParams = dict(checks = 6)
        flann = cv.FlannBasedMatcher(indexParams, searchParams)

        matches = flann.knnMatch(des1, des2, k = 2)
        num, mask = getMatch(matches, 0.4)
        drawParams = dict(matchColor = (0, 255, 0),
                    singlePointColor = (255, 0, 0),
                    matchesMask = mask,
                    flags = cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
                    
        comparisonImage = cv.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **drawParams)
        plt.figure(), plt.imshow(comparisonImage), plt.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
