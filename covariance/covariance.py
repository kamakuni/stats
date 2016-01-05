import numpy as np

def covariance(data1,data2):
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)
    result = 0
    #for index, value in data1:
    #    result += (value - mean1)(data2[index] - mean2)
    #return result/len(data1)
    return sum((x -mean1) * (y - mean2)for x,y in zip(data1, data2))/len(data1)

def main():
    data1 = np.array([22,25,27,30,35,40,41,45,51,58])
    data2 = np.array([12,15,14,21,21,28,24,29,31,37])
    print(covariance(data1,data2))

main()