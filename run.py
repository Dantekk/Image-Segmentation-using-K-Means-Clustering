from K_means import K_means
import argparse
import cv2 as cv

def main():

    parser = argparse.ArgumentParser(description='K-means image')
    parser.add_argument('--image', help='Path to image file.')
    parser.add_argument('--num_clusters', help='Number of clusters.')
    args = parser.parse_args()
    path_image   = args.image
    num_clusters = int(args.num_clusters)

    img = cv.imread(path_image)
    k_means = K_means()
    img_clustered = k_means.clustering(img, num_clusters)
    cv.imshow("Clustered image",img_clustered)


if __name__ == "__main__":
    main()
