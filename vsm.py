__author__ = 'pranavi'
import math
from stemming.porter2 import stem
from nltk.corpus import stopwords

def cosinesimilarity(data1,data2):
    dot = 0
    vecA = 0
    vecB = 0
    for token in data1.keys():
        if data2.has_key(token):
            dot = dot + data1[token]*data2[token]
    for token in data1.keys():
        vecA = vecA + data1[token]*data1[token]
    for token in data2.keys():
        vecB = vecB + data2[token]*data2[token]
    modA = math.sqrt(vecA)
    modB = math.sqrt(vecB)
    print (dot)/(modA*modB)
    pass

def main():
    stop = set(stopwords.words('english'))
    tokens1 = []
    with open("/home/pranavi/Downloads/selected/file1","r") as f1:
        for line in f1:
            tokens1 = tokens1 + [i for i in line.split() if i not in stop]
    tokens2 = []
    with open("/home/pranavi/Downloads/selected/file2","r") as f2:
        for line in f2:
            tokens2 = tokens2 + [i for i in line.split() if i not in stop]


    data1= {}

    for token in tokens1:
        modified= stem(token)

        if modified not in data1:
            data1[modified]=1
        else :
            data1[modified]=data1[modified] + 1


    data2= {}

    for token in tokens2:
        modified= stem(token)

        if modified not in data2:
            data2[modified]=1
        else :
            data2[modified]=data2[modified] + 1

    cosinesimilarity(data1,data2)

if __name__ == "__main__":
    main()