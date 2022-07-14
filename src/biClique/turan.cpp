#include "turan.h"
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>

void turan::sample(uint64_t T, double rho) {
    std::vector<uint32_t> vs1(g->n1), vs2(g->n1);
    vs1.clear();
    vs2.clear();

    std::vector<uint32_t> degs(g->n2);
    for(uint32_t v = 0; v < g->n2; v++) {
        degs[v] = g->deg2(v);
    }

    // uint64_t upperBoundEdgesForSampling = 0;
    for(uint32_t u = 0; u < g->n1; u++) {
        uint32_t sumDeg = 0;
        for(uint32_t i = g->pU[u]; i < g->pU[u + 1]; i++) {
            uint32_t v = g->e1[i];

            --degs[v];
            sumDeg += degs[v] * (g->pU[u + 1] - i - 1);
        }
        
        if(sumDeg >= rho) {
            vs2.push_back(u);
            // upperBoundEdgesForSampling += g->deg1(u);
        }
        else vs1.push_back(u);
    }

    // for(uint32_t u = 0; u < g->n1; u++) {
    //     uint32_t e = g->deg1(u);
    //     if(e < 4) continue;

    //     for(uint32_t i = g->pU[u]; i < g->pU[u + 1]; i++) {
    //         uint32_t v = g->e1[i];
    //         for(uint32_t j = g->pV[v + 1] - 1; j >= g->pV[v]; j--) {
    //             uint32_t w = g->e2[j];
    //             if(w == u) break;

    //             e++;
    //         }
    //     }

    //     if(e >= rho * g->pU[u]) {
    //         vs1.push_back(u);
    //         // printf("%u\n", u);
    //     }
    //     else {
    //         vs2.push_back(u);
    //     }
    // }

    printf("%d %d\n", int(vs1.size()), int(vs2.size()));
    fflush(stdout);
    exactCount(vs2);

    printf("ans: %.0f\n", ans);
}

void turan::exactCount(std::vector<uint32_t> & nodes) {
    
    collect2HopNeighbors();
    printf("collect 2\n"); fflush(stdout);
#ifdef DEBUG
    H.print();
#endif
    S.resize(g->n2);

    uint32_t maxDegree = 0;
    for(uint32_t u = 0; u < g->n1; u++) {
        maxDegree = std::max(maxDegree, (uint32_t)H.lists[u].size());
    }


    tmpNodes.resize(p + 1);
    tmpNodes[0].resize(g->n1);
    for(int i = 1; i <= p; i++) {
        tmpNodes[i].resize(maxDegree);
    }
    H.nodes.resize(g->n1);
    // H.nodes.resize(p + 1);
    // for(int i = 0; i <= p; i++) {
    //     H.nodes[i].resize(g->n1);
    // }

    H.d.resize(p + 1);
    for(int i = 0; i <= p; i++) {
        H.d[i].resize(g->n1);
    }
    for(uint32_t u = 0; u < g->n1; u++) {
        H.d[0][u] = H.lists[u].size();
    }

    printf("maxDegree of H %u\n", maxDegree);
    fflush(stdout);
    
#ifdef DEBUG
double tmppp = 0;
for(uint32_t v = 0; v < g->n2; v++) {
    if(g->deg2(v) >= 3) {
        tmppp += C[g->deg2(v)][3];
    }
}
printf("3-1 %.2f\n", tmppp);
#endif
    

    ans = 0;

    // layerBasedListing(0, g->n1, g->n2);
    int pH = g->n1, l = 0;
    for(auto u: nodes) {
        printf("%u\n", u); fflush(stdout);
        
        if(H.lists[u].size() < uint32_t(p - l - 1)) {
            continue;
        }

        int pSS = 0;
        if(l == 0) {
            for(uint32_t i = g->pU[u]; i < g->pU[u + 1]; i++) {
                S.changeTo(g->e1[i], pSS++);
            }
        }

        if(pSS < q) continue;
        
        int pHH = 0;

        for(int i = 0; i < H.d[0][u]; i++) {
            auto v = H.lists[u][i];
            if(H.nodes.idx(v) < (uint32_t)pH) {
                H.nodes.changeTo(v, pHH++);
            }
        }

        // if(1 < p)
        for(int i = 0; i < pHH; i++) {
            // uint32_t u = H.nodes[l + 1][i];
            uint32_t u = H.nodes[i];
            int d = H.d[0][u];
            for(int k = 0; k < d; k++) {
                auto v = H.lists[u][k];
                if(H.nodes.idx(v) >= pHH) {
                    std::swap(H.lists[u][k], H.lists[u][--d]);
                    --k;
                }
                // if(H.nodes[l + 1].idx(v) >= pHH) {
                //     std::swap(H.lists[u][k], H.lists[u][--d]);
                //     --k;
                // }
            }
            H.d[1][u] = d;
        }

        layerBasedListing(1, pHH, pSS);
    }

    printf("ans %.2f\n", ans);
    fflush(stdout);
}

void turan::layerBasedListing(int l, int pH, int pS) {
#ifdef DEBUG
printf("l:%d pH:%d pS:%d\n", l, pH, pS);
#endif
    if(l == p) {
        ans += C[pS][q];
        return;
    }

    H.nodes.copy(tmpNodes[l].data(), pH);
// for(int i = 0; i < pH; i++) {
//     printf("%u ", tmpNodes[l][i]);
// }printf("\n");fflush(stdout);

// auto t1 = std::chrono::steady_clock::now();

    for(int j = 0; j < pH; j++) {
// if(l == 0 && j % 200 == 0) {
//     auto t2 = std::chrono::steady_clock::now();
//     auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1);
//     printf("%u, %lld\n", j/10000, (long long)duration.count());fflush(stdout);
//     t1 = t2;
// }

        uint32_t u = tmpNodes[l][j];
        // uint32_t u = H.nodes[l][j];
        // if(l == 0)
        if(H.lists[u].size() < uint32_t(p - l - 1)) {
            continue;
        }

        int pSS = 0;

        for(uint32_t i = g->pU[u]; i < g->pU[u + 1]; i++) {
            if(S.idx(g->e1[i]) < (uint32_t)pS) {
                S.changeTo(g->e1[i], pSS++);
            }
        }
        

        if(pSS < q) continue;
        
        int pHH = 0;

        for(int i = 0; i < H.d[l][u]; i++) {
            auto v = H.lists[u][i];
            if(H.nodes.idx(v) < (uint32_t)pH) {
                H.nodes.changeTo(v, pHH++);
            }
            // if(H.nodes[l].idx(v) < (uint32_t)pH) {
            //     H.nodes[l + 1].changeTo(v, pHH++);
            // }
        }

        if(l + 1 < p)
        for(int i = 0; i < pHH; i++) {
            // uint32_t u = H.nodes[l + 1][i];
            uint32_t u = H.nodes[i];
            int d = H.d[l][u];
            for(int k = 0; k < d; k++) {
                auto v = H.lists[u][k];
                if(H.nodes.idx(v) >= pHH) {
                    std::swap(H.lists[u][k], H.lists[u][--d]);
                    --k;
                }
                // if(H.nodes[l + 1].idx(v) >= pHH) {
                //     std::swap(H.lists[u][k], H.lists[u][--d]);
                //     --k;
                // }
            }
            H.d[l + 1][u] = d;
        }

        layerBasedListing(l + 1, pHH, pSS);
    }
}

void turan::collect2HopNeighbors() {
    H.lists.resize(g->n1);

    std::vector<uint32_t> sum(g->n1);
    std::vector<uint32_t> tmp(g->n1);
    uint32_t l = 0;

// double twotwo = 0;
    for(uint32_t u = 0; u < g->n1; u++) {
        for(uint32_t i = g->pU[u]; i < g->pU[u + 1]; i++) {
            uint32_t v = g->e1[i];
            for(uint32_t j = g->pV[v]; j < g->pV[v + 1]; j++) {
                uint32_t w = g->e2[j];
                if(w > u) {
                    if(sum[w] == 0) tmp[l++] = w;
                    sum[w]++;
                }
            }
        }

        for(uint32_t i = 0; i < l; i++) {
            uint32_t w = tmp[i];
            if(sum[w] >= q) {
// twotwo += C[sum[w]][q];
                H.lists[u].push_back(w);
            }
            sum[w] = 0;
        }
        l = 0;
    }
// printf("2-2 clique %.0f\n", twotwo);
}


void turan::collect2HopNeighborsContainedCDAG() {
    H.contained.resize(g->n1);
    H.lists.resize(g->n1);
    H.nodes.resize(g->n1);
    H.containNodes.resize(g->n1);

    std::vector<uint32_t> sum(g->n1);
    std::vector<uint32_t> tmp(g->n1);
    uint32_t l = 0;

// int twotwo = 0;
    for(uint32_t u = g->n1; u >= 0; u--) {
        H.contained[u] = false;

        for(uint32_t i = g->pU[u]; i < g->pU[u + 1]; i++) {
            uint32_t v = g->e1[i];
            for(uint32_t j = g->pV[v]; j < g->pV[v + 1]; j++) {
                uint32_t w = g->e2[j];
                if(w >= u) {//w < u也可能dw == du
                    if(sum[w] == 0) tmp[l++] = w;
                    sum[w]++;
                }
            }
        }

        for(uint32_t i = 0; i < l; i++) {
            uint32_t w = tmp[i];
            
            if(sum[w] >= (uint32_t)p) {
                if(sum[w] == g->deg1(u)) {
                    H.containNodes[w].push_back(u);
                    H.contained[u] = true;
                }
                
                H.lists[w].push_back(u);
            }
            sum[w] = 0;
        }
        l = 0;
    }
}

bool turan::costEstimate() {
    // std::default_random_engine e(10007);
    // std::uniform_int_distribution<unsigned> chooseU(0, g->n1 - 1);
    // std::uniform_int_distribution<unsigned> chooseV(0, g->n2 - 1);

    std::vector<uint32_t> sum(std::max(g->n1, g->n2));
    std::vector<uint32_t> tmp(std::max(g->n1, g->n2));
    int l = 0;

    uint32_t rd = 100;
    // uint32_t t = rd;
    uint32_t Du = 0, maxDu, rdu = 0;
    double sumDu = 0.0;
    // while(t--) {
        // uint32_t u = chooseU(e);
    for(uint32_t u = 0; u < g->n1; u += rd) {
        rdu++;
        for(uint32_t i = g->pU[u]; i < g->pU[u + 1]; i++) {
            uint32_t v = g->e1[i];
            for(uint32_t j = g->pV[v]; j < g->pV[v + 1]; j++) {
                uint32_t w = g->e2[j];

                if(w > u) {
                    if(sum[w] == 0) tmp[l++] = w;
                    sum[w]++;
                }
            }
        }

        for(int i = 0; i < l; i++) {
            if(sum[tmp[i]] >= (uint32_t)q) {
                Du++;
            }
            sum[tmp[i]] = 0;
        }
        l = 0;

        maxDu = std::max(maxDu, Du);
        sumDu += Du;
    }
    
    uint32_t Dv = 0, maxDv, rdv = 0;
    double sumDv = 0.0;
    // while(t--) {
        // uint32_t v = chooseV(e);
    for(uint32_t v = 0; v < g->n2; v += rd) {
        rdv++;
        for(uint32_t i = g->pV[v]; i < g->pV[v + 1]; i++) {
            uint32_t u = g->e2[i];
    // if(u >= g->n1) {
    //     printf("n2 %u, %u, %u, i %u\n", g->n2, v, u, i);fflush(stdout);
    // }
            for(uint32_t j = g->pU[u]; j < g->pU[u + 1]; j++) {
                uint32_t w = g->e1[j];

                if(w > v) {
                    if(sum[w] == 0) tmp[l++] = w;
                    sum[w]++;
                }
            }
        }

        for(int i = 0; i < l; i++) {
            if(sum[tmp[i]] >= (uint32_t)p) {
                Dv++;
            }
            sum[tmp[i]] = 0;
        }
        l = 0;

        maxDv = std::max(maxDv, Dv);
        sumDv += Dv;
    }
    
    sumDu = sumDu / rdu * g->n1;
    sumDv = sumDv / rdv * g->n2;

    double avgDu = std::max(2.0, sumDu / g->n1);
    double avgDv = std::max(2.0, sumDv / g->n2);

    double costU = pow(avgDu, p - 2) * sumDu;
    double costV = pow(avgDv, q - 2) * sumDv;
    printf("cost:%.2f %.2f, du %u, dv %u\n", costU, costV, Du, Dv);

    return costU > costV;
}

 // void turan::sample(uint64_t T) {
//     std::vector<uint32_t> L(g->m), R(g->m);
//     double sum = 0.0;
//     double ans = 0.0;
// // g->print();
// // printf("pq: %d %d\n", p, q);

//     for(uint32_t u = 0; u < g->n1; u++) {
//         for(uint32_t i = g->pU[u]; i < g->pU[u + 1]; i++) {
//             uint32_t v = g->e1[i];
//             auto st = g->e2.begin() + g->pV[v];
//             auto ed = g->e2.begin() + g->pV[v + 1];
//             uint32_t pL = ed - std::upper_bound(st, ed, u);
//             uint32_t pR = g->pU[u + 1] - i - 1;

//             if(pL < q - 1) continue;
//             if(pR < p - 1) continue;

//             L[i] = pL;
//             R[i] = pR;
//             sum += C[pL][p - 1] * C[pR][q - 1];
// // printf("i %u, u:%u, v:%u, %u %u, %.0f*%.0f=%.0f\n", i, u, v, L[i], R[i],
// //     C[pL][p - 1], C[pR][q - 1], C[pL][p - 1] * C[pR][q - 1]);
//         }
//     }
//     printf("sum %.0f\n", sum);

