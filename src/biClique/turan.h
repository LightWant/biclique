#ifndef TURAN
#define TURAN

#include "../biGraph/biGraph.hpp"
#include "../tools/linearSet.hpp"

class turan{
private:
    biGraph * g;
    int p, q;

    const int maxD = 100000;
    int minPQ = 100;
    double ** C, *bf3;
    void computeC() {
        int maxPQ = std::max(p, q) + 1;
        C = new double*[maxD];
        bf3 = new double[maxPQ * maxD];
        for(int i = 0; i < maxD; i++) {
            C[i] = bf3 + i * maxPQ;
        }
        C[0][0] = 1;
        C[1][0] = 1;
        C[1][1] = 1;
        for(int i = 2; i < maxD; i++) {
            C[i][0] = 1;
            if(i < maxPQ) C[i][i] = 1;
            for(int j = 1; j < i && j < maxPQ; j++) {
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
            }
        }
    }
    double ans = 0;

    LinearSet candL, candR;

private:
    struct twoHopGraph {
        std::vector<std::vector<uint32_t>> lists;
        std::vector<std::vector<int>> d;
        // std::vector<LinearSet> nodes;
        LinearSet nodes;
        std::vector<bool> contained;
        std::vector<std::vector<uint32_t>> containNodes;

        void print() {
            for(uint32_t i = 0; i < lists.size(); i++) {
                printf("%u:", i);
                for(auto v:lists[i]) printf("%u ", v);
                printf("\n");
            }
        }

        bool contain(uint32_t u, uint32_t v) {
            return std::binary_search(containNodes[u].begin(), containNodes[u].end(), v);
        }
    } H;
    void collect2HopNeighbors();
    void collect2HopNeighborsContained();
    void collect2HopNeighborsContainedCDAG();

    LinearSet S;
    std::vector< std::vector<uint32_t> > tmpNodes;
    void exactCount(std::vector<uint32_t> & nodes);
    void layerBasedListing(int l, int pH, int pS);
    bool costEstimate();

public:
    turan(const std::string & filePath, const std::string & outFilePath, 
        int p = 3, int q = 3):p(p), q(q) {
        minPQ = std::min(p, q);
        g = new biGraph(filePath);

        printf("load graph\n");fflush(stdout);

        if(costEstimate()) {
            g->swapUV();
            std::swap(p, q);
            printf("swap\n");
        }

        computeC();

        candL.resize(g->n1);
        candR.resize(g->n2);
    }

    void sample(uint64_t T, double rho);
};

#endif