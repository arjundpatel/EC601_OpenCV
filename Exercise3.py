import cv2
import numpy as np 


def Add_gaussian_Noise(image,mean,sigma):
    noiseArr = image.copy()
    noiseArr = np.random.normal(mean,sigma,image.shape)
    np.add(image,noiseArr,image,casting="unsafe")
    return;

def Add_salt_pepper_Noise(image,pa,pb):
    row,col,ch=image.shape
    blackspot=row*col*pa
    whitespot=row*col*pb
    for i in range(int(blackspot)):
        image[int(np.random.uniform(0,row))][int(np.random.uniform(0,col))]=0
    for i in range(int(whitespot)):
        image[int(np.random.uniform(0,row))][int(np.random.uniform(0,col))]=255

def main():

    image=cv2.imread('OpenCV_homework/Test_images/baboon.jpg')
    cv2.namedWindow('Original image')
    cv2.imshow('Original',image)

#gaussian_Noise
    noise_img=image.copy()
    mean=0
    sigma=50
    Add_gaussian_Noise(noise_img,mean,sigma)
    cv2.imshow('Gaussian Noise',noise_img)

    noise_dst=noise_img.copy()
    cv2.blur(noise_dst,(3,3))
    cv2.imshow('Box filter',noise_dst)

    noise_dst1=noise_img.copy()
    cv2.GaussianBlur(noise_dst1,(3,3),1.5)
    cv2.imshow('GaussianBlur filter',noise_dst1)

    noise_dst2=noise_img.copy()
    cv2.medianBlur(noise_dst2,3)
    cv2.imshow('Median filter',noise_dst2)


#salt_pepper_Noise
    noise_img2=image.copy()
    pa=0.01
    pb=0.01
    Add_salt_pepper_Noise(noise_img2,pa,pb)
    cv2.imshow("Salt and Peper Noise", noise_img2)

    noise_dst3=noise_img2.copy()
    cv2.blur(noise_dst3,(3,3))
    cv2.imshow('Box filter2',noise_dst3)

    noise_dst4=noise_img2.copy()
    cv2.GaussianBlur(noise_dst4,(3,3),1.5)
    cv2.imshow('GaussianBlur filter2',noise_dst4)

    noise_dst5=noise_img2.copy()
    cv2.medianBlur(noise_dst5,3)
    cv2.imshow('Medianfilter2',noise_dst5)
    
    print('MEAN:',mean)
    print('SIGMA:',sigma)
    print('Pa:',pa)
    print('Pb:',pb)
    print('Best Kernel Size: 3x3')
   
    cv2.waitKey(0)


if __name__ == "__main__":
    main()