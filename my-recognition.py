#!/usr/bin/python3
#ai needed
import jetson_inference
import jetson_utils
#get location of the file
import argparse

#parser file name and use google net
parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str)
parser.add_argument("googlenet", type=str)

#get image
img = jetson_utils.loadImage(opt.filename)
#get recogination network
net = jetson_inference.imageNet(googlenet)


#get the index of the class
class_idx = net.Classify(img)
#get the name of the class
class_desc = net.GetClassDesc(class_idx)
print("this is a  "+str(class_desc))