#ifndef RAWEDGEPIVOT_H
#define RAWEDGEPIVOT_H
#include <string>
#include <algorithm>
#include <cmath>
#include <random>
#include <unordered_set>
#include <chrono>

#include "../biGraph/biGraph.hpp"
#include "../tools/linearSet.hpp"

class rawEdgePivot {
private:
    const int maxD = 1100000;
    const int maxD2 = 10;

    biGraph * g;

    double ** C, *bf3;
    void computeC() {
        C = new double*[maxD];
        bf3 = new double[maxD2 * maxD];
        for(int i = 0; i < maxD; i++) {
            C[i] = bf3 + i * maxD2;
        }
        C[0][0] = 1;
        C[1][0] = 1;
        C[1][1] = 1;
        for(int i = 2; i < maxD; i++) {
            C[i][0] = 1;
            if(i < maxD2) C[i][i] = 1;
            for(int j = 1; j < i && j < maxD2; j++) {
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
            }
        }
    }

    
    double ans;
private:
    //pivot
    struct treePath {
        int p1, h1, p2, h2;
    };
    std::vector<std::vector<double>> ansAll;
    LinearSet candL, candR;
    std::vector< std::vector<uint32_t> > tmpNodesL, tmpNodesR;

private:
    void pivotCount(int l, int pL, int pR, treePath t);
    
public:
    ~rawEdgePivot() {
        delete [] bf3;
        delete [] C;
    }
    rawEdgePivot(const std::string & filePath, const std::string & outFilePath) {
        computeC();
        g = new biGraph(filePath);
        // g->coreReduction(2, 2);
        printf("load graph\n");fflush(stdout);

        // {
        //     uint32_t maxOutU = 0, maxOutV = 0, maxSum = 0;
        //     uint32_t lBar = 50, rBar = 50;

        //     for(uint32_t u = 0; u < g->n1; u++) {
        //         for(uint32_t i = g->pU[u]; i < g->pU[u + 1]; i++) {
        //             uint32_t v = g->e1[i];

        //             // maxOutU = std::max(maxOutU, pU[u + 1] - i);
        //             auto st = g->e2.begin() + g->pV[v];
        //             auto ed = g->e2.begin() + g->pV[v + 1];
        //             // maxOutV = std::max(uint32_t(ed - std::upper_bound(st, ed, u)), maxOutV);
        //             // maxSum = std::max(
        //             //     maxSum, 
                        
        //             //     g->pU[u + 1] - i + uint32_t(ed - std::upper_bound(st, ed, u))
        //             // );
        //             // printf("%u %u\n", g->pU[u + 1] - i, uint32_t(ed - std::upper_bound(st, ed, u)));
        //             if(g->pU[u + 1] - i >= lBar && uint32_t(ed - std::upper_bound(st, ed, u)) >= rBar) {
        //                 maxSum++;
        //             }
        //         }
        //     }

            // printf("maxOut: %u %u\n", maxOutU, maxOutV);
            // printf("maxD: %u %u\n", maxDu, maxDv);
            // printf("maxSum: %u\n", maxSum);
            // fflush(stdout);
        // }
        // exit(0);
    }
    
    void exactCountMaximalPivot();
    void approximateCountMaximalPivot(double rate);

    void exactCountMaximalPivotV2();
};

#endif