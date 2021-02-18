from Voronoi_set import Voronoi_set
import random

class K_means:
    def __init__(self, ):
        self.voronoi_sets = []
        self.num_clusters = 0
        self.img = None
        self.img_clustered = None

    #Initialize Codebook that include k codevectors
    def codebook_initialization(self,):
        tmp = []
        (rows, cols, _) = self.img.shape

        self.img_clustered = [[0 for i in range(rows)] for j in range(cols)]

        #chose k random points as initial clusters (without replacement)
        for i in range(0,self.num_clusters):

            repeat = False
            while True:
                row = random.randint(0, rows)
                col = random.randint(0, cols)

                #assure without replacement
                for codebook in tmp:
                    if row and col in codebook:
                        repeat = True
                        break

                if repeat == False:
                    break

            codevector = [self.img[row][col][0], self.img[row][col][1], self.img[row][col][2]]
            voronoi_set = Voronoi_set(codevector, i)
            self.voronoi_sets.append(voronoi_set)
            tmp.append([row, col])

    def euclidean_distance(self, p1, p2):
        return pow(pow(p1[0]-p2[0],2) + pow(p1[1]-p2[1],2) + pow(p1[2]-p2[2],2) , 1/2)

    #For each point, find the nearest codevector
    def e_step(self,):
        for i in range(len(self.img_clustered)):
            for j in range(len(self.img_clustered[i])):

                point = []
                point.append(self.img[j][i][0])
                point.append(self.img[j][i][1])
                point.append(self.img[j][i][2])

                dist = float("inf")
                voronoi_set_track = None
                for voronoi_set in self.voronoi_sets:
                    new_dist = self.euclidean_distance(point, voronoi_set.get_codevector())
                    if new_dist < dist :
                        dist = new_dist
                        voronoi_set_track = voronoi_set

                self.img_clustered[i][j] = voronoi_set_track.get_ID()
                voronoi_set_track.add_sum(point)

    #For each codevector, compute the new position (mean).
    #When no codevector changes position, we have come to convergence.
    def m_step(self):
        convergence = True
        for voronoi_set in self.voronoi_sets:
            new_codevector = voronoi_set.get_new_codevector()
            current_codevector = voronoi_set.get_codevector()
            print("current codevector : ",current_codevector)
            print("new codevector : ", new_codevector)
            if new_codevector != current_codevector :
                convergence = False
                voronoi_set.set_codevector(new_codevector)

        return convergence

    #Color for each pixel is equal to the corrispondent codevector.
    def image_clustered(self):
        img = self.img.copy()

        for i in range(len(self.img_clustered)):
            for j in range(len(self.img_clustered[i])):
                for voronoi_set in self.voronoi_sets:
                    if self.img_clustered[i][j] == voronoi_set.get_ID():
                        img[j][i] = voronoi_set.get_codevector()
                        break
        return img

    def clustering(self, img, num_clusters):

        self.num_clusters = num_clusters
        self.img = img
        self.codebook_initialization()

        steps = 1
        while True:
            print("Step number : ",steps)
            self.e_step()
            convergence = self.m_step()
            for voronoi_set in self.voronoi_sets: voronoi_set.reset_sum()
            if convergence:
                break
            steps = steps + 1

        return self.image_clustered()