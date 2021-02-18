A simple implementation of K-means for image segmentation in python.

# Run the program
To use *run.py* for run the program. In particulary : 
* `python3 run.py --image= img_file --num_clusters= n` 

# Example Results
K-means output examples. </br>
| Lena original  |  Lena after k-means with k=5 |
:---------:|:-----:|
![](https://github.com/Dantekk/Image-Segmentation-using-K-Means-Clustering/blob/main/img/lena.png) | ![](https://github.com/Dantekk/Image-Segmentation-using-K-Means-Clustering/blob/main/img/lena_clustered.jpg)

| Landscape  |  Landscape after k-means with k=7 |
:---------:|:-----:|
![](https://github.com/Dantekk/Image-Segmentation-using-K-Means-Clustering/blob/main/img/p.jpg) | ![](https://github.com/Dantekk/Image-Segmentation-using-K-Means-Clustering/blob/main/img/p_clustered.jpg)

# How to use it
K-means is EM (Expectation–Maximization algorithm) based, for this reason the convergence is guaranteed.
If you want a global minimum you need to run more times the program.

# Important Notes:
* Used Python Version: 3.6.0
* Used OpenCV Version: 4.1.2
