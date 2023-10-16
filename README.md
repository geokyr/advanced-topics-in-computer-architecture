# ntua-advanced-computer-architecture

Lab Assignments for the [Advanced Topics in Computer Architecture](https://www.ece.ntua.gr/en/undergraduate/courses/3352) course, during the 8th semester of the School of Electrical and Computer Engineering at the National Technical University of Athens.


## Lab 1 - Memory Hierarchy

The first lab was about utilizing the [PIN tool](https://www.intel.com/content/www/us/en/developer/articles/tool/pin-a-dynamic-binary-instrumentation-tool.html) to explore the impact of memory hierarchy parameters on application performance. The [PARSEC benchmarks](https://parsec.cs.princeton.edu/) were also utilized. The primary goal was to become proficient with the PIN tool and the experimental methods for meaningful conclusions. Additionally, it was essential to develop skills in analyzing memory parameter effects on application performance, yielding valuable insights into memory hierarchy performance. 

The lab assignment included the following tasks:

- Use the PIN tool for performance analysis
- Employ a simulator to emulate application execution on a system with an in-order processor, L1 and L2 caches, TLB, and main memory
- Evaluate various parameters of the memory hierarchy, including L1 cache size, associativity, and block size, L2 cache characteristics, TLB parameters, and prefetching in L2 cache
- Measure performance using IPC (Instructions Per Cycle) and illustrate the changes using graphs

## Lab 2 - Branch Prediction and Predictors

The second lab was about exploring branch prediction and evaluating various predictors for their impact on program execution. The [PIN tool](https://www.intel.com/content/www/us/en/developer/articles/tool/pin-a-dynamic-binary-instrumentation-tool.html) was used again. The primary objective was to delve into branch prediction techniques and assess different predictors' performance in terms of mispredictions and accuracy, enabling you to make informed decisions when selecting a predictor for your computer system.

The lab assignment included the following tasks:

- Use the PIN tool to analyze the impact of different branch prediction systems
- Assess N-bit predictors (1-bit to 4-bit) and compare them using direction MPKI
- Study the effect of predictor bit length while keeping BHT entries constant
- Implement and evaluat BTB with varying sizes and associativities
- Analyze the performance of the Return Address Stack (RAS) for different entry counts
- Compare a range of predictors, including Static AlwaysTaken, Static BTFNT, Pentium-M predictor, Local-History, Global History, Alpha 21264 predictor, and Tournament Hybrid predictors
- Simulated predictor performance on provided benchmarks and presented results graphically

## Lab 3 - Cache Coherence Protocols

The third lab was about cache coherence protocols and performance analysis in multi-core systems using the [Sniper Multicore Simulator](http://snipersim.org/w/The_Sniper_Multi-Core_Simulator) and the [PIN tool](https://www.intel.com/content/www/us/en/developer/articles/tool/pin-a-dynamic-binary-instrumentation-tool.html). This lab aimed to enhance the understanding of cache coherence mechanisms and evaluate the performance of synchronization mechanisms in parallel programming, while providing hands-on experience in optimizing them.

The lab assignment include the following tasks:

- Gain proficiency in using the Sniper Multicore Simulator and the PIN tool
- Implement synchronization mechanisms such as Test-and-Set (TAS) and Test-and-Test-and-Set (TTAS)
- Assess the scalability of synchronization mechanisms by comparing different implementations (TAS_CAS, TAS_TS, TTAS_CAS, TTAS_TS, and Pthread mutex) for various thread counts
- Analyze the impact of grain size on performance and include energy consumption analysis using McPAT
- Investigate the influence of thread topologies (share-all, share-L3, share-nothing) on performance following a similar analysis