//     std::random_device rd;
//     std::default_random_engine generator(rd());
//     std::uniform_real_distribution<double> uiDistribution(0, 1);
//     std::vector<uint32_t> stackL(g->maxDv), stackR(g->maxDu);
//     std::vector<bool> visL(g->maxDv), visR(g->maxDu);
//     uint64_t totalCnt = 0, totalT = 0;
//     double rho = 0.5;

//     for(uint32_t u = 0; u < g->n1; u++) {
// // if(u % 1000 == 0) {
// //     printf("%u\n", u);fflush(stdout);
// // }
//         if(g->deg1(u) < q) continue;
//         // int pR = 0;
//         // for(uint32_t i = g->pU[u]; i < g->pU[u + 1]; i++) {
//         //     uint32_t v = g->e1[i];
//         //     candR.changeTo(v, pR++);
//         // }
//         // if(pR < q) continue;
//         int pR = g->deg1(u);

//         for(uint32_t i = g->pU[u]; i < g->pU[u + 1]; i++) {
//             uint32_t v = g->e1[i];
//             // candR.changeTo(v, --pR);
//             // if(pR < q - 1) continue;
//             pR--;
//             int pL = 0;

//             auto st = g->e2.begin() + g->pV[v];
//             auto ed = g->e2.begin() + g->pV[v + 1];
//             auto mid = std::upper_bound(st, ed, u);

//             if(ed - mid + 1 < p) continue;

//             uint32_t j = mid - g->e2.begin();
            
//             for(; j < g->pV[v + 1]; j++) {
//                 uint32_t w = g->e2[j];
//                 candL.changeTo(w, pL++);
//             }
//             assert(pL >= p - 1);

//             uint32_t e = 0;
//             for(int a = 0; a < pL; a++) {
//                 for(int b = i + 1; b < g->pU[u + 1]; b++) {
//                     if(g->connectVU(candL[a], g->e1[b])) {
//                         e++;
//                     }
//                 }
//             }

//             if(e >= rho * pL) {
//                 totalCnt++;
//             }

// //             uint64_t sampleSize = std::ceil(T*(C[pL][p - 1] * C[pR][q - 1]) / sum);
// //             totalT += sampleSize;
// //             uint64_t cnt = 0;
// // // if(u > 1811000) {
// //     // printf("%llu\n", sampleSize);fflush(stdout);
// // // }
// //             for(uint64_t j = 0; j < sampleSize; j++) {
// //                 for(int k = 0; k < p - 1; k++) {
// //                     int x = (pL - k) * uiDistribution(generator);
// //                     while(visL[x]) {
// //                         x = (x + 1) % pL;
// // // printf("there\n"); fflush(stdout);
// //                     }
// //                     visL[x] = true;

// //                     stackL.push_back(x);
// //                 }

// //                 bool f = true;
// //                 for(int k = 0; k < q - 1; k++) {
// //                     int x = (pR - k) * uiDistribution(generator);
// //                     while(visR[x]) {
// //                         x = (x + 1) % pR;
// //                     }
// //                     visR[x] = true;
// //                     stackR.push_back(x);
                    
// //                     for(int h = 0; h < p - 1; h++) {
// //                         if(!g->connectVU(candR[x], candL[stackL[h]])) {
// //                             f = false;
// //                             break;
// //                         }
// //                     }
// //                     if(!f) {
// //                         break;
// //                     }
// //                 }

// //                 if(f) {
// //                     cnt++;
// //                 }

// //                 for(int k = 0; k < stackL.size(); k++) visL[stackL[k]] = false;
// //                 stackL.clear();
// //                 for(int k = 0; k < stackR.size(); k++) visR[stackR[k]] = false;
// //                 stackR.clear();
// //             }

// //             ans += (1.0*cnt / sampleSize) * C[pL][p - 1] * C[pR][q - 1];
// // // printf("i %u, u:%u, v:%u, %.0f*%.0f=%.0f, %llu/%llu=%.2f, ans %.2f\n", i, u, v, 
// // //     C[pL][p - 1], C[pR][q - 1], C[pL][p - 1] * C[pR][q - 1], cnt, sampleSize, (1.0*cnt / sampleSize), ans);
// // // for(int i = 0; i < pL; i++) {
// // //     printf("%u ", candL[i]);
// // // }printf("\n");
// // // for(int i = 0; i < pR; i++) {
// // //     printf("%u ", candR[i]);
// // // }printf("\n");

// //             totalCnt += cnt;
//         }
//     }

//     printf("%llu\n", totalCnt);

//     // printf("%.0f\n", 1.0 * totalCnt / totalT * sum);
//     // printf("%.0f\n", ans);
// } 