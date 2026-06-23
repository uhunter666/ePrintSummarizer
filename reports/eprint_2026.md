# IACR ePrint 论文摘要 - 2026

> 密码学论文自动摘要，来源：[IACR ePrint Archive](https://eprint.iacr.org/2026/)
> 由 [ePrint Summary Tool](https://github.com/lym/ePrintSummary) 生成

---

## 更新: 2026-06-23 08:12

*新增 3 篇论文 (编号 1286--1289)*

### [推荐] [2026/1289] A Toolkit for Succinct Lattice-Based Zero Knowledge Proofs

- **匹配关键字:** lattice, post-quantum

- **作者:** Beatrice Biasioli, Madalina Bolboceanu, Vadim Lyubashevsky, Antonio Merino-Gallardo, Michał Osadnik, Gregor Seiler, Patrick Steuer

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1289) | [PDF](https://eprint.iacr.org/2026/1289.pdf)


> **研究背景:** 近年来，基于格问题的证明系统的开发取得了显著进展，这些系统以极快的速度运行且输出大小小于100KB。然而，在实现证词隐私方面仍存在挑战。
>
> **主要贡献:** 本文通过将Lyubashevsky等人提出的线性大小零知识证明集成到LaBRADOR协议中，首次实现了具有证词隐私的基于格的零知识证明系统。
>
> **达到效果:** 该系统的构建和实施显著提高了证明的效率和实用性，并为其他应用提供了易于使用的库。
>
> **技术梗概:** 通过整合Lyubashevsky等人的线性大小零知识证明技术，本文解决了实现证词隐私的技术挑战。

---
### [2026/1286] Multiple-of Property for Related-Differential Distinguishers on 5-Round AES

- **作者:** Hanbeom Shin, Donggeun Kwon, Byoungjin Seok, Deukjo Hong, Jaechul Sung, Seokhie Hong, Dongjae Lee

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1286) | [PDF](https://eprint.iacr.org/2026/1286.pdf)


> **研究背景:** 该研究探讨了针对5轮AES的依赖差分区分器，结合了一轮相关差分传播与四轮广义零差特征，旨在揭示AES在理想随机置换下的固有结构偏差。
>
> **主要贡献:** 作者证明了满足基本性质的有效四元组数量具有多重形式，并分析了不同配对方式下有效四元组的数量分布特性。
>
> **达到效果:** 研究结果表明，在选择明文设置中，不同的配对方式会影响区分器的性能，n_z=0表现最佳，而n_z=1次之，n_z=2几乎失效。
>
> **技术梗概:** 通过数学证明和统计分析，作者确定了有效四元组数量的具体形式，并比较了不同配对策略下的效果差异。

---
### [2026/1287] Towards a Doubly Efficient IP=PSPACE

- **作者:** Liyan Chen, Matthew M. Hong, Yael Tauman Kalai, Zoe Xi

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1287) | [PDF](https://eprint.iacr.org/2026/1287.pdf)


> **研究背景:** 研究旨在扩展双效交互证明系统的适用范围，以支持更长的时间复杂度问题。
>
> **主要贡献:** 贡献在于提出了一个直接构造的双效交互证明系统，适用于时间复杂度为 \(T(n) = n^{O(\log n)}\) 的PSPACE语言。
>
> **达到效果:** 结果是首次将双效证明系统的适用范围扩展到该时间复杂度区间，并且简化了证明过程。
>
> **技术梗概:** 技术上采用了一种直接构造方法，避免了间接构建批交互证明的步骤，从而简化了整体设计。

---

## 更新: 2026-06-22 08:26

*新增 26 篇论文 (编号 1259--1285)*

### [推荐] [2026/1262] PQ-SMS: A Post-Quantum Sanitizable Multi-Signature Scheme for Satellite PKI

- **匹配关键字:** lattice, post-quantum

- **作者:** Long Wang, Zhaoman Liu, Jing Fan, Yanhong Fan

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1262) | [PDF](https://eprint.iacr.org/2026/1262.pdf)


> **研究背景:** 针对卫星通信系统面临的量子计算威胁和传统公共密钥基础设施操作灵活性差的双重挑战，本文提出了一种后量子可清理多签方案（PQ-SMS），旨在解决证书管理中的效率问题。
>
> **主要贡献:** 该研究贡献了一种新的后量子可清理多签方案，能够在保持根信任完整性的前提下，实现跨层级信任的信任证书适应性调整。
>
> **达到效果:** 通过实验证明，所提出的PQ-SMS方案在不改变原始联盟机构基础签名的情况下，能够轻量级地进行轨道内策略更新，并且性能评估表明该方案能有效绕过交互式重签过程。
>
> **技术梗概:** 基于NIST标准CRYSTALS-Dilithium签名和ISIS基的可变哈希函数实现PQ-SMS方案，并在标准格假设下证明了其安全性。

---
### [推荐] [2026/1263] LCPDTE: Low-Complexity Private Decision Tree Evaluation over Homomorphic Encryption

- **匹配关键字:** homomorphic encryption

- **作者:** Dongjin Park, Gyeongwon Cha, Joon-Woo Lee

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1263) | [PDF](https://eprint.iacr.org/2026/1263.pdf)


> **研究背景:** 随着机器学习即服务（MLaaS）的普及，通过私有推理保护模型查询变得越来越重要。现有的基于同态加密（HE）的私有决策树评估（PDTE）协议在树深度D上的服务器复杂度至少为$O(2^D)$，导致每个树的评估成本随着深度呈指数增长；在梯度提升决策树（GBDT）集成中，这种单个树的成本直接放大。
>
> **主要贡献:** 本文提出了一种基于CKKS方案的非交互式HE-PDTE协议，其端到端复杂度为$O(p\sqrt{2^D})$，这是首次在保持非交互性的同时，从理论上改进了$O(2^D)$对深度D的依赖。
>
> **达到效果:** 实验结果表明，在树深$D=12$时，与FASTER相比，我们的协议将通信量减少了8.38倍，并将运行时间缩短了7.74倍。
>
> **技术梗概:** 我们采用了PROBONITE中的One-Branch-Only（OBO）范式进行比较，并设计了基于Baby-Step Giant-Step的分支选择算法以实现遍历。此外，通过应用按层次顺序的树评估技术来进一步利用GBDT集成结构，部署了批量启动技术。

---
### [推荐] [2026/1264] The Power of Low Rank: Fast CKKS Functional Bootstrapping for High-Precision Lookup Tables

- **匹配关键字:** homomorphic encryption

- **作者:** Zhihao Li, Xuan Shen, Cheng Hong, Ruida Wang, Xianhui Lu, Tao Wei

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1264) | [PDF](https://eprint.iacr.org/2026/1264.pdf)


> **研究背景:** CKKS方案通常被认为仅适用于近似计算，但近期研究引入了功能启动技术以实现高精度查找表评估。然而，现有方法在处理高精度问题时需要对查找表进行重塑，导致运行时间显著增加。
>
> **主要贡献:** 本文提出了一种基于低秩的新型功能启动框架LRMT-FBT，通过奇异值和奇异向量而非直接矩阵乘法来评估查找表，从而将同态乘法成本从O(P)降低到O(r√P)，其中r为矩阵的秩。
>
> **达到效果:** 该方法显著减少了高精度查找表评估的成本，并支持多值和多输入场景的应用。实验结果表明，与现有方案相比，性能大幅提升。
>
> **技术梗概:** 通过分析函数类与奇异值分解的关系，本文提出了一个基于低秩的方法来优化CKKS中的查找表评估过程，利用了函数的结构化特性以减少计算复杂度。

---
### [推荐] [2026/1265] A Billion Hard CRYSTALS: Exploring Practical Aspects of Arithmetic Masking for PQC in Hardware

- **匹配关键字:** post-quantum

- **作者:** Fabian Buschkowski, Niklas Höher, Pascal Sasdrich, Tim Güneysu

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1265) | [PDF](https://eprint.iacr.org/2026/1265.pdf)


> **研究背景:** 针对后量子密码学（PQC）算法在硬件中的实现，由于其复杂性及需要的安全侧信道保护机制，设计高效且安全的硬件架构变得日益耗时且容易出错。
>
> **主要贡献:** 作者提出了一种基于HADES框架的支持布尔和算术遮蔽域的新框架，能够自动在不同类型的秘密共享之间转换，并扩展了性能评估指标以优化PQC方案的实现。
>
> **达到效果:** 该研究通过系统地探索安全高效的非幂次遮蔽随机数生成成本，显著提升了依赖于有限域算术运算的PQC算法在硬件中的性能。
>
> **技术梗概:** 新框架结合了自动预综合设计空间探索和任意阶遮蔽能力，并能够在不同遮蔽域之间无缝转换，同时保持高效的设计流程。

---
### [推荐] [2026/1266] Practical End-to-end Fault Attacks on PERK

- **匹配关键字:** post-quantum

- **作者:** Tanguy Stekke, Durba Chatterjee, Lejla Batina

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1266) | [PDF](https://eprint.iacr.org/2026/1266.pdf)


> **研究背景:** 本文首次展示了针对基于MPC-in-the-Head范式和GGM树扩展的后量子签名方案PERK的实用端到端故障注入攻击，揭示了实现选择对安全假设的影响。
>
> **主要贡献:** 作者提出了两种攻击方法，分别针对GGM树构建的不同阶段，并成功地在优化编译器设置下实现了这些攻击。
>
> **达到效果:** 通过使用时钟触发和电磁故障注入技术，在两个硬件平台上实现了100%和85%的成功率，验证了攻击的有效性。
>
> **技术梗概:** 利用指令跳过引发GGM根的重用，并固定树根以实现确定性的树生成。

---
### [推荐] [2026/1267] Efficient Private Set Intersection and Searchable Encryption using Homomorphic Bloom Filters

- **匹配关键字:** post-quantum, homomorphic encryption, LWE

- **作者:** Anil Kumar Pradhan, Killari Nandini, Harsh Kasyap, Sayantan Mukherjee

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1267) | [PDF](https://eprint.iacr.org/2026/1267.pdf)


> **研究背景:** 现有的加密搜索和私有集合交集（PSI）协议难以在后量子安全性和实际效率之间取得平衡，往往泄露了查询模式或需要深度全同态加密（FHE）电路。
>
> **主要贡献:** 作者提出了一种新的哈希同态布隆过滤器（HBF）框架，该框架将长度为$m$的布隆过滤器直接嵌入到基于RLWE的FHE方案的明文空间中，从而实现浅层同态评估和匹配而无结构泄漏。
>
> **达到效果:** 该方法构建了一个无需旋转或重新加密且不增加额外计算成本的可搜索加密（SE）方案，并提出了一种将每个打包布隆过滤器比较减少为单个密文-明文乘法运算的私有集合交集协议，其成本取决于布隆过滤器长度而非直接元素级比较。
>
> **技术梗概:** 该框架通过限制泄漏到良性数据集维度、可调的假阳性率和其他公共元数据来消除显式模式泄漏。

---
### [推荐] [2026/1272] Parameter-Aware and Instruction-Driven  Dilithium Optimization on AVX2 and NEON

- **匹配关键字:** lattice

- **作者:** Shi Ya, Liu Bingqian, Lu Xianhui, Qian Wenfei, Liu Ying, Wang Kunpeng

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1272) | [PDF](https://eprint.iacr.org/2026/1272.pdf)


> **研究背景:** 本文旨在通过利用Dilithium算法的特性及其底层架构指令集的特点，优化其在AVX2和NEON平台上的性能。
>
> **主要贡献:** 作者提出了针对不同架构的具体优化策略，包括单模16位NTT与多模16位NTT结合矢量化CRT重构等技术。
>
> **达到效果:** 这些优化措施显著提升了Dilithium签名生成的效率，在AVX2平台上减少了7%-8%的时间，在NEON平台上则实现了10%-13%的加速。
>
> **技术梗概:** 通过算法层面的小系数边界和高稀疏性特性，结合指令集特定的操作进行优化，包括NTT、CRT重构以及针对稀疏多项式的高效乘法方法。

---
### [推荐] [2026/1274] Design and Performance Evaluation of Post-Quantum Authentication for Embedded Systems: A Case Study on PIV

- **匹配关键字:** post-quantum

- **作者:** Emmanuelle Dottax, Rina Zeitoun

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1274) | [PDF](https://eprint.iacr.org/2026/1274.pdf)


> **研究背景:** 随着后量子密码学的兴起，安全协议必须进化以抵御量子威胁，同时保持在资源受限设备上的实用性。
>
> **主要贡献:** 研究提出了基于KEM的身份认证方案，并评估了其与基于签名方案相比的成本和性能优势。
>
> **达到效果:** 实验结果显示，基于KEM的身份认证显著减少了执行时间和传输数据量，而基于KEM的后量子安全消息传递相对于经典版本仅增加了适度开销。
>
> **技术梗概:** 研究通过在实际智能卡平台上实现并评估了签名基和KEM基的方案来验证其性能。

---
### [推荐] [2026/1279] BootNet: Homomorphic CNN Inference with Convolution and ReLU Fused in Bootstrapping

- **匹配关键字:** homomorphic encryption

- **作者:** Zhaomin Yang, Chao Niu, Cheng Hong, Tao Wei

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1279) | [PDF](https://eprint.iacr.org/2026/1279.pdf)


> **研究背景:** 研究背景：全同态加密（FHE）允许在保持隐私的前提下进行神经网络推理，但传统的同态卷积、多项式激活近似和CKKS刷新操作导致了高开销。
>
> **主要贡献:** 主要贡献是提出了BootNet框架，将卷积、ReLU激活函数和噪声刷新融合到每次CNN层的单一刷新调用中，实现了端到端的ImageNet推理。
>
> **达到效果:** 达到的效果是在多个ResNet模型上实现了与最先进的Orion相比，端到端延迟减少了67-73%，存储减少了76-90%，同时保持了明文准确性。
>
> **技术梗概:** 技术梗概：通过一系列协同设计技术和优化方法，包括分合刷新调度、改进的RBOOT配置和模型量化方法等，解决了融合操作带来的挑战。

---
### [推荐] [2026/1280] Public Parameters as a First-Class Cost: A Three-Dimensional View of Updatable Vector Commitments, and a Group/Lattice Separation

- **匹配关键字:** lattice

- **作者:** Kefan Liu

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1280) | [PDF](https://eprint.iacr.org/2026/1280.pdf)


> **研究背景:** 研究了可更新向量承诺的更新效率，将其公钥大小P纳入评估维度，构建三维评价体系(S,T,P)。
>
> **主要贡献:** 证明了线性组模型下的位置绑定向量承诺需要至少N大小的公钥，而基于格的同态Merkle树实现了亚线性更新和公钥精简。
>
> **达到效果:** 首次将公钥大小作为与广播更新信息S及每证更新时间T同等重要的评价维度，并证明了组模型与格模型之间的效率差距。
>
> **技术梗概:** 通过系统化现有方案并引入新的三维评估体系，结合理论证明和实例分析展示了不同模型的优劣。

---
### [2026/1259] Collaborative Rate Limiting Nullifier Signaling

- **作者:** Yağmur Gürel, Uğur Şen, Oğuz Yayla

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1259) | [PDF](https://eprint.iacr.org/2026/1259.pdf)


> **研究背景:** 研究背景：现有Rate Limiting Nullifier (RLN)机制虽然能够保护隐私并防止匿名广播网络中的垃圾信息，但每个成员的身份、授权和惩罚单元统一绑定到单一密钥上，这限制了在某些场景下集体发言、共享资源的需求。
>
> **主要贡献:** 主要贡献：提出了Collaborative Rate Limiting Nullifier Signaling (coRLN)协议，允许多个参与者联合注册为一个RLN成员，并通过协作生成身份承诺、每周期评价和广播证明，而不重建整体密钥。
>
> **达到效果:** 达到的效果：实现了集体占用一个叶子节点的会员Merkle树，锁定一个聚合的保证金stake_G，并受到统一速率限制，同时确保在无需重构整体密钥的情况下安全退出。
>
> **技术梗概:** 技术梗概：coRLN使用SPDZ下的加法份额持有全局秘密sk_G；通过协作零知识SNARKs在MPC网络中生成身份承诺、周期评价和广播证明，并提供了协作的提取程序以确保成员安全退出。

---
### [2026/1260] TruthTable: A Verifiable Query Engine

- **作者:** Bharath Namboothiry, Alireza Shirzad, Spencer Solit, Ryan Marcus, Pratyush Mishra

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1260) | [PDF](https://eprint.iacr.org/2026/1260.pdf)


> **研究背景:** TruthTable旨在提供一种可验证的数据库引擎，使证明者能够为验证者生成简洁的证明，以确信其SQL查询在承诺的数据库上的正确执行。
>
> **主要贡献:** 该系统支持广泛的SQL操作，并且能够在TPC-H基准测试中证明17个查询的有效性，同时显著提高了证明效率和保持了竞争力的验证时间和证明大小。
>
> **达到效果:** TruthTable通过优化查询计划以最小化证明时间而非执行时间，并设计新的加密技术和数据库技术来实现高效的小型证明和快速验证。
>
> **技术梗概:** 系统采用了新的多项式表示法来表示数据库表，并设计了用于验证各种关系运算符正确执行的新子协议，同时在查询规划中优化了证明时间。

---
### [2026/1261] RondoMPC: Asynchronous MPC with G.O.D. made More Practical

- **作者:** Xuanji Meng, Zhaoyang Xie, Zhaoxin Yang, Sisi Duan, Aggelos Kiayias

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1261) | [PDF](https://eprint.iacr.org/2026/1261.pdf)


> **研究背景:** 异步多方计算（AMPC）允许一组互不信任的各方在任意网络延迟下安全地计算其私有输入的任何联合函数。G.O.D.属性对于可用性至关重要，但在实践中实现极具挑战性。
>
> **主要贡献:** RondoMPC提出了一个具有G.O.D.属性的一阶段共识AMPC协议，解决了先前协议中由于同步网络假设导致的问题，并且在保持性能的同时实现了更强的实用性。
>
> **达到效果:** 通过构建实用的异步和完备随机双分享（ACRDS）协议，RondoMPC能够在单个阶段内完成共识过程，从而显著降低了延迟并提高了效率。
>
> **技术梗概:** RondoMPC采用了批处理技术来生成多个随机双分享，并支持聚合秘密份额的有效验证，使得这些共享可以用于Beaver三重生成，进一步简化了在线计算过程。

---
### [2026/1268] Decentralized Multi-Authority (Attribute-Based) Traitor Tracing

- **作者:** Pratish Datta, Robert Schädlich, Erkan Tairi

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1268) | [PDF](https://eprint.iacr.org/2026/1268.pdf)


> **研究背景:** 该研究旨在提出一种去中心化的多权威（属性基）盗版追踪方案，通过分散的多个独立机构来实现盗版者的识别能力，避免单一实体的信任风险。
>
> **主要贡献:** 研究提出了MA-AB-TT方案，结合了分布式追踪和基于属性的加密中的去中心化访问控制，支持多种类型的追踪策略，并首次在标准假设下构建了任意单调访问结构下的MA-AB-TT方案。
>
> **达到效果:** 该方案实现了对用户行为的有效追踪而不依赖于单一实体的信任，提高了系统的安全性和隐私性。同时，构造证明了其在随机预言模型下的自适应安全性。
>
> **技术梗概:** 研究基于矩阵决策性Diffie-Hellman (MDDH) 假设，在素数阶配对群中构建了MA-AB-TT方案，并确保了参数独立于用户数量。

---
### [2026/1270] Actively Secure MPC with $O(|C|)$ Computation and Communication via CRT

- **作者:** Alexander Bienstock, Daniel Escudero, Antigoni Polychroniadou

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1270) | [PDF](https://eprint.iacr.org/2026/1270.pdf)


> **研究背景:** 该研究致力于在恶意主动攻击者存在的情况下，实现安全多方计算(MPC)协议，同时保持低通信和计算复杂度。
>
> **主要贡献:** 论文提出了基于中国剩余定理的新型秘密共享技术，实现了在超过一半节点可能被恶意控制的情况下，仍能以线性计算和通信复杂度进行安全计算。
>
> **达到效果:** 研究成功地将通信和计算复杂度都降低至O(|C|)，同时确保了协议的安全性和有效性。
>
> **技术梗概:** 通过引入基于中国剩余定理的秘密共享方法，该工作实现了在恶意攻击者存在的情况下，仍能以线性复杂度进行安全多方计算。

---
### [2026/1271] Boosting Efficiency and Security in Arithmetization-Oriented Hashing for Zero-Knowledge Proof Systems

- **作者:** Stefano Trevisani, Elena Andreeva, Rishiraj Bhattacharyya, Arnab Roy

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1271) | [PDF](https://eprint.iacr.org/2026/1271.pdf)


> **研究背景:** 研究背景：在零知识证明系统中，如ZK-SNARK和STARK框架，矢量承诺方案的核心组件是压缩函数。Arithmetization-Oriented (AO) 压缩函数通过减少代数电路中的乘法复杂性，在效率上优于位导向设计。然而，现有的AO压缩函数大多基于Sponge模式构建，缺乏安全性和可组合性的正式证明。
>
> **主要贡献:** 主要贡献：作者提出了PA和PAX两种新型的基于置换的AO压缩模式，并证明了它们在碰撞抗性和预象抗性方面达到最优。PAX进一步被证明与随机预言机不可区分，增强了其安全性和可组合性保证。
>
> **达到效果:** 达到的效果：通过PA(X)模式，研究统一并扩展了几种最近提出的但缺乏正式安全性证明的模式描述，如Jive和Trunc，并且这些模式在Anemoi和Poseidon2的设计中被使用。实验表明，基于PA(X)模式的安全哈希函数实例化是可行的。
>
> **技术梗概:** 技术梗概：作者采用Permutation with feedforward Addition（PA）和其扩展PAX来构建AO压缩模式，并通过形式验证证明了这些模式在安全性上的优势，同时展示了如何利用适当的方法扩展输入长度以实现安全哈希函数实例化。

---
### [2026/1273] Achieving Tight Space-Time Tradeoff and Practical Performance in Preprocessing PIR with Multi-level Recursion

- **作者:** Chang Shi, Bo Peng, Zhechen Li, Cheng Hong, Mingxun Zhou

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1273) | [PDF](https://eprint.iacr.org/2026/1273.pdf)


> **研究背景:** 研究背景：客户端特定预处理PIR支持在离线阶段准备客户端特定提示后，实现子线性在线私密查询。然而，现有方案要么在客户端存储上有所不足，要么依赖于复杂的提示管理机制并导致高实际成本。
>
> **主要贡献:** 主要贡献是提出了一种名为Multi-level PIR的预处理PIR方案，该方案仅使用简单的随机集组件就达到了紧致的空间-时间权衡，并且具有竞争力的实际性能。
>
> **达到效果:** 达到的效果是在客户端存储和在线成本方面实现了$O(\sqrt{n})$的预期值，同时通过减少查询无关的失败概率来降低整体失败概率至可忽略水平。与Piano和S3PIR相比，它在客户端空间上减少了9-20倍；与Balanced PIR相比，在预处理时间和在线通信方面分别减少了约8-45倍和5-67倍。
>
> **技术梗概:** 技术梗概：Multi-level PIR方案采用了多层次的组合结构，早期层次允许以可察觉的概率失败，并在这些查询无关的失败发生时仅调用后续层次。这种‘瀑布’结构将整体失败概率降至可忽略水平，同时保持了预期的在线成本和客户端存储。

---
### [2026/1275] The Indifferentiability of the Duplex and its Practical Applications

- **作者:** Jean Paul Degabriele, Marc Fischlin, Jérôme Govinden

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1275) | [PDF](https://eprint.iacr.org/2026/1275.pdf)


> **研究背景:** Duplex构造由Bertoni等人引入，是一种基于置换的密码学工具，能够实现多种加密对象。STROBE协议框架完全依赖于Duplex及其丰富的函数调用，证明了其广泛应用性。
>
> **主要贡献:** 研究主要贡献在于证明了标准Duplex从在线随机Oracle的角度来看是不可区分的，但全状态Duplex不满足这一性质。
>
> **达到效果:** 该理论成果为Duplex在各种场景下的安全性提供了坚实的基础，并特别适用于基于Duplex的AEAD方案SpongeWrap对抗密钥相关消息输入的安全性。
>
> **技术梗概:** 通过建立从在线随机Oracle的角度来看标准Duplex是不可区分的定理，利用了不可区分性的强大功能来证明SpongeWrap的安全性。

---
### [2026/1276] Forget-me-not Trees: Mass-scale Auditable Key Transparency from Hash Functions

- **作者:** Gabriel Kaptchuk

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1276) | [PDF](https://eprint.iacr.org/2026/1276.pdf)


> **研究背景:** 当前的密钥透明系统依赖强大的审计者来验证密钥更新的有效性，但实际部署中由于审计证明文件过大，导致只有少量审计者参与。
>
> **主要贡献:** Forget-me-not Trees通过结合Merkle树和Bloom滤波器，提出了一种新的密钥透明方案。
>
> **达到效果:** 该系统将审计证明的大小减少了约500倍，从15MB-30MB降至30KB-60KB，实现了仅依赖哈希函数的大规模可审计密钥透明性。
>
> **技术梗概:** Forget-me-not Trees巧妙地利用了Merkle树和Bloom滤波器的特点，以减少证明大小并提高效率。

---
### [2026/1277] On the Round Complexity of Dishonest-Majority MPC

- **作者:** Ran Cohen, Daniel Collins, Pouyan Forghani, Juan Garay, Vassilis Zikas

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1277) | [PDF](https://eprint.iacr.org/2026/1277.pdf)


> **研究背景:** 研究在点对点信道上的MPC协议，在诚实多数失败的情况下，其轮次复杂度是多少？尽管存在两轮的MPC协议和预期常数轮次的广播协议，但现有技术无法直接应用于解决该问题。
>
> **主要贡献:** 论文首次系统地探讨了这一问题，并证明了严格的一致中止的（严格）恒定轮次MPC是不可能实现的。此外，还提出了……
>
> **达到效果:** 研究结果表明，在诚实多数失败的情况下，任何一致中止的安全广播协议在面对超级常数数量的恶意参与者时都需要超过常数轮次。
>
> **技术梗概:** 通过证明和构造性的方法，论文分析了广播协议与MPC之间的关系，并探讨了它们在不同假设下的复杂度差异。

---
### [2026/1278] Barriers for Transparent Algebraic Generation of Hard Supersingular Curves

- **作者:** Anis Bkakria

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1278) | [PDF](https://eprint.iacr.org/2026/1278.pdf)


> **研究背景:** 研究探讨了透明公共生成安全超奇异曲线的方法，即公开、基于种子的可重复算法输出超奇异曲线，并暴露种子、验证转录以及可通过实现推导的所有代数信息。
>
> **主要贡献:** 定义了一个转录安全性模型，并分析了几种拟合的代数生成路径中的障碍。
>
> **达到效果:** 证明了模化共轭采样器和直接采样器在某些条件下的局限性，这些结果限制了可隐藏证人的仪式、高阶索引映射等的可能性。
>
> **技术梗概:** 通过分析超奇异不变量的特征以及代数生成路径中的泄漏原则来构建障碍。

---
### [2026/1281] Resultants Meet Resultant: Improving CICO-1 and CICO-2 Attacks on ZK-Friendly Permutations

- **作者:** Antoine Bak, Augustin Bariant, Maël Hostettler, Vincent Neiger

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1281) | [PDF](https://eprint.iacr.org/2026/1281.pdf)


> **研究背景:** 随着零知识证明协议的广泛应用，需要高效的算术化原语以确保其在该环境下的安全性。CICO-$k$问题是评估此类置换安全性的标准方法。
>
> **主要贡献:** 本文提出了一种使用双变量结果式的新型CICO-2攻击框架，并改进了基于$\alpha$-反转的CICO-1攻击，通过引入临时变量和高效消除技术，显著提高了攻击效率。
>
> **达到效果:** 新的攻击框架在理论上实现了复杂度接近线性的进步，对于CICO-$2$攻击为$\tilde{\mathcal{O}}(\alpha^n D_I)$，而对于CICO-$1$攻击为$\tilde{\mathcal{O}}(D_I)$。
>
> **技术梗概:** 通过利用快速双变量结果式算法解决最终的双变量系统问题，本文提出的方法在理论上实现了复杂度的优化。

---
### [2026/1282] Physics-Aware Temporal Feature Engineering for Eavesdropping Detection in BBM92 Quantum Key Distribution

- **作者:** Saksham Gupta

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1282) | [PDF](https://eprint.iacr.org/2026/1282.pdf)


> **研究背景:** 在无噪声自由空间光学（FSO）信道中，自然大气变化可能隐藏短时低强度窃听突发，使静态量子位错误率（QBER）阈值失效。
>
> **主要贡献:** 提出了基于物理感知的时间特征工程方法，用于BBM92量子密钥分发（QKD）遥测的机器学习异常检测。
>
> **达到效果:** 实验结果显示，使用所提特征集训练的XGBoost分类器在模拟FSO遥测数据集中达到了96.9%的召回率和97.6%的精度，显著优于静态QBER阈值方法。
>
> **技术梗概:** 通过计算30秒滑动窗口内的24维特征空间来表征QBER、贝尔S参数和光子 coincidence 率的时间演化及交叉可观测量相关性。

---
### [2026/1283] Privacy-Preserving Outsourced Witness Updates for Append-Only RSA Accumulators

- **作者:** Hongzi He, Qianhong Wu, Bo Qin, Hao Gao, Willy Susilo

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1283) | [PDF](https://eprint.iacr.org/2026/1283.pdf)


> **研究背景:** 针对频繁插入操作导致的附录只读RSA累加器中见证维护难题，尤其是匿名凭证系统中的间歇在线用户无法持续同步更新信息的问题，本文提出了一种隐私保护的外包见证更新协议。
>
> **主要贡献:** 该协议结合了见证更新与线性整数秘密共享（LISS），实现了按需、客户端无状态的见证更新，并保持了在低于阈值的更新服务器联盟攻击下见证的隐私性和不可链接性，同时提供了对恶意或错误响应服务端的可问责性。
>
> **达到效果:** 通过形式化系统和威胁模型分析，该协议支持在长时间离线后进行实际的一次性见证更新，客户端成本与丢失的更新次数无关，服务器成本主要取决于回溯窗口长度和LISS分布矩阵。
>
> **技术梗概:** 该协议利用了线性整数秘密共享（LISS）技术来实现客户端无状态的见证更新，并结合了外包计算机制以保护见证隐私性和不可链接性。

---
### [2026/1284] Zero-Knowledge Proofs of Generalized Regular Expression Matching for Anonymized Email Verification

- **作者:** Shreyas Londhe, Aayush Gupta, Sora Suegami, Yogesh Shahi, Rute Figueiredo, Parisa Hassanizadeh, Shahriar Ebrahimi

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1284) | [PDF](https://eprint.iacr.org/2026/1284.pdf)


> **研究背景:** 随着数字通信在身份验证、金融交易和合规性中的应用日益广泛，证明对DKIM签名邮件的控制权通常需要揭示完整邮件内容或依赖中心化中介，这带来了隐私风险并增加了信任假设。现有的零知识证明（ZKP）系统在处理复杂结构化格式和丰富字符集时效率低下。
>
> **主要贡献:** 本文提出了一种基于路径验证的ε-自由NFA正则表达式匹配ZKP系统，实现了证明者复杂度线性于捕获路径且与原始邮件大小无关。该方法支持全面的DKIM签名邮件验证所需的复杂标准结构。
>
> **达到效果:** 通过结合DKIM签名验证、任意长度SHA-256电路及通用正则表达式原语等组件，本文设计了完整的端到端ZK电路，显著提高了验证效率和实用性。
>
> **技术梗概:** 该系统利用ε-自由NFA的路径验证技术，将复杂正则表达式的匹配问题转化为图形上的路径查找问题，从而大幅降低了证明者计算负担。

---
### [2026/1285] Oblivious Priority Queue and Single-Source Shortest Path in the External Memory Setting

- **作者:** Arya Maheshwari, Elaine Shi

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1285) | [PDF](https://eprint.iacr.org/2026/1285.pdf)


> **研究背景:** 研究了在外部存储模型下设计隐私保护算法的问题，这些算法的内存访问模式不应泄露秘密输入信息。这类算法已在大规模生产系统中部署，例如Signal的私人联系发现服务。
>
> **主要贡献:** 提出了一个针对无向图的外部存储隐私保护单源最短路径算法，该算法在I/O效率和总工作量上几乎达到了最优性能。
>
> **达到效果:** 该算法实现了I/O效率$O(V + \frac{E}{B}\log\frac{E}{M})$和总工作量$O(E\log E)$，假设边数$E = \Omega(V)$，其中$V$表示顶点数，$E$表示边数，$M$和$B$分别代表目标机器的缓存大小和块大小。
>
> **技术梗概:** 通过定制化的方法设计了适用于特定计算任务的隐私保护算法，以提高实际应用中的效率。

---

## 更新: 2026-06-17 07:46

*新增 4 篇论文 (编号 1254--1257)*

### [推荐] [2026/1255] Bootstrapping is All You Need: Secure Transformer Inference via Improved CKKS Functional Bootstrapping

- **匹配关键字:** homomorphic encryption

- **作者:** Pan Xiao, Rending Ouyang, Heng Zhang, Jiawen Zhang, Jian Liu

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1255) | [PDF](https://eprint.iacr.org/2026/1255.pdf)


> **研究背景:** 研究背景：全同态加密（FHE）允许非交互式安全变换推理（NISTI），但由于启动程序成本高，传统方法通常选择支持大乘法深度的参数以减少启动频率。然而，较大的深度会增加密文大小，导致更高的通信和计算开销。
>
> **主要贡献:** 主要贡献：提出了一种新的功能启动程序（FBS）方案，通过将尽可能多的操作融合到每个启动程序操作中，显著减少了规定的乘法深度。
>
> **达到效果:** 达到的效果：该FBS框架实现了1.9倍的运行时加速（从662.3秒减少到349.5秒），并使通信量减少了3倍（从48.3MB减少到16.1MB），相比最先进的方法。
>
> **技术梗概:** 技术梗概：通过为目标函数提供三角最小最大逼近，使得FBS适用于精度敏感组件如变换非线性层；将线性层整合到槽至系数（S2C）转换中，从而避免单独评估它们。

---
### [2026/1254] Top Gun: Degree Annihilation Attacks on Poseidon

- **作者:** Antonio Sanso, Giuseppe Vitto

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1254) | [PDF](https://eprint.iacr.org/2026/1254.pdf)


> **研究背景:** Poseidon作为广泛使用的算术化密码置换，在现代零知识证明系统中占据核心地位，尽管已有针对其简化轮数版本的代数攻击提出，但推荐参数集的安全性尚未被突破。关键挑战在于控制由置换产生的多项式表示中的次数增长。
>
> **主要贡献:** 作者提出了度消亡这一新的代数密码分析框架，通过施加代数约束使主要次数项消失，从而降低现有轮次的贡献，生成有效次数显著较低的多项式系统。
>
> **达到效果:** 该方法结合了传统的跳过轮次技术，并进一步推广至多元情况，利用控制方程组逐步消除部分轮次的次数贡献，通过消元、结果和Gr...等方法求解这些系统。
>
> **技术梗概:** 度消亡框架通过施加特定代数约束来减少多项式系统的有效次数，这种方法既适用于二元形式也扩展到了多元情况，并且能够与传统的跳过轮次技术相结合以增强攻击效果。

---
### [2026/1256] Problems in algebra inspired by tropical cryptography

- **作者:** I. Buchinskiy, M. Kotov, A. Treier

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1256) | [PDF](https://eprint.iacr.org/2026/1256.pdf)


> **研究背景:** 该研究背景源于2011年Grigoriev和Shpilrain提出的将热带代数结构应用于密码学的构想，近年来基于此类结构的多种协议被提出，并且也发现了其中许多协议的安全漏洞。
>
> **主要贡献:** 作者综述了在设计安全方案及分析其脆弱性过程中产生的多项纯代数与计算问题的研究成果和开放问题。
>
> **达到效果:** 研究结果包括解决特定类热带及其他类似结构方程组的复杂度、算法及其方法，以及这些方程组满足系统的渐近密度等。
>
> **技术梗概:** 采用了一般化边际集的概念，并探讨了不同类型的两两可交换矩阵。

---
### [2026/1257] Stickel-type key exchange with hidden subspaces

- **作者:** Fintan Costello, Paul Watts

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1257) | [PDF](https://eprint.iacr.org/2026/1257.pdf)


> **研究背景:** 研究背景：本文针对Stickel类型密钥交换方案进行了分析，这些方案涉及在有限域上的$n 	imes n$矩阵的双侧乘法，并且这些矩阵来自具有特定可交换结构的公共子空间。
>
> **主要贡献:** 主要贡献：作者提供了一种证人查找密码分析方法，可以以多项式时间破解所有基于此类公钥子空间的方法，包括Stickel原始提案及其多项式扩展和代数扩展等。
>
> **达到效果:** 达到的效果：通过隐藏用于形成密钥的可交换子空间，提出的新方案能够避免上述特定的公共子空间分析，并将证人查找问题直接归约为一个标准NP难问题（Edmonds问题）。
>
> **技术梗概:** 技术梗概：该研究使用了矩阵乘法和代数结构来构建新的密钥交换协议，并通过私有术语进行混淆，从而提高了安全性。

---

## 更新: 2026-06-15 07:53

*新增 10 篇论文 (编号 1242--1251)*

### [推荐] [2026/1248] Atlantis: Lattice-based Anonymous Tokens with Private Metadata Bit

- **匹配关键字:** lattice, post-quantum, homomorphic encryption

- **作者:** Foteini Baldimtsi, Aayush Yadav

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1248) | [PDF](https://eprint.iacr.org/2026/1248.pdf)


> **研究背景:** 现有的匿名令牌与私有元数据位（ATPM）方案依赖于经典硬假设，缺乏后量子安全性。
>
> **主要贡献:** 本文提出了首个基于格假设的ATPM方案Atlantis，实现了公开验证和部分知识下私有提取隐藏位的功能。
>
> **达到效果:** Atlantis方案通过结合盲签名范式与格基线性同态加密技术实现，并使用Falcon-512和LNP22系统实例化，通信量为70 KB，令牌大小为129 KB。
>
> **技术梗概:** 该方案采用了Fischlin盲签名框架并引入了基于格的线性同态加密方法来承载隐藏位。

---
### [2026/1242] SoK: The Constant Time Model

- **作者:** Billy Bob Brumley

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1242) | [PDF](https://eprint.iacr.org/2026/1242.pdf)


> **研究背景:** 研究背景：常时间模型是抵御密码学实现中的定时攻击的主要防护手段，但学术界和工业界的定义存在差异。
>
> **主要贡献:** 主要贡献在于系统化地梳理了常时间模型及其演变过程，并识别出模型保护范围与规范假设之间的差距。
>
> **达到效果:** 研究结果揭示了一个与私钥加载相关的规范级漏洞，并在OpenSSL和BoringSSL中确认了此泄漏现象。
>
> **技术梗概:** 采用了一种进攻性方法来发现起源于加密原语边界之外的定时漏洞。

---
### [2026/1243] LendLocked: Privacy & Transparency for Digital Library Lending

- **作者:** Boya Wang, Peter Hall, Sunoo Park

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1243) | [PDF](https://eprint.iacr.org/2026/1243.pdf)


> **研究背景:** 当前的数字图书馆借阅模式存在透明度低和隐私保护不足的问题，这限制了读者的信息访问自由。
>
> **主要贡献:** 研究通过访谈揭示了现有系统的缺陷，并提出了LendLocked系统以实现与实体图书馆借阅相当的隐私性和透明性。
>
> **达到效果:** LendLocked系统在随机预言模型下证明能够满足强安全、隐私和透明性的要求，显著提升了数字借阅的安全性。
>
> **技术梗概:** 该系统基于密码学和可信硬件设计，并通过微基准测试验证了其关键加密功能的有效性。

---
### [2026/1244] Resource Estimation of a Distributed Quantum Algorithm for Elliptic Curve Discrete Logarithms

- **作者:** MohamadAli Khajeian

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1244) | [PDF](https://eprint.iacr.org/2026/1244.pdf)


> **研究背景:** 研究背景：评估椭圆曲线密码系统的量子安全性需要精确估计在容错量子硬件上解决椭圆曲线离散对数问题（ECDLP）所需的资源，特别是在单块实现Shor算法时，逻辑量子比特的数量是一个主要限制。
>
> **主要贡献:** 主要贡献：作者提出了一种分布式量子离散对数框架，并将其应用于椭圆曲线设置中，通过经典二分驱动协调器验证候选子集中的秘密标量，显著减少了所需的控制寄存器宽度。
>
> **达到效果:** 达到的效果：结合最新的空间高效可逆模除电路模型，单节点逻辑量子比特要求从现有的单一实现大幅减少至约1080到1140个量子比特，低于现有技术。
>
> **技术梗概:** 技术梗概：该研究采用分布式算法分解全局标量搜索空间，并通过经典二分法协调器进行验证，同时使用了Luo等人（2026）提出的高效可逆模除电路来压缩量子内存占用。

---
### [2026/1245] Accountable Asynchronous Multi-Party Computation

- **作者:** Pierre Civit, Rachid Guerraoui

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1245) | [PDF](https://eprint.iacr.org/2026/1245.pdf)


> **研究背景:** 在非同步网络中，经典的分区论证表明，在故障数量达到$f \geq n - 2t$时，任何$t\text{-resilient}$协议无法确保许多功能的安全性。因此，需要构建问责制机制来检测并阻止安全违规行为。
>
> **主要贡献:** 本文提出了首个具备问责制的异步多方计算（AAMPC）协议，能够在$f \leq t < n/3$时保证目标超属性，并在故障数量位于$(t,\,t_{\mathrm{acc}}]$区间内提供强问责机制。
>
> **达到效果:** 该协议确保了在指定条件下所有目标超属性的正确性、隐私性、输入独立性和输出交付，同时提供了针对部分故障情况的公开可验证证据。
>
> **技术梗概:** 技术上，本文贡献了一种高效的可问责加法同态高阈值异步完全（可验证）秘密共享功能，具有摊销线性通信成本。这使得在线阶段的延迟为$O\big(\mathsf{Depth}(\mathcal{C})\big)$，并实现了高效的安全计算。

---
### [2026/1246] A Note on Combined Attacks on Fallen Sanctuary

- **作者:** Enanko Basak, Sayandeep Saha

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1246) | [PDF](https://eprint.iacr.org/2026/1246.pdf)


> **研究背景:** 泄漏抗性重钥方案旨在通过定期刷新临时密钥来维持加密安全性，即使在存在侧信道泄露的情况下。Fallen Sanctuary (LR4) 是一种高阶泄漏抗性重钥构造，能够在足够多的踪迹被积累之前实现指数级的安全放大。
>
> **主要贡献:** 本文研究了 LR4 在结合故障攻击和侧信道攻击模型下的安全性。作者证明了针对计数器更新和验证机制的瞬态故障可以阻止重新初始化状态的进展，导致临时密钥重复使用。
>
> **达到效果:** 结果表明，攻击者可以积累对应相同秘密状态的任意数量泄漏踪迹，从而将受保护原语的安全性降低到没有重钥的传统实现水平。
>
> **技术梗概:** 通过模拟存在故障的实现来评估攻击，并分析其对 LR4 所宣称的泄漏抗性保证的影响。

---
### [2026/1247] Practical Attacks on a Decentralized Secure Messenger Session

- **作者:** Kota Urushigaki, Hayato Kimura, Atsushi Tanaka, Takanori Isobe

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1247) | [PDF](https://eprint.iacr.org/2026/1247.pdf)


> **研究背景:** Session是一款注重用户匿名性和隐私性的去中心化即时通讯应用，采用独特的消息协议V1版本替代了广泛研究的Signal Protocol。然而，该协议存在设计漏洞，可能被利用进行攻击。
>
> **主要贡献:** 作者通过实施驱动的安全分析发现了Session协议中的两个关键设计缺陷，并展示了三种实际可行的攻击方法：冒充攻击、消息时间戳伪造攻击以及消息丢弃和重放攻击。
>
> **达到效果:** 这些攻击允许恶意服务器节点或未授权的内部人员替换公钥，静默删除或重复发送消息，篡改对话的时间顺序感知。研究结果强调了这些漏洞对协议基本安全保证的重大威胁。
>
> **技术梗概:** 作者采用全面的安全分析方法，结合实际应用环境进行测试，揭示了Session协议中的根本性设计缺陷，并提出了即时的缓解策略以确保协议的安全性。

---
### [2026/1249] A family of invertible shift-invariant maps with strong arithmetic properties

- **作者:** Xiao-Xin Zhao, Deng Tang, Zhong-Xiao Wang, Qun-Xiong Zheng

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1249) | [PDF](https://eprint.iacr.org/2026/1249.pdf)


> **研究背景:** 研究背景：移不变映射在许多对称密码方案中被用于设计非线性层，如Keccak中的$\chi$-映射。本文探讨了基于无前缀后缀序列诱导的$n$元布尔函数的移不变映射族，这些映射定义于$\mathbb{F}_2^n$上，并研究其代数性质。
>
> **主要贡献:** 主要贡献：作者证明了该映射族形成一个关于复合运算的交换幺半群，并且当$m mid n$时与特定多项式环的单位群同构，当$m\mid n$时则与另一个形式的多项式环的单位群同构。
>
> **达到效果:** 达到的效果：通过上述同构关系，作者将映射族的复合运算转化为多项式的乘法运算，并研究了$\rho=x_0+(x_1+a_1+1)(x_2+a_2+1)\cdots (x_m+a_m+1)$的具体性质。
>
> **技术梗概:** 技术梗概：利用代数结构和同构关系，将移不变映射的复合运算转化为多项式的乘法运算，并通过多项式环的已有理论来研究这些映射的可逆性和周期结构等特性。

---
### [2026/1250] TensorZKP: Repurposing GPU Tensor Cores for High-Performance Zero-Knowledge Proofs

- **作者:** Tao Lu, Jipeng Zhang, Yanpei Guo, Xuanming Liu, Wenjie Qu, Zonghui Wang, Wenzhi Chen, Jiaheng Zhang

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1250) | [PDF](https://eprint.iacr.org/2026/1250.pdf)


> **研究背景:** GPU Tensor Cores旨在加速矩阵乘法，已成为AI革命的主要驱动力。然而，现有的零知识证明（ZKPs）的GPU实现仅依赖通用SIMT内核，未能充分利用Tensor Cores的强大计算能力。
>
> **主要贡献:** 作者首次提出了TensorZKP框架，将ZKP的关键模块重新设计为适用于Tensor Core的矩阵乘法任务，并开发了异步Warp特化框架以优化内存访问和操作流程。
>
> **达到效果:** 实验结果表明，TensorZKP在大规模实例下表现出显著的效率提升，特别是在证明生成成本方面取得了突破性进展。
>
> **技术梗概:** 通过重新设计有限域算术并将其映射到Tensor Core硬件上，并利用异步Warp特化框架来优化内存访问和操作流程，实现了高效的数据处理与计算加速。

---
### [2026/1251] Related Differentials of $4\times4$ MDS Matrices: A Complete Characterization

- **作者:** Kamil Otal, Ali Mert Sülçe, Oğuz Yayla

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1251) | [PDF](https://eprint.iacr.org/2026/1251.pdf)


> **研究背景:** 研究背景：相关差分是线性层中的一种特殊性质，与零差攻击密切相关。对于$4	imes4$ MDS矩阵，关于其是否允许存在相关差分的问题尚未完全解决。
>
> **主要贡献:** 主要贡献在于完整地刻画了所有$4	imes4$ MDS矩阵（除同构外）是否允许存在相关差分，并给出了明确的判别条件。
>
> **达到效果:** 达到的效果是，通过15个具体的方程和280个显式多项式方程，全面解决了$4	imes4$ MDS矩阵是否存在相关差分的问题，这些方程具有独特的数学结构。
>
> **技术梗概:** 技术梗概：采用代数几何方法，特别是射影几何中的点集理论，结合多项式方程的不可约性和互素性分析，确定了所有可能的条件。

---

## 更新: 2026-06-12 07:53

*新增 14 篇论文 (编号 1225--1240)*

### [推荐] [2026/1225] Towards Post-Quantum Secure eSIM Provisioning Protocols

- **匹配关键字:** post-quantum

- **作者:** Harrison Banda, Hannes Bartz, Juliane Krämer, Michael Meyer, Vincent Quentin Ulitzsch

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1225) | [PDF](https://eprint.iacr.org/2026/1225.pdf)


> **研究背景:** eSIM技术通过远程方式提供SIM卡服务，避免了物理SIM卡的分发。然而，通用量子计算机的发展可能威胁现有基于公钥加密的安全性。
>
> **主要贡献:** 论文提出了PQC-RSP协议，这是一种后量子安全版本的RSP协议，并解决了在RSP中引入KEMs所带来的挑战和安全性问题。
>
> **达到效果:** 通过证明PQC-RSP的安全性和评估其性能开销，该研究增强了eSIM远程配置过程的安全性以抵御潜在的量子攻击。
>
> **技术梗概:** 研究采用了后量子密码学中的关键封装机制(KEMs)，并在纯后量子和混合版本中进行了实现与安全性分析。

---
### [推荐] [2026/1228] Advancing Pseudorandom Codes: Beyond Parity Checks and Standard-Model CCA1 Security

- **匹配关键字:** LWE

- **作者:** Yu Chen, Xinyu Mao, Hongxu Yi

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1228) | [PDF](https://eprint.iacr.org/2026/1228.pdf)


> **研究背景:** 研究背景：伪随机码（PRCs）是一种纠错码，其码字在计算上难以与均匀随机字符串区分开来，这一原理旨在为生成式AI模型提供鲁棒的水印功能。尽管近期的研究已经证明了PRCs的可能性，但它们的基础加密假设多样性以及对抗主动对手的安全性仍然是关键挑战。
>
> **主要贡献:** 主要贡献：该研究在结构多样性和高级安全性两个方面推进了PRCs的研究。提出了一个新的基于密集矩阵和隐藏结构的伪随机码模板，并首次在标准模型中构建了一个抗预挑战选择码字攻击（CCA1）的公钥伪随机码。
>
> **达到效果:** 达到的效果：新提出的伪随机码模板为从代码之外的假设构造PRCs提供了可能，特别是通过引入一个新的LPN型假设——密集植入LPN，该假设基于局部窗口搜索而非全局奇偶校验的新解码机制。同时，在标准模型中实现了首个抗预挑战选择码字攻击（CCA1）的安全公钥伪随机码。
>
> **技术梗概:** 技术梗概：研究采用了新的LPN型假设来构建伪随机码模板，通过引入密集矩阵和隐藏结构，提出了基于局部窗口搜索的新解码机制，并在标准模型中实现了抗预挑战选择码字攻击（CCA1）的安全性证明。

---
### [推荐] [2026/1230] Formula Freshness for Staged Hybrid Authenticated Key Exchange

- **匹配关键字:** post-quantum

- **作者:** Anis Bkakria, Merland Chrislain Chadrel BAFOUETILA

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1230) | [PDF](https://eprint.iacr.org/2026/1230.pdf)


> **研究背景:** 研究背景：随着后量子密码学在握手协议中的应用，现有混合KEM的安全性仅保护共享密钥输入，未全面覆盖分支揭示、阶段密钥揭示、选择性破坏或延迟破坏后的安全性问题。
>
> **主要贡献:** 主要贡献：通过引入分枝公式新鲜度的概念，为每个阶段提供一个单调的分枝暴露、认证新鲜度、转录绑定、KDF谱系和显式非揭示原子的公式，从而全面描述这些阶段性声明的安全性。
>
> **达到效果:** 达到的效果：证明了在特定TLS 1.3 ECDHE-ML-KEM 1-RTT场景下，通过替换存活分枝贡献并使用标记HKDF/PRF风格的目标隐藏论证，以及新鲜KDF切片，可以实现握手、应用、导出器和恢复目标的具体保存边界。
>
> **技术梗概:** 技术梗概：采用选择局部计费方法，固定可接受的见证选择器来确定哪些存活分枝和KDF切片被收费，并通过认证绑定和单射转录表示分别独立地实现协议一致性。

---
### [推荐] [2026/1231] The Best of Both Worlds: Hybrid Authenticated Key Exchange for QKD(N) without Signatures

- **匹配关键字:** post-quantum

- **作者:** Sebastian Clermont, Johanna Henrich

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1231) | [PDF](https://eprint.iacr.org/2026/1231.pdf)


> **研究背景:** 后量子密码学(PQC)和量子密钥分发(QKD)都是抵御量子攻击的通信安全方案，但处于不同的成熟阶段。为了降低安全风险，通常采用混合化策略。
>
> **主要贡献:** 本文提出了一种结合PQ认证密钥交换(AKE)与QKD密钥协商的混合AKE协议(HAKE)，并完全去除了数字签名的需求。
>
> **达到效果:** 该协议在CK01模型下实现了AKE的安全性，并在QKD部分未被破坏的情况下提供了条件信息论安全性保证，优于先前的混合协议。
>
> **技术梗概:** 通过利用Backendal等人提出的多输入KDF框架进行全模块化安全分析，结合使用ML-KEM、FrodoKEM和Classic McEliece等方案展示了其实用可行性。

---
### [推荐] [2026/1233] Implementation of Learning with Errors in Non-Commuting Multiplicative Groups

- **匹配关键字:** LWE

- **作者:** Aleksejus Mihalkovich, Lina Dindiene, Eligijus Sakalauskas

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1233) | [PDF](https://eprint.iacr.org/2026/1233.pdf)


> **研究背景:** 本文旨在将学习误差（LWE）推广到非交换乘法群的模极大循环群家族，利用$\mathbb{M}_{2^t}$组具有两个最大乘法周期的事实来恢复消息位。
>
> **主要贡献:** 作者通过在考虑的组中实现O. Regev 的原始想法，充分利用了$\mathbb{M}_{2^t}$的非交换性，并提出了一种准确的准则以高概率恢复消息位。
>
> **达到效果:** 该方法使得达到与原方案相当的安全水平。
>
> **技术梗概:** 通过在模极大循环群中应用LWE，结合非交换乘法组的特点来提高安全性。

---
### [2026/1226] Changing of the Guards with Two Shares - Security Flaws, Corrrections, and Application to Low-Latency AES

- **作者:** Feng Zhou, Gehui Yang, Junhuai Yang, Hua Chen, Limin Fan

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1226) | [PDF](https://eprint.iacr.org/2026/1226.pdf)


> **研究背景:** 文章针对侧信道攻击中的掩码技术，特别是第一阶掩码方案进行了研究。
>
> **主要贡献:** 作者首先指出了Askeland等人在CARDIS 2022会议上提出的基于COTG技术的轮次设计中存在的安全漏洞，并提出了一种修正方案。
>
> **达到效果:** 通过结合CHES 2025引入的时间共享掩码S盒，实现了延迟为20个时钟周期且无需新鲜随机数的一阶掩码AES实现。
>
> **技术梗概:** 研究采用了修改后的COTG技术和TSM S盒来提高安全性并减少延迟。

---
### [2026/1227] Chosen Ciphertext Secure Pseudorandom Codes in the Standard Model

- **作者:** Nico Döttling, Antoine Joux, Venkata Koppula, Mahesh Sreekumar Rajasree, Hendrik Waldner

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1227) | [PDF](https://eprint.iacr.org/2026/1227.pdf)


> **研究背景:** Pseudorandom codes (PRCs)提供了一种增强的加密方案，能够抵抗有限数量的汉明错误。尽管Alrabiah等人在随机预言模型中实现了选择密文安全（CCA-secure）的公钥PRC，但在标准模型下构建此类系统仍是一个挑战。
>
> **主要贡献:** 本文解决了这一问题，首次提出了在标准模型下的选择密文安全公钥PRC构造，并且能够以恒定速率解码并容忍恒定比例的错误。此外，还基于一种新的假设——Noisy McEliece，构建了一个具有推测次指数安全性、适应性鲁棒性的公钥伪随机代码。
>
> **达到效果:** 该构造不仅填补了理论空白，还在实际应用中提供了更强的安全保障，并且能够广泛应用于多种标准密码学假设下。
>
> **技术梗概:** 通过结合纠错码和加密技术，本文提出了一种通用框架来实现这些目标。Noisy McEliece假设的引入为这一框架提供了新的安全基础，同时也增加了系统的鲁棒性。

---
### [2026/1229] Invisible Traces: Subversion Attacks on Batch-Issued Credentials

- **作者:** Anna-Birgitta Burmeister, Anna Fennig, Andreas Franke, Karla Friedrichs, Anja Lehmann, Kurt-Kester Leißering, Konrad Letz, Cavit Özbay

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1229) | [PDF](https://eprint.iacr.org/2026/1229.pdf)


> **研究背景:** 欧盟成员国需在2026年底前推出数字身份系统，强调强隐私保护，要求支持选择性披露和不可链接性。现有方案虽能实现弱形式的不可追踪性，但存在被恶意发行方利用进行跟踪攻击的风险。
>
> **主要贡献:** 研究提出了更隐蔽的篡改攻击类型，即允许持有短追踪密钥的验证者去匿名化用户的同时保持攻击未被察觉，并正式定义了此类攻击下的不可追踪性。
>
> **达到效果:** 证明批处理发放的带有盐散列的ECDSA凭证无法实现所定义的隐私形式。提出了几种隐蔽的篡改攻击方法，并建议了一些轻量级机制来解决这些问题。
>
> **技术梗概:** 通过引入短追踪密钥和未被察觉的篡改策略，研究设计了新型攻击模型，并利用形式化方法验证其有效性。

---
### [2026/1232] A Heuristic Subexponential Attack on the McEliece Cryptosystem

- **作者:** Pierre Briaud, Axel Lemoine, Hugues Randriambololona, Jean-Pierre Tillich

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1232) | [PDF](https://eprint.iacr.org/2026/1232.pdf)


> **研究背景:** 本文提出了一种针对基于二元Goppa码的McEliece密码系统的启发式次指数攻击方法，该方法不仅适用于偶特征下的Goppa码，还借鉴了[CMT23, M25, BLT26]中的二次关系矩阵模型。
>
> **主要贡献:** 贡献在于提供了一种新的代数建模方法来寻找与攻击的Goppa码相关的二次关系代码中秩为2的矩阵，并利用这些矩阵恢复秘密代数结构，从而破解了方案。
>
> **达到效果:** 该攻击在McEliece TII挑战上展示了有效性，包括83、89、119、166、210甚至248位的安全性目标，以及CFS密钥参数r=9和m=16对应74.9位安全性。针对CFS密钥的攻击耗时14小时，使用了24GB的RAM。
>
> **技术梗概:** 该方法基于二次关系矩阵模型，在代码中寻找秩为2的矩阵，并利用这些矩阵恢复秘密代数结构。作为副产品，还提供了一种新的偶特征下Goppa码区分器，其复杂度与syzygy区分器相同，均为次指数级。

---
### [2026/1236] New bounds on private simultaneous quantum message passing

- **作者:** Uma Girish, Alex May, Natalie Parham, Henry Yuen

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1236) | [PDF](https://eprint.iacr.org/2026/1236.pdf)


> **研究背景:** 私有同时消息传递(PSM)设置是一种安全多方计算的最小模型，在此设置中，k个玩家获得输入$x_i\in\{0,1\}^n$并独立地向裁判发送消息，裁判仅能得知$f(x_1,...,x_k)$而不能获取$(x_1,...,x_k)$的其他信息。
>
> **主要贡献:** 论文提出了量子和经典PSM模型的新上界和下界，特别是首次利用隐私条件给出了量子PSM的两个下界，并展示了允许量子通信和共享纠缠时的上界结果。
>
> **达到效果:** 通过证明两个下界，研究揭示了实施私有同时消息传递所需的资源可能远超非私有情况；对于某些显式函数，给出二次下界；并首次利用隐私条件给出了量子PSM的下界。
>
> **技术梗概:** 技术上，论文使用Neciporuk度量来评估量子纠缠需求，并通过通信矩阵的秩来限制完美隐私但不完全正确的2玩家量子PSM。

---
### [2026/1237] SING: Improving the Efficiency of MPC Protocol Assignment using Graph Neural Networks

- **作者:** Jannis Blüml, Moritz Huppert, Nora Khayata, Joachim Schmidt, Thomas Schneider

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1237) | [PDF](https://eprint.iacr.org/2026/1237.pdf)


> **研究背景:** 传统的安全多方计算(MPC)协议分配方法依赖于特定部署的成本模型和耗时的整数线性规划(ILP)，这限制了其在不同协议和环境中的可扩展性和适用性。
>
> **主要贡献:** SING引入了一种基于图神经网络(GNN)的方法，用于加速MPC协议分配，并支持非线性成本模型的学习，从而提高效率并增强灵活性。
>
> **达到效果:** 通过使用GNN模仿现有系统的行为以及学习预测成本，SING显著提高了MPC协议分配的速度和质量，同时减少了对复杂ILP的依赖。
>
> **技术梗概:** SING利用图神经网络进行模仿学习和成本驱动的学习，前者加速了协议分配过程，后者则能够适应新的协议套件和部署环境。

---
### [2026/1238] On the Additive Sensitivity of LZ77 Under Consecutive Edits

- **作者:** Jeremiah Blocki, Seunghoon Lee

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1238) | [PDF](https://eprint.iacr.org/2026/1238.pdf)


> **研究背景:** 研究背景：探讨在连续编辑下LZ77压缩算法的加性敏感性，以解决传统加密方式中密文长度泄露明文信息的问题。
>
> **主要贡献:** 主要贡献：提出了g-连续敏感性的定义，并对LZ77进行了近似紧致的敏感性刻画。
>
> **达到效果:** 达到的效果：改进了针对较长秘密（如密码、会话标识符等）的信息保护效果，避免了组隐私下的参数退化问题。
>
> **技术梗概:** 技术梗概：通过定义g-邻居字符串并分析LZ77在连续编辑下的敏感性来增强信息泄漏防护机制。

---
### [2026/1239] Balanced Additive Randomized Encodings for Shuffle Differential Privacy

- **作者:** Yu Wei, Jaspal Singh, Adya Agrawal, Vassilis Zikas

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1239) | [PDF](https://eprint.iacr.org/2026/1239.pdf)


> **研究背景:**  shuffle差分隐私通过安全洗牌器对用户随机编码进行混排，提供个体数据隐私性，而无需中央可信实体。然而，实现通用性和客户端效率仍然是一个挑战。
>
> **主要贡献:** 作者提出了一种客户端高效的单轮编译器，将中心DP转换为非鲁棒计算shuffle DP，并构建了一个新的平衡的加法随机编码方案。
>
> **达到效果:** 该方案将机制M在最坏情况下的每客户端计算量从O(|M|)减少到O(|M|/n)，显著提高了资源受限设备如移动电话、物联网传感器和网页浏览器的实用性。
>
> **技术梗概:** 通过引入新的permute-XOR随机编码原语实现跨独立信道的线缆焊接，从而均衡客户端之间的计算负担。

---
### [2026/1240] Adaptive attacks on FESTA variants with masked-degree isogenies

- **作者:** Tomoki Moriya

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1240) | [PDF](https://eprint.iacr.org/2026/1240.pdf)


> **研究背景:** FESTA是一种基于曲率的陷阱门函数，作为高性能替代品在基于曲率的密码学中提出。MOXZ攻击利用恶意密文和检查预言机访问权，旨在破解FESTA及其变体。
>
> **主要贡献:** 该研究提出了一个新颖的一般化MOXZ攻击方法，能够针对具有掩码度量等式的关键字的多个FESTA变体进行攻击。
>
> **达到效果:** 通过此攻击，研究人员成功地突破了几个FESTA变体的安全性，证明了这些变体在某些特定条件下的脆弱性。
>
> **技术梗概:** 该技术利用了恶意密文和检查预言机访问权，对具有掩码度量等式的关键字的FESTA变体进行了一种新颖的一般化攻击方法。

---

## 更新: 2026-06-10 20:41

*新增 45 篇论文 (编号 1147--1224)*

### [推荐] [2026/1147] FATT Chance: On the Robustness of Standalone and Hybrid ML-KEM Key Exchange in TLS 1.3

- **匹配关键字:** post-quantum

- **作者:** Nadim Kobeissi

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1147) | [PDF](https://eprint.iacr.org/2026/1147.pdf)


> **研究背景:** 文章针对TLS 1.3中的两种后量子密钥交换模式进行研究，一种是结合了椭圆曲线Diffie-Hellman (ECDHE) 和机器学习基密钥封装机制(ML-KEM)的混合模式，另一种是仅使用ML-KEM的独立模式。现有的基于Diffie-Hellman的证明不再适用于ML-KEM，因此需要新的安全性分析。
>
> **主要贡献:** 作者扩展了reftls ProVerif模型以包含非交换性的KEM，并对经典ECDHE、独立ML-KEM以及混合模式进行了并发会话的安全性分析。
>
> **达到效果:** 研究结果表明，独立的ML-KEM存在单一故障点，仅在ML-KEM未被攻破时才安全；而混合模式则更稳健，在任一组件存活的情况下保持安全，攻击者必须在同一会话中同时攻破两者才能获取信息。此外，这种单一故障点不仅影响保密性也会影响认证。
>
> **技术梗概:** 研究使用了形式验证工具ProVerif来建模和分析这些密钥交换模式的安全性，并通过非交换性的KEM模型扩展了现有的分析框架。

---
### [推荐] [2026/1186] Butterfly Effect: Multi-Key FHE from Ring-LWR

- **匹配关键字:** homomorphic encryption, LWE, LWR

- **作者:** Mansi Goyal, Ali Raya, Mohakjot Dhiman, Aditi Kar Gangopadhyay

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1186) | [PDF](https://eprint.iacr.org/2026/1186.pdf)


> **研究背景:** 基于LWE的全同态加密方案是构建FHE的主要理论基础，而LWR则提供了另一种简洁高效的替代方案。尽管如此，现有的MKFHE方案多基于Ring-LWE假设，缺乏基于Ring-LWR的实现。
>
> **主要贡献:** 本文提出了两种基于环LWR（Ring-LWR）的MKFHE构造，填补了该领域的空白，并实现了更优的存储和通信成本。
>
> **达到效果:** 通过具体参数化设计，我们的方案支持不同深度的电路，并提供了概念验证实现以证明其有效性。
>
> **技术梗概:** 我们采用了环扩展机制而非传统的密文扩展方式来构建MKFHE，并针对Ring-LWR假设进行了优化。

---
### [推荐] [2026/1188] Rank Ceiling for Twiddle-Perturbation Faults on the Forward NTT

- **匹配关键字:** lattice, post-quantum

- **作者:** Chakshu Gupta

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1188) | [PDF](https://eprint.iacr.org/2026/1188.pdf)


> **研究背景:** NIST标准化了基于格的密钥封装机制(ML-KEM)和数字签名方案(ML-DSA)，作为后量子时代的经典密钥建立和数字签名的替代品，其中NTT的蝴蝶因子是已知的故障攻击面。
>
> **主要贡献:** 论文提供了在任意层中单个蝴蝶因子扰动下信息泄露的确切等级阶梯，揭示了泄漏率，并证明了无论哪个蝴蝶因子被击中，ML-KEM和ML-DSA中的残留不确定性都是相同的。
>
> **达到效果:** 通过精确的等级梯度表征，论文为ML-KEM和ML-DSA提供了单个蝴蝶因子故障下的确切信息泄露量，从而限制了可能的信息泄漏范围。
>
> **技术梗概:** 研究使用了形式验证工具Lean 4进行机器检查，并基于此构建了一个闭合形式的预算模型来分配保护措施。

---
### [推荐] [2026/1191] Accelerating NTRU+ Key Generation via Hierarchical Batch Inversion

- **匹配关键字:** post-quantum

- **作者:** Jonghyun Kim, Haehyun Cho, Jong Hwan Park

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1191) | [PDF](https://eprint.iacr.org/2026/1191.pdf)


> **研究背景:** 在基于KEM的TLS 1.3密钥协商中，客户端为每次连接生成一个新的KEM密钥对，使得密钥生成成为握手过程中的关键路径。对于NTRU+这一基于NTRU问题的KEM，在此路径上的主要成本是计算公钥所需的多项式求逆操作。
>
> **主要贡献:** 本文提出了一种加速NTT域中多项式求逆的方法，通过将基求逆产生的模逆运算收集到一个阶段，并应用蒙哥马利技巧将其数量减少为一次，同时使用分层批处理技术进一步提高指令级并行性。
>
> **达到效果:** 该方法在C和AVX2两种实现下对所有NTRU+参数集进行了评估，特别是在具有最大收益的NTRU+$864参数集中，与非批处理多项式求逆相比，显著减少了计算周期数。
>
> **技术梗概:** 通过将基求逆中的模逆运算合并，并应用蒙哥马利技巧减少其数量；然后使用分层批处理技术进一步优化独立的产品链，从而提高指令级并行性。

---
### [推荐] [2026/1196] Grand Danois: Succinct Multilinear Polynomial Commitments over Lattices

- **匹配关键字:** lattice, post-quantum

- **作者:** Anders Kallesoe, Hamidreza Khoshakhlagh

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1196) | [PDF](https://eprint.iacr.org/2026/1196.pdf)


> **研究背景:** 该研究旨在设计一种适用于多项式承诺方案的后量子密码学方法，以应对潜在的量子计算威胁。
>
> **主要贡献:** 作者提出了一种基于格的新颖多线性多项式承诺方案Grand Danois，并通过引入新的假设和协议改进了验证复杂性和证明大小。
>
> **达到效果:** 该方案实现了多项式验证复杂度和证明大小为多项对数级，具体为$O(\lambda \ell)$，且估计的证明大小约为80-90 KB。
>
> **技术梗概:** 通过采用消失短整数解(vSIS)假设和结构化投影策略，作者设计了一种适应简洁验证的求和检查协议，并将范数界限证明与多项式评估集成到单个协议中以减少通信复杂性。

---
### [推荐] [2026/1199] A Post-Quantum Commitment Scheme from Richelot Isogeny Walks on Superspecial Genus-2 Jacobians

- **匹配关键字:** post-quantum

- **作者:** Nouhou Abdou Idris, Mustapha Hedabou

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1199) | [PDF](https://eprint.iacr.org/2026/1199.pdf)


> **研究背景:** 该研究旨在设计一种后量子承诺方案，基于Richelot超特殊 genus-2 Jacobians上的核标记穿孔 Richelot 弓形走动。
>
> **主要贡献:** 贡献在于提出了一种新的后量子承诺方案，并通过引入核标记来防止已知的产品区域攻击。
>
> **达到效果:** 该方案在特定长度的走动下保持统计隐藏性，并将绑定问题归约为短Richelot自同态问题。
>
> **技术梗概:** 技术上，使用谱界估计 Richelot 图以证明穿孔保留快速混合特性，并通过SageMath原型验证其实用性能。

---
### [推荐] [2026/1208] Preimage sampleable function families without discrete Gaussians

- **匹配关键字:** lattice

- **作者:** Eamonn W. Postlethwaite, Filip Trenkić

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1208) | [PDF](https://eprint.iacr.org/2026/1208.pdf)


> **研究背景:** 本文构建了一种基于$q$-元格子的预像可采样函数族，该族的预像采样问题等价于从简单的多面体中均匀采样单位三角形格子上的点：$\ell_1$和$\ell_\infty$球体的仿射线性变换及其交集的缩放版本。
>
> **主要贡献:** 作者通过改进Kannan–Vempala算法并调整其分析，实现了仅使用均匀位和均匀分布$[0,1]$上的仿射线性变换进行采样的目标，并回答了关于Lee度量中此类函数族构建的问题。
>
> **达到效果:** 基于短整数解问题在不同$\ell_p$范数下的抗碰撞性，本文提出了适用于Lee度量的预像可采样函数族，并通过减少多面体的内半径来解决了一个开放问题。
>
> **技术梗概:** 作者采用并改进了Kannan–Vempala算法进行采样的方法，并通过仿射线性变换和均匀位生成器实现了所需的功能，同时提供了从足够条件构造预像可采样函数族的一般框架。

---
### [推荐] [2026/1209] Latency-Aware, High-Throughput Homomorphic AES Evaluation with CKKS

- **匹配关键字:** homomorphic encryption

- **作者:** Taeseong Kim, Jonghoo Lee, Taeyeong Noh, Jung Hee Cheon, Guillaume Hanrot

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1209) | [PDF](https://eprint.iacr.org/2026/1209.pdf)


> **研究背景:** 研究背景：现有同态AES评估方法在延迟和吞吐量之间存在明显权衡，CKKS方法侧重于高吞吐量而牺牲延迟，TFHE方法则相反。
>
> **主要贡献:** 主要贡献：提出了一种同时优化延迟和吞吐量的同态AES评估方案，实现了单个AES块34ms的解密速度，并且能够一次性处理2048个AES块，提高了吞吐量。
>
> **达到效果:** 达到的效果：第一种变体在NVIDIA RTX-5090上实现了单AES块34ms的延迟，比最近的TFHE基线快4倍以上；第二种变体通过新的$	extrm{GF}(16)$嵌入提高了吞吐量至200KB/s。
>
> **技术梗概:** 技术梗概：采用CKKS同态加密方法，并引入新的$	extrm{GF}(16)$嵌入技术，结合SIMD并行处理，实现了延迟和吞吐量的双重优化。

---
### [推荐] [2026/1215] On the Cryptographic Structure Required for Verifying Qubits

- **匹配关键字:** post-quantum

- **作者:** James Bartusek, Itay Shalit

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1215) | [PDF](https://eprint.iacr.org/2026/1215.pdf)


> **研究背景:** 经典测试在量子设备上检测反交换算子的存在是近期经典验证量子计算进展的关键工具。然而，现有的构造依赖于高度结构化的假设，如陷阱门爪函数。
>
> **主要贡献:** 作者提出了测试非交换性（ToNC）的概念，并证明了它能够从广泛的参数中推导出经典的密钥协议和盲传输。
>
> **达到效果:** 通过ToNC及其与单向函数的结合，作者实现了后量子通信中的密钥协议和盲传输，同时发展了后量子硬核度量定理等工具。
>
> **技术梗概:** 该研究开发了一套新的技术来处理经典通信但对手可能是量子的场景下的后量子密钥协议和盲传输的安全性问题。

---
### [推荐] [2026/1221] Achieving Shannon Capacity for Computationally Bounded Errors

- **匹配关键字:** LWE

- **作者:** George Lu, Jad Silbak, Daniel Wichs

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1221) | [PDF](https://eprint.iacr.org/2026/1221.pdf)


> **研究背景:** 研究背景：在计算受限的环境中，对抗性信道以任意多项式时间引入错误。现有工作通过共享公共随机种子构建了编码和解码程序，在保持较高速率的同时实现了较好的纠错能力，但仍未达到香农容量。
>
> **主要贡献:** 主要贡献：作者首次提出了CCA安全的秘密密钥代码，并通过伪随机代码（PRCs）实现香农容量；同时，提出了一种启发式的将秘密密钥代码升级为种子代码的方法。
>
> **达到效果:** 达到的效果：在二进制字母表中，实现了接近最优的香农容量，速率约为$R \approx 1 - H_2(p)$，对于$p < 1/4$比例的错误。
>
> **技术梗概:** 技术梗概：通过使用伪随机代码（PRCs）和秘密密钥来构建CCA安全的秘密密钥代码，并提出了一种基于编码/解码过程混淆的方法来启发式地升级为种子代码。

---
### [2026/1148] Pushing the boundaries of group-based aggregation with zero-evading generators of low additive complexity

- **作者:** Ariel Gabizon, Dmitry Krachun

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1148) | [PDF](https://eprint.iacr.org/2026/1148.pdf)


> **研究背景:** 研究了零逃逸生成器在计算内积时所需的加法复杂度，以提高基于群的聚合协议的安全性和效率。
>
> **主要贡献:** 提出了一个仅需$O(n^2 + \lambda)$次加法的新构造方法，显著减少了传统方法中至少需要$\Omega(\lambda n/(\log(\lambda n)))$次加法的数量。
>
> **达到效果:** 新构造降低了基于群的承诺方案（如KZG承诺）聚合时的加法复杂度，提高了协议效率。
>
> **技术梗概:** 通过设计具有较低加法复杂性的零逃逸生成器来优化内积计算过程，从而减少所需加法次数。

---
### [2026/1150] The Key Control Security of KDF Combiners

- **作者:** Ritam Bhaumik

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1150) | [PDF](https://eprint.iacr.org/2026/1150.pdf)


> **研究背景:** 研究背景：Bhaumik等人在CRYPTO 2025会议上提出了KDF的密钥控制(KC)安全概念，旨在防范攻击者通过操纵辅助输入来获取预选密钥。本文在此基础上进一步探讨了KDF组合器的结合密钥控制(CKC)安全性。
>
> **主要贡献:** 主要贡献：作者扩展了KC安全性的定义至KDF组合器，并证明了在一定限制下，KDF组合器的CKC安全性可以由其组件KDF的KC安全性推导得出。
>
> **达到效果:** 达到的效果：通过引入CKC安全性概念及其与KC安全性的关系，该研究为评估和设计更安全的KDF组合方案提供了理论基础。
>
> **技术梗概:** 技术梗概：本文采用形式化方法定义了CKC安全性，并通过分析组件KDF的安全性来推导整个KDF组合器的安全特性。

---
### [2026/1158] A Geometric Approach to Quantum Distinguishers

- **作者:** Zhili Wu, Zhenzhen Bao

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1158) | [PDF](https://eprint.iacr.org/2026/1158.pdf)


> **研究背景:** 本文提出了一种结合经典对称密钥密码分析中的几何方法和广义相关提取算法的量子区分器几何框架。
>
> **主要贡献:** 该研究的主要贡献在于提供了一个统一的准备-测量模板，能够恢复多种已知的量子区分器。
>
> **达到效果:** 通过这种方法，作者分析了区分质量稀释的原因，并提供了特定基底下的信号集中机制以恢复二次优势。
>
> **技术梗概:** 技术上，通过单个叠加查询和适当的酉变换操作来准备“相关态”，其幅度是所选基底下几何相关矩阵的元素。

---
### [2026/1181] AICE: An Arithmetic-Oriented Stream Cipher for Heterogeneous Computing

- **作者:** Bishwajit Chakraborty, Jiahui Gao, Kai Hu, Tao Huang, Zhongfeng Niu, Phuong Pham, Wenhan Xu, Guang Zeng, Chenxu Zhao

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1181) | [PDF](https://eprint.iacr.org/2026/1181.pdf)


> **研究背景:** 针对异构计算平台对高吞吐量数据路径的需求，现有高速软件密码算法主要优化了CPU为中心的执行模型，AICE旨在提供一种适用于此类平台的新型算术导向流密码。
>
> **主要贡献:** AICE通过设计新颖的非线性反馈机制和初始化流程，在保持安全性的同时显著提升了在华为昇腾加速器上的吞吐量。
>
> **达到效果:** AICE在昇腾950和昇腾910B4加速器上分别实现了高达114.13 Gbps和55.36 Gbps的单核峰值吞吐率，并且在32个昇腾910B4核心上的吞吐量达到了约1.59 Tbps，远超AES-CTR和SM4-CTR。
>
> **技术梗概:** AICE采用模加、模乘、位或和旋转等算术操作构建非线性反馈机制，并通过多轮初始化和状态更新确保安全性。

---
### [2026/1182] Fast Bounded-Independence Functions and Their Duals

- **作者:** Martijn Brehm, Yuval Ishai, Nicolas Resch

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1182) | [PDF](https://eprint.iacr.org/2026/1182.pdf)


> **研究背景:** 研究快速函数，即由线性大小电路计算的具有随机函数有用性质的函数，以支持密码学应用。
>
> **主要贡献:** 作者构建了常数$t$阶的快速$t$-wise独立哈希函数，并简化并改进了快速码及其共轭的设计，使其满足吉尔伯特-瓦尔沙姆夫界，同时具有可忽略的失败概率和系统编码能力。
>
> **达到效果:** 这些设计支持更快的通用编码器，并实现了最优组合列表解码。此外，它们被用于构建第一个电路复杂度与参与方数量线性相关的完美安全多方计算协议，以及具有最佳渐近电路复杂性的加密矩阵-向量乘积计算协议。
>
> **技术梗概:** 通过构造常数$t$阶的快速线性函数，将任何$t$个线性独立输入映射到均匀且统计上独立的输出来实现上述结果。

---
### [2026/1183] Validity in Responsive Byzantine Agreement

- **作者:** Diana Ghinea, Simon Holmgaard Kamp, Chen-Da Liu-Zhang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1183) | [PDF](https://eprint.iacr.org/2026/1183.pdf)


> **研究背景:** 研究背景在于探索在响应式拜占庭一致协议中的一致性条件，特别是在半同步模型下的一致性特性。
>
> **主要贡献:** 主要贡献是提出了一个关于响应式拜占庭一致协议中一般一致性属性的精确刻画，并证明了非平凡的一致性属性所需的阈值条件。
>
> **达到效果:** 研究结果表明，在认证设置下需要$n>2 t_r+t_s$，在未认证设置下需要$n>3 t_s$，同时提出了满足这些条件的匹配协议。
>
> **技术梗概:** 通过形式化的方法和严格的证明来确定不同一致性属性下的系统阈值，并设计了相应的协议以实现这些特性。

---
### [2026/1184] Public-Key Pseudorandom Codes from Distorted McEliece Assumptions

- **作者:** Victor Dyseryn, Danilo Francati, Daniele Venturi

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1184) | [PDF](https://eprint.iacr.org/2026/1184.pdf)


> **研究背景:** 论文提出了基于扭曲McEliece假设的首个二进制公钥伪随机码（PRC）构造，该构造在面对常量分数替换攻击下具有鲁棒性，并且能够抵抗亚指数时间区分器。
>
> **主要贡献:** 贡献在于引入了一种新的扭曲McEliece假设，并通过使用扩展子码Reed-Solomon码（即Raw Reed-Solomon码）来实现公钥PRC的构造。
>
> **达到效果:** 结果是实现了在面对常量分数替换攻击下具有鲁棒性的公钥PRC，同时满足了亚指数时间区分器下的伪随机性要求。
>
> **技术梗概:** 技术上，通过重新审视Christ和Gunn的McEliece假设蓝图，并使用Raw Reed-Solomon码作为基础，克服了直接使用Raw Reed-Solomon码时遇到的问题。

---
### [2026/1185] A Note on ``Secure and Efficient Data Deduplication in JointCloud Storage''

- **作者:** Zhengjun Cao, Lihua Liu

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1185) | [PDF](https://eprint.iacr.org/2026/1185.pdf)


> **研究背景:** 该研究针对2023年IEEE Transactions on Cloud Computing发表的关于基于RSA和配对密码体制的混合加密认证机制的数据去重方案提出了安全漏洞。
>
> **主要贡献:** 作者指出原方案在不同组运算混淆方面存在缺陷，导致云服务提供商无法正确匹配临时标签与存储标签，进而无法提供请求数据。
>
> **达到效果:** 研究揭示了该方案的安全隐患，并提出明确区分模幂运算和椭圆曲线上点乘法随机化操作的建议以改进方案安全性。
>
> **技术梗概:** 通过分析RSA模幂运算和配对密码体制中的组运算差异，作者提出了具体的修正措施来确保数据去重过程的安全性和效率。

---
### [2026/1187] HEGIDE: A MIMD Oblivious Processor for Private Function Evaluation over CKKS

- **作者:** Jules Dumezy, Nicolas Ye, Pierre-Emmanuel Clet, Olive Chakraborty, Aymen Boudguiga

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1187) | [PDF](https://eprint.iacr.org/2026/1187.pdf)


> **研究背景:** 在FHE（Fully Homomorphic Encryption）允许对加密数据进行计算的同时，保护程序本身的安全性仍然是一个理论和实践上的难题，这迫使实际应用中要么暴露核心逻辑，要么遭受性能损失。
>
> **主要贡献:** 本文提出了基于CKKS方案的Oblivious Processor HEGIDE，通过OSReM（Oblivious Shift Register Memory）创新内存架构解决了FHE-RAM写入的线性复杂度问题，并采用MIMD设计并行评估不同程序线程以提高吞吐量。
>
> **达到效果:** 实验结果表明，该方法实现了每周期6.4毫秒的平均延迟，比现有方案快两个数量级，在吞吐量上提供了可行的解决方案。
>
> **技术梗概:** 通过将内存视为移位寄存器，并利用CKKS打包技术处理不同程序线程，OSReM实现了低延迟、常数时间写入而无需昂贵的全内存重新启动过程。

---
### [2026/1189] Do You Need a Receipt? Anonymous Credential Revocation at Continental Scale via Private Record Certification

- **作者:** Kasra Edalatnejad, Sebastian Faust, Jonas Hofmann, Philipp-Florens Lehwalder, Thomas Schneider

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1189) | [PDF](https://eprint.iacr.org/2026/1189.pdf)


> **研究背景:** 现有的匿名凭证撤销方案通常存在客户端或验证者计算负担重、撤销生效延迟长或需要频繁更新所有用户等问题，这限制了匿名凭证在大规模系统中的应用。
>
> **主要贡献:** 作者提出了一种基于新型私有记录认证（PRC）的高效实时匿名凭证撤销方案，并通过结合私人信息检索和安全多方计算技术构建了PRC。
>
> **达到效果:** 该方案将成本外包给分散化的撤销机构，减少了客户端和验证者的开销，同时确保通信成本在撤销机构中是亚线性的。实验表明系统能在超过10亿凭证的规模下实现亚秒级实时延迟，并且在线运营成本低。
>
> **技术梗概:** 通过结合私人信息检索和安全多方计算技术构建了PRC，实现了用户从服务器管理数据库获取证书而不泄露请求的具体记录。

---
### [2026/1190] CMoSS: Composable Modular Security Specifications Framework

- **作者:** Sara Wrótniak, Hemi Leibowitz, Ewa Syta, Amir Herzberg

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1190) | [PDF](https://eprint.iacr.org/2026/1190.pdf)


> **研究背景:** CMoSS框架旨在通过模块化设计和分析方法，支持密码协议的可组合安全性验证。
>
> **主要贡献:** 该框架扩展了MoSS的方法，允许独立定义协议规范中的各个组件，并实现黑盒子协议的安全组合。
>
> **达到效果:** CMoSS使得能够精确地指定、开发并分析涉及多种攻击者能力、延迟、故障和同步挑战的实际应用密码协议，从而确保其实现的可证明安全性。
>
> **技术梗概:** 通过定义独立的谓词（游戏）来实现模块化规范，并支持实时并发性，CMoSS提供了一种形式化的手段来验证非正式规范的安全性。

---
### [2026/1192] Lower Bounds on Black-Box Constructions of Pseudorandom Functions

- **作者:** Bar Alon, Itai Dinur, Muthuramakrishnan Venkitasubramaniam

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1192) | [PDF](https://eprint.iacr.org/2026/1192.pdf)


> **研究背景:** 研究背景：Goldreich、Goldwasser和Micali在1984年提出了通过伪随机生成器（PRG）构建伪随机函数（PRF）的方法，但至今尚未找到能减少调用次数的黑盒构造方法。
>
> **主要贡献:** 主要贡献：本文证明了对于完全黑盒构造，无论是强PRF还是弱PRF，在非适应性查询下，都不能有少于$o(n/\log n)$和$o(\mathsf{in}/\log\mathsf{in})$次调用PRG的方法。
>
> **达到效果:** 达到的效果：该研究为构建伪随机函数设定了理论极限，并证明了在某些限制条件下，减少调用次数的构造方法是不可行的。
>
> **技术梗概:** 技术梗概：通过引入新的归约技术和分析方法，本文严格证明了上述下限结果。

---
### [2026/1193] Cryptanalytic Properties of Mealy Machines

- **作者:** Zhongfeng Niu, Tim Beyne, Kai Hu, Meiqin Wang

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1193) | [PDF](https://eprint.iacr.org/2026/1193.pdf)


> **研究背景:** 本文提出了一种系统化的计算任意Mealy机器或S函数的密码分析性质的方法，基于几何密码分析方法，提供了一个统一的公式来计算这些函数的任何兼容输入输出分割方式的密码分析属性。
>
> **主要贡献:** 贡献在于提出了一个通用框架来计算Mealy机器和S函数的各种密码分析特性，并通过具体实例展示了该方法的有效性。
>
> **达到效果:** 结果包括对模加、Chi-和ChiChi函数以及SHA-1步函数等重要例子的线性、（准）差分、超度量积分、差分线性和波纹分析属性进行了计算，还提出了Subterranean置换的波纹区分器，并更准确地计算了分区基础下的差分线性攻击的相关性。
>
> **技术梗概:** 技术上采用了几何密码分析方法，并通过输入输出分割兼容性的统一公式来系统化地计算各种密码分析性质。

---
### [2026/1194] Unconditionally Secure MPC for Boolean Circuits with Constant Communication

- **作者:** Yubo Zeng, Kang Yang, Dengguo Feng, Min Zhang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1194) | [PDF](https://eprint.iacr.org/2026/1194.pdf)


> **研究背景:** 研究背景：在大多数现有的安全多方计算（MPC）协议中，为了评估任意布尔电路的通信复杂度已有所改进，但仍然需要较高的通信成本。
>
> **主要贡献:** 主要贡献：本文首次提出了一种针对任意布尔电路的安全多方计算协议，并实现了每门电路仅需常数比特的通信效率。
>
> **达到效果:** 达到的效果：该协议在半诚实对手存在的情况下是无条件安全的，通过进一步增强，在恶意对手的存在下也保持了相同的高效通信特性。
>
> **技术梗概:** 技术梗概：首先构建了一个半诚实对手环境下无条件安全的协议，然后利用特定技术确保了协议对恶意对手同样有效且具有常数比特的通信效率。

---
### [2026/1198] Splittings and Endomorphism Rings

- **作者:** Péter Kutas, Min-Yi Shen

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1198) | [PDF](https://eprint.iacr.org/2026/1198.pdf)


> **研究背景:** 研究背景：寻找给定超奇异椭圆曲线的非平凡自同构是基于曲率密码学中的一个难度假设。
>
> **主要贡献:** 主要贡献：证明了将其归约到找到给定主正交阿贝尔表面分裂的问题，并且通过这种新归约，还证明了在维度二下分裂问题（带有度数限制）与端射影环问题是统计等价的。
>
> **达到效果:** 达到的效果：为基于曲率的密码学提供了一个新的理论框架，增强了对相关安全假设的理解。
>
> **技术梗概:** 技术梗概：利用阿贝尔表面的分裂问题来研究超奇异椭圆曲线的自同构环问题，并证明了两者在统计上的等价性。

---
### [2026/1200] Character Block Encodings for Discrete CKKS: Single-Level LUTs and Low-Depth Arithmetic

- **作者:** Jules Dumezy, Elias Suvanto

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1200) | [PDF](https://eprint.iacr.org/2026/1200.pdf)


> **研究背景:** 在Cheon-Kim-Kim-Song (CKKS)同态加密方案中，功能自举使得离散计算成为可能，但其将LUT评估、模数缩减、噪声清理和密文刷新四个任务融合为单一的固定管道，导致通用LUT的成本与$\log_2 t$成比例，并消耗了大量的模数预算。
>
> **主要贡献:** 作者提出通过改变表示方式而非优化自举过程来解绑这些任务，引入了字符块编码方法，将有限字母表值分布在多个CKKS槽中，形成函数基，使得每个LUT评估仅在一个乘法级别完成，深度与字母表大小无关。
>
> **达到效果:** 这种新的表示方式消除了模数缩减的需要，并且噪声增长独立于字母表大小，在最坏情况下与最小字母表$\mathbb{Z}_2$上的标准离散CKKS噪声增长相同，在典型工作负载下线性增加，比离散CKKS在$t>2$时的表现要好得多。
>
> **技术梗概:** 作者通过引入基于字符的块编码方法，将有限字母表值表示为多个CKKS槽中的坐标，并利用这些坐标的函数基来评估LUT，从而实现了深度独立于字母表大小的LUT评估和模数缩减操作。

---
### [2026/1201] Silentium revisited: Pseudorandom Beaver Triple Expansion

- **作者:** Vincent Rieder, Enrico Sorbera

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1201) | [PDF](https://eprint.iacr.org/2026/1201.pdf)


> **研究背景:** Silentium revisited探讨了在安全多方计算中Beaver三元组的生成问题，这是SPDZ协议中最昂贵的任务。
>
> **主要贡献:** 研究提出了两个理论贡献：一是扩展了二进制域上的Beaver三元组生成方法；二是设计了一种Beaver三元组扩展方案。
>
> **达到效果:** 这些改进使得Beaver三元组的生成更加高效，同时解决了Silentium在实际应用中的问题。
>
> **技术梗概:** 研究采用了Number Theoretic Transform的具体实例化，并提出了Beaver三元组扩展方案来优化预处理阶段。

---
### [2026/1202] Morphic Accumulators and Applications: Optimal Range Proofs, Polynomial Commitments, and Ring Signatures

- **作者:** Dimitrios Papadopoulos, Qiang Tang, Jiajun Xin

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1202) | [PDF](https://eprint.iacr.org/2026/1202.pdf)


> **研究背景:** 现有的基于未知阶群（GUO）的密码学聚合器提供了常量大小的集合成员证明，但由于安全需求需要通过难以分割（DI）哈希函数进行编码，这限制了它们在与相同GUO组中承诺整数相关的现有加密证明技术中的应用。
>
> **主要贡献:** 作者引入了形态聚合器的概念，用离散对数编码替代了难以分割的哈希函数，并证明了这种编码具有内在的难以分割性，同时保持了群同态性质，从而解决了紧凑表示与代数结构之间的基本矛盾。
>
> **达到效果:** 形态聚合器在多个领域实现了渐近最优的设计：范围证明中的验证者时间复杂度为O(n)，证明大小为O(1)，验证时间为O(1)。
>
> **技术梗概:** 通过引入离散对数编码，形态聚合器能够在保持集合绑定承诺的同时，支持其元素上的同态计算。

---
### [2026/1203] Signatures with Post-Compromise Accountability

- **作者:** Dennis Dayanikli, Johannes Lang, Anja Lehmann

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1203) | [PDF](https://eprint.iacr.org/2026/1203.pdf)


> **研究背景:** 传统的签名方案依赖于私钥的秘密性，一旦私钥泄露，所有由该私钥产生的签名将失效，即使这些签名是合法签署的。本文提出了一种新的签名机制——后泄密问责签名（SPCA），旨在提供在私钥泄露后的安全保证。
>
> **主要贡献:** 作者首次正式定义了SPCA及其安全性要求，并提出了两种实现SPCA的构造方法。其中一种方法通过嵌套签名技术实现了签名验证过程中的私钥隐藏，另一种则在此基础上进一步提升了安全性。
>
> **达到效果:** 这两种构造方法均能在私钥泄露后仍保持合法签名的有效性，为数字系统提供了一种新的安全解决方案。
>
> **技术梗概:** 第一种构造基于嵌套签名技术，在外层签名中嵌入内层签名的随机数，而第二种则通过巧妙设计避免了在验证过程中暴露私钥，从而增强了安全性。

---
### [2026/1204] Robust Single-Trace Full-Key Extraction from Million-Point Traces With Cross-Implementation Transfer

- **作者:** Aron Gohr, Friederike Laus, Gregor Leander

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1204) | [PDF](https://eprint.iacr.org/2026/1204.pdf)


> **研究背景:** 针对公钥实现的端到端深度学习侧信道攻击已能在百万样本迹线中实现，但现有方法需要大量计算资源且只能提取部分密钥份额，需额外处理才能成功恢复密钥。
>
> **主要贡献:** 作者提出了一种端到端序列到序列预测方法，能够从单个原始迹线中完整提取256位密钥份额，并结合了激进的迹线压缩和1-D U-Net训练。
>
> **达到效果:** 这种方法在单一GPU上几分钟内完成训练，对SCAAML ECC数据集实现了高准确率，并表现出高度鲁棒性。
>
> **技术梗概:** 该方法通过分离泄漏检测与每个泄漏位置到正确部分的秘密映射，利用合成任务展示了如何绕过神经网络架构和训练方法在大规模多目标或错位提取任务中的固有问题。

---
### [2026/1205] StakeNote: A Proof-of-Stake Protocol for CryptoNote Payments

- **作者:** Bernardo David, Dimitris Karakostas

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1205) | [PDF](https://eprint.iacr.org/2026/1205.pdf)


> **研究背景:** StakeNote旨在结合Proof-of-Stake (PoS)共识机制与CryptoNote的隐私保护支付系统，以提供安全性和匿名性的双重保障。
>
> **主要贡献:** 该研究贡献了一种新的分布式账本协议，通过将Ouroboros Praos与CryptoNote相结合，实现了PoS与隐私保护支付的融合。
>
> **达到效果:** StakeNote继承了Ouroboros Praos的安全性以及CryptoNote的匿名性，并通过概念验证实现展示了其高效性和实用性。
>
> **技术梗概:** 该协议利用Ouroboros Praos确保安全性，同时采用CryptoNote中的环签名技术来保护隐私。

---
### [2026/1206] Scalable, quantum-accessible, and adaptive pseudorandom quantum state and pseudorandom function-like quantum state generators

- **作者:** Rishabh Batra, Zhili Chen, Rahul Jain, YaoNan Zhang

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1206) | [PDF](https://eprint.iacr.org/2026/1206.pdf)


> **研究背景:** 该研究旨在构建可扩展、量子可访问和适应性的伪随机量子态（PRS）及函数似量子态（PRFS）生成器，以满足现代密码学的需求。
>
> **主要贡献:** 作者提出了首个基于量子安全单向函数的可扩展、量子可访问且适应性PRFS构造，并使用更强的量子可访问定义，允许辅助量子输入。
>
> **达到效果:** 该研究不仅提供了新的伪随机量子态和函数似量子态生成器，还推导出多种相关密码学原语，简化了微密码学领域的复杂性。
>
> **技术梗概:** 通过引入等距过程准备任意随机的量子态，并结合更强的量子可访问定义，实现了上述贡献。

---
### [2026/1207] "Sticking their heads out above the parapets": Lived Experiences of Legal Risks in Research (Extended)

- **作者:** Sunoo Park, Daniel R. Thomas

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1207) | [PDF](https://eprint.iacr.org/2026/1207.pdf)


> **研究背景:** 研究指出，过于宽泛的计算机犯罪、知识产权等相关法律会限制重要研究活动，尤其是涉及软件或硬件漏洞识别及数据抓取的研究。尽管学术界对此有广泛的认识，但对其实际影响的理解有限，主要依赖于零星的证据而非系统性研究。
>
> **主要贡献:** 本研究首次通过定性的方法，详细记录了研究人员在面临法律风险时的实际体验及其应对策略，并为政策改革提供了实证依据。
>
> **达到效果:** 研究结果揭示了法律风险对科研活动的具体影响及研究人员如何规避这些风险，为相关政策的制定和改进提供了重要参考。
>
> **技术梗概:** 通过与36名具有英国或美国法律风险经历的研究人员以及8名提供支持的专业人士进行访谈，收集并分析了跨越三十年、涉及130个项目和事件的数据。

---
### [2026/1210] Uncloneable Cryptography in Linear Quantum Memory

- **作者:** Andrew Huang, Omri Shmueli, Vinod Vaikuntanathan, Mark Zhandry

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1210) | [PDF](https://eprint.iacr.org/2026/1210.pdf)


> **研究背景:** 量子密码学利用量子信息来实现经典计算中不可能完成的任务，其中量子态常被用作长期密钥，依赖于量子不可克隆定理确保密钥不会被对手复制。然而，量子态容易退相干，因此持久性量子记忆是量子计算机中最宝贵且最具挑战性的资源之一。
>
> **主要贡献:** 本文的主要贡献在于显著减少了量子秘密密钥的大小，在某些情况下实现了渐近最优的尺寸。我们提出了一种保证完美正确性和另一种支持长消息并行签名算法的方案，并实现了强签名不可压缩性，从而实现公钥量子防火墙方案。
>
> **达到效果:** 通过优化量子签名方案中的量子记忆使用量，本文减少了对持久性量子存储的需求，提高了量子签名协议的安全性和效率。
>
> **技术梗概:** 我们利用了量子态的特性设计了一种新的量子签名方案，并结合了多项式时间内的量子计算技术来减少所需的量子秘密密钥大小。

---
### [2026/1211] Private Information Retrieval: Share Conversions vs. Decoding Polynomials

- **作者:** Amos Beimel, Or Lasri

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1211) | [PDF](https://eprint.iacr.org/2026/1211.pdf)


> **研究背景:** 私有信息检索（PIR）协议允许客户端从分布在多个服务器上的数据库中检索数据而不泄露任何关于所检索数据的信息。现代PIR协议依赖于匹配向量来实现这一目标。
>
> **主要贡献:** 本文通过引入份额转换的概念，将解码多项式的作用进行抽象化，并展示了如何使用份额转换替代解码多项式在PIR协议中的应用。
>
> **达到效果:** 研究结果表明，份额转换可以用于构建具有信息论隐私性的PIR协议，并且可以实现比传统解码多项式更灵活的方案。
>
> **技术梗概:** 通过定义和利用份额转换技术，作者展示了如何从环到有限域进行秘密分享方式之间的转换，从而为PIR协议提供了新的设计思路。

---
### [2026/1212] SecLoRA: Secure Aggregation of Low-Rank Matrix Products via Functional Encryption

- **作者:** Jiangtao Li, Wei Zhang, Chen Gong, Jason (Minhui) Xue, Junqing Gong

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1212) | [PDF](https://eprint.iacr.org/2026/1212.pdf)


> **研究背景:** 联邦学习中通过低秩适应（LoRA）微调大型语言模型面临隐私-效率权衡：低秩因子可能泄露敏感数据，而标准的安全聚合仅限于线性操作。现有解决方案要么牺牲精确度，要么依赖可信第三方，或者在大规模部署时成本高昂。
>
> **主要贡献:** SecLoRA提出了首个实现LoRA更新精确聚合的去中心化框架，并且具有线性通信复杂度。其核心是新颖的密码学原语：可组合多客户端功能加密（PC-DMCFE）。
>
> **达到效果:** SecLoRA确保了跨孤岛部署的实用性，同时实现了矩阵产品的安全和分布式聚合，而不会失去LoRA的线性通信优势，并且防止了时间泄漏。
>
> **技术梗概:** SecLoRA利用PC-DMCFE的独特属性，允许任意配对的密文通过功能密钥计算内积，从而实现精确的安全聚合。此外，它还确保了解密过程是轮次隔离的，以防止时间泄露。

---
### [2026/1213] Another Look at Non-Frameability in Group Signatures for Anonymous Auctions

- **作者:** Cao Shiqi, Keita Emura

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1213) | [PDF](https://eprint.iacr.org/2026/1213.pdf)


> **研究背景:** 非框架性是群签名为匿名拍卖提供的一种重要安全属性，除了匿名性和可追溯性之外，它确保即使敌对手与所有权威（开启者和发行者）合谋也无法伪造签名来陷害诚实用户。
>
> **主要贡献:** 本文从新的角度探讨了非框架性的意义，指出它不仅能保护用户免受陷害，还能保护权威机构不受虚假指控。
>
> **达到效果:** 研究结果表明，在匿名拍卖场景中，非框架性可以有效应对竞标者否认投标行为并指责主办方伪造签名的情况。
>
> **技术梗概:** 通过形式化定义和分析，本文重新审视了非框架性的安全属性，并提出了相应的验证方法以确保其在实际应用中的有效性。

---
### [2026/1216] New Quantum-Classical Algorithm or the Discrete Logarithm Problem over $\mathbb{Z}_{p}^{*}$

- **作者:** Hidenori Kuwakado, Shoichi Hirose

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1216) | [PDF](https://eprint.iacr.org/2026/1216.pdf)


> **研究背景:** 研究背景：Shor提出了利用量子傅里叶变换和周期查找算法在$\mathbb{Z}_{p}^{*}$中高效解决离散对数问题的方法。本文旨在提出一种不依赖于周期性的量子-经典算法，以探索新的解决方案路径。
>
> **主要贡献:** 主要贡献：作者通过将Blum和Micali引入的硬核预言家问题与伯努利分布区分问题联系起来，并利用交换测试实现了这一目标。
>
> **达到效果:** 达到的效果：该算法能够在不依赖量子傅里叶变换的情况下，通过经典计算完成大部分工作，同时结合了量子技术的优势，提供了一种新的离散对数问题求解方法。
>
> **技术梗概:** 技术梗概：算法利用交换测试作为量子子程序，并主要依靠经典计算来实现其功能，展示了量子-经典混合计算在解决复杂数学问题上的潜力。

---
### [2026/1217] Secure Computation against $\mathsf{NC^1}$ Leakage without Secure Hardware

- **作者:** Yuyu Wang

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1217) | [PDF](https://eprint.iacr.org/2026/1217.pdf)


> **研究背景:** 本文解决了Bogdanov等人和Wang关于在无任何硬件保护的前提下，构建能够抵抗\(\mathsf{NC}^1\)泄漏函数的电路的安全性问题。
>
> **主要贡献:** 作者首次提出了一个适用于2自适应\(\mathsf{NC}^1\)泄漏的简短设置抗泄露容忍电路(sAI-LTC)，并通过结合抗泄露编码方案，实现了目标电路。
>
> **达到效果:** 该方法不仅解决了开放问题，还提供了一种无需任何硬件保护即可抵抗\(\mathsf{NC}^1\)泄漏的安全计算机制，并且优化了电路大小。
>
> **技术梗概:** 通过构造sAI-LTC并结合抗泄露编码方案，作者利用非黑盒技术实现了目标效果，同时证明了这种机制可以推导出适用于所有\(\mathsf{NP}\)问题的细粒度多定理非交互式证明系统。

---
### [2026/1218] High-Accuracy, Poisoning-Resilient Frequency Estimation in the Shuffle Model

- **作者:** Shaoqiang Wu, Jingyu Jia, Yikuan Zhu, Xinhao Li, Changyu Dong, Zheli Liu

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1218) | [PDF](https://eprint.iacr.org/2026/1218.pdf)


> **研究背景:** 研究在差分隐私的shuffle模型下频率估计问题，特别是在存在中毒攻击的情况下。现有的协议需要在匿名化前生成灵活的多消息噪声，这可能会放大中毒影响。
>
> **主要贡献:** 提出了一种对称二项式和噪声分布（即$\mathrm{Bin}(n/2,p) + \mathrm{Bin}(n/2,1-p)$），并利用预处理引导噪声生成技术来限制中毒信息的影响。
>
> **达到效果:** 该协议在二元估计中仅需每个用户一次伯努利试验，最多每用户发送2条消息（平均为1.5条），同时将单个受污染用户的最坏情况影响限制在$O(1/n)$。实验表明，在小域工作负载下，与最强基线相比，我们的协议可以减少MAE近两倍，并保持鲁棒性。
>
> **技术梗概:** 通过预处理引导噪声生成技术，平衡地传输模式标志以固定用户在shuffling前的噪声采样行为，从而实现高准确性和抗中毒攻击的能力。

---
### [2026/1219] Algorithms for solving the isogeny problem with oriented elliptic curves

- **作者:** Maria Corte-Real Santos, Arthur Herlédan Le Merdy, Joseph Macula, Michael Meyer, Travis Morrison, Eli Orvis

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1219) | [PDF](https://eprint.iacr.org/2026/1219.pdf)


> **研究背景:** 研究旨在扩展Delfs-Galbraith和SuperSolver算法，解决超奇异椭圆曲线的isogeny问题，并提出适用于更广泛上下文的成本模型。
>
> **主要贡献:** 贡献在于提出了WayFinder框架，该框架能够处理包含$\mathbb{Z}[\ell_1\sqrt{-\ell_2p}]$的更一般性的模曲线，并提供了一种低存储算法来计算两个定向超奇异椭圆曲线之间的isogeny。
>
> **达到效果:** 结果是提出的方法和成本模型提高了解决isogeny问题的效率，为基于isogeny的密码学参数选择提供了潜在应用。
>
> **技术梗概:** 技术上，通过引入更一般的模曲线和低存储算法来扩展搜索范围，并开发了适用于超奇异椭圆曲线定向isogeny计算的新方法。

---
### [2026/1220] Explicit Transformations from Edge-Depth-Robust to Node-Depth-Robust Graphs with Improved Concrete Efficiency

- **作者:** Jeremiah Blocki, Nathan Smearsoll

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1220) | [PDF](https://eprint.iacr.org/2026/1220.pdf)


> **研究背景:** 深度鲁棒有向无环图（DAG）在密码学中是重要组合原语，应用于内存硬函数、空间证明和顺序工作证明。然而，构建具有强具体保证的稀疏节点深度鲁棒图仍然是一个长期挑战。
>
> **主要贡献:** 作者提出了一种新的、效率更高的从边深度鲁棒图到节点深度鲁棒图的转换方法，该方法使用单个超集中器替换每个节点，从而在输入图为显式构造时显著提高了具体效率。
>
> **达到效果:** 通过这种方法，给定一个$(e,d)$-边深度鲁棒图$G$，生成的新图$G'$具有$N' = O(m)$节点、常数入度和$(e/3,\, 2d-1)$-节点深度鲁棒性。
>
> **技术梗概:** 该转换方法通过将每个节点替换为单个超集中器而非ST鲁棒图来实现，从而在保持输入图为显式构造时提高了效率。

---
### [2026/1222] UCX is All You Need: A Universal Transform for Committing Authenticated Encryption

- **作者:** Mihir Bellare, Rishabh Ranjan, Nujud Senan, Basel Alomair

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1222) | [PDF](https://eprint.iacr.org/2026/1222.pdf)


> **研究背景:** 随着新型攻击和应用的出现，需要开发能够将现有认证加密(AE)方案转化为承诺型认证加密(cAE)方案的变换。
>
> **主要贡献:** UCX是一种新颖的变换方法，能够在不依赖于起始方案为标签基的情况下，适用于广泛的AE5框架，并保持UNAE和MRAE安全性。
>
> **达到效果:** UCX在理想密码模型中证明了承诺安全，在标准模型中证明了AE5安全。
>
> **技术梗概:** 通过引入并构建一个新的可调整承诺遮掩器(TCC)作为设计UCX的基础，该TCC具有独立研究价值。

---
### [2026/1223] Neon NTT - (Auto)formalised

- **作者:** Hanno Becker

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1223) | [PDF](https://eprint.iacr.org/2026/1223.pdf)


> **研究背景:** 本文档提供了对Becker等人Neon NTT论文中模算术核心部分的机器检查Isabelle/HOL形式化，包括Barrett和Montgomery减法与乘法理论及其等价性。
>
> **主要贡献:** 贡献在于开发了参数化的Barrett和Montgomery减法与乘法理论，并证明了其正确性和边界定理，确保Neon汇编内核的准确性。
>
> **达到效果:** 结果是实现了针对手写模型底层字节算术的Neon指令内核的手动验证，确保了形式化与非正式描述的一致性。
>
> **技术梗概:** 技术上采用了Claude Opus 4.7和4.8自动形式化工具，并通过LLM-Isabelle集成层生成定义、定理陈述及证明。

---
### [2026/1224] On Arithmetic Private Information Retrieval: Why Code-Based PIR (Usually) Fails

- **作者:** Benny Applebaum, Yuval Ishai, Shahar Shechter

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1224) | [PDF](https://eprint.iacr.org/2026/1224.pdf)


> **研究背景:** 研究了算术私有信息检索（APIR）方案，其中数据库是一个字段元素向量，并且方案对字段进行黑盒使用。主要关注单服务器APIR方案的下载成本下限以及基于编码假设的安全性。
>
> **主要贡献:** 证明了单服务器APIR方案无法实现非平凡的下载成本小于n个字段元素；提出了两种替代模型下的正结果，即通过秘密密钥预处理可以构建计算安全的APIR方案。
>
> **达到效果:** 展示了基于分布式点函数的APIR方案和秘密密钥单服务器PIR方案的算术化方法，并在两服务器或具有秘密密钥预处理的单服务器模型中实现了这些方案；证明了线性代数条件下信息论意义下双服务器APIR方案的存在性，通信量为O(n^1/3)。
>
> **技术梗概:** 通过分析编码假设下的安全性和算术化方法来构建计算安全的APIR方案，并使用线性代数的方法来描述信息论意义下的两服务器APIR方案。

---

## 更新: 2026-06-07 13:46

*新增 11 篇论文 (编号 1126--1136)*

### [推荐] [2026/1127] Verifiable Bootstrapping from Lattice-based Folding

- **匹配关键字:** lattice

- **作者:** Amit Deo, Louis Tremblay Thibault

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1127) | [PDF](https://eprint.iacr.org/2026/1127.pdf)


> **研究背景:** 本文构建并测试了首个基于格的可验证初始化方案（IVC），利用折叠技术支持环上的自定义约束系统，以实现同态加密（FHE）的正确执行证明。
>
> **主要贡献:** 作者引入了一种新颖的CCS关系，能够进行自同构稳定性检查，增强了环上CCS的表现力，并将其应用于折迭方案验证者和TFHE的密文评估操作的算术化。
>
> **达到效果:** 实验表明，该方案与现有技术相比具有更小的证明大小，但证明者和验证者的运行时间显著增加。此外，作者还讨论了基于折叠的IVC方案的安全性，并提出了在随机预言机模型中知识完整性的论证。
>
> **技术梗概:** 通过利用折叠技术实现环上的自定义约束系统，该研究实现了FHE的可验证执行，并通过算术化方法优化了证明过程。

---
### [推荐] [2026/1130] Reassessing the Security of LPN-C and its HHE-Oriented Variants

- **匹配关键字:** homomorphic encryption

- **作者:** Orr Dunkelman, Semira Einsele, Hans Heum, Morten Øygarden, Gerhard Wunder

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1130) | [PDF](https://eprint.iacr.org/2026/1130.pdf)


> **研究背景:** 文章重新评估了基于LPN-C及其面向HHE的变体的安全性，这些变体旨在通过结合对称和同态加密来提高效率。
>
> **主要贡献:** 贡献在于量化了通过拒绝采样施加有界噪声的效果，并扩展了Arora-Ge风格的代数攻击以适应有界噪声环境，从而改进了参数选择的安全评估。
>
> **达到效果:** 研究结果表明，某些参数设置比之前估计的更安全，而在其他情况下，新的代数策略提供了已知的最佳攻击方法。
>
> **技术梗概:** 技术上采用了拒绝采样来控制噪声，并结合Arora-Ge风格的方法分析了有界噪声下的LPN实例解密问题。

---
### [推荐] [2026/1131] Public Key Encryption Secure Against Quantum Leakage

- **匹配关键字:** post-quantum, LWE

- **作者:** Alper Cakan, Fuyuki Kitagawa, Ryo Nishimaki, Manasi Shingane, Takashi Yamakawa

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1131) | [PDF](https://eprint.iacr.org/2026/1131.pdf)


> **研究背景:** 针对现代密码方案中的侧信道攻击，现有研究主要集中在经典泄漏场景下的安全性，而忽视了量子泄漏的安全性。
>
> **主要贡献:** 本文扩展了公钥加密在有界泄漏模型中对泄漏的抵抗定义，以包括量子泄漏，并提出了两种构造：一种使用量子密钥的PKE方案和另一种使用经典密钥的PKE方案。
>
> **达到效果:** 前者能够在存在无界经典泄漏的同时容忍恒定速率（小于0.057）的量子泄漏；后者则在假设多项式安全后量子不可区分性混淆（iO）及单向函数（OWFs）存在的前提下实现了对有界量子泄漏的安全性。
>
> **技术梗概:** 通过引入新的安全性定义并结合多项式安全后量子不可区分性混淆和单向函数等高级加密技术，本文解决了公钥加密在面对量子泄漏时的安全性问题。

---
### [2026/1126] A correlation duet: Correlation attacks on correlation generators

- **作者:** Antoine Joux

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1126) | [PDF](https://eprint.iacr.org/2026/1126.pdf)


> **研究背景:** 针对基于准阿贝尔综合征解码问题的伪随机相关生成器，首次在2025年Asiacrypt会议上使用压缩感知技术进行了攻击。
>
> **主要贡献:** 作者提出了一种新的相关攻击方法，这种方法比之前的攻击更加有效，并且能够恢复具有更大汉明重量的秘密错误多项式。
>
> **达到效果:** 新攻击使得伪随机相关生成器的参数需要进行全面重新评估，特别是FOLEAGE方案。
>
> **技术梗概:** 该研究使用了传统的密码分析工具——相关攻击，并结合了压缩感知技术来提高攻击效率和降低资源消耗。

---
### [2026/1128] Optimized Point Addition Circuits for Elliptic Curve Discrete Logarithms

- **作者:** André Schrottenloher

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1128) | [PDF](https://eprint.iacr.org/2026/1128.pdf)


> **研究背景:** 针对Shor算法对量子计算机在破解RSA公钥加密中的主要威胁，研究者们致力于降低其实现成本。Babbush等人通过优化椭圆曲线离散对数的量子计算电路，在门数量和量子比特数量上实现了显著减少。
>
> **主要贡献:** 本文详细描述了一种逻辑量子电路架构，该架构在secp256k1曲线上达到了与Babbush等人相似的效果，虽然量子比特略有增加但减少了Toffoli门的数量，并提供了通用变体的门计数结果。
>
> **达到效果:** 通过优化点加电路设计，本文实现了对椭圆曲线离散对数问题的有效计算，验证了其在实际应用中的可行性。
>
> **技术梗概:** 该研究采用了逻辑量子电路的设计方法，结合了特定椭圆曲线和通用变体的门计数分析，以实现更高效的量子算法。

---
### [2026/1129] pSquare-hash: A Family of Tweakable Hash Functions for Physically Secure PQ Signatures

- **作者:** Lorenzo Grassi, Mario Marhuenda-Beltrán, Thorben Moos, Fabian Schmid, Matthias Johann Steiner, Hailun Yan

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1129) | [PDF](https://eprint.iacr.org/2026/1129.pdf)


> **研究背景:** 针对NIST推荐的基于哈希的抗量子签名方案，现有实例主要依赖SHA-2或SHA-3家族，但这些标准家族在物理安全方面并不理想。
>
> **主要贡献:** 提出了pSquare-hash，一种专门设计的轻量级可调制哈希函数族，旨在更好地满足基于哈希的签名方案的需求和安全性要求。
>
> **达到效果:** 通过减少置换大小或调用次数，pSquare-hash相比标准连接方法可能具有效率优势，并且其可调制特性有助于物理安全防护。
>
> **技术梗概:** pSquare-hash基于算术化设计，选择特定的素数以优化性能并增强安全性。

---
### [2026/1132] Oblivious Garbling and its Applications

- **作者:** Tomer Ashur, Carmit Hazay, Rahul Satish

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1132) | [PDF](https://eprint.iacr.org/2026/1132.pdf)


> **研究背景:** 传统的加法器方案虽然实现了函数与输入的分离，但暴露了执行方的功能信息，这在功能可能涉及机密或敏感逻辑的情况下成为障碍。
>
> **主要贡献:** 提出了无知识加法器的新范式，在该框架中，加法人仅接收电路拓扑结构的信息并保持对其他一切内容的无知。
>
> **达到效果:** 首次构建了这一概念实例，实现了线性复杂度且无需增加门电路大小，同时在恶意设置下没有渐近开销。
>
> **技术梗概:** 通过设计一种新颖的方法来实现加法器方案中的无知识特性，确保功能信息不被泄露。

---
### [2026/1133] SoK: PIOP-based SNARKs for General Computation

- **作者:** Yonghui Guan, Rihe Zhang, Bin Liu, Tianyu Zhao, Jialu Hao, Antonis Michalas

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1133) | [PDF](https://eprint.iacr.org/2026/1133.pdf)


> **研究背景:** 现代SNARK构造通常结合了Polynomial Interactive Oracle Proof (PIOP)和适当的Polynomial Commitment Scheme (PCS)，通过交互式多项式查询和简洁的承诺来实现高效论证系统，包括紧凑的证明和高效的验证程序。
>
> **主要贡献:** 作者提出了一种统一框架，细化了SNARKs前端与后端的分离，并将其作为单一连贯结构进行分析，引入了lookup arguments和递归证明组合等关键组件。
>
> **达到效果:** 该框架展示了如何将这些组件与前端和后端交互，从而提高效率和适用性。
>
> **技术梗概:** 通过采用Thaler提出的SNARKs前端与后端分解，并在统一视图中整合lookup arguments和递归证明组合技术。

---
### [2026/1134] SPIDER: Two Server Functionality for the Cost of Zero

- **作者:** Ofir Dvir, Kali Hale, Javin Zipkin, Divyakant Agrawal, Dahlia Malkhi

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1134) | [PDF](https://eprint.iacr.org/2026/1134.pdf)


> **研究背景:** 文章介绍了SPIDER和baseSPIDER两种私有信息检索（PIR）方案，旨在改进现有PIR协议的通信复杂度和设计复杂性。
>
> **主要贡献:** 贡献在于提出了baseSPIDER协议，实现了与最优复杂度相当但常数因子更低的性能；SPIDER则无需服务器配合，通过简单转换实现单服务器模式下的隐私保护。
>
> **达到效果:** 结果是两种方案分别在不同场景下提高了PIR效率和适用性，尤其适用于大型数据库查询。
>
> **技术梗概:** 技术上，baseSPIDER采用预处理和存储提示的方法优化通信复杂度；SPIDER通过简单转换适应默认服务器接口，简化设计并减少部署障碍。

---
### [2026/1135] Private Information Retrieval: A Tutorial and Survey

- **作者:** Pranav Shriram Arunachalaramanan, Yue Chen, Ling Ren

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1135) | [PDF](https://eprint.iacr.org/2026/1135.pdf)


> **研究背景:** 私有信息检索（PIR）是一种保护用户隐私的基本原语，使用户能够在不泄露查询内容的情况下从公共数据库中检索所需数据。
>
> **主要贡献:** 文章总结了多个易于理解的PIR方案，并涵盖了关键词查询和批量查询等扩展功能。
>
> **达到效果:** 通过对比不同PIR范式的具体效率，为实际选择提供了指导，并讨论了PIR的实际应用。
>
> **技术梗概:** 文章描述了几种概念上简单的PIR方案，这些方案概括了主流设计范式的核心思想。

---
### [2026/1136] Local Constraints Behind Fourier Analysis of Neural Distinguishers for SPECK32/64

- **作者:** Yunjae Hwang, Sunyeop Kim, Hanbeom Shin, Deukjo Hong, Seokhie Hong, Dongjae Lee, Jaechul Sung, Byoungjin Seok

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1136) | [PDF](https://eprint.iacr.org/2026/1136.pdf)


> **研究背景:** 研究了ARX密码体制中基于神经区分器的傅里叶分析方法，特别是针对SPECK32/64算法。
>
> **主要贡献:** 提出了将局部模加约束与训练后的神经区分器傅里叶分析相结合的新框架，并揭示了主导的傅里叶项背后的特定局部条件和分支效应。
>
> **达到效果:** 通过傅里叶分析，分离出值依赖型变体差分线性项和差异依赖的传统项，解释了它们的偏差；进一步在回转右四元组设置中扩展了分析，并揭示了主导的值依赖型傅里叶特征与具体的进位或借位约束之间的联系。
>
> **技术梗概:** 结合局部模加约束和神经区分器的傅里叶分析技术，通过构建仅以原始密文对为输入的神经区分器进行研究。

---

## 更新: 2026-06-02 20:13

*新增 15 篇论文 (编号 1106--1125)*

### [推荐] [2026/1107] KAT-Seeded Fuzzing of Stateful Hash-Based Signature Verification in liboqs

- **匹配关键字:** post-quantum

- **作者:** Vishnu Ajith, Muhammad Ibrahim, Muhammed Sihan Haroon

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1107) | [PDF](https://eprint.iacr.org/2026/1107.pdf)


> **研究背景:** 针对后量子密码学部署中的状态依赖哈希签名方案（如XMSS和LMS），其验证路径难以有效模糊测试，因为密钥生成远比验证昂贵。
>
> **主要贡献:** 提出了一种基于libFuzzer的结构化方法，利用预计算的已知答案测试(KAT)向量初始化公钥、签名和消息缓冲区，从而无需重复密钥生成即可高效地变异验证输入。
>
> **达到效果:** 通过此方法，在liboqs中实现了并上游了针对XMSS/XMSSMT和LMS/HSS-LMS验证路径的两个模糊测试框架，并发现了一个与OID混淆相关的堆溢出漏洞（CVE-2026-46344），并在liboqs 0.16.0版本中修复。
>
> **技术梗概:** 利用KAT向量初始化验证所需的缓冲区，减少重复密钥生成的开销，并通过轮询字段旋转策略解决短输入LMS模糊测试中的变异分布偏差问题。

---
### [推荐] [2026/1113] HRA-Secure Lattice-based Proxy Re-Encryption without Noise Flooding

- **匹配关键字:** lattice, LWE

- **作者:** Haotian Yin, Jie Zhang, Yuji Dong, Dominik Wojtczak, Eng Gee Lim

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1113) | [PDF](https://eprint.iacr.org/2026/1113.pdf)


> **研究背景:** 现有的基于格的代理重加密方案通常通过噪声泛滥来实现抵抗诚实重加密攻击的安全性，但这会显著增加密文中的噪声并导致参数增长。
>
> **主要贡献:** 本文提出了一种无需统计噪声泛滥即可达到诚实重加密攻击安全性的单跳所有者加密代理重加密方案（oePRE）。
>
> **达到效果:** 该方案通过引入确定性的填充误差而非隐藏继承的噪声，实现了高效重加密，并证明了其在计算上可模拟且满足HRA安全性。
>
> **技术梗概:** 文中引入了带噪音错误泄漏LWE（NEL-LWE）假设来形式化此方法，并基于Leaky-LWE框架定义了所有者加密代理重加密的计算再加密模拟性。

---
### [推荐] [2026/1122] Pseudo-Oil Subspaces and the Geometry of Underdetermined MQ Problems

- **匹配关键字:** post-quantum

- **作者:** Massimo Ostuzzi

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1122) | [PDF](https://eprint.iacr.org/2026/1122.pdf)


> **研究背景:** 随着NIST后量子签名方案标准化进程的推进，多变量后量子签名方案的安全性受到越来越多的关注。
>
> **主要贡献:** 作者重新解释了Hashimoto算法，并设计了一种新的方法来解决欠定多元二次方程问题。
>
> **达到效果:** 该方法通过计算更丰富的伪油子空间结构，将初始问题分解为多个可独立求解的子问题，从而降低了针对MAYO和QR-UOV安全等级I参数集直接攻击的成本。
>
> **技术梗概:** 作者采用几何视角重新审视Hashimoto算法，并优化了一系列离散参数以平衡代数求解与组合搜索之间的权衡。

---
### [推荐] [2026/1125] Threshold Signatures in the Head

- **匹配关键字:** post-quantum

- **作者:** Thibauld Feneuil, Matthieu Rivain, Damien Vergnaud, Auguste Warmé-Janville

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1125) | [PDF](https://eprint.iacr.org/2026/1125.pdf)


> **研究背景:** 阈值密码学通过将信任分散在多个参与方中，使它们能够进行联合加密操作而不重构密钥。然而，基于MPC-in-the-Head (MPCitH) 原理的后量子签名方案要么导致分布式对称计算成本高昂，要么使得签名大小随着签署者数量增加而增长，这给实际应用带来了挑战。
>
> **主要贡献:** 作者提出了一种基于梅克尔树承诺的通用阈值MPCitH签名框架，并引入了阈值多项式承诺方案（TPCS）的概念及其实现方法。这种方法结合了PIOP、TPCS和算术黑盒，构建了一个通用的阈值签名方案，并证明其不可伪造性依赖于组件的安全性。
>
> **达到效果:** 通过使用具体的基于梅克尔树的TPCS，作者实现了适度的签名大小开销，最低可达到每个签署者200字节，在128位安全性水平下。这与之前基于GGM树的方法相比，每个签署者的开销大约为2kB。
>
> **技术梗概:** 该方法通过适应分布式环境中的PIOP+PCS范式，并引入和实例化了阈值多项式承诺方案（TPCS），结合了PIOP、TPCS和算术黑盒来构建一个通用的阈值签名方案。

---
### [2026/1106] AN EFFICIENT VALIDATED ASYNCHRONOUS BYZANTINE AGREEMENT PROTOCOL USING COMMITTEE

- **作者:** Nasit Sarwar Sony

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1106) | [PDF](https://eprint.iacr.org/2026/1106.pdf)


> **研究背景:** 针对多值拜占庭一致协议中存在的效率问题，本文提出了一种验证异步拜占庭一致协议，旨在减少不必要的广播并提高协议的执行效率。
>
> **主要贡献:** 该贡献在于通过随机选择部分节点进行请求广播，并在达成共识时仅考虑选定节点的请求，从而优化了资源使用和提高了协议性能。
>
> **达到效果:** 理论分析表明，此方法能有效降低消息传递和计算开销，但同时也增加了协议执行时间。
>
> **技术梗概:** 该协议采用随机选择部分节点进行广播，并在达成共识时仅考虑选定节点的请求，结合外部验证机制确保了协议的安全性和有效性。

---
### [2026/1108] A Comparative Evaluation of End-to-End-Encrypted Key Retrieval in Backup Protocols

- **作者:** Dennis Funke, Kai Gellert

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1108) | [PDF](https://eprint.iacr.org/2026/1108.pdf)


> **研究背景:** 研究背景：随着端到端加密（E2EE）在备份协议中的应用，用户数据的安全性得到了增强，但同时也带来了新的操作挑战，特别是在设备丢失后如何恢复E2EE保护的备份。
>
> **主要贡献:** 主要贡献：提出了一种结构化的框架来对比评估不同E2EE备份密钥检索方案在易用性、部署性和安全性方面的表现，并对现有简单恢复代码、实际部署和文献中的最新提案进行了分析。
>
> **达到效果:** 达到的效果：研究表明，依赖用户选择的低熵秘密进行恢复的方案可能比使用简单恢复代码的方法，在面对大规模攻击者时提供更弱的安全保护。
>
> **技术梗概:** 技术梗概：通过构建一个综合框架来系统地评估不同E2EE备份密钥检索方案，并明确区分了基于用户自选低熵秘密和高熵材料进行的恢复方法。

---
### [2026/1110] Exploiting Strong Key Bridges: Full-Fledged Automatic Rectangle Attacks on Deoxys-BC and SKINNY

- **作者:** Ling Song, Yincen Chen, Qianqian Yang, Huimin Liu, Lei Wang, Lei Hu, Jian Weng

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1110) | [PDF](https://eprint.iacr.org/2026/1110.pdf)


> **研究背景:** 本文针对TWEAKEY框架下的Deoxys-BC和SKINNY两个标准化密码算法，分析其密钥调度并发现强键桥依赖关系，利用这些依赖进行相关密钥矩形攻击。
>
> **主要贡献:** 作者开发了一种综合约束编程模型来搜索矩形攻击，并结合了状态测试技术、显式最后一轮计算以及强键桥等新组件，显著提升了对这两个算法的分析结果。
>
> **达到效果:** 在Deoxys-BC-384和Deoxys-BC-256上分别将时间复杂度降低了$2^{40}$和$2^{32}$倍，并且延长了现有最长攻击轮数。对于SKINNY，作者的攻击比之前最好结果多了一到两轮。
>
> **技术梗概:** 通过结合状态测试技术、显式最后一轮计算以及利用强键桥依赖关系，开发了一个统一的约束编程模型来寻找矩形攻击。

---
### [2026/1111] Identity-Based Revocable and Linkable Ring Signature

- **作者:** Muyuan Wang

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1111) | [PDF](https://eprint.iacr.org/2026/1111.pdf)


> **研究背景:** 现有可撤销和可链接环签名（$\mathsf{RLRS}$）方案存在依赖于PKI带来的证书管理负担、计算或通信开销随环大小线性增长以及通常假设完全受信任的RA等问题，限制了其在大规模场景中的应用。
>
> **主要贡献:** 提出了基于身份的可撤销和可链接环签名（$\mathsf{IB\text{-}RLRS}$）的概念，并设计了一个无需可信设置、具有对数级签名字节大小的安全方案。
>
> **达到效果:** 该方案能够确保真实签名者的身份始终可以被提取，且恶意RA无法诬陷未参与签名生成的真实用户。
>
> **技术梗概:** 基于IEEE P1363标准，采用新颖的环签名构造方法，证明了其在随机预言模型下的安全性。

---
### [2026/1112] DeepProve: Verifiable End-to-End Large Language Model Inference

- **作者:** Nicolas Gailly, Ismael Hishon-Rezaizadeh, Tianyi Liu, Nicholas Mainardi, Dimitrios Papadopoulos, Charalampos Papamanthou, Christodoulos Pappas, Shravan Srinivasan, Zack Youell, Yupeng Zhang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1112) | [PDF](https://eprint.iacr.org/2026/1112.pdf)


> **研究背景:** 大语言模型（LLMs）在广泛的人工智能服务中取得了显著成功，但其巨大的计算和内存需求使其难以部署到本地硬件上。因此，用户通常依赖不可信的云基础设施提供商来执行模型推理，这导致了验证返回结果真实性的挑战。
>
> **主要贡献:** DeepProve 是首个能够在不可信云服务器上对整个大语言模型推理进行全面验证（即对于提示生成的所有标记）的系统，利用零知识证明（ZKPs）。它通过认证输出序列的正确性而非将昂贵的推理计算电路化来实现端到端验证。
>
> **达到效果:** DeepProve 通过使用求和检查协议和查找论证等核心构建块，实现了对 GPT-2 和 Gemma 等模型中所需的所有操作（如多头注意力和层归一化）正确性的高效证明，从而达到了全面验证大语言模型推理的目的。
>
> **技术梗概:** DeepProve 采用了求和检查协议和查找论证等技术，避免了将昂贵的推理计算电路化的需要，从而实现了在云服务器上对整个生成序列进行端到端验证。

---
### [2026/1114] Counterexamples to the Low-Norm Nullstellensatz Hypothesis

- **作者:** Alex Lombardi

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1114) | [PDF](https://eprint.iacr.org/2026/1114.pdf)


> **研究背景:** 本文旨在通过构造反例来挑战Low-Norm Nullstellensatz Hypothesis（LNNH），该假设在多项式分解领域具有重要地位。
>
> **主要贡献:** 作者提供了多项式族的实例，证明了在特定条件下LNNH不成立，即存在系数$L^1$范数为1的多项式$f$，但其任何分解形式$\sum_i p_i \cdot q_i$都需满足$\sum_i ||q_i||_1 = 2^{\Omega(n)}$。
>
> **达到效果:** 这些反例揭示了当$d$为素数时，一类特定函数对于可能推翻LNNH至关重要。
>
> **技术梗概:** 通过构造指示函数$f(x) = f_C(x)$及其在$\mathbb Z_d^n$子空间上的推广形式来构建反例。

---
### [2026/1115] The Fact of the MATTER: Efficient Hardware Accelerators for Wide-Block Memory Encryption

- **作者:** Shubham Namdeo Shende, Utsav Banerjee

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1115) | [PDF](https://eprint.iacr.org/2026/1115.pdf)


> **研究背景:** 随着大数据应用如人工智能和机器学习的发展，需要新的大带宽内存技术，这推动了宽块内存加密的需求及其高效实现。
>
> **主要贡献:** 作者探索并比较了基于MATTER的不同硬件架构设计空间，包括基于轮次、展开和流水线的实现方式。
>
> **达到效果:** 研究结果提供了不同配置下MATTER在功率、性能、面积和能量消耗方面的详细对比分析。
>
> **技术梗概:** 使用7nm FinFET ASIC标准单元库进行数字综合，评估了针对新兴边缘计算系统特定内存加密硬件要求的架构适用性。

---
### [2026/1117] On the Secrecy of the Encapsulation Coin in ML-KEM

- **作者:** Madjid G. Tehrani, William J Buchanan, Mouad Lemoudden

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1117) | [PDF](https://eprint.iacr.org/2026/1117.pdf)


> **研究背景:** 研究背景：ML-KEM标准要求在每次封装过程中生成一个新的32字节密币，共享秘密是公钥和该密币的确定性函数。本文探讨了实际应用中密币的安全性保护情况。
>
> **主要贡献:** 主要贡献：通过实验分析了六个未修改库（OpenSSL 3.5, wolfSSL 5.9, AWS-LC, Go 1.26, Bouncy Castle 1.83, CIRCL）和一个从头开始的参考实现，揭示了密币恢复的可能性。
>
> **达到效果:** 达到的效果：研究发现，在未经过FIPS-140-3验证配置的情况下，密币的安全性依赖于惯例而非设计，允许外部不可见且参数可控的可预测性。
>
> **技术梗概:** 技术梗概：通过实验对比分析了不同库在密钥封装过程中的实现细节，并提出了两种方法来利用密币的可预测性。

---
### [2026/1119] Packed Pre-Constructed PVSS for Randomness Generation and E-Voting

- **作者:** Karim Baghery, Eleftheria Makri, Dheeraj Kumar Suryakari

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1119) | [PDF](https://eprint.iacr.org/2026/1119.pdf)


> **研究背景:** 预构建的可验证秘密共享（PPVSS）通过要求经销商发布共享秘密的承诺或加密，增强了传统的PVSS，提供了更高效的多种密码协议构造方法。
>
> **主要贡献:** 作者提出了Packed Pre-constructed PVSS (3PVSS)方案，允许经销商在一个多项式中编码多个秘密，同时保持预构建属性。
>
> **达到效果:** 通过两种不同的3PVSS构造，作者展示了如何在不同应用场景下优化通信和验证效率，并扩展了普遍可验证的随机数生成协议。
>
> **技术梗概:** 第一种构造使用单个承诺表示所有共享秘密，适用于需要高效通信的应用；第二种构造为每个秘密发布独立承诺，提供更高的灵活性以支持独立验证需求。

---
### [2026/1120] Pushing Collision Attacks on SHA-2 to 39 Steps

- **作者:** Yingxin Li, Fukang Liu, Haifeng Qian, Jinwei Zhu

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1120) | [PDF](https://eprint.iacr.org/2026/1120.pdf)


> **研究背景:** SHA-2家族是美国联邦标准的一部分，主要包括SHA-256和SHA-512。尽管这些哈希函数在实际应用中至关重要，但Li等人在CRYPTO 2026提出的方法仅能针对37步SHA-2进行碰撞攻击，未能达到38步。
>
> **主要贡献:** 本文作者改进了搜索程序以找到适用于38步SHA-256和SHA-512的高质量差分特征，并利用特殊形状的差分特征采用meet-in-the-middle方法实现了内存高效的碰撞攻击。
>
> **达到效果:** 该研究首次成功实现了针对38步SHA-256和SHA-512的碰撞攻击，时间复杂度分别为$2^{104.3}$和$2^{125.4}$，且内存复杂度可忽略不计。此外，还改进了先前针对36步和37步SHA-2的碰撞攻击方法。
>
> **技术梗概:** 通过分析38步差分特征的独特形状，并利用meet-in-the-middle技术实现高效的内存使用，从而成功推进了SHA-2的碰撞攻击至39步。

---
### [2026/1121] Security Amplification via Robust Indistinguishability Combiners

- **作者:** Benny Applebaum, Nir Bitansky, Nathan Geier

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1121) | [PDF](https://eprint.iacr.org/2026/1121.pdf)


> **研究背景:** 研究旨在通过鲁棒不可区分组合器来增强密码学原语的安全性，特别是在统计和计算设置下，解决现有技术的局限性。
>
> **主要贡献:** 提出了一个新的鲁棒不可区分组合器框架，该框架扩展了先前工作的覆盖范围，并证明了其自然地充当安全放大器。
>
> **达到效果:** 结果包括在单次查询情况下将鲁棒组合器应用于计算环境中的功能加密，并首次实现了功能加密的安全放大器，解决了相关领域的开放问题。
>
> **技术梗概:** 通过构建新的鲁棒不可区分组合器框架，该框架能够处理多种候选构造并生成安全的最终构造，同时考虑了“好随机性”和“坏随机性”的影响。

---

## 更新: 2026-06-01 14:21

*新增 49 篇论文 (编号 1055--1105)*

### [推荐] [2026/1056] Multivariate Polynomial Inference in a Cryptographic Setting

- **匹配关键字:** lattice, homomorphic encryption

- **作者:** Ramona Corbeanu, Diana Maimut, George Teseleanu

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1056) | [PDF](https://eprint.iacr.org/2026/1056.pdf)


> **研究背景:** 本文扩展了一维多项式推理到多变量设置，针对通过重复加法和乘法递归构建的二元多项式的方法。
>
> **主要贡献:** 作者提出了基于多项式插值的第一种方法以及依赖于求解模背包问题的第二种基于格的技术。
>
> **达到效果:** 这两种方向都提供了自然且实用的一般化，并对基本操作进行了详细的数学结构分析，这些操作是构建块，例如在全同态加密方案中。
>
> **技术梗概:** 第一种方法利用多项式插值技术，而第二种方法依赖于求解模背包问题的格基技术。

---
### [推荐] [2026/1058] Efficient MPC-Based Modulus Conversion for Threshold FHE Decryption

- **匹配关键字:** lattice, homomorphic encryption

- **作者:** Ivan Damgård, Sebastian Kolby, Claudio Orlandi, Stanislas Pawlak

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1058) | [PDF](https://eprint.iacr.org/2026/1058.pdf)


> **研究背景:** 本文提出了在算术多方计算（arithmetic MPC）中不依赖位分解的新技术，用于在不同模数之间的秘密共享值转换。
>
> **主要贡献:** 贡献了三种变体协议：适用于幂次模数的简单协议、源模数任意且目标模数为素数的协议以及通过中间素数模数实现的目标模数通用协议。
>
> **达到效果:** 这些协议在统计意义上的普遍计算安全（statistical UC security）下对抗恶意对手，实现了高效的门限全同态加密解密，并避免了噪声泛滥的问题。
>
> **技术梗概:** 技术上采用了常数轮次的开销和少量预处理步骤，在算术黑盒模型中实现，可基于任何支持基本模运算的MPC协议进行实例化。

---
### [推荐] [2026/1060] An Improved Hybrid Dual Attack on LWE with Sparse Secrets and its Application to FHE

- **匹配关键字:** homomorphic encryption, LWE

- **作者:** Lei Bi, Yijian Liu, Xianhui Lu, Junjie Luo, Kunpeng Wang

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1060) | [PDF](https://eprint.iacr.org/2026/1060.pdf)


> **研究背景:** 基于学习误差（LWE）问题的现代密码学方案，如全同态加密（FHE），依赖于稀疏三元秘密实例，但这些实例易受攻击。
>
> **主要贡献:** 提出了一种新的混合双攻算法，结合了May的MITM算法的不同列表构造和哈希函数，有效解决了原有攻击中的效率瓶颈。
>
> **达到效果:** 该新方法在FHE参数范围内表现出更优的效果，并且不依赖于存在争议的独立性假设，从而增强了攻击的有效性和可靠性。
>
> **技术梗概:** 通过系统分析May MITM算法的不同变体，并采用改进的假设检验算法来增强攻击效果。

---
### [推荐] [2026/1064] Post-Quantum Security of Practical Correlation-Robust Hashing

- **匹配关键字:** post-quantum

- **作者:** Akinori Hosoyamada, Haruhisa Kosuge, Keita Xagawa

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1064) | [PDF](https://eprint.iacr.org/2026/1064.pdf)


> **研究背景:** 文章探讨了在量子计算环境下，基于块密码的抗相关稳健哈希函数的安全性。
>
> **主要贡献:** 作者证明了Matyas-Meyer-Oseas (MMO)及其变体\(\widehat{\mathsf{MMO}}\)和$\mathsf{EncFF}$在量子理想密码模型中的多用户可调整参数抗相关稳健性和带泄漏的特性。
>
> **达到效果:** 这些结果不仅保证了无泄漏和单用户的安全性，还推导出CR和TCR对于MMO以及CR、CCR、TCR和TCCR对于\(\widehat{\mathsf{MMO}}\)和$\mathsf{EncFF}$的量子随机置换模型下的安全性。
>
> **技术梗概:** 研究采用了量子理想密码模型来分析这些哈希函数在面对量子对手时的安全性，确保了它们在实际应用中的可靠性。

---
### [推荐] [2026/1071] Event Algebras and Applications to Cryptography

- **匹配关键字:** lattice

- **作者:** Konstantin Gegier, Ueli Maurer

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1071) | [PDF](https://eprint.iacr.org/2026/1071.pdf)


> **研究背景:** 文章探讨了离散步骤模型中事件的代数结构，这些模型在计算机科学等多个领域广泛存在。
>
> **主要贡献:** 作者引入了事件代数的概念，并证明了其公理精确且最小地捕捉了离散步骤模型中事件的抽象数学结构。
>
> **达到效果:** 通过事件不等式，文章展示了多个密码学及其他领域的基本陈述可以直接从特定的通用事件不等式推导出来。
>
> **技术梗概:** 使用了布尔分配格的概念，并引入了一个额外的操作符$∸$来定义事件代数中的关系。

---
### [推荐] [2026/1072] Proactive Secret Sharing without Erasures

- **匹配关键字:** post-quantum

- **作者:** Alexandru Cojocaru, Aggelos Kiayias, Yu Shen, Petros Wallden

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1072) | [PDF](https://eprint.iacr.org/2026/1072.pdf)


> **研究背景:** 研究背景：在移动对手模型中，秘密共享需要定期刷新以保持安全性。传统方法假设可以在刷新后安全擦除私人状态，但在实际操作中这可能难以实现。因此，探索无需擦除即可实现主动秘密共享（PSS）的方法变得尤为重要。
>
> **主要贡献:** 主要贡献：作者通过利用一次性签名和后量子经典可提取见证加密技术，提出了一个在仅需经典通信的情况下实现无擦除主动秘密共享的方案，并定义并构建了阈值一次性解密的概念。
>
> **达到效果:** 达到的效果：该方案不仅解决了传统PSS中需要安全擦除的问题，还通过结合后量子安全功能见证加密使得秘密可以在不显式重建的情况下使用。
>
> **技术梗概:** 技术梗概：利用一次性签名和后量子经典可提取见证加密技术，在无需实际进行秘密恢复的前提下实现了主动秘密共享，并定义了阈值一次性解密的概念。

---
### [推荐] [2026/1076] Decentralizing Traitor Tracing: A Multi-Authority Approach

- **匹配关键字:** LWE

- **作者:** Rishab Goyal, Alex Snyder, Saikumar Yadugiri

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1076) | [PDF](https://eprint.iacr.org/2026/1076.pdf)


> **研究背景:** 传统密钥托管的恶行追踪方案依赖单一受信任机构，这在去中心化的广播网络中是不兼容的。因此，需要一种新的分布式模型来实现恶行追踪。
>
> **主要贡献:** 提出了多权威恶行追踪（MA-TT）方案，该方案将任何多权威属性基加密（MA-ABE）与新引入的分布式混合功能加密（DMFE）相结合，实现了去中心化的恶行追踪。
>
> **达到效果:** 通过使用LWE构建DMFE，并结合已知的MA-ABE方案，成功设计了MA-TT方案，确保即使有任意数量的权威机构被破坏，也能保持语义安全性和可追溯性。
>
> **技术梗概:** 该方案采用了分布式混合功能加密和属性基加密相结合的技术，通过LWE构建DMFE，并结合单密钥同态私钥约束PRF实现去中心化的恶行追踪。

---
### [推荐] [2026/1077] Authenticated and Incremental Single-Server Private Information Retrieval

- **匹配关键字:** LWE

- **作者:** Pengfei Lu, Zengpeng Li, Mei Wang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1077) | [PDF](https://eprint.iacr.org/2026/1077.pdf)


> **研究背景:** 该研究旨在解决单服务器认证私有信息检索（Authenticated PIR）中的通信效率和增量更新问题，现有方案要么在线通信开销高，要么缺乏有效的增量机制。
>
> **主要贡献:** 作者提出了两种新的单服务器认证PIR方案LWE-AuthPIR和DDH-AuthPIR，并首次实现了具有子线性在线通信的此类方案；此外，还提出了一种支持单条目即时更新及周期性更新场景下高效行聚合的新方案LWE-AuthIncPIR。
>
> **达到效果:** 实验结果显示，对于大型数据库中的少量数据更新，LWE-AuthIncPIR显著减少了预处理计算时间和通信开销，分别达到19-88倍和2.9倍的效率提升。
>
> **技术梗概:** 研究采用了基于学习误差（LWE）和决策性Diffie-Hellman（DDH）假设的安全证明方法，并结合了高效的行聚合技术以优化增量更新过程。

---
### [推荐] [2026/1078] Post-Quantum HAWK Signature Acceleration with RISC-V-Based Hardware-Software Co-Design

- **匹配关键字:** lattice, post-quantum

- **作者:** Rishabh Shrivastava, Utsav Banerjee

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1078) | [PDF](https://eprint.iacr.org/2026/1078.pdf)


> **研究背景:** 随着量子计算技术的进步，推动了后量子密码学（PQC）算法的发展。HAWK是一种基于格的新型数字签名方案，在NIST PQC标准制定过程中被选为第三轮候选算法之一，具有紧凑的密钥和签名大小，并且避免使用浮点运算，非常适合资源受限的应用场景。
>
> **主要贡献:** 本文通过对HAWK在Vex RISC-V处理器上的软件运行时分析，识别出最耗计算资源的操作，并提出了一种基于硬件-软件协同设计的方法来加速这些操作，从而提高了签名验证的速度并减少了面积-时间-产品值。
>
> **达到效果:** 通过使用Vex RISC-V自定义函数单元和定制指令，实现了约3倍的加速效果以及40%的面积-时间-产品值减少，在Xilinx Artix-7 FPGA上进行了实现验证。
>
> **技术梗概:** 通过对HAWK签名计算和验证过程中的关键操作进行分析，并结合Vex RISC-V处理器的特点，设计了多种轻量级硬件-软件协同加速方案。

---
### [推荐] [2026/1079] Witness Pseudorandom Functions for Vector Commitments and Applications

- **匹配关键字:** LWE

- **作者:** Rishabh Bhadauria, Pedro Branco, Nico Döttling, Sanjam Garg, Guru-Vamsi Policharla

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1079) | [PDF](https://eprint.iacr.org/2026/1079.pdf)


> **研究背景:** Witness pseudorandom函数（WPRF）是一种具有附加公共评估模式的伪随机函数，其输出对未提供有效NP证明的人保持伪随机性。这种强大的对象目前仅从假设中构建，这些假设意味着不可区分混淆。
>
> **主要贡献:** 本文提出了一个基于特定语言的向量承诺WPRF构造，该构造依赖于配对群的标准假设，并且是完全黑盒的。
>
> **达到效果:** 此构造使得我们能够解决安全计算中的几个开放问题：实现了总通信复杂度为$2k+\mathsf{poly}(\lambda)$的率-1压缩盲目传输协议；构建了接近最优的压缩私有集合交集，其平均通信复杂度接近$\lambda$比特/元素。
>
> **技术梗概:** 通过利用特定语言和配对群假设，实现了WPRF构造，并将其应用于解决安全计算中的开放问题。

---
### [推荐] [2026/1081] From Perfect to Approximate Hints: Efficient LWE Secret Recovery Leveraging Low Hamming Weight

- **匹配关键字:** lattice, homomorphic encryption, LWE

- **作者:** Minki Hhan, Ga Hee Hong, Jiseung Kim, Changmin Lee, JeongHwan Lee

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1081) | [PDF](https://eprint.iacr.org/2026/1081.pdf)


> **研究背景:** LWE问题是基于格的密码学中的基石，广泛应用于多种加密方案的安全性。然而，使用稀疏秘密时，可能会因侧信道攻击泄露部分信息而降低安全性。
>
> **主要贡献:** 本文提出了利用低汉明重量的秘密恢复算法，能够在较少的提示下有效破解LWE问题，特别关注于近似或完美提示，并证明了在实际参数集上该方法的有效性。
>
> **达到效果:** 通过实验和理论分析，作者表明仅需$O(h \log_2 h)$个提示即可实现秘密恢复，显著减少了所需提示的数量，从而提高了效率。
>
> **技术梗概:** 本文采用了一种新的算法框架，结合了Gaussian Approximation Assumption（高斯逼近假设）来处理稀疏秘密的LWE问题，并通过实际参数集验证了其有效性。

---
### [推荐] [2026/1084] BRaccoon: Concurrently Secure Blind Lattice Signatures from Raccoon

- **匹配关键字:** lattice, post-quantum, homomorphic encryption

- **作者:** Lucjan Hanzlik, Mark Manulis, Marzio Mula, Alan Pulval-Dady, Tjerand Silde, Daniel Slamanig

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1084) | [PDF](https://eprint.iacr.org/2026/1084.pdf)


> **研究背景:** 盲签名是隐私保护应用如电子现金、匿名凭证和电子投票的核心机制。然而，现有的后量子密码学中的构造通常遵循两种模式之一：非交互式零知识证明或通过Fiat-Shamir变换从身份方案获得，这些方法导致签名与标准签名不兼容。
>
> **主要贡献:** BRaccoon是首个在保持并发安全的同时生成与标准签名语法相同的格基盲签方案。该方案基于无拒绝的格基签名方案Raccoon，并将Fuchsbauer和Wolf提出的‘从签名假设获得盲签’方法扩展至格。
>
> **达到效果:** BRaccoon实现了与普通签名兼容且具备并发安全性的目标，显著提升了其在实际应用中的灵活性和互操作性。
>
> **技术梗概:** 通过在承诺阶段引入混淆，并利用线性同态加密结合非交互式零知识证明来确保正确的挑战和响应生成。

---
### [推荐] [2026/1086] A Machine-Checked EUF-CMA Proof for the Hybrid Fiat-Shamir Signature Scheme

- **匹配关键字:** post-quantum

- **作者:** Sara Zain

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1086) | [PDF](https://eprint.iacr.org/2026/1086.pdf)


> **研究背景:** 该研究针对Bindel和Hale提出的FS-FS混合签名方案，该方案结合了两个独立的Fiat-Shamir组件，并通过共享挑战实现了一种强安全性和验证性，但其EUF-CMA安全性未被证明。
>
> **主要贡献:** 作者首次提供了FS-FS混合签名方案的机器检查EUF-CMA安全证明，在随机预言模型中使用EasyCrypt形式化，并参数化为抽象的sigma协议接口；该证明适用于任何异构FS基对，经典或后量子。
>
> **达到效果:** 研究证明了两个对称的安全性界限，分别针对每个组件独立验证，确保当任一组件EUF-CMA安全时，整体安全性成立；FS-FS-Schnorr推论确认结果非空洞。
>
> **技术梗概:** 通过在随机预言模型中使用EasyCrypt形式化，并识别出两个隐藏的证明义务——共享懒惰预言机的日志不变性和模块限制框架论证，从而减少了假设数量并提高了证明的有效性。

---
### [推荐] [2026/1088] FlipFields-New Building Blocks for  Cryptograpic Primitives?

- **匹配关键字:** post-quantum

- **作者:** Christopher Wolf

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1088) | [PDF](https://eprint.iacr.org/2026/1088.pdf)


> **研究背景:** 本文提出了一种新的代数结构FlipFields，旨在为后量子密码学提供潜在的替代构建块。
>
> **主要贡献:** 作者定义了两种结构：FlipInts和FlipPolys，并探讨了它们在Unbalanced Oil and Vinegar、Learning with Errors和Saber等方案中的应用。
>
> **达到效果:** 研究表明，尽管这些新结构具有潜力，但某些密码学原语可能不适合使用FlipFields或难以调整。
>
> **技术梗概:** 通过从自然数和一元多项式环中导出，作者展示了如何利用这些新的代数结构来构建后量子密码方案。

---
### [推荐] [2026/1090] How To Track Qubits Through Space and Time (Or: Sailing in a Quantum Boat)

- **匹配关键字:** post-quantum

- **作者:** James Bartusek, Zikuan Huang, Leo Orshansky, Henry Yuen

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1090) | [PDF](https://eprint.iacr.org/2026/1090.pdf)


> **研究背景:** 现有量子位置验证的安全定义仅确保部分敌对者位于声称的位置，这为分布式团队通过联合模拟证明者来规避位置密码学中‘在某地’的含义留下了可能性。
>
> **主要贡献:** 作者提出了更强的定位验证概念——量子本地化，并展示了它如何自然引出轨迹验证的概念，即通过空间和时间追踪量子信息。
>
> **达到效果:** 他们构建了基于量子锚态的量子本地化和轨迹验证协议，并证明其安全性在经典或acles（理想混淆）模型中成立，可以在实际模型中使用后量子不可区分混淆实现。
>
> **技术梗概:** 该研究利用了通用子集态的概念进行扩展，并提出了功能本地化概念以确保敌对者只能在指定的时间空间点计算秘密函数。

---
### [推荐] [2026/1091] Practical Homomorphic LSTM via Programmable Bootstrapping

- **匹配关键字:** homomorphic encryption

- **作者:** Thomas Crasson, Nathan Cassereau, Florian Méhats

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1091) | [PDF](https://eprint.iacr.org/2026/1091.pdf)


> **研究背景:** 传统的深度学习模型在处理敏感的序列数据时，如自然语言，需要将数据发送到不可信服务器进行集中处理，这导致了隐私与性能之间的权衡。全同态加密（FHE）能够直接在加密数据上进行计算，但标准神经网络移植到FHE中会遇到严重的延迟瓶颈，尤其是在连续非线性激活函数占据大部分计算预算的情况下。
>
> **主要贡献:** 本文提出了一种TFHE优化的递归结构——盲突触门循环单元（BSLSTM），通过与密码学框架协同设计，用高效的多阈值可编程重新加密范式替代了昂贵的连续非线性激活函数。
>
> **达到效果:** 在标准自然语言处理任务上，BSLSTM实现了128个标记序列推理延迟5.2秒的结果，显著优于传统同态方法的同时保持了竞争力的准确率，并且每次重新加密操作的成本为211微秒，展示了低延迟、全同态推断的实际可行性。
>
> **技术梗概:** 通过与可编程重新加密框架协同设计BSLSTM网络结构，本文利用多阈值可编程重新加密机制替代了传统模型中的连续非线性激活函数，从而大幅降低了计算成本和推理延迟。

---
### [推荐] [2026/1094] Asymmetric Message Franking in the Plain Model: Generic and Efficient Constructions

- **匹配关键字:** post-quantum, LWE

- **作者:** Milan Gonzalez-Thauvin, Keitaro Hashimoto

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1094) | [PDF](https://eprint.iacr.org/2026/1094.pdf)


> **研究背景:** Asymmetric Message Franking (AMF)旨在为安全消息应用提供具有隐私保护的内容审核功能，但现有方案多在随机预言机模型下工作，缺乏实际部署所需的简洁性和安全性。
>
> **主要贡献:** 该研究首次提出了一个通用的AMF构造方法，并基于非对称配对群构建了一个具体实例，实现了更小的签名大小和更高的效率。同时，还提出了一种后量子安全的AMF方案。
>
> **达到效果:** 通过上述贡献，该工作不仅提高了AMF在普通模型下的安全性与效率，还展示了其在实际应用中的可行性。
>
> **技术梗概:** 研究采用了公钥加密、签名以及NP语言的ZAP证明系统来构建AMF，并基于非对称配对群设计了具体方案以优化性能。

---
### [推荐] [2026/1098] A gentle introduction to lattice-based cryptography

- **匹配关键字:** lattice

- **作者:** Alfred Menezes

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1098) | [PDF](https://eprint.iacr.org/2026/1098.pdf)


> **研究背景:** 本文旨在为高级本科生和初年级研究生介绍基于格的密码学，特别是量子安全的Kyber密钥封装机制和Dilithium签名方案。
>
> **主要贡献:** 文章提供了理解Kyber和Dilithium为何被视为基于格的密码系统的数学背景，并深入探讨了底层格问题的计算难度。
>
> **达到效果:** 通过本文，读者能够掌握基于格的密码学基础知识，并了解Kyber和Dilithium的工作原理及其安全性基础。
>
> **技术梗概:** 文章采用易于理解的方式介绍了复杂的数学概念和技术细节，使非专业背景的读者也能理解。

---
### [推荐] [2026/1099] Lynx: Symmetric Primitive for Shorter and Faster VOLE-in-the-Head Signatures

- **匹配关键字:** post-quantum

- **作者:** Lin Jiao, Hongsen Yang, Hongrui Cui, Yituo He, Yonglin Hao, Xiaojie Guo, Qunxiong Zheng, Jiang Zhang, Yu Yu, Kang Yang

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1099) | [PDF](https://eprint.iacr.org/2026/1099.pdf)


> **研究背景:** VOLE-in-the-Head（VOLEitH）框架是设计后量子数字签名的一种有前景的方法，但现有的对称原语未能充分利用该框架的特性，导致效率低下。
>
> **主要贡献:** 作者提出了一种名为Lynx的VOLEitH友好的对称原语，优化了所需的VOLE相关性数量，从而提高了基于VOLEitH的签名方案的效果。
>
> **达到效果:** 基于Lynx设计的后量子签名方案Lynxer，在公共密钥大小和签名大小方面比现有最佳方案减少了25%至51%，显著提升了效率。
>
> **技术梗概:** Lynx采用多分支结构，结合非线性组件定制化处理和线性层策略性交织，以减小证词长度、多项式度数及有限域乘法次数，并增强安全性。

---
### [推荐] [2026/1102] Finite-Field Arithmetic in CKKS

- **匹配关键字:** homomorphic encryption

- **作者:** Tim Seuré, Elias Suvanto

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1102) | [PDF](https://eprint.iacr.org/2026/1102.pdf)


> **研究背景:** 该研究旨在利用CKKS同态加密技术在具有小特征素数p的有限域F_{p^r}上实现高效的算术运算，通过引入两种互补的密文表示方式来优化计算过程。
>
> **主要贡献:** 作者提出了一种基于CKKS的有限域F_{p^r}上的同态算术方法，并设计了两种编码方案以支持加法和乘法操作。
>
> **达到效果:** 实验结果显示，该方法在多次乘法运算中实现了显著的速度提升，最高可达178倍，特别是在特征素数p较小且扩展度r较大的情况下表现更优。
>
> **技术梗概:** 通过同态方式在两种编码间切换，并结合现有的CKKS自举技术来管理计算的正确性与效率。

---
### [推荐] [2026/1103] Jevil: A Catastrophic-Failure-by-Design Signature Scheme

- **匹配关键字:** post-quantum

- **作者:** Nadim Kobeissi

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1103) | [PDF](https://eprint.iacr.org/2026/1103.pdf)


> **研究背景:** 研究背景：现有的后量子时代一次性签名方案在安全性上存在渐进下降的问题，缺乏一个明确的安全阈值。
>
> **主要贡献:** 主要贡献：Jevil 是首个后量子且透明（无需设置）的一次性签名方案，具有严格的密钥恢复悬崖特性。
>
> **达到效果:** 达到的效果：当签发次数超过预设值时，整个秘密多项式将被公开恢复，实现灾难性失败的设计要求，并提供约68字节的公钥、32字节的私钥和40-500KB的签名。
>
> **技术梗概:** 技术梗概：Jevil 基于秘密多项式与多项式承诺的次数绑定，确保即使恶意选择公钥也无法绕过这个限制。

---
### [2026/1055] Extending FRIDA Beyond Unique Decoding for Free

- **作者:** Nicolas Mohnblatt, Benedikt Wagner

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1055) | [PDF](https://eprint.iacr.org/2026/1055.pdf)


> **研究背景:** 本文扩展了FRIDA方法，使其超越唯一解码半径的限制，从而构建更高效的可用性采样方案。
>
> **主要贡献:** 作者定义了一种新的开集一致性属性，并证明了该属性不依赖于代码的独特解码半径。
>
> **达到效果:** 通过应用此新属性，作者成功地将批处理FRI协议应用于数据可用性采样方案中，从而减小了承诺大小。
>
> **技术梗概:** 研究采用了对FRIDA编译器的新型安全分析，并结合最近关于FRI协议的研究成果来实现上述目标。

---
### [2026/1057] Computer-Aided Proof for Extended Generalized Feistel Networks

- **作者:** Yuchao Chen, Chun Guo, Muzhou Li, Shuo Peng, Hao Lei, Guang Zeng, Meiqin Wang

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1057) | [PDF](https://eprint.iacr.org/2026/1057.pdf)


> **研究背景:** 研究背景：(多分支)广义费舍尔网络(GFN)能够通过使用小域的非线性组件来构建分组密码，已被广泛应用于各种分组密码中。然而，对于扩展广义费舍尔网络(EGFN)，确定足够的轮数以达到伪随机置换(PRP)和强伪随机置换(SPRP)安全性通常非常困难。
>
> **主要贡献:** 主要贡献：作者提出了AutoEGFN工具，这是一个计算机辅助证明方法，能够为各种EGFN变体确定满足PRP和SPRP安全性的轮数。该工具通过计算三个参数$r_1$、$r_2$和$r_3$来实现这一目标。
>
> **达到效果:** 达到的效果：通过应用AutoEGFN到多个结构中，如Type-1/2 GFN、YI11的Type-1 GFN、DFLM19的GFN等，证明了该工具的有效性，并为这些结构确定了满足安全性要求的轮数。
>
> **技术梗概:** 技术梗概：AutoEGFN通过计算三个参数来确定EGFN的安全轮数，其有效性和正确性通过详细的安全证明正式确立。

---
### [2026/1059] Threshold Traitor Tracing with Partial-Insider Resilience

- **作者:** Jan Bormet, Hussien Othman

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1059) | [PDF](https://eprint.iacr.org/2026/1059.pdf)


> **研究背景:** 针对阈值加密中合谋者利用部分解密信息构建非法解码器以逃避追踪的问题，现有研究存在局限性。
>
> **主要贡献:** 本文提出了首个在更强模型下具备抵抗部分内部人攻击的阈值叛徒追踪方案，并且不依赖于可信经销商。
>
> **达到效果:** 该方案能够在合谋者访问部分解密服务时保持可追踪性，有效防止了合谋者和外部买家通过输入额外信息来构建解码器以逃避追踪。
>
> **技术梗概:** 通过非交互零知识证明的知识提取技术，将针对有效密文的追踪能力扩展到任意密文上。

---
### [2026/1061] S4 Is All You Need

- **作者:** Donald Beaver

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1061) | [PDF](https://eprint.iacr.org/2026/1061.pdf)


> **研究背景:** 研究背景：本文提出了使用四张牌的完全洗牌来实现一对一保密传输（1-of-2 Oblivious Transfer），这是首次利用唯一元素集实现两方秘密计算，突破了以往受限置换和人工重复符号牌的研究限制。
>
> **主要贡献:** 主要贡献：作者开发了新的“租用”和“筛选”技术，并展示了设计模式和协议生成参数，为信息论置换与计算单向性的解耦提供了系统化的途径。
>
> **达到效果:** 达到的效果：该研究不仅实现了高效的保密传输，还建立了从保密传输到密钥交换协议的联系，促进了更广泛且新颖的多方计算（MPC）协议的设计、洞察和简化。
>
> **技术梗概:** 技术梗概：通过几何对称性分析，作者设计了一种基于四面体边缘分割的新颖协议，并提出了十ancy技术和narrowing技术来实现保密传输。

---
### [2026/1062] Pairing-Based Registered ABE for Boolean Formulas with a Linear-Size CRS

- **作者:** Roy Stracovsky, Brent Waters, David J. Wu

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1062) | [PDF](https://eprint.iacr.org/2026/1062.pdf)


> **研究背景:** 注册属性加密（RABE）是一种通用的ABE形式，其中取消了中央可信密钥发行者，转而使用一个不可信的关键曲馆。现有研究致力于提高基于对称配对的RABE效率和表达能力。
>
> **主要贡献:** 本文提出了第一个支持一般策略且具有线性大小公共参考字符串（CRS）的基于配对的注册属性加密方案。
>
> **达到效果:** 该方案实现了静态安全性，并基于$q$-型假设证明了其安全。
>
> **技术梗概:** 通过设计一种新的聚合机制，将用户公钥和属性透明地聚合为一个短的主公钥，从而实现线性大小的CRS。

---
### [2026/1063] The Cost of Intelligence: Proving Machine Learning Inference with Zero-Knowledge

- **作者:** Ryan Cao, Nick Cosby, Vishruti Ganesh, Ende Shen, Daniel Shorr, Benjamin Wilson

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1063) | [PDF](https://eprint.iacr.org/2026/1063.pdf)


> **研究背景:** 当前零知识证明系统在处理计算密集型的人工智能算法时的具体局限性尚未得到充分理解。
>
> **主要贡献:** 本文通过对比多种零知识证明系统对多层感知机（MLPs）的性能，揭示了这些系统的瓶颈，并为实际应用提供了参考。
>
> **达到效果:** 研究展示了不同零知识证明系统在处理大型和深层神经网络时的时间和内存消耗差异，明确了其适用范围。
>
> **技术梗概:** 通过基准测试多种零知识证明系统并分析其在不同规模MLPs上的表现来评估它们的性能瓶颈。

---
### [2026/1065] Formal Analysis and Verification of DigiLocker with Tamarin

- **作者:** Nayan Kakade, Aditya Mundada, Raghvendra Rohit

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1065) | [PDF](https://eprint.iacr.org/2026/1065.pdf)


> **研究背景:** Digilocker作为印度数字公共基础设施的关键组成部分，依赖于OAuth 2.0、HMAC、数字签名和加密存储等协议，需要通过形式验证来确保其安全性。
>
> **主要贡献:** 研究使用Tamarin Prover对DigiLocker的身份验证和文档处理工作流进行了形式化建模与验证，并针对多种安全属性进行了正式规格说明和验证。
>
> **达到效果:** 研究表明，在理想假设下，DigiLocker的协议设计满足了这些安全属性的要求；但在受控凭证泄露场景中，敏感值如API密钥或digilockerid的泄露可能导致可利用的攻击路径。
>
> **技术梗概:** 研究采用了Dolev–Yao对手模型来建模OAuth 2.0授权代码流程、PKCE绑定、基于发行者的文档检索机制以及文档推送工作流等。

---
### [2026/1066] Breaking Slope and Structure Restrictions:  Broadening Hard-Label Cryptanalytic Extraction of PReLU Neural Networks

- **作者:** Ruijie Ma, Yi Chen, Jiarui Zhang, Hongbo Yu, Xiaoyun Wang

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1066) | [PDF](https://eprint.iacr.org/2026/1066.pdf)


> **研究背景:** 研究了在硬标签设置下PReLU神经网络模型参数提取的问题，这是最具挑战性的设置。现有的攻击方法存在两个根本限制：可学习的斜率被限制为小于1，并且不适用于扩展的PReLU神经网络。
>
> **主要贡献:** 提出了两种新技术和一个重要发现，首次打破了这两个限制。具体包括提出了一种新的网络同构‘翻转与缩放’，以及针对扩展PReLU神经网络的新神经元签名恢复方法。
>
> **达到效果:** 通过实验验证了提出的攻击方法在数百个扩展的PReLU神经网络上的正确性和有效性，不仅克服了现有攻击方法的限制，还为未来工作提供了灵感。
>
> **技术梗概:** 采用了‘翻转与缩放’技术打破斜率限制，并发现了扩展PReLU神经网络内部状态的线性约束条件，提出了针对扩展PReLU神经网络的新神经元签名恢复方法。

---
### [2026/1068] Self-Guarding Arbitrary Cryptographic Primitives and 2PC Protocols

- **作者:** Daniele Friolo, Andrea Reale, Daniele Venturi

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1068) | [PDF](https://eprint.iacr.org/2026/1068.pdf)


> **研究背景:** 研究背景：Fischlin和Mazaheri在IEEE CSF '18中提出了自卫加密协议的概念，作为对抗算法替换攻击的对策。
>
> **主要贡献:** 主要贡献：本文提出了一种通用的自卫方案，可以在单一可信初始化设置下支持无限次执行，并且可以应用于任何加密原语和两方计算协议。
>
> **达到效果:** 达到的效果：该方案能够在不依赖多次初始化的情况下，持续保护用户的算法实现免受恶意篡改的影响，同时保持正确性。
>
> **技术梗概:** 技术梗概：通过使用可验证计算编译器辅助，实现了对任意加密原语和两方计算协议的自卫封装与校验机制。

---
### [2026/1069] ISAC Privacy: Challenges and Solutions for 6G

- **作者:** Onur Gunlu, Stefano Tomasin, Joao P. Vilela, Francesco Chiti, Prajnamaya Dass, Angeliki Alexiou, Utz Roedig

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1069) | [PDF](https://eprint.iacr.org/2026/1069.pdf)


> **研究背景:** ISAC技术通过集成感知与通信功能，有望提升未来网络性能并支持外部服务，但同时也带来了超出通信内容保密性的隐私挑战。
>
> **主要贡献:** 作者将隐私敏感的ISAC数据分为三个层次，并讨论了内部和外部应用中的隐私问题及解决方案方向。
>
> **达到效果:** 该研究为6G部署中如何保护个人隐私提供了分类框架和潜在解决方案，有助于满足未来网络的隐私要求。
>
> **技术梗概:** 通过定义不同的感知级别来组织数据，并基于此对内、外部ISAC应用进行分析，识别并讨论相关隐私挑战。

---
### [2026/1070] Revisiting Security Definitions of Sender-Anamorphic Encryption

- **作者:** Yuichi Tanishita, Takahiro Matsuda, Kanta Matsuura

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1070) | [PDF](https://eprint.iacr.org/2026/1070.pdf)


> **研究背景:** 研究背景：发送者异形加密是一种允许发送者在不被权威机构察觉的情况下，将替代消息嵌入密文中的密码学原语。现有工作对这种加密的安全性定义存在不足，未充分考虑挑战密文生成过程中使用的随机性的威胁。
>
> **主要贡献:** 主要贡献：重新定义了发送者异形加密的安全性，确保挑战密文中使用的随机性也提供给攻击者，并研究现有方案是否满足新的安全观念。
>
> **达到效果:** 达到的效果：通过改进后的安全性定义，更全面地评估了现有发送者异形加密方案的脆弱性和可靠性。
>
> **技术梗概:** 技术梗概：采用形式化方法重新构建安全定义，引入随机性分析以增强对抗攻击的能力。

---
### [2026/1073] SoK: Impermanent Loss, An Unavoidable Fee or a Controlled Phenomenon?

- **作者:** Arad Kotzer, Ori Rottenstreich

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1073) | [PDF](https://eprint.iacr.org/2026/1073.pdf)


> **研究背景:** 研究探讨了自动做市商(AMM)协议下流动性提供者面临的独特市场风险——即无常损失(IL)，并综述了其主要理论模型、实证证据及缓解策略。
>
> **主要贡献:** 文章统一了IL的主要理论模型，总结了来自领先DeFi协议的发现，并回顾了包括协议层面调整和金融工程方法在内的缓解措施。
>
> **达到效果:** 研究揭示了不同视角下的反复出现的成本、复杂性和安全性权衡，并指出了管理IL系统性影响的开放问题，以确保去中心化流动性提供既对参与者有利又可持续。
>
> **技术梗概:** 综述涵盖了恒定函数和集中流动性AMM市场制作人，并综合分析了DeFi协议的研究成果及缓解方法。

---
### [2026/1075] Asymptotically Optimal Distance-Tail Bounds for Large-Field RAA Codes

- **作者:** Majid Khabbazian

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1075) | [PDF](https://eprint.iacr.org/2026/1075.pdf)


> **研究背景:** RAA码结合了简单的线性时间编码过程和强大的距离特性，适用于经典编码理论及现代密码学应用如基于代码的多项式承诺、zkSNARKs和伪随机相关生成器。现有的具体分析主要针对二元域，但在大域中需要随着块长度增长的字段大小的距离保证，这使得现有方法在大域情况下失效。
>
> **主要贡献:** 作者提供了大域RAA码族\(G=RP_1AP_2A\)的最佳尾部距离界证明，并证明了匹配的大域下界，表明上界在对数因子内是最佳的。同时，还证明了二元域的对应下界，进一步明确了二元域尾部行为。
>
> **达到效果:** 通过上述分析，作者为大域RAA码族提供了精确的距离界，解决了现有方法在大域情况下的不足，并且对于特定重复因子和领域大小条件，给出了最佳上界和下界。
>
> **技术梗概:** 采用覆盖间隙证明方法来处理大域中的取消效应，从而获得尖锐的尾部边界。

---
### [2026/1080] Pushing the Limit of Memory-efficient Collision Attack Framework for SHA-2

- **作者:** Yingxin Li, Fukang Liu, Gaoli Wang, Jiali Shi

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1080) | [PDF](https://eprint.iacr.org/2026/1080.pdf)


> **研究背景:** SHA-2哈希函数因其广泛应用而受到持续的安全关注，尽管已有工具和框架提高了内存效率的碰撞攻击能力，但实际攻击仅限于较少步骤。
>
> **主要贡献:** 研究者通过精心选择特定的消息差异，并利用开源的SAT/SMT自动化工具，改进了38/39步半自由开始碰撞攻击的策略。
>
> **达到效果:** 实现了对35步SHA-256和SHA-512的第一个实际碰撞攻击，分别提高了4和6个步骤；当$i\in\{1,2\}$时，理论上可达到36/37步的碰撞攻击。
>
> **技术梗概:** 研究采用了选择特定消息字节注入差异，并结合SAT/SMT自动化工具搜索差分特征的技术方法。

---
### [2026/1082] Compact Yet Fast: An Efficient d-Order Masked Implementation of Ascon

- **作者:** Mattia Mirigaldi, Maurizio Martina, Guido Masera

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1082) | [PDF](https://eprint.iacr.org/2026/1082.pdf)


> **研究背景:** Ascon被NIST选为轻量级加密标准，广泛应用于资源受限设备中，需要同时具备高性能和抗侧信道攻击能力。
>
> **主要贡献:** 提出了一种动态配置硬件防护措施的设计方案，并引入了具有双重功能的掩码组件，支持任意安全级别并最大限度地提高每轮吞吐量。
>
> **达到效果:** 实验结果表明该实现满足安全性要求，并在所有保护级别的吞吐量与面积比方面表现出色。
>
> **技术梗概:** 通过利用Ascon模式级结构，在关键操作中采用动态可重构的硬件防护措施，同时并行处理多数据路径以加速批量计算。

---
### [2026/1083] When KGC Meets Curator: New Paradigm of Registered ABE and FE

- **作者:** Ziqi Zhu, Jun Zhao, Kai Zhang, Junqing Gong, Haifeng Qian

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1083) | [PDF](https://eprint.iacr.org/2026/1083.pdf)


> **研究背景:** 功能加密（FE）是一种细粒度控制加密数据访问的密码学工具，传统FE依赖于中心可信权威机构发放密钥，存在安全风险。注册功能加密（Reg-FE）通过用户自行生成密钥并登记公钥至保管人来实现无信任模型。
>
> **主要贡献:** 本文提出了委托型注册功能加密（Delegated Reg-FE），这是一种新的注册范式，允许某些授权机构为其各自的经典FE子系统发放密钥。
>
> **达到效果:** 该研究构建了四种委托型注册功能加密方案，涵盖线性函数和策略检查的组合功能，并实现了混合信任模型。
>
> **技术梗概:** 通过重新定义密钥托管为功能性机制而非安全问题，该模型在上层采用无信任模式去除密钥托管，而在每个授权机构的子系统中保持局部全信任并保留密钥托管机制。

---
### [2026/1085] Autonomous LLM-Orchestrated Side-Channel Extraction Against Fully Unrolled and Masked Architectures

- **作者:** Mani Rupak Gurram, Daniel Ifeoluwa Idowu, Yamini Swetha Nadella, Nouf Nur Nabilah, Sarita Bista, Mohamed Chouikha, Annamalai Annamalai, Akshay “AK” Raghavendra Kulkarni

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1085) | [PDF](https://eprint.iacr.org/2026/1085.pdf)


> **研究背景:** 针对全展开和掩码架构的自主LLM调度侧信道提取方法，旨在克服传统时间侧信道分析（SCA）在面对算法噪声时的不足。
>
> **主要贡献:** 提出了一种利用大语言模型代理进行差分功率评估的新框架，成功从161,000个门电路的全展开AES-128核心中提取了组合泄漏信息。
>
> **达到效果:** 通过动态切换到零状态差分功率隔离方法，实现了超过r=0.318的最佳相关性，并自主生成了16个独特的物理到逻辑路由映射。
>
> **技术梗概:** 该框架利用单通道基线减法技术从全局功耗记录中数学消除多轮算法噪声，从而实现目标组合泄漏的隔离。

---
### [2026/1087] Low-Norm Nullstellensatz Hypothesis for the AND Code is False

- **作者:** Zhengzhong Jin

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1087) | [PDF](https://eprint.iacr.org/2026/1087.pdf)


> **研究背景:** 该研究针对AND码的低范Nullstellensatz假设提出了挑战，旨在通过多项式分解来验证其有效性。
>
> **主要贡献:** 作者提供了第一个关于Nullstellensatz反驳在{\pm1}基下的低范下界，并改进了证明以提高清晰度。
>
> **达到效果:** 研究证明了一个指数级的低范下界，推翻了之前的假设，并扩展了对Nullstellensatz反驳的理解。
>
> **技术梗概:** 通过构造一个双线性泛函并利用二次形式的秩来限制傅里叶相关性进行分析。

---
### [2026/1089] Faster Polynomial Evaluations for SIMD FHEs and Application to BGV in HElib

- **作者:** Jiachen Zhao, Jiang Zhang, Binwu Xiang, Songyu Wu, Yi Deng, Dengguo Feng

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1089) | [PDF](https://eprint.iacr.org/2026/1089.pdf)


> **研究背景:** 现有FHE方案在评估多项式时，对于非幂次基数的情况效率较低，Paterson–Stockmeyer方法虽然有效但并非最优。
>
> **主要贡献:** 作者提出了一种新的多项式评估算法，在任意非幂次基数下实现对数级乘法复杂度，并优化了密文模数大于2的情况下的计算效率。
>
> **达到效果:** 该算法在HElib中实现了BGV方案的数字提取多项式的评估，相比现有最佳工作提高了1.22-2.16倍的速度。
>
> **技术梗概:** 通过改进现有的启发式算法和引入新的优化策略，实现更高效的多项式评估。

---
### [2026/1092] The Equivalence of Two Quadratic Based IBEs

- **作者:** George Teseleanu

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1092) | [PDF](https://eprint.iacr.org/2026/1092.pdf)


> **研究背景:** 本文探讨了两个看似不同的基于身份的加密方案，指出它们实际上是等价的。
>
> **主要贡献:** 贡献在于证明了这两个方案在本质上是相同的，并且指出了它们之间的唯一区别在于优化目标不同。
>
> **达到效果:** 结果是通过改进Joye的方案，在公钥中添加最多一个整数的情况下，实现了更好的加密复杂度，同时保持与Zhao等人的方案相同的带宽要求。
>
> **技术梗概:** 技术上，作者通过对Joye方案进行加速处理，展示了如何在不牺牲带宽效率的前提下提高加密速度。

---
### [2026/1093] Anonymous yet Verifiable Privacy-preserving Demand Response

- **作者:** Rosario Giustolisi, Emad Heydari Beni, Daniele Marletta, Maryam Sheikhi Garjan

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1093) | [PDF](https://eprint.iacr.org/2026/1093.pdf)


> **研究背景:** 需求响应（DR）机制通过使消费者根据网络运营商的信号调整其用电量来提高电网可靠性，特别是基于激励的DR计划因其能提供更高的用户参与度而更有效。然而，这些计划在隐私保护方面存在不足，因为它们需要智能电表披露用户的能耗基线和模式以确定奖励。
>
> **主要贡献:** 本文提出了一种隐私保护方案，该方案支持基于激励的需求响应计划，并确保用户数据和身份的保密性。
>
> **达到效果:** 实验结果表明，该方案在大规模用户群体中具有实际可行性，并能提供数据隐私、参与隐私以及公共可验证性。
>
> **技术梗概:** 通过设计一种匿名但可验证的隐私保护机制，结合零知识证明技术来实现用户的能耗信息不被泄露，同时保证聚合商能够验证用户的响应行为以发放奖励。

---
### [2026/1095] Key Transport over Untrusted QKD Relay Networks

- **作者:** Sebastian Clermont, Antoine Gansel, Patrick Struck

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1095) | [PDF](https://eprint.iacr.org/2026/1095.pdf)


> **研究背景:** 量子密钥分发(QKD)能够实现信息论意义上的安全对称密钥交换，但其范围有限。现有的长距离QKD网络依赖于可信的中继节点，任何一个节点的妥协都会导致整个密钥的安全性受到威胁。
>
> **主要贡献:** 提出了一种基于主动秘密共享与一对一时间垫加密相结合的关键传输协议，该协议在多层中继节点之间进行密钥分发和重组，从而消除了对单一可信中继节点的依赖。
>
> **达到效果:** 通过游戏化安全模型证明了该协议在半诚实敌手控制每层最多$t{-}1$个节点的情况下是信息论意义上的安全的，并且能够抵御跨层攻击。
>
> **技术梗概:** 结合主动秘密共享和一对一时间垫加密技术，通过多层中继节点的密钥分发与重组机制确保了安全性，依赖于单一层内最大可能被攻破的节点数量而非总节点数。

---
### [2026/1096] Toward zkSNARK-assisted Isogeny-based Cryptography

- **作者:** Yi-Fu Lai, Luciano Maino

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1096) | [PDF](https://eprint.iacr.org/2026/1096.pdf)


> **研究背景:** 零知识证明是现代隐私保护系统的基本构建块，但在基于曲率的密码学中，现有的零知识证明构造要么局限于小度数的曲率链，要么效率低下。这限制了这些关系在通用证明系统中的支持。
>
> **主要贡献:** 本文旨在使 zkSNARKs 实际上能够用于更广泛的曲率关系，而不仅仅是经典的曲率路径知识语言。通过利用优化后的 Vélu 样式公式，我们提供了 $3^m$-和 $4^n$-曲率的高效 R1CS 编码及其屏蔽评估。
>
> **达到效果:** 我们的工具在签名、SQISign 和公钥加密设计（如 POKÉ）中得到了实际应用。实验结果表明，在各种 NIST-1 素数设置下，证明大小受到约束。
>
> **技术梗概:** 我们基于 Vélu 样式公式提供了 $3^m$-和 $4^n$-曲率及其屏蔽评估的高效 R1CS 编码，并提出了特殊度数 q(2^e - q) 的非光滑曲率的 R1CS，其中 q 为奇数。

---
### [2026/1097] Schnorr-like Signatures in the Non-Observable Random Oracle Model

- **作者:** Marian Dietz, Dennis Hofheinz

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1097) | [PDF](https://eprint.iacr.org/2026/1097.pdf)


> **研究背景:** Schnorr签名方案及其变体是效率最高的基于群的数字签名方案之一，具有紧凑的签名形式。然而，它们的安全性归约通常不紧，并需要强随机预言机模型的支持。
>
> **主要贡献:** 作者定义了一类“Schnorr-like”签名方案，并在非可观察随机预言机模型下证明了其安全性，表明这些方案的安全性归约不可能紧。
>
> **达到效果:** 研究结果表明，对于此类基于群的假设，不存在紧凑的安全性归约。同时展示了存在非紧安全性的方案和更广义定义下的紧安全性方案。
>
> **技术梗概:** 研究采用了元归约方法，并引入了一种新的“过滤”技术，这些技术可能具有独立的研究价值。

---
### [2026/1100] Adaptively Secure (Aggregatable) PVSS from Standard Assumptions

- **作者:** Renas Bacho, Yanbo Chen, Julian Loss

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1100) | [PDF](https://eprint.iacr.org/2026/1100.pdf)


> **研究背景:** Publicly verifiable secret sharing（PVSS）是阈值密码学中的一个基本原语，允许经销商通过公开可验证的转录将秘密S分发给一组n个参与者。任何t+1个参与者的子集可以使用其单独份额重建完整秘密S，而t或更少份额则不提供关于S的信息。
>
> **主要贡献:** 该研究首次提出了在标准假设下适应性安全的PVSS方案，并提供了两个具有不同特性的PVSS方案。
>
> **达到效果:** 第一个方案基于任何配对自由循环群和决策性Diffie-Hellman（DDH）假设，第二个方案基于不对称配对组并依赖于DDH和co-计算性Diffie-Hellman（co-CDH）假设，并具有特别有价值的可聚合特性。
>
> **技术梗概:** 研究采用了新颖的技术来构建适应性安全的PVSS方案，确保在标准假设下实现安全性。

---
### [2026/1101] Tail-Hammer: Optimized Statistics for Anonymous Committees and Applications

- **作者:** Bernardo David, Lucia Lavagnino, Elena Pagnin, Paul Stankovski Wagner

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1101) | [PDF](https://eprint.iacr.org/2026/1101.pdf)


> **研究背景:** 匿名委员会的选择技术在高效的适应性安全共识协议和YOLO模型中的多方计算中广泛应用，但现有的分析方法存在精度不足的问题。
>
> **主要贡献:** 作者提出了Tail-Hammer库，并提供了更准确的匿名委员会大小估计公式，改进了现有分析方法的精确度。
>
> **达到效果:** 与Blum等人的研究相比，Tail-Hammer能够在保持相同安全水平的情况下，识别出较小的委员会规模，从而提高效率。
>
> **技术梗概:** 通过使用紧密的二项式近似和开发高效高精度库Tail-Hammer来改进匿名委员会选择的技术方法。

---
### [2026/1104] The ABC of Symmetric Primitives over Integer Rings: Milk Before Meat

- **作者:** Tim Beyne, Lorenzo Grassi, Morten Øygarden, Berenika Richterová, Arne Sandrib

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1104) | [PDF](https://eprint.iacr.org/2026/1104.pdf)


> **研究背景:** 研究背景：在有限域$\mathbb{F}_{p^n}^t$上设计安全的对称密钥密码体制已有成熟理论，但当转换到整数环$\mathbb{Z}_{p^n}^t$时，攻击向量和算术特性差异显著，现有方法不再适用。
>
> **主要贡献:** 主要贡献：本文为在整数环上设计密码体制奠定了基础，并分析了统计和代数攻击的性质，提出了针对非多项式S盒的新属性。
>
> **达到效果:** 达到的效果：通过新方法，作者揭示了多项式与非多项式S盒的安全性差异，为未来的设计提供了指导原则。
>
> **技术梗概:** 技术梗概：本文深入分析了整数环上的算术特性，并提出了新的攻击模型和设计策略，以提高密码体制的安全性。

---
### [2026/1105] Dishonest Majority Multi-Party Arithmetic Garbling with Constant Rate

- **作者:** Tianyao Gu, Hanjun Li, Elaine Shi

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1105) | [PDF](https://eprint.iacr.org/2026/1105.pdf)


> **研究背景:** 在安全多方计算（MPC）中，降低通信复杂度是关键目标，尤其是对于高延迟网络的应用。现有的常数轮次协议虽然效率具体化，但通常针对布尔电路设计，并且每个门的带宽成本与安全性参数成线性关系。
>
> **主要贡献:** 本文提出了首个同时实现常数轮次和常量速率通信的安全多方计算协议，适用于静态恶意对手控制至多$n-1$个参与方。该协议基于Ball等人（Eurocrypt 2023）的算术遮蔽框架，并采用BMR模板。
>
> **达到效果:** 实验表明，该协议在矩阵向量乘法等基本操作上表现出色，显著减少了通信成本和计算延迟。
>
> **技术梗概:** 通过结合算术遮蔽技术和学习噪声线性同余假设，实现了高效的安全多方计算。

---

## 更新: 2026-05-28 07:35

*新增 6 篇论文 (编号 1048--1053)*

### [推荐] [2026/1048] Unified Dual Attack Analyses: Covariance-Based Score Distribution Prediction for LWE

- **匹配关键字:** post-quantum, LWE

- **作者:** Yechen Li, Qunxiong Zheng

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1048) | [PDF](https://eprint.iacr.org/2026/1048.pdf)


> **研究背景:** LWE问题支撑了包括NIST选定的CRYSTALS-KYBER和CRYSTALS-DILITHIUM在内的许多后量子密码系统，但现有的双攻击分析存在独立性假设错误的问题，导致方差估计过小。
>
> **主要贡献:** 作者提出了一种统一预测模型，用于估计三种类型的双攻击得分的期望和方差：原始双攻击、模切换双攻击以及解码双攻击（Crypto 2025）。
>
> **达到效果:** 该模型克服了现有方法中的理论缺口，提供了一个更准确的双攻击成功概率分析框架。
>
> **技术梗概:** 通过预测得分分布，作者利用余弦角度的不同来改进方差估计，并提出了一个统一的评估框架。

---
### [推荐] [2026/1051] Streamlined Symmetric Private Information Retrieval via Rényi Divergence

- **匹配关键字:** post-quantum, LWE

- **作者:** Alex Davidson, Nuno Nogueira, Samuel Pearson, João Ribeiro

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1051) | [PDF](https://eprint.iacr.org/2026/1051.pdf)


> **研究背景:** 现有Symmetric PIR方案需要并行运行多个加密原语，且难以自然地适应后量子环境。
>
> **主要贡献:** 本文通过利用噪声泛滥维持数据库隐私性，首次直接从PIR导出SPIR，并采用基于Rényi散度的分析方法优化参数。
>
> **达到效果:** 实现了具有多项式噪声维度和密文模数（具体为64位）的后量子、轮次最优SPIR方案。
>
> **技术梗概:** 通过改进后的参数分析，简化了单服务器SPIR，并确保数据库的安全性。

---
### [2026/1049] Decomposition of the Ate Pairing and its Relation to Generalized Pairing Inversion

- **作者:** Takakazu Satoh

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1049) | [PDF](https://eprint.iacr.org/2026/1049.pdf)


> **研究背景:** 研究了特定有限域上椭圆曲线的Ate对的数量分解，并探讨其与广义配对逆运算的关系。
>
> **主要贡献:** 提出了将广义配对逆运算归约为根寻找问题的方法，特别适用于超奇异曲线。
>
> **达到效果:** 对于满足特定条件的超奇异曲线，算法中的根寻找调用次数理论上为线性增长。
>
> **技术梗概:** 基于Miller函数构成因子系统的观察，设计了无需固定参数配对逆运算的算法。

---
### [2026/1050] Guess-and-Determine Rebound Revisited: Full Collision Attack on AES-256 in DM Hash Mode

- **作者:** Liyuan Tang, Lingyue Qin, Shiqi Hou, Xiaoyang Dong

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1050) | [PDF](https://eprint.iacr.org/2026/1050.pdf)


> **研究背景:** 该研究基于Qin等人在CRYPTO 2025提出的一种结合了猜测与确定方法的反弹攻击，旨在通过量子和经典模型将半自由开始或自由开始碰撞攻击转化为针对DM哈希模式的碰撞攻击。
>
> **主要贡献:** 论文贡献了一种新的全碰撞攻击方法，首次实现了对AES-256-DM的全量子碰撞攻击，并改进了之前针对AES-128-DM和AES-192-DM的最佳攻击效果。
>
> **达到效果:** 该研究显著提升了对AES-256-DM的安全性评估，填补了在三大主流哈希模式中尚未有全碰撞攻击实现的空白。
>
> **技术梗概:** 通过引入经典和量子模型，将半自由开始或自由开始碰撞攻击转化为针对DM哈希模式的碰撞攻击，并具体实现了对AES-256-DM的全量子碰撞攻击。

---
### [2026/1052] Full Key Recovery of Masked PRESENT on an Out-of-Order RISC-V Processor: A First Reported Case Study

- **作者:** Siddhartha Chowdhury, Nimish Mishra, Sarani Bhattacharya, Debdeep Mukhopadhyay

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1052) | [PDF](https://eprint.iacr.org/2026/1052.pdf)


> **研究背景:** 研究背景：针对现代出序（OoO）处理器，假设基于屏蔽的对策如阈值实现和探针隔离非干扰性（PINI）能够保护密码学软件免受侧信道泄漏的影响。然而，在这种假设下，由于微架构后端效应导致的秘密份额之间的隔离可能被打破。
>
> **主要贡献:** 主要贡献：提出了一种名为	exttt{OoOLyzer}的基于跟踪的分析框架，用于从RISC-V流水线跟踪中重建物理寄存器重用和后端执行交互。该工作揭示了由于OoO注册表重命名导致的直接表示秘密份额之间的关联，并展示了如何利用这些关联恢复PRESENT子密钥。
>
> **达到效果:** 达到的效果：通过实验验证，成功从屏蔽的PRESENT实现中恢复出第一轮的子密钥，证明了基于物理寄存器重用的侧信道泄漏是主要来源。
>
> **技术梗概:** 技术梗概：该研究使用了一种新的分析方法来识别和利用OoO处理器中的微架构效应，通过模拟和实验验证了这些效应对屏蔽密码算法安全性的实际影响。

---
### [2026/1053] Beyond 128 Bits: The Concrete Security of EKE

- **作者:** Jiawei Bao, Tibor Jager, Eike Kiltz, Aysan Nishaburi, Samin Nooripoor, Jiaxin Pan

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1053) | [PDF](https://eprint.iacr.org/2026/1053.pdf)


> **研究背景:** 研究探讨了在NIST P-256椭圆曲线上实现的密码学原语是否可以达到超过128位的安全性。
>
> **主要贡献:** 贡献在于提出了一个新的方法来证明破解加密系统所需的计算假设数量，并引入了隐藏目标Diffie-Hellman (HTDH) 假设。
>
> **达到效果:** 结果表明，EKE协议在理想密码模型中的安全性等价于HTDH假设，从而实现了宣称的128+log_2(N)/2位的安全性水平。
>
> **技术梗概:** 技术上，通过分析破解概率与所需解决Diffie-Hellman实例数量之间的关系，证明了HTDH假设的有效性。

---

## 更新: 2026-05-27 10:21

*新增 8 篇论文 (编号 1040--1047)*

### [推荐] [2026/1041] CoNAN: A Structure-Aware Framework for Lattice Cryptanalysis

- **匹配关键字:** lattice, LWE

- **作者:** Ali Raya, Vikas Kumar, Kushal Dey, Sugata Gangopadhyay

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1041) | [PDF](https://eprint.iacr.org/2026/1041.pdf)


> **研究背景:** 现有的格安全性评估通常基于最佳已知攻击的成本估计，这指导了实际参数的选择。然而，现有评估方法未能充分考虑由基础代数引入的额外结构带来的影响。
>
> **主要贡献:** 本文提出CoNAN框架，旨在通过整合代数结构来改进对格构造的安全性评估，并展示了其在NTRU类似构造和若干结构化LWE方案中的应用。
>
> **达到效果:** 该框架不仅重现了已知的代数攻击，还揭示了一些特定方案（如非交换群环上的LWE）的实际安全性比标准估计低至少60位。
>
> **技术梗概:** 通过引入CoNAN框架，作者开发了一种分析方法，利用代数同态将高维格表示为低维形式，从而实现更高效的攻击。

---
### [推荐] [2026/1045] Ciphertext-Updatable Attribute-Based and Predicate Encryption from Lattices

- **匹配关键字:** lattice, LWE

- **作者:** Robert Schädlich, Linda Scheu-Hachtel, Erkan Tairi, Yuejun Wang

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1045) | [PDF](https://eprint.iacr.org/2026/1045.pdf)


> **研究背景:** 本文提出了细粒度加密范式的新型变体——可更新密文的属性基加密（CU-ABE）和谓词加密（CU-PE），旨在通过允许对密文进行受控更新来增强其实用性。
>
> **主要贡献:** 作者定义了这些新的原语，并在区分安全性框架下建立了它们的安全性，同时提供了多种具有不同权衡的构造方法。
>
> **达到效果:** 研究结果包括基于LWE构建了一种通用转换，将普通ABE转化为单向和单一跳CU-ABE，并通过结合锁住混淆技术实现了从LWE构建单向和单一跳CU-PE。此外，还提出了支持有限更新令牌数量的多跳和无限制令牌设置下的密钥策略和密文策略CU-ABE方案。
>
> **技术梗概:** 为证明这些多跳构造的安全性，作者开发了新的技术，并依赖于...

---
### [2026/1040] Classical and Quantum Full Plaintext Recovery for Low-Round Feistel-Type Designs

- **作者:** Tingting Guo, Peng Wang, Jiwu Jing, Shuping Mao, Gang Liu

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1040) | [PDF](https://eprint.iacr.org/2026/1040.pdf)


> **研究背景:** 研究了低轮数Feistel结构的区分攻击与全明文恢复之间的关系，特别是在经典和量子环境下。
>
> **主要贡献:** 提出了针对2轮和3轮Feistel结构的经典和量子辅助恢复攻击方法。
>
> **达到效果:** 成功实现了对4/5/6轮Feistel-FK及多种实际加密方案的全明文恢复攻击。
>
> **技术梗概:** 利用经典选择明文攻击(CPA)、选定密文攻击(qCCA)以及基于Simon算法的前向/后向扩展技术。

---
### [2026/1042] Doubly Aggregatable Signatures

- **作者:** Georg Fuchsbauer, Pranav Garimidi, Joachim Neu, Guru-Vamsi Policharla, Max Resnick, Ertem Nusret Tas

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1042) | [PDF](https://eprint.iacr.org/2026/1042.pdf)


> **研究背景:** 多签名称的签名允许多个签署者联合生成单一（简短）的消息签名。本文引入了一种新的双重可聚合签名机制，该机制涉及两组签署者，旨在实现一层签署者创建针对同一消息的观察层零签名的简洁证明，并将许多一层签名公开展示为一个简洁证书的功能。
>
> **主要贡献:** 作者提出了双重可聚合签名这一新原理，并提供了两种在随机预言模型下的具体高效构造方案，这两种方案均能实现常量大小的聚合一层签名。
>
> **达到效果:** 通过引入双重可聚合签名机制，该研究显著提升了多签系统的效率和验证速度，同时确保了签名的安全性和不可抵赖性。
>
> **技术梗概:** 利用随机模子集求和问题（RMSS），两种方案均实现了纯代数验证方法，这使得可以使用承诺并证明的SNARK来检查位图上的简洁谓词。

---
### [2026/1043] Safe and Secure Autonomy by Machine Learning Techniques: A Systematic Literature Review

- **作者:** Afshin Hassani, Mehran Alidoost Nia, Reza Ebrahimi Atani

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1043) | [PDF](https://eprint.iacr.org/2026/1043.pdf)


> **研究背景:** 本文综述了2018年至2024年间利用机器学习技术确保自主系统安全性的最新进展，分析了129篇学术文章，揭示了主要方法、关键技术及应用领域。
>
> **主要贡献:** 研究指出了强化学习和深度学习在需要实时适应的场景中（如自动驾驶汽车、无人机和机器人）的应用优势，并识别出关键的研究趋势。
>
> **达到效果:** 研究表明，安全运动控制、预测、漏洞检测和安全性保障是当前研究的重点，但也指出标准化基准和模型在对抗条件下的鲁棒性不足的问题亟待解决。
>
> **技术梗概:** 该综述采用了系统文献回顾的方法，分析了多种机器学习技术，并强调了安全性和鲁棒性的提升需求。

---
### [2026/1044] Finding Random Collisions for Random Degree-2 Functions

- **作者:** Xinyu Mao

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1044) | [PDF](https://eprint.iacr.org/2026/1044.pdf)


> **研究背景:** 研究了随机二次函数在素域上的分布碰撞抵抗性，探讨了如何高效地找到统计上接近理想碰撞分布的输出。
>
> **主要贡献:** 提出了一个高效的算法，当$p^{N - M}$为超多项式时，其输出分布与理想碰撞分布统计上相近，解决了Bitansky等人提出的一个开放问题。
>
> **达到效果:** 证明了随机二次函数在参数区间内不是分布性碰撞抵抗的，从而解决了该领域的一个关键问题。
>
> **技术梗概:** 通过分析和设计高效的算法来逼近理想碰撞分布，并利用概率论方法验证其统计性质。

---
### [2026/1046] AWARE: A Non-Interactive Anonymous Whistleblowing System against Recipient Corruption

- **作者:** Ge Gao, Haining Yu, Jinbo Yang, Dongyang Zhan, Xiaohua Jia

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1046) | [PDF](https://eprint.iacr.org/2026/1046.pdf)


> **研究背景:** 现有匿名举报系统通过Tor网络和公钥加密保护提交者的身份信息，但仍依赖认证服务器进行身份验证，存在泄露风险。
>
> **主要贡献:** AWARE提出了一种非交互式匿名举报协议，分离了身份认证与提交过程，并采用委员会门限解密机制增强报告开放的公正性。
>
> **达到效果:** 在预设的篡改和泄漏假设下，证明了AWARE的安全属性，包括匿名性、令牌不可伪造性、举报内容保密性和开报告完整性。
>
> **技术梗概:** AWARE利用本地完成的令牌和门限解密技术，在不联系认证服务器的情况下实现提交，并通过委员会成员验证确保报告开放过程的公正性。

---
### [2026/1047] Round-Optimal Subversion-Resilient UC PAKE from Malleable Trapdoor Smooth Projective Hash Functions

- **作者:** Behzad Abdolmaleki, Suvradip Chakraborty, Shahram Khazaei, Lorenzo Magliocco, Nahid Roustaeifar, Behzad Vahdani, Daniele Venturi

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1047) | [PDF](https://eprint.iacr.org/2026/1047.pdf)


> **研究背景:** 该研究旨在构建一种在密码学可组合性框架下具备子撤销抗性的密码认证密钥交换协议(PAKE)，确保即使一方恶意且代码被不可察觉地篡改，安全仍能得到保障。
>
> **主要贡献:** 作者引入了一种新的可变通门道平滑投影哈希函数(M-TSPHF)，并基于此及标准加密原语设计了一个高效的子撤销抗性UC-PAKE协议。
>
> **达到效果:** 该协议实现了单轮完成，相比之前的方案在通信复杂度上有所改进，并达到了最优的轮次效率。
>
> **技术梗概:** 通过引入M-TSPHF和利用反向防火墙技术来实现子撤销抗性，从而保证了协议的安全性和有效性。

---

## 更新: 2026-05-26 07:52

*新增 6 篇论文 (编号 1034--1039)*

### [推荐] [2026/1037] On Publicly Verifiable Tokens in Group Signatures with Message-Dependent Opening

- **匹配关键字:** lattice

- **作者:** Takuma Watanabe, Keita Emura

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1037) | [PDF](https://eprint.iacr.org/2026/1037.pdf)


> **研究背景:** 研究背景：组签名（GSs）允许成员匿名证明其身份，同时让特定的权威机构（开者）在必要时能够识别该成员。然而，在带有消息依赖性开启功能的组签名（GS-MDO）中，开者的权力被进一步限制，引入了另一个授权机构（准入者），发放与消息相关的令牌。现有方案中的这些令牌可以被视为签名，并且可以通过基础签名方案的验证算法进行公开验证。但尚未明确定义令牌的公开可验证性，即是否能够公开验证一个令牌是否有权用于开启组签名。
>
> **主要贡献:** 主要贡献：本文正式定义了令牌的公开可验证性，并建立了验证令牌作为签名与验证其开启能力之间的适当关系，通常需要开者的私钥。此外，作者证明了Ohara等人基于配对的GS-MDO方案、Libert等人基于格的GS-MDO方案以及Libert等人基于配对的GS-MDO方案均符合定义，表明该形式化是合理的。
>
> **达到效果:** 达到的效果：通过正式定义令牌的公开可验证性，作者澄清了隐含的安全属性，并证明现有方案满足这一定义，从而为理解GS-MDO的实际可行性提供了理论基础。
>
> **技术梗概:** 技术梗概：本文采用形式化方法定义并分析了令牌的公开可验证性，通过对比签名验证和开启验证之间的关系来确保安全性。

---
### [2026/1034] Vistrutah on FPGA: High-Throughput Pipelined Architecture and Comparison with Wider AES Variant

- **作者:** Ahmet MALAL, Oğuz Yayla

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1034) | [PDF](https://eprint.iacr.org/2026/1034.pdf)


> **研究背景:** 针对NIST 2024年对AES扩展变体的征集，该研究首次在FPGA上评估了Vistrutah，这是一种基于AES轮函数的新提出的宽块密码。
>
> **主要贡献:** 论文贡献了一种高吞吐量流水线架构，并与已发布的WAES-256进行了比较。
>
> **达到效果:** Vistrutah在256位全配置下实现了211.57 Gbps的吞吐率，频率为826.44 MHz，相比WAES-256分别低了2.6%和2.7%，同时功耗降低了33.2%，资源使用减少了17.7%。
>
> **技术梗概:** 设计采用FPGA实现，并通过与WAES-256的对比评估其性能和效率。

---
### [2026/1035] SoK: Rijndael-256

- **作者:** Dessalegn Ayalneh, Anas Hlayhel, Setareh Sharifian, Alexander Tereschenko

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1035) | [PDF](https://eprint.iacr.org/2026/1035.pdf)


> **研究背景:** 大多数依赖于PRP原语的对称加密模式在块大小上受到生日界限的限制，这使得它们无法处理超过$2^{n/2}$个块的数据。对于当前128位宽的块来说，在云系统中处理大量数据时可能会遇到严重的问题。
>
> **主要贡献:** 本文综述了Rijndael-256的安全理论和实践，并探讨了利用向量化AES-NI优化性能的实现方法，以克服这一限制。
>
> **达到效果:** 通过使用具有更宽块大小（如Rijndael-256）的模式，可以加密超过$2^{128}$个块的数据，从而解决了传统模式在处理大量数据时遇到的问题。
>
> **技术梗概:** 本文采用了理论分析和实际实现相结合的方法，重点介绍了如何利用向量化技术提高Rijndael-256的性能。

---
### [2026/1036] Resettable Non-Interactive Zero-Knowledge: Attacks and Defenses

- **作者:** Behzad Abdolmaleki, Matteo Campanelli, Quang Dao, Shadman Mohammadi, Nahid Roustaeifar

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1036) | [PDF](https://eprint.iacr.org/2026/1036.pdf)


> **研究背景:** 随着零知识证明在实际系统中的广泛应用，它们面临着超越传统理论保证的新安全威胁，特别是重置攻击。
>
> **主要贡献:** 研究提出了强重置零知识（srZK）的新定义，并展示了广泛使用的非交互式零知识构造对重置攻击的脆弱性。
>
> **达到效果:** 研究表明，包括Fiat-Shamir编译版本的各种NIZK构造都存在漏洞，且提出了一种通用防御方法来增强其安全性。
>
> **技术梗概:** 通过修改NIZK中的随机性生成过程，提出了一个简单的编译器来实现强重置零知识属性。

---
### [2026/1038] Scaling Intelligence: Verifiable Decision Forest Inference with $\textit{Remainder}$

- **作者:** Makis Arsenis, Ryan Cao, Nick Cosby, Vishruti Ganesh, Ende Shen, Daniel Shorr, Benjamin Wilson

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1038) | [PDF](https://eprint.iacr.org/2026/1038.pdf)


> **研究背景:** 本文提出了一种基于ZKML的可验证决策森林推理电路实现，利用结构化的GKR协议提高了证明效率和可扩展性。
>
> **主要贡献:** 贡献在于通过数据并行化和多项优化策略实现了高效的大规模决策森林推理证明，并显著降低了每棵树每个样本的证明时间。
>
> **达到效果:** 结果是成功构建了包含128棵高度为9的树、针对128个输入（每个有64个特征）的GKR证明，总证明时间低于54秒，展示了该方法在增加森林中的树木数量和批量处理样本时仍能保持亚线性的时间增长。
>
> **技术梗概:** 技术上采用了多阶段声明聚合优化策略，并将其应用于插值策略中，同时将线性时间验证者技术推广到数据并行场景，从而实现了高效的证明生成过程。

---
### [2026/1039] Related-Differential Distinguishers on up to 7 Rounds of AES

- **作者:** Xueping Yan, Lin Tan, Wenfeng Qi

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1039) | [PDF](https://eprint.iacr.org/2026/1039.pdf)


> **研究背景:** 研究了圆减少版本的AES在密码方案设计中的应用，探讨其非随机属性和区分器是重要课题。尽管已知最长的秘密密钥区分器覆盖6轮AES，但在相关差异方向的研究仍有限。
>
> **主要贡献:** 作者通过交换和移位操作提供了对相关差异的新视角，并基于相关差异提出了5至7轮AES的新型非随机性质和秘密密钥区分器。
>
> **达到效果:** 在选择明文（CP）和自适应选择明文（ACP）设置中，改进了5轮AES的秘密密钥区分器的数据/时间复杂度分别为$2^{27.2}$/$2^{28.05}$和$2^{23.32}$/$2^{23.54}$。首次提出了7轮AES的秘密密钥区分器，其数据复杂度低于全码本。
>
> **技术梗概:** 通过结合一轮字节相关差异与四轮零差分性质，作者发现了5轮AES的新特性；利用一轮交换对角线相关差异和Bardeh及Rijmen给出的四轮相关差异，作者识别了7轮AES的第一个非随机性质。

---

## 更新: 2026-05-25 11:12

*新增 13 篇论文 (编号 1021--1033)*

### [推荐] [2026/1022] Thorns in Polynomial Convolution: Correlation, Large Deviations, and Applications

- **匹配关键字:** lattice

- **作者:** Dongshu Cai, Yijian Liu, Jiabo Wang, Xianhui Lu

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1022) | [PDF](https://eprint.iacr.org/2026/1022.pdf)


> **研究背景:** 研究背景在于，在基于结构化格的密码方案中，解密失败率（DFR）估计通常假设解密噪声系数是独立的，但在实践中，这些噪声包含由小多项式卷积产生的相关项，这会导致基于独立性的估计与实际失败率之间存在差距。
>
> **主要贡献:** 主要贡献在于首次系统地对具有高斯系数的卷积多项式的系数间相关性进行了刻画，并通过中心嵌入视角建立了大偏差结果。
>
> **达到效果:** 研究结果显示，随着范数增长，卷积多项式系数渐近集中在有限个二维平面附近，导致n维联合概率密度出现方向性的尾部结构，称为棘刺。
>
> **技术梗概:** 技术梗概包括使用中心嵌入视角来刻画相关性，并通过大偏差结果分析了这些棘刺的形成机制。

---
### [推荐] [2026/1029] Towards a Unified Memory-Less Framework for TCitH

- **匹配关键字:** post-quantum

- **作者:** Jesús-Javier Chi-Domínguez, Décio Luiz Gazzoni Filho, Marco Palumbi, Luis Rivera-Zamarripa

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1029) | [PDF](https://eprint.iacr.org/2026/1029.pdf)


> **研究背景:** 针对NIST后量子签名竞赛中的TCitH和VOLEitH两种MPCitH变体，现有研究发现VOLEitH虽然具有更短的签名和更多的堆栈内存，但不适合受限设备。
>
> **主要贡献:** 本文提出了一种统一的无状态框架，旨在使基于TCitH的方案在嵌入式系统中可行，并贡献了一个常数时间、位切片实现的Rijndael-256，用于目标架构的GGM树扩展、PRG和Commit功能。
>
> **达到效果:** 该框架实现了高达99%的堆栈使用率减少，同时具有最小的代码大小开销和可忽略不计的性能开销，并且设计为可扩展：只需实现底层问题的数学和多项式证明过程即可添加新方案。
>
> **技术梗概:** 通过简化统一的零知识证明框架来覆盖所有基于TCitH的NIST竞赛提交，以及提供一种针对嵌入式架构的Rijndael-256常数时间位切片实现。

---
### [推荐] [2026/1031] Compact Quaternion Algorithms for SQIsign

- **匹配关键字:** post-quantum

- **作者:** Won Kim, Changmin Lee, Hyunwoo Yoo

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1031) | [PDF](https://eprint.iacr.org/2026/1031.pdf)


> **研究背景:** SQIsign是一种基于_isogeny_的后量子签名方案，其公钥和签名极其紧凑。然而，由于该方案依赖于有理数域上的四元数代数算术，此前缺乏适用于固定精度整数算术的实现方法，这阻碍了在内存受限设备上的常时间实施与部署。
>
> **主要贡献:** 本文提出了更紧凑的四元数算法，显著减少了SQIsign中固定精度整数算术所需的内存需求。通过修改和分析SQIsign中的四元数算法，并推导出改进后的最坏情况大小界，实现了公钥生成和签名过程中小整数值的精确度预算大幅降低。
>
> **达到效果:** 经过优化后，NIST-I/III/V安全级别的精度预算分别从7026/10713/14150位减少到1774/2696/3555位，分别提高了74.75%、74.83%和74%，显著减少了内存占用并提升了在受限平台上的适用性。
>
> **技术梗概:** 通过分析SQIsign中的四元数算法，并推导出改进后的最坏情况大小界来优化固定精度整数算术，从而减少所需的内存需求。

---
### [推荐] [2026/1032] When Removing Reductions Goes Wrong: Auditing Reduction Placement in Production ML-DSA Implementations

- **匹配关键字:** post-quantum

- **作者:** Sunwoo Lee, Hyuk Lim, Seunghyun Yoon

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1032) | [PDF](https://eprint.iacr.org/2026/1032.pdf)


> **研究背景:** 在生产环境中正确实现后量子签名仍然具有挑战性，即使经过标准化。ML-DSA实施依赖于基于NTT的多项式算术和延迟蒙哥马利约简，但省略约简可能是有效的优化或潜在的算术缺陷。
>
> **主要贡献:** 本文提出了一种基于证书的审计方法来审查生产环境中ML-DSA实现中的约简放置。该方法从保守的pq-crystals拓扑开始，分析系数边界并分类约简站点为冗余或必要。
>
> **达到效果:** 应用该方法到八个ML-DSA库中，发现wolfSSL内存优化路径WOLFSSL-DILITHIUM-SMALL中存在的未报告缺陷：省略矩阵乘法后的约简导致溢出、非标准算术和签名失败，而这些错误通过现有KAT测试未被检测出来。
>
> **技术梗概:** 关键的技术成分为稀疏挑战产品的精确整数恢复结果，将后InvNTT边界从(-Q,Q)紧缩到[-τη, τη]，区分了安全省略的稀疏产品路径和承载负载的密集产品站点。

---
### [2026/1021] Schnorr-like Proofs of Knowledge for Hidden Oil Subspaces in UOV

- **作者:** Zhiwei Wang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1021) | [PDF](https://eprint.iacr.org/2026/1021.pdf)


> **研究背景:** 该研究针对UOV公钥密码体制中的隐藏油子空间，探讨了如何在不泄露信息的前提下证明对该子空间的知识。
>
> **主要贡献:** 作者构建了一个类似于Schnorr的Sigma协议，用于证明对隐藏油子空间的知识而不揭示其内容。
>
> **达到效果:** 通过该协议，证明者能够以计算上3-特殊完备性和计算上诚实验证者零知识的方式回应挑战，从而验证隐藏油子空间的存在性。
>
> **技术梗概:** 该技术涉及构造满足特定条件的矩阵，并在响应挑战时进行线性掩码处理。

---
### [2026/1023] Faster CoeffToSlot and SlotToCoeff for Sparsely Packed Ciphertexts with Application to CKKS Bootstrapping

- **作者:** Xiaopeng Zheng

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1023) | [PDF](https://eprint.iacr.org/2026/1023.pdf)


> **研究背景:** CKKS加密方案中的bootstrapping技术对于实现超越固定层次电路的同态计算至关重要，而CoeffToSlot和SlotToCoeff线性变换是其中的关键组成部分。
>
> **主要贡献:** 作者提出了一种利用稀疏打包设置中重复模式来优化这两个变换的方法，使得它们在保持乘法深度为1的同时减少了所需的同态操作数量。
>
> **达到效果:** 通过这种方法，在特定条件下，CoeffToSlot和SlotToCoeff的计算成本显著降低；同时证明了新布局产生的辅助槽同样满足所需的统计特性。
>
> **技术梗概:** 该研究利用重复模式简化了变换过程，并通过对变换过程中所需操作数的具体分析来优化算法效率。

---
### [2026/1024] Separating the Pebbling Model from the Random Oracle Model

- **作者:** Susanna F. de Rezende, David Engström, Leonid Reyzin

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1024) | [PDF](https://eprint.iacr.org/2026/1024.pdf)


> **研究背景:** 研究背景：在证明工作或空间的加密构造中，其安全性通常通过随机预言机模型来证明。该模型假设对手只能以黑盒方式访问预言机的功能，并且对于存储资源（如空间）的使用进行了进一步的理想化处理，即预言机输出仅能被完整存储或丢弃，而不能进行计算操作。然而，在某些情况下，这种理想化的限制可能并不充分，因为可以提取出对应于‘鹅卵石’的位串并对其进行计算。
>
> **主要贡献:** 主要贡献：本文通过构建一系列在鹅卵石模型下的空间证明和内存硬函数，展示了允许对手将预言机输出视为位串并进行计算操作的算法可以在效率上显著优于仅限于使用鹅卵石模型的算法，从而解决了关于鹅卵石模型与随机预言机模型之间关系的长期开放问题。
>
> **达到效果:** 达到的效果：证明了在特定情况下，鹅卵石模型不能准确地模拟对手的能力，并且存在一种更高效的算法可以在允许对手对预言机输出进行计算操作的情况下运行。
>
> **技术梗概:** 技术梗概：通过设计一系列基于空间和内存硬函数的构造，并展示了如何利用这些构造来区分鹅卵石模型与随机预言机模型之间的差异，从而解决了该问题。

---
### [2026/1025] Geometric Critical Point Screening: Clustering-Free Cryptanalytic Extraction of Neural Network Models

- **作者:** Ming Duan, Peiyao Tang

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1025) | [PDF](https://eprint.iacr.org/2026/1025.pdf)


> **研究背景:** 研究背景：神经网络模型提取已成为网络安全中的关键问题。现有方法通常采用计算优先、聚类后期的策略，导致查询和计算开销巨大。
>
> **主要贡献:** 主要贡献：提出了一种基于几何关系的关键点筛选方法，通过在共面平行线上搜索关键点，快速分离第一隐藏层神经元的关键点，减少了签名提取的查询复杂度。
>
> **达到效果:** 达到的效果：该方法仅需计算少量非目标关键点的签名，显著降低了查询复杂度，并提高了效率。
>
> **技术梗概:** 技术梗概：通过在共面平行线上搜索关键点，快速分离第一隐藏层神经元的关键点；对于输入维度超过第一隐藏层维度的情况，在全激活空间内使用共面线段进一步高效筛选第二隐藏层关键点。

---
### [2026/1026] Sparse Hermite Interpolation Method for Discrete-CKKS Functional Bootstrapping

- **作者:** Andreea Alexandru, Andrey Kim, Yuriy Polyakov, Hongren Zheng

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1026) | [PDF](https://eprint.iacr.org/2026/1026.pdf)


> **研究背景:** Discrete CKKS通过结合CKKS同态加密方案实现精确计算，其核心操作之一是功能自举，该过程允许在密文上执行任意函数并减少噪声。
>
> **主要贡献:** 作者提出了“稀疏”三角Hermite插值方法，这是一种CKKS友好的高阶Hermite插值技术，能够有效克服现有方法的局限性，并实现更好的噪声降低效果。
>
> **达到效果:** 该方法不仅保持了与先前最快方法相当的效率，还在噪声减少方面表现出色，从而提高了密文计算的准确性和效率。
>
> **技术梗概:** 通过利用约束和系数的稀疏特性，作者开发了一种新的Hermite插值技术，能够在保持高效的同时实现显著的噪声降低。

---
### [2026/1027] Computing Asymptotic Bounds for the Automated Coppersmith Method via Linear Programming

- **作者:** Zhaopeng Ding, Zhaopeng Dai, Baofeng Wu, Yanshuo Zhang, Kejun Zhang

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1027) | [PDF](https://eprint.iacr.org/2026/1027.pdf)


> **研究背景:** Coppersmith's方法是用于求解模多项式方程的小根的基础技术，确定可恢复根的渐近界是其分析中的核心和挑战部分。
>
> **主要贡献:** 作者将Automated Coppersmith方法中渐近界的计算转化为线性规划问题，从而获得一个证明正确且明确可计算的公式。
>
> **达到效果:** 通过该方法，作者为五个密码分析场景提供了改进的渐近界：交换式Isogeny隐藏数字问题、模逆隐藏数字问题、椭圆曲线隐藏数字问题、未知乘数的一次线性同余生成器和具有提示的等级化Isogeny问题。
>
> **技术梗概:** 该研究将Automated Coppersmith方法中的渐近界计算转化为线性规划问题，利用了线性编程技术来求解复杂的数学问题。

---
### [2026/1028] Collusion-Resistant Asymmetric Anamorphic Encryption: Framework, Generic Construction, and Concrete Instantiations

- **作者:** Zhikang Xie, Rupeng Yang, Man Ho Au, Zuoxia Yu, Willy Susilo

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1028) | [PDF](https://eprint.iacr.org/2026/1028.pdf)


> **研究背景:** 研究背景：论文针对Anamorphic加密技术，特别是其在非对称形式下的应用进行了深入探讨。该技术允许通过看似无害的密文进行隐蔽通信，即使在强审查环境下仍能保持秘密性。
>
> **主要贡献:** 主要贡献是提出了首个通用框架以实现抗合谋攻击的非对称Anamorphic加密方案，并引入了新的密码学抽象——用于PKE的证人伪随机函数（witness PRF），以精确捕捉嵌入安全隐蔽信道所需的结构。
>
> **达到效果:** 达到的效果是在不依赖于混淆技术的前提下，提供了一种统一且概念清晰的方法来构建非对称Anamorphic加密方案，并能适用于任何具有高最小熵密文的PKE方案。
>
> **技术梗概:** 技术梗概：通过引入新的密码学抽象和基于此开发通用框架，论文解决了在合谋攻击下实现非对称Anamorphic加密的技术难题。

---
### [2026/1030] Pushforward Problems and Applications to Isogeny-based Cryptography

- **作者:** Luciano Maino, Christophe Petit

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1030) | [PDF](https://eprint.iacr.org/2026/1030.pdf)


> **研究背景:** 研究探讨了在超奇异椭圆曲线上的isogeny问题，特别是在无法高效表示N-扭子的情况下，如何通过推前算子oracle进行isogeny恢复。
>
> **主要贡献:** 提出了一个新的框架来编码torsion信息，并展示了访问推前算子oracle可以实现高效的isogeny恢复实例。
>
> **达到效果:** 该研究揭示了对Kim, Kim和Lee的阈值签名方案、Basso的盲伪随机函数以及Leroux和Roméas的可更新加密方案的安全性影响。
>
> **技术梗概:** 通过引入推前算子oracle来处理不可高效表示的N-扭子问题，并证明了在某些实例下可以利用该oracle进行isogeny恢复。

---
### [2026/1033] A New Construction Method for More Efficient Quadratic One-Time Noisy Multi-Client Functional Encryption Schemes

- **作者:** Jasmin Zalonis, Linda Scheu-Hachtel, Frederik Armknecht

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1033) | [PDF](https://eprint.iacr.org/2026/1033.pdf)


> **研究背景:** 该研究旨在构建一种支持噪声二次函数的一次性多客户端功能加密方案，具备抗篡改性和标签功能，适用于隐私保护的机器学习等实际应用。
>
> **主要贡献:** 作者提出了一种不同于先前构造的新结构设计方法，使用更简单的组件实现更高的效率，并且安全性仅依赖于其基础构建块而无需额外的困难假设。
>
> **达到效果:** 通过具体实例QUILT证明了该方案在性能上的显著优势，在私有逻辑回归训练中实现了4.8到6.8倍的速度提升。此外，与现有方案相比，该构造允许使用标签，从而减轻了一次性的限制。
>
> **技术梗概:** 研究采用了一种不同于以往的结构设计方法，利用更简单的构建块实现高效性，并且不依赖于双线性群结构。

---

## 更新: 2026-05-23 09:59

*新增 2 篇论文 (编号 1019--1020)*

### [2026/1019] On the Security of Public Key Authenticated Encryption with Keyword Search with Sender-independent Search Complexity

- **作者:** Takeshi Yoshida, Keita Emura

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1019) | [PDF](https://eprint.iacr.org/2026/1019.pdf)


> **研究背景:** 研究背景：Li等人提出了一个无需代理的公钥认证加密方案，支持密文更新和关键词搜索（PAUKS），旨在提供高效的数据保护与检索机制。
>
> **主要贡献:** 主要贡献：作者揭示了该方案在密文更新过程中存在安全漏洞，即关键词信息可能泄露，并验证了攻击的有效性。
>
> **达到效果:** 达到的效果：证明了PAUKS方案的安全性不足，在实际应用中可能导致敏感信息的暴露风险。
>
> **技术梗概:** 技术梗概：通过分析密文更新过程中的加密机制，作者设计了一种新的攻击方法来检测并利用关键词信息泄露的问题。

---
### [2026/1020] On the Formal Verification of Authenticated Encryption of the MQTT Protocol

- **作者:** Varsha Jarali, Shashi Kant Pandey

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1020) | [PDF](https://eprint.iacr.org/2026/1020.pdf)


> **研究背景:** MQTT协议因其轻量级架构在物联网环境中广泛应用，但通过中央代理传输敏感医疗数据存在严重的隐私风险。
>
> **主要贡献:** 提出了一种高性能的端到端加密（E2EE）安全MQTT协议，该协议利用嵌套AES-GCM加密架构和HMQV密钥交换协议，确保消息内容对中间人攻击者不可见。
>
> **达到效果:** 通过ProVerif验证器在Dolev-Yao威胁模型下证明了该模型的安全性，提供了一种计算开销低且高度安全的解决方案。
>
> **技术梗概:** 设计采用了嵌套AES-GCM加密和MQTT v5.0增强认证密钥交换机制，结合Schnorr数字签名版本的HMQV协议进行一次性的Broker Nonce挑战响应验证。

---

## 更新: 2026-05-21 20:24

*新增 35 篇论文 (编号 980--1018)*

### [推荐] [2026/982] Zero-shot deep-unfolding decoder for QC-MDPC McEliece cryptosystems

- **匹配关键字:** post-quantum

- **作者:** Shingo Kukita, Rei Iseki, Takeshi Namatame, Kohtaro Watanabe

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/982) | [PDF](https://eprint.iacr.org/2026/982.pdf)


> **研究背景:** QC-MDPC McEliece密码系统因其抗量子特性而备受关注，但其解码性能直接影响系统的安全性。
>
> **主要贡献:** 提出了一种零样本转移的深度展开译码器，通过权重同质化约束可训练权重，使其与特定 Tanner 图独立，从而实现小码本训练后直接应用于大码本。
>
> **达到效果:** 实验表明，在80比特和128比特安全参数下，所提方法比标准 BP 方法具有更低的解码错误率。
>
> **技术梗概:** 采用深度展开框架将迭代算法转化为具有可训练权重的神经网络，并通过权重同质化技术实现跨码本的零样本转移学习。

---
### [推荐] [2026/984] Quantum algorithm for Discrete Gaussian Sampling

- **匹配关键字:** lattice

- **作者:** Clémence Chevignard, André Schrottenloher, Yixin Shen

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/984) | [PDF](https://eprint.iacr.org/2026/984.pdf)


> **研究背景:** 离散高斯采样在基于格的密码学中是一个基本问题，出现在数字签名等基础加密原语以及解决困难的格问题的重要分析构建块中。
>
> **主要贡献:** 提出了一种基于量子拒绝采样的算法，其复杂度比经典对应物快约平方量级，并且可以输出一个量子态，既可以测量以获得所需的分布，也可以直接用于其他量子算法。
>
> **达到效果:** 通过这种方法，我们推导出两种版本的量子对偶攻击，改进了之前的版本并提高了效率，每种版本各有优势（速度 vs 内存需求）。其中第二个版本特别有趣，因为它只需要多项式经典和量子内存，不包括离散高斯采样器预处理步骤中的经典内存。
>
> **技术梗概:** 该算法基于量子拒绝采样的技术，并且能够加速解决短整数解决方案问题的算法，在任何范数下都有效。

---
### [推荐] [2026/987] Impact of Post-Quantum Signatures on InnoDB B+-Trees and Efficient Batch Signing

- **匹配关键字:** post-quantum

- **作者:** Seung-Won Lee, Min-Seo Kim, Ui-Jae Kim, Hui-Ju Kang, Hwa-Jeong Seo

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/987) | [PDF](https://eprint.iacr.org/2026/987.pdf)


> **研究背景:** 后量子密码学（PQC）数字签名的过渡对关系数据库的存储结构构成了意外威胁，特别是对于InnoDB B+树这种关键数据结构。
>
> **主要贡献:** 研究提出了结合分表方案与基于Merkle树的批量签名方法的新架构，以解决签名大小增加导致的问题。
>
> **达到效果:** 新架构恢复了B+树的扇出至41，减少了97%的叶子页面，并将插入吞吐量提高了28.1倍，同时降低了文档签名存储成本高达97.6%。
>
> **技术梗概:** 研究通过分析传统单表存储方式在PQC迁移环境中的局限性，并提出了一种实用的缓解架构来应对这些挑战。

---
### [推荐] [2026/988] Maskaglia: A New, Efficient Approach to Masked Discrete Gaussian Sampling

- **匹配关键字:** lattice

- **作者:** Calvin Abou Haidar, Thomas Espitau, Clément Hoffmann, Mehdi Tibouchi

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/988) | [PDF](https://eprint.iacr.org/2026/988.pdf)


> **研究背景:** 离散高斯抽样是许多基于格的密码系统的核心操作，但实现时面临显著的安全挑战，尤其是对抗侧信道攻击。现有研究主要集中在常时间侧信道攻击上，而针对更强的如相关功率分析等攻击的掩码保护措施较少且性能不佳。
>
> **主要贡献:** 作者提出了一种新的、高效的离散高斯抽样方法Maskaglia，并基于连续正态分布提出了一个新的拒绝采样器，以实现对强侧信道攻击的有效防护。
>
> **达到效果:** 该方法显著提高了在保护对抗相关功率分析等强侧信道攻击下的性能，同时保持了较高的效率。
>
> **技术梗概:** 作者通过离散化与Marsaglia算法相关的连续正态分布抽样器，并采用拒绝采样的策略来实现掩码保护，避免了传统基于累积分布表的方法带来的高昂成本。

---
### [推荐] [2026/990] Single-Trace Power Analysis of LESS Key Generation

- **匹配关键字:** post-quantum

- **作者:** Süleyman Emir Akın, Abdullah Talayhan, Özcan Öztürk

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/990) | [PDF](https://eprint.iacr.org/2026/990.pdf)


> **研究背景:** LESS是一种基于线性等价问题的签名方案，作为NIST后量子密码标准化过程中的候选者之一，其安全性依赖于秘密密钥生成的多项式矩阵。
>
> **主要贡献:** 作者提出了一种针对LESS v2.0的单迹横向侧信道攻击方法，能够完全恢复秘密多项式矩阵，从而伪造签名。
>
> **达到效果:** 实验结果表明，在NIST类别1参数集上，该攻击从单一电源轨迹中以96%的成功率精确恢复了秘密多项式矩阵。
>
> **技术梗概:** 通过分析矩阵乘法函数的功耗特性来提取密钥中的系数信息，并利用行简化阶梯形变换函数进一步获取置换列表，最后结合公钥进行代数关系推断以完整恢复系数列表。

---
### [推荐] [2026/995] On Local Invariants for Permutation Equivalence

- **匹配关键字:** lattice

- **作者:** Benjamin Benčina

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/995) | [PDF](https://eprint.iacr.org/2026/995.pdf)


> **研究背景:** 研究背景：本文探讨了置换等价问题（(Signed) Permutation Code Equivalence，(S)PCE）中的局部不变量，旨在提供一种新的可计算不变量以挑战现有假设，并扩展相关领域的知识。
>
> **主要贡献:** 主要贡献在于提出了一个称为平方类不变量的新不变量，该不变量未被编码理论所识别。此外，证明了构造A格的体维数和本文提出的平方类不变量完全决定了其体结构，且在高维度下不会进一步分裂，从而揭示了所有已知的有效计算不变量。
>
> **达到效果:** 达到的效果是提供了一种区分(S)PCE问题决策版本的新方法，并通过比较构造A格的体结构来重新表述这一区别。此外，还描述了随机$q$-元格的体分布情况。
>
> **技术梗概:** 技术梗概：本文采用代数编码理论和格论中的技术，特别是利用平方类不变量和构造A格的相关性质，提出了新的算法和技术以解决(S)PCE问题并扩展相关研究。

---
### [推荐] [2026/997] Miraidon: MinRank Identification

- **匹配关键字:** lattice, post-quantum

- **作者:** Ryann Cartor, Freeman Slaughter

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/997) | [PDF](https://eprint.iacr.org/2026/997.pdf)


> **研究背景:** 研究旨在提出一种基于MinRank问题的新颖后量子签名方案，以应对量子计算对现有公钥基础设施的潜在威胁。
>
> **主要贡献:** 贡献在于设计了Miraidon-S、Miraidon-RS和Miraidon-LRS三种签名方案，并通过零知识证明系统提高了安全性与效率。
>
> **达到效果:** 结果表明，基于MinRank问题的签名方案在公共密钥大小、签名大小及安全参数方面具有竞争力，并且首次实现了基于该问题的可链接环签名。
>
> **技术梗概:** 技术上采用了新颖的零知识证明方法来构建签名方案，确保了方案的安全性和效率。

---
### [推荐] [2026/998] Balanced and Adaptively Secure Asynchronous Common Coin and Byzantine Agreement With Sub-Quadratic Communication

- **匹配关键字:** homomorphic encryption

- **作者:** Hanwen Feng, Tiancheng Mai, Qiang Tang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/998) | [PDF](https://eprint.iacr.org/2026/998.pdf)


> **研究背景:** 分布式共同随机性生成（即公共硬币问题）是随机化分布式计算的基础。尽管已有大量研究寻求可扩展的解决方案，异步设置仍然是一个挑战。
>
> **主要贡献:** 本文通过提出首个具有亚二次通信复杂性的平衡异步公共硬币协议，解决了这一问题。该协议支持最多半数减ε节点的适应性敌手。
>
> **达到效果:** 与前人工作相比，我们的方案避免了使用全同态加密等复杂的密码学工具，并且只需两轮确定性通信即可终止。
>
> **技术梗概:** 核心在于构造显式和高效的采样器。这些采样器将具有半数以上诚实多数的群体划分为O(√n)个社区，确保大多数社区保持...

---
### [推荐] [2026/1004] PQKryvos: Post-Quantum Secure E-Voting With Flexible Ballot Formats and Public Tally-Hiding

- **匹配关键字:** lattice, post-quantum

- **作者:** Nicolas Huber, Pascal Reisert, Ralf Kuesters

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1004) | [PDF](https://eprint.iacr.org/2026/1004.pdf)


> **研究背景:** 传统的电子投票协议依赖于如离散对数问题等传统假设来提供安全性保证，但在量子计算时代面临不安全的风险。
>
> **主要贡献:** PQKryvos提出了一种高效且灵活的后量子安全同态电子投票协议，能够支持多种选举方法和选票格式，并首次实现了公共计票隐藏这一更强的隐私性。
>
> **达到效果:** 该协议不仅保证了选民隐私和结果可验证性，还确保仅公开预期的选举结果，不泄露额外信息，进一步提升了选民和候选人隐私。
>
> **技术梗概:** PQKryvos通过结合同态格承诺和基于哈希的一般证明技术来实现选票正确性，并利用Huber等人提出的Kryvos框架进行后量子安全实例化。

---
### [推荐] [2026/1006] Current trends in AI-Aided Cryptography

- **匹配关键字:** post-quantum

- **作者:** Tobias Höbbel, Sebastian Kavalir, Gero Knoblauch, Alexander Wiesmaier

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1006) | [PDF](https://eprint.iacr.org/2026/1006.pdf)


> **研究背景:** 该研究聚焦于人工智能(AI)与密码学交叉领域的最新趋势，旨在填补现有综述文章在特定技术或仅提供高层次概述方面的空白。
>
> **主要贡献:** 作者通过回顾2021-2025年间90篇相关文献，并结合期刊、会议及公开招标的征稿信息，进行跨领域比较分析，揭示了研究领域的不均衡分布。
>
> **达到效果:** 研究表明，密码分析和哈希算法的研究较为集中，而协议设计、加密技术和后量子密码学则较少涉及。
>
> **技术梗概:** 研究采用文献回顾与需求征集相结合的方法，全面评估AI在密码学各子领域中的应用现状与发展潜力。

---
### [推荐] [2026/1007] Quantum Circuit Implementation and Grover’s Search on the Lightweight Block Cipher KLEIN Family

- **匹配关键字:** post-quantum

- **作者:** Indranil Mukherjee, Ranit Dutta, Bhupendra Singh, Lexy Alexandar, Bimal Mandal

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1007) | [PDF](https://eprint.iacr.org/2026/1007.pdf)


> **研究背景:** 随着量子计算的发展，许多经典加密算法可能因量子攻击如Grover搜索而变得脆弱。因此，研究如何在量子计算机上实现轻量级块密码KLEIN及其组件显得尤为重要。
>
> **主要贡献:** 本文贡献了KLEIN家族所有变体的高效量子电路实现，并详细描述了包括密钥添加、替换、RotateNibbles、MixNibbles和密钥调度在内的各个功能模块。
>
> **达到效果:** 通过资源估算，展示了在提出的量子电路中执行Grover搜索算法的可能性，证明了其在后量子加密环境下的实用性和鲁棒性。
>
> **技术梗概:** 该设计采用了CCNOT、CNOT和Pauli-X等门来实现各组件，并提供了全面的资源估计以评估其实现的有效性。

---
### [推荐] [2026/1008] Unified FPGA Design of Kyber and Dilithium with Provable Fault Tolerance

- **匹配关键字:** lattice, post-quantum

- **作者:** Siddhartha Chowdhury, Nimish Mishra, Sarani Bhattacharya, Debdeep Mukhopadhyay

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1008) | [PDF](https://eprint.iacr.org/2026/1008.pdf)


> **研究背景:** 针对后量子密码方案的高效且安全的硬件实现对于实际应用至关重要。
>
> **主要贡献:** 提出了一种统一的FPGA架构，支持Kyber和Dilithium两种方案，并具备可验证的容错机制。
>
> **达到效果:** 该设计不仅实现了两个方案的无缝集成，还提供了首个统一的容错架构，确保在无故障环境下低重试次数和最小性能下降。
>
> **技术梗概:** 采用微编码可编程数据路径支持两种方案，同时嵌入基于拒绝采样的概率验证机制以增强抗传播故障攻击能力。

---
### [推荐] [2026/1014] Updatable Public-Key Encryption from FESTA

- **匹配关键字:** post-quantum

- **作者:** Andrea Basso, Tako Boris Fouotsa, Fatna Kouider, Péter Kutas, Luciano Maino, Laurane Marco

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1014) | [PDF](https://eprint.iacr.org/2026/1014.pdf)


> **研究背景:** UPKE旨在为安全消息传递提供前向保密性，通过结合标准公钥加密和可更新机制来实现。
>
> **主要贡献:** 该研究提出了基于FESTA的isogeny UPKE方案，并解决了传统假设下高效且后量子安全的无限制更新问题。
>
> **达到效果:** 所提出的UPKE方案既实用又高效，能够支持无限次更新，并提供了基于isogeny难题的形式化安全性证明。
>
> **技术梗概:** 该技术利用了FESTA公钥加密方案的四维版本来实现高效的可更新机制。

---
### [推荐] [2026/1018] Symmetric Attribute-Based Encryption from Minimal Hardness Assumptions

- **匹配关键字:** post-quantum

- **作者:** Riccardo Longo, Enrico Sorbera

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1018) | [PDF](https://eprint.iacr.org/2026/1018.pdf)


> **研究背景:** 该研究提出了一个新颖的同态属性加密方案，将其应用于具有对称性的密文策略属性加密框架中，使得加密者也需要具备足够的属性才能生成符合给定策略的密文。
>
> **主要贡献:** 贡献在于从碰撞 resistant 哈希函数和伪随机函数的最小假设出发，利用线性秘密共享和多项式插值的特性构建方案，并定义了一种新的访问树形式，增强了关联的秘密共享原语的算术可能性。
>
> **达到效果:** 该方案不仅实现了对量子计算的安全性，还通过改进的访问树结构提高了加密效率和可预测性。
>
> **技术梗概:** 技术上采用了线性秘密共享和多项式插值的方法，并结合碰撞 resistant 哈希函数和伪随机函数来构建安全的同态属性加密方案。

---
### [2026/980] Key-Independent Secret-Key Distinguisher for 7-Round AES based on the Joint Generalized Zero-Difference Property

- **作者:** Hanbeom Shin, Sunyeop Kim, Byoungjin Seok, Deukjo Hong, Jaechul Sung, Seokhie Hong, Sangjin Lee, Dongjae Lee

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/980) | [PDF](https://eprint.iacr.org/2026/980.pdf)


> **研究背景:** 研究旨在填补7轮AES中缺乏独立于密钥的秘密密钥区分器的空白，通过分析其结构特性来理解AES的内在属性。
>
> **主要贡献:** 提出了首个基于联合广义零差分性质的7轮AES独立于密钥的秘密密钥区分器。
>
> **达到效果:** 该区分器成功概率约为77.8%，数据、时间和内存复杂度分别为$2^{126.2}$，验证了理论预测与实验结果的一致性。
>
> **技术梗概:** 利用联合广义零差分性质构造了一个新的7轮差分特性，并基于此设计了一种区分攻击。

---
### [2026/981] Profiling-Device-Free SASCA Framework for ML-KEM

- **作者:** Yuxuan Wang

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/981) | [PDF](https://eprint.iacr.org/2026/981.pdf)


> **研究背景:** 针对NIST标准的PQC算法ML-KEM的侧信道分析，传统的SASCA攻击需要与目标设备完全匹配的 profiling 设备，但在实际应用中难以获得。
>
> **主要贡献:** 本文提出了一种无需 profiling 设备的 ML-KEM SASCA 框架，通过控制 NTT 输入并训练泄漏模型，实现了对 INTT 的适应性微调和密钥恢复。
>
> **达到效果:** 实验验证表明，该框架在实际嵌入式设备上能够有效恢复密钥，并且所需的采样迹数与传统 profiling SASCA 相当。
>
> **技术梗概:** 通过选择特定的密文控制 NTT 输入以训练泄漏模型，并利用 NTT 和 INTT 之间的相似性进行对抗性的无监督域适应，从而实现目标设备的密钥恢复。

---
### [2026/983] A formal analysis of FLEX and FLEX2

- **作者:** Ramses Fernandez

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/983) | [PDF](https://eprint.iacr.org/2026/983.pdf)


> **研究背景:** 本文对FLEX协议及其增强版本FLEX2的加密核心进行了形式化分析，旨在验证其在区块链环境下的安全性和实用性。
>
> **主要贡献:** 主要贡献在于证明了链上可强制执行性、CDS秘密性、健全性、泄漏受限隐私以及通用组合实现，均基于标准假设。
>
> **达到效果:** 通过形式化分析，确保了FLEX和FLEX2协议在实际应用中的安全性和可靠性，并为后续研究提供了理论基础。
>
> **技术梗概:** 采用交易有向无环图（DAG）和状态机的形式化方法来定义理想功能，并证明其安全性特性。

---
### [2026/985] A New Insight into Constructing Cryptographic Boolean Functions via Walsh Spectral Analysis

- **作者:** Shaozheng He, Jiongjiong Ren, Shaozhen Chen, Jiaxin Yan, Jianhua Hou

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/985) | [PDF](https://eprint.iacr.org/2026/985.pdf)


> **研究背景:** 研究背景：Walsh谱直接决定了布尔函数的关键密码学属性，因此构建具有所需频谱特性的布尔函数一直是长期的研究重点。
>
> **主要贡献:** 主要贡献：提出了一个统一框架来解决一类特定的布尔函数构造问题，并设计了迭代Walsh恢复（IWR）算法及其优化版本（FG-IWR和OIWR）。
>
> **达到效果:** 达到的效果：通过理论分析和实验验证，该方法同时实现了理论保证、设计灵活性和计算效率。
>
> **技术梗概:** 技术梗概：采用迭代Walsh恢复算法，并结合遗忘和贪婪策略进行启发式优化，最终提出优化的迭代Walsh恢复（OIWR）算法。

---
### [2026/986] VeinoCert: Binding an Object to an Owner

- **作者:** Serge Vaudenay

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/986) | [PDF](https://eprint.iacr.org/2026/986.pdf)


> **研究背景:** 该研究旨在通过结合RFID技术和生物识别技术，提供一种安全且私密的方法来验证物品的所有权。
>
> **主要贡献:** 作者提出了VeinoCert协议，能够有效确认持有特定物品的人是否是该物品的合法所有者。
>
> **达到效果:** 实验结果显示，该系统能够在不存储生物特征数据的情况下，实现高效准确的身份认证，并确保访问权限仅限于真正的物品所有者。
>
> **技术梗概:** 该技术方案采用了一种低成本的RFID芯片，并结合了指纹静脉识别技术进行身份验证。

---
### [2026/989] BumbleBee: Best-of-Both-Worlds MVBA with Optimal Communication, Latency and Resilience Tradeoffs

- **作者:** Fatima Elsheimy, Simon Holmgaard Kamp

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/989) | [PDF](https://eprint.iacr.org/2026/989.pdf)


> **研究背景:** 在同步和异步网络中，共识协议对拜占庭容错的要求不同，这导致了响应性和安全性之间的权衡问题。
>
> **主要贡献:** 本文提出了一种名为BumbleBee的协议，实现了最优的通信复杂度，并同时满足异步安全、同步安全和响应性。
>
> **达到效果:** 该协议在给定的拜占庭容错阈值下，首次实现了MVBA的同时安全性与高效性。
>
> **技术梗概:** 通过设计一种新颖的消息验证机制，BumbleBee能够在不增加通信复杂度的情况下，确保协议的安全性和响应性。

---
### [2026/991] DDYF: Differential Dolev-Yao Fuzzing of Cryptographic Protocols

- **作者:** Tom Gouville, Lucca Hirschi, Steve Kremer

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/991) | [PDF](https://eprint.iacr.org/2026/991.pdf)


> **研究背景:** DDYF旨在解决传统Dolev-Yao (DY) fuzzing在检测逻辑漏洞时对精确运行时属性建模的需求，这种需求导致了劳动密集且非详尽的特性定义过程，通常需要复杂的PUTs仪器化。
>
> **主要贡献:** DDYF通过引入差分Oracle来比较不同协议实现间的执行差异，并利用DY模型解释这些差异，从而识别出可能表示漏洞或错误的语义差异，减少了误报率。
>
> **达到效果:** 实验结果表明，DDYF能够检测到传统DY fuzzing未能发现的漏洞，显著提高了漏洞检测的有效性和全面性。
>
> **技术梗概:** DDYF采用了一种通用设计，并在puffin DY fuzzer中实现，通过比较不同协议实现间的执行差异来识别潜在的逻辑错误或漏洞。

---
### [2026/992] Suppressing Hidden Extension-Field Linearity in Rank-Metric Cryptography via Structural Incompatibility

- **作者:** Dengchuan Liao, Xiangxue Li, Yu Yu

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/992) | [PDF](https://eprint.iacr.org/2026/992.pdf)


> **研究背景:** 研究背景：基于秩距离的编码密码学长期以来依赖于结构化的代数码族，如加比鲁林码，以利用其最优的秩距离性质和高效的解码算法。然而，这种结构化导致了可被利用的代数不变量，特别是扩展域线性和Frobenius不变性，这些特性使得攻击者能够开发出有效的多项式时间区分器和密钥恢复攻击。
>
> **主要贡献:** 主要贡献：本文通过识别一种简单的结构性不兼容性来解决这一问题，这种不兼容性排除了直接的扩展域线性表示，从而避免了相关攻击。作者引入了一种新的编码族——增强加比鲁林矩阵子码（EnGMS），并证明了其在标准安全级别下的性能优势。
>
> **达到效果:** 达到的效果：基于EnGMS的构造方案实现了IND-CCA2安全性，并且具有确定性解码和零解密失败率的特点。此外，该方案在保持紧凑的密文大小的同时还拥有适度的公钥尺寸，证明了结构性保证的有效性。
>
> **技术梗概:** 技术梗概：通过引入EnGMS编码族，作者利用维度不匹配来排除隐藏的Fq^m线性扩展结构，从而避免了相关攻击，并且使用通用变换实现了安全的公钥加密和密钥封装机制。

---
### [2026/993] Format-Preserving Encryption Creates a Privacy Attack Surface for Re-Identification

- **作者:** Martin Staal Boesgaard, Markus Larsen

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/993) | [PDF](https://eprint.iacr.org/2026/993.pdf)


> **研究背景:** 格式保持去识别方法，如格式保持加密，在保留原始数据的语法属性的同时实现了数据的匿名化。然而，当应用于具有多种格式的数据类型时，这种格式保持会引入信息论上的泄漏，使得格式本身可以揭示关于原始数据的重要信息，从而在适当辅助信息存在的情况下构成攻击面。
>
> **主要贡献:** 作者通过形式化定义了格式保持，并利用香农熵量化了由此产生的泄漏。他们还通过对实际数据集的分析验证了理论结果。
>
> **达到效果:** 研究发现长度和词保留变换对姓名的泄露为10.12比特，对城市的泄露为3.9比特（最大可能泄露为17.2比特）。这种泄漏虽然需要适当的辅助信息才能利用，但在实践中这些信息往往容易获取，可能导致部分数据记录被重新识别。
>
> **技术梗概:** 研究使用了香农熵来量化格式保持带来的信息泄漏，并通过实际数据集的应用验证了理论模型的有效性。

---
### [2026/994] Super-intelligence Survival Guide: Verification via Proof-Carrying Output

- **作者:** Hillel Avni, Shlomi Dolev, Avraam Yagudaev, Moti Yung

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/994) | [PDF](https://eprint.iacr.org/2026/994.pdf)


> **研究背景:** 随着大型语言模型（LLMs）在高风险领域中的广泛应用，确保AI生成结果和行为的信任度变得至关重要。然而，由于其推理过程的不透明性，用户难以验证这些结果。
>
> **主要贡献:** 本文提出了一种名为证明携带输出（PCO）的框架，该框架要求AI系统返回答案的同时附带可机器检查的证明，以正式定义φ合规性，并引入了加密问责制层来绑定AI输出及其形式证明、验证者版本和可信时间戳。
>
> **达到效果:** 这一机制确保了AI决策的不可抵赖性，这是LLM输出和单独的形式证明所不能提供的。
>
> **技术梗概:** 该技术通过在输出执行前将AI输出、其正式证明、验证者的版本以及可信时间戳绑定到一个不可否认的承诺中，并记录在只读日志上，实现了这一目标。

---
### [2026/996] Topology-Hiding Computation From Key Agreement in Diameter-Two Graphs

- **作者:** D'or Banoun, Elette Boyle, Ran Cohen

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/996) | [PDF](https://eprint.iacr.org/2026/996.pdf)


> **研究背景:** 研究背景：拓扑隐藏计算（THC）允许一组通过不完整网络通信的各方执行安全多方计算（MPC），同时隐藏网络拓扑结构，适用于特定直径的图类。
>
> **主要贡献:** 主要贡献：本文探讨了在直径为2的图上实现多个腐败情况下的拓扑隐藏广播和拓扑隐藏计算，并基于密钥协商（KA）提供了多种图类的安全协议。
>
> **达到效果:** 达到的效果：对于某些支持大量腐化的图类，提出了基于KA假设的最优抗腐化能力的THC协议。
>
> **技术梗概:** 技术梗概：使用了基于密钥协商的拓扑隐藏计算方法，并针对直径为2的图进行了优化，以实现更高的安全性和抗腐化能力。

---
### [2026/1000] Information-Theoretic Optimistic Verifiable Secret Sharing

- **作者:** Martin Hirt, Chen-Da Liu-Zhang, Emanuele Marsicano

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1000) | [PDF](https://eprint.iacr.org/2026/1000.pdf)


> **研究背景:** Verifiable secret sharing (VSS)是安全计算中的基本构建块，其通信复杂性已得到广泛研究。现有协议即使在实际故障数量低于最优阈值时也需三轮通信。
>
> **主要贡献:** 作者提出了一个信息论乐观可验证秘密共享方案，在完美安全性下当实际故障数不超过给定阈值时实现两轮通信，超过则为三轮；在统计安全性下相应地减少一轮。
>
> **达到效果:** 该方案提高了效率，特别是在实际故障数量低于理论最优阈值时显著减少了通信轮次。
>
> **技术梗概:** 通过结合信息论方法和乐观协议设计，实现了上述目标。

---
### [2026/1001] Distributed Simon's Algorithm with Less Per-Node Qubit Overhead and Its Application to Cryptanalysis

- **作者:** Zhenqiang Li, Xiao-Fan Zhen, Shu-Qin Fan, Yonglin Hao, Fei Gao

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1001) | [PDF](https://eprint.iacr.org/2026/1001.pdf)


> **研究背景:** 分布式量子计算(DQC)允许多个设备协作以降低每个节点的电路深度并解决超出单个量子设备处理能力的问题。前人研究提出了通过串联型周期函数实现的分布式Simon算法，但存在节点量子查询复杂度高和所需量子比特数多的问题。
>
> **主要贡献:** 本文提出了一种基于异或型周期函数的新分布式Simon算法，能够同时降低每个节点的量子查询复杂度和所需量子比特数量。
>
> **达到效果:** 该新算法将每个节点的量子查询复杂度降至$2c(n-t)$（其中$c>3$），与Tan等人方案相匹配；并且将每个节点所需的量子比特数从$2^{t+1}m$减少到$m+n-t$，相对于$t$呈指数级降低。
>
> **技术梗概:** 通过设计异或型周期函数，并利用分布式计算的优势，本文实现了在保持较低量子查询复杂度的同时显著减少了所需量子比特数量。

---
### [2026/1002] On weak keys of POKE

- **作者:** Tomoki Moriya

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/1002) | [PDF](https://eprint.iacr.org/2026/1002.pdf)


> **研究背景:** POKE是一种基于isogeny的公钥加密(PKE)方案，尽管其性能较高但安全性依赖于某些假设，且安全分析可能不够全面。
>
> **主要贡献:** 作者发现了POKE中的弱密钥，并指出这些弱密钥在2D设置中对整体安全性影响较小，但在4D设置中则构成威胁。
>
> **达到效果:** 通过建议新的参数以缓解弱密钥攻击，虽然使得4D设置的参数大小与2D相同，但其主要性能优势不再保持。
>
> **技术梗概:** 研究采用了一种新颖的方法来识别和分析POKE中的弱密钥，并提出了相应的对策。

---
### [2026/1005] More from Less: Composable General Multi-Party Computation with Global Public Verifiability from a Single Enclave Only

- **作者:** Saskia Bayreuther, Robin Berger, Felix Dörre, Eva Hetzel, Yufan Jiang, Christian Martin, Jeremias Mechler, Jörn Müller-Quade

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/1005) | [PDF](https://eprint.iacr.org/2026/1005.pdf)


> **研究背景:** 该研究基于可信执行环境（TEEs）的广泛应用，特别是在处理高度敏感数据时。现有模型如Pass等人的工作为在通用化普遍一致性框架下的受验证计算提供了形式化的安全分析方法。
>
> **主要贡献:** 作者提出了一个新颖的功能性设计$\mathcal{G}_{\mathrm{att}}$与局部理想功能$\mathcal{F}$结合，以实现全局公共可验证的多方计算，解决了传统模型中缺乏外部可验证性的难题。
>
> **达到效果:** 通过这种新的模拟技术，研究实现了在单一受信执行环境中进行通用多党计算，并且能够被任何外部实体进行合理的验证，显著提升了计算的安全性和透明性。
>
> **技术梗概:** 该方法涉及多个关键技术问题的解决，特别是如何协调$\mathcal{G}_{\mathrm{att}}$与$\mathcal{F}$的功能以处理欺骗行为。

---
### [2026/1010] Signal and Ready to MINGLE: In-Band Gossip for Key Transparency Split-View Detection in E2EE Messengers

- **作者:** Edona Fasllija, Lena Heimberger, Kevin Paul

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1010) | [PDF](https://eprint.iacr.org/2026/1010.pdf)


> **研究背景:** 当前E2EE信使如Signal、WhatsApp和iMessage通过部署密钥透明性（KT）来防范恶意密钥替换，但需用户锚定相同的全球KT历史记录才能有效。然而，恶意运营商可以通过等效行为破坏这一条件，向不同客户端展示不兼容的KT目录视图。
>
> **主要贡献:** 我们提出了MINGLE协议，这是一种嵌入式内部传播协议，能够在普通消息中捎带紧凑的KT承诺信息，无需外部服务或覆盖网络即可实现密钥一致性检查的分布化。
>
> **达到效果:** 通过MINGLE，客户端可以在通信过程中自动检测到等效行为，而不需要依赖第三方审计员。这使得恶意运营商维持分裂视图变得更加困难，因为需要永久隔离目标客户端以阻止任何跨分区消息的传递。
>
> **技术梗概:** MINGLE协议通过在加密前捎带KT承诺信息来实现密钥透明性的内部传播，并利用通信图中的节点分布化一致性检查任务，从而提高系统的健壮性和安全性。

---
### [2026/1011] Can We Tolerate Small Side-Channel Leakages: The Role of Registers in Glitch-Stopping Circuits

- **作者:** Artemii Ovchinnikov, Jelle Biesmans, Kris Myny, Ventzislav Nikov, Svetla Nikova

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/1011) | [PDF](https://eprint.iacr.org/2026/1011.pdf)


> **研究背景:** 研究聚焦于硬件中加密算法实现的安全性，特别是针对侧信道攻击的防护。现有技术如阈值实现和域导向掩码提供了理论上的安全性保证，并通过测试矢量泄漏评估等方法进行实验验证。
>
> **主要贡献:** 作者提出了一种新的对抗模型，探讨了寄存器布局对电路抵抗侧信道攻击的影响，旨在减少延迟和面积的同时提高安全性。
>
> **达到效果:** 研究表明，在特定逻辑链路布局下，可以通过牺牲部分寄存器来隐藏由瞬态故障引起的泄漏，从而增强设计的安全性。
>
> **技术梗概:** 通过引入新的对抗模型，并结合实验评估方法（如TVLA），作者分析了寄存器在瞬态故障防护中的作用。

---
### [2026/1012] Linear self-equivalence of the known families of APN functions: a unified point of view

- **作者:** Jules Baudrin, Anne Canteaut, Léo Perrin

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/1012) | [PDF](https://eprint.iacr.org/2026/1012.pdf)


> **研究背景:** 研究背景：已知的唯一APN函数解是通过探索Kim映射的CCZ等价类找到的，该映射与多种高度结构化的函数线性等价。
>
> **主要贡献:** 主要贡献：作者提出了一种新的类型——多变量投影映射，并证明了几乎所有已知的无限APN函数家族都可以被这种形式或与其交换Frobenius映射的函数CCZ等价。
>
> **达到效果:** 达到的效果：无论这些函数家族初始表示形式如何（单变量、双变量或三变量），都存在这样的模式，这为理解APN函数提供了统一的观点。
>
> **技术梗概:** 技术梗概：通过识别线性等价类中是否存在多变量投影映射来检测给定函数的等价形式，并开发了具体的技术来检测（或排除）此类映射的存在。

---
### [2026/1013] Sequence-Level Security for Active Weighted Signature Reconfiguration

- **作者:** Sunghyeon Jo

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1013) | [PDF](https://eprint.iacr.org/2026/1013.pdf)


> **研究背景:** 研究背景：动态调整签名者权重、阈值和委员会成员的主动加权阈值签名支持灵活的签名者变更。然而，局部有效的加权更新操作的安全性抽象存在局限性。
>
> **主要贡献:** 主要贡献：提出了秩暴露防护器（rank-exposure guards），这是一种编译器，能够确保实时、过期、衍生、公开和临时签发材料的安全重建不变式。
>
> **达到效果:** 达到的效果：通过将ledger一致的一步更新引擎与原子激活及旧周期摘要限制转换证书结合，实现了序列级的动态不可伪造性，并且在公共ADAPT Go实现之上构建了REG-ADAPT方案。
>
> **技术梗概:** 技术梗概：该编译器包裹了一步更新引擎，并通过原子激活和旧周期摘要限制过渡证书提升了固定状态加权不可伪造性和更新一致性到序列级的动态不可伪造性。

---
### [2026/1015] Comments on "Server-Aided Public Key Authenticated Searchable Encryption With Constant Ciphertext and Constant Trapdoor"

- **作者:** Takeshi Yoshida, Keita Emura

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/1015) | [PDF](https://eprint.iacr.org/2026/1015.pdf)


> **研究背景:** 该研究针对Cheng和Meng在2024年提出的一种基于服务器辅助的公钥认证可搜索加密方案（SA-PAEKS），指出其中存在的安全漏洞，使得云服务器能够从密文和陷阱门中获取关键词信息。
>
> **主要贡献:** 作者通过分析提出了两种通用攻击方法，证明了该加密方案在设计上存在缺陷，无法有效保护用户的隐私数据。
>
> **达到效果:** 研究揭示了SA-PAEKS方案的安全性不足，并为后续改进此类加密技术提供了理论依据和实际案例。
>
> **技术梗概:** 通过对密文和陷阱门的分析，作者发现了云服务器可以利用这些信息泄露关键词的秘密途径，从而验证了攻击的有效性。

---
### [2026/1016] Efficient Homomorphic String Search via TFHE

- **作者:** Shintaro Narisada, Hiroki Okada, Takashi Nishide, Kazuhide Fukushima

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/1016) | [PDF](https://eprint.iacr.org/2026/1016.pdf)


> **研究背景:** 该研究旨在通过TFHE实现加密文本中的安全模式匹配，以解决大规模数据处理中对隐私保护的需求。
>
> **主要贡献:** 本文提出的方法利用了TFHE的两种整数输入操作模式，实现了首个完全安全的二分查找算法，并显著减少了字符比较次数。
>
> **达到效果:** 实验结果显示，该方法能够在一个包含一百万字符的加密文本中快速找到长度为100的模式，比现有技术快约100倍。
>
> **技术梗概:** 研究通过结合TFHE的不同操作模式来优化二分查找算法，从而在保持安全性的前提下提高了效率。

---

## 更新: 2026-05-18 20:08

*新增 6 篇论文 (编号 974--979)*

### [推荐] [2026/974] LoTRS: Practical Post-Quantum Structured Threshold Ring Signatures from Lattices

- **匹配关键字:** lattice, post-quantum

- **作者:** Nikai Jagganath, Muhammed F. Esgin, Ron Steinfeld, Amin Sakzad, Markku-Juhani O. Saarinen, Dongxi Liu

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/974) | [PDF](https://eprint.iacr.org/2026/974.pdf)


> **研究背景:** 研究提出了一个结构化阈值环签名（structured threshold ring signature，sTRS）的概念，并设计了基于格的$\mathsf{LoTRS}$方案，旨在减少交互次数并提高效率。
>
> **主要贡献:** $\mathsf{LoTRS}$通过结合两层机制实现了这一目标：第一层是基于格的双签协议，第二层则是隐藏选择的$1$-out-of-$N$证明，从而避免了传统TRoS方案中需要的领导者和多轮交互。
>
> **达到效果:** 该方案在保持匿名性的同时显著减少了通信开销，并且具体实例化使用了$\mathsf{DualMS}$协议和Esgin等人提出的基于格的一对多证明机制。
>
> **技术梗概:** 技术上，$\mathsf{LoTRS}$通过分离签名关系和匿名机制来实现两轮交互，并利用$1$-out-of-$N$证明代替传统的$T$-out-of-$N$证明以提高效率。

---
### [推荐] [2026/975] Functional Bootstrapping for a Single LWE Ciphertext with \(\tilde{O}(1)\) Polynomial Multiplications

- **匹配关键字:** homomorphic encryption, LWE

- **作者:** Xiaopeng Zheng, Hongbo Li, Dingkang Wang

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/975) | [PDF](https://eprint.iacr.org/2026/975.pdf)


> **研究背景:** 研究背景：Bootstrap技术是将层次同态加密转换为全同态加密的关键，但其效率仍然是一个主要瓶颈。现有方法虽然实现了近似常数复杂度，但在单个密文上的非分摊常数复杂度尚未实现。
>
> **主要贡献:** 主要贡献：本文提出了一种基于BFV方案的稀疏打包多项式评估方法，实现了对大明文空间上任意函数的单个LWE密文的全同态加密功能，并支持小批量处理，总代价为近似常数级。
>
> **达到效果:** 达到的效果：在128位安全性和单线程环境下，对于9位明文的单个密文进行任意函数评估耗时3.15秒，而对128个相同密文的小批量调用则需要3.77秒；对于16位明文，则分别耗时10.6秒和14.2秒。
>
> **技术梗概:** 技术梗概：通过利用BFV密文中重复槽结构来评估任意多项式在m个加密输入上的值，总代价为近似线性级。

---
### [推荐] [2026/979] Improved Dual Attack via Quantum Rejection Sampling

- **匹配关键字:** lattice

- **作者:** Nicholas Zhao, Cong Ling

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/979) | [PDF](https://eprint.iacr.org/2026/979.pdf)


> **研究背景:** 本文重新审视了Pouly和Shen提出的双攻击框架，重点关注其中的格Lattice高斯采样步骤，这是整体攻击复杂度中的主要瓶颈。
>
> **主要贡献:** 作者通过结合Wang和Ling对Klein算法分析中的下界与Ozols等人提出的量子拒绝采样(QRS)框架，将该采样步骤加速。
>
> **达到效果:** 采用这种采样器替换原有的双攻击框架后，估计的攻击成本分别减少了9、4和13位密钥长度，适用于Kyber-512、Kyber-768和Kyber-1024。
>
> **技术梗概:** 通过使用量子拒绝采样的技术，作者能够以二次减少的方式降低采样复杂度，并选择适当的截断半径确保截断分布与完整格高斯分布之间的总变异距离可忽略不计。

---
### [2026/976] Revisiting DKLs Threshold ECDSA: Enhanced OT-based VOLE and Two-Party Signing

- **作者:** Gilad Asharov

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/976) | [PDF](https://eprint.iacr.org/2026/976.pdf)


> **研究背景:** 阈值ECDSA签名已成为保护加密货币资产的标准构建块，Doerner等人的DKLs协议因其效率和广泛采用而成为领先解决方案。
>
> **主要贡献:** 研究重新审视了DKLs协议的安全性和实现权衡，并改进了其子协议Vector Oblivious Linear Evaluation (VOLE)，提出了三种不同权衡的VOLE变体。
>
> **达到效果:** 研究成果巩固了该协议的安全性，同时通过将大部分计算和通信移至预处理阶段，显著提高了在线阶段的效率，通信量减少了约600倍。
>
> **技术梗概:** 研究通过对VOLE子协议进行彻底分析，并提出优化后的双方签名协议，实现了高效安全的阈值ECDSA签名过程。

---
### [2026/977] ThriftyMPC: Reducing the Cost of Large-Scale MPC in the Cloud

- **作者:** David Inyangson, Sahbaaz Ansari, Tushar M. Jois, Rosario Gennaro, Gamze Gursoy, Gabriel Kaptchuk, Moti Yung, Diogo Barradas

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/977) | [PDF](https://eprint.iacr.org/2026/977.pdf)


> **研究背景:** 随着云计算成为大规模计算的标准，其弹性和按需资源超越了传统的本地能力。然而，许多涉及敏感数据的大规模计算（如全基因组关联研究GWAS）因隐私和监管限制而难以采用云服务，尽管多方计算等加密原语可以提供可证明的隐私保障，但高昂的成本仍然是主要障碍。
>
> **主要贡献:** ThriftyMPC框架通过结合安全多方计算与预emption容忍执行，利用临时性云计算实例（spot instances）来解决成本和隐私问题。
>
> **达到效果:** 在Google云平台上对现实中的GWAS工作负载进行评估表明，尽管存在临时实例的频繁变更，ThriftyMPC仍能实现稳健执行，并且相比传统使用按需实例运行的最先进的多方计算框架（MP-SPDZ）显著降低了成本。
>
> **技术梗概:** ThriftyMPC通过提出在临时性计算条件下多方执行的形式模型，展示了如何处理spot实例的预emption同时保持密码学安全保证。

---
### [2026/978] Verifying Consensus Protocols from LLM-assisted TLA$^+$: A Case Study of Byzantine Reliable Broadcast

- **作者:** Shuhe Cao, Xin Wang, Chenxu Wang, Xiao Sui, Sisi Duan

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/978) | [PDF](https://eprint.iacr.org/2026/978.pdf)


> **研究背景:** TLA$^+$作为描述分布式系统的正式规范语言，但在编写时需要高深的专业知识。针对拜占庭容错共识协议（BFT），模拟恶意行为是基本挑战：简化模型会遗漏关键漏洞，而详细的模型会导致状态空间爆炸。
>
> **主要贡献:** 本文提出TLAssist工具，通过大型语言模型辅助生成半自动化的TLA$^+$规范，特别适用于拜占庭可靠广播（RBC）协议。
>
> **达到效果:** 在五个RBC协议案例研究中，TLAssist生成的规范优于许多开源TLA$^+$脚本，并能帮助专家发现深层次的设计缺陷。此外，非专家也能通过微调协议并利用生成的错误轨迹理解复杂情况。
>
> **技术梗概:** 该工具提供了一种高度结构化的流程和领域特定的数据格式来改进LLM提示的质量。

---

## 更新: 2026-05-17 21:27

*新增 25 篇论文 (编号 943--973)*

### [推荐] [2026/943] Optimized G+G Signature

- **匹配关键字:** LWE

- **作者:** Renjie Jin, Shuoqu Jian, Longjiang Qu

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/943) | [PDF](https://eprint.iacr.org/2026/943.pdf)


> **研究背景:** G+G签名基于Fiat-Shamir变换而设计，不使用拒绝采样技术，但其优化研究尚未达到Lyubashevsky类型签名的水平。
>
> **主要贡献:** 本文将Asymmetric Learning with Errors (ALWE)问题整合到G+G签名的关键生成阶段，并提出了一种更精确的秘密密钥最大奇异值估计方法及新的非球形高斯分布来描述签名分布。
>
> **达到效果:** 实验结果表明，在确保相同安全级别的前提下，优化后的G+G签名版本将签名大小减少了约25%。
>
> **技术梗概:** 通过引入ALWE问题和改进的统计模型，提高了G+G签名的安全性和效率。

---
### [推荐] [2026/945] Threshold PRISM Signature Schemes via Graph-Based Threshold Access Structures

- **匹配关键字:** post-quantum

- **作者:** Hyeonhak Kim, Won Kim, Changmin Lee

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/945) | [PDF](https://eprint.iacr.org/2026/945.pdf)


> **研究背景:** 分布式系统中的阈值签名要求紧凑的公钥和签名以减少通信开销，避免数据包分割。然而，现有的后量子阈值签名方案要么公钥过大，要么签名过长，无法完全容纳在一个未分割的数据包中。
>
> **主要贡献:** 本文提出了一种基于超曲面的后量子阈值PRISM签名方案Threshold PRISM，其公钥和签名均能在每个NIST安全级别下完全包含在单个未分割的数据包中，并且适用于任意数量的参与方。
>
> **达到效果:** 通过不同的参数选择，在NIST安全级别I/III/V下，构造实现了65-129/97-193/129-257字节的公钥和159-222/239-335/319-447字节的签名。在NIST MPTC第一轮候选方案中，我们的构造拥有最小的签名大小。
>
> **技术梗概:** 通过引入一种针对超曲面设置定制的新颖图基阈值访问结构来解决通用参与方数量下的阈值化难题。

---
### [推荐] [2026/948] Anamorphic Construction For The Winternitz OTS Scheme Family

- **匹配关键字:** post-quantum

- **作者:** Lucas Mayr, João Gabriel Feres, Bruno Bianchi Pagani, Ricardo Custódio

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/948) | [PDF](https://eprint.iacr.org/2026/948.pdf)


> **研究背景:** Winternitz One-Time Signature (WOTS)方案是后量子密码学中基于哈希函数安全性的基本构建块，已被标准化，并作为XMSS、LMS和SPHINCS等标准哈希签名方案的关键组成部分。
>
> **主要贡献:** 文章首次提出了针对WOTS家族签名方案的anamorphic构造，并证明了这些构造在传统方案中不可区分。
>
> **达到效果:** 通过形式化这些构造并在基于游戏的安全框架下进行证明，表明所得到的方案满足anamorphic不可区分性。
>
> **技术梗概:** 研究采用anamorphic假设下的游戏式安全框架来验证其安全性，并讨论了不同构造方法的支持anamorphic隐秘信道的能力和特性。

---
### [推荐] [2026/949] Quantum Circuit Realization and Grover Cryptanalysis of the Hybrid ARX-SPN Cipher GFSPX

- **匹配关键字:** post-quantum

- **作者:** Ibrahim Ulgen, Hasan Ozgur Cildiroglu, Oğuz Yayla

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/949) | [PDF](https://eprint.iacr.org/2026/949.pdf)


> **研究背景:** 随着量子计算的出现，经典对称密钥算法的安全性受到了根本性的挑战，因此需要对其后量子安全性进行严格的评估。
>
> **主要贡献:** 该研究提出了GFSPX轻量级分组密码的量子电路实现和Grover密码分析方法，展示了其在量子攻击下的表现。
>
> **达到效果:** 通过优化资源分配并采用紧凑的进位传递加法器，实现了209个量子比特的高效设计，并揭示了针对GFSPX的关键恢复攻击所需的量子门成本为1.12×2^159。
>
> **技术梗概:** 研究采用了结合4分支通用Feistel结构和ARX与SPN组件的独特混合架构，并通过并行化Grover oracle来消除误匹配，优化了电路深度和量子成本。

---
### [推荐] [2026/953] Tight Lattice-Based Signatures without Trapdoors from Search LWE

- **匹配关键字:** lattice, LWE

- **作者:** Rutchathon Chairattana-Apirom, Nico Döttling, Julian Loss, Stefano Tessaro, Benedikt Wagner

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/953) | [PDF](https://eprint.iacr.org/2026/953.pdf)


> **研究背景:** 研究紧致归约的数字签名在过去二十年中引起了广泛关注，因为这样的方案继承了其基础计算问题的基本硬度。在格基密码学背景下，GPV方法提供了一个简单的紧致归约，但依赖于预象采样的陷阱门，这通常会导致复杂的实现。
>
> **主要贡献:** 该研究首次提出了一种基于格的签名方案，该方案具有对搜索假设（即搜索LWE问题的难度）的紧致归约，并且不需要在自身中使用任何陷阱门（但证明中使用了陷阱门）。
>
> **达到效果:** 通过遵循Fiat-Shamir范式，该方案提供了一种新的基于格的签名方法。与之前的依赖决策假设的方法相比，这种基于搜索假设的方法在实际安全性方面更具优势。
>
> **技术梗概:** 为了克服格环境中固有的弱稳健性保证等技术障碍，研究开发了若干新技术来应对这些挑战。

---
### [推荐] [2026/954] Black-box validation of Falcon key generation under numerical instability

- **匹配关键字:** lattice, post-quantum

- **作者:** Maxime Bros, Christopher Celi, Pierre Ciadoux, Ray Perlner

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/954) | [PDF](https://eprint.iacr.org/2026/954.pdf)


> **研究背景:** Falcon是一种基于格的数字签名方案，以其高性能和较小的关键大小而著称，并被美国国家标准与技术研究院（NIST）选为后量子标准项目的一部分。然而，浮点数或定点数算术在Falcon中的使用带来了不可再现性等独特挑战，这可能导致实现结果不一致。
>
> **主要贡献:** 研究提出了一种新的黑盒验证方法，用于验证Falcon密钥生成的正确性，该方法能够容忍由浮点和定点数算术引起的数值不稳定性和不可再现性，并确保这些差异不会导致安全性问题。
>
> **达到效果:** 通过结合签名和验证的黑盒一致性测试，这种方法为在特定平台上验证Falcon实现的正确性提供了一种途径。此外，研究还定义并计算了使用无限精度生成的理想密钥，并估计了有效密钥总数。
>
> **技术梗概:** 该方法采用黑盒测试技术，不依赖于具体实现细节，仅通过输入输出行为来验证算法的正确性，从而避免了对实现特性的直接检查。

---
### [推荐] [2026/956] Efficient Bootstrapping in Fully Homomorphic Encryption for Matrix Arithmetic

- **匹配关键字:** homomorphic encryption

- **作者:** Eric Crockett, Craig Gentry, Hyojun Kim, Yeongmin Lee, Yongwoo Lee

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/956) | [PDF](https://eprint.iacr.org/2026/956.pdf)


> **研究背景:** 针对全同态加密（FHE）方案在矩阵算术优化方面，Gentry和Lee提出了一个专门的方案。然而，现有的基于该方案的密文重启动技术效率较低，尤其是在处理线性变换时消耗大量时间。
>
> **主要贡献:** 本文提出了一种新的高效密文重启动方法，通过将CtS和StC操作视为矩阵乘法，并利用CKKS范式中的ModRaise、EvalMod等步骤进行优化，显著减少了密钥切换操作的数量。
>
> **达到效果:** 实验结果表明，与之前的CKKS方案相比，该方法在执行线性变换时所占时间比例大幅降低至20.1%，同时其平均CtS运行时间比现有的高度优化库（Lattigo）快约3倍。
>
> **技术梗概:** 技术上，通过扩展GL方案以支持非幂次矩阵维度，并引入环上的广义迹定义来确保线性变换的正确性。此外，优化了密文重启动过程中的关键步骤，特别是将瓶颈从CtS/StC和EvalMod转移到EvalMod。

---
### [推荐] [2026/957] Threshold FHE with Short Decryption Shares without a Semi-trusted Server

- **匹配关键字:** homomorphic encryption

- **作者:** Hiroki Okada, Tsuyoshi Takagi

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/957) | [PDF](https://eprint.iacr.org/2026/957.pdf)


> **研究背景:** 传统的阈值全同态加密（ThFHE）方案由于需要超多项式模数，导致密文、密钥和解密份额过长。Passel`egue 和 Stehl´e 提出了一种解决方案，通过半可信服务器对输入密文进行四舍五入处理来缩短密文长度，但该方案在单个参与方与服务器合谋的情况下存在安全风险。
>
> **主要贡献:** 本文提出了一种无需半可信服务器的阈值全同态加密方案，使得解密份额为多项式长度，并通过降通信技术将输入密文发送给各方的成本降低到多项式级别。
>
> **达到效果:** 该方案在确保安全性的同时实现了低通信成本的阈值全同态加密，提高了实际部署的可能性。
>
> **技术梗概:** 本文的核心思想是让参与方直接对解密份额进行四舍五入处理，而非依赖半可信服务器对密文进行处理，并通过降通信技术降低发送输入密文的成本。

---
### [推荐] [2026/964] Beyond Quadratic: Unlocking Pseudorandomness with Quartic Character

- **匹配关键字:** post-quantum

- **作者:** Mriganka Dey, Sampa Dey, Sampurna Pal, Subhabrata Samajder, Rana Barua

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/964) | [PDF](https://eprint.iacr.org/2026/964.pdf)


> **研究背景:** 研究通过探讨四次狄利克雷特征产生的伪随机性，结合解析和密码学视角，旨在超越二次特征的限制，探索更高阶特征在伪随机生成器中的应用。
>
> **主要贡献:** 贡献在于定义了基于四次特征的布尔函数$\psi_\pi$，并通过经典字符和修正后的Mauduit-Sárközy及Oon界展示了其强伪随机性，并证明了四次特征可用于安全的伪随机生成器和弱伪随机函数。
>
> **达到效果:** 结果表明，在二次 residuosity 假设下，四次特征不仅能够提供安全的伪随机生成器，还能确保$\mathsf{Quartapus}$签名方案及$\mathsf{PorcRoast}_{4}$后量子安全签名方案的安全性和效率优势。
>
> **技术梗概:** 采用Corrigan-Gibbs和Wu的技术，通过一系列多项式时间归约证明了区分四次wPRF等价于解决二次 residuosity 问题，并利用经典字符和修正后的界分析了序列的伪随机性质。

---
### [推荐] [2026/966] A New Multiscalar Multiplication Method Resistant to Timing Attacks

- **匹配关键字:** homomorphic encryption

- **作者:** Abhraneel Dutta, Veronika Kuchta, Francesco Sica

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/966) | [PDF](https://eprint.iacr.org/2026/966.pdf)


> **研究背景:** 多标量乘法（MSM）是现代密码系统中的核心操作，广泛应用于零知识简洁非交互式知识论证（ZK-SNARKs）和同态加密等应用中。在基于椭圆曲线的ZK-SNARK构建中，MSM占总证明生成时间的80-90%，因此优化至关重要。
>
> **主要贡献:** 本文重新审视了Pippenger的MSM算法，并提出了一种新的标量编码算法，将传统的$q$进制表示转换为等效的非零表示，从而确保所有标量位均被均匀处理。在此基础上，我们引入了一种避免零位的安全Pippenger桶方法。
>
> **达到效果:** 通过这些改进，我们的MSM算法在保持性能提升近25%的同时实现了对定时攻击的抵抗力。这是首个明确设计用于抵抗定时攻击的MSM算法。
>
> **技术梗概:** 我们提出了一种新的标量编码技术，将包含零位的传统$q$进制表示转换为等效的非零表示，并在此基础上改进了Pippenger的桶方法，避免使用零位。此外，利用端元本征分裂进一步缩短了数字扩展并提高了效率。

---
### [推荐] [2026/971] Explicit cost analysis of Toom-4 multiplication for incomplete NTT in lattice-based cryptography

- **匹配关键字:** lattice

- **作者:** Sakura Oku, Momonari Kudo

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/971) | [PDF](https://eprint.iacr.org/2026/971.pdf)


> **研究背景:** 在基于格的密码学中，多项式乘法是基础操作。Hafiz等人通过分析不完全NTT解决了模数约束问题，但Toom-4的具体成本表达式尚未与该框架兼容。
>
> **主要贡献:** 本文重新审视了不完全NTT背景下Toom-4乘法，并推导出明确的操作计数，区分了系数域内的加减法和乘法操作。
>
> **达到效果:** 通过基于加法链的分析，我们提出了一个简洁的成本模型，并实验验证了结合使用Toom-4、Karatsuba和不完全NTT的混合策略的有效性。
>
> **技术梗概:** 本文采用加法链方法来推导成本模型，并通过具体实现和操作计数分离技术来评估不同参数范围内的性能优势。

---
### [推荐] [2026/973] Asynchronous Lagrange-Based Threshold FHE with Smaller Modulus Overhead

- **匹配关键字:** homomorphic encryption

- **作者:** Won Kim, Changmin Lee, JeongHwan Lee, Alain Passelègue, Damien Stehlé

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/973) | [PDF](https://eprint.iacr.org/2026/973.pdf)


> **研究背景:** 研究了基于Shamir秘密共享的异步设置下的$t$-out-of-$n$门限全同态加密（ThFHE），重点关注Lagrange重构在分布式解密中的噪声放大问题，导致需要更大的密文模数以保持正确性。
>
> **主要贡献:** 通过严格的分析和比较不同的Lagrange插值点族，提出了新的参数选择方案，显著减少了分布式解密所需的模数开销。
>
> **达到效果:** 与先前的参数化相比，在$n = 512$的情况下，对于$t = n/2$，模数开销减少了30%，而对于接近$n$的$t$值，则最多可减少90%。
>
> **技术梗概:** 通过分析正确性和模拟安全性约束条件来选择Lagrange插值点族，并据此提供理论上的边界以更准确地跟踪实际行为。

---
### [2026/944] On MPC-friendly Softmax

- **作者:** Marcel Keller, Ke Sun

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/944) | [PDF](https://eprint.iacr.org/2026/944.pdf)


> **研究背景:** softmax函数在深度学习中用于映射表示到概率分布，但由于其基于昂贵的指数函数，在多方计算中效率较低。
>
> **主要贡献:** 作者分析了简化替代方案在单层网络中的显著加速效果，并提出了一个新颖的安全幂运算协议以减少通信量并保持准确性。
>
> **达到效果:** 研究发现，该替代方案仅对单层网络提供速度优势，但始终降低精度，有时差异很大，因此建议使用原始softmax函数。
>
> **技术梗概:** 通过比较分析和提出新型安全幂运算协议来优化多方计算中的softmax实现。

---
### [2026/946] Constant-Round Secure Distributed Decoding and HQC Threshold Decryption

- **作者:** Pascal Giorgi, Fabien Laguillaumie, Lucas Ottow, Damien Vergnaud

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/946) | [PDF](https://eprint.iacr.org/2026/946.pdf)


> **研究背景:** 文章旨在提出首个适用于分布式解密HQC密文的专用协议，增强基于HQC的门限公钥加密系统的安全性与实用性。
>
> **主要贡献:** 贡献在于首次实现了针对Reed-Muller和Reed-Solomon编码错误单词的安全分布式解码，并开发了多项创新技术以支持特定的多方计算任务。
>
> **达到效果:** 这些成果不仅推动了HQC门限密码体制的发展，还为安全分布式计算提供了新的方法和技术，可能在其他高级加密协议中找到独立应用价值。
>
> **技术梗概:** 通过设计用于特征2域中的特定多方计算的新技术，包括多数投票协议和共享多项式上Padé逼近的安全求解协议来实现上述贡献。

---
### [2026/950] Beyond the Anonymous Inbox: Secure Whistleblowing for All

- **作者:** Gabriel Wechta, Mirosław Kutyłowski, Tomasz Lizurej, Ewa Syta

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/950) | [PDF](https://eprint.iacr.org/2026/950.pdf)


> **研究背景:** 该研究针对欧盟指令（EU）2019/1937对举报渠道的全面要求，旨在设计一个符合规范的举报系统。
>
> **主要贡献:** 提出了一个基于合规性的威胁模型和安全目标，并设计了一个包含注册与报告分离、可审计日志服务及身份管理组件的具体举报系统架构。
>
> **达到效果:** 该系统能够保护报告内容和报告者的机密性，限制提交给授权人员，并确保符合法定时限下的程序处理和记录可追溯性。
>
> **技术梗概:** 通过分离注册与报告流程，结合使用可审计日志服务和身份管理组件来实现举报过程中的匿名性和可问责性。

---
### [2026/951] Early-stopping Consensus with Adaptive Bit Complexity

- **作者:** Erica Blum, Christoph Lenzen, Julian Loss

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/951) | [PDF](https://eprint.iacr.org/2026/951.pdf)


> **研究背景:** 传统的拜占庭容错协议受到强健的下限约束，涉及最优鲁棒性、轮次复杂性和通信复杂性。然而，当实际故障数量$f$小于最大可容忍故障数$t$时，并不意味着这些下限立即排除了更快且更少通信的可能性。
>
> **主要贡献:** 本文提出了一种随机化、提前停止的拜占庭协议，具有自适应通信复杂度，在同步网络中最多$n/2$个节点故障的情况下，可在$O(f+1)$轮内终止，并且在失败概率为$2^{-\kappa}$时，比特复杂度为$O((f+1)n\kappa)$。
>
> **达到效果:** 该协议能够在实际故障数少于最大可容忍故障数的条件下，显著减少通信量和终止时间，同时对抗强适应性攻击者。
>
> **技术梗概:** 通过设计自适应通信策略和随机化算法，在保证安全性的前提下实现了提前停止功能，并减少了通信复杂度。

---
### [2026/955] YsPIR: HE-Based Single-Server Private Information Retrieval with Low Communication Cost and High Throughput

- **作者:** Yingchu Lv, Yanbin Pan, Huaxiong Wang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/955) | [PDF](https://eprint.iacr.org/2026/955.pdf)


> **研究背景:** YsPIR是一种改进的单服务器私有信息检索协议，旨在提高服务器响应时间和离线通信效率。
>
> **主要贡献:** 该研究提出了第一维度折叠技术，显著降低了在线计算时间并减少了离线阶段所需的公钥材料。
>
> **达到效果:** 实验结果显示，YsPIR在高吞吐量设置下实现了约1.64倍的在线吞吐量提升，并将离线通信量减少了约3.09倍。
>
> **技术梗概:** 通过利用第一维度折叠技术，YsPIR能够将最耗资源的计算预处理到离线阶段，从而减少在线响应时间。

---
### [2026/959] Operationalising Post‑Quantum TLS: Automated Configuration Profiling and Hybrid PQC Deployment in Financial Infrastructure

- **作者:** Harish Balaji, Aarav Varshney, Prasanna Ravi, Sripal Jain, Robin Foe, Jorden Seet, Huaxiong Wang, Kwok-Yan Lam, Anupam Chattopadhyay

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/959) | [PDF](https://eprint.iacr.org/2026/959.pdf)


> **研究背景:** 随着大规模量子计算机的出现，组织正急于升级其加密基础设施以实现后量子安全。现有的PQC标准适用于密钥交换和数字签名，但如何在复杂的环境中可靠地部署这些标准仍然是一个亟待解决的问题。
>
> **主要贡献:** 本文提出了一种配置解析方法，能够自动提取并标准化主流企业Web服务器堆栈中的TLS加密状态，生成统一且可追溯的加密库存，为迁移和合规提供基础。
>
> **达到效果:** 该方法在8,443个实际Nginx配置中进行了验证，并在一家金融机构的概念验证部署中实现了ML-KEM-512和X25519-ML-KEM-768在TLS终止点的上线，展示了其有效性和可行性。
>
> **技术梗概:** 通过机器学习技术自动解析和标准化TLS配置，生成详细的加密库存，支持后量子密钥交换算法的部署。

---
### [2026/961] Delving Deep into Security Guarantees against Integral Distinguishers with Applications to PRESENT, TWINE and LBLOCK

- **作者:** Shuo Peng, Jiahui He, Kai Hu, Meiqin Wang

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/961) | [PDF](https://eprint.iacr.org/2026/961.pdf)


> **研究背景:** 针对PRESENT、TWINE和LBLOCK等密钥流密码，integral攻击构成了重要的安全威胁。现有方法难以提供全面的安全保障，并且在处理复杂Feistel结构时存在局限性。
>
> **主要贡献:** 作者提出了避免干扰多项式的策略，成功证明了11轮PRESENT的安全性，并扩展了integral抵抗性质到一般的Feistel网络结构TWINE和LBLOCK中。
>
> **达到效果:** 研究提高了对PRESENT的攻击抵抗性，从13轮提升至11轮，并首次确认了20轮TWINE的安全边界。
>
> **技术梗概:** 通过分析目标密码的第一和最后一部分中的干扰多项式特性，作者提出了一种关键的选择密钥多项式的策略，从而加速了识别过程并提高了安全性证明的效率。

---
### [2026/963] Multi-leveled and ISA/IEC 62443-aware Certificate Transparency to Protect the PKI Service Supply Chain of Operational Technology

- **作者:** Adrian Reuter, Michael P. Heinl, Maximilian Pursche

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/963) | [PDF](https://eprint.iacr.org/2026/963.pdf)


> **研究背景:** 针对工业自动化和控制系统(IACS)中日益扩大的攻击面，研究者探索将公共网络中的证书透明度(CT)技术应用于OT环境以增强PKI服务供应链的安全性。
>
> **主要贡献:** 提出了一种适应于IACS的多层级和ISA/IEC 62443意识下的证书透明度方案，旨在解决OT环境中PKI服务提供方带来的信任依赖问题。
>
> **达到效果:** 通过实验证明了该方法在缺乏针对OT设备的加密库支持下仍具有可行性，并展示了其对增强OT环境安全性的潜力。
>
> **技术梗概:** 采用了修改后的CT流程和角色分配，构建了一个由IACS操作者控制的CT基础设施，并设计了一种分层架构以符合ISA/IEC 62443标准。

---
### [2026/965] Device Binding for Anonymous Credentials on Legacy Phones

- **作者:** Anja Lehmann, Alexandros Zacharakis

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/965) | [PDF](https://eprint.iacr.org/2026/965.pdf)


> **研究背景:** 随着全球数字身份系统的构建，旨在实现安全、便捷且隐私保护的用户认证，匿名凭证被开发用于确保选择性属性披露和不可链接的身份验证。然而，现有解决方案缺乏设备绑定功能，即将存储在用户手机上的凭证与其中的安全硬件元素绑定，以防止凭证克隆或共享。
>
> **主要贡献:** 本文展示了如何通过结合基于对配曲线的匿名凭证及其原生设备绑定协议，以及现有的ECDSA签名和经典P256曲线，使匿名凭证能够在旧款手机上实现设备绑定功能。
>
> **达到效果:** 该方法使得在不兼容现有安全硬件的前提下，在旧款手机上实现了高效的设备绑定功能，从而支持了匿名凭证的使用。
>
> **技术梗概:** 通过引入一种新的协议机制，将对配曲线应用于ECDSA签名环境中，并结合特定的安全硬件保护措施来实现这一目标。

---
### [2026/967] Revisiting Linear Subspace Trails in Poseidon2 and Neptune

- **作者:** Enyan Li, Gaoli Wang

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/967) | [PDF](https://eprint.iacr.org/2026/967.pdf)


> **研究背景:** Poseidon2和Neptune通过在内部部分轮次中稀疏激活S盒来降低算术化成本，这使得线性子空间路径与代数攻击相关。
>
> **主要贡献:** 研究者重新审视了Poseidon类似设计中的无限和有限线性子空间路径，并探讨了产生无限路径的不变子空间条件。
>
> **达到效果:** 对于宽度为$t$的状态，在每轮激活$s$个S盒坐标的情况下，当不存在这样的不变子空间时，有限路径长度最多为$\lceil t/s\rceil-1$。对于Poseidon2和Neptune，这给出了至多$t-1$个连续的线性化内部部分轮次。
>
> **技术梗概:** 研究者通过分析Cauchy MDS矩阵的特征多项式来关联不变子空间条件，并讨论了在大特征域上的可能性。

---
### [2026/968] Frobenius-UOV: A Very Efficient Multivariate Public Key Signature Scheme

- **作者:** Gilles Macario-Rat

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/968) | [PDF](https://eprint.iacr.org/2026/968.pdf)


> **研究背景:** Frobenius-UOV是一种基于油醋不平衡（UOV）家族的多变量公钥签名方案，旨在通过使用特定结构化的二次多项式来提高效率和安全性。
>
> **主要贡献:** 该方案通过对传统的UOV方案进行改进，采用 Frobenius型二次形式替代通用的二次多项式，从而实现了更紧凑的公钥表示，并保持了高效的签名过程。
>
> **达到效果:** 实验结果表明，Frobenius-UOV在密钥生成、签名和验证的成本上具有竞争力，同时显著减小了公钥和签名的大小。
>
> **技术梗概:** 该方案通过从紧凑的秘密描述中推导出公共系统，并详细描述了密钥生成、签名和验证算法来实现其目标。

---
### [2026/969] Icy-DVRF: A Distributed Verifiable Random Function based on FROST signatures

- **作者:** Ahmet Ramazan Ağırtaş, Arda Buğra Özer, Zülfükar Saygı, Oğuz Yayla

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/969) | [PDF](https://eprint.iacr.org/2026/969.pdf)


> **研究背景:** Web3安全依赖于无偏且不可预测的随机性，分布式可验证随机函数(DVRFs)能够消除单点故障，但现有设计往往在性能上有所妥协。
>
> **主要贡献:** Icy-DVRF通过引入类似于FROST的预处理方案，减少了参与者间的交互轮次，并保持了常量大小的证明，从而提高了DVRF的效率。
>
> **达到效果:** 与基于对偶配对的标准设计相比，Icy-DVRF在验证成本上实现了显著降低，理论估计约为标准设计的一 quarter。实验测试表明其性能优于现有的成对基协议。
>
> **技术梗概:** 该协议采用非交互式零知识证明的阈值结构来减少额外通信开销，并通过预处理方案降低了交互轮次。

---
### [2026/972] Breaking ACDGV MinRank Gabidulin encryption schemes over matrix codes

- **作者:** Thai Hung Le

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/972) | [PDF](https://eprint.iacr.org/2026/972.pdf)


> **研究背景:** 文章针对Aragon等在Asiacrypt 2024提出的增强Gabidulin矩阵码(EGMC)进行攻击研究，旨在揭示其加密方案的安全性假设并提出有效的破解方法。
>
> **主要贡献:** 作者通过结合组合和代数技术，首次展示了如何从被掩盖的EGMC代码中恢复等价的Gabidulin压缩代码，并进一步将其扩展为完整的等价秘密密钥。
>
> **达到效果:** 该攻击成功区分了EGMC加密方案与随机矩阵码，并且能够以多项式时间复杂度破解所有16种参数集，显著降低了声称的安全水平。例如，在(2,17,37,4,0)参数集中将安全级别从186比特降至仅35比特。
>
> **技术梗概:** 攻击利用了组合和代数方法来恢复等价的压缩代码，并在多项式时间内扩展为完整的等价秘密密钥，从而实现对EGMC加密方案的有效破解。

---

## 更新: 2026-05-15 21:33

*新增 22 篇论文 (编号 918--942)*

### [推荐] [2026/921] Adaptively Secure Permissive Unbounded Inner Product Functional Encryption from Lattices

- **匹配关键字:** lattice, post-quantum

- **作者:** SUPRAVA ROY, Ratna Dutta

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/921) | [PDF](https://eprint.iacr.org/2026/921.pdf)


> **研究背景:** 内积功能加密(IPFE)在无界设置下的容许关系提供了在不可信云环境中实现细粒度访问控制的强大密码学方法，并广泛应用于云计算安全、电子健康记录的受控访问、网络隐私、移动数据保护及物联网等领域。
>
> **主要贡献:** 本文首次提出了基于格的适应性安全且无界的容许内积功能加密方案，该方案在随机预言模型中实现了适应性不可区分性，并假设学习误差问题的困难性来保证安全性。
>
> **达到效果:** 该方案在后量子安全环境中提供了隐私保护机制，并通过实验验证了其计算效率较高。
>
> **技术梗概:** 该技术基于修改后的Abdalla等人(ASIACRYPT 2020)提出的ALS-IPFE方案，采用了格基的方法来实现无界设置和容许关系的支持。

---
### [推荐] [2026/924] RIC: Randomize Invalid Coefficients to Mitigate Side-Channel Assisted Chosen-Ciphertext Attacks on ML-KEM

- **匹配关键字:** lattice, post-quantum

- **作者:** Junichi Sakamoto, Kentaro Imafuku

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/924) | [PDF](https://eprint.iacr.org/2026/924.pdf)


> **研究背景:** 模块格基密钥封装机制（ML-KEM）容易受到侧信道辅助选择明文攻击（SCA-CCAs），这些攻击利用解封装过程中重新加密过程的泄漏，使对手能够用数百到数千次查询恢复密钥，对后量子密码学的实际部署构成严重威胁。
>
> **主要贡献:** 该论文提出了一种名为RandInvalidCoeff的新颖且轻量级对策，通过在解密函数中引入随机性来缓解SCA-CCAs。
>
> **达到效果:** 通过在解密消息多项式中的无效系数中注入随机性，RandInvalidCoeff显著减少了攻击者进行可靠密钥恢复的能力，并通过理论分析和实际测试验证了其效果。
>
> **技术梗概:** RandInvalidCoeff通过对解密过程中无效系数的随机化处理，增加了侧信道观测中的概率错误，从而降低了信息泄漏量。

---
### [推荐] [2026/925] LogVOLE: Succinct and Efficient Chosen-Input VOLE for ZK and Beyond

- **匹配关键字:** LWE

- **作者:** Lucien K. L. Ng, Peter Rindal, Akash Shah

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/925) | [PDF](https://eprint.iacr.org/2026/925.pdf)


> **研究背景:** 随机向量不知情线性评估（VOLE）关联广泛用于零知识证明和安全计算，但现有方法在接收方实际输入上的应用仍存在主要通信瓶颈。
>
> **主要贡献:** \(\textsf{LogVole}\) 提出了一个具体高效的选定输入 VOLE (CI-VOLE) 协议，实现了对数级的端到端通信量，并支持公钥非交互模式。
>
> **达到效果:** 该协议在环-LWE 下实现了多项式对数的端到端通信复杂度和每查询操作复杂度，并且能够为固定 \(\Delta\) 的情况提供可重用参数。
>
> **技术梗概:** 通过递归收缩/扩展设计，\(\textsf{LogVole}\) 验证了选定输入的小摘要关系并将其扩展回完整向量。

---
### [推荐] [2026/927] Fully Homomorphic Encryption on the Ring of Gaussian Periods

- **匹配关键字:** homomorphic encryption

- **作者:** Yimeng He, San Ling, Yimin Shi, Benjamin Hong Meng Tan, Huaxiong Wang, Allen Siwei Yang

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/927) | [PDF](https://eprint.iacr.org/2026/927.pdf)


> **研究背景:** 研究背景：Geelen和Vercauteren提出了一种基于通用BFV（GBFV）的全同态加密方案，通过使用特定形式的多项式环来减少SIMD槽的数量，从而降低维度并提高灵活性。然而，这种方法限制了模数的选择范围，仅限于大素数，这在某些应用场景中可能是不必要的。
>
> **主要贡献:** 主要贡献：本文提出了一种基于分解环子环的新方法来进行全同态加密（FHE），通过引入编码和解码映射的方法，在保持足够安全性的前提下进一步降低维度，提高了效率。
>
> **达到效果:** 达到的效果：实验结果表明，使用该方法可以实现更高的效率，并且在实际应用中表现出色，证明了其可行性。
>
> **技术梗概:** 技术梗概：通过利用分解环的子环结构，在模数选择上更加灵活，并开发了适用于子环的编码和解码映射的方法，从而优化了全同态加密方案的性能。

---
### [推荐] [2026/928] Wombat: Post-Quantum Blind Signature from Standard Group Action Assumptions and More

- **匹配关键字:** post-quantum

- **作者:** Lucjan Hanzlik, Yi-Fu Lai, Eugenio Paracucchi, Edoardo Persichetti

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/928) | [PDF](https://eprint.iacr.org/2026/928.pdf)


> **研究背景:** 该研究旨在改进Tanuki盲签名框架，以解决其依赖非标准假设带来的安全性和性能问题。
>
> **主要贡献:** 作者提出了一种新的基于标准假设的盲签名方案Wombat，并通过特定技术减少了LESS实例下的签名大小。
>
> **达到效果:** Wombat实现了并发安全性，并且在保持高效性的同时，依赖于更广泛接受的标准假设。
>
> **技术梗概:** 该研究采用了针对代码基础的具体技术来减小签名尺寸，并提供了对标准问题的严格归约。

---
### [推荐] [2026/932] Zephyr: GPU-Efficient Homomorphic Encryption for Privacy-Preserving Transformer Inference

- **匹配关键字:** homomorphic encryption

- **作者:** Sieun Seo, Chohong Min

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/932) | [PDF](https://eprint.iacr.org/2026/932.pdf)


> **研究背景:** 现有的CKKS方案主要基于64位同余数系统(RNS)表示，与现代GPU优化的32位整数算术不匹配，导致了显著的计算开销，限制了加密变换器推理的实际应用。
>
> **主要贡献:** Zephyr框架通过采用32位算术和嫁接技术重新设计CKKS，并构建完全由30位素数组成的RNS基，从而简化了模数管理并提高了操作灵活性。
>
> **达到效果:** 与基于固定25-30素系统的Cheddar相比，Zephyr减少了缩放开销并优化了密文-密文矩阵乘法（CCMM），进一步提升了加密变换器推理的效率。
>
> **技术梗概:** Zephyr通过嫁接结构解耦了比例管理与模数链，并利用辅助嫁接结构实现了灵活的比例调整，同时保持了高效的32位GPU执行能力。

---
### [推荐] [2026/935] SoK: Private LLM Inference using Approximate Homomorphic Encryption

- **匹配关键字:** homomorphic encryption

- **作者:** Ahmad Al Badawi, Andreea Alexandru, Yuriy Polyakov, Vinod Vaikuntanathan

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/935) | [PDF](https://eprint.iacr.org/2026/935.pdf)


> **研究背景:** 尽管近期关于增强隐私技术的综述认为FHE在现代ML架构中无法实现实用性，但基于CKKS框架的20种方法已证明能够实现具有高达8B参数的LLM的端到端私有推理。然而，随着该领域的快速发展，文献变得碎片化，不同框架在密文布局、模型保真度、软件和硬件堆栈以及报告指标方面存在差异，这阻碍了直接比较和可重复性。
>
> **主要贡献:** 本文首次系统化地总结了基于CKKS的非交互式私有LLM推理的知识。我们提出了一个私有LLM卡系统(PLCS)，以标准化研究人员之间的框架配置和结果报告，并引入了一个模型保留的参考框架POLARIS，支持BERT-Tiny和BERT-Mini的加密推理并利用GPU加速提高性能。
>
> **达到效果:** 我们的分析表明，只有大约20%的调查实现是模型保真的，即它们评估了标准、未修改的LLM而无需重新训练或架构替换。
>
> **技术梗概:** 我们通过定义两个轴来分类设计空间：一个模型级轴（线性块的密文布局和非线性块的模型保留）以及一个系统级轴（涵盖硬件、编译器、密钥管理及混合执行）。

---
### [推荐] [2026/936] Efficient and Privacy-preserving Outsourced Training of Decision Tree Models Based on (Leveled) Fully Homomorphic Encryption

- **匹配关键字:** lattice, homomorphic encryption

- **作者:** Tongyu Xu, Jun Wang, Honglian Liang, Shiwei Xu

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/936) | [PDF](https://eprint.iacr.org/2026/936.pdf)


> **研究背景:** 传统的机器学习模型训练对计算资源要求高，云外包训练能缓解本地资源限制，但存在隐私泄露风险。现有方法如多方计算(MPC)或基于格的全同态加密(HE)通常会带来较高的通信或计算开销。
>
> **主要贡献:** 本文提出了一种基于(SLEveled)全同态加密的高效且保护隐私的决策树模型外包训练方案，通过使用对称全同态加密(SHE)，并结合修改后的基尼不纯度指数(MGII)和SIMD打包技术来加速处理。
>
> **达到效果:** 实验结果表明，该方案显著降低了整体执行时间，并在准确率方面达到了与现有方法相当甚至更好的效果，同时保证了数据和模型的隐私性。
>
> **技术梗概:** 利用SHE实现快速训练，通过MGII适应整数同态操作限制，并使用SIMD打包技术加速处理过程。

---
### [推荐] [2026/938] Storing Less in-the-Head: An Area-Efficient Hardware Architecture for SDitH-v2

- **匹配关键字:** lattice, post-quantum

- **作者:** Stef Halmans, Niklas Höher, Dina Hesse, Sanjay Deshpande, Jakub Szefer, Tim Güneysu

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/938) | [PDF](https://eprint.iacr.org/2026/938.pdf)


> **研究背景:** 随着NIST启动第二轮后量子数字签名方案征集，旨在扩展算法多样性，SDitH-v2作为基于VOLE-in-the-Head框架的候选方案之一，面临在资源受限嵌入式设备上的应用挑战。
>
> **主要贡献:** 研究提出了一个面积高效的硬件架构，并优化了Batch Line Commitment和Polynomial Interactive Oracle Proof两种关键组件，显著减少了内存需求。
>
> **达到效果:** 与SDitH-v1相比，SRAM使用量降低了82到104倍，同时保持了竞争力的运行时间；展示了该技术在软件实现中的潜在应用价值。
>
> **技术梗概:** 通过详细分析SDitH-v2规范和参考实现之间的差异，并针对性地优化硬件设计，实现了内存使用的大幅减少。

---
### [推荐] [2026/939] More Efficient SNARKs via Quasi-Abelian Codes: Faster, Smaller, and Field-Agnostic

- **匹配关键字:** post-quantum

- **作者:** Zhe Li, Hongqing Liu, Chaoping Xing, Yizhou Yao, Chen Yuan

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/939) | [PDF](https://eprint.iacr.org/2026/939.pdf)


> **研究背景:** 现有非交互式知识证明（SNARKs）方案主要依赖线性纠错码来实现高效且安全的验证，但尚未找到同时具备高最小距离和快速编码算法的理想候选代码。
>
> **主要贡献:** 本文通过构造一类在任意大素域上的拟阿贝尔（QA）码族，实现了既具有较高最小距离又具备快速编码算法的线性纠错码。
>
> **达到效果:** 实验结果表明，在实际参数设置下，该随机QA码能实现Gilbert-Varshamov界，并且相对最小距离显著优于现有方案如Spielman码。
>
> **技术梗概:** 通过精细分析随机QA码在秩为1和指数c下的群环$\mathbb{F}_p[\mathbb{Z}_2^n]$中的具体最小距离，证明其可达到Gilbert-Varshamov界，并展示了在特定参数设置下相对最小距离的提升。

---
### [推荐] [2026/942] On the Investigation of Variants for Discrete Logarithm Problems in Abelian Groups: An Algebraic Structure Approach

- **匹配关键字:** post-quantum

- **作者:** Denis Wong Chee Keong, Low Lik How

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/942) | [PDF](https://eprint.iacr.org/2026/942.pdf)


> **研究背景:** 本文研究了基于不同代数群性质的离散对数问题（DLP）变体，特别是在阿贝尔群中，多生成元DLP在多项式时间内可约化为经典DLP实例，表明这些变体继承了传统DLP的安全性弱点。
>
> **主要贡献:** 作者提出了将多生成元DLP从阿贝尔群转移到非阿贝尔群的方案，并详细描述了一个基于非交换结构的具体问题定义。
>
> **达到效果:** 通过这种变换，可以避免已知的量子攻击，为后量子安全性的新假设提供可能的新代数结构。
>
> **技术梗概:** 研究利用了代数群的不同性质，特别是阿贝尔群与非阿贝尔群之间的差异来构建新的DLP变体，并分析其在量子计算环境下的安全性。

---
### [2026/918] Efficient 1-Round MVZK for Dishonest Majority with Superior Online Overhead

- **作者:** Yuanyuan Duan, Hongxu Yi, Yu Chen

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/918) | [PDF](https://eprint.iacr.org/2026/918.pdf)


> **研究背景:** 现有零知识证明协议在处理大规模声明时证明者开销高，而指定验证者零知识(DVZK)虽然提高了证明者的效率和可扩展性，但仅限于单一验证者。因此，在需要证明者同时向多个验证者证明同一陈述且不增加证明者开销的场景中存在技术缺口。
>
> **主要贡献:** 本文提出了一种高效的一轮多验证者零知识(MVZK)协议，能够在预处理模型下抵抗大多数恶意行为者的攻击，并在保持证明者效率的同时扩展到多方设置。
>
> **达到效果:** 该协议仅需证明者向所有验证者发送一次消息即可完成证明过程，相较于现有的一轮MVZK协议减少了多项式次数的乘法运算，显著提高了在线开销效率。实验结果表明，该协议实现了优于现有方案的效果。
>
> **技术梗概:** 通过优化零知识证明的技术细节和引入预处理模型，本文设计了一种新的MVZK协议，能够在保证安全性和效率的同时满足多验证者场景的需求。

---
### [2026/922] Generic Construction of CCA-Secure PKE from Key-Insulated and Privacy-Preserving Signatures with Publicly Derived Public Key

- **作者:** Ryo Mizuno, Keita Emura

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/922) | [PDF](https://eprint.iacr.org/2026/922.pdf)


> **研究背景:** 为了增强隐蔽地址的安全性和保护用户隐私，Liu等人提出了一个结合密钥隔离和隐私保护签名机制的方案（PDPKS），其中支付方生成主公私钥对，支付方使用该主公钥生成派生公钥并绑定加密资产。
>
> **主要贡献:** 本文展示了如何从PDPKS中泛型构建出选择明文攻击（CCA）安全的公钥加密（PKE）方案。
>
> **达到效果:** 通过利用不可关联性隐藏派生公钥的来源主公钥，以及模拟解密预言机来确保方案正确性，实现了这一目标。
>
> **技术梗概:** 该技术依赖于PDPKS中的不可关联性属性和一致性属性，以保证最终构建出的PKE方案的安全性。

---
### [2026/923] Practical and Verifiable Encrypted Vector Search for Retrieval-Augmented Generation

- **作者:** Xiangyu Hui, Xingliang Yuan, Olga Ohrimenko, Sid Chi-Kin Chau

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/923) | [PDF](https://eprint.iacr.org/2026/923.pdf)


> **研究背景:** 针对外包的检索增强生成（RAG）系统中的向量检索阶段，存在查询意图泄露、数据库信息外泄及恶意服务提供商操控检索结果的风险，需要一种既能保护隐私又能验证检索结果正确性的方案。
>
> **主要贡献:** VeriANN是首个同时实现查询隐私、数据库保密性和检索结果可验证性的加密近似最近邻（ANN）检索框架，适用于非协作双服务器模型。
>
> **达到效果:** VeriANN通过结合基于分布式点函数的局部敏感哈希索引私有信息检索与认证门限电路，实现了从解密桶到构建Merkle树根、频率计数及top-k选择的整个过程的全同态执行和端到端完整性。
>
> **技术梗概:** VeriANN采用了基于排序的分层模糊频率计算等三项新技术来确保其实现的可行性与效率。

---
### [2026/926] Private Function Evaluation with Linear Complexity

- **作者:** Shuaishuai Li, Cong Zhang, Anyu Wang, Xiaoyun Wang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/926) | [PDF](https://eprint.iacr.org/2026/926.pdf)


> **研究背景:** 研究背景：现有私有函数评估(PFE)协议在电路大小和参与方数量上复杂度较高，且主要支持布尔电路。
>
> **主要贡献:** 主要贡献：提出了一种新型框架，实现了首个线性复杂度的PFE协议，适用于布尔和算术电路。
>
> **达到效果:** 达到的效果：该协议将复杂度从$O(mn^2)$降低至与$n$和$m$成线性关系，显著提升了效率。
>
> **技术梗概:** 技术梗概：通过优化多方计算机制，实现了私有电路的高效安全评估。

---
### [2026/929] On the Statistical vs. Computational Security of the DKLs23 Multiparty ECDSA Protocol

- **作者:** Gil Segev

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/929) | [PDF](https://eprint.iacr.org/2026/929.pdf)


> **研究背景:** DLKs23协议是目前最先进的多方ECDSA签名协议，因其简洁性、高效性和在优雅的混合模型中的统计UC安全性而被广泛采用。
>
> **主要贡献:** 研究揭示了该协议并非如最初所声称的那样具有统计安全性，并提出了使其具备计算安全性的方法；同时证明了其基于特定假设下的计算安全性。
>
> **达到效果:** 通过分析，展示了存在一种攻击方式可导致多个诚实参与者在相同消息上生成不同的有效签名，从而确认DLKs23不具统计安全性；但证明了该协议在满足一定假设条件下具有计算安全性。
>
> **技术梗概:** 研究采用了一种“分裂视图”对手模型来构造攻击，并通过补充分析进一步证明了其计算安全性的理论基础。

---
### [2026/930] Improved Quantum Attacks on Iterated Even-Mansour Ciphers with Classical Queries

- **作者:** Mathieu Degré, Alisée Lafontaine, Aurel Pichollet--Mugnier, André Schrottenloher

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/930) | [PDF](https://eprint.iacr.org/2026/930.pdf)


> **研究背景:** Even-Mansour 密码构造在单轮情况下量子安全性已得到验证，但在多轮情况下的研究较少。
>
> **主要贡献:** 作者首次提出了针对两密钥迭代 Even-Mansour 密码的量子攻击方法，并改进了经典穷举密钥搜索的方法。
>
> **达到效果:** 对于4轮和6轮的情况，新提出的攻击分别达到了量子时间复杂度 $2^{7n/9}$ 和 $2^{n} / \sqrt{\log n}$，显著优于经典穷举搜索。
>
> **技术梗概:** 研究采用了碰撞搜索技术和基于多桥攻击的量子行走方法，并对经典的多碰撞攻击进行了量子化改进。

---
### [2026/931] Fair Multiparty Coin Tossing from Minimal Assumptions

- **作者:** Marshall Ball, Miranda Christ, Yevgeniy Dodis, Rachit Garg

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/931) | [PDF](https://eprint.iacr.org/2026/931.pdf)


> **研究背景:** 研究背景：多方诚实多数条件下公平硬币投掷是密码学中的基本原语，但其需求缺乏清晰的定义。此前的工作已经证明了公平硬币投掷与延迟函数之间的下界关系，但在已知的上界协议中存在显著差距，这些协议依赖于无法在明文模型中实例化的假设。
>
> **主要贡献:** 主要贡献：本文填补了这一空白，展示了在至多$n-1$个恶意方的情形下，公平$n$方硬币投掷可以从延迟函数这一最小假设中推导出来，从而完成了两者之间的等价性证明。
>
> **达到效果:** 达到的效果：通过这一结果，研究者们现在可以基于延迟函数来构建所有可能的公平多方硬币投掷协议，这为该领域的实际应用提供了理论基础。
>
> **技术梗概:** 技术梗概：本文采用了一种新颖的方法，将已知的延迟函数与公平硬币投掷之间的关系进行了形式化证明，并通过一系列复杂的数学推导和论证来实现这一目标。

---
### [2026/934] First-Order Masked Fine-Shuffling Implementation Against Side-Channel Attacks with Application to ML-KEM

- **作者:** Noura Ait Manssour, Souhayl Ben El Haj Soulami, Sylvain Duquesne, Guillaume Fumaroli

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/934) | [PDF](https://eprint.iacr.org/2026/934.pdf)


> **研究背景:** 针对细乱序操作中基本实现的条件交换掩码易受模板攻击的问题，本文提出了一种新的掩码细乱序方案，旨在提高Numeric theoretic Transform (NTT)的安全性。
>
> **主要贡献:** 作者通过聚合16个位级AND操作产生的泄漏信息，成功破解了原有的比特级细乱序实现，并提出了一个保护细乱序操作的新型掩码细乱序变体。
>
> **达到效果:** 新方案在探针模型下证明对第一阶攻击具有安全性，并且与之前被攻破的比特级细乱序相比，在ARM-Cortex-M4处理器上实现了整个ML-KEM768解封装算法25%的整体开销，降低了51%。
>
> **技术梗概:** 通过掩码秘密依赖性内存访问并将其交换掩码应用于布尔共享之上，本文提出的技术能够有效对抗第一阶侧信道攻击。

---
### [2026/937] Pseudonymization and reporters’ protection by design in the EU whistleblower directive

- **作者:** Mirosław Kutyłowski, Gabriel Wechta

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/937) | [PDF](https://eprint.iacr.org/2026/937.pdf)


> **研究背景:** 欧盟举报人指令旨在为报告违反欧盟法律的行为者提供保护，但与GDPR不同，该指令主要基于信任假设而非隐私和安全设计的概念。
>
> **主要贡献:** 作者分析了伪onym化在GDPR中的作用及其在德国和波兰等国法律中的体现，并指出当前法律未能充分利用伪onym化带来的机会，未建立清晰的法律框架以转化为技术要求。
>
> **达到效果:** 研究揭示了现有法律体系中对伪onym化的不足之处，强调需要进一步完善相关法律法规和技术标准。
>
> **技术梗概:** 通过对比GDPR和欧盟举报人指令中的隐私保护措施，并分析具体国家法律实施情况来评估伪onym化工具的有效性。

---
### [2026/940] Efficiently deciding and recovering CCZ and EA equivalence for arbitrary vectorial Boolean functions using the partition refinement framework

- **作者:** Nikolay Kaleyski, Joakim Sunde

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/940) | [PDF](https://eprint.iacr.org/2026/940.pdf)


> **研究背景:** 本文提出了一种基于分区细化框架的算法，用于测试和恢复任意向量布尔函数之间的CCZ和EA等价性。
>
> **主要贡献:** 该方法可以应用于任何函数对，无论其代数度、像集大小及其他属性，并且在时间和内存性能上优于现有所有算法。
>
> **达到效果:** 实验结果表明，该算法能够高效地计算函数的自同构群。
>
> **技术梗概:** 通过利用分区细化框架，该算法能够在不依赖于特定属性的情况下处理任意向量布尔函数之间的等价性问题。

---
### [2026/941] MAYA: A Short Shuffle Argument With Fast Verification

- **作者:** Thi Van Thao Doan, Olivier Pereira, Thomas Peters

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/941) | [PDF](https://eprint.iacr.org/2026/941.pdf)


> **研究背景:** 现有的混排证明方案在大规模密文混排时，其通信复杂度和验证时间随着密文数量线性增长，导致审计数据量庞大且验证耗时较长。
>
> **主要贡献:** MAYA提出了一种基于分组折叠的混排论证方案，实现了对数级的通信复杂度，并具备透明设置无需信任参数的特点。
>
> **达到效果:** 实验结果表明，对于10^6个密文，MAYA生成的证明长度仅为Verificatum的0.002%，验证时间减少至其12%。
>
> **技术梗概:** MAYA通过利用简洁论证和分组折叠技术，支持任意数量密文的同时保持操作混排部署使用的聚合结构。

---

## 更新: 2026-05-12 19:41

*新增 34 篇论文 (编号 878--916)*

### [推荐] [2026/886] From NIZK Arguments to ZAPs, Generically

- **匹配关键字:** LWE

- **作者:** Anish Banerjee, Brent Waters, David J. Wu

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/886) | [PDF](https://eprint.iacr.org/2026/886.pdf)


> **研究背景:** Dwork和Naor提出了从统计性声请假随机论证(NIZK)到零知识证明(ZAP)的通用转换方法。近年来，多项工作展示了如何在公共随机字符串模型下从多种假设（如DDH或LWE）中构建NIZK论证，但将这些NIZK论证转化为ZAP的过程较为复杂。
>
> **主要贡献:** 作者引入了有时约束生成器的概念，并提出了一种通用方法，可以使用该方法将任何计算性或统计性的NIZK论证在公共随机字符串模型下转换为相应的ZAP论证。
>
> **达到效果:** 通过这种方法，可以从DDH或LWE假设中直接恢复ZAP构造，同时也能支持不同组合的加密假设的新构建，这些假设之前是不可达的。
>
> **技术梗概:** 该工作提出了有时约束生成器的概念，并展示了如何利用这种生成器将NIZK论证转换为ZAP论证，从而提供了一种通用机制来增强证明系统的零知识性和声请假随机性。

---
### [推荐] [2026/889] RingSLIP: Ring Signatures from the Lattice Isomorphism Problem

- **匹配关键字:** lattice, post-quantum, LWE

- **作者:** Callum London, Daniel Gardham, Constantin Catalin Dragan

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/889) | [PDF](https://eprint.iacr.org/2026/889.pdf)


> **研究背景:** 环签名提供了一种在一组由签名人定义的公钥中匿名认证消息的方法，广泛应用于加密货币、电子投票和并发签名领域。然而，后量子构造通常依赖于格理论，特别是利用Learning with Errors (LWE) 和 Short-Integer-Solution (SIS) 问题，这导致了与经典构造相比的效率低下。
>
> **主要贡献:** 本文提出了基于Lattice Isomorphism Problem (LIP) 的RingSLIP环签名方案，结合HAWK签名机制，实现了在环成员数量对数级大小的签名，并且具有在线/离线计算特性，显著提高了性能和安全性。
>
> **达到效果:** RingSLIP 签名方案在4096个环成员的情况下，具体实现大小为46KB，达到了128位的安全性要求，与其它基于格的方案相比具有竞争力，并且支持在线/离线计算特性。
>
> **技术梗概:** 该技术通过利用LIP和HAWK签名机制，在保持匿名性和可链接性的前提下，实现了高效的环签名构造，并通过优化解码过程提高了性能。

---
### [推荐] [2026/890] Cryptanalysis of Definite and Indefinite Lattice Isomorphism Problems With Applications to HAWK and DEFI

- **匹配关键字:** lattice

- **作者:** Markus Kirschmer, Cong Ling, Ali Sadreddin

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/890) | [PDF](https://eprint.iacr.org/2026/890.pdf)


> **研究背景:** 研究了不定和定二次型的格同构问题，并将其应用于分析基于等向二次形式的签名方案DEFI和HAWK。
>
> **主要贡献:** 提出了结合算术与算法技术的有效攻击方法，特别针对高维不定二次形式的决策/区分-格同构问题。
>
> **达到效果:** 成功攻破了基于等向二次形式的高效数字签名方案DEFIv2，并展示了经典多项式时间算法和量子多项式时间算法的应用效果。
>
> **技术梗概:** 通过利用二次型的算术理论，特别是在高维不定二次形式上，实现了对DEFI的结构坍缩分析。

---
### [推荐] [2026/895] On the Properties of HighBits and LowBits Functions and their Applications

- **匹配关键字:** lattice

- **作者:** Alice Pellet-Mary, Michel Seck

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/895) | [PDF](https://eprint.iacr.org/2026/895.pdf)


> **研究背景:** ML-DSA是一种基于格的签名方案，已被NIST标准化为FIPS 204。其中涉及高位和低位函数，用于处理整数的部分位信息。
>
> **主要贡献:** 研究证明了Seck和Roux-Langlois关于高位函数性质的猜想，并完全描述了误差项的行为。
>
> **达到效果:** 通过这些理论成果，可以设计出具有高级特性的基于格的签名方案。
>
> **技术梗概:** 利用数学分析方法验证了高位函数的加法性质，并详细研究了其误差项的可能性取值。

---
### [推荐] [2026/896] CORAL Faster Isogeny Group Action for Post-Quantum NIKE

- **匹配关键字:** post-quantum

- **作者:** Andrea Basso, Giacomo Borin, Ryan Rueger, Sina Schaeffler

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/896) | [PDF](https://eprint.iacr.org/2026/896.pdf)


> **研究背景:** 研究背景：CORAL算法旨在通过牺牲通用性来提高效率，以实现更快速的有限群作用评估。
>
> **主要贡献:** 主要贡献在于提出了一种新的、更快的有限群作用算法CORAL，能够比现有方法更高效地执行与(qt-)PEGASIS相同的操作。
>
> **达到效果:** 达到的效果是实现了2032位素数下仅需240毫秒就能完成群作用评估，并构建了一个具有紧凑公钥（例如256字节）的后量子非交互式密钥交换系统。
>
> **技术梗概:** 技术梗概：CORAL通过计算二维$2$-isogenies来实现有限群作用，从而在不牺牲安全性的前提下显著提高了效率。

---
### [推荐] [2026/901] Threshold (T)FHE without smudging by means of correct threshold additive HE

- **匹配关键字:** lattice, homomorphic encryption, LWE

- **作者:** Antonina Bondarchuk, Renaud Sirdey, Aymen Boudguiga, Olive Chakraborty

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/901) | [PDF](https://eprint.iacr.org/2026/901.pdf)


> **研究背景:** 设计基于门限的LWE同态加密方案面临挑战，主要是由于分布式解密过程中可能出现的噪声泄漏问题。主流方法是使用噪声泛滥或模糊技术来避免这一问题，但这些方法会增加参数大小并限制了较小模数方案的应用。
>
> **主要贡献:** 本文提出了一种新的门限LWE同态加密方案thPLWE，通过结合正确线性同态加密（LHE）和门限变异的Paillier方案来避免噪声模糊技术的使用，从而减少参数大小并提高安全性。
>
> **达到效果:** 实验结果表明，该方法在静态篡改和适应查询下是IND-CPA安全的，并且与现有工作相比具有更高的实用性。
>
> **技术梗概:** 通过将门限变异的Paillier方案用于加密LWE对中的b项，并结合同态计算后的去噪处理来实现噪声泄漏问题的解决，从而设计出无需模糊技术的门限同态加密方案。

---
### [推荐] [2026/903] Magic Pot: Cryptanalysis of full AIM2 in the standard and related-/reused-key settings using new elimination framework

- **匹配关键字:** post-quantum

- **作者:** Alex Biryukov, Pablo García Fernández, Aleksei Udovenko

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/903) | [PDF](https://eprint.iacr.org/2026/903.pdf)


> **研究背景:** 本文针对后量子签名方案AIMer v2.1进行密码分析，该方案是Korean Post-Quantum Cryptography竞赛的获胜者之一，并且其早期版本曾是美国NIST后量子数字签名征集活动中的候选方案。
>
> **主要贡献:** 作者开发并应用了一种新的代数攻击框架，基于扩展线性化和一个新颖的多项式矩阵零向量查找算法，揭示了AIM2的安全性不足。
>
> **达到效果:** 在误用场景下，如重密钥或相关密钥设置中，提出的攻击变得可行，允许实验验证并进行基准测试。此外，作者还评估了该方法对Rainier方案中的RAIN分组密码，并获得了改进的攻击结果。
>
> **技术梗概:** 通过扩展线性化和多项式矩阵零向量查找算法构建了一种新的代数攻击框架。

---
### [推荐] [2026/909] On Succinct Non-Interactive Secure Computation with Malicious Security

- **匹配关键字:** homomorphic encryption

- **作者:** Maya Farber Brodsky, Arka Rai Choudhuri, Abhishek Jain, Omer Paneth

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/909) | [PDF](https://eprint.iacr.org/2026/909.pdf)


> **研究背景:** 研究背景：非交互式安全计算(NISC)协议允许客户端和服务器分别输入$x$和$y$，通过单向通信完成函数$f(x,y)$的计算。在半诚实模型下，已知从全同态加密(FHE)可以实现简洁型NISC；然而，在恶意模型下的简洁型NISC仅基于非标准假设如SNARKs for NP。
>
> **主要贡献:** 主要贡献：本文提出了首个基于标准假设（FHE和批验证论证BARGs）的恶意安全简洁型NISC协议，适用于多种自然功能，包括私有集合成员资格、字典查找及其可验证版本和UP搜索问题。
>
> **达到效果:** 达到的效果：所提出的协议在恶意服务器模型下实现了分拆模拟安全性，并且输出大小仅依赖于计算结果而与输入数据无关或复杂度无关。
>
> **技术梗概:** 技术梗概：通过结合FHE和批验证论证BARGs，设计了针对多种功能的高效简洁型NISC协议，确保在恶意服务器攻击下仍能正确执行计算任务。

---
### [推荐] [2026/911] UC4Free! Existing Threshold Signatures are UC Secure

- **匹配关键字:** post-quantum

- **作者:** Jan Bobolz, Elizabeth Crites, Markulf Kohlweiss, Akira Takahashi

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/911) | [PDF](https://eprint.iacr.org/2026/911.pdf)


> **研究背景:** 近年来，阈值签名由于标准化努力和实际系统中的部署而受到广泛关注。本文旨在证明多种现有阈值签名方案在通用组成性方面的安全性。
>
> **主要贡献:** 作者设计了自然的游戏化定义来捕捉不同组合的主要阈值签名属性，并且这些定义扩展并涵盖了先前的工作，如Bellare等人（CRYPTO'22），同时识别并解决了前人工作中的不足。
>
> **达到效果:** 通过上述方法，作者证明了一个阈值签名方案等同于实现UC理想功能$\mathcal{F}\text{-}\mathtt{TS3}$，从而使得现有方案能够在通用组成性环境中使用。
>
> **技术梗概:** 研究采用了游戏化定义和理想功能表达方式来描述属性，并通过形式化方法证明了其等价性。

---
### [推荐] [2026/912] Improved TensorPIR: Single-Server PIR with Lower Communication Cost

- **匹配关键字:** lattice

- **作者:** Yingchu Lv, Yanbin Pan, Huaxiong Wang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/912) | [PDF](https://eprint.iacr.org/2026/912.pdf)


> **研究背景:** Private Information Retrieval (PIR)技术在隐私保护的数据访问中日益重要，它允许用户从数据库中检索信息而不泄露查询内容，符合现代数据保护和监管标准。
>
> **主要贡献:** 本文提出了一种新的框架，重新思考索引的加密策略，通过减少CRT模数的数量来降低通信和计算成本。
>
> **达到效果:** 实验表明，在16 GB至128 GB的不同数据库规模下，总通信成本降至TensorPIR的45.5%，理论上随着数据量的增长，查询和答案大小分别减少了36.9%和22.2%。
>
> **技术梗概:** 该方案通过优化CRT模数的数量来减少通信和计算成本，并在大规模数据检索中实现了比HintlessPIR更低的实际通信开销。

---
### [推荐] [2026/914] Post-Quantum Authenticated Key Exchange via Signcryption with Ephemeral Key Masking

- **匹配关键字:** post-quantum, LWE

- **作者:** Mostefa Kara, Konstantinos Karampidis, Muath AlShaikh

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/914) | [PDF](https://eprint.iacr.org/2026/914.pdf)


> **研究背景:** 该研究针对后量子计算环境下的安全通信需求，提出了一种基于PQES方案的新型双向认证密钥交换协议。
>
> **主要贡献:** 贡献在于设计并实现了PQES-AKE协议，该协议通过在签加密算法内部生成的随机性中隐藏临时Diffie-Hellman密钥来实现会话密钥保密性和前向安全性。
>
> **达到效果:** 实验结果显示，PQES-AKE协议能够在两个网络往返周期内完成，并且通信成本和计算开销均保持在合理范围内，验证了其作为后量子安全信道建立的单原语替代方案的有效性。
>
> **技术梗概:** 技术上采用了基于LWE、SBDE假设和CDH问题的安全机制来确保协议的安全性，并通过Python原型实现了该协议以评估其实现效果。

---
### [推荐] [2026/915] Execution-time and microarchitectural profiling of RustCrypto and PQClean ML-KEM/ML-DSA implementations under Linux cgroup resource constraints

- **匹配关键字:** post-quantum

- **作者:** Akram Bensebaa

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/915) | [PDF](https://eprint.iacr.org/2026/915.pdf)


> **研究背景:** 现有对后量子密码学（PQC）算法的基准测试主要关注硬件上的原始吞吐量或延迟，而未考虑不同资源限制下实现选择对其微架构行为的影响。
>
> **主要贡献:** 本文通过在三个cgroups强制执行配置（0.5个CPU、1.0个CPU和无约束）下对RustCrypto和PQClean的ML-KEM-768和ML-DSA-65实现进行分析，填补了这一空白。
>
> **达到效果:** 结果表明，在严重限制为0.5个CPU的情况下，评估的Rust配置在ML-KEM（+42.4%）和ML-DSA（+47.8%）上表现出更高的延迟开销。Massif跟踪记录显示所有额外的堆使用都归因于运行时初始化，而在测量的加密核心执行路径中没有观察到动态分配。
>
> **技术梗概:** 我们利用稳健的非参数统计方法（中位数和四分位距）来减少调度器引起的定时变化的影响，并通过火焰图分析采样执行热点。

---
### [2026/878] Verifiable Anomaly and Similarity Detection Using Matrix Profile in Private Time-series

- **作者:** Xavier Bultel, Charlène Jojon, Benjamin Nguyen, Haoying Zhang

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/878) | [PDF](https://eprint.iacr.org/2026/878.pdf)


> **研究背景:** 在保护隐私的前提下分析时间序列数据库变得尤为重要，尤其是在涉及敏感个人信息（如医疗记录或时空轨迹数据）的情况下。
>
> **主要贡献:** 本文提出了一种工具包，用于证明私有时间序列中是否存在异常或相似性，并利用Matrix Profile进行子序列级别的检测而非仅针对完整的时间序列。
>
> **达到效果:** 该方法通过结合承诺和零知识证明系统确保了结果的有效性和时间序列的无条件保护，即使在大规模实时数据情况下也能保持合理的执行速度。
>
> **技术梗概:** 本文采用了Matrix Profile技术来检测时间序列中的子序列异常和相似性，并通过承诺和零知识证明系统保证隐私安全。

---
### [2026/880] On the Common Bias of Majorities: Poly-Time Attacks on THR-XOR PRGs

- **作者:** Antonio Giulio D’Antona, Pierrick Méaux, Akin Ünal

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/880) | [PDF](https://eprint.iacr.org/2026/880.pdf)


> **研究背景:** 基于Threshold-XOR谓词的伪随机生成器（PRG）因其浅层性和高效性，在多方计算协议中受到广泛关注。
>
> **主要贡献:** 作者提出了针对此类PRG的新颖快速攻击方法，显著提高了攻击效率。
>
> **达到效果:** 这些攻击成功破解了多个参数设置，并证明在特定条件下实现了多项式时间内的显著优势。
>
> **技术梗概:** 通过分析谓词的共同偏差，设计了一种基于概率的方法来加速攻击过程。

---
### [2026/881] Unique SNARGs with Adaptive Security: Constructions and Black-Box Separations

- **作者:** Cody Freitag, Daniel Wichs

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/881) | [PDF](https://eprint.iacr.org/2026/881.pdf)


> **研究背景:** 研究背景：Succinct non-interactive arguments (SNARGs) 允许证明者以远短于原始NP证据的证明来高效地使验证者相信一个NP语句的真实性。然而，Gentry和Wichs指出，对于适应性安全的SNARGs，无法通过任何可证伪假设的黑盒归约进行证明。
>
> **主要贡献:** 主要贡献：作者探讨了唯一SNARGs（每个陈述最多只有一个接受证明）在适应性安全性方面的可能性，并提供了完美唯一且适应性安全的SNARGs 构造，基于亚指数难解单向函数和不可区分混淆。
>
> **达到效果:** 达到的效果：通过黑盒分离展示了对于完美完整且唯一的SNARGs 无法仅依赖于亚指数难度假设和长公共参考字符串实现适应性安全性。同时提供了实际构造，并证明了其安全性和有效性。
>
> **技术梗概:** 技术梗概：作者通过放松完美完整性并允许微小的不完全性来克服现有限制，进而实现了所需的安全特性。

---
### [2026/882] Abuse Reporting and Enforcement for Third-Party Moderators in Private Messaging

- **作者:** Matthew Gregoire, Jade Keegan, Saba Eskandarian

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/882) | [PDF](https://eprint.iacr.org/2026/882.pdf)


> **研究背景:** 该研究旨在解决私有即时通讯平台中第三方调解员对滥用信息的举报和执行问题，特别是在平台不希望参与或承担责任的情况下。
>
> **主要贡献:** 作者提出了一种轻量级的凭证发放与撤销机制，无需平台介入即可支持调解员验证举报并执行决策。
>
> **达到效果:** 该方法显著降低了调解员验证举报所需的计算和通信成本，分别减少了6倍和7倍。
>
> **技术梗概:** 研究基于非对称消息封缄技术，并在此基础上进行了性能优化，提高了系统的效率。

---
### [2026/883] Secure Two-Party Quantum Computation with Complete Fairness without Trusted Third Party

- **作者:** Arpita Maitra, Goutam Paul, Asim K. Pal, Asmita Samanta, Hridam Basu

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/883) | [PDF](https://eprint.iacr.org/2026/883.pdf)


> **研究背景:** 在1997年，Lo证明了如果一方是恶意的，则无法实现量子比特承诺的安全性，从而影响两方量子计算的安全性。尽管通过假设存在一个对任何多项式时间量子对手都安全的一次函数置换可以实现安全的量子比特承诺方案，但完全公平性在实际框架下的量子两方计算中仍然是一个问题。
>
> **主要贡献:** 本文首次展示了对于某些函数，在假设计算能力受限的对手下，可以在量子领域内实现具有完全公平性的安全两方量子计算。
>
> **达到效果:** 通过使用Gordon等人提出的混合模型思想和非同时信道，以及Canetti关于多方计算组合的思想，本文在量子环境中实现了完全公平性。
>
> **技术梗概:** 本文采用了一种基于假设计算能力受限对手的策略，并结合了混合模型和非同时通信的概念来实现量子环境下的完全公平性。

---
### [2026/884] Formalizing and Strengthening the Security Proof of NTOR

- **作者:** François Dupressoir, Kristian Gjøsteen, Cameron Low, Charlotte Mylog

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/884) | [PDF](https://eprint.iacr.org/2026/884.pdf)


> **研究背景:** 本文旨在为NTOR密钥交换协议提供形式化的安全证明，该协议用于建立Tor洋葱路由系统中的连接。此前的研究未能充分考虑前向安全性。
>
> **主要贡献:** 贡献在于使用EasyCrypt全面形式化了NTOR的安全性证明，并提出了一种处理涉及执行全局属性的失败事件的中断归约方法。
>
> **达到效果:** 通过这种方法，作者证明了NTOR在一种新的单方认证密钥交换模型中是安全的，该模型能够捕捉前向安全性，并且与现有的双边AKE模型（如eCK）保持接近。
>
> **技术梗概:** 技术上，作者改进了EasyCrypt框架，并提出了一个新模型来处理身份和公钥在密钥交换协议中的使用方式，从而简化了形式化论证并引入了几种UAKE安全模型的变体。

---
### [2026/885] Optimized Final Exponentiation for Optimal Ate Pairings Using Cyclotomic Cubing

- **作者:** Leila Ben Abdelghani, Walid Haddaji

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/885) | [PDF](https://eprint.iacr.org/2026/885.pdf)


> **研究背景:** 在基于配对的密码学中，最终幂运算步骤是计算双线性配对中最耗时的部分。
>
> **主要贡献:** 作者提出了一种在SG54曲线和BLS15、BLS27曲线上优化最终幂运算的方法。
>
> **达到效果:** 该方法分别在SG54、BLS15和BLS27曲线上实现了24%和22%的效率提升。
>
> **技术梗概:** 通过利用现有的结果来计算弗罗贝尼乌斯映射，并引入了新的最终幂运算硬部分分解，作者优化了配对计算。

---
### [2026/888] BlindReview: Anonymous and End-to-End Verifiable Peer Review

- **作者:** Xavier Bultel, Ashley Fraser, Elizabeth A. Quaglia

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/888) | [PDF](https://eprint.iacr.org/2026/888.pdf)


> **研究背景:** BlindReview旨在解决学术同行评审过程中存在的隐私泄露和透明度不足的问题，通过加密技术确保评审过程的匿名性和可审计性。
>
> **主要贡献:** 该研究正式定义了系统的安全属性，并通过严格的证明展示了BlindReview满足这些要求，为建立可验证且保护隐私的同行评审系统奠定了基础。
>
> **达到效果:** BlindReview实现了评审过程中的匿名提交和透明验证，增强了学术评审的公正性和可信度。
>
> **技术梗概:** 该系统采用加密技术确保匿名性，并通过零知识证明等方法实现评审结果的可审计性。

---
### [2026/891] Interleaving Stability for Mutual Correlated Agreement and Curve Decodability

- **作者:** Sunghyeon Jo

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/891) | [PDF](https://eprint.iacr.org/2026/891.pdf)


> **研究背景:** 本文研究了行间插编对两种编码理论稳健性属性——生成器互相关协议（Generator Mutual Correlated Agreement, G-MCA）和曲线可解码性（Curve Decodability）的影响，旨在解决这些属性在行间插编下的线性损失问题。
>
> **主要贡献:** 作者证明了对于特定的系数生成器和距离参数，在任何行间插编宽度下，G-MCA的误差率保持不变或仅轻微增加，并引入了一种标记形式来确保曲线可解码性的稳定性。
>
> **达到效果:** 研究结果表明，线性行间插编不会对G-MCA产生线性损失，对于特定条件下的代码，行间插编前后曲线可解码性保持一致。
>
> **技术梗概:** 通过数学证明和引入标记形式定义，作者展示了如何在保持编码理论稳健性的同时进行行间插编操作。

---
### [2026/897] SEFA: A Secure, Efficient, and Flexible Algorithm Design Strategy for Block Ciphers and Sponge Permutations

- **作者:** Gökçe Düzyol, Nida Fidan, Kamil Otal

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/897) | [PDF](https://eprint.iacr.org/2026/897.pdf)


> **研究背景:** SPNs作为块密码和Sponge置换的主流构建方法，通常被划分为字节级与位级扩散两种类型。本文旨在结合这两种方式，提出一种更高效、更具灵活性的设计策略。
>
> **主要贡献:** 作者提出了SEFA算法家族，包括多种轻量级且灵活的块密码、AEAD和哈希函数，展示了其在安全性及性能上的优势。
>
> **达到效果:** 通过设计具有4比特S-box、16轮结构的SEFA-128/256；采用8比特S-box、10或16轮结构的SEFA-512/256；以及使用1536比特状态置换、含8比特S-box和12轮结构的SEFA-1536，实现了高效灵活的设计。
>
> **技术梗概:** 结合字节级与位级扩散特性，采用小尺寸S-box、仅包含XOR运算及位移操作的线性层，并通过减少轮数来优化设计。

---
### [2026/898] Bluestreak: Scaling DAG BFT by Sparsifying Metadata

- **作者:** Nikita Polianskii, Ilya Vorobyev, Sebastian Muller

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/898) | [PDF](https://eprint.iacr.org/2026/898.pdf)


> **研究背景:** 现有的DAG基BFT共识协议通过允许多个验证者并发提议来实现高吞吐量，但在大型委员会中仍面临扩展挑战。
>
> **主要贡献:** Bluestreak提出了一种稀疏的非认证DAG BFT共识协议，该协议在扩大委员会规模时保持非领导者块的大小恒定，并将委员会级别的祖先集中在每个回合的一个领导者的块中。
>
> **达到效果:** 通过这种设计，Bluestreak实现了随着委员会的增长平均元数据每块保持常数，在广泛区域延迟下，从10到400个验证者在商用4-CPU实例上均能保持亚秒级的网络延迟。
>
> **技术梗概:** Bluestreak结合了稀疏块格式、新的领导者提交规则以及基于拉取的新节拍器，并使用仅碰撞抗原函数和标准数字签名证明其安全性和活性。

---
### [2026/899] VCVio: Verified Cryptography in Lean via Oracle Effects and Handlers

- **作者:** Devon Tuma, Quang Dao, James Waters, Alexander Hicks, Nicholas Hopper

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/899) | [PDF](https://eprint.iacr.org/2026/899.pdf)


> **研究背景:** 现有的形式化证明框架在确保性和表达性之间存在长期权衡，难以处理现代密码学中常见的预言机操作和回滚论证。
>
> **主要贡献:** VCVio引入了Lean 4中的代数效果和处理器来建模预言机交互，并结合模块化的关系程序逻辑增强了战术基础设施。
>
> **达到效果:** 该框架实现了预言机访问计算的自由单调，通过缓存、日志记录、重新编程和种子预采样等处理器组合提升了灵活性；并通过扩展Loom框架支持了一致性的概率推理。
>
> **技术梗概:** VCVio利用代数效果和处理器来表示预言机交互历史，并将其作为显式语法树暴露出来，简化了回滚操作为确定性传输重放。

---
### [2026/900] Secure Protocol Composition under Dynamic Corruption: Scaling Up Symbolic Analysis for Real-World Security Properties

- **作者:** Cas Cremers, Erik Pallas, Aleksi Peltonen

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/900) | [PDF](https://eprint.iacr.org/2026/900.pdf)


> **研究背景:** 现有的自动符号协议验证方法在处理复杂协议时开始遇到限制，而组合验证虽然被提出作为解决方案，但通常依赖于不切实际的协议假设。
>
> **主要贡献:** 本文提出了一个适用于现代安全属性的组合符号分析结果，在动态攻击者存在的情况下仍然有效，前提是协议满足分离性要求。
>
> **达到效果:** 该方法在数据交换协议与Diffie-Hellman密钥交换的组合分析中取得了成功，并且在TLS 1.3及其ECH扩展的组合分析中验证了前向保密属性。
>
> **技术梗概:** 通过开发应用于π-演算的实际组合结果，本文提出了一种新的分析技术来支持现实世界的安全协议。

---
### [2026/902] End-to-End Polynomial-Time Cryptanalytic Extraction of Convolutional Neural Networks in the Hard-Label Setting

- **作者:** Chun Li, Zheng Gong, Di Li, Liping Zhuang, Yufeng Tang, Yin Lv, Xingfu Yan

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/902) | [PDF](https://eprint.iacr.org/2026/902.pdf)


> **研究背景:** 针对卷积神经网络(CNN)参数作为知识产权的保护问题，现有API仅提供最高概率标签而隐藏底层逻辑，攻击者难以直接恢复模型参数。
>
> **主要贡献:** 提出了一种端到端的硬标签提取攻击方法，适用于已知架构的ReLU CNN分类器，并在平均池化情况下有效。
>
> **达到效果:** 该方法能够实现100%预测准确率，并揭示了隐藏标签并不能完全保护模型参数的事实，即使在拥有网络结构信息的情况下。
>
> **技术梗概:** 通过SVGR引导保留候选离散优化算法，在通道级别恢复共享通道签名并解决通道符号问题，逐层剥离以吸收ReLU缩放因子到后续线性层中。

---
### [2026/904] Sponsored Fair Exchange (Extended Abstract)

- **作者:** Serge Vaudenay

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/904) | [PDF](https://eprint.iacr.org/2026/904.pdf)


> **研究背景:** 本文提出了一种基于智能合约的无成本公平交换平台，旨在促进经济包容性。
>
> **主要贡献:** 贡献在于设计了一个低成本的知识币交换协议，并引入了赞助机制以降低交易成本。
>
> **达到效果:** 该协议确保在取消交易时双方均不受损失，在完成交易时则有预设费用，同时保持交易隐私。
>
> **技术梗概:** 技术上采用自动可验证描述的数字物品进行交换，且智能合约大部分通信发生在链下，复杂度优化至最坏情况下为对数级。

---
### [2026/905] Maintaining Sublinear Locality Over Time: Adaptively Secure MPC on a Reusable Hidden Graph

- **作者:** Elette Boyle, Ran Cohen, Pierre Meyer

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/905) | [PDF](https://eprint.iacr.org/2026/905.pdf)


> **研究背景:** 在适应性故障对手环境下，实现同时具有亚线性通信局部性和自适应安全性的多方计算（MPC）似乎几乎是不可能的。
>
> **主要贡献:** 本文提出了两种设置下的解决方案：一种是针对半诚实对手和信息论安全性，另一种是针对失败停止对手和计算安全性，并分别实现了多项式对数和近似三次根级别的亚线性通信局部性。
>
> **达到效果:** 通过这些方案，成功地在面对适应性对手的情况下，维护了多次MPC执行过程中的亚线性通信局部性。
>
> **技术梗概:** 本文采用了一种可重用的隐藏图模型，在每一轮中使用一个新的初始隐藏低度图，并结合不同轮次的图以增加总通信度，从而实现亚线性通信局部性和自适应安全性。

---
### [2026/906] An analysis of a weakened version of PRISM

- **作者:** Jolijn Cottaar, Steven D. Galbraith, Luciano Maino, Monika Trimoska

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/906) | [PDF](https://eprint.iacr.org/2026/906.pdf)


> **研究背景:** PRISM是一种基于计算大素因子度数超曲线上伊瑟吉亚的签名方案的安全性分析，该研究探讨了弱质数检验对PRISM安全性的影响。
>
> **主要贡献:** 作者展示了使用弱质数测试时，标准模型下的安全证明假设不成立，并进一步分析了量子随机预言机模型下所需的Miller-Rabin测试迭代次数以确保安全级别。
>
> **达到效果:** 通过调整质数测试方法和估计所需迭代次数，研究降低了签名成本并提高了PRISM的安全性。
>
> **技术梗概:** 研究采用了形式化的方法来验证假设的有效性，并使用概率算法来估算安全参数的值。

---
### [2026/907] Zero-Knowledge Proofs for Gradient Boosted Decision Trees

- **作者:** Jiacheng Gao, Wenjie Qu, Yuan Zhang, Sheng Zhong, Jiaheng Zhang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/907) | [PDF](https://eprint.iacr.org/2026/907.pdf)


> **研究背景:** 在金融、医疗和风险评估等领域中，梯度提升决策树（GBDT）是最有效的表格数据模型之一。随着这些模型越来越多地由外部提供商训练和服务，客户需要验证预测或模型更新是否由声称的训练管道产生，同时提供商可能希望保持训练数据和模型参数的秘密性。
>
> **主要贡献:** 	extsc{Terrae} 提出了一个基于 KZG 多项式承诺的量化 GBDT 训练和推理零知识证明系统，解决了现有构造中验证成本高和辅助见证者过多的问题。
>
> **达到效果:** 该系统能够高效地验证 GBDT 的训练和推理过程，同时保护敏感数据不被泄露，并且在证明大小和证明者时间上表现出色。
>
> **技术梗概:** 通过将证明分解为代数约束并利用 KZG 多项式承诺技术，	extsc{Terrae} 实现了高效的零知识证明，避免了高验证成本和大量独立辅助承诺带来的问题。

---
### [2026/908] Titan: Efficient Polynomial Commitments from IOPs over Groups

- **作者:** Chethan Kamath, Ravi Prakash, Samipa Samanta, Sruthi Sekar, Nitin Singh

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/908) | [PDF](https://eprint.iacr.org/2026/908.pdf)


> **研究背景:** 论文提出了一种高效的多项式承诺方案Titan，旨在提供比基于哈希的PCS更小的证明大小，并且相比现有组基方案如Dory和Hyrax具有更高的证明者和验证者的效率。
>
> **主要贡献:** Titan通过借鉴Dory中的两层承诺技术，并利用基于群体的交互接近度协议（IOPP）实现外层承诺，特别是使用WHIR代替昂贵的双线性对，从而实现了在通用曲线如Pasta Curves上的实例化。
>
> **达到效果:** Titan达到了$O(n)$的承诺时间、$O(\sqrt{n})$的评估时间和$O(\sqrt[4]{n})$的比例证明大小和验证规模。与现有方案相比，其证明大小减少了数量级，并且在电路大小$\geq 2^{22}$时实现了约3倍更高效的证明大小和验证。
>
> **技术梗概:** Titan采用了一种结合IOPP（交互接近度协议）和Pedersen风格的内层承诺的新方法，以高效实现WHIR IOPP在素数阶群上的实例化。

---
### [2026/910] UnifOMR: Oblivious Message Retrieval with Near-optimal Concrete Efficiency

- **作者:** Ben Fisch, Zeyu Liu, Eran Tromer, Yunhao Wang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/910) | [PDF](https://eprint.iacr.org/2026/910.pdf)


> **研究背景:** 研究背景：传统的端到端加密确保了消息的机密性，但未能隐藏发送者和接收者的通信模式或其身份等元数据。Oblivious Message Retrieval (OMR) 是一种能够使服务器在不学习消息与接收者之间映射关系的情况下帮助接收者检索其消息的密码学协议，从而保护这些元数据。
>
> **主要贡献:** 主要贡献：论文探讨了 OMR 与更成熟的 Private Information Retrieval (PIR) 原理之间的精确关系，并展示了如何通过将 PIR 的效率直接应用于 OMR 来实现近最优的实际效率。
>
> **达到效果:** 达到的效果：UnifOMR 实现了比 SophOMR 快 20 到 1080 倍的服务器运行时间，在实际参数设置下，对于每条 612 字节的消息总数为 $2^{19}$ 的情况，仅需约 25 秒完成，通信量约为 4 MB；而 SophOMR 需要超过 1250 秒和 260 KB 的通信。
>
> **技术梗概:** 技术梗概：UnifOMR 使用了一种称为强检测密钥不可链接性的属性，并通过将 PIR 的效率直接应用于 OMR 来实现高效性，同时引入了两轮交互以平衡性能与通信量。

---
### [2026/913] Algorithmic Toolkit for Linearization of S-boxes

- **作者:** Alex Biryukov, Philip Tureček, Aleksei Udovenko

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/913) | [PDF](https://eprint.iacr.org/2026/913.pdf)


> **研究背景:** 线性化是一种密码分析技术，用于将非线性函数（S盒）表示为特定输入子集上的仿射映射。尽管在Keccak、LowMC、RAIN和AIM等机制中已应用了其变体，但对任意大小的S盒进行线性化从未实际探索过，因为缺乏理论、算法和密码分析的理解。
>
> **主要贡献:** 首次开发了一套算法工具箱，能够计算出当存在时的最佳可能近似线性化。该工具箱适用于8位及以下的S盒，并能为更大的S盒提供良好的近似解及其上界。
>
> **达到效果:** 通过对多种现有的S盒、多项式函数以及16位超S盒的应用，获得了有趣的结果，提出了许多新的开放问题，并开辟了新的研究方向和攻击基础。
>
> **技术梗概:** 通过解决覆盖S盒的多个逼近问题来推进线性化的密码分析用途。开发了一种通用的方法来处理SPN基置换（Substitution-Permutation Networks）中具有一般线性层的CICO问题。

---
### [2026/916] Cryptanalysis of the Subfield Bilinear Collision Problem

- **作者:** Pierre Briaud, Romaric Neveu

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/916) | [PDF](https://eprint.iacr.org/2026/916.pdf)


> **研究背景:** Subfield Bilinear Collision (SBC)问题最初由Huth和Joux在Crypto 2024提出，用于构建MPC-in-the-Head签名方案，并在Asiacrypt 2025中被证明更高效地应用于VOLE-in-the-Head框架。
>
> **主要贡献:** 作者通过建立SBC问题与秩解码问题之间的联系，增强了其理论难度；分析了Gröbner基算法以解决SBC双线性系统，并提出了关于该系统的猜想；并使用矩阵最大余子式间的Plücker关系提供了另一种代数建模。
>
> **达到效果:** 这些改进为SBC问题的攻击范围和行为提供了更深入的理解，虽然并未直接威胁到基于SBC参数的安全性，但为进一步精确分析铺平了道路。
>
> **技术梗概:** 研究通过理论分析、Gröbner基算法应用以及代数建模等技术手段，对SBC问题进行了全面剖析。

---

## 更新: 2026-05-05 19:42

*新增 21 篇论文 (编号 844--865)*

### [推荐] [2026/845] Compressed FHE:  Accelerating Encrypted Matrix Multiplication in CKKS with Precision-Balanced Low-Rank Factor Chains

- **匹配关键字:** homomorphic encryption

- **作者:** Dimitrios Schoinianakis, Maryam Sabzevari

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/845) | [PDF](https://eprint.iacr.org/2026/845.pdf)


> **研究背景:** 该研究旨在通过引入压缩FHE（cFHE）框架，将低秩矩阵分解技术整合到CKKS同态加密方案中，以加速加密矩阵乘法并保持精度。
>
> **主要贡献:** 贡献在于提出了一个理论分析和实证方法相结合的框架，并推导出相对误差累积的理论边界，从而实现目标精度下的计算深度优化。
>
> **达到效果:** 实验结果表明，使用cFHE进行低秩加密矩阵乘法可以显著提高运行时性能并减小密文大小，同时保持所需的精度水平。
>
> **技术梗概:** 技术上通过建立精度平衡模型将低秩近似误差与密文噪声联系起来，并据此自动选择CKKS参数以优化计算精度和加密强度之间的关系。

---
### [推荐] [2026/846] A Survey on Security Reductions in Post-Quantum Cryptography

- **匹配关键字:** lattice, post-quantum

- **作者:** Thomas Attema, Ronald Cramer, Serge Fehr, Yu-Hsuan Huang, Bor de Kock, Jana Sotáková

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/846) | [PDF](https://eprint.iacr.org/2026/846.pdf)


> **研究背景:** 本文综述了后量子密码方案安全性的计算难题及其证明方法，特别是在量子计算机模型下的有效性问题。
>
> **主要贡献:** 文章概述了在设计和证明后量子密码方案安全性时遇到的挑战，并讨论了克服这些挑战所开发的一些数学技术。
>
> **达到效果:** 研究揭示了通用转换（如Fiat-Shamir和Fujisaki-Okamoto变换）以及具体加密方案（尤其是NIST标准化的方案）的安全性降低情况。
>
> **技术梗概:** 文章探讨了几种技术，包括量子难题的选择、安全证明方法及其在经典与量子计算环境下的差异。

---
### [推荐] [2026/847] Lattice Group Signatures, Revisited

- **匹配关键字:** lattice

- **作者:** Paul Delhom, Pierre-Alain Fouque, Corentin Jeudy, Olivier Sanders

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/847) | [PDF](https://eprint.iacr.org/2026/847.pdf)


> **研究背景:** 集团签名是一种重要的隐私保护认证机制，提供了问责制和匿名性之间的良好平衡。尽管已经有许多工作将Bellare、Micciancio和Warinschi提出的经典框架应用于基于格的设置中，但至今缺乏有效的量子安全构造。
>
> **主要贡献:** 本文提出了一种新的基于格的集团签名方案，通过最小化零知识证明中需要隐藏的元素数量，并利用最近的格采样器的一些技巧，实现了在保持BMW安全性的同时仅依赖标准的格假设。
>
> **达到效果:** 该方案不仅达到了与传统方法相当的安全性水平，而且在效率上有所提升，为量子安全环境下提供了有效解决方案。
>
> **技术梗概:** 通过使用委托格基并避免复杂的OR证明，结合特定的格采样器技巧，实现了高效且安全的集团签名方案。

---
### [推荐] [2026/851] From Blind to Oblivious Identity-Based Encryption: A Generic Compiler and Instantiations

- **匹配关键字:** lattice, post-quantum

- **作者:** Olivier Blazy, Estelle Blin, Sayantan Mukherjee

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/851) | [PDF](https://eprint.iacr.org/2026/851.pdf)


> **研究背景:** 身份基加密（IBE）简化了公钥基础设施，但存在密钥托管问题，导致权威机构能够解密任何密文。Mitrokotsa等人提出了更安全的盲态IBE和不可忽略的IBE概念，但仍需复合群组方法且缺乏通用编译器。
>
> **主要贡献:** 作者提出了一种通用编译器，将任意盲态IBE转换为不可忽略的IBE，建立了密钥提取盲态与加密不可忽略之间的基本联系。
>
> **达到效果:** 通过结合盲态IBE和哈希函数，证明了权威机构必须穷尽搜索接收者身份才能解密，展示了编译器的多样性和实际影响。
>
> **技术梗概:** 该编译器利用哈希函数处理身份空间输入，确保权威机构在解密时需进行全面搜索，从而实现不可忽略性。

---
### [推荐] [2026/852] ∆-SQIsign:  A New Isogeny-Based Signature Scheme Using Degree Challenges

- **匹配关键字:** post-quantum

- **作者:** Kohei Nakagawa, Ryo Yoshizumi

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/852) | [PDF](https://eprint.iacr.org/2026/852.pdf)


> **研究背景:** 基于Isogeny的密码学因其抗量子计算攻击的能力而受到关注，成为后量子密码学的重要候选方案。
>
> **主要贡献:** 本文提出了一种新的基于Isogeny的签名方案∆-SQIsign，通过引入度挑战显著改进了现有方案。
>
> **达到效果:** 该方案在NIST后量子密码标准化竞赛中表现出色，并且能够生成具有较小规范的理想。
>
> **技术梗概:** 为了实现这一目标，作者提出了一种新的算法∆-KLPT，它是GeneralizedKLPT的变体，在特定条件下能产生更小规范的理想。

---
### [推荐] [2026/853] MRFHE: Mixed-Radix Fully Homomorphic Encryption with Better Batch Bootstrapping

- **匹配关键字:** homomorphic encryption

- **作者:** Jung Hee Cheon, Seungwan Hong, Minsik Kang, Jonghyun Kim, Taeseong Kim, Changmin Lee, Junho Lee

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/853) | [PDF](https://eprint.iacr.org/2026/853.pdf)


> **研究背景:** 全同态加密是一种有前景的密码学原语，用于隐私保护计算，但其实际部署的主要瓶颈在于密钥切换操作，尤其是批量评估离散傅里叶变换及其逆变换所需的大量旋转操作。
>
> **主要贡献:** 作者提出了一种新的全同态加密方案MRFHE，该方案基于混合基数循环环，并将DFT分解为两层——基2 DFT和基3 DFT，从而减少密钥切换操作的数量并加速批量评估过程。
>
> **达到效果:** 通过这种结构化的方法，MRFHE能够显著降低每次解密所需的旋转次数至常数级别，并且在实际应用中表现出更好的性能。
>
> **技术梗概:** 该方案利用了混合基数分解技术来优化DFT的同态计算，从而减少关键操作的数量并提高批量评估效率。

---
### [推荐] [2026/855] Zinc+: SNARKs for Polynomial Rings

- **匹配关键字:** lattice

- **作者:** Alexander Abdugafarov, Albert Garreta, Amit Kumar, Michał Osadnik, Psi Vesely, Ilia Vlasov, Kai Zhe Zheng

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/855) | [PDF](https://eprint.iacr.org/2026/855.pdf)


> **研究背景:** 现有的简洁证明系统通常将计算表示为有限域上的代数约束，但非原生的位操作、模算术和环多项式运算需要额外的归约步骤，这会显著增加见证大小。
>
> **主要贡献:** 论文提出了通用约束系统(UCS)及其框架Zinc$+$，用于构建多项式环上的SNARKs，特别适用于包含多种多项式环的理想成员资格谓词。
>
> **达到效果:** 使用Zinc$+$ SNARKs可以高效地验证复杂计算的正确性，同时保持较小的证明大小和较快的验证速度。
>
> **技术梗概:** 通过将标准有限域PIOP编译为UCS PIOP，并结合基于哈希的多线性多项式IOPP设计（针对不同环），实现了上述目标。

---
### [推荐] [2026/857] Lasagne: Practical Verifiable Computation over Encrypted Data

- **匹配关键字:** homomorphic encryption

- **作者:** Xinxuan Zhang, Ruida Wang, Qingyun Niu, Peixin Liu, Xianhui Lu, Lutan Zhao, Rui Hou, Yi Deng

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/857) | [PDF](https://eprint.iacr.org/2026/857.pdf)


> **研究背景:** Verifiable Computation on Encrypted Data (VCoED)旨在解决全同态加密（FHE）中的计算完整性的缺口，但现有协议在服务器端证明生成方面仍存在高计算成本的问题。
>
> **主要贡献:** Lasagne提出了一种新的高效VCoED方案，支持多层乘法电路，并允许这些电路在SIMD消息编码下进行同态评估，从而适应实际FHE部署的需求。
>
> **达到效果:** 对于一个16层、$2^{20}$-gate的负载电路，Lasagne仅需6–12分钟（单核）生成30 MB证明，比Phalanx快了11到23倍。当负载自然支持SIMD执行时，证明时间进一步减少至4–5分钟，提高了27到34倍的速度。
>
> **技术梗概:** Lasagne通过优化证明者时间和保持可接受的通信/验证开销来实现高效性，并允许灵活选择参数以权衡证明者时间和通信开销。

---
### [推荐] [2026/858] FRI Soundness Above the Johnson Bound via Threshold Halving

- **匹配关键字:** post-quantum

- **作者:** Raullen Chai, Xinxin Fan

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/858) | [PDF](https://eprint.iacr.org/2026/858.pdf)


> **研究背景:** 研究旨在证明FRI、STIR和WHIR协议的安全性，这些协议是许多部署在以太坊路线图上的STARK、zkVM和FRI系统的底层技术。
>
> **主要贡献:** 贡献包括首次提供上述约翰逊界限的无条件声学定理，并通过阈值减半方法优化了查询参数，同时保持协议不变。
>
> **达到效果:** 结果表明，在特定条件下，声学误差率有所降低，同时证明了在相关协议框架下的最优查询开销，并提出了p-依赖列表大小的新边界。
>
> **技术梗概:** 技术上采用了阈值减半的方法来重新校准查询参数，并通过BCIKS锁定距离以提高安全性。

---
### [推荐] [2026/859] SoliloQuat: Throwing Caution to the Wind

- **匹配关键字:** lattice, post-quantum

- **作者:** Andrew Mendelsohn, Ben Nelson

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/859) | [PDF](https://eprint.iacr.org/2026/859.pdf)


> **研究背景:** 本文提出了一种基于四元数代数中短生成器理想问题（SG-PIP）的可加同态公钥加密方案SoliloQuat，旨在应对量子计算带来的挑战。
>
> **主要贡献:** 该贡献在于设计了一个新颖的安全方案，并证明了其在特定假设下的安全性。
>
> **达到效果:** 研究结果表明，SoliloQuat在某些假设下是IND-CPA安全的。
>
> **技术梗概:** 通过利用四元数代数中的左正则表示法特征值的新颖结果来实现同态加密功能。

---
### [推荐] [2026/862] Adaptively-Secure Flexible and Identity-Based Broadcast Encryption from Decomposed LWE

- **匹配关键字:** lattice, post-quantum, LWE

- **作者:** Rishab Goyal, Saikumar Yadugiri

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/862) | [PDF](https://eprint.iacr.org/2026/862.pdf)


> **研究背景:** 广播加密（BE）允许发送者向任意动态选择的用户子集加密消息，其黄金标准是参数独立于用户的最优简洁性和自适应安全性。然而，如何在可伪造后量子假设下同时实现这两点仍然是一个核心开放问题。
>
> **主要贡献:** 本文提出了首个基于分解LWE假设的自适应安全、参数与用户数量无关的灵活广播加密（FBE）和身份基广播加密（IBBE），并在随机预言模型中达到这些目标。
>
> **达到效果:** 该方案实现了所有参数大小独立于用户的最优简洁性，并且在技术上，通过扩展GY的可争议加密框架来捕捉无界和动态广播系统。
>
> **技术梗概:** 本文引入了可争议矩阵承诺作为核心技术之一，以支持上述结果。

---
### [推荐] [2026/864] Field-Agnostic SNARKs with Small Proofs via Encode-Repeat-Accumulate (ERA) Codes

- **匹配关键字:** post-quantum

- **作者:** Anubhav Baweja, Giacomo Fenzi, Pratyush Mishra, Tushar Mopuri

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/864) | [PDF](https://eprint.iacr.org/2026/864.pdf)


> **研究背景:** 哈希基础的SNARK因其后量子安全性和避免公钥密码学的特点而广为应用，其构建的关键在于纠错码和该码的接近性交互预言机证明（IOPP）。
>
> **主要贡献:** 研究引入了一种新的线性时间可编码的场无关纠错码——ERA码，并设计了适用于这些码的高效接近性交互预言机证明。
>
> **达到效果:** ERA码及其IOPP的设计使得生成的小型SNARK证明成为可能，同时保持了良好的性能指标。
>
> **技术梗概:** 通过结合快速编码时间和强距离保证，ERA码实现了场无关的SNARK，并利用其特性优化了接近性验证过程。

---
### [2026/844] MPlookup: A Quasilinear Multi-Party Lookup Argument in Collaborative zkSNARKs via Four Sorts and a Multi-Point Evaluation

- **作者:** Huayi Qi, Tingchuang Zhang, Zhijun Li, Minghui Xu, Xiuzhen Cheng, Chao Zhang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/844) | [PDF](https://eprint.iacr.org/2026/844.pdf)


> **研究背景:** 现有的查找论证协议仅适用于单方证明场景，无法满足多方协作零知识简洁非交互式知识论证（collaborative zkSNARKs）的需求。
>
> **主要贡献:** MPlookup是首个为collaborative zkSNARKs设计的多方查找论证协议，通过四次盲排序操作和多点多项式评估实现了准线性复杂度。
>
> **达到效果:** 该工作证明了MPlookup协议在分布式盲多项式评估设置下满足安全性、完整性、正确性和零知识性，并且性能表现良好。
>
> **技术梗概:** MPlookup利用了盲排序操作和基于不可知因子的盲多项式除法来实现多点多项式评估，构建了一个开源的Rust库。

---
### [2026/848] PPML Is More Vulnerable to Cryptanalytic Extraction Attacks

- **作者:** Wen Zhang, Bingsheng Zhang, Tianpei Lu, Kui Ren

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/848) | [PDF](https://eprint.iacr.org/2026/848.pdf)


> **研究背景:** 随着机器学习即服务(MLaaS)的扩展，安全多方计算(MPC)被广泛用于保护推理过程中的私有模型和客户端数据隐私。然而，为了实现实际性能，这些协议通常依赖于有限环上的定点算术，这引入了独特的算术漏洞：静默模周期溢出。
>
> **主要贡献:** 本文提出了一种新颖的模型提取攻击方法，该方法主动利用模周期溢出行为精确恢复神经网络参数。与现有方法主要依赖分段线性激活函数（如ReLU）的非可微点不同，我们的攻击利用了由模周期溢出触发的不连续跳跃。
>
> **达到效果:** 我们提出了多项式时间算法来恢复神经元签名、范数和符号，并证明即使在仅提供最高1标签和概率的受限黑盒场景中，我们的方法仍然具有高度鲁棒性。理论证明和信噪比(SIR)分析表明，我们的符号恢复方法显著优于现有神经元抖动技术。
>
> **技术梗概:** 该研究利用了模周期溢出这一独特漏洞，并开发了一种基于此现象的新型提取算法，能够从使用平滑激活函数（如Swish、GELU）的网络中有效提取参数。

---
### [2026/849] On Why and How to Minimize the Arithmetic Complexity of Fast Matrix Multiplication Algorithms

- **作者:** Erik Mårtensson, Paul Stankovski Wagner

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/849) | [PDF](https://eprint.iacr.org/2026/849.pdf)


> **研究背景:** 研究背景：矩阵乘法的快速算法在减少计算复杂度方面具有重要意义，尤其是通过减少所需的乘法和加法操作。Strassen提出了一个使用较少乘法但更多加法的操作方法，而Karstadt和Schwartz则进一步优化了加法的数量。
>
> **主要贡献:** 主要贡献：本文提出了一种新的方法来优化大型矩阵乘法方案中的加法数量，无需改变基底，并且在整体快速矩阵生成过程中同时考虑方案生成和加法减少的优化。
>
> **达到效果:** 达到的效果：通过实施这些方法，作者成功地减少了多个维度（最大至5x7x10）的方案中所需的加法操作数，并表明其方法相对于Karstadt-Schwartz框架在较大矩阵尺寸时表现更优。
>
> **技术梗概:** 技术梗概：本文的技术涉及对Strassen型矩阵乘法方案进行优化，通过改进生成过程中的加法减少策略，从而实现整体计算复杂度的降低。

---
### [2026/854] How to Simulate Random Oracles with Auxiliary Input

- **作者:** Yevgeniy Dodis, Aayush Jain, Huijia Lin, Ji Luo, Daniel Wichs

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/854) | [PDF](https://eprint.iacr.org/2026/854.pdf)


> **研究背景:** 随机预言机模型（ROM）在设计实用密码系统时提供了安全属性的乐观推理，但对非统一对手来说过于理想化。Unruh提出了辅助输入随机预言机模型（AI-ROM），允许对手获得关于随机预言机的部分信息，以更接近现实情况。
>
> **主要贡献:** 作者解决了Unruh提出的一个长期悬而未决的问题：如何在计算设置中高效模拟具有辅助输入的随机预言机查询，并证明了广泛类别的计算方案在AI-ROM中的安全性。
>
> **达到效果:** 通过高效的模拟技术，研究达到了低实际开销和较小的安全损失，使得理论结果更接近于实际应用。
>
> **技术梗概:** 作者利用新颖的技术工具，在保持安全性的前提下实现了随机预言机查询的高效模拟，并将其应用于证明多种计算方案在AI-ROM中的安全性。

---
### [2026/856] MERIDIAN: A Toroid-Inspired Permutation Block Cipher for Constrained Environments

- **作者:** Basker Palaniswamy, Paolo Palmieri, Ashok Kumar Das, Ruei-Hau Hsu

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/856) | [PDF](https://eprint.iacr.org/2026/856.pdf)


> **研究背景:** MERIDIAN旨在为资源受限环境提供一种轻量级替代方案，同时保持AES-128的接口兼容性。
>
> **主要贡献:** 该设计通过引入Directional Substitution、Meridian Diffusion和Admittance Mixing等操作，实现了在不使用MDS乘法的情况下，在三轮内达到全字节扩散的效果。
>
> **达到效果:** MERIDIAN经过了MILP验证的安全性分析，并通过实验对比证明其在关键灵活性、冷启动延迟、能耗、防侧信道成本、内存占用和硬件复杂度等方面优于AES-128。
>
> **技术梗概:** 该算法基于四维离散环Z4 × Z4的状态表示，利用两个正交字排列与列混合来实现快速扩散。

---
### [2026/860] Your Loss is My Gain: Low Stake Attacks on Liquid Staking Pools

- **作者:** Sen Yang, Aviv Yaish, Arthur Gervais, Fan Zhang

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/860) | [PDF](https://eprint.iacr.org/2026/860.pdf)


> **研究背景:** 研究背景：无许可的权益证明（PoS）经济安全性依赖于违反共识安全或活性的成本高昂。然而，流动性质押引入了额外的风险，这些风险未被标准的PoS经济安全性论证所涵盖。
>
> **主要贡献:** 主要贡献：作者提出了一个跨层攻击框架，低风险对手可以通过操纵共识协议来降低目标池的表现，并在应用层采取获利策略。
>
> **达到效果:** 达到的效果：通过深度强化学习（DRL）框架自动发现的攻击策略能够恢复接近最优理论攻击，并揭示了显著损害目标池性能的新操纵行为。
>
> **技术梗概:** 技术梗概：研究利用蒙特卡洛模拟详细分析了杠杆做空渠道，并开发了一个基于DRL的框架来自动发现攻击策略，从而具体化共识层的操纵机制。

---
### [2026/861] Action–Orbit FRI Soundness Above the Johnson Radius: A Rigorous $O(1)/|F|$ Bound on Plain Reed–Solomon, with $2\times$ Smaller STARK Proofs   at Ethereum Scale

- **作者:** Raullen Chai, Xinxin Fan

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/861) | [PDF](https://eprint.iacr.org/2026/861.pdf)


> **研究背景:** 该研究解决了Reed-Solomon码在Johnson半径以上区域的FRI验证相距性问题，这是领域内的一个关键开放问题，尤其紧迫的原因是关于容量上限猜想的近期反驳。
>
> **主要贡献:** 作者提出了首个针对稀疏输入条件下的严格$O(1)/|F|$ FRI验证相距性界，并通过新的行动-轨道对称机制证明了这一结果。
>
> **达到效果:** 该研究将STARK证明大小减半，对于128位安全性的部署实例，与ABF最小可部署候选相比，证明大小从161.4 KiB和281.2 KiB分别减少到79.8 KiB。
>
> **技术梗概:** 通过引入行动-轨道对称性机制，在循环FRI评估域上构建了这一新的验证界限，无需相关一致性、字符求和或列表解码技术。

---
### [2026/863] Conquering Bad Norms in RstOE: Pure-Database Substitution and Early-Defense

- **作者:** Shuping Mao, Zhiyu Zhang, Peng Wang, Lei Hu, Luying Li, Ying Chen

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/863) | [PDF](https://eprint.iacr.org/2026/863.pdf)


> **研究背景:** 传统的RstOE技术在量子安全证明中至关重要，但面对自适应的量子选择明文攻击者时，可能会遭遇'规范退化'问题。
>
> **主要贡献:** 研究提出了Pure-Database Substitution和Early-Defense两种改进方法，以解决这一问题。
>
> **达到效果:** 通过这些改进，减少了进入不良子空间的概率，并避免了$O(1)$范数坍缩，从而提升了安全性。
>
> **技术梗概:** Pure-Database Substitution通过代数消除未记录的外部变量并重新定义碰撞约束来实现；Early-Defense则将碰撞检查提前到新内部变量生成时进行。

---
### [2026/865] Secret-Key PIR from One-Way Functions

- **作者:** Nir Bitansky, Noam Mazor

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/865) | [PDF](https://eprint.iacr.org/2026/865.pdf)


> **研究背景:** SK-PIR允许客户端在不泄露访问记录的情况下从服务器获取信息，且通信量远小于数据库大小。
>
> **主要贡献:** 作者首次仅基于单向函数构建了具有$\tilde{O}(\sqrt{N})$在线通信的SK-PIR方案，并展示了满足特定属性的门限加密方案的应用。
>
> **达到效果:** 该研究显著降低了SK-PIR的通信复杂度，同时证明了在更弱的安全假设下实现高效SK-PIR的可能性。
>
> **技术梗概:** 通过设计满足特定输入编码特性的门限加密方案来构建SK-PIR，并利用点和置换方案的性质。

---

## 更新: 2026-05-03 20:24

*新增 10 篇论文 (编号 834--843)*

### [推荐] [2026/834] Detecting Post-Quantum and Hybrid TLS Deployments via Raw TLS Record Inspection

- **匹配关键字:** post-quantum

- **作者:** Muhammad Ibrahim, Vishnu Ajith, Muhammed Sihan Haroon

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/834) | [PDF](https://eprint.iacr.org/2026/834.pdf)


> **研究背景:** 随着量子计算的发展，过渡到后量子密码学（PQC）以保护网络系统免受未来量子对手的攻击变得至关重要。然而，验证这些算法在实际系统中的正确部署仍然具有挑战性。
>
> **主要贡献:** 本文提出了一种通过直接检查原始TLS握手记录来检测后量子和混合TLS密钥交换机制的新方法，该方法能够准确地将端点分类为CLASSICAL_ONLY、PQC_ONLY和HYBRID_CONFIRMED状态。
>
> **达到效果:** 实验结果表明，在验证阶段1中，所有三个测试节点（包括一个具备PQC能力的应用服务器）都被正确地归类为CLASSICAL_ONLY状态；在验证阶段2中，随着OQS兼容的TLS前端升级，实现了100%的目标准确性，并确认了一个HYBRID_CONFIRMED的结果。
>
> **技术梗概:** 通过解析ServerHello消息并从密钥共享扩展中提取密钥组标识符来进行字节级解析，从而实现对端点状态的准确分类。

---
### [推荐] [2026/837] Trident: Efficient FPGA Acceleration of XMSS Tree in Post-Quantum Signature Scheme SLH-DSA

- **匹配关键字:** post-quantum

- **作者:** Tianyou Bao, Joshua Ennis, Kirill Morozov, Jiafeng Xie

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/837) | [PDF](https://eprint.iacr.org/2026/837.pdf)


> **研究背景:** 量子计算的发展对传统密码系统构成了重大威胁，需要在FPGA等硬件平台上高效加速后量子密码学（PQC），特别是XMSS树的计算密集型操作。
>
> **主要贡献:** Trident提出了三角哈希单元架构和优化的内存缓存方案，分别解决了XMSS树构建中的并行执行瓶颈和芯片内存需求问题。
>
> **达到效果:** 在所有参数集上实现了8.6倍的签名生成速度提升，并且提高了5.4倍的速度。
>
> **技术梗概:** 通过设计三角哈希单元实现三个哈希操作的同时进行，优化内存缓存管理以减少芯片内存使用。

---
### [推荐] [2026/838] On the Resilience Order of Weightwise Almost Perfectly Balanced Functions

- **匹配关键字:** homomorphic encryption

- **作者:** Martin Grenouilloux, Chunlei Li, Pierrick Méaux

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/838) | [PDF](https://eprint.iacr.org/2026/838.pdf)


> **研究背景:** 研究背景：随着全同态加密(FHE)的发展，需要设计满足其特定要求的新一代定制密码学原语。FLIP密码中的布尔函数仅在$\mathbb{F}_2^n$的某些子集上进行评估，而Weightwise Almost Perfectly Balanced (WAPB)函数在这种背景下引起了关注，但其抗攻击性（尤其是正确性）仍需进一步研究。
>
> **主要贡献:** 主要贡献：本文首次系统地探讨了WAPB函数的抗攻击性，通过与限制沃尔什变换的关系揭示了Krawtchouk矩阵和范德蒙德矩阵之间的代数联系，并将确定WAPB函数正确性阶的问题归约为Prouhet-Tarry-Escott问题的一个特例。
>
> **达到效果:** 达到的效果：证明了对于无限多个整数$n$，在$n$个变量中的WAPB函数的正确性阶紧致上界为$n-1$的汉明重量。同时提出猜想认为这一观察对任意正整数$n$都成立，并验证了该猜想在$n \leq 62$时的有效性。
>
> **技术梗概:** 技术梗概：通过研究WAPB函数与限制沃尔什变换的关系，以及Krawtchouk矩阵和范德蒙德矩阵之间的联系，将复杂问题简化为Prouhet-Tarry-Escott问题的一个实例进行求解。

---
### [推荐] [2026/840] All You Need Is Addition

- **匹配关键字:** homomorphic encryption

- **作者:** Dimitrios Schoinianakis

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/840) | [PDF](https://eprint.iacr.org/2026/840.pdf)


> **研究背景:** 本文提出了一种加速CKKS同态加密的框架，通过使用对数数值系统（LNS）来替代密文间的乘法运算，从而减少计算复杂度。
>
> **主要贡献:** 该工作贡献了一种新的执行策略，并在OpenFHE平台上实现了三种不同的执行方式，以适应不同的应用场景。
>
> **达到效果:** 实验结果显示，在注意力管道中，与线性基线相比，LNS方法能够显著提高速度并大幅减小密文大小，尤其是在深度较大的情况下效果更为明显。
>
> **技术梗概:** 该技术通过在需要累加的地方进行交互式刷新操作，并利用LNS来避免完全的重新密封过程。

---
### [推荐] [2026/841] HAKE: Efficient Hardware Accelerator for Key Generation of Post-Quantum Signature Scheme PERK

- **匹配关键字:** post-quantum

- **作者:** Brendan Funk, Tianyou Bao, Loïc Bidoux, Jiafeng Xie

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/841) | [PDF](https://eprint.iacr.org/2026/841.pdf)


> **研究背景:** 随着量子计算的进步，后量子密码学（PQC）成为研究热点，旨在开发能够抵御量子攻击的加密方案。PERK是NIST后量子签名方案标准制定过程中的候选算法之一。
>
> **主要贡献:** 本文贡献了两个版本的硬件加速器，分别基于PERK的旧版和新版规范设计，以提高密钥生成效率。
>
> **达到效果:** 通过优化硬件设计并分解密钥生成过程，HAKE显著提高了PERK签名方案的密钥生成速度，展示了在硬件平台上的高效实现能力。
>
> **技术梗概:** 通过对PERK算法进行详细分析，将密钥生成过程拆分为三个独立组件，并提出减少这些组件复杂性的创新方法，同时设计了专用的硬件微架构。

---
### [2026/835] Fault Injection Attacks Against zkSTARKs

- **作者:** Alexander Dalton, Markus Schofnegger, Daniel Page

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/835) | [PDF](https://eprint.iacr.org/2026/835.pdf)


> **研究背景:** 当前文献中针对零知识（ZK）属性方案的故障注入攻击相对较少，而最近有研究指出一种ZK签名方案存在此类漏洞。
>
> **主要贡献:** 本文首次详细探讨了针对Zero-Knowledge Scalable Transparent Argument of Knowledge (zkSTARK)证明者实施候选故障注入攻击的可能性，以破坏其零知识特性。
>
> **达到效果:** 通过提出针对不同算法基础组件的多种故障注入攻击方法，展示了对zkSTARK证明系统的潜在威胁，并填补了该领域的研究空白。
>
> **技术梗概:** 本文匹配STARK实现生态系统的多样性，提出了针对各种算法基础组件的不同故障注入技术。

---
### [2026/836] Privacy-Preserving Aggregate-Signatures: Generic Constructions and Practical Instantiations

- **作者:** Xiaoyang Wei, Shuai Han, Shengli Liu

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/836) | [PDF](https://eprint.iacr.org/2026/836.pdf)


> **研究背景:** 现有聚合签名方案不支持密钥聚合且缺乏对签署者的强隐私保护，而DahLIAS虽解决了部分问题但未能提供聚合验证和隐私属性。
>
> **主要贡献:** 作者正式提出了带有可验证密钥聚合的聚合签名（ASvKA）概念，并提供了新的不可伪造性和隐私性定义，同时设计了一种通用转换方法将任何多签方案转化为具有可验证密钥聚合和隐私性的聚合签名方案。
>
> **达到效果:** 该研究实现了在保持高效的同时提供最强不可伪造性和隐私性的无配对方案PP-SpeedyASvKA，并通过实例化展示了其实用性。
>
> **技术梗概:** 作者采用了一种通用转换技术，将多签方案转化为具有可验证密钥聚合和隐私属性的聚合签名方案，从而提升了底层多签方案的安全性。

---
### [2026/839] Efficient Non-Interactive Key Refresh with Multiple Independent Refreshers for Threshold Cryptography

- **作者:** Dragan Lambić

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/839) | [PDF](https://eprint.iacr.org/2026/839.pdf)


> **研究背景:** 针对阈值密码学中单个经销商的集中信任问题，本文提出了一种新型的非交互式密钥刷新架构。
>
> **主要贡献:** 该设计通过引入多个独立第三方刷新者来实现密钥的异步分发和刷新，从而避免了协调交互的需求，并提高了系统的可用性。
>
> **达到效果:** 此方法确保在所有刷新者被攻破的情况下仍能保持保密性（只需一个诚实的签名方），并在最少参与下实现前瞻性的安全性。
>
> **技术梗概:** 通过将签名方与刷新操作分离，以及允许部分刷新者的缺席，该设计实现了高效的安全性，并减少了链上密钥轮换的成本。

---
### [2026/842] Secure Integrated Sensing and Communication: Information Theory Offers Insights

- **作者:** Truman Welling, Onur Gunlu, Aylin Yener

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/842) | [PDF](https://eprint.iacr.org/2026/842.pdf)


> **研究背景:** ISAC通过共享信号实现感测与通信的集成，提高了频谱和硬件使用效率，但也带来了新的安全挑战。
>
> **主要贡献:** 论文综述了信息论在确保ISAC安全中的应用，包括模型、性能指标及基本限制。
>
> **达到效果:** 研究明确了不同保护功能和对手模型下的安全ISAC形式化方法，并探讨了通信安全与感测安全的相互作用及其与隐私和隐蔽通信的关系。
>
> **技术梗概:** 通过信息论模型分析，论文揭示了在确保可靠通信、良好感测性能及安全性之间的权衡。

---
### [2026/843] Toward Practical Fair Data Exchange: Eliminating In-Circuit Public-Key Operations

- **作者:** Dongwook Kim, Jihye Kim, Hyunok Oh

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/843) | [PDF](https://eprint.iacr.org/2026/843.pdf)


> **研究背景:** 研究背景：现有的公平数据交换（FDE）协议在客户端验证时效率较低，而VECK\(^{\star}_{\mathrm{EL}}\)虽然提高了实用性，但在证明者成本方面仍有改进空间。
>
> **主要贡献:** 主要贡献在于提出了一种新的基于代码的FDE构造方法，去除了电路中ElGamal一致性检查的需求，并通过哈希掩码、KZG承诺和CP链接等技术实现了更高效的验证。
>
> **达到效果:** 达到的效果是显著降低了SNARK约束的数量，提高了证明者的效率，在基准实现中直接使用了BLS12-381曲线，而非VECK\(^{\star}_{\mathrm{EL}}\)所需的曲线循环。与之前的方案相比，证明者时间大幅减少。
>
> **技术梗概:** 技术梗概包括哈希掩码生成密文、KZG承诺验证一致性、CP链接绑定隐藏值以及一个小型的commit-and-prove SNARK来检查掩码、插值和公钥关系。

---

## 更新: 2026-05-02 20:26

*新增 9 篇论文 (编号 823--833)*

### [2026/823] TieredOMap: Skewness-Aware Oblivious Map

- **作者:** Juan Li, Xinle Cao, Huazhen Yu, Weiqi Feng, Jian Liu

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/823) | [PDF](https://eprint.iacr.org/2026/823.pdf)


> **研究背景:** 现有的Oblivious Map (OMAP)设计主要遵循均匀最坏情况原则，即每个记录的检索时间几乎相同，而不考虑查询频率。然而，在实际工作负载中，数据通常高度偏斜，一小部分热点数据占了大多数请求。
>
> **主要贡献:** TieredOMap是首个针对偏斜性的OAM框架，通过将热和冷记录分离到独立的OMAP中以提高对热记录的访问效率，同时不削弱标准OMAP的安全性保证。
>
> **达到效果:** 实验结果表明，基于偏斜性的访问并不必遵循均匀最坏情况行为，偏斜性感知结构为OAM设计提供了一个新的有前景的方向。
>
> **技术梗概:** TieredOMap通过分离热和冷记录并独立管理它们来优化性能，并且其设计支持在安全性的轻微放松下进一步提高性能。

---
### [2026/824] Better Usability: Leakage-Resistant AEADs from Single-length Blockciphers

- **作者:** Chun Guo, Mustafa Khairallah, Kazuhiko Minematsu

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/824) | [PDF](https://eprint.iacr.org/2026/824.pdf)


> **研究背景:** 现有抗侧信道AEAD方案大多不适用于单长度密钥块密码，本文旨在填补这一空白。
>
> **主要贡献:** 提出了UEDTDM和UEDTMX两种基于单长度密钥块密码的抗侧信道AEAD构造。
>
> **达到效果:** 这两种构造都实现了1/4速率的一次通过模式，并且在实际效率上使用了部分固定密钥块密码，达到了三级泄漏抵抗级别，并具有与当前最佳构造TEDT相当的安全边界，同时具备生日界限上下文绑定安全性。
>
> **技术梗概:** 引入了框架UEDT来扩展并统一证明EDT构造的可证明安全性结果，从而为UEDTDM和UEDTMX实例推导出具体的安全界。

---
### [2026/825] Scalable Secure Biometric Authentication without Auxiliary Identifiers

- **作者:** Alexander Bienstock, Daniel Escudero, Antigoni Polychroniadou, Zhen Zeng, Pranav Bhat, Ashok Singal, Prashant Sharma, Manuela Veloso

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/825) | [PDF](https://eprint.iacr.org/2026/825.pdf)


> **研究背景:** 随着生物特征认证系统的普及，其便捷性和安全性优势日益凸显。然而，现有的云数据库存储大量用户生物特征数据的系统存在安全风险和高计算成本问题。
>
> **主要贡献:** 本文提出了一种新的生物特征认证系统，结合了人工智能与高级加密技术，提供数据泄露防护的同时保持高效性，并且无需辅助标识符。
>
> **达到效果:** 该系统实现了大规模隐私保护生物特征认证的可行性，显著提升了用户体验和安全性。
>
> **技术梗概:** 通过创新地融合AI技术和加密方法，并进行多项优化，本文解决了现有系统的安全性和性能问题。

---
### [2026/826] Efficient Implementation of ARIA on ARMv8 via Cryptographic Extensions

- **作者:** Myoungsu Shin, Dongjae Lee

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/826) | [PDF](https://eprint.iacr.org/2026/826.pdf)


> **研究背景:** ARIA是一种广泛使用的对称加密算法，尽管它已经具备了硬件加速支持，但在现代ARMv8处理器上的高效实现仍然有限。
>
> **主要贡献:** 本文通过重新利用AESE/AESD指令扩展来并行处理16个块，实现了ARIA在ARMv8 NEON上的高效实现。
>
> **达到效果:** 该实现将ARIA-128的每字节周期数从5.845降低至1.483，并且多线程模式下达到了接近线性的可扩展性。
>
> **技术梗概:** 通过使用字节切片数据布局和64指令转置蝴蝶操作，作者实现了对ARIA S-boxes的有效处理。

---
### [2026/828] ZEE200: Zero Knowledge for Everything and Everyone @ 200 KHz

- **作者:** Sunghyeon Jo, Vladimir Kolesnikov, Yibin Yang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/828) | [PDF](https://eprint.iacr.org/2026/828.pdf)


> **研究背景:** ZEE200基于零知识执行高阶程序的现有框架，通过高效证明通用声明来实现，这些声明以实际程序表示。
>
> **主要贡献:** 该研究贡献了一种新的常数轮次零知识系统ZEE200，显著提高了验证速度。
>
> **达到效果:** 与ZEE相比，ZEE200在商品笔记本电脑上实现了约200 KHz的CPU速度，并且支持更丰富的指令集。
>
> **技术梗概:** 该技术通过结合最新的紧致零知识CPU和快速零知识RAM等关键进展来实现高效证明，并开发了更好的整数算术编码和多种低级优化。

---
### [2026/829] Beyond Binary: crosscorrelation of Quartic and Cubic Character Sequences

- **作者:** Mriganka Dey, Sampa Dey, Sampurna Pal, Subhabrata Samajder, Rana Barua

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/829) | [PDF](https://eprint.iacr.org/2026/829.pdf)


> **研究背景:** 研究非二进制伪随机序列的算术互相关性对于密码学和通信应用至关重要，但现有工作主要集中在二进制序列上，非二进制情况的研究尚属空白。
>
> **主要贡献:** 作者首次系统地研究了基于有限域高阶乘法字符构造的非二进制伪随机序列的算术互相关性，并建立了四次和三次序列的相关性上界。
>
> **达到效果:** 通过应用特征正交性、联合模式分布及Weil界，作者证明了两个互素周期为P和Q的四次序列在所有偏移τ下的互相关性的绝对值小于dP^(1/2)Q(log P)^2，并且得到了三次序列类似的结果。
>
> **技术梗概:** 研究采用了特征正交性、联合模式分布及Weil界等技术，首次提供了非二进制伪随机序列算术互相关的非平凡上界。

---
### [2026/830] DY* Unchained: Now with Composable Security Proofs and Precise Compromise Scenarios

- **作者:** Théophile Wallez

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/830) | [PDF](https://eprint.iacr.org/2026/830.pdf)


> **研究背景:** DY*协议验证框架旨在解决现实世界协议中难以分析的特性，如无界循环、数据结构和参与者数量。然而，该框架存在安全证明不可组合及妥协场景描述过于简单的局限性。
>
> **主要贡献:** 作者通过开发模块化定义追踪不变量的框架以及全面泛化安全性标签的概念，解决了DY*的安全证明不可组合性和妥协场景描述精度不足的问题。
>
> **达到效果:** 这些改进使得DY*能够分析大型协议，并且已被用于TreeKEM协议的安全性证明中。
>
> **技术梗概:** 通过引入模块化的追踪不变量定义和更通用的安全性标签概念，提高了DY*的灵活性和精确度。

---
### [2026/832] Private Delegation of (Non-)Membership Proof Updates in Cryptographic Accumulators

- **作者:** Bence Soóki-Tóth, Botond Glasz, Alireza Kavousi, István András Seres

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/832) | [PDF](https://eprint.iacr.org/2026/832.pdf)


> **研究背景:** 研究背景：在许多应用中，有效的（非）成员身份证明是访问服务的前提条件。然而，当客户端与服务器断开连接后重新连接时，由于需要频繁更新所有现有的（非）成员身份证明，这将导致客户端持有无效的证明。
>
> **主要贡献:** 主要贡献在于设计并实现了允许资源受限的客户端能够私下委托给不可信服务器更新其（非）成员身份证明的算法，并在RSA和双线性积聚器中进行了验证。
>
> **达到效果:** 达到的效果是，客户端可以保持有效的（非）成员身份证明，即使在网络连接不稳定的情况下也能访问服务。此外，在批量设置下研究了证明委托问题，并展示了在线客户端算法的时间复杂度与更新集大小无关。
>
> **技术梗概:** 技术梗概：利用RSA和双线性积聚器设计并实现了常数时间的在线客户端算法以及具有较小计算开销的私有委托算法。

---
### [2026/833] Scale, Round, Break: Simple Leakage Attacks on Secret Sharing Schemes

- **作者:** Katharina Boudgoust, Mark Simkin

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/833) | [PDF](https://eprint.iacr.org/2026/833.pdf)


> **研究背景:** 研究了$t$-out-of-$n$门限秘密共享方案在局部泄漏下的鲁棒性，特别是针对线性重建和有限域上的攻击。
>
> **主要贡献:** 提出了一个简单且完美的攻击方法，能够在$\lg t + \mathcal{O}(1)$比特的泄漏下完全破解任何线性重建的秘密共享方案。
>
> **达到效果:** 该研究揭示了更大的有限字段不一定能提高泄露鲁棒性，并表明提高Shamir方案中的重构阈值帮助不大。
>
> **技术梗概:** 提出了一种近似线性的尺度和舍入函数，将来自任意大域的份额映射到较小的环中，同时保持分离良好秘密的距离。

---

## 更新: 2026-04-29 19:49

*新增 17 篇论文 (编号 802--822)*

### [推荐] [2026/802] A Primer on Dependency in Polynomial Product: Identify, Exploit, and Trim

- **匹配关键字:** lattice

- **作者:** Yijian Liu, Jiangxia Ge, Yu Zhang, Jiabo Wang, Xianhui Lu

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/802) | [PDF](https://eprint.iacr.org/2026/802.pdf)


> **研究背景:** 研究背景：许多基于格的加密方案允许非零但可忽略的解密失败率（DFR），这与正确性和安全性密切相关，并通过基于故障的攻击来衡量。现有的模块化格构造通常假设噪声在系数上是独立且均匀分布的，但在实际安全场景中这种假设可能过于乐观。
>
> **主要贡献:** 主要贡献：作者通过对二进制循环环中的多项式乘积进行范数分解，明确展示了由于卷积引入的结构依赖性，使得噪声向立方体而非球体扩散。这为理解多项式产品的重尾现象提供了精确解释，并揭示了基于独立性的估计与实际故障行为之间的差距。
>
> **达到效果:** 达到的效果：该研究不仅澄清了多项式乘积中的依赖关系，还为设计更安全的加密方案奠定了理论基础，有助于提高基于格的密码学的安全性和可靠性。
>
> **技术梗概:** 技术梗概：通过范数分解方法，将多项式乘积分为外项和内项，分别对应于噪声的半径部分和表面不均匀部分，并利用对角能量术语来捕捉卷积引起的依赖性。

---
### [推荐] [2026/807] When Data Movement Becomes the Bottleneck in Modern Workloads: Compute-in-Transit as an Architectural Model

- **匹配关键字:** post-quantum, homomorphic encryption

- **作者:** Flavio Bergamaschi

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/807) | [PDF](https://eprint.iacr.org/2026/807.pdf)


> **研究背景:** 现代计算工作负载中，性能受限于数据移动的成本而非计算本身，特别是在大规模数据集的频繁转换场景下。
>
> **主要贡献:** 提出Compute-in-Transit架构模型，在数据传输过程中嵌入计算操作，减少中间存储和重复传输的需求。
>
> **达到效果:** 该模型通过将计算与数据流对齐，显著提高了系统效率，并为后量子密码学、全同态加密及人工智能等领域提供了新的解决方案。
>
> **技术梗概:** 采用光子技术直接在信号传输过程中执行转换操作，突破了传统电子架构的限制，实现计算与数据移动同步进行。

---
### [推荐] [2026/810] Decomposing Multiplication: A Vertical Packing Approach for Faster TFHE

- **匹配关键字:** homomorphic encryption

- **作者:** Rostin Shokri, Nektarios Georgios Tsoutsos

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/810) | [PDF](https://eprint.iacr.org/2026/810.pdf)


> **研究背景:** 在全同态加密(FHE)中，尽管现代方案如TFHE能够高效处理非线性操作，但其乘法的时间复杂度仍然是性能瓶颈，特别是在需要大量密文-密文(CxC)和密文-明文(CxP)乘法的机器学习等应用中。
>
> **主要贡献:** 该研究提出了针对CxC和CxP乘法及点积的新算法，并通过垂直打包技术将乘法分解为一系列依赖精度的查找表操作，从而显著提高了FHE的性能。
>
> **达到效果:** 实验结果表明，与TFHE-rs默认实现及最近的先进工作相比，该方法实现了几倍于原来的执行速度，大幅加速了FHE在实际应用中的运行效率。
>
> **技术梗概:** 研究采用垂直打包技术，将乘法操作分解为一系列查找表操作，并通过优化这些操作来减少计算复杂度和提高执行效率。

---
### [推荐] [2026/811] Efficient Bootstrapping of Matrices in FHE

- **匹配关键字:** homomorphic encryption

- **作者:** Rostin Shokri, Nektarios Georgios Tsoutsos

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/811) | [PDF](https://eprint.iacr.org/2026/811.pdf)


> **研究背景:** 近年来，全同态加密（FHE）因其在神经网络推理、私有信息检索和基因组分析等隐私保护应用中的实用性而受到广泛关注。然而，在FHE中高效实现矩阵乘法仍然是一个巨大的挑战。
>
> **主要贡献:** 本文首次提出了GL方案中矩阵乘法的高效Bootstrapping算法，解决了该方案特有的环结构所带来的问题，并支持CKKS的所有操作。
>
> **达到效果:** 通过引入新的编码策略和优化技术，该工作显著降低了评估密钥的大小，缩短了执行时间，并消除了对矩阵维度的限制，从而提高了FHE中深度学习推理的效率。
>
> **技术梗概:** 本文采用GL方案特有的环结构和3D DFT编码方法，并结合高效的NTT变换，设计了一种新颖的Bootstrapping算法以支持大规模深学习模型的计算。

---
### [推荐] [2026/814] Threshold Signatures as-a-Service: Achieving Threshold ML-DSA in One Online Round

- **匹配关键字:** lattice

- **作者:** Matthieu Rambaud, Sascha Roth, Antoine Urban

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/814) | [PDF](https://eprint.iacr.org/2026/814.pdf)


> **研究背景:** 本文提出了Threshold Signatures as-a-Service (TSaaS)模型，旨在为工业中的钱包服务提供安全的阈值签名解决方案。
>
> **主要贡献:** 贡献在于定义了TSaaS，并提出了一种结合前两轮操作的ML-DSaaS方案，显著减少了在线阶段的时间消耗。
>
> **达到效果:** 实验表明，与[Celi et al., USENIX'26]相比，在线阶段的速度提高了两到三倍。
>
> **技术梗概:** 通过将客户端和参与方之间的通信集中化，并利用协调机器过滤请求来实现优化。

---
### [推荐] [2026/817] SOLMAE: Lightweight Post-Quantum Signature based on NTRU lattices with Hybrid Sampling

- **匹配关键字:** lattice, post-quantum

- **作者:** Kwangjo Kim

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/817) | [PDF](https://eprint.iacr.org/2026/817.pdf)


> **研究背景:** SOLMAE是一种基于NTRU格的轻量级后量子签名方案，旨在结合Falcon、Mitaka和Antrag等早期设计的优点，提供更高效的性能和更高的安全性。
>
> **主要贡献:** SOLMAE通过引入新颖的关键生成算法，增强了安全性并消除了Falcon中的僵化性，同时保持了参数的灵活性和快速的签名过程。
>
> **达到效果:** 该方案实现了与Falcon相似的安全性和紧凑的密钥及签名大小，同时提高了效率，并兼容最近的椭球高斯采样技术以减小签名大小。
>
> **技术梗概:** SOLMAE采用混合高斯抽样器在NTRU格上实现，并结合Mitaka的速度和并行性以及Falcon的安全性和紧凑性。

---
### [推荐] [2026/819] Topology-Driven Symbolic Verification of Post-Quantum Migration Paths Using Tamarin Prover

- **匹配关键字:** post-quantum

- **作者:** Vishnu Ajith, Mohammed Ibrahim, Muhammed Sihan Haroon

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/819) | [PDF](https://eprint.iacr.org/2026/819.pdf)


> **研究背景:** 研究背景：随着从经典公钥密码学向后量子密码学的过渡，协议层面的风险并未通过配置审查、性能基准测试或端点可达性测试得到充分解决。现有的抽象可能使部署看似操作正确，但实际上仍存在机密性、认证或前向保密方面的协议级违规问题。
>
> **主要贡献:** 主要贡献：提出了一种拓扑驱动的符号验证工作流，将分布式系统通信图转换为Tamarin模型进行分析，并基于图基部署表示推导出协议角色、通信约束和迁移策略，生成了可执行性、机密性、认证性和前向保密性的模型和相关引理。
>
> **达到效果:** 达到的效果：实验评估表明，该框架能够产生区分性强的符号验证结果而非统一失败报告。注册仅控制场景验证了所有报告的引理，其余场景表现出两种不同的反证模式：三个场景中的机密性和前向保密性失败，一个场景中认证失败。这些结果表明，符号验证为后量子迁移分析提供了补充保证层。
>
> **技术梗概:** 技术梗概：采用图基拓扑表示以确保从语义等价的输入生成确定性的模型，并使用Dolev--Yao对手模型进行分析，从而推导出协议角色、通信约束和迁移策略。

---
### [推荐] [2026/820] Improving Correlation Power Analysis on Masked CRYSTALS-Kyber with Lattice Attack

- **匹配关键字:** lattice, post-quantum

- **作者:** Yen-Ting Kuo, Atsushi Takayasu

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/820) | [PDF](https://eprint.iacr.org/2026/820.pdf)


> **研究背景:** 针对掩码版CRYSTALS-Kyber的关联功率分析攻击，前人研究未能有效恢复全密钥，且所需的电容迹线数量较多。
>
> **主要贡献:** 本文提出了一种新的攻击方法，仅需400条电容迹线即可完全恢复密钥，显著减少了所需数据量。
>
> **达到效果:** 通过结合Kannan嵌入法和Bai-Galbra方法，成功实现了全密钥的恢复，并验证了该方法的有效性。
>
> **技术梗概:** 采用了非传统的嵌入技术，将部分已知信息与绝对值信息相结合以提高攻击效率。

---
### [2026/803] X24 Down: Cryptanalysis of Hankel-based Multivariate Signatures

- **作者:** Alexandre Camelin, Thai Hung Le, Brice Minaud, Phong Q. Nguyen, Florian Tousnakhoff

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/803) | [PDF](https://eprint.iacr.org/2026/803.pdf)


> **研究背景:** X24是一种由Di Muzio等人在PQCrypto 2026会议上提出的新型多变量签名方案，它提供了短小的签名并采用了一种不同于UOV和HFE框架的新设计方法。
>
> **主要贡献:** 作者提出了一种有效的X24密码分析方法，能够从公钥中恢复私钥，并将外代数应用于多变量密码分析，揭示了与之前楔形攻击不同的应用方式。
>
> **达到效果:** 该攻击在时间复杂度为$O(q \cdot \mathsf{poly}(n))$下成功实现了对X24的密钥恢复，在实际参数设置下仅需几分钟即可完成。
>
> **技术梗概:** 攻击利用了外代数，最终将X24的密码分析问题转化为基于Generalized Reed-Solomon码的McEliece方案的密码分析问题。

---
### [2026/804] Verifying Provenance of Digital Media: Security Analysis of C2PA and its Implementation

- **作者:** Enis Golaszewski, Neal Krawetz, Alan T. Sherman, Edward Zieglar, Sai K. Matukumalli, Roberto Yus, Carson L. Kegley, Michael Barthel, William Bowman, Bharg Barot, Kaur Kullman

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/804) | [PDF](https://eprint.iacr.org/2026/804.pdf)


> **研究背景:** 随着生成式AI和高级编辑工具的发展，恶意行为者可以创建高质量的伪造图像，用于欺诈、攻击声誉和操纵选举。因此，研究如何验证数字媒体的真实性变得尤为重要。
>
> **主要贡献:** 该论文分析了C2PA数字溯源系统的安全特性，并对其规范、实现和一致性计划进行了首次形式化方法分析，指出了现有系统中的安全缺陷。
>
> **达到效果:** 通过分析，作者识别并描述了C2PA在时间戳协议一致性、验证者一致性和文件完整性等方面的不足之处，为改进该系统提供了理论依据。
>
> **技术梗概:** 研究采用了规范分析、实现审查和形式化方法相结合的技术手段，对C2PA的多个组件进行了全面的安全评估。

---
### [2026/806] Spectre Without Dependent Load

- **作者:** Can Aknesil, Andreas Lindner, Roberto Guanciale, Hamed Nemati

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/806) | [PDF](https://eprint.iacr.org/2026/806.pdf)


> **研究背景:** 传统的暂态执行攻击假设需要一个多阶段的读取-传输机制，即先进行一次暂态加载以获取机密数据，然后通过侧信道泄露这些数据。然而，本文揭示了在电磁泄漏的情况下，这一假设并不成立。
>
> **主要贡献:** 作者证明了一个单一的暂态加载操作即可产生值相关的电磁泄漏，无需任何后续传输指令或依赖于预取机制。
>
> **达到效果:** 该研究扩展了可利用的小型化攻击载体集合，并指出即使是简单的Cortex-A53处理器也存在安全风险。
>
> **技术梗概:** 通过实验验证了在电磁观测下，单一暂态加载操作即可产生值相关的泄漏现象，无需依赖复杂的传输机制。

---
### [2026/808] New Techniques for Communication-Efficient Secure Comparison Protocols

- **作者:** Koji Nuida, Satsuya Ohata

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/808) | [PDF](https://eprint.iacr.org/2026/808.pdf)


> **研究背景:** 安全比较是安全多方计算中频繁使用的基本构建块，尤其是在安全机器学习等应用中。现有的基于秘密共享的安全比较协议通常在吞吐量上优于门控电路，但历史上传统上具有更高的在线轮次复杂度。
>
> **主要贡献:** 作者提出了两种新的两轮安全比较协议：一种通过多扇区门实现的协议将在线位复杂度降低到$O(n \log n)$；另一种则通过优化乘法技术将离线位复杂度从$O(n^3)$减少到$O(n^2)$，但增加了在线位复杂度。
>
> **达到效果:** 这些新协议显著降低了安全比较所需的通信量，并且在某些情况下达到了与门控电路相当的两轮复杂度。特别是在带宽优化方面，第三种协议将在线位复杂度从$8n$降低到$6n$。
>
> **技术梗概:** 作者利用了“round absorption”技术以及针对乘法的新优化方法来减少通信量，并且采用了基于三叉树和四进制整数的框架。

---
### [2026/809] Formal Verification, Integration and Physical Evaluation of Prime-Field Masking on Silicon

- **作者:** Gaëtan Cassiers, Thorben Moos, Amir Moradi, Nicolai Müller, François-Xavier Standaert

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/809) | [PDF](https://eprint.iacr.org/2026/809.pdf)


> **研究背景:** 研究背景：在理论上和实践中，基于奇素数有限域的掩码技术已被证明能够增强电路对抗侧信道和故障攻击的能力。然而，缺乏兼容Fp算术的自动化验证工具以及常量时间生成均匀分布随机数的有效方法仍然是其应用和发展中的障碍。
>
> **主要贡献:** 主要贡献：本文通过形式化验证、安全集成并物理评估了基于小-p平方实例的小素数掩码实现，解决了上述障碍，并提供了首个针对更高阶掩码实现的ASIC和PCB制造案例研究。
>
> **达到效果:** 达到的效果：成功实现了对小素数掩码技术的安全验证与实际应用，展示了其在硬件上的可行性和有效性，为后续相关研究奠定了基础。
>
> **技术梗概:** 技术梗概：采用形式化方法验证了小素数掩码的实现，并通过定制化的PCB和ASIC制造进行了物理评估，确保了算法在实际硬件环境中的安全与性能。

---
### [2026/815] Non-Adaptive Programmable PRFs and Applications to Stacked Garbling

- **作者:** Vipul Goyal, David Heath, Abhishek Jain, Yibin Yang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/815) | [PDF](https://eprint.iacr.org/2026/815.pdf)


> **研究背景:** 非适应性可编程伪随机函数（napPRFs）与堆叠遮蔽方案之间的关系，以及如何基于单向函数实现高效的napPRFs以支持大规模输入场景。
>
> **主要贡献:** 提出了一个基于单向函数的堆叠遮蔽方案，该方案适用于大规模输入，并且其遮蔽大小仅与单一分支的大小及其输入长度成正比（至对数因子），同时包含分支数量的附加项。
>
> **达到效果:** 通过引入非适应性可编程伪随机函数（napPRFs）的概念，实现了在保持安全性和效率的同时支持更大规模输入的堆叠遮蔽技术。
>
> **技术梗概:** 利用SGC文献中的技术构建了满足所需效率的napPRFs，并在此基础上进一步优化了堆叠遮蔽方案以达到预期效果。

---
### [2026/816] From Rerandtopia to Interceptopia, the Anamorphic Encryption Saga Rises

- **作者:** Vincenzo Botta, Dario Catalano, Emanuele Giunta, Francesco Migliaro, Daniele Venturi, Ivan Visconti

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/816) | [PDF](https://eprint.iacr.org/2026/816.pdf)


> **研究背景:** 本文探讨了在政府可能滥用解密基础设施进行大规模监控的背景下，如何设计一种名为anamorphic加密方案以防止这种威胁。
>
> **主要贡献:** 作者提出了新的定义并在极端场景下提供了积极的结果，特别是在Rerandtopia和Interceptopia两种情景中。
>
> **达到效果:** 通过双层加密机制，该研究提出了一种可重新随机化的适应性选择明文攻击(CCA)安全方案，并在假设数量和效率上超越了现有技术。
>
> **技术梗概:** 该方案采用了两层加密结构，在特定实现下达到了超越当前最优的CCA安全性。

---
### [2026/821] A spectral approach to arithmetic correlations for binary FCSR sequences with prime connection integers

- **作者:** Feifei Yan, Pinhui Ke, Chenhuang Wu

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/821) | [PDF](https://eprint.iacr.org/2026/821.pdf)


> **研究背景:** 研究了反馈进位移位寄存器(FCSR)序列的算术相关性，特别是当连接整数为素数且$2$模$p$的阶为奇数时的情况。
>
> **主要贡献:** 提出了统一的谱方法来表达和分析此类FCSR序列的算术相关性，并推导了其上界及取得较小值的条件。
>
> **达到效果:** 通过该方法，确定了当连接整数$p$对应的陪集数量为2、4或6时，算术相关性取小值的情况。
>
> **技术梗概:** 利用谱分析技术，结合群论中的子群和陪集概念，精确计算并优化FCSR序列的算术相关性。

---
### [2026/822] Maliciously Secure Exact Fixed-Point Multiplication over Power-of-Two Rings for Replicated 3PC

- **作者:** Yutao Sun, Jianguo Xie, Guozhen Shi, Jiale Han, Huiyan Chen, Rongna Xie

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/822) | [PDF](https://eprint.iacr.org/2026/822.pdf)


> **研究背景:** 在诚实多数恶意安全3PC设置下，现有工作未能同时提供跨环兼容性、精确语义和恶意安全性。
>
> **主要贡献:** 作者提出了一种通用的商数校正框架，将复杂的非线性跨环操作简化为高效的2位有界商提取问题，并构建了首个满足所有上述要求的端到端精确定点乘法协议。
>
> **达到效果:** 通过该框架和标准同环乘法的组合，实现了在复制3PC设置下具有精确语义和恶意安全性的精确定点乘法协议。
>
> **技术梗概:** 作者利用统一的代数结构，提出了商数校正框架，并将其实例化为精确截断和扩展的具体方案。

---

## 更新: 2026-04-26 21:16

*新增 5 篇论文 (编号 797--801)*

### [推荐] [2026/798] Implementing CCZ Gates with Variation of Gate Teleportation for Quantum Homomorphic Encryption on NISQ Platform

- **匹配关键字:** homomorphic encryption

- **作者:** Gia Phat Dang, Weisheng Si, Belal Alsinglawi, Jim Basilakis

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/798) | [PDF](https://eprint.iacr.org/2026/798.pdf)


> **研究背景:** 针对分布式量子硬件服务主要由IBM、Google和AWS等量子提供商主导的问题，提出了量子同态加密（QHE）以确保在银行业、国防和医疗等行业中的数据安全。然而，由于电路复杂性和当前量子系统的噪声，部署QHE仍然具有挑战性。
>
> **主要贡献:** 本文通过结合VGT方案与CQC-QHE框架，实现了CCZ门的高效实现，从而支持7个量子比特和14次T-门操作，显著降低了计算成本并提高了资源利用率。
>
> **达到效果:** 实验结果表明，该方法能够在不引入大量错误的情况下支持更多的量子比特和更复杂的量子门操作，提升了QHE在NISQ平台上的实用性。
>
> **技术梗概:** 本文采用VGT方案对CCZ门进行变种实现，并结合Ortega等人提出的CQC-QHE框架，通过优化电路设计减少了计算资源的消耗。

---
### [推荐] [2026/799] EQuADiSE: Efficient Quantum-safe Adaptive Distributed Symmetric-key Encryption

- **匹配关键字:** post-quantum, LWR

- **作者:** Sayani Sinha, Sikhar Patranabis, Debdeep Mukhopadhyay

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/799) | [PDF](https://eprint.iacr.org/2026/799.pdf)


> **研究背景:** 分布式对称密钥加密(DiSE)允许传统对称密钥认证加密的阈值版本，其中长期主密钥在多个参与方之间秘密共享，并且加密和解密都是分布式的。然而，现有的适应性安全DiSE实例要么因依赖于离散对数难题组而量子脆弱，要么在线加密/解密开销呈指数增长。
>
> **主要贡献:** EQuADiSE是首个基于模块学习近似(MLWR)假设在量子随机预言模型(QROM)下的实用高效、适应性安全且可能后量子DiSE构造，其加密和解密开销为线性。此外，引入了具有QROM下适应性安全性的MLWR基分布式伪随机函数(DPRF)，在线评估时间表现优于现有所有适应性安全DPRF构造。
>
> **达到效果:** EQuADiSE在保持适应性安全性的同时实现了线性加密和解密开销，并且是首个实用高效的量子安全DiSE实例，显著提高了性能。
>
> **技术梗概:** 通过引入基于MLWR的分布式伪随机函数(DPRF)，EQuADiSE利用QROM下的适应性安全性技术，在不牺牲效率的情况下提供了适应性安全性保证。

---
### [2026/797] Factorisation-Based Multivariate Schemes: Structural Properties and New Constructions

- **作者:** Borja Gomez

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/797) | [PDF](https://eprint.iacr.org/2026/797.pdf)


> **研究背景:** 研究基于因子分解的多变量方案，特别是利用多项式环上的代数结构进行秘密因子分解作为陷阱门机制。
>
> **主要贡献:** 提出了一个通用性质：如果某个代数结构允许隐藏因子分解，则该性质可作为陷阱门原理。
>
> **达到效果:** 基于此方法，设计了两种方案：一种签名方案和一种加密方案。
>
> **技术梗概:** 通过分析多项式环上的秘密因子分解来构建陷阱门机制，并据此提出了具体的密码学构造。

---
### [2026/800] Deploying decryption oracles for fun and non-profit: Backing up with friends and TEEs

- **作者:** Kanav Gupta, Gabriel Kaptchuk, Ian Miers

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/800) | [PDF](https://eprint.iacr.org/2026/800.pdf)


> **研究背景:** 现有的安全备份系统未能将前向保密性和后妥协安全性作为首要设计约束，且部分方案依赖可信执行环境的PKI来提供安全，这在部署中存在关键风险。
>
> **主要贡献:** 提出了一种新颖、高效且简单的安全备份系统，通过定期轮换备份服务器并独立采样密钥材料来解决这些问题，并引入了社会密钥恢复机制以增强灵活性。
>
> **达到效果:** 该设计已被证明是安全的并通过基准测试表明其可部署性，能够在普通硬件上运行而无需WhatsApp或苹果加密备份所需的资源。
>
> **技术梗概:** 通过定期更换备份服务器并独立采样密钥材料来实现密钥轮换，并设计了一种静默备份过程以减少服务器负载。

---
### [2026/801] Outsourced Private Set Intersection for Pairwise Analytics

- **作者:** Ferran Alborch, Tangi De Kerdrel, Antonio Faonio, Melek Önen

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/801) | [PDF](https://eprint.iacr.org/2026/801.pdf)


> **研究背景:** 研究背景：在多方持有敏感数据并希望计算全局统计信息而不泄露其数据的情况下，隐私保护的数据分析变得尤为重要。本文关注的是跨多个数据集对成对元素的共同数量（交集的基数）进行计算的问题，确保仅披露最终汇总结果而不会泄露任何中间信息。
>
> **主要贡献:** 主要贡献：提出了一种新的密码学原语——外包计算的秘密共享输出私有集合交集（CaOPSI-SS），并基于此设计了一个协议来实现多对一的聚合分析，能够计算多个参与方间交集基数之和。
>
> **达到效果:** 达到的效果：通过应用该框架到实际场景中，实现了大型组织内不同子公司间的隐私保护邮件分析，能够在不泄露敏感人力资源数据的情况下进行细粒度查询。同时，通过扩展差分隐私机制进一步保护了个体记录的隐私。
>
> **技术梗概:** 技术梗概：利用伪随机函数和两个非协作服务器来卸载计算任务，使得该解决方案适用于资源异构环境，并展示了其在大规模数据集上的可扩展性和实用性。

---

## 更新: 2026-04-24 20:50

*新增 18 篇论文 (编号 778--796)*

### [推荐] [2026/778] Cobra: All-in-one for full-fledged defense — a hybrid nested KEM

- **匹配关键字:** post-quantum, LWE

- **作者:** Basker Palaniswamy, Paolo Palmieri, Ashok Kumar Das, Chun-I Fan

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/778) | [PDF](https://eprint.iacr.org/2026/778.pdf)


> **研究背景:** 针对后量子密码学（PQC）算法有限的破译历史，论文提出了一种混合嵌套KEM方案Cobra，以增强整体安全性。
>
> **主要贡献:** Cobra整合了FrodoKEM、ML-KEM、HQC和Dummy KEM四种不同的KEM机制，并分析了15种数学上独特的组合方法。
>
> **达到效果:** 通过市场理论安全框架（MTSF）证明所有Cobra方法均能达到IND-CCA2安全性，同时实现了约2^-127的后量子问价。
>
> **技术梗概:** 采用平行、级联、多阶段和嵌套拓扑结构，并通过定理7.1简化了部署选择至五个最优架构。

---
### [推荐] [2026/779] And TLS lived happily ever after

- **匹配关键字:** post-quantum

- **作者:** Michael Scott, Gora Adj, Francisco Rodríguez-Henríquez

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/779) | [PDF](https://eprint.iacr.org/2026/779.pdf)


> **研究背景:** 面对潜在的密码相关量子计算机(CRQC)威胁，研究转向了后量子安全的等价物以替代传统公钥加密方法。
>
> **主要贡献:** 提出了一种融合签名方案，该方案结合了经典和后量子签名技术，旨在保护现有TLS架构免受量子攻击。
>
> **达到效果:** 这种新的签名方案提高了数字证书的安全性，同时保持了与现有网络基础设施的兼容性。
>
> **技术梗概:** 通过在X.509证书链中使用双重签名方法来实现经典和后量子加密技术的融合。

---
### [推荐] [2026/781] Panther: Robust Hybrid KEM Combiners via Structural Splicing

- **匹配关键字:** post-quantum, LWE

- **作者:** Basker Palaniswamy, Paolo Palmieri, Ashok Kumar Das, Chun-I Fan

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/781) | [PDF](https://eprint.iacr.org/2026/781.pdf)


> **研究背景:** Panther旨在通过结合FrodoKEM（未结构化LWE）和ML-KEM（模块-LWE，FIPS 203），提供一种健壮的混合密钥封装机制（KEM）组合方案，确保在任一假设成立时均能保持IND-CCA2安全性。
>
> **主要贡献:** Panther贡献了六种健壮的组合器，并提出了一种新颖的结构拼接构造Panther-SS，该构造通过结构标签绑定分段位置，每个组合器都满足统一的健壯性谓词（传输绑定、领域分离、隐式拒绝、长度规范化和∨安全性）。
>
> **达到效果:** 实验结果表明，Panther组合器在多个方面优于NIST PQC轮次1-4中的密钥封装候选方案，包括生成/封装/解封延迟、吞吐量、内存占用、密文和密钥大小以及随查询数量的扩展性。
>
> **技术梗概:** Panther采用了市场理论安全框架证明方法，每个竞标回合都记录了其目的、替换的方案组件及其复杂度成本；该框架可扩展到正确性、无界会话安全性、QROM安全性及定量侧信道抗性。

---
### [推荐] [2026/783] Batch-Puncturing Circuit CP-ABE (and More) from Lattices

- **匹配关键字:** lattice, LWE

- **作者:** Yongkang Lang, Fangguo Zhang, Jianghong Wei, Xinyi Huang, Xiaofeng Chen

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/783) | [PDF](https://eprint.iacr.org/2026/783.pdf)


> **研究背景:** 现有的属性基加密（$\mathsf{PABE}$）方案仅支持逐个标签撤销，导致密钥大小随撤销的标签数量增加，这在需要频繁撤销或大规模撤销的情况下效率低下。
>
> **主要贡献:** 本文提出了一种电路属性基加密（$\mathsf{CPABE}$）方案，支持批量撤销多个标签，并且撤销后的密钥大小与撤销的标签数量和电路规模无关。
>
> **达到效果:** 该方案通过利用逃逸学习错误假设（$\mathsf{LWE}$）和张量$\mathsf{LWE}$假设实现，显著提高了撤销操作的效率和实用性。
>
> **技术梗概:** 本文采用了一种新颖的技术框架，结合了电路属性基加密与批量撤销机制，并通过数学假设确保了方案的安全性和高效性。

---
### [推荐] [2026/785] Neural Leakage–based Cryptanalysis of LowMC with Linear Complexity

- **匹配关键字:** post-quantum

- **作者:** Kwangjo Kim

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/785) | [PDF](https://eprint.iacr.org/2026/785.pdf)


> **研究背景:** 针对基于LowMC块密码的MPC-in-the-Head协议，现有分析假设了精确的布尔电路语义，但近期研究表明，分段线性实现可能会引入激活边界泄漏。
>
> **主要贡献:** 作者提出了一种基于扰动的探测方法，用于建模神经泄漏，并通过多数投票将轮密钥恢复简化为独立的二元假设检验。
>
> **达到效果:** 利用LowMC密钥调度的线性结构，首次展示了从第一轮密钥恢复到主密钥的攻击效率，证明了在所提模型下成功恢复128位、192位和256位密钥的可能性。
>
> **技术梗概:** 该研究采用了一种基于扰动的方法来建模神经泄漏，并通过多数投票将轮密钥恢复简化为独立的二元假设检验，从而揭示了分段线性实现可能带来的新维度攻击面。

---
### [推荐] [2026/790] Towards a Field-Informed Risk-Based Framework for PQC Migration in Legacy Systems

- **匹配关键字:** post-quantum

- **作者:** Paul CHAMMAS, Khalil HARISS, Carole BASSIL, Maroun CHAMOUN

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/790) | [PDF](https://eprint.iacr.org/2026/790.pdf)


> **研究背景:** 随着量子计算的进步，现代密码学面临巨大风险，尤其是对非对称和对称加密协议构成威胁。这促使全球网络安全社区启动了向后量子密码学(PQC)迁移的计划。然而，将传统系统迁移到量子安全密码学存在诸多挑战，包括硬件限制、技术陈旧以及监管约束等。
>
> **主要贡献:** 该研究提出了一个针对遗留系统的基于风险的PQC迁移框架，旨在解决上述问题，并强调了领域特定因素的重要性。
>
> **达到效果:** 通过该框架，研究人员能够更好地评估和管理传统系统向后量子密码学过渡的风险，为实际应用提供了更具体的操作指南。
>
> **技术梗概:** 研究采用了批判性审查现有标准和技术文献的方法，识别出关键限制并提出解决方案。

---
### [推荐] [2026/791] Experimental Validation of AUX scheme for Quantum Homomorphic Encryption on IBM Quantum Platforms

- **匹配关键字:** homomorphic encryption

- **作者:** Gia Phat Dang, Weisheng Si, Belal Alsinglawi, Jim Basilakis

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/791) | [PDF](https://eprint.iacr.org/2026/791.pdf)


> **研究背景:** 量子同态加密(QHE)旨在解决量子云计算(QCC)中的安全问题，确保客户端数据和算法在不可信的第三方量子服务器上的隐私性。然而，当前的QHE方案面临资源扩展带来的额外开销和硬件噪声问题，影响了准确性和安全性。
>
> **主要贡献:** 该研究实现了并分析了一个非交互式的AUX-QHE方案，利用预生成辅助态实现通用计算，并识别出三个关键瓶颈：辅助态数量指数增长、复杂的同态评估以及符号密钥的广泛更新。
>
> **达到效果:** 通过在IBM量子硬件上的实验评估，量化了NISQ噪声对AUX-QHE性能的影响，并确定了实际部署时所需的资源阈值，从而弥合了理论QHE框架与在嘈杂量子设备上实现之间的差距，为未来的降噪努力提供了具体的基准。
>
> **技术梗概:** 研究采用了预生成辅助态的方法来处理通用计算问题，并通过实验评估技术来量化噪声影响和确定实际部署的资源限制。

---
### [推荐] [2026/792] Equivocal Broadcast Encryption: Adaptively-Secure Optimal Distributed Broadcast Encryption from Lattices

- **匹配关键字:** lattice

- **作者:** Rishab Goyal, Saikumar Yadugiri

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/792) | [PDF](https://eprint.iacr.org/2026/792.pdf)


> **研究背景:** 本文提出了首个基于可验证格假设的分布式广播加密(DBE)方案，实现了适应性安全性和最优参数设置。
>
> **主要贡献:** 该研究引入了一种新的证明适应性安全性的方法：等价加密系统(Equivocal Encryption Systems)，并在此基础上构建了DBE方案。
>
> **达到效果:** 该方案在随机预言模型中具有简洁的公共参考字符串(CRS)，或在标准模型中具有较长的CRS，同时实现了适应性和最优参数设置。
>
> **技术梗概:** 通过引入等价加密系统框架，在两种不可区分模式下工作：真实模式使用标准算法和伪造模式下联合采样密钥和密文以动态地将密文与挑战值等价。

---
### [推荐] [2026/793] Oriole: Adaptively Secure Partially Non-Interactive Threshold Signatures from Lattices

- **匹配关键字:** lattice, LWE

- **作者:** Kaijie Jiang, Hoeteck Wee, Chenzhi Zhu

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/793) | [PDF](https://eprint.iacr.org/2026/793.pdf)


> **研究背景:** 本文提出了一种基于格的、适应性安全的部分非交互式门限签名方案，能够在最多$T-1$个签署者被适应性篡改的情况下保持安全性。
>
> **主要贡献:** 该方案在MSIS和MLWE假设下构建，并且只需要两轮通信，其中第二轮依赖消息。
>
> **达到效果:** 相比之前的适应性安全格基方案，本文的工作减少了通信轮次并提高了通信效率。
>
> **技术梗概:** 通过巧妙地设计签名协议的两轮通信机制，实现了在保持安全性的同时减少通信复杂度的目标。

---
### [2026/780] Montgomery Multiplication in Signed Redundant Representations

- **作者:** Thomas Pornin

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/780) | [PDF](https://eprint.iacr.org/2026/780.pdf)


> **研究背景:** 本文探讨了在带有符号缩减因子的多部件冗余表示整数中使用蒙哥马利乘法的技术，特别适用于缺乏硬件进位传播支持的RISC-V等处理器平台。
>
> **主要贡献:** 作者开发了一种技术，通过利用无缩减部件级加减操作来优化实现，并展示了如何进行整个原语范围分析以证明溢出不可行。
>
> **达到效果:** 该方法实现了对NIST P-256曲线的ECDSA签名验证的小型化实现，在x86处理器上仅需848字节，RISC-V为984字节，Armv8-A为1136字节，并提供了可移植C语言实现。
>
> **技术梗概:** 通过使用虚拟CPU和自定义指令集（“字节码”）来优化加减操作的大小，同时保持计算效率。

---
### [2026/782] Failure of proximity gaps close to capacity

- **作者:** Dmitry Krachun, Stepan Kazanin, Ulrich Haböck

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/782) | [PDF](https://eprint.iacr.org/2026/782.pdf)


> **研究背景:** 研究背景：本文探讨了Reed--Solomon码在极大相对距离附近的行为，特别是关于其接近性间隙是否存在的问题。
>
> **主要贡献:** 主要贡献在于提供了一个简单的反例，证明对于乘法子群上的Reed--Solomon码，在容量附近的接近性间隙假设可能不成立。
>
> **达到效果:** 达到的效果是，当相对距离为$\theta = 1-\rho-\eta$时，构造了一条包含多项足够接近于代码的点的仿射线，并且这些点的数量与$\eta$呈反比关系。
>
> **技术梗概:** 技术梗概：证明使用了关于单位根和加法组合的新引理来构建反例。

---
### [2026/784] Secure and Updatable Single Password Authentication

- **作者:** Devriş İŞLER, HamidReza Saadi Dadmarzi, Alptekin Küpçü

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/784) | [PDF](https://eprint.iacr.org/2026/784.pdf)


> **研究背景:** 尽管密码存在诸如离线字典攻击和密码重用等弱点，单密码认证(Single Password Authentication, SPA)通过在可信赖的存储提供商之间保护高熵秘密来减轻这些风险。然而，现有方案无法防止存储提供商发起的预篡改和覆盖攻击，并且缺乏安全高效的秘钥和密码更新机制。
>
> **主要贡献:** $\protocol$ 提出了一种高效、安全且可更新的门限单密码认证方案，解决了上述问题，无需对登录服务器进行更改。
>
> **达到效果:** 该方案通过存储提供商特定的高熵标识秘密防止预篡改攻击，并支持通过隐式认证实现秘钥更新以及使用密码保护签名密钥进行显式认证以实现密码更新。证明了在理想现实范式下的安全性，包括抵抗标准静态门限假设下的离线字典攻击。
>
> **技术梗概:** 该方案采用了高熵标识秘密、隐式和显式认证机制，并通过形式化证明确保了安全性和效率。

---
### [2026/786] Integral Resistance and Degree Bounds for Complex Linear Layers: Application to PRINCE and Lower-Latency Alternatives

- **作者:** Simon Gerhalter, Maria Eichlseder

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/786) | [PDF](https://eprint.iacr.org/2026/786.pdf)


> **研究背景:** 研究旨在通过引入通用框架和工具intres，扩展并应用于具有复杂线性层的密码体制，以验证其抵抗积分区分器的能力。
>
> **主要贡献:** 贡献包括提出一种通用框架intres，并开发了度传播模型来确定有效密钥掩码，从而为Rijndael-256提供了更紧致的上界估计。
>
> **达到效果:** 结果是成功证明了PRINCE 7轮和Beanie 6轮的积分抵抗性，并通过MILP方法提出了具有更低延迟替代方案的MixColumns矩阵，同时保持了积分抵抗性。
>
> **技术梗概:** 技术包括使用intres框架进行度传播分析以确定有效密钥掩码，并结合SAT求解器验证新矩阵的有效性。

---
### [2026/787] Efficient Construction of Threshold BBS+ Signatures and its Extensions

- **作者:** Yang Heng, Mengling Liu, Xingye Lu, Haiyang Xue, Zijian Bao, Man Ho Au

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/787) | [PDF](https://eprint.iacr.org/2026/787.pdf)


> **研究背景:** BBS+签名广泛应用于保护隐私的系统中，如匿名凭证和直接匿名认证(DAA)，但现有方案存在显著的效率问题。
>
> **主要贡献:** 提出了一种基于Castagnos–Laguillaumie（CL）密码系统的三轮门限BBS+签名方案，并扩展了该技术以涵盖门限BBS签名、Dodis-Yampolskiy可验证随机函数(DY VRF)和乘法协议。
>
> **达到效果:** 与现有四轮方案相比，新方案在通信量上减少了77.4%，计算速度提高了10.6至16.6倍，在多线程环境下提升了3.3至5.4倍。此外，还实现了门限BBS签名、DY VRF和乘法协议的两轮或三轮方案。
>
> **技术梗概:** 采用了基于CL密码系统的创新方法来优化通信效率与计算性能之间的平衡。

---
### [2026/788] Secret-Carrying Puzzles and Garbled Circuits Optimized for Zero-knowledge Proofs

- **作者:** Debasish Ray Chawdhuri, Manoj Prabhakaran

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/788) | [PDF](https://eprint.iacr.org/2026/788.pdf)


> **研究背景:** 本文提出了Obliviously Checkable Secret-Carrying Puzzles (OxSP)的概念，并构建了证明友好的Garbled Circuits (GC)，以实现其实用化。
>
> **主要贡献:** 主要贡献在于设计了一种新的证明友好的GC构造，使得生成正确编译的证明成本降低了近三分之一，无需依赖非标准密码学假设。
>
> **达到效果:** 这一技术不仅适用于OxSP，还为可审计的安全多方计算提供了一个重要的工具。
>
> **技术梗概:** 通过优化Garbled Circuits和ZK-SNARKs的结合使用，显著减少了生成正确编译证明的成本。

---
### [2026/794] sigma-rs: A Modular Approach for Keyed-Verification Anonymous Credentials

- **作者:** Michele Orru, Lindsey Tulloch, Victor Snyder-Graf, Ian Goldberg

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/794) | [PDF](https://eprint.iacr.org/2026/794.pdf)


> **研究背景:** sigma-rs旨在简化基于现代匿名凭证系统的协议的构建和部署，通过模块化设计降低加密复杂性。
>
> **主要贡献:** 该工具包通过分层设计抽象了复杂的密码学操作，并支持多种凭证方案、证明方法及访问策略。
>
> **达到效果:** 通过重新实现Tor的Lox桥分布协议以及用户认证机制，展示了其实用性和灵活性。
>
> **技术梗概:** sigma-rs利用类型安全、领域分离和证明者状态纪律来增强误用抵抗性，并采用侧信道意识的常量时间策略。

---
### [2026/795] On the Decoding Failure Rate of HQC

- **作者:** Alessandro Annechini, Alessandro Barenghi, Gerardo Pelosi

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/795) | [PDF](https://eprint.iacr.org/2026/795.pdf)


> **研究背景:** 基于纠错码的密码学因其对抗经典和量子攻击的能力而受到广泛关注。HQC作为一种Hamming准循环（Quasi-Cyclic, QC）编码的密钥封装机制被选为标准候选方案，但其解码失败率可能泄露私钥信息。
>
> **主要贡献:** 本文推导了无独立性假设下的新的HQC解码失败率闭式模型，并证明了原有近似保守且当前的解码失败率低于所需水平。
>
> **达到效果:** 通过优化技术，本文展示了可以在不牺牲安全性的情况下减小HQC公钥和密文的大小。
>
> **技术梗概:** 采用概率模型推导新的解码失败率公式，并利用此模型进行参数调整以提高安全性。

---
### [2026/796] Masking Ordering Failures in BFT SMR via Proactive Pre-Commit Execution

- **作者:** Jianting Zhang, Alberto Sonnino, Lefteris Kokoris-Kogias, Aniket Kate

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/796) | [PDF](https://eprint.iacr.org/2026/796.pdf)


> **研究背景:** 现代拜占庭容错状态机复制（BFT SMR）系统通过解耦的BFT共识过程分离数据传播和事务排序，以实现即使在部分同步下排序过程偶尔停滞时仍能高效异步传播。然而，这可能导致交易确认延迟增加，因为执行过程需要等待排序过程完成。
>
> **主要贡献:** Pufferfish是首个有效掩盖实践中间断性排序失败的BFT SMR系统，通过引入预提交执行方案，允许副本在排序过程中停滞时推测性地执行事务，并在排序问题解决后直接提交这些结果。
>
> **达到效果:** 评估结果显示，Pufferfish能够在地理分布的AWS环境中实现更快的交易确认速度和更低的延迟。
>
> **技术梗概:** Pufferfish基于有向无环图（DAG）的BFT共识协议构建了自适应概率推测机制，并采用了解决推测失败时最小化事务重执行开销的提交感知快照机制。

---

## 更新: 2026-04-23 19:48

*新增 10 篇论文 (编号 767--777)*

### [推荐] [2026/767] Cryptanalysis of the Sharafi–Daghigh digital signature scheme

- **匹配关键字:** LWE

- **作者:** Nour-eddine Rahmani, Taoufik Serraj, Abdelmalek Azizi

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/767) | [PDF](https://eprint.iacr.org/2026/767.pdf)


> **研究背景:** 该研究旨在分析Sharafi和Daghigh提出的基于Ring-LWE的数字签名方案的安全性，该方案借鉴了Lindner–Peikert加密范式，并采用Fiat–Shamir变换的哈希签名方法。
>
> **主要贡献:** 作者通过证明该方案不安全并将其分析推广到plain-LWE设置下的类似方案，揭示了其潜在的安全漏洞。
>
> **达到效果:** 研究结果表明Sharafi和Daghigh的签名方案在理论和实际应用中均存在安全隐患，不能依赖于Ring LWE和Ring-SIS问题的假设难度来保证安全性。
>
> **技术梗概:** 采用密码分析技术对方案进行深入研究，并通过构造特定实例展示了其脆弱性。

---
### [推荐] [2026/768] Towards More Efficient Registration-Based Encryption from LWE

- **匹配关键字:** post-quantum, LWE

- **作者:** Toi Tomita

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/768) | [PDF](https://eprint.iacr.org/2026/768.pdf)


> **研究背景:** 现有后量子注册加密方案因密文大小过大而难以大规模实施，这限制了其在社会中的应用。
>
> **主要贡献:** 作者提出了一种基于LWE假设的高效RBE构造框架，并引入了可分解精简加密技术。
>
> **达到效果:** 该方案即使用户数量增加到$2^{10}$时，密文大小仍保持在约221MB左右。
>
> **技术梗概:** 通过结合可分解精简加密和改进的快照技巧来实现高效性。

---
### [推荐] [2026/772] Lattice-based Ring Verifiable Random Functions

- **匹配关键字:** lattice, post-quantum

- **作者:** Jie Xu, Muhammed F. Esgin, Ron Steinfeld

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/772) | [PDF](https://eprint.iacr.org/2026/772.pdf)


> **研究背景:** Verifiable Random Functions (VRFs)在去中心化协议中广泛应用，但标准的VRF验证会泄露签名者的身份，这使得他们容易受到针对性攻击。
>
> **主要贡献:** 研究提出了Ring VRFs（RVRFs），允许环中的成员发布与输入和秘密密钥相关联的可验证伪随机值，并隐藏其在环内的索引位置。
>
> **达到效果:** 通过设计一个综合的安全概念框架，包括正确性、匿名性、伪随机性和新颖的抗篡改唯一性($T$-uniqueness)，实现了对匿名环境下的可验证随机性的全面保护。
>
> **技术梗概:** 提出了一种模块化编译器，将任何证明VRF转换为RVRF，通过在随机预言机模型中使用优化后的Fiat-Shamir OR (FS-OR)组合实现后量子安全。

---
### [推荐] [2026/777] How Strong is the FO-Calypse, Really? Instantiating Plaintext-Checking Oracles against Masked Software Implementations of ML-KEM

- **匹配关键字:** lattice

- **作者:** Brieuc Balon, Gaëtan Cassiers, Thibaud Schoenauen, François-Xavier Standaert

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/777) | [PDF](https://eprint.iacr.org/2026/777.pdf)


> **研究背景:** 研究背景：针对基于ML-KEM的软件实现中的明文检查预言机（PCO）侧信道攻击已有广泛研究，但较少关注如何在实际掩码实现中有效利用这些预言机。
>
> **主要贡献:** 主要贡献：系统地对三种开源Keccak函数的掩码软件实现进行了PCO实例化，并提出了一个简单、具体且可重用的Keccak掩码实现模型。
>
> **达到效果:** 达到的效果：通过状态最前沿的攻击方法，成功利用了多达7份额码的高准确性泄漏信息，证实了“计算更多意味着泄露更多”的说法，并表明在这些平台上实施高级安全级别将不可行。
>
> **技术梗概:** 技术梗概：使用ARM Cortex-M4平台进行基于最新攻击技术的定量评估，结合不同掩码技术和编程风格实现PCO实例化。

---
### [2026/769] High-Order Masking for MQOM v2.1 Signing

- **作者:** Yi-Lin Hung, Jiun-Peng Chen, Ho-Lin Chen, Bo-Yin Yang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/769) | [PDF](https://eprint.iacr.org/2026/769.pdf)


> **研究背景:** 该研究旨在为NIST额外数字签名标准化过程中的MQOM v2.1候选算法提供首个高阶完全共享掩码构造，以提高其安全性并优化性能。
>
> **主要贡献:** 贡献在于提出了基于标准探针泄漏模型的基线高阶掩码签名设计，并引入了基于Rijndael LUT的加速模式来缓解在线时间瓶颈。
>
> **达到效果:** 研究结果表明，虽然加速模式增加了离线时间和内存成本，但显著减少了在线签名延迟；全面评估了36种MQOM v2.1签名变体在GF(2)、GF(16)和GF(256)上的性能和泄漏情况。
>
> **技术梗概:** 技术上采用了高阶掩码技术和Rijndael查找表来优化签名过程，确保安全性和效率的平衡。

---
### [2026/770] Cryptanalysis of Hecke-KE: A Linear-Algebra Attack via Hecke Eigenbasis Decomposition

- **作者:** Xiyao Chen

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/770) | [PDF](https://eprint.iacr.org/2026/770.pdf)


> **研究背景:** 本文针对Hecke-KE密钥交换方案提出了一种被动攻击方法，该方案利用Hecke算子在$S_k(\Gamma_0(N))$上的乘积作为单向函数。
>
> **主要贡献:** 作者证明了Hecke代数在任何固定的空间$S_k(\Gamma_0(N))$上可以同时对角化，并将共享密钥恢复归结为$d$次标量除法运算，其中$d=\dim S_k(\Gamma_0(N))$。
>
> **达到效果:** 通过预计算Hecke算子的特征基，攻击者可以在每次会话中仅需$O(d^2)$次数域操作来恢复共享密钥，验证结果表明该方法在SageMath 10.7上对所有参数集均有效。
>
> **技术梗概:** 技术上，通过分解Hecke算子的作用空间并利用特征基进行线性代数攻击，将复杂的密钥恢复问题简化为标量除法运算。

---
### [2026/771] Vector-Input Hashing Modes for Collision-Resistant Pseudorandom Function

- **作者:** Shoichi Hirose, Tetsu Iwata, Hidenori Kuwakado

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/771) | [PDF](https://eprint.iacr.org/2026/771.pdf)


> **研究背景:** 该研究旨在通过使用密钥哈希函数构建抗冲突伪随机函数（CR PRF），解决现有字符串输入模式在处理向量输入时的局限性。
>
> **主要贡献:** 提出了一种新的向量输入密钥哈希模式VIM1和VIM2，以及一种并行处理向量中字符串的模式PVIM。
>
> **达到效果:** 通过结合最近提出的KHC1或KHC2模式，证明了在满足扩展抗冲突性和相关密钥攻击下为安全伪随机函数的压缩函数的基础上，可以构建CR PRFs。
>
> **技术梗概:** 该研究通过替换压缩函数来实现向量输入，并利用现有的字符串输入模式进行优化，从而提高效率和安全性。

---
### [2026/774] Provably Secure Hybrid Inner Product and Boolean Masking via Composable Conversion

- **作者:** Jaeseung Han, Dong-Guk Han

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/774) | [PDF](https://eprint.iacr.org/2026/774.pdf)


> **研究背景:** 文章针对掩码技术中的布尔掩码（BM）和内积掩码（IPM）的安全性进行了研究，旨在解决现有方案在实现高安全级别时面临的挑战。
>
> **主要贡献:** 作者提出了BM到IPM及IPM到BM的转换机制，并优化了内积乘法器，实现了两个掩码域之间的可组合且证明安全的互操作。
>
> **达到效果:** 通过这些贡献，文章成功地减少了随机比特的需求量并提高了效率，同时保持了所需的安全级别。
>
> **技术梗概:** 采用行打包和行列减少技术优化了IPM乘法器，并设计了混合IPM-BM框架以实现高效安全的线性操作处理。

---
### [2026/775] Differential and Linear Cryptanalysis of Modular Addition

- **作者:** Halil İbrahim Kaplan, Ali Doğan, Gökçe Yetişer

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/775) | [PDF](https://eprint.iacr.org/2026/775.pdf)


> **研究背景:** 本文从密码分析的角度全面分析了模加操作，探讨了进位比特的概率分布及其对线性逼近的影响。
>
> **主要贡献:** 作者提出了构造模加操作的线性逼近表（LAT）和差分分布表（DDT）的具体算法，并提供了理论证明和实际案例。
>
> **达到效果:** 研究揭示了随着位位置增加，进位比特的概率接近1/2，这对线性密码分析的有效性产生了显著影响。
>
> **技术梗概:** 通过利用较小的表格和进位比特关系来扩展大尺寸差分分布表（DDT），作者展示了如何构建适用于更大位数模加操作的算法。

---
### [2026/776] SCOUT-CT: Sound Constant-Time Outcome with Uncertainty Tracking using multi-taint analysis

- **作者:** Damien Maier, Jean-François Pasche, Maxim Golay, Alexandre Duc

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/776) | [PDF](https://eprint.iacr.org/2026/776.pdf)


> **研究背景:** 侧信道攻击是一种重要的安全威胁，通过观察系统无意中泄露的信息来获取敏感数据。编写常量时间代码是防止基于时间和微体系结构侧信道攻击的常见防御措施。
>
> **主要贡献:** 本文提出了一种新颖的声音分析方法，用于在常量时间模型下检测信息泄露，并通过系统跟踪精度损失来确定检测到的信息泄露是否由过度近似引起。
>
> **达到效果:** 该技术能够直接对二进制可执行文件进行分析，减少手动检查的需要，并保证未检测到精度损失的确认发现的真实性。
>
> **技术梗概:** 本文的方法通过多污点分析系统地跟踪精度损失，以确定检测到的信息泄露是否由过度近似引起，并仅需对检测到精度损失的发现进行传统的人工验证。

---

## 更新: 2026-04-22 20:27

*新增 23 篇论文 (编号 742--766)*

### [推荐] [2026/742] Efficient and Post-Quantum Conjunctive Dynamic SSE with Strong Privacy Guarantees

- **匹配关键字:** lattice, post-quantum

- **作者:** Bibhas Chandra Das, Nilanjan Datta, Avijit Dutta, Avishek Majumder, Debdeep Mukhopadhyay, Sikhar Patranabis, Subhabrata  Samajder, Laltu Sardar

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/742) | [PDF](https://eprint.iacr.org/2026/742.pdf)


> **研究背景:** 现有高效的动态可搜索对称加密(DSSE)方案大多无法同时满足前向和后向隐私，或者通信开销过大、客户端计算负担过重。此外，所有已知的兼具前向和后向隐私的DSSE方案在量子攻击下均不安全。
>
> **主要贡献:** 作者提出了首个系统化的联合查询后向隐私定义，并设计了一种名为fp-GA-ODXT的新框架，该框架同时实现了全面的前向隐私和强大的后向隐私保证，且具有较小的客户端计算开销和低通信成本。
>
> **达到效果:** 实验结果表明，与现有方案相比，该方案在保持高效的同时显著增强了隐私保护能力，并且通信量和客户端计算负担得到了有效控制。
>
> **技术梗概:** 通过引入新的理论框架和改进的协议设计，作者解决了前向和后向隐私之间的冲突问题，在不牺牲性能的前提下实现了更强的安全性。

---
### [推荐] [2026/744] SPARQ: Scalable Privacy-preserving Aggregate Range Queries

- **匹配关键字:** homomorphic encryption

- **作者:** Mahdieh Heidaripour, Maryam Rezapour, Benjamin Fuller, Hoda Maleki, Gagan Agrawal

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/744) | [PDF](https://eprint.iacr.org/2026/744.pdf)


> **研究背景:** 现有方法在多维数组数据上执行关联聚合查询时存在显著限制，包括存储大小与总域大小成正比或最坏情况下的线性时间搜索。此外，基于桶的方法仅适用于最大桶较小的情况，而全同态加密方法则因计算成本过高而不切实际。
>
> **主要贡献:** 研究提出了SPARQ（可扩展隐私保护聚合范围查询），通过使用秘密分段树实现高效存储和搜索，达到了多项式对数的查询复杂度，并在典型数据分布下证明了其长度短于标准替代方案。
>
> **达到效果:** 在具有1-3个维度且最多包含500万条记录的数据集上进行评估时，与非FHE方法相比，该方法减少了存储项的数量达10倍至十亿倍。服务器端查询处理时间保持在合理范围内。
>
> **技术梗概:** SPARQ 使用秘密分段树技术，在保证隐私的同时实现了高效的数据检索和聚合操作，避免了传统方法的存储和搜索瓶颈问题。

---
### [推荐] [2026/763] LEAH: Lightweight and Efficient Hardware Accelerator for Code-based PQC Scheme HQC

- **匹配关键字:** post-quantum

- **作者:** Yazheng Tu, Jiafeng Xie

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/763) | [PDF](https://eprint.iacr.org/2026/763.pdf)


> **研究背景:** 量子计算的发展对现代密码学构成了重大威胁，为此，美国国家标准与技术研究院（NIST）启动了后量子密码学（PQC）标准化进程。在这一背景下，本文提出了一种针对HQC方案的轻量高效硬件加速器LEAH。
>
> **主要贡献:** 本文的主要贡献包括：设计专用流程以优化HQC的关键组件；创新数据流布局支持所有参数集的操作阶段；以及FPGA实现结果表明，与现有解决方案相比，在等效面积延迟积（EADP）方面至少节省了13.66%至最多49.87%。
>
> **达到效果:** 通过LEAH的设计，本文实现了HQC方案在不同安全级别下的高效硬件加速，并且在FPGA实现中展示了显著的效率提升。
>
> **技术梗概:** LEAH采用了针对稀疏多项式乘法器、采样器、编码器和解码器等关键组件的高度优化设计；并创新地安排了数据流以支持HQC的所有操作阶段。

---
### [推荐] [2026/764] CEDAR: A Compact and Efficient Decoder Architecture for RS-RM Code in HQC

- **匹配关键字:** post-quantum

- **作者:** Yazheng Tu, Tianyou Bao, Jiafeng Xie

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/764) | [PDF](https://eprint.iacr.org/2026/764.pdf)


> **研究背景:** 随着量子计算的快速发展，后量子密码学(PQC)成为研究热点，旨在开发能够抵御量子攻击的新算法。HQC作为最新的PQC方案之一，在硬件加速方面尚未得到充分研究。
>
> **主要贡献:** 本文提出了CEDAR架构，包括优化的RM解码器、高效的低复杂度RS解码器以及完整的HQC解码器实现，并展示了其性能优势。
>
> **达到效果:** 通过设计CEDAR架构，该研究显著提升了HQC在硬件加速方面的效率，并为NIST PQC标准化进程提供了有力支持。
>
> **技术梗概:** 采用多层次优化策略，包括算法层面和结构层面的改进，以降低解码复杂度并提高解码速度。

---
### [2026/743] Improved Rate for Non-Malleable Codes and Time-Lock Puzzles

- **作者:** Cody Freitag, Ilan Komargodski, Manu Kondapaneni, Jad Silbak

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/743) | [PDF](https://eprint.iacr.org/2026/743.pdf)


> **研究背景:** 非可塑编码允许发送者向接收者传输消息，同时提供一种最佳的完整性保证，确保攻击者（无法解码原始信息）不能篡改消息。
>
> **主要贡献:** 研究提出了新的技术，用于构建具有改进率的非可塑编码和时间锁谜题。
>
> **达到效果:** 通过这些技术，实现了率1的CCA隐藏时间锁谜题，并在辅助输入随机预言模型中实现了率1的非可塑编码。
>
> **技术梗概:** 研究识别了一种新的安全性概念——'CCA隐藏'，并将其应用于构建高效的非可塑编码和时间锁谜题。

---
### [2026/745] Round-Optimal Privacy Preserving Authenticated Key Exchange Even for Incomplete Sessions

- **作者:** Xavier Bultel, Khouredia Cisse

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/745) | [PDF](https://eprint.iacr.org/2026/745.pdf)


> **研究背景:** 该研究针对现代应用中使用的高效Noise-like隐式认证密钥交换协议，这些协议仅需少量的指数运算和两次交互。
>
> **主要贡献:** 作者提出了一种高效的Noise-like协议，能够在中断会话的情况下仍保持隐私性，并且在交互次数上达到最优。
>
> **达到效果:** 该协议不仅实现了与非隐私保护协议相当的效率，还在理论安全性假设上有所改进，同时提供了更强的隐私保证。
>
> **技术梗概:** 研究采用了新的安全模型来定义强隐私属性，并设计了一种基于CDH假设的新协议以优化交互次数和计算成本。

---
### [2026/747] MDSS-STAR: Private Heavy-Hitters through Multi-Dealer Secret Sharing

- **作者:** Harry Eldridge, Aditya Hegde, Brennon Brimhall, Gabrielle Beck, Matthew Green

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/747) | [PDF](https://eprint.iacr.org/2026/747.pdf)


> **研究背景:** 本文提出了一种新的私有遥测系统，用于在STAR和POPSTAR模型下计算t-重击者。该系统通过轻量级随机性服务器协助客户端生成报告并提交给中心聚合服务器来实现隐私保护。
>
> **主要贡献:** 与STAR和POPSTAR相比，该协议减少了泄漏：聚合服务器仅在频率超过预定义阈值时才学习非重击者的值，并且能够抵御聚合服务器与客户端共谋的安全威胁。
>
> **达到效果:** 通过将多重经销商秘密共享技术适应到STAR/POPSTAR模型并引入新型的盲秘密份额抽样协议，该协议实现了这些隐私保证。实验表明其在多种应用场景中是可行的，并支持可调的正确性、效率和隐私之间的权衡。
>
> **技术梗概:** 本文采用了多重经销商秘密共享（MDSS）技术来适应STAR/POPSTAR模型，并引入了新型的盲秘密份额抽样协议以确保对抗共谋聚合服务器的安全性。

---
### [2026/748] Related-Key Multi-Pair Neural Distinguishers: Analysis and Applications to Lightweight Block Ciphers

- **作者:** Thanh-Phong Nguyen, Nguyen Tan Cam, Thanh-Hien Vu, Van-Than Huynh, Hieu-Minh Nguyen

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/748) | [PDF](https://eprint.iacr.org/2026/748.pdf)


> **研究背景:** 研究了神经差分密码分析在相关密钥和多对设置下的扩展，通过聚合多个密文对的微弱统计偏差来增强攻击效果。
>
> **主要贡献:** 提出了基于信号中心的方法，分析了四个轻量级块密码（PRESENT-80, SIMECK-32/64, LEA-128, HIGHT）的相关密钥、多对神经区别的性能。
>
> **达到效果:** 结果表明，多对聚合可以增强弱统计偏差的可区分性，但随着轮数增加，信号逐渐衰减，导致区分能力边界清晰。
>
> **技术梗概:** 使用独立于模型的几何度量（如PCA嵌入和轮廓评分）来表征密文分布，并关联这些数据级测量与在不同聚合水平下的神经区别的性能。

---
### [2026/749] Divide-and-Pair: Faster subgroup membership testing for elliptic curves

- **作者:** Yu Dai, Youssef El Housni, Dimitri Koshelev, Krijn Reijnders

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/749) | [PDF](https://eprint.iacr.org/2026/749.pdf)


> **研究背景:** 在椭圆曲线上进行子群成员身份测试（SMT）对于防止小子群攻击至关重要，尤其是在具有非平凡陪数的曲线中。现有方法包括Pornin的方法和Koshelev的方法，但两者各有局限。
>
> **主要贡献:** 本文提出了一种新的方法Divide-and-Pair，它在分拆和配对之间进行权衡，能够在多种情况下比原有方法更快。
>
> **达到效果:** 该方法被应用于五种广泛使用的曲线，并实现了显著的速度提升，尤其是在Curve25519、Curve448、GC256A、Four$\mathbb{Q}$ 和 JubJub 曲线上。
>
> **技术梗概:** Divide-and-Pair 方法通过结合使用分拆和配对技术来优化SMT过程，在不需要非退化条件的情况下提高了效率。

---
### [2026/750] MCU: Exact and Constant-Round Nonlinear Function Evaluation in MPC without Preprocessing

- **作者:** Min Yang, Jinxuan Du, Zihang Zhou, Dongcan Guo, Qingshu Meng

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/750) | [PDF](https://eprint.iacr.org/2026/750.pdf)


> **研究背景:** 随着人工智能应用的迅速增长，特别是大规模语言模型和深度神经网络的发展，对大量训练数据的需求激增，引发了隐私保护问题。现有的安全多方计算（MPC）系统虽然有效但效率低下且难以扩展，尤其是在处理现代基于Transformer的大规模参数模型时需要大量的预处理工作量。
>
> **主要贡献:** 本文提出了一种名为MCU的新颖MPC架构，能够在无需任何预处理的情况下直接支持广泛的非线性函数。该方法通过引入半诚实的辅助计算方来实现这一目标，显著减少了隐私泄露风险并提高了效率。
>
> **达到效果:** MCU架构能够以精确且常数轮次的方式执行非线性函数计算，并且在不牺牲安全性的前提下大幅提升了性能和可扩展性。
>
> **技术梗概:** MCU通过输入加掩码、辅助方进行计算以及输出解掩码的流程，实现了非线性函数的有效计算，同时保持了协议的安全性和效率。

---
### [2026/751] LigeSIS: Distribution-friendly Polynomial Commitment \\ Based on Error-correcting Code

- **作者:** Yanpei Guo, Hancheng Lou, Wenjie Qu, Zhuoyuan Xu, Jiaheng Zhang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/751) | [PDF](https://eprint.iacr.org/2026/751.pdf)


> **研究背景:** 多项式承诺方案（PCS）是现代证明系统的基本构建块。随着证明系统应用的工作负载增大，分布式PCS变得至关重要，以减少证明者的时间和内存压力。
>
> **主要贡献:** 本文提出了LigeSIS，这是首个分布友好的基于纠错码的多线性PCS。
>
> **达到效果:** LigeSIS实现了跨节点通信量的亚线性增长，并保持最终证明大小与机器数量无关。在分布式设置中，LigeSIS在证明者时间上表现出接近线性的可扩展性。
>
> **技术梗概:** 通过用Goldilocks64上的同态子集和哈希替换梅克尔树哈希，LigeSIS实现了部分承诺的代数聚合，并引入了预处理加速的子集和哈希以减少哈希开销。

---
### [2026/752] GlitchSnipe: Toward Localized Voltage Fault Attacks

- **作者:** Fatemeh Khojasteh Dana, Saleh Khalaj Monfared, Hamed Okhravi, Shahin Tajik

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/752) | [PDF](https://eprint.iacr.org/2026/752.pdf)


> **研究背景:** 电压故障注入技术因其有效性和简单性而广受关注，尽管通常认为其影响是全局性的，但研究发现特定位置可能受到更大影响。
>
> **主要贡献:** 作者提出了GlitchSnipe方法，通过分析电压瞬变的频域特性并将其视为通过电源分配网络（PDN）传播的传导电磁能量来建模，从而实现局部故障注入。
>
> **达到效果:** 该方法能够识别系统PDN最脆弱的频率范围，并确定每个频率分量影响的芯片区域，验证了局部故障注入的可能性。
>
> **技术梗概:** 通过使用分布式时间-数字转换器（TDC）对多个FPGA进行详尽分析，作者提出了一种后硅探测框架来定位受影响的频率带宽和空间区域。

---
### [2026/753] DDR-SSE: Duplicated Retrieval of Documents for System-wide Secure Searchable Symmetric Encryption

- **作者:** Zichen Gui, Simon-Philipp Merz, Kenneth G. Paterson, Sikhar Patranabis

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/753) | [PDF](https://eprint.iacr.org/2026/753.pdf)


> **研究背景:** 现有的高效可系统安全性搜索加密方案存在客户端状态更新频繁或泄漏特征难以精确描述的问题，这限制了其在实际场景中的应用。
>
> **主要贡献:** 本文提出了一种名为DDR-SSE的新方案，该方案仅需静态客户端状态，并具有简单的泄漏模式，从而解决了现有方案的不足。
>
> **达到效果:** 通过形式化的系统安全性泄漏模型和广泛的泄漏密码分析，证明了DDR-SSE能够抵御查询重构攻击并保持高效性。
>
> **技术梗概:** 该方案利用重复文档存储和随机化检索机制来抑制访问模式泄漏，同时不牺牲实际效率。

---
### [2026/754] BTX: Simple and Efficient Batch Threshold Encryption

- **作者:** Amit Agarwal, Sourav Das, Babak Poorebrahim Gilkalaye, Peter Rindal, Victor Shoup

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/754) | [PDF](https://eprint.iacr.org/2026/754.pdf)


> **研究背景:** Batched threshold encryption (BTE)允许多个服务器联合解密大量密文中的任意子集，同时保持未选中密文的隐私性。这是构建加密内存池的关键组件，在交易被区块包含前进行加密以减轻最大可提取价值(MEV)的问题。现有的无周期BTE方案要么需要用户选择密文索引导致协调和审查问题，要么计算效率低下。
>
> **主要贡献:** 本文提出了一种名为BTX的简单且高效BTE构造，无需用户选择批次索引即可实现无周期和碰撞自由特性，并在相同大小的标准Elgamal密文中实现了最短的密文长度。
>
> **达到效果:** 通过使方案适用于FFT，我们将解密成本降低到$O(B\log B)$组指数运算和$O(B)$对数运算。在批量大小为512时，使用单个核心进行解密，BTX所需时间为约598毫秒，比Boneh等人部分分数评估基线的FFT优化版本快了大约2.0倍。
>
> **技术梗概:** 通过在BLS12-381上共享并高度优化C++代码，并使用AVX-512矢量化和适用时的FFT后端，实现了上述性能提升。

---
### [2026/755] ACTS: Attestations of Contents in TLS Sessions

- **作者:** Pierpaolo Della Monica, Ivan Visconti, Andrea Vitaletti, Marco Zecchini

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/755) | [PDF](https://eprint.iacr.org/2026/755.pdf)


> **研究背景:** 现有技术如DECO和TLSNotary虽然能够在不修改TLS服务器的情况下验证用户从TLS服务器获取特定数据的能力，但这些方法要求验证器运行复杂的非标准化加密方案（如ZK-SNARKs），这限制了其大规模应用。
>
> **主要贡献:** ACTS通过利用Fuchsbauer和Wolf提出的谓词盲签名概念，提出了一种新的分布式架构，允许用户仅需验证器软件检查标准签名即可证明拥有从TLS服务器获取的数据，从而绕过了先前工作的局限性。
>
> **达到效果:** ACTS实现了圆最优的谓词盲签名协议，并生成了标准RSA-PSS签名。该方案能够与DECO及其后续版本集成使用，用于认证从TLS服务器检索的数据。
>
> **技术梗概:** ACTS基于谓词盲签名技术，设计了一种分布式架构，使得验证器只需检查标准签名即可完成数据认证过程，从而简化了验证流程并提高了应用的可行性。

---
### [2026/756] Integral Attack on Reduced-Round Kalyna

- **作者:** Nitish Kumar, Ranit Dutta, Bimal Mandal

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/756) | [PDF](https://eprint.iacr.org/2026/756.pdf)


> **研究背景:** 研究背景：本文探讨了对乌拉尔区块密码Kalyna的整数攻击，旨在构建具有低数据、时间和内存复杂度的减少轮次区分器和密钥恢复攻击。尽管Kalyna采用SPN型圆结构，其预白化和后白化层使用列向量模$2^{64}$加法，这使得整数属性的传播比仅XOR设计更为微妙。
>
> **主要贡献:** 主要贡献：作者通过精心选择输入多集并结合逆轮变换进行反向扩展，为Kalyna-128、Kalyna-256和Kalyna-512提供了标准设置下的区分器，并在弱密钥假设下以及无预白化变体中进行了研究。这些区分器的数据复杂度低至$2^8$或$2^{16}$个选择文本，显著提高了之前公开的Kalyna整数结果的数据复杂度。
>
> **达到效果:** 达到的效果：作者进一步将这些区分器扩展为针对减少轮次Kalyna的部分解密和平衡性测试的密钥恢复攻击。例如，他们对Kalyna-128/128实现了5轮密钥恢复攻击，数据复杂度为$2^9$个选择明文，时间复杂度为$2^{74}$加密运算，并且内存开销可以忽略不计。据我们所知，这是首次提供针对Kalyna-256/256和Kalyna-512/512的整数密码分析。
>
> **技术梗概:** 技术梗概：通过结合精心选择的输入多集与逆轮变换进行反向扩展，作者提出了针对减少轮次Kalyna的区分器，并进一步将其转化为密钥恢复攻击。这种方法利用了模$2^{64}$加法对整数属性传播的影响，从而提高了攻击的有效性和效率。

---
### [2026/757] Integral Distinguishers and a 4-Round Key-Recovery Attack on Kuznyechik Without Initial Key Whitening

- **作者:** Nitish Kumar, Ranit Dutta, Bimal Mandal

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/757) | [PDF](https://eprint.iacr.org/2026/757.pdf)


> **研究背景:** 本文研究了Kuznyechik密码算法，通过集成密码分析方法追踪特定明文集合在多轮函数中的传播特性。
>
> **主要贡献:** 作者提出了一种2轮区分器，并在此基础上扩展至3轮，最终实现了一个无需初始密钥混洗的4轮密钥恢复攻击。
>
> **达到效果:** 该研究揭示了Kuznyechik在特定条件下的弱点，能够有效减少密钥空间搜索的时间和资源消耗。
>
> **技术梗概:** 通过构造平衡测试并结合部分逆向操作来过滤密钥猜测，从而实现高效的密钥恢复。

---
### [2026/759] A Scalable Fault Countermeasure for SLH-DSA: Trade-offs Between Memory, Performance, and Fault Resilience

- **作者:** Melissa Azouaoui, Tobias Schneider, Denise Verbakel

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/759) | [PDF](https://eprint.iacr.org/2026/759.pdf)


> **研究背景:** 针对SLH-DSA中的嫁接树故障攻击，研究提出了一种可扩展且参数化的压缩缓存对策。
>
> **主要贡献:** 该方法通过减少缓存的WOTS+签名和公钥占用的内存空间来实现显著的记忆节省，并保持强大的故障检测能力。
>
> **达到效果:** 安全性和性能分析表明，在有限的缓存内存（少于约256 kB）下，压缩缓存比标准缓存具有更高的故障检测概率并表现出更好的性能。
>
> **技术梗概:** 通过调整缓存大小、故障恢复能力和性能之间的权衡来实现定制化配置，并研究了标准和压缩缓存的细粒度变体以优化内存-性能权衡。

---
### [2026/760] A Simple Batched Threshold Encryption Scheme

- **作者:** Guru-Vamsi Policharla

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/760) | [PDF](https://eprint.iacr.org/2026/760.pdf)


> **研究背景:** 该研究旨在设计一种简单高效的批量门限加密方案，以解决现有方案中的审查抵抗性、周期限制及解密复杂度过高等问题。
>
> **主要贡献:** 作者提出了一种满足挑战适应性选择攻击（CPA）和挑战选择适应性选择攻击（CCA）安全性的批量门限加密方案，并且该方案具有线性增长的密钥大小和准线性解密复杂度。
>
> **达到效果:** 实验结果显示，该方案在批量大小为B时，解密复杂度为O(BlogB)，并且其CPA安全的密文长度为|\(\mathbb{G}_1\)| + |\(\mathbb{G}_T\)|，CCA安全的密文长度为|\(\mathbb{G}_1\)| + 2|\(\mathbb{F}\)| + |\(\mathbb{G}_T\)|。
>
> **技术梗概:** 该方案通过引入交互式的设置阶段（涉及安全乘法）来实现，并且需要在每个批量中生成和维护线性增长的密钥。

---
### [2026/761] Improved Garbled RAM via Garbled Merge

- **作者:** Can Liu, Lenny Liu, Ning Luo, David Heath

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/761) | [PDF](https://eprint.iacr.org/2026/761.pdf)


> **研究背景:** 研究背景：在加密电路（GC）中，合并两个长度为$n$的$w$位数组以生成一个单一的长度-$n$数组是构建加密随机存取存储器（GRAM）的关键问题。GRAM技术允许高效地编译通用程序。
>
> **主要贡献:** 主要贡献：提出了一种基于对称密钥的新颖合并方法，实现了$(w + 1) \cdot n \cdot \lambda$比特的电路大小，相比现有最佳结果在渐进性和具体实现上均有所改进。
>
> **达到效果:** 达到的效果：通过应用此合并方法，获得了适用于操作$\Theta(\lg n)$位字且在$n$步内停止运行的字RAM程序的对称密钥GRAM，其通信成本为$O(n \lg^3 n \cdot \lambda) \cdot \omega(1)$比特，相比前最佳结果减少了$O(\lg \lg n)$倍。
>
> **技术梗概:** 技术梗概：该方法基于对称密钥机制，并通过优化合并过程实现了更小的电路大小和通信成本。

---
### [2026/762] The Sum-Check Protocol over the Monomial Basis, and Other Optimizations

- **作者:** Quang Dao, Ari Biswas, Liam Eagen, Andrew Milson, Shahar Papini, Justin Thaler

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/762) | [PDF](https://eprint.iacr.org/2026/762.pdf)


> **研究背景:** 该研究基于快速证明者SUMCHECK协议，旨在优化SNARKs（简洁可验证论证系统），特别是在多变量多项式上的求和验证。
>
> **主要贡献:** 作者提出了一种项目化SUMCHECK协议，通过将插值集从布尔超立方体{0,1}^n更改为无穷超立方体{0,∞}^n，实现了证明者速度提升约10%，并简化了多项式的绑定过程。
>
> **达到效果:** 在BN254和伪梅森素数域上，项目化SUMCHECK协议显著提高了SNARKs的验证效率，并减少了字段减法操作。对于结构化的多项式如等式和小于关系，该方法进一步降低了计算复杂度。
>
> **技术梗概:** 通过改变插值集并引入无穷点的评估方法，直接提取多项式的相应单项式系数，从而简化了多项式表示、轮次身份验证及评估公式。

---
### [2026/765] MBU:  Scalable and Constant-Round  Evaluation of Non-linear Functions in Standard MPC Setting

- **作者:** Min Yang, Dongcan Guo, Zihang Zhou, Jinxuan Du, Qingshu Meng

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/765) | [PDF](https://eprint.iacr.org/2026/765.pdf)


> **研究背景:** 尽管多 party 计算 (MPC) 在处理变量乘法和基于比较的函数方面取得了显著进展，但对于多项式、幂、指数、三角函数、Sigmoid、Softmax 和 GeLU 等一般非线性函数，仍缺乏高效且精确的常数轮次 MPC 解决方案。
>
> **主要贡献:** 作者提出了一种统一的 '掩码-广播-去掩码' 设计模式，实现了多种非线性函数的一轮次评估，并保持了无近似特性。贡献包括一种适用于 \(k\) 个变量的一轮次乘法协议，通信复杂度为最优的 \(O(kn)\)。
>
> **达到效果:** 该方法不仅简化了现有解决方案中的多轮次问题和精度损失，还提高了非线性函数评估的效率与准确性，支持更多参与方的大规模计算。
>
> **技术梗概:** 通过结合广播机制和去掩码技术，实现了对多种复杂非线性函数的精确且高效的常数轮次评估。

---
### [2026/766] Dynamic Group Time-based One-time Passwords

- **作者:** Xuelian Cao, Zheng Yang, Jianting Ning, Chenglu Jin, Zhiming Liu, Jianying Zhou

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/766) | [PDF](https://eprint.iacr.org/2026/766.pdf)


> **研究背景:** 研究背景：针对静态组管理设置下的一次性密码（OTP）方案，提出了动态组时间基一次性密码（DGTOTP），以支持成员的非破坏性加入和退出，同时保持匿名性和可追踪性。
>
> **主要贡献:** 主要贡献：首次定义了动态组时间基一次性密码的概念及其安全模型，并提出了一种利用可变色哈希函数家族和Merkle树方案将异步时间基一次性密码转换为DGTOTP的有效构造方法。
>
> **达到效果:** 达到的效果：实现了在动态组管理下轻量级的一次性密码生成过程，确保了成员的非破坏性加入与退出，并保持了匿名性和可追踪性。
>
> **技术梗概:** 技术梗概：通过设计外包解决方案实现先发问题后加入（IFJL）策略，结合使用可变色哈希函数家族和Merkle树方案来支持动态组管理。

---

## 更新: 2026-04-19 15:52

*新增 24 篇论文 (编号 716--741)*

### [推荐] [2026/717] Scalable Registration-Based Encryption from Lattices

- **匹配关键字:** lattice, post-quantum

- **作者:** Michael Klooß, Russell W. F. Lai, Jan Niklas Siemer, Monisha Swarnakar

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/717) | [PDF](https://eprint.iacr.org/2026/717.pdf)


> **研究背景:** 注册基加密(RBE)允许用户将其身份和自动生成的公钥注册给密钥托管者，后者将这些密钥聚合为紧凑摘要。使用此摘要和收件人的身份即可对消息进行加密，而无需密钥托管者的任何秘密，从而解决了阻碍基于身份加密采用的关键托管问题。
>
> **主要贡献:** 作者识别了从Laconic Encryption (LE)转换到RBE过程中的效率瓶颈，并提出了Batched Laconic Encryption (BLE)，这是一种新的原始形式，使得RBE方案在同时支持大量注册用户和渐近性能超越所有类似RBE方案方面取得了突破。
>
> **达到效果:** 该工作提出的RBE方案是首个既能支持大量注册用户又能提供后量子安全性的构造，并且在性能上优于现有方案。
>
> **技术梗概:** 通过设计Batched Laconic Encryption (BLE)，作者优化了从LE到RBE的转换过程，从而提高了效率和安全性。

---
### [推荐] [2026/721] Improving LatticeFold+ with ℓ2-norm Checks

- **匹配关键字:** lattice, post-quantum

- **作者:** Michał Osadnik

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/721) | [PDF](https://eprint.iacr.org/2026/721.pdf)


> **研究背景:** LatticeFold+等折叠方案通过压缩多个关系实例为小型累加器来实现增量证明，但$\ell_\infty$范数检查导致证明者性能受限。
>
> **主要贡献:** 提出了一种最终的$\ell_2$-范数检查设计，结合了随机投影约束和精确缩短步骤，以在提取时恢复原始证词的$\ell_2$-范数界限。
>
> **达到效果:** 该方法与LatticeFold+组合使用，实现了可控的范数增长、保持绑定性和知识健全性目标，并显著降低了证明者成本，同时保持了相似的证明大小和验证成本。
>
> **技术梗概:** 通过在提取时恢复原始证词$\ell_2$-范数界限，该设计结合了随机投影约束和精确缩短步骤，提供了一种模块化的方法，可以应用于其他基于格的折叠方案。

---
### [推荐] [2026/722] (Mis)using the Lattice Isomorphism Problem. Cryptanalysis of the double-LIP and Construction of LIP-Based Blind Signatures

- **匹配关键字:** lattice, post-quantum

- **作者:** Veronika Kuchta, Francesco Sica

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/722) | [PDF](https://eprint.iacr.org/2026/722.pdf)


> **研究背景:** 研究基于格同构问题(Lattice Isomorphism Problem, LIP)的盲签名方案，旨在探索LIP在后量子密码学中的应用潜力及其局限性。
>
> **主要贡献:** 分析了Abe-Okamoto框架的安全性，并提出了针对双LIP问题的有效攻击方法，揭示了该框架下的安全性弱点。
>
> **达到效果:** 成功破解了基于LIP的双方案，并提出了一种结合LIP、最近向量问题(Closest Vector Problem, CVP)和模短整数解问题(modular Short Integer Solution, SIS)的新盲签名方案。
>
> **技术梗概:** 通过设计特定攻击算法，从两个独立的LIP实例中恢复秘密非奇异矩阵，并在此基础上构建新的安全机制。

---
### [推荐] [2026/724] Decomposition of Large Look-Up Tables for Fast Homomorphic Evaluation

- **匹配关键字:** homomorphic encryption

- **作者:** Sonia Belaïd, Nicolas Bon, Matthieu Rivain

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/724) | [PDF](https://eprint.iacr.org/2026/724.pdf)


> **研究背景:** TFHE作为一种具有实践潜力的全同态加密方案，其核心优势在于强大的可编程启动操作（PBS），但随着明文空间大小增加，计算成本急剧上升，限制了高精度应用。
>
> **主要贡献:** 提出了一种加速高精度LUT评估的技术，显著提升了现有最佳方法，并且在概念上更为简单。
>
> **达到效果:** 该方法对于大于6位的明文空间表现优于原PBS，同时与WoP-PBS竞争，无需设计新的同态操作符，便于集成到更大的同态编译系统中。
>
> **技术梗概:** 通过分解大LUT来减少计算成本，并结合标准TFHE方案中的PBS操作，实现高效高精度的LUT评估。

---
### [推荐] [2026/728] MAGNET: MAsked Gaussian Now Efficient and Table-less

- **匹配关键字:** post-quantum

- **作者:** Mert Yassi, Soundes Marzougui, Raymond K. Zhao, Muhammed F. Esgin, Amin Sakzad, Ron Steinfeld

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/728) | [PDF](https://eprint.iacr.org/2026/728.pdf)


> **研究背景:** 离散高斯采样（DGS）是后量子密码学中生成随机噪声的关键方法，但其易受侧信道攻击，因此需要有效的防护措施。
>
> **主要贡献:** $\textsf{MAGNET}$ 提出了一个基于 Wei 等人 (2023) 引入的布尔电路设计的高效掩码方案，解决了 DGS 的实现难题。
>
> **达到效果:** 该方法无需依赖耗时的浮点运算或大型查找表技术，在标准差 $\sigma$ 较大时表现出显著的速度优势，分别在 $\sigma = 256$ 和 $\sigma = 1024$ 下实现了最高 $17\times$ 和 $56\times$ 的加速。
>
> **技术梗概:** 通过设计高效的布尔电路实现 DGS 掩码化，$\textsf{MAGNET}$ 在保持性能的同时减少了计算复杂度和存储需求。

---
### [推荐] [2026/729] Code-based Scalable Collaborative SNARKs

- **匹配关键字:** post-quantum

- **作者:** Christodoulos Pappas, Dimitrios Papadopoulos, Charalampos Papamanthou

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/729) | [PDF](https://eprint.iacr.org/2026/729.pdf)


> **研究背景:** 本文提出了首个基于纠错码的可扩展协作SNARK，旨在分散证明计算开销，提高效率。
>
> **主要贡献:** 贡献在于定义了$(t,l)$-零知识协作码，并展示了如何将其用于构建协作交互式近似证明（coIOPP），进而构造出第一个透明且后量子安全的可扩展协作SNARK。
>
> **达到效果:** 实验评估表明，该方法在保持高效性的同时，还实现了零知识属性和后量子安全性。
>
> **技术梗概:** 通过使用张量码及优化后的Spartan PIOP，并结合编译器技术，确保了证明过程的安全性和有效性。

---
### [推荐] [2026/730] Towards Zero Rotation and Beyond: Architecting Neural Networks for Fast Secure Inference with Homomorphic Encryption

- **匹配关键字:** homomorphic encryption

- **作者:** Yifei Cai, Yizhou Feng, Qiao Zhang, Chunsheng Xin, Hongyi Wu

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/730) | [PDF](https://eprint.iacr.org/2026/730.pdf)


> **研究背景:** 隐私保护的深度学习通过同态加密（HE）解决MLaaS中的隐私问题，但高计算成本仍然是一个挑战。
>
> **主要贡献:** 提出了一种专门针对HE环境设计的神经网络架构，包括StriaBlock和新的架构原则，以大幅提高效率。
>
> **达到效果:** 该设计显著减少了HE操作的成本，实现了在保持灵活性的同时控制局部和总体HE成本的目标。
>
> **技术梗概:** 通过引入ExRot-Free Convolution、Cross Kernel以及Focused Constraint Principle和Channel Packing-Aware Scaling Principle等技术策略来优化网络结构。

---
### [推荐] [2026/733] Explicit Bounds on the Existence Probability of Random Multivariate Quadratic Systems over Finite Fields

- **匹配关键字:** post-quantum

- **作者:** Michiya Iwata, Ryomei Sugai, Kosuke Sakata, Tsuyoshi Takagi

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/733) | [PDF](https://eprint.iacr.org/2026/733.pdf)


> **研究背景:** 研究背景：多变量二次方程组在后量子密码学中的安全性依赖于求解有限域上此类系统的计算难度。然而，固定参数下的解的存在概率尚未有充分的研究。
>
> **主要贡献:** 主要贡献：通过分析系数空间并利用包含-排除原则，作者首次给出了固定参数下随机生成的多变量二次方程组解存在的显式上下界估计。
>
> **达到效果:** 达到的效果：对于$m=n$的情况，获得了约0.625的下界和约0.667的上界，并且还推导了当$m=n$时解恰好为一个的概率的边界。此外，也分析了$m 
eq n$情况下的解存在概率。
>
> **技术梗概:** 技术梗概：通过研究系数空间并应用包含-排除原则来估计解的存在概率，从而提供了解决多变量二次方程组安全性的理论依据。

---
### [推荐] [2026/736] Compact Fully Asynchronous Updatable Public Key Encryption Scheme from Hamming Quasi-Cyclic Cryptosystem

- **匹配关键字:** lattice, post-quantum

- **作者:** Sanajit Patra, Ratna Dutta, Jayashree Dey

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/736) | [PDF](https://eprint.iacr.org/2026/736.pdf)


> **研究背景:** 本文旨在构建首个基于汉明准循环码的全异步可更新公钥加密方案，并结合高效的密钥更新机制，解决现有后量子安全异步方案在随机预言模型中的存储和通信效率问题。
>
> **主要贡献:** 作者提出了一种利用精心设计的确定性采样算法实现汉明准循环码公钥加密方案的全异步可更新机制，并正式证明了其安全性。
>
> **达到效果:** 该方案在标准模型下实现了与现有随机预言模型相比显著提高的存储和通信效率，特别是在公共密钥大小、密文大小及更新密文大小方面表现出色。
>
> **技术梗概:** 通过利用保持汉明重量且满足特定代数性质的结构化置换集，作者设计了一种高效的采样算法来实现密钥更新机制。

---
### [推荐] [2026/741] How to Authenticate a Non-Deterministic Computation: Shift-Hiding Functions, Compressed LWE Sampling, Broadcast Encryption, and Obfuscation

- **匹配关键字:** lattice, LWE

- **作者:** Damiano Abram, Giulio Malavolta, Lawrence Roy

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/741) | [PDF](https://eprint.iacr.org/2026/741.pdf)


> **研究背景:** 本文旨在构建支持非确定性计算的同态认证码，扩展了Boneh等人在Eurocrypt 2014年提出的基于格的同态编码方法。
>
> **主要贡献:** 作者提出了一种新的技术工具，用于解决文献中的几个开放问题，包括构造约束伪随机函数、安全压缩和重新扩展LWE样本以及实现适应性安全广播加密方案等。
>
> **达到效果:** 这些贡献使得从格假设中首次证明了上述所有原始密钥的存在性，并且还提供了一种基于格技术的简单直接的隐藏陷阱门取样机制，以构建可证明安全的简单功能性的混淆。
>
> **技术梗概:** 该方法基于分解的学习误差问题（LWE）的困难性，并利用此新工具解决了多个开放问题。

---
### [2026/716] ISE-supported erasure of residual shares

- **作者:** Hao Cheng, Linus Mainka, Daniel Page, Kostas Papagiannopoulos

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/716) | [PDF](https://eprint.iacr.org/2026/716.pdf)


> **研究背景:** 软件实现中，寄存器文件中存储的份额管理是重要方面，因为它会影响相应的侧信道泄漏。消除过期份额是这种管理的一个组成部分：这可以防止后续意外的份额重组并减少泄漏。
>
> **主要贡献:** 研究提出了两个贡献：一是分析基础问题并系统化相关概念和术语；二是设计、实现并评估了支持该问题解决方案的两种组件。
>
> **达到效果:** 通过结合使用这些组件，可以在有效性和效率方面消除与过期份额相关的泄漏。
>
> **技术梗概:** 提出了一种扩展ABI作为策略，并利用扩展ISA（或ISE）来更高效地执行份额清除操作。

---
### [2026/718] Zero-Knowledge Proof of Progress: Secure Multi-Phase Capture-the-Flag Competitions

- **作者:** Salam Khanji, Behzad Abdolmaleki, John Clark, Aryan Pasikhani

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/718) | [PDF](https://eprint.iacr.org/2026/718.pdf)


> **研究背景:** 现有的CTF平台依赖单一组织者，审计性有限，并且容易受到基础设施层面的操纵。
>
> **主要贡献:** zk–MPSFV引入了一种基于zk-SNARK的多阶段子旗验证方案，通过智能合约实现公开可验证的计分板，替代了中心化的评分机制。
>
> **达到效果:** 该方案证明了在标准假设下实现了DAG门控进度、防重放攻击以及阈值稳健的组织者安全性等目标，并且在测试床中展示了高效的性能。
>
> **技术梗概:** 通过将挑战分解为子挑战并构建有向无环图（DAG），团队只能在完成所有父节点后解锁下一步。使用多方计算（MPC）生成联合子旗和解密密钥并通过(t, n) Shamir–BLS门限签名发布，确保了密钥的安全性。

---
### [2026/719] Polynomial-Time Cryptanalytic Extraction of Graph Neural Networks in the Hard-Label Setting

- **作者:** Chun li, Liping Zhuang, Di Li, Yufeng Tang, Zheng Gong

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/719) | [PDF](https://eprint.iacr.org/2026/719.pdf)


> **研究背景:** 研究背景：图神经网络参数作为有价值的知识产权，在高保真提取后可导致模型盗窃、规避和下游滥用。现有方法主要针对前馈模型，未能扩展至消息传递图神经网络。
>
> **主要贡献:** 主要贡献：首次提出了针对ReLU消息传递图神经网络的硬标签设置下的密码分析性提取框架。该框架通过SVD基提取并利用ON/OFF距离比较解决隐藏符号问题，从而恢复隐藏签名。
>
> **达到效果:** 达到的效果：在ogbn-arxiv目标上实现了10,660个参数的攻击，对8,171个评估节点达到了100%预测准确率，并仅使用了4.86亿次节点查询。
>
> **技术梗概:** 技术梗概：通过定位类对决策边界和激活超平面上的双重点约束，结合SVD基提取和ON/OFF距离比较解决隐藏符号问题，从而避免显式比例拟合并利用固定顺序的两节点查询接口。

---
### [2026/720] ABRA-CAPA-DABRA: Full break of CAPA

- **作者:** Paco Azevedo-Oliveira

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/720) | [PDF](https://eprint.iacr.org/2026/720.pdf)


> **研究背景:** 研究背景：Reparaz等人在CRYPTO18上提出了一种新的模型Tile-Probe-and-Fault-Model，旨在通过结合侧信道泄漏和故障注入攻击来模拟更现实的攻击场景。
>
> **主要贡献:** 主要贡献：作者通过攻击CAPA中Beaver triples生成过程，证明了该综合防物理攻击措施在模型中的不安全性，并成功破解了这些防护机制。
>
> **达到效果:** 达到的效果：研究揭示了CAPA方案在Tile-Probe-and-Fault-Model下的脆弱性，表明需要重新评估和改进现有的侧信道与故障注入防御策略。
>
> **技术梗概:** 技术梗概：通过解析线性系统的方法，作者成功地破解了CAPA中的Beaver triples生成过程，展示了其不安全性。

---
### [2026/725] The Cost of Fluidity: Communication Complexity Trade-offs in Fluid MPC

- **作者:** Shancheng Zhang, Zongyang Zhang, Bernardo Magri

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/725) | [PDF](https://eprint.iacr.org/2026/725.pdf)


> **研究背景:** 研究背景：经典的安全多方计算（MPC）协议假设参与者集是静态的，所有参与者必须在整个计算过程中保持在线。然而，在实际应用中，动态参与的需求日益增加，因此提出了具有动态参与机制的流式MPC模型。
>
> **主要贡献:** 主要贡献：作者正式化了基于$d$-out-of-$n$门限秘密共享的流式MPC的通信复杂性，并证明了在恶意方腐败阈值$t$超过$d$的比例时，线性通信复杂度是不可能实现的。
>
> **达到效果:** 达到的效果：通过构造协议，作者实现了在半诚实对手下的乘法门通信成本为$9.3n$个元素，在恶意对手下的通信成本为$37.3n$个元素，证明了流式MPC的成本可以被控制在实际范围内。
>
> **技术梗概:** 技术梗概：该研究通过形式化分析和构造性协议设计，探讨了动态参与机制下MPC的通信复杂性边界，并提出了高效的实现方案。

---
### [2026/726] Bitsliced Segment-Based Search Technique for Low-Depth and Hardware-Efficient S-Box Circuits

- **作者:** Giyoon Kim, Seungjun Baek, Yongjin Jeon, Vedad Hadžić, Jongsung Kim

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/726) | [PDF](https://eprint.iacr.org/2026/726.pdf)


> **研究背景:** 本文旨在提出一种新的低深度S盒电路构造技术，以提高硬件效率并适用于多种S盒大小。
>
> **主要贡献:** 作者提出了SLICE方法，并结合eBPD算法优化了XOR门的数量，从而实现了低深度和高硬件效率的S盒电路设计。
>
> **达到效果:** 通过应用SLICE方法，作者成功构建了针对AES、Ascon S盒以及Dillon 6比特APN S盒的新低深度电路设计，其中部分设计打破了现有记录。
>
> **技术梗概:** SLICE技术通过分段和位级优化来减少电路深度，并在搜索过程中暂时降低大位宽或高AND深度子电路的位宽。

---
### [2026/727] Automated formal analysis of Signal’s Double Ratchet: attacks, fixes and security proofs

- **作者:** Vincent Cheval, Charlie Jacomme, Jessica Richards

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/727) | [PDF](https://eprint.iacr.org/2026/727.pdf)


> **研究背景:** Double Ratchet (DR)协议是多个广泛使用的端到端加密通信服务的核心安全组件，此次研究旨在首次对其进行全面形式化分析，涵盖所有功能并特别证明了后密钥泄露安全性。
>
> **主要贡献:** 研究实现了高度自动化的形式化分析方法，并发现了三个针对该协议的攻击，其中两个已被确认存在于主要实现中，一个存在于规范中。
>
> **达到效果:** 通过此次研究，我们为Signal Messenger提供了新的安全保证，并展示了在多种强威胁模型下DR提供的高水平安全性。
>
> **技术梗概:** 研究采用了高度自动化的形式化分析技术，能够处理所有可能的密钥泄露情况，并对复杂协议变体的部分安全性进行了证明。

---
### [2026/731] SecDTD: Dynamic Token Drop for Secure Transformers Inference

- **作者:** Yifei Cai, Zhuoran Li, Yizhou Feng, Qiao Zhang, Hongyi Wu, Danella Zhao, Chunsheng Xin

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/731) | [PDF](https://eprint.iacr.org/2026/731.pdf)


> **研究背景:** 随着Transformer模型的广泛应用，特别是通过API服务提供给开发者和企业使用，隐私保护成为关键问题。现有的安全推理框架虽然有效，但计算和通信开销高，限制了实际部署。
>
> **主要贡献:** SecDTD提出了一种动态令牌丢弃方案，专为安全的Transformer推理设计。它通过在更早的推理阶段进行令牌丢弃来降低成本，并引入了Max-Centric Normalization (MCN) 和 OMSel 两种核心技术。
>
> **达到效果:** 实验结果表明，与现有方法相比，SecDTD 在保持准确性的前提下显著降低了计算和通信开销，提高了安全推理的效率。
>
> **技术梗概:** SecDTD 引入了 Max-Centric Normalization (MCN) 和 OMSel 两种技术。MCN 是一种独立于 Softmax 的新型评分方法，OMSel 则是一种更快的安全中位数选择协议。

---
### [2026/732] Faster Logical Operations from Discrete CKKS

- **作者:** Jaehyung Kim

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/732) | [PDF](https://eprint.iacr.org/2026/732.pdf)


> **研究背景:** 研究高效非算术操作在(G)BFV同态加密方案中的实现，特别是在任意明文模数的情况下。
>
> **主要贡献:** 提出了一种将(G)BFV与离散CKKS方案进行转换的方法，使得(G)BFV密文能够在离散CKKS环境中利用基于基数的整数计算。
>
> **达到效果:** 这一方法实现了对于明文模数p的同态比较操作在BFV中运行时间为$O(\log p \log\log p)$，在GBFV中为$O(\log\log p)$，显著提高了逻辑运算效率。
>
> **技术梗概:** 通过设计(G)BFV与离散CKKS之间的方案转换，利用了离散CKKS的基数整数计算特性来加速同态比较等逻辑操作。

---
### [2026/734] Assessing Geometric Security of AES Neural Realizations: Linear-Time Key Recovery via Neural Leakage

- **作者:** Kwangjo Kim

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/734) | [PDF](https://eprint.iacr.org/2026/734.pdf)


> **研究背景:** 研究了基于ReLU的神经网络实现AES-128/192/256的安全性，特别是在实值输入下这些实现如何将AES扩展为$\mathbb{R}^{128}$上的连续分段线性函数。
>
> **主要贡献:** 提出了利用几何特性在确定时间内通过神经泄漏恢复主密钥的方法，并证明了攻击复杂度为$O(128R)$的神经查询次数。
>
> **达到效果:** 实验表明，对于AES-128、AES-192和AES-256的1000个随机密钥，该方法实现了100%的成功恢复率。
>
> **技术梗概:** 通过局部可分引理利用对称扰动技术，确定一个唯一保持线性区域成员性的密钥假设，并通过简单的输出等式测试实现位级恢复。

---
### [2026/735] CLAASP-MP: An Automated MILP Framework for Monomial Prediction

- **作者:** Emanuele Bellini, Mohamed Rachidi, Sharwan K. Tiwari

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/735) | [PDF](https://eprint.iacr.org/2026/735.pdf)


> **研究背景:** 该研究旨在开发一种基于3SDP-woU的自动MILP框架，用于预测多项式在对称密钥密码学中的应用。
>
> **主要贡献:** 贡献在于提出了一种名为CLAASP-MP的新工具，能够直接从CLAA组件图生成传播规则模型，并应用于多种现代对称设计中。
>
> **达到效果:** 通过该方法，研究者成功计算了特定输出位的代数规范形式（ANF），并确定了MSX-128密钥流密码至多7轮存在的积分特性。
>
> **技术梗概:** 技术上，使用MILP模型直接从组件图生成传播规则，并结合精确的比特级模乘法建模技术以提高分析精度。

---
### [2026/737] Blind Verifiable Delay Functions

- **作者:** Charlotte Hoffmann, Krzysztof Pietrzak

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/737) | [PDF](https://eprint.iacr.org/2026/737.pdf)


> **研究背景:** Verifiable delay functions (VDFs)确保计算输出需要特定数量的顺序步骤，同时提供正确性的证明。然而，当前的硬件实现成本高昂且资源有限，限制了其广泛应用。
>
> **主要贡献:** 本文提出了盲VDF的概念，并构建了一个方案，使得客户端可以将输入匿名化后发送给服务器进行评估，从而实现在不泄露输入的情况下安全外包计算任务。
>
> **达到效果:** 通过构造基于Pietrzak VDF的盲版本，实现了在服务器无法得知输入的前提下正确输出和证明的生成与验证过程。
>
> **技术梗概:** 该方案借鉴了盲签名的思想，客户端对输入进行匿名化处理后发送给服务器，服务器仅根据本地状态和接收到的信息生成结果，客户端能够解密恢复正确的输出和证明。

---
### [2026/739] Additive FFTs for HQC on ARM Cortex-M4, Revisited

- **作者:** Ming-Shing Chen, Tun-You Chien, Chun-Ming Chiu, Han-Hsuan Lin, Chun-Tao Peng, Bo-Yin Yang

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/739) | [PDF](https://eprint.iacr.org/2026/739.pdf)


> **研究背景:** 针对ARM Cortex-M4平台优化Hamming Quasi-Cyclic (HQC)密钥封装机制的实现，重点在于使用加性快速傅里叶变换(FFT)进行多项式乘法以提高效率。
>
> **主要贡献:** 提出了一种结合Frobenius加性FFT (FAFFT)与中国剩余定理(CRT)的新方法来高效地处理特定度数的多项式乘法，并用扩展欧几里得算法(EEA)替代Berlekamp-Massey解码器。
>
> **达到效果:** 该优化方案在ARM Cortex-M4平台上显著优于传统的Toom-Karatsuba方法，封装和解封装过程分别获得了19.5%和20.4%的加速。
>
> **技术梗概:** 通过重新解释FAFFT的编码步骤为环同构，并推导出模数的确切公式来实现多项式乘法；利用优化的GF(256) SIMD算术，改进了数据流以支持EEA方法。

---
### [2026/740] Fully Adaptive Threshold Blind Signature Without AGM

- **作者:** Shaolong TANG, Peng Jiang, Fuchun Guo, Willy Susilo, Liehuang Zhu

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/740) | [PDF](https://eprint.iacr.org/2026/740.pdf)


> **研究背景:** 现有适应性安全的盲签名方案依赖于代数群模型（AGM）来证明安全性，但AGM作为强理想化假设要求敌手在输出任何群元素时也需提供其线性表示。因此，构建不依赖AGM的适应性安全阈值盲签名方案具有挑战性。
>
> **主要贡献:** $\mathsf{Rainblind}$是首个无需AGM即可实现适应性安全性的TBS方案，通过将离散对数等式（DLEQ）声明与决策性Diffie-Hellman（DDH）元组声明进行OR编译来实现这一目标。
>
> **达到效果:** 该方案在实际执行中利用均匀哈希随机性使DDH元组分支失败，从而激活DLEQ分支，在安全证明中通过编程OR编译到DDH元组分支，实现了无需AGM的适应性安全性。
>
> **技术梗概:** 核心思想是将DLEQ声明与从哈希函数派生的DDH元组声明进行OR编译，使得安全证明仅需提取群元素而非离散对数。

---

## 更新: 2026-04-16 08:17

*新增 4 篇论文 (编号 712--715)*

### [2026/712] Public Key Encryption from High-Corruption Constraint Satisfaction Problems

- **作者:** Isaac M Hair, Amit Sahai

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/712) | [PDF](https://eprint.iacr.org/2026/712.pdf)


> **研究背景:** 该研究旨在构建一种基于高腐蚀约束满足问题的公钥加密方案，以实现可证明的安全性。
>
> **主要贡献:** 贡献在于提出了两种新的假设难题：大字母表随机谓词约束满足问题（LARP-CSP）和高腐蚀率的kXOR问题，并据此设计了一种新型的公钥加密方案。
>
> **达到效果:** 该方案首次结合了高腐蚀约束满足问题，实现了远超准多项式级别的安全级别。同时，还提供了一种新的基于约束满足问题标签扩展因子图的加密陷阱门方法。
>
> **技术梗概:** 技术上，通过构建一种新型的纠错码，使得生成矩阵既具有扩张性又低密度，并能高效地从几乎全部错误中解码。

---
### [2026/713] How to construct even faster and indifferentiable hash functions from random permutations

- **作者:** Liting Zhang, Han Sui, Lei Zhang, Wenling Wu

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/713) | [PDF](https://eprint.iacr.org/2026/713.pdf)


> **研究背景:** 传统的哈希函数设计，如Merkle-Damgård和SPONGE模式，在安全性与效率之间存在固有的权衡，并且容易受到长度扩展攻击。
>
> **主要贡献:** 提出了Compress-then-Randomize范式，将哈希函数模块化为两个独立组件：一个可变输入长度的压缩组件和一个固定输入长度的最终化组件。
>
> **达到效果:** Rocket系列哈希函数通过此设计实现了高速消息吸收并有效抵御了长度扩展攻击，达到了紧致的安全边界。
>
> **技术梗概:** 该方法利用独立随机置换确保最终化组件从理想散列器的角度看是不可区分的，并且压缩组件优化以接近全原语宽度进行处理。

---
### [2026/714] $\mathsf{Veloz}$: Efficient and Flexible Distribution Framework for Code-Based Polynomial Commitment Scheme

- **作者:** Yuanzhuo Yu, Shi-Feng Sun, Yuncong Zhang, Chenhua Fan, Tianyi Ma, Dawu Gu

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/714) | [PDF](https://eprint.iacr.org/2026/714.pdf)


> **研究背景:** 现有的多项式承诺方案（PCS）在大规模计算的证明生成中效率低下，并且存在第三方依赖和量子威胁的问题，因此需要一种能够分布式处理这些任务的方法。
>
> **主要贡献:** $\mathsf{Veloz}$框架首次实现了通信成本与$N$的次线性关系，并消除了证明大小对子证明者数量的依赖性，同时保持了证明速度和安全性。
>
> **达到效果:** 通过$\mathsf{Veloz}$框架，证明时间减少到$O(\frac{N}{M}\log{\frac{N}{\log{N}}})$，通信成本降低至$O(\lambda \cdot \frac{\log^{2}{N}}{\log\log{N}} + M\cdot\frac{N}{\log{N}})$。
>
> **技术梗概:** 该框架的核心是一种定制化的交织码证明聚合方法，能够高效地结合子证明而仅需最小的通信量。

---
### [2026/715] Chorus: Secret Recovery with Ephemeral Client Committees

- **作者:** Deevashwer Rathee, Emma Dauterman, Allison Li, Raluca Ada Popa

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/715) | [PDF](https://eprint.iacr.org/2026/715.pdf)


> **研究背景:** 传统的密码恢复系统依赖于安全硬件或非合谋服务器，但这些方法可能增加系统的复杂性和成本。
>
> **主要贡献:** Chorus通过设计临时委员会来分散信任，每个委员会由大约一千个客户端组成，并且不依赖服务器进行隐私保护，从而提供强大的隐私性并提高可扩展性。
>
> **达到效果:** 在每四个月内，每个客户端的预期开销低于30秒的计算时间和13.2MB的通信量，在拥有1亿客户端的配置中，最多可以有1000万个客户端离线且最多100万个客户端被攻破的情况下实现这一性能。
>
> **技术梗概:** Chorus通过频繁更换临时委员会来限制攻击者的能力，并为不稳定的、资源受限的客户端设计了系统，以减少每个客户端的开销。

---

## 更新: 2026-04-13 21:10

*新增 7 篇论文 (编号 705--711)*

### [推荐] [2026/705] Cross-Paradigm Models of Restricted Syndrome Decoding with Application to CROSS

- **匹配关键字:** lattice, post-quantum

- **作者:** Étienne Burle, Aleksei Udovenko

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/705) | [PDF](https://eprint.iacr.org/2026/705.pdf)


> **研究背景:** 研究背景：受限 Syndrome 解码（ResSD）问题是线性码解码的一种变体，其中每个错误项必须属于固定的小值集合。该问题构成了后量子签名方案CROSS的安全基础，CROSS是NIST正在进行的附加签名调用中Round 2的候选者之一。
>
> **主要贡献:** 主要贡献：作者展示了如何从特定结构和小范数的向量在新构造的码中推导出ResSD问题的解，并将该问题归约为基于代码（常规 Syndrome 解码）和基于格（最近向量问题，列表短/接近向量集）的问题。
>
> **达到效果:** 达到的效果：这种方法增加了攻击面并为 ResSD 的安全性提供了新的见解。作者还对CROSS实例进行了理论和实验评估，特别是在减少参数的情况下。
>
> **技术梗概:** 技术梗概：通过构造特定结构的码，并利用小范数向量来解决ResSD问题，将该问题归约为代码基和格基问题。

---
### [推荐] [2026/706] Improved Cryptanalysis of the Permuted Kernel Problem with Applications to PERK v2.2.0, SUSHSYFISH and PKP-DSS

- **匹配关键字:** post-quantum

- **作者:** Abul Kalam, Sudeshna Karmakar, Arindam Mukherjee, Soumya Sahoo, Santanu Sarkar

- **分类:** Unknown

- **链接:** [论文](https://eprint.iacr.org/2026/706) | [PDF](https://eprint.iacr.org/2026/706.pdf)


> **研究背景:** Permuted Kernel Problem (PKP)是Shamir提出的一个计算难题，支撑了PERK、SUSHSYFISH和PKP-DSS等后量子签名方案。尽管已有攻击方法，但其复杂度仍为超指数级别，且内存需求与其时间复杂度相当。
>
> **主要贡献:** 本文提出了超越所有已知攻击的新型PKP分析结果，特别是对于PERK v2.2.0的所有参数集，首次提供了在估计的安全位数以下实现秘密向量恢复的可能性。
>
> **达到效果:** 研究不仅改进了SUSHSYFISH和PKP-DSS参数集的比特复杂度估算，还引入了一种Schroeppel-Shamir风格的时间-内存权衡方法，显著减少了内存需求同时保持时间复杂度接近最佳已知攻击。
>
> **技术梗概:** 通过组合meet-in-the-middle技术，并结合新颖的时间-内存权衡策略，实现了对PKP的有效分析。

---
### [推荐] [2026/710] Optimizing and Implementing Threshold MAYO

- **匹配关键字:** post-quantum

- **作者:** Diego F. Aranha, Giacomo Borin, Sofia Celi, Guilhem Niot

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/710) | [PDF](https://eprint.iacr.org/2026/710.pdf)


> **研究背景:** 阈值签名将信任分散到多个参与方，消除了单点故障的风险，并减少了内部人员和密钥泄露的风险，这些特性对于高保证部署越来越重要。
>
> **主要贡献:** 作者提出了一种实用的t-out-of-n阈值变体和MAYO的仿真实现，这是NIST量子后签名候选方案之一。
>
> **达到效果:** 通过引入两种针对分布式环境的技术：Explicit-Salt MAYO和Depth-Reduced MAYO，并结合其他特定于MPC的优化技术，作者实现了最小化在线延迟的目标。
>
> **技术梗概:** 该工作提出了统一协议框架，集成这些技术和其它特定于MPC的优化方法，以确保在诚实多数设置下安全，并对抗活跃对手。

---
### [2026/707] Alternating Sponge: A Low-Memory Hash Function with Beyond-Birthday-Bound Security

- **作者:** Ziyang Luo, Yaobin Shen, Hailun Yan, Lei Wang, Dawu Gu

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/707) | [PDF](https://eprint.iacr.org/2026/707.pdf)


> **研究背景:** 针对低内存环境下的哈希函数设计，提出了Alternating Sponge (ASP)方案以实现超越生日界限的安全性。
>
> **主要贡献:** ASP通过重新设计双海绵结构的状态布局和置换机制，减少了状态空间并增加了每轮挤压的比特数。
>
> **达到效果:** 证明了ASP在保持与双海绵构造相似安全性的同时，实现了更紧凑的状态表示和更多的每轮挤压比特数。
>
> **技术梗概:** ASP采用两阶段串行置换序列更新共享状态，并通过分层吸收和交替置换确保每一处理轮次的紧凑性和扩散性。

---
### [2026/708] Block Circulant Codes for Ethereum PeerDAS

- **作者:** Birenjith Sasidharan, Emanuele Viterbo, Dankrad Feist

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/708) | [PDF](https://eprint.iacr.org/2026/708.pdf)


> **研究背景:** 本文探讨了如何在Ethereum PeerDAS协议中使用块循环码（BC码）作为一维Reed-Solomon (RS)码和二维RS码的替代方案。
>
> **主要贡献:** 贡献在于开发了一套高效的编码与重建算法，并展示了BC码在相同实现框架下的应用，同时允许KZG承诺方案的平滑集成。
>
> **达到效果:** 结果表明，BC码在码率、停止率以及本地代码大小方面优于一维和二维RS码。
>
> **技术梗概:** 技术上采用了循环矩阵结构来设计编码算法，并优化了错误恢复过程以提高效率。

---
### [2026/709] zkRAG: Efficiently Proving RAG Retrieval in Zero Knowledge

- **作者:** Yanze Jiang, Xinyang Yang, Xuanming Liu, Yanpei Guo, Jiaheng Zhang

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/709) | [PDF](https://eprint.iacr.org/2026/709.pdf)


> **研究背景:** 在RAG-as-a-Service环境中，客户端无法验证服务器的检索结果是否忠实执行了约定的近似最近邻搜索算法，这引发了服务一致性问题。
>
> **主要贡献:** 作者提出了第一个针对广泛使用的HNSW近似最近邻搜索算法的多项式交互公证证明（PIOP），并基于此设计了zkRAG，这是一种零知识、简洁且非交互式的论证系统。
>
> **达到效果:** 该系统实现了在线证明者效率的渐进最优性，在单线程下可以快速验证典型的HNSW查询，比现有基线快约1000倍。
>
> **技术梗概:** 设计中引入了混合查找论证、基于检查器的PIOP以高效检查优先队列更新以及高效的成员选择向量检查器等新技术。

---
### [2026/711] Drop-In Masked Modular Reduction for ML-DSA: Cutting Side-Channel Cost in the Root-of-Trust

- **作者:** Merve Karabulut, Reza Azarderakhsh

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/711) | [PDF](https://eprint.iacr.org/2026/711.pdf)


> **研究背景:** 在硬件受限环境下，掩码技术虽能有效抵御侧信道攻击，但通常会带来较大的面积开销。Caliptra Root-of-Trust的ML-DSA实现即面临这一挑战，其面积开销高达约6倍。
>
> **主要贡献:** 作者提出了一种新颖的一阶掩码解决方案，旨在优化Caliptra的设计，显著提升其实现效率。
>
> **达到效果:** 与Caliptra的ML-DSA减少相比，该设计实现了12.1倍的速度提升，减少了86.7%的LUT和94.5%的FF，并将面积延迟效率提高了91倍。
>
> **技术梗概:** 通过提出一种滴入式掩码模块化减少方法，作者优化了Caliptra的设计，同时确保了安全性要求并大幅降低了硬件开销。

---

## 更新: 2026-04-12 20:29

*新增 19 篇论文 (编号 684--704)*

### [推荐] [2026/687] High-Throughput Side-Channel-Protected Stream Cipher Hardware for 6G Systems

- **匹配关键字:** post-quantum

- **作者:** Yuluan Cao, Cankun Zhao, Bohan Yang, Wenping Zhu, Hanning Wang, Min Zhu, Leibo Liu

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/687) | [PDF](https://eprint.iacr.org/2026/687.pdf)


> **研究背景:** 6G通信系统对密码学原语提出了前所未有的要求，需要超高吞吐量、低延迟和强抗实现层攻击能力。LOL2.0是一种最近提出的流密码框架，在后量子设置中实现了高软件效率和强大的安全性。
>
> **主要贡献:** 本研究首次提出了一种侧信道保护硬件实施方法，能够满足6G级的吞吐量需求，并基于LOL2.0流密码框架采用了时间共享掩码技术实现了一次性安全。
>
> **达到效果:** 快速实现方案分别在非屏蔽和屏蔽配置下达到了183 Gbps和142 Gbps的最大吞吐量，而紧凑架构则通过减小硬件成本实现了最低为23.25 kGE和141.98 kGE的面积，在保持竞争力的同时验证了安全性。
>
> **技术梗概:** 研究采用时间共享掩码技术在glitch-extended探针模型下实现了一次性安全，并设计了两种架构：一种优化区域和随机性的紧凑变体，另一种针对最大吞吐量的目标快速变体。

---
### [推荐] [2026/688] Too Far Behind? Narrowing the Gap with a Dual-Enhanced Two-Stage Algebraic Framework for LWE

- **匹配关键字:** lattice, post-quantum, LWE

- **作者:** Rui-Jie Wang, Hong-Sen Yang, Zhong-Xiao Wang, Qun-Xiong Zheng

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/688) | [PDF](https://eprint.iacr.org/2026/688.pdf)


> **研究背景:** LWE问题构成了许多后量子密码方案的基础，如NIST选定的CRYSTALS-KYBER和CRYSTALS-DILITHIUM。传统的代数分析依赖于通过格罗布ner基解阿莫拉-杰系统，但在样本有限时表现不佳。
>
> **主要贡献:** 作者提出了一种新颖的两阶段代数算法，结合了双攻击技术，并引入了一种基于结果的方法来解决新的多项式构造，从而提高了复杂度估计。
>
> **达到效果:** 该算法在给定\(m = n\)样本的情况下，对于CRYSTALS-KYBER的复杂性估计优于Steiner工作中报告的格罗布ner基方法。此外，直接应用于阿莫拉-杰系统的基于结果的方法为小秘密LWE提供了可证明的复杂度估计，实现了指数级加速。
>
> **技术梗概:** 该算法包括两个阶段：首先使用双格子减少将原始样本转换为低维；其次通过引入新的多项式构造并利用误差分布来解决系统，而不是直接解阿莫拉-杰系统。

---
### [推荐] [2026/689] Evaluating PQC KEMs, Combiners, and Cascade Encryption via Adaptive IND-CPA Testing Using Deep Learning

- **匹配关键字:** post-quantum

- **作者:** Simon Calderon, Niklas Johansson, Onur Günlü

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/689) | [PDF](https://eprint.iacr.org/2026/689.pdf)


> **研究背景:** 研究背景：确保密文不可区分性是密码学安全性的基础，但在实际实现和混合设置中进行经验验证面临实践挑战。随着向后量子密码学（PQC）的过渡，结合经典和抗量子原语的混合构造使得经验验证方法变得越来越有价值。
>
> **主要贡献:** 主要贡献：通过将选择明文攻击下的不可区分性（IND-CPA）游戏建模为二元分类任务，并使用带有二元交叉熵损失的标记密文数据训练深度神经网络（DNN），研究了用于密文不可区分性的DNN辨别器。
>
> **达到效果:** 达到的效果：在PQC算法、KEM组合和级联加密实验中，没有单一算法或算法组合表现出显著优势（通过双侧二项式检验评估）。
>
> **技术梗概:** 技术梗概：利用深度学习方法，特别是DNN模型来测试PQC KEMs的IND-CPA安全性，并扩展到混合KEM和级联加密的实验中。

---
### [推荐] [2026/692] Efficient Partially Blind Signatures from Isogenies

- **匹配关键字:** post-quantum

- **作者:** Dung Hoang Duong, Chunpeng Ge, Xuan Thanh Khuc, Willy Susilo

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/692) | [PDF](https://eprint.iacr.org/2026/692.pdf)


> **研究背景:** 部分盲签名是数字系统中隐私保护认证的基础密码学组件，允许用户在不泄露消息内容的情况下获取签名，并且部分盲签名允许将事先协商的公共信息纳入签名消息。
>
> **主要贡献:** 本文提出了一种基于Isogenies的新颖高效部分盲签名方案，其签名和公钥大小显著小于CSI-Otter，成为目前已知最紧凑的后量子安全部分盲签名方案之一。
>
> **达到效果:** 该方案在顺序安全性方面优于先前的工作，并且使用较小的挑战空间，但仅实现了顺序安全性而非并发安全性。
>
> **技术梗概:** 通过利用Isogenies框架和精心设计的小挑战空间，本文提出的方法能够在保持高效性的同时提供紧凑的签名大小。

---
### [推荐] [2026/693] Breaking Optimized HQC: The First Cache-Timing Full Decryption Oracle Key-Recovery Attack in Post-Quantum Cryptography

- **匹配关键字:** post-quantum

- **作者:** Haiyue Dong, Qian Guo

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/693) | [PDF](https://eprint.iacr.org/2026/693.pdf)


> **研究背景:** HQC作为一种后量子密码算法，在NIST标准制定过程中被选中，其源代码声称实现常数时间执行以提高安全性。然而，编译器优化可能破坏这种安全假设。
>
> **主要贡献:** 研究首次揭示了HQC官方AVX2优化版本中的隐蔽漏洞，并展示了首个基于缓存侧信道的全解密攻击方法。
>
> **达到效果:** 通过Flush+Reload技术，未授权的邻近攻击者可以提取解码器内部状态的细粒度信息，最终在不到10秒的时间内完成密钥恢复。
>
> **技术梗概:** 研究结合了缓存侧信道分析与软信息集解码后处理策略，并利用GPU加速的会合于中间技术来实现高效的密钥恢复。

---
### [推荐] [2026/697] Post-Quantum Secure k-Times Traceable Ring Signature

- **匹配关键字:** lattice, post-quantum

- **作者:** Vishal Pareek, Aditi Kar Gangopadhyay, Sugata Gangopadhyay

- **分类:** Unknown

- **链接:** [论文](https://eprint.iacr.org/2026/697) | [PDF](https://eprint.iacr.org/2026/697.pdf)


> **研究背景:** 环签名是一种密码学原语，允许用户以匿名方式为一组用户中的某一个代签消息。然而，无限制的匿名性可能导致恶意签署者发送垃圾信息或过度使用。
>
> **主要贡献:** 本文提出了一种k次可追踪环签名方案，当签署者超过预设的签名上限k时，可以公开其公钥进行追溯。该方案基于格假设构建，确保后量子安全性。
>
> **达到效果:** 所提出的方案在提供更强的安全保证的同时实现了竞争性的性能，适用于现代加密应用，并且通过效率分析与现有构造进行了比较。
>
> **技术梗概:** 该技术方案依赖于格基假设来实现后量子安全的k次可追踪环签名机制。

---
### [推荐] [2026/699] HAWK with Hint: Algebraic Key Recovery from Side-Channel Leakage

- **匹配关键字:** lattice

- **作者:** Byoungchan Chi, Changmin Lee, Inhun Lee

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/699) | [PDF](https://eprint.iacr.org/2026/699.pdf)


> **研究背景:** 随着量子计算的发展，经典公钥系统面临威胁，推动了NIST的后量子密码标准制定过程。HAWK作为一种基于格的签名方案被提出，但其在实际应用中的侧信道泄漏问题尚未得到全面研究。
>
> **主要贡献:** 本文通过将离散高斯采样器泄漏形式化为带有提示信息的HAWK，并分析了三种不同的泄漏类别，设计了相应的代数密钥恢复算法。
>
> **达到效果:** 针对HAWK-1024，在不同类型的泄漏模型下，作者提出了有效的密钥恢复方法：全系数泄漏情况下仅需一个签名即可完成密钥恢复；仅符号泄漏情况下使用约14个签名在大约100秒内恢复秘密键；对于噪声符号泄漏，则需要约400个签名并在30秒内成功恢复，即使错误率增加到40%，仍能在一分钟内通过约7,000个签名实现密钥恢复。
>
> **技术梗概:** 研究采用了代数方法来设计密钥恢复算法，并利用这些算法解决结构化的线性系统以提取隐含的线性关系。

---
### [推荐] [2026/700] GRAFHEN is not IND-CPA secure

- **匹配关键字:** homomorphic encryption

- **作者:** Remi Geraud-Stewart

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/700) | [PDF](https://eprint.iacr.org/2026/700.pdf)


> **研究背景:** GRAFHEN是一种基于对称群重写系统的无噪声全同态加密方案，近期被提出。
>
> **主要贡献:** 作者提供了有效的区分器，揭示了该方案不满足IND-CPA安全性。
>
> **达到效果:** 通过构造区分器，证明了GRAFHEN在IND-CPA安全性的失效。
>
> **技术梗概:** 利用对称群重写系统的特性，设计并实现了有效区分器来识别加密方案的弱点。

---
### [推荐] [2026/703] Quick Draw Queries: Lightweight Searchable Public-key Ciphertexts with Hidden Structures via Non-Interactive Key Exchange

- **匹配关键字:** lattice, post-quantum

- **作者:** Keita Emura, Toshihiro Ohigashi, Nobuyuki Sugio

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/703) | [PDF](https://eprint.iacr.org/2026/703.pdf)


> **研究背景:** 传统的公共密钥可搜索加密方案在处理大量密文时需要线性搜索时间，这限制了其效率。Xu等人提出了一种具有隐藏结构的可搜索公共密文（SPCHS），通过陷阱门揭示隐藏结构以高效检索匹配密文。
>
> **主要贡献:** 本文提出了基于非交互式密钥交换(NIKE)的通用SPCHS构造方案，采用对称密钥机制替代了原有的配对或身份基加密方法，实现了更高效的搜索算法。
>
> **达到效果:** 通过使用Diffie-Hellman NIKE、HMAC基础PRF和AES实现的具体方案，在搜索速度上比Wang等人基于配对的方案快250多倍。
>
> **技术梗概:** 该方案的核心在于利用NIKE生成共享密钥，结合对称加密与伪随机函数技术，实现了独立于任何公钥机制的高效搜索算法。

---
### [2026/684] Zeal: PIR for Non-Cooperative Databases

- **作者:** Javin Zipkin, Ofir Dvir, Divyakant Agrawal, Trinabh Gupta, Soamar Homsi

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/684) | [PDF](https://eprint.iacr.org/2026/684.pdf)


> **研究背景:** Private Information Retrieval (PIR)技术允许用户从公共数据库中检索数据而不泄露查询意图，即使数据库不信任。然而，现有的PIR方案通常需要数据库或网站管理员执行额外的操作，这在没有激励的情况下难以实现。
>
> **主要贡献:** 本文提出了Zeal，一种无需数据库特别配合的PIR方案，并证明了其安全性，能够抵抗强敌手攻击。
>
> **达到效果:** Zeal实现了较低的查询延迟，在AWS上对含有百万记录的数据库进行检索时，平均延迟约为3-4分钟，相比朴素解决方案性能提高了50倍。
>
> **技术梗概:** 通过引入新的技术框架和机制，Zeal能够在不依赖数据库配合的情况下提供安全的数据检索服务，并使用差分隐私保证其安全性。

---
### [2026/685] Efficient e = 3 Threshold RSA via Integer Coordinates for Intel SGX

- **作者:** Sam Ng, Jason Lau

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/685) | [PDF](https://eprint.iacr.org/2026/685.pdf)


> **研究背景:** 现有针对RSA的阈值签名方案在实现$e=3$时存在显著的安全性和效率问题，尤其是在Intel SGX等关键部署场景下。
>
> **主要贡献:** 该研究提出了一种基于整数坐标的框架，实现了在不牺牲安全性的前提下支持$e=3$的阈值RSA签名，并且只需要标准的整数运算和模幂运算。
>
> **达到效果:** 通过这种方法，达到了与现有方案相比更小的份额大小、完美的秘密性和更高的计算效率，特别适用于Intel SGX等应用场景。
>
> **技术梗概:** 该框架通过精心选择插值坐标以产生整数值的拉格朗日系数来消除所有模$\phi(N)$的除法运算，仅使用标准的整数算术和模幂运算实现。

---
### [2026/691] PipeSC: A Resource-efficient and Pipelined Hardware Accelerator for Sumcheck Protocol

- **作者:** Kaixuan Wang, Yifan Yanggong, Xiaoyu Yang, Chenti Baixiao, Lei Wang

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/691) | [PDF](https://eprint.iacr.org/2026/691.pdf)


> **研究背景:** zk-SNARKs通过允许证明者在不泄露额外信息的情况下向验证者证明语句的正确性，近年来其构建方式从单变量多项式转向了多变量多项式设计，这虽然降低了证明复杂度但使得sumcheck协议成为证明者工作负载中的主要瓶颈。
>
> **主要贡献:** PipeSC通过深度流水线、模块乘法器重用和基于状态机的依赖调度器，实现了计算资源在协议各阶段的高利用率，并引入了用于生成Equality-MLE的层次化调度和乘法器重用模块。
>
> **达到效果:** 与最先进的CPU、GPU和ASIC实现相比，PipeSC在GPU实现上提供了高达5.02倍的速度提升。
>
> **技术梗概:** PipeSC采用了深度流水线技术，结合了模块乘法器重用以及基于状态机的依赖调度策略来优化计算资源利用率，并通过多层次调度和乘法器复用来统一支持多个证明子程序。

---
### [2026/694] Proximity Signatures

- **作者:** Guillermo Angeris, Kobi Gurkan

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/694) | [PDF](https://eprint.iacr.org/2026/694.pdf)


> **研究背景:** 研究背景：在大数据环境中，验证者需要确保接收到的数据块是大消息的一部分，并且该消息已被特定密钥签名。由于验证者的计算资源有限，仅能访问数据的局部，因此设计了一种新的签名方案以满足这些需求。
>
> **主要贡献:** 主要贡献：提出了接近签名的概念，允许只有部分访问权限的验证者确认数据与特定消息相关联，并且该消息已被正确签名。
>
> **达到效果:** 达到的效果：通过这种方法，即使验证者只能下载矩阵的一部分，也能有效地验证整个数据集的完整性和签名的有效性，解决了大规模数据分发中的数据可用性问题。
>
> **技术梗概:** 技术梗概：设计了一种基于线性子空间签名的构造方法，使得验证者能够从局部数据中推断出全局消息，并进行有效的签名验证。

---
### [2026/695] 2G2T: Constant-Size, Statistically Sound MSM Outsourcing

- **作者:** Majid Khabbazian

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/695) | [PDF](https://eprint.iacr.org/2026/695.pdf)


> **研究背景:** 多标量乘法（MSM）是离散对数基密码学中的主要计算内核，常成为验证者和其他资源受限客户端的瓶颈。
>
> **主要贡献:** 2G2T 提出了一种简单协议，用于将 MSM 外包给不可信服务器，并证明了其实现统计上的正确性。
>
> **达到效果:** 该协议在服务器端仅需执行两次 MSM 计算并返回两个组元素给客户端，验证者侧的验证工作量显著减少，且独立于 n。
>
> **技术梗概:** 2G2T 通过设计高效的验证方法和利用简单的计算步骤实现了上述目标，同时保持了统计上的安全性。

---
### [2026/696] A Key Schedule Design and Evaluation under Boundary Round-Key Leakage

- **作者:** Yu Morishima, Hideki Yoshikawa, Masahiro Kaminaga

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/696) | [PDF](https://eprint.iacr.org/2026/696.pdf)


> **研究背景:** 研究背景：本文探讨在边界轮密钥泄漏模型下（即首尾轮密钥泄漏）的密钥调度设计问题，旨在评估其安全性。
>
> **主要贡献:** 主要贡献在于提出了一种非线性密钥调度方案，并通过方程和差分约束形式描述了泄漏的影响，为该领域的研究提供了新的视角。
>
> **达到效果:** 达到的效果是通过Gröbner基实验、SAT基于的密钥恢复实验以及Weibull AFT模型下的右截断运行时间分析，验证了在边界泄漏模型下，所提出的密钥调度方案未表现出明显的高效反解路径。
>
> **技术梗概:** 技术梗概：采用非线性密钥调度公式$\mathrm{RK}_i = K \oplus F\bigl(K \oplus T(i)\bigr)$设计并评估了其安全性。

---
### [2026/698] Entropy-based Fuzzy Deduplication with Perfect Resistance to Key Recovery Attack

- **作者:** Zehui Tang, Shengke Zeng, Minfeng Shao

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/698) | [PDF](https://eprint.iacr.org/2026/698.pdf)


> **研究背景:** 针对加密数据的去重技术在保持敏感数据安全的同时减少存储成本，但现有方法面临诸如暴力猜测攻击和密钥恢复攻击等安全性威胁。
>
> **主要贡献:** 本文基于信息熵理论重新定义了数据相似性，并首次提出了参数鲁棒性验证以抵抗密钥恢复攻击和猜测攻击。
>
> **达到效果:** 实验结果显示，在保证篡改检测成功率不低于97%的前提下，该方案可节省约87%的存储空间。
>
> **技术梗概:** 通过引入信息熵理论定义数据相似性，并结合参数鲁棒性验证机制来增强系统的安全性。

---
### [2026/701] Boolean Arithmetic over $\mathbb{F}_2$ from Group Commutators

- **作者:** Marc Joye

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/701) | [PDF](https://eprint.iacr.org/2026/701.pdf)


> **研究背景:** 本文研究了在非交换群中仅使用基本的群运算（如乘法和求逆）实现二进制域$\mathbb{F}_2$上的算术操作，特别是通过群交换子来执行布尔计算。
>
> **主要贡献:** 作者提出了两种互补的方法：一种是构建通用的布尔门电路（NAND），另一种是直接实现XOR和AND运算，并展示了这些方法在有限非交换简单群中的应用。
>
> **达到效果:** 具体实例化于交替群$A_5$和$A_6$中，特别是在最小的非交换简单群$A_5$上的构造达到了最先进的效率水平。
>
> **技术梗概:** 通过利用群的交换子来实现布尔运算，并且这些技术仅依赖于群的基本操作，如乘法和求逆。

---
### [2026/702] A Constructive Treatment of Authentication

- **作者:** Christopher Battarbee

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/702) | [PDF](https://eprint.iacr.org/2026/702.pdf)


> **研究背景:** 本文从构造性密码学的角度回顾了消息认证的传统技术，这是一种主要的可组合安全框架。
>
> **主要贡献:** 作者整理并补充了已知的结果，并指出了研究空白及实现可组合性的障碍。
>
> **达到效果:** 该工作提供了一个工具箱，展示了如何使用各种加密原语来实现可组合的消息认证，并明确了安全保证和前提条件。
>
> **技术梗概:** 通过构造性密码学的方法，本文详细分析了消息认证的各种传统技术，并填补了现有研究中的空白。

---
### [2026/704] Fast Isogeny Evaluation on Binary Curves

- **作者:** Gustavo Banegas, Nicolas Sarkis, Benjamin Smith

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/704) | [PDF](https://eprint.iacr.org/2026/704.pdf)


> **研究背景:** 本文研究了在特征为2的有限域上普通椭圆曲线上的等概映射高效计算方法，扩展了奇数特征技术至二元域。
>
> **主要贡献:** 作者提出了适用于奇数度$\ell = 2s+1$的等概映射有效公式，并设计了一种无逆运算的变体，能够在投影和扭曲Kummer坐标下评估$x$-映射。
>
> **达到效果:** 实验表明，在$\mathbb{F}_{2^{511}}$上，无逆运算的投影和扭曲版本比Vélu风格的$x$-评价更快；而带一次逆运算的仿射版本则快约4.2倍。
>
> **技术梗概:** 通过优化乘法次数并利用特定坐标系保持点的投影性来加速等概映射计算过程。

---

## 更新: 2026-04-10 20:20

*新增 8 篇论文 (编号 676--683)*

### [推荐] [2026/678] Mergeable SNARGs for Trapdoor Languages and Their Applications

- **匹配关键字:** homomorphic encryption, LWE

- **作者:** Zvika Brakerski, Maya Farber Brodsky, Omer Paneth, Tomer Solomon

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/678) | [PDF](https://eprint.iacr.org/2026/678.pdf)


> **研究背景:** 该研究旨在开发一种新的方法，用于合并短的计算声学论证(SNARGs)，使从两个声明的简短证明生成一个逻辑后果的简短证明成为可能。
>
> **主要贡献:** 研究首次实现了对任意拓扑结构下的多项式数量级的递归合并处理，并且安全性的验证时间仅与合并过程的深度成正比，而不受关联的“树大小”的影响。
>
> **达到效果:** 通过这种方法，研究人员构建了基于子指数级iO和LWE的第一个完全紧凑型证明系统，并提出了第一个适应性多跳聚合签名方案。
>
> **技术梗概:** 该技术适用于所谓的‘陷阱门语言’，其中声明的有效性可以在给定陷阱门的情况下在多项式时间内决定。

---
### [推荐] [2026/683] VEIL: Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems

- **匹配关键字:** post-quantum

- **作者:** Rahul Dalal, Tamir Hemo, Eugene Rabinovich, Ron Rothblum

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/683) | [PDF](https://eprint.iacr.org/2026/683.pdf)


> **研究背景:** 随着高效的证明系统迅速成熟，越来越多需要零知识（ZK）保证的实际应用场景正在出现。然而，添加ZK通常需要将非ZK基础系统与昂贵的ZK系统结合使用，或者对基础协议的每个组件进行紧密耦合的修改。
>
> **主要贡献:** 我们提出了VEIL，一种轻量级且不侵入式的编译器，用于基于哈希的多线性证明系统。VEIL通过解耦协议的代数交互和加密哈希，并仅将ZK包装器应用于代数组件来实现ZK。
>
> **达到效果:** 我们的概念验证实现表明，在31位基素域中，对于2^29个字段元素的踪迹，与非ZK证明系统相比，VEIL的证明者开销约为3%，验证者开销为22%，证明大小开销为12%。
>
> **技术梗概:** VEIL通过解耦协议的代数交互和加密哈希，并仅将ZK包装器应用于代数组件来实现ZK，从而保持基础证明系统的架构完整性。

---
### [2026/676] An Efficient Identity-Based Blind Signature Scheme from SM9

- **作者:** Zhiwei Wang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/676) | [PDF](https://eprint.iacr.org/2026/676.pdf)


> **研究背景:** 盲签名是实现电子现金、电子投票和匿名认证等隐私保护协议的基本密码学工具，但同时满足形式安全性和与现有国家标准兼容性仍是一个挑战。
>
> **主要贡献:** 作者提出了一种直接基于SM9国家标准的高效身份基盲签名方案，并提供了严格的形式安全性模型。
>
> **达到效果:** 该方案在随机预言机模型下实现了单次伪造不可抵赖性和完美盲签，相比当前最先进的多因子SM9盲签名减少了至少60%的配对操作和约73%的整体签名延迟。
>
> **技术梗概:** 通过将盲签名直接构建于SM9标准之上，并利用\(q\)-SBDH假设证明了安全性，同时实现了信息论意义上的完美盲签。

---
### [2026/677] SPLASH: SPeculative Leakage-Adaptive Secure Hardware

- **作者:** Huimin Li, Mohamadreza Rostami, Pallavi Borkar, Lichao Wu, Ahmad-Reza Sadeghi

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/677) | [PDF](https://eprint.iacr.org/2026/677.pdf)


> **研究背景:** 现代处理器在制造时基本固定，导致无法进行后硅安全更新。现有的防御措施通常是硬编码的、范围狭窄且不具备适应性，一旦部署就难以应对新的攻击变种，从而留下严重的安全漏洞。
>
> **主要贡献:** SPLASH框架引入了Speculative Information Flow Tracking (SIFT)，实现了对推测数据传播的细粒度跟踪；同时提供了可重构的推测表，首次在处理器流水线中实现全面且灵活的推测行为控制。
>
> **达到效果:** 通过在小型和中型BOOM处理器上实施SPLASH，成功地缓解了所有类型的推测泄漏漏洞，并展示了其动态安全策略调整能力，无需重新设计硬件。
>
> **技术梗概:** SPLASH采用运行时可配置的方法，在制造后可以灵活调整安全策略，如调整推测窗口大小或选择性保护特定微架构结构。

---
### [2026/679] Compressed Key Exchange Protocol from Orientations of Large Discriminant Using AVX-512

- **作者:** Yuhao Zheng, Jianming Lin, Yutong Liang, Yanzhen Ren, Huixin Zhang, Chang-An Zhao

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/679) | [PDF](https://eprint.iacr.org/2026/679.pdf)


> **研究背景:** CSIDH是一种基于类群的密钥交换协议，但在提出时由于Kuperberg算法的存在而面临安全性的挑战。一种基于大型判别式的定向椭圆曲线的新协议（CSIDH-LDO）被提出以解决这一问题。
>
> **主要贡献:** 本文通过优化常数时间实现和有效的公钥压缩框架，解决了CSIDH-LDO的性能瓶颈。
>
> **达到效果:** 实现了对CSIDH-LDO的高度优化，并成功减少了其公钥大小，提高了其实用性。
>
> **技术梗概:** 结合了差分加法链的标量乘法、扭曲爱德华模型上的仿射变换计算以及通过Intel AVX-512指令利用并行性的技术。

---
### [2026/680] Open Problems in List Decoding and Correlated Agreement

- **作者:** Gal Arnon, Dan Boneh, Giacomo Fenzi

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/680) | [PDF](https://eprint.iacr.org/2026/680.pdf)


> **研究背景:** 本文回顾了与Ethereum基金会的Proximity Prize相关的开放问题，重点关注与证明系统和Reed-Solomon码相关的列表解码边界、接近差距、相关协议以及互相关协议等重大挑战。
>
> **主要贡献:** 文章总结了当前在这些领域已知的结果，并指出了需要解决的关键问题，为未来的研究提供了方向。
>
> **达到效果:** 通过分析现有研究，本文揭示了一些关键的理论缺口和实际应用中的技术障碍，有助于推进证明系统的前沿发展。
>
> **技术梗概:** 作者们采用了综述的方法，结合了现有的数学和技术成果来探讨这些开放问题，并提出了可能的技术路径。

---
### [2026/681] The many faces of Schnorr: a touch-up

- **作者:** Victor Shoup

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/681) | [PDF](https://eprint.iacr.org/2026/681.pdf)


> **研究背景:** 本文是对Shoup在2023年关于阈值Schnorr签名方案工具箱的研究的进一步探讨，特别是重新审视了批量随机性提取与再随机化预签名组合的随机预言机分析。
>
> **主要贡献:** 作者通过使模拟论证完全明确，并详细分析了通过预签名、编程哈希值和签名值泄露的信息，填补了批量再随机化处理中的空白。
>
> **达到效果:** 这种方法使得在随机预言机加通用群模型中获得紧致的安全边界变得更加简单直接，避免了对哈希函数内部假设的复杂依赖。
>
> **技术梗概:** 技术上，作者通过将安全证明归约到Schnorr交互式身份验证方案，并观察该方案在通用群模型中的硬度来简化了路径。

---
### [2026/682] Witness-Indistinguishable Arguments of Knowledge and One-Way Functions

- **作者:** Gal Arnon, Noam Mazor, Rafael Pass, Jad Silbak

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/682) | [PDF](https://eprint.iacr.org/2026/682.pdf)


> **研究背景:** 研究了非平凡知识证明中的目击者不可区分性（WI）论证的密码学复杂性，特别是在假设NP不在多项式时间电路类P/poly中时，其与辅助输入单向函数的关系。
>
> **主要贡献:** 证明了在特定假设下，常数轮计算复杂度的知识型WI论证的存在性等价于某些形式的辅助输入单向函数的存在；并指出了统计学上WI论证从单向置换构造的限制。
>
> **达到效果:** 通过这些理论结果，进一步明确了知识提取器的设计边界，并为构建更安全的密码系统提供了指导。
>
> **技术梗概:** 采用了假设验证和复杂性类之间的归约方法来证明上述结论。

---

## 更新: 2026-04-08 21:15

*新增 7 篇论文 (编号 667--675)*

### [推荐] [2026/670] Verification Facade: Masquerading Insecure Cryptographic Implementations as Verified Code

- **匹配关键字:** post-quantum

- **作者:** Nadim Kobeissi

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/670) | [PDF](https://eprint.iacr.org/2026/670.pdf)


> **研究背景:** 研究探讨了Hax验证管道在将Rust代码转换为F*以进行形式化证明时，是否能够准确地保持其声称的加密实现的安全特性。
>
> **主要贡献:** 贡献在于识别并分类了三种类型的安全性差距：翻译不忠、不可验证的信任边界和规范游戏，并通过具体实例展示了这些差距的存在。
>
> **达到效果:** 结果表明，即使经过形式化验证的代码也可能存在未被发现的安全漏洞，验证过程并不能完全保证加密实现的安全性。
>
> **技术梗概:** 研究通过对Hax验证管道的35个阶段转换、F*证明库和规范API进行结构分析来识别这些差距，并通过针对ML-DSA等标准算法的具体攻击案例进行了展示。

---
### [推荐] [2026/671] A note on the Unsuitability of LIGA for Linkable Ring Signatures: The perils of non-commutativity

- **匹配关键字:** lattice

- **作者:** Iñigo Diaz Iribarnegaray, Václav Gregor, Florian L’écu Leal

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/671) | [PDF](https://eprint.iacr.org/2026/671.pdf)


> **研究背景:** 本文研究了[KTS+24]中基于群作用框架的链可追溯环签名(LRS)方案，该方案使用Lattice Isomorphism Group Action (LIGA)，其安全性依赖于著名的Lattice Isomorphism Problem (LIP)。
>
> **主要贡献:** 作者指出，尽管[BKP20]框架提供了保证，但由于使用了非交换群，导致[LTS+24]中的签名方案不符合链可追溯环签名的要求，即不满足正确性和链接性。
>
> **达到效果:** 研究进一步揭示了[KTS+24]中提出的匿名属性也不成立，并探讨了将秘密密钥空间限制为GL_n(ℤ)的交换子群以修复签名方案的可能性，但发现这并不容易实现。
>
> **技术梗概:** 通过分析非交换群GL_n(ℤ)及其在LIP中的应用障碍，作者尝试通过限制秘密密钥空间来解决链可追溯环签名的问题。

---
### [2026/667] Which Privacy Blanket is Optimal in the Shuffle Model?

- **作者:** Pengcheng Su, Haibo Cheng, Ping Wang

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/667) | [PDF](https://eprint.iacr.org/2026/667.pdf)


> **研究背景:** 近年来，混洗模型作为隐私保护数据分析的主流范式之一，通过‘隐私放大’机制模糊个体用户的报告，本文从信息论角度系统研究了这一机制。
>
> **主要贡献:** 作者首次系统性地探讨了最优噪声设计问题：在给定目标用户消息遵循特定分布的情况下，寻找最大化隐私保护的混洗噪声分布。
>
> **达到效果:** 研究表明，最优化的噪声分布通常与目标分布不同。对于二元字母表，几乎均匀分布是最优的；对于一般有限字母表，作者推导出了显式的最优解。
>
> **技术梗概:** 通过分析互信息、总变差信息、消息恢复优势和预期后验方差等指标来评估隐私保护程度，并证明了最优化噪声设计的重要性。

---
### [2026/668] Cryptographic Implications of Worst-Case Hardness of Time-Bounded Kolmogorov Complexity

- **作者:** Yanyi Liu, Noam Mazor, Rafael Pass

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/668) | [PDF](https://eprint.iacr.org/2026/668.pdf)


> **研究背景:** 研究探讨了时间限制下的Kolmogorov复杂性问题的最坏情况难度，及其对密码学应用的影响。
>
> **主要贡献:** 作者提出了在适当假设下，该问题不属于$P/poly$时的新结论，包括非统一模拟器的零知识证明系统和难分离NP对的存在性。
>
> **达到效果:** 这些结果表明，在最坏情况下假设该问题不属于$P/poly$可以推导出密码学中的重要应用实例。
>
> **技术梗概:** 通过展示在适当假设下，如果该问题不属于$P/poly$，则可以证明上述结论，技术上涉及复杂性类的分离和零知识证明理论。

---
### [2026/672] FLOSS: Fast Linear Online Secret-Shared Shuffling

- **作者:** Ian Chang, Sela Navot, Alex Ozdemir, Nirvan Tyagi

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/672) | [PDF](https://eprint.iacr.org/2026/672.pdf)


> **研究背景:** 随机秘密数据向量的置换是许多隐私保护协议的核心组件，包括数据分析、广告和通信等领域。现有的方法要么依赖于计算密集型的公钥密码学和零知识证明，要么在处理大型向量时由于使用了准线性大小的置换网络而性能不佳。
>
> **主要贡献:** 本文提出了一种预处理方法，以实现恶意安全下的双方计算（2PC）中快速的线性时间在线洗牌。我们提出了FLOSS协议，这是一种用于安全计算任何交互式算术置换电路的2PC协议。
>
> **达到效果:** 我们的实验证明了FLOSS在执行在线洗牌方面的高效性：在不到500毫秒的时间内完成了$2^{20}$个元素的洗牌操作，比现有最佳替代方案快800多倍。
>
> **技术梗概:** 我们通过将秘密共享排序（数据统计中的子协议）描述为算术置换电路，并使用FLOSS将其编译为高效的在线2PC协议来实现这一目标。

---
### [2026/674] Efficient Batch Threshold Encryption Using Partial Fraction Techniques

- **作者:** Dan Boneh, Rohit Nema, Arnab Roy, Ertem Nusret Tas

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/674) | [PDF](https://eprint.iacr.org/2026/674.pdf)


> **研究背景:** 现有的批量加密方案要么依赖于时间周期，要么在无时间周期的情况下存在公共参数过大和易受审查的问题。
>
> **主要贡献:** 本文提出了一种无时间周期、抗审查的批量加密方案，该方案具有线性大小的公共参数、常量大小的预解密密钥和密文，并且支持高效的批量解密。
>
> **达到效果:** 通过使用部分分数技术，我们的方案能够发布单个群元素作为预解密密钥，从而允许解密者解密整个批次中的所有密文。我们证明了该方案在选择明文攻击下的安全性，并展示了如何对其进行门限化。
>
> **技术梗概:** 我们利用部分分数分解技术，使得发布单个组元素即可作为预解密密钥，从而实现批量解密功能。

---
### [2026/675] SoK: DeFi Lending and Yield Aggregation Protocol Taxonomy, Empirical Measurements, and Security Challenges

- **作者:** Arad Kotzer, Tom Azoulay, Yoad Abels, Aviv Yaish, Ori Rottenstreich

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/675) | [PDF](https://eprint.iacr.org/2026/675.pdf)


> **研究背景:** 研究旨在系统化DeFi借贷生态系统，涵盖抵押借贷、非抵押原语及收益聚合协议，并通过实证分析揭示设计选择对行为和安全的影响。
>
> **主要贡献:** 贡献在于构建了DeFi借贷机制的分类体系，提供了Compound V2和AAVE V2的实际案例研究，并指出了由于特定设计导致的安全漏洞。
>
> **达到效果:** 结果包括识别出关键的设计缺陷及其潜在风险，并为未来的研究提出了开放性问题。
>
> **技术梗概:** 技术上采用了实证方法来测量链上借贷活动和用户行为，并分析了利率设定机制和时间计量方法中的安全挑战。

---

## 更新: 2026-04-06 20:44

*新增 54 篇论文 (编号 606--666)*

### [推荐] [2026/607] Refined Approx-SVP Rank Reduction Conditions and Adaptive Lattice Reduction for MSIS Security Estimation

- **匹配关键字:** lattice

- **作者:** Xiaohan Zhang, Zijian Zhou, Longjiang Qu

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/607) | [PDF](https://eprint.iacr.org/2026/607.pdf)


> **研究背景:** 研究背景：基于格的密码学的安全性依赖于近似最短向量问题（Approx-SVP）的具体难度。现有的Rank缩减条件可能过于激进，因为它们隐含地假设可以访问大量极其短的格矢量。
>
> **主要贡献:** 主要贡献：作者系统化并细化了从可行性角度考虑的Approx-SVP Rank缩减条件，提出了基于几何特性的第一种条件和结合基质量依赖概率界的第二种条件。
>
> **达到效果:** 达到的效果：通过在高维格上的广泛实验验证，紧凑型条件在维度850和925时比先前方法性能高出60倍。结合这些进展，作者开发了改进的具体安全估计方法。
>
> **技术梗概:** 技术梗概：提出了APBKZ动态选择块大小和D4f参数的适应性泵基格缩减策略，并引入了限制缩减到关键前缀的HeadAPBKZ头部聚焦执行模式。

---
### [推荐] [2026/610] Concrete Estimation of Correctness and IND-CPA-D Security for FHE via Rare Event Simulation

- **匹配关键字:** homomorphic encryption, LWE

- **作者:** Mathieu Ballandras, Jean-Baptiste Orfila, Samuel Tap

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/610) | [PDF](https://eprint.iacr.org/2026/610.pdf)


> **研究背景:** 全同态加密方案由于其底层的密码学假设具有概率正确性，加密过程中会添加随机误差项。这种误差在进行同态计算时会逐渐增长，影响方案的安全性和正确性。
>
> **主要贡献:** 本文提出了一种框架，通过重要性分裂算法，提供了理论上预测噪声演化的实际保证，并验证了改进的Irwin-Hall分布模型的有效性。
>
> **达到效果:** 该研究确保了全同态加密方案在IND-CPA-D模型下的概率满足安全性和正确性的严格界限，具体到TFHE的Bootstrapping及其变体中得到了实证支持。
>
> **技术梗概:** 通过应用重要性分裂算法，本文实现了对噪声演化的精确模拟，并验证了改进后的分布模型的有效性，从而提高了全同态加密方案的安全性和可靠性。

---
### [推荐] [2026/612] Improving ML Attacks on LWE with Data Repetition and Stepwise Regression

- **匹配关键字:** lattice, LWE

- **作者:** Alberto Alfarano, Eshika Saxena, Emily Wenger, François Charton, Kristin Lauter

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/612) | [PDF](https://eprint.iacr.org/2026/612.pdf)


> **研究背景:** 研究背景：Learning with Errors (LWE)问题是基于格的密码学中的一个困难数学问题。在二进制秘密的简单情况下，它是带误差的子集和问题。已有有效的机器学习(ML)攻击成功应用于稀疏的秘密样本。
>
> **主要贡献:** 主要贡献：作者展示了使用更大的训练集和重复示例能够恢复更密集的秘密，并引入了一种逐步回归技术来恢复秘密中的“凉爽位”。
>
> **达到效果:** 达到的效果：通过增加数据量和重复样本，研究实现了对更密集秘密的恢复。实验观察到基于模型的尝试、数据集大小与重复样本之间的幂律关系。
>
> **技术梗概:** 技术梗概：采用逐步回归方法来识别并恢复秘密中的关键位，并结合大数据训练提高了攻击效果。

---
### [推荐] [2026/614] Attacks on Sparse LWE and Sparse LPN with new Sample-Time tradeoffs

- **匹配关键字:** LWE

- **作者:** Shashwat Agrawal, Amitabha Bagchi, Rajendra Kumar

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/614) | [PDF](https://eprint.iacr.org/2026/614.pdf)


> **研究背景:** 本文扩展了Kikuchi方法，针对更高模数$q$的$k$-稀疏LWE和LPN问题提供了算法。
>
> **主要贡献:** 作者提出了基于Kikuchi图的新攻击方法，并将其应用于$LWE$和$LPN$问题。
>
> **达到效果:** 这两种攻击分别通过计算邻接矩阵的谱范数和非平凡闭路径来决定，为稀疏$LWE/LPN$问题提供了新的样本复杂性和时间复杂性之间的权衡。
>
> **技术梗概:** 利用Kikuchi图的性质，作者设计了两种基于谱范数和闭路径的方法来解决$k$-稀疏LWE/LPN问题。

---
### [推荐] [2026/615] On the Security of MPC-in-the-Head Signatures with Correlated GGM Trees

- **匹配关键字:** post-quantum

- **作者:** Thibauld Feneuil, Matthieu Rivain

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/615) | [PDF](https://eprint.iacr.org/2026/615.pdf)


> **研究背景:** MPC-in-the-Head技术通过GGM树及其优化（如一树技术和相关树技术）构建了具有紧凑签名大小的签名方案，但对后者的安全性分析缺失。
>
> **主要贡献:** 首次提供了基于相关树技术的MPC-in-the-Head签名方案的形式安全分析，并揭示了一个潜在的安全漏洞。
>
> **达到效果:** 证明了恢复秘密证词前$\lambda$位足以实现完整的密钥恢复，因此要求基础假设应使得恢复这$\lambda$位与恢复完整证词一样困难。
>
> **技术梗概:** 通过形式化证明，在随机预言模式或理想密码模式下为基于相关树技术的签名方案提供了安全保证。

---
### [推荐] [2026/617] Scaling of Memory and Bandwidth Requirements of Post-Quantum Signatures with Message Size

- **匹配关键字:** post-quantum

- **作者:** Falko Strenzke

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/617) | [PDF](https://eprint.iacr.org/2026/617.pdf)


> **研究背景:** 本文分析了当前标准化的后量子签名算法及其在X.509上下文中的协议集成，在消息大小方面，评估其内存和带宽效率特性。
>
> **主要贡献:** 研究探讨了签名和验证操作中算法是否支持针对已签名消息进行在线计算，并审查了不同签名方案预计算短消息代表性的可能性。
>
> **达到效果:** 研究表明，对于特定的实际应用场景，后量子签名方案在协议使用中的内存和带宽效率差异较大，且总体上低于基于RSA和椭圆曲线的传统签名方案，后者总是允许通过哈希值预先计算短消息代表。
>
> **技术梗概:** 研究通过分析现有的标准和协议集成来评估不同后量子签名算法的性能，并提出了PKCS#11标准中即将引入的相关加密API。

---
### [推荐] [2026/619] Breaking the One-Way Property of a SHA-3 Implementation via Fault Injection: Key Recovery Attacks on Post-Quantum Digital Signatures

- **匹配关键字:** post-quantum

- **作者:** Mona Sobhani, Sönke Jendral, Elena Dubrova, Mats Näslund

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/619) | [PDF](https://eprint.iacr.org/2026/619.pdf)


> **研究背景:** 本文针对NIST后量子数字签名标准第二轮候选方案中的六种基于SHA-3的哈希函数进行了故障注入攻击研究，旨在揭示这些依赖于SHA-3的安全机制在面对特定故障时的脆弱性。
>
> **主要贡献:** 作者通过单指令跳过故障注入技术，在Keccak-f置换阶段破坏了SHA-3的一次性特性，并成功恢复了密钥，从而实现了对受影响签名方案的全面破解。
>
> **达到效果:** 实验验证表明，该攻击方法在优化后的pqm4 ARM Cortex-M4 CROSS实现中通过电压瞬变有效执行，证实了其实际可行性并揭示了现有保护措施的不足。
>
> **技术梗概:** 研究采用故障注入技术，在 sponge 挤压阶段对Keccak-f进行单指令跳过操作，从而揭示隐藏的秘密值，并利用这些秘密值恢复密钥。

---
### [推荐] [2026/627] Efficient and Parallel Implementation of Isogeny-based Deterministic Group Actions

- **匹配关键字:** post-quantum

- **作者:** Weize Wang, Yi-Fu Lai, Kaizhan Lin, Yunlei Zhao

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/627) | [PDF](https://eprint.iacr.org/2026/627.pdf)


> **研究背景:** 该研究针对Houben提出的基于类群作用的OSIDH-LD方案，旨在实现高效的确定性无交互密钥交换协议。尽管现有SageMath实现较慢，但理论上有最快的性能。
>
> **主要贡献:** 作者通过算法优化和并行技术改进了OSIDH-LD方案，包括尾部修剪、更快的同态识别以及定制化的isogeny计算策略，并实现了接近完美的并行性。
>
> **达到效果:** 经过优化后，该方案在密钥生成和密钥协商中的性能显著提升，达到了理论上的最优速度。
>
> **技术梗概:** 通过算法层面的优化和并行执行模型的应用，特别是在类群操作中采用fork-join模式，实现了高效的并行化处理。

---
### [推荐] [2026/628] Fast and Compact Lattice-Based Registration-Based Encryption

- **匹配关键字:** lattice, post-quantum

- **作者:** Tianwei Zhang, Xiuquan Ding, Giulio Malavolta, Nico Döttling

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/628) | [PDF](https://eprint.iacr.org/2026/628.pdf)


> **研究背景:** 注册加密（$\mathsf{RBE}$）作为一种新兴的公钥基础设施替代方案，结合了身份基加密（IBE）和传统公钥加密的优点，但现有的高效构造较少且安全性不足。
>
> **主要贡献:** 本文提出了一种基于格的$\mathsf{RBE}$方案，实现了更小的密文大小和更快的加解密速度，提升了$\mathsf{RBE}$的实际应用潜力。
>
> **达到效果:** 该方案将$1000$用户的密文大小从$9$\,MB减少到$0.148$\,MB，并且加密/解密时间缩短了一个数量级。
>
> **技术梗概:** 通过优化格基构造，本文减少了密文的尺寸并提高了加解密效率，同时保证了后量子安全。

---
### [推荐] [2026/630] Asymptotic Analysis of Ternary Sparse LWE

- **匹配关键字:** lattice, LWE

- **作者:** Byoungchan Chi, Nathan Cho, Jiseung Kim, Changmin Lee

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/630) | [PDF](https://eprint.iacr.org/2026/630.pdf)


> **研究背景:** 研究背景：本文针对Jain--Lin--Saha在CRYPTO'24提出的稀疏学习误差问题（spLWE）的三元变体进行了渐近分析，探讨了其在密钥稀疏度$k$极小情况下的安全性。
>
> **主要贡献:** 主要贡献：作者提出了两种攻击框架来处理不同参数区域的spLWE问题，分别针对几何区域和统计区域设计了不同的攻击策略。
>
> **达到效果:** 达到的效果：实验结果证实了理论预测的突变过渡点，并表明在某些参数设置上比先前工作具有更低的复杂度；同时指出了我们的方法不适用的范围。
>
> **技术梗概:** 技术梗概：通过将稀疏行简化为$k$维格空间中的短向量问题，利用筛法算法获得复杂性；对于统计区域，则采用贪婪坐标恢复攻击。

---
### [推荐] [2026/631] Rethinking r-PKP: a New Formulation for the Relaxed Permuted Kernel Problem

- **匹配关键字:** post-quantum

- **作者:** Giuseppe D'Alconzo, Andrea Gangemi, Lorenzo Romano, Giuliano Romeo

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/631) | [PDF](https://eprint.iacr.org/2026/631.pdf)


> **研究背景:** 研究背景：PERK签名方案的安全性基于Permuted Kernel Problem (PKP)的难解性，但其最初的松弛版本依赖于特定实例和向量，限制了性能优化。
>
> **主要贡献:** 主要贡献在于重新定义松弛问题，使其不再依赖于具体实例和向量，而是寻找满足秩亏条件的置换矩阵，从而简化了建模过程。
>
> **达到效果:** 达到的效果是提出了一种新的代数攻击方法，借鉴了MinRank和Rank Syndrome Decoding的技术，构建了一个基于置换矩阵项的多项式系统，并对这些项进行了研究。
>
> **技术梗概:** 技术梗概：通过将问题转化为寻找满足秩亏条件的置换矩阵，并利用多项式系统的代数方法进行分析。

---
### [推荐] [2026/632] A tight security analysis of the FIPS-205 standard (SLH-DSA)

- **匹配关键字:** post-quantum

- **作者:** Dai Chi Do, Quoc Toan Nguyen, Phong Quang Trieu, Ba Danh Vu

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/632) | [PDF](https://eprint.iacr.org/2026/632.pdf)


> **研究背景:** SPHINCS+框架作为后量子时代的无状态哈希签名方案，已被NIST标准化为SLH-DSA (FIPS 205)，但其具体安全性分析存在权衡：紧界需要多目标决策性第二单程抵抗（SM-DSPR）的假设，而完全证明则会带来显著的宽松度。
>
> **主要贡献:** 本文通过分析SM-openPRE和SM-PRE属性，而非依赖SM-DSPR，改进了SPHINCS+的具体安全分析，并采用精确的概率模拟技术限制多目标紧界退化仅限于实际揭示的最大目标数。
>
> **达到效果:** 在SLH-DSA参数集上应用此无假设方法，填补了理论缺口，恢复了高达18位的经典安全性及9位的量子安全性，优于NIST宽松评估。
>
> **技术梗概:** 通过精确的概率模拟技术，本文限制多目标紧界退化仅限于实际揭示的最大目标数，而非总理论目标数。

---
### [推荐] [2026/633] Progressive Sieving-Style Information-Set Decoding Algorithm

- **匹配关键字:** lattice

- **作者:** Tong Yu, Haodong Jiang, Hong Wang, Rongmao Chen, Qingfeng Cheng, Xinyi Huang, Yuefei Zhu

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/633) | [PDF](https://eprint.iacr.org/2026/633.pdf)


> **研究背景:** 信息集解码(ISD)算法是评估基于代码的密码方案如经典McEliece、HQC和BIKE等实际比特安全性的重要工具。最近，Guo等人提出了基于局部敏感过滤器(LSF)的筛法-ISD算法，并将其与BJMM/MMT算法在攻击经典McEliece方面进行了比较。
>
> **主要贡献:** 本文提出了一种通用的筛法-ISD框架（称为渐进式筛法-ISD），允许更灵活的参数配置。通过二元筛假设下的复杂性分析，展示了该方法及其“一次解码多个”(DOOM)变体在攻击经典McEliece方面的改进。
>
> **达到效果:** 通过搜索最优参数配置，证明了本文提出的渐进式筛法-ISD相较于之前的非渐进版本，在攻击时间复杂度上实现了5-12比特的改进。
>
> **技术梗概:** 该方法基于局部敏感过滤器(LSF)和二元筛假设，通过优化参数配置提高了信息集解码算法在特定密码方案中的效率。

---
### [推荐] [2026/635] Low-Stack HAETAE for Memory-Constrained Microcontrollers

- **匹配关键字:** lattice

- **作者:** Gustavo Banegas, YoungBeom Kim, Seog Chung Seo, Christine van Vredendaal

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/635) | [PDF](https://eprint.iacr.org/2026/635.pdf)


> **研究背景:** 针对具有8-16 kB可用SRAM的微控制器，实现模块化格签名方案HAETAE，以解决峰值栈使用量成为绑定约束的问题。
>
> **主要贡献:** 提出了拒绝感知分层分解、组件级早期拒绝以及逆序流式熵编码（rANS）等技术，优化了HAETAE在微控制器上的实现。
>
> **达到效果:** 通过上述方法，签名的栈使用从71-141 kB减少到5.8-6.0 kB，密钥生成减少了至4.7-5.7 kB，验证则降至4.7-4.8 kB，覆盖了HAETAE-2/3/5三种安全级别。
>
> **技术梗概:** 引入了分层分解、早期拒绝以及逆序流式熵编码技术，并结合了流式矩阵生成和两阶段超球体采样器等方法。

---
### [推荐] [2026/638] THED: Threshold Dilithium from FHE

- **匹配关键字:** homomorphic encryption

- **作者:** Jai Hyun Park, Alain Passelègue, Damien Stehlé

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/638) | [PDF](https://eprint.iacr.org/2026/638.pdf)


> **研究背景:** 本文提出了一种基于门限全同态加密（ThFHE）的Dilithium签名方案THED，旨在实现多方安全签署，同时保持与标准Dilithium验证算法的一致性。
>
> **主要贡献:** 该贡献在于将Dilithium的签名过程嵌入到ThFHE中，并开发了多项新的工具和技术来解决由此带来的挑战。
>
> **达到效果:** 通过这些技术，THED实现了高效的多方签署协议，支持任意数量的用户和可调阈值参数，且验证算法与标准Dilithium一致。
>
> **技术梗概:** 该方案利用CKKS同态计算，并开发了连续CKKS-BFV、混合格式同态比较以及大整数同态比较等新工具来优化性能。

---
### [推荐] [2026/641] HyperVerITAS: Verifying Image Transformations at Scale on Boolean Hypercubes

- **匹配关键字:** post-quantum

- **作者:** Garrett Greiner, Toshi Mowery, Pratik Soni

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/641) | [PDF](https://eprint.iacr.org/2026/641.pdf)


> **研究背景:** 针对大规模图像变换验证的需求，提出了HyperVerITAS系统，旨在提供可扩展、高效且隐私保护的图像来源验证方法。
>
> **主要贡献:** HyperVerITAS通过使用布尔超立方体上的多项式编码，减少了证明时间和内存消耗，并支持多种多项式承诺方案的模块化集成。
>
> **达到效果:** 实验表明，在普通硬件上，HyperVerITAS能够生成33MP图像的证明，仅需27GB内存和6.6分钟的时间，而VerITAS则无法处理超过4MP的图像。
>
> **技术梗概:** 该系统采用了两种不同的承诺方案（Brakedown和多线性KZG），并分离了签名验证与图像变换的过程。

---
### [推荐] [2026/643] FOVA: Fast One-Shot Verifiable Aggregation for Federated Learning

- **匹配关键字:** homomorphic encryption

- **作者:** Yin Zhu, Junqing Gong, Kai Zhang, Shay Gueron, Haifeng Qian

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/643) | [PDF](https://eprint.iacr.org/2026/643.pdf)


> **研究背景:** 在联邦学习中，安全聚合允许服务器计算模型更新的总和而不访问客户端的单独梯度，以保护客户端本地数据集不被推断。然而，现有协议可能因恶意服务器从聚合梯度重建客户端数据而变得脆弱。
>
> **主要贡献:** FOVA提出了一种快速的一次性可验证聚合协议，同时实现了对抗活跃恶意服务器时的聚合隐藏性和真实性。
>
> **达到效果:** 该协议通过基于Paillier同态加密方案的设计，实现了高效的安全性和实用性，并能够与现有的Paillier基联邦学习框架集成。
>
> **技术梗概:** FOVA利用了可验证线性同态加密方案的新构造，确保在支持一次性客户端的同时满足高效率和安全性需求。

---
### [推荐] [2026/650] A Search-to-Decision Reduction for Continuous LWE

- **匹配关键字:** LWE

- **作者:** Kirpa Prince

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/650) | [PDF](https://eprint.iacr.org/2026/650.pdf)


> **研究背景:** 本文解决了连续版本的LWE问题(CLWE)中搜索到决策的约简问题，这是在现有研究基础上进一步完善CLWE问题的研究。
>
> **主要贡献:** 作者提出了一个相对简单的算法，能够将秘密向量近似到一个小误差范围内，并证明了决策 oracle 能够解决CLWE的问题。
>
> **达到效果:** 该研究填补了CLWE从搜索版本到决策版本约简的空白，为相关领域的进一步研究提供了基础。
>
> **技术梗概:** 通过设计一个近似算法和利用决策oracle的强大性来实现约简目标。

---
### [推荐] [2026/651] Robot: Robust Threshold BBS+ in Two Rounds

- **匹配关键字:** homomorphic encryption

- **作者:** Guofeng Tang, Tian Qiu, Bowen Jiang, Haiyang Xue, Guomin Yang, Man Ho Au, Robert H. Deng, Kwok-Yan Lam

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/651) | [PDF](https://eprint.iacr.org/2026/651.pdf)


> **研究背景:** BBS+签名方案因其支持选择性披露和证明凭证持有而被广泛应用于匿名凭证系统，但传统设置中单一权威机构发行凭证存在单点故障风险。
>
> **主要贡献:** 	extit{Robot}是首个两轮的阈值BBS+签名方案，实现了最小化轮次并确保至少$t+1$个诚实参与方即可顺利完成签名过程。
>
> **达到效果:** Robot在理论上实现了恒定每方上传通信和线性计算开销，并且相比Wong等人四轮方案，在相同渐近复杂度下具有更小的常数因子。
>
> **技术梗概:** 通过使用基于DDH的阈值可验证随机函数（TVRF）构造来稳健生成公共非随机数，结合阈值Castagnos-Laguillaumie和阈值ElGamal同态加密完成剩余非线性操作。

---
### [推荐] [2026/660] QED-Lite: Lightweight Detection of Quantum-Vulnerable ELF Binaries via Cryptographic Library Version Fingerprinting

- **匹配关键字:** post-quantum

- **作者:** Ha-Gyeong Kim, Seung-Won Lee, Ji-Won Bang, Ui-Jae Kim, Hui-Ju Kang, Min-Seo Kim, Hwa-Jeong Seo

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/660) | [PDF](https://eprint.iacr.org/2026/660.pdf)


> **研究背景:** 随着量子计算的进步，广泛使用的公钥加密系统面临严重威胁，组织需要识别其系统中的量子易受攻击（QV）可执行文件并迁移到后量子密码学（PQC）。
>
> **主要贡献:** 本文提出了一种轻量级近似工具QED-Lite，通过使用版本指纹法确定加密库的PQC支持来简化分析阶段。
>
> **达到效果:** 实验结果表明，QED-Lite在Network数据集上的执行时间比QED快855倍（0.84秒），内存使用量减少了228倍（22.9MB），同时保持了100%的TPR。
>
> **技术梗概:** QED-Lite通过构建针对11个主要加密库的新PQC风险分类数据库，并依赖pyelftools实现，减轻了高计算开销分析阶段的影响。

---
### [推荐] [2026/662] Verifiable Divide-and-Conquer

- **匹配关键字:** LWE

- **作者:** Omer Paneth, Rafael Pass

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/662) | [PDF](https://eprint.iacr.org/2026/662.pdf)


> **研究背景:** 研究背景：简洁非交互式证明（SNARGs）作为验证外包计算的强大工具，使得能够将一个大计算问题分解为较小的子问题并分别委托给不同的实体解决。
>
> **主要贡献:** 主要贡献：本文提出了在分布式分而治之设置下的可验证外包策略，并基于LWE假设构建了一个支持任意多项式次数递归合并且证明大小仅线性增长的SNARG系统。
>
> **达到效果:** 达到的效果：该系统解决了现有方法中安全性能随递归合并次数指数下降的问题，实现了高效、安全的递归外包计算验证。
>
> **技术梗概:** 技术梗概：通过基于LWE假设设计新的SNARG方案，并引入了可合并性机制，使得子问题证明可以被有效组合成原始问题的证明。

---
### [推荐] [2026/666] Signature Placement in Post-Quantum TLS Certificate Hierarchies: An Experimental Study of ML-DSA and SLH-DSA in TLS 1.3 Authentication

- **匹配关键字:** post-quantum

- **作者:** José Luis Delgado

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/666) | [PDF](https://eprint.iacr.org/2026/666.pdf)


> **研究背景:** 研究背景：在TLS 1.3中实现后量子迁移不仅仅是简单地替换签名算法的问题，还涉及到证书层次结构中的签名位置、暴露深度以及计算负担的分布等因素。
>
> **主要贡献:** 主要贡献：通过实验比较了ML-DSA和SLH-DSA在不同证书放置策略下的性能，特别是在TLS 1.3认证机制中探索了后量子安全性的实现方式。
>
> **达到效果:** 达到的效果：研究揭示了签名算法在服务器叶子证书中的不利影响，表明将其限制在信任层可以显著减少握手延迟和计算成本。
>
> **技术梗概:** 技术梗概：使用OpenSSL 3和oqsprovider进行实验，通过多轮实验对比分析不同配置下的性能表现，涵盖叶子节点、完整层次结构策略矩阵、深度比较以及密钥交换探索等方面。

---
### [2026/606] PD-Net: Learning Device-Invariant Representations for Heterogeneous Cross-Device Side-Channel Attacks

- **作者:** Dalin He, Wei Cheng, Yuejun Liu, Jingdian Ming, Yongbin Zhou

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/606) | [PDF](https://eprint.iacr.org/2026/606.pdf)


> **研究背景:** 针对不同硬件平台的侧信道攻击模型难以泛化的问题，本文提出了一种新的深度学习框架PD-Net，旨在学习设备不变特征以实现跨架构的零样本攻击。
>
> **主要贡献:** 该工作通过分离算法内容和设备特定样式，并使用原型和最大均值差异损失对特征分布进行对齐，从而实现了这一目标。
>
> **达到效果:** 实验结果表明，PD-Net在8位与32位设备之间实现了稳健的零样本跨架构迁移，且攻击成功率远超现有方法。
>
> **技术梗概:** 通过构建一个包含多种硬件平台和泄漏模态的数据集进行训练，并使用特定损失函数对齐特征分布以学习设备不变表示。

---
### [2026/608] Can Adaptive Communication Graphs Lower the Bottleneck Complexity of (Secure) Multiparty Computation?

- **作者:** Lisa Kohl, Pierre Meyer, Divya Ravi, Nicolas Resch

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/608) | [PDF](https://eprint.iacr.org/2026/608.pdf)


> **研究背景:** 研究背景：(安全的)多方计算协议的瓶颈复杂度是衡量其通信效率的一个指标，反映了通信负载是否均衡。以往工作主要关注固定通信图的协议，即在执行过程中，某一参与方是否与其他方通信仅取决于轮次。
>
> **主要贡献:** 贡献在于展示了通过适应性选择通信图的强大能力，开发了多种瓶颈高效协议，并证明任何函数都可以安全地以$O(n/\log n)$的瓶颈复杂度进行计算（我们证明这是必要的）。
>
> **达到效果:** 结果是达到了比固定通信图更低的瓶颈复杂度，对于任意函数$f\colon\{0,1\}^n\to\{0,1\}$，通过适应性选择通信图可以实现$O(n/\log n)$的瓶颈复杂度。
>
> **技术梗概:** 技术梗概是通过限制协议在异步网络中正确运行来确保其有效性，并开发了多种适应性选择通信图的方法以降低瓶颈复杂度。

---
### [2026/611] A Comparative Evaluation of DATA and Microwalk for Detecting Constant-Time Violations in Cryptographic Libraries

- **作者:** Dominik Schneider, Paul Fuchs, Kerstin Lemke-Rust

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/611) | [PDF](https://eprint.iacr.org/2026/611.pdf)


> **研究背景:** 文章对比评估了两种先进的动态二进制仪器化(DBI)工具DATA和Microwalk，用于检测密码学库中常量时间(CT)违规情况。
>
> **主要贡献:** 研究通过统一的测试环境和多种加密实现（包括LibTomCrypt、OpenSSL和liboqs），比较了这两种工具的结果。
>
> **达到效果:** 实验结果表明，在对称密钥算法上，两种工具都能提供可靠的结果；但在非对称密码方案中，内部随机数导致大量差异化的报告结果。
>
> **技术梗概:** 为了提高工具结果的可比性，测试设置被调整为外部注入随机数，这些随机数原本由加密库生成。

---
### [2026/613] Haechi: Simple Commitment-based Keyless In-person Verifiable Elections

- **作者:** Jiwon Kim, Michael Naehrig, Olivier Pereira, Josh Benaloh

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/613) | [PDF](https://eprint.iacr.org/2026/613.pdf)


> **研究背景:** 传统的加密选票方法依赖于密钥管理，这往往是系统中最复杂和易出错的部分。相比之下，基于承诺的现场投票方案可以完全避免使用密钥，简化并增强了系统的鲁棒性。
>
> **主要贡献:** Haechi 提出了一个无需密钥的现场可验证选举方案，并结合现代零知识证明技术显著减小了选票记录的大小。
>
> **达到效果:** 与现有部署相比，Haechi 的解决方案将选票记录的大小减少了超过一个数量级，从而降低了托管、分发和验证数据的成本。
>
> **技术梗概:** 该方案利用了基于承诺的方法，并结合了现代零知识证明技术来减小选举记录的体积。

---
### [2026/616] On the properties of arithmetic crosscorrelation for sequences with coprime periods

- **作者:** Feifei Yan, Pinhui Ke

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/616) | [PDF](https://eprint.iacr.org/2026/616.pdf)


> **研究背景:** 研究了反馈带进位移寄存器（FCSRs）生成的伪随机序列的算术交叉相关性，这是评估其性能的关键指标。
>
> **主要贡献:** 作者推导了由Legendre符号构造的序列和通过迹函数生成的序列的上界，并证明了具有互质周期的非二进制序列的算术交叉相关性也保持恒定。
>
> **达到效果:** 这些结果扩展了Chen等人关于经典Legendre序列的研究，为更广泛的序列类型提供了理论依据。
>
> **技术梗概:** 通过数学推导和分析迹函数及Legendre符号的性质来确定上界，并证明相关性的恒定性。

---
### [2026/620] AHAB: Asynchronous, High-throughput, Adaptively-secure, Batched Threshold Schnorr Signatures

- **作者:** Victor Shoup

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/620) | [PDF](https://eprint.iacr.org/2026/620.pdf)


> **研究背景:** 本文旨在提出一种适用于异步通信环境的门限 Schnorr 签名方案 AHAB，确保在静态和适应性恶意行为者存在的情况下仍能正常工作。
>
> **主要贡献:** 作者通过改进现有协议并提供全面的安全证明，在适应性恶意行为模型中实现了输出交付保证，并引入了签名生产流水线以限制活跃作恶者的损害。
>
> **达到效果:** 该方案能够在 t < n/3 的静态和适应性恶意行为者存在的情况下，实现门限 Schnorr 签名的异步高通量生成，并且在恶意行为发生时能够快速识别并移除恶意参与者。
>
> **技术梗概:** 通过引入玩家淘汰机制和简化协议变体，以及使用星形查找算法优化预签名批次处理，提高了系统的通信效率和安全性。

---
### [2026/621] Efficient Conflict-Free NTT Hardware Architecture with Single-Port RAMs: Applications to ML-DSA

- **作者:** Henrique S. Ogawa, Thales B. Paiva, Marcos A. Simplicio Jr, Syed M. Hafiz, Bahattin Yildiz

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/621) | [PDF](https://eprint.iacr.org/2026/621.pdf)


> **研究背景:** 本文提出了一种基于Prouhet-Thue-Morse (PTM) 码的Number Theoretic Transform (NTT) 硬件架构，旨在实现仅依赖单端口RAM (SPRAM) 的NTT 实现，以提高效率并减少资源消耗。
>
> **主要贡献:** 该研究的主要贡献在于通过利用PTM码支持的冲突自由、事务性和流水线化特性，设计了符合参考软件的ML-DSA专用NTT模块，并实现了高吞吐量和低延迟的性能。
>
> **达到效果:** 实验结果显示，基于PTM的单蝶形和双蝶形NTT设计分别达到了接近每蝴蝶一周期和半周期的性能，同时保持与现有紧凑型NTT实现相当的FPGA资源利用率。
>
> **技术梗概:** 该技术通过使用SPRAM替代DPRAM，并利用PTM码特性来优化NTT计算阶段的流水线化处理和并行性，从而减少了硬件复杂性和资源消耗。

---
### [2026/622] Locally Computable High Independence Hashing

- **作者:** Yevgeniy Dodis, Shachar Lovett, Daniel Wichs

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/622) | [PDF](https://eprint.iacr.org/2026/622.pdf)


> **研究背景:** 研究几乎$k$-wise独立哈希函数，这些函数在任何$k$个输入上的评估几乎是均匀随机的。这类哈希函数需要一个与$k$成线性关系的大密钥，但可能通过只读取一个小于$k$的子集$t \ll k$来实现亚线性时间计算，称为$t$-局部哈希函数。
>
> **主要贡献:** 论文提出了非构造性的完美$k$-wise独立$t$-局部哈希函数，具有键大小$O(kn)$和局部性$t = O(n)$位，并且展示了这些哈希函数的显式实现依赖于显式的最优双部不损失扩张器。
>
> **达到效果:** 通过这种哈希函数，可以生成具有相应参数的扩展器。即使访问的位置可以适应性选择，这也表明显式哈希函数的进步需要显式扩展器的进步。
>
> **技术梗概:** 技术上涉及非构造性的证明方法和对现有最优不损失双部扩张器的利用，以实现局部哈希函数的目标。

---
### [2026/623] Bad Benchmarks and a Fourier-Analytic Framework for Characterizing the (Un)Hideability of Combinational-Logic Circuits

- **作者:** Animesh Chhotaray, Kollin Labowski, Thomas Shrimpton

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/623) | [PDF](https://eprint.iacr.org/2026/623.pdf)


> **研究背景:** 设计隐藏（DH）方案旨在保护集成电路（IC）供应链中的电路设计知识产权。然而，大多数实际的DH方案已被高效的攻击破解。
>
> **主要贡献:** 作者通过识别使电路不可隐藏的属性，并开发新的白盒傅里叶分析算法来评估这些属性在标准DH基准测试中的普遍存在性。
>
> **达到效果:** 研究发现ISCAS'85和MCNC测试套件中的大多数电路本质上是不可隐藏的，而新基准则表现出更强的对傅里叶分析算法的抵抗力，并值得更广泛地用于DH评估。
>
> **技术梗概:** 通过利用白盒访问电路并结合模型计数技术，作者开发了高效的白盒傅里叶分析算法来评估电路是否具有使其不可隐藏的属性。

---
### [2026/624] Weak-key cryptanalysis of Blink

- **作者:** Tim Beyne

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/624) | [PDF](https://eprint.iacr.org/2026/624.pdf)


> **研究背景:** 本文针对最近在FSE 2026会议上介绍的可调块密码Blink进行了弱密钥分析，揭示了其潜在的安全漏洞。
>
> **主要贡献:** 作者发现Blink两轮加密存在非线性不变量，并据此提出了部分密钥恢复攻击方法。
>
> **达到效果:** 该攻击能够在数据和时间复杂度均为$2^{23}$的情况下，对一小部分（约$2^{-96}$）的弱密钥或调整值进行部分密钥恢复。
>
> **技术梗概:** 攻击基于与作者之前对Midori-64发起的攻击相同的技术策略。

---
### [2026/626] Deep Learning-Assisted Improved Differential Fault Attacks on Lightweight Stream Ciphers

- **作者:** Kok Ping Lim, Dongyang Jia, Iftekhar Salam

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/626) | [PDF](https://eprint.iacr.org/2026/626.pdf)


> **研究背景:** 针对资源受限环境中的轻量级密码原语，尤其是物联网设备，由于其公共性易遭受物理攻击，特别是故障攻击。现有基于深度学习的密码分析技术虽有进展，但在流密码上的应用仍有限。
>
> **主要贡献:** 提出了一种利用多层感知机模型辅助差分故障攻击的方法，并成功应用于ACORNv3、MORUSv2和ATOM三种轻量级流密码中。
>
> **达到效果:** 实验表明，所提方法在识别故障位置上取得了高准确率，并且相较于传统签名基方法具有优势；同时，通过阈值法优化了密钥恢复所需的故障注入次数，降低了攻击复杂度。
>
> **技术梗概:** 采用多层感知机训练模型来定位未知位置的单比特翻转故障，并结合阈值法提高密钥恢复效率。

---
### [2026/629] Towards Formal Security Proofs of MQOM

- **作者:** Haruhisa Kosuge, Keita Xagawa

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/629) | [PDF](https://eprint.iacr.org/2026/629.pdf)


> **研究背景:** 文章针对MPC-in-the-Head (MPCitH)签名中广泛应用的GGM树优化技术，特别是其中涉及的秘密密钥相关联的GGM树，探讨了其在MQOM中的应用及其带来的安全证明挑战。
>
> **主要贡献:** 作者提出了两种改进版本的MQOM，并提供了相应的EU-F-CMA安全性证明。这些改进包括对盐值的小幅调整以及替换GGM树中的块密码哈希函数为随机函数。
>
> **达到效果:** 通过这些改进，文章成功地在量子随机预言模型下证明了第一种变体的安全性，并在理想密钥和随机预言模型下证明了第二种变体的安全性。
>
> **技术梗概:** 研究采用了H系数技术来解决随机化验证与隐藏验证之间的依赖关系问题。

---
### [2026/634] PlasmaBlind: A Private Layer 2 With Instant Client-Side Proving

- **作者:** Pierre Daix-Moreux, Chengru Zhang

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/634) | [PDF](https://eprint.iacr.org/2026/634.pdf)


> **研究背景:** PlasmaBlind旨在通过利用折叠方案的特性来设计一种既隐私又可扩展的Layer-2协议，以减少L2用户的开销并提高交易数据的证明效率。
>
> **主要贡献:** 该研究贡献了一种新颖的架构，结合了盲化技术和聚合验证技术，实现了高效且紧凑的区块生成和验证过程。
>
> **达到效果:** 实验结果表明，PlasmaBlind能够在消费级硬件上实现客户端侧小于100毫秒的证明时间和每交易小于300毫秒的聚合验证时间。
>
> **技术梗概:** 通过提出一种优化技术，将两个具有共享输入的不同验证任务高效链接起来，并避免了复杂非均匀电路组合的问题，从而提高了证明聚合性能。

---
### [2026/636] From LFSRs to LFGs: Periodicity and Structural Transformations in Stream Ciphers

- **作者:** Shivarama K. N, Susil Kumar Bishoi, Vadiraja Bhatta G. R., Vashek Matyas

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/636) | [PDF](https://eprint.iacr.org/2026/636.pdf)


> **研究背景:** 研究反馈移位寄存器（LFSRs）、多递归矩阵方法（MRMMs）和滞后斐波那契生成器（LFGs）在流密码系统中的基础性作用，探讨了不同配置下的周期性和结构变换。
>
> **主要贡献:** 提出了两种LFSR配置的分析方法，并推导出特定条件下级联系统的精确周期；进一步将字长扩展至m位，并展示了如何通过多个LFSR和简单加法器实现等效的LFG，从而在资源受限环境下提高效率。
>
> **达到效果:** 成功计算了不同LFSR配置下的系统周期性，为设计高效的流密码提供了理论基础。
>
> **技术梗概:** 采用数学分析方法推导周期公式，并通过级联和引入进位机制来研究系统的结构变换。

---
### [2026/637] VeriRAG: Efficient Zero-Knowledge Proofs for Verifiable Retrieval-Augmented Generation

- **作者:** Chenqi Lin, Yubo Cui, Zhelei Zhou, Cheng Hong, Yufei Wang, Zhaohui Chen, Meng Li

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/637) | [PDF](https://eprint.iacr.org/2026/637.pdf)


> **研究背景:** VeriRAG旨在解决检索增强生成(RAG)系统中的数据完整性和真实性问题，特别是在大型语言模型(LLMs)中，恶意提供者可能通过'幻觉'特性绕过检索或声称不存在的数据质量。
>
> **主要贡献:** VeriRAG框架利用零知识证明(ZKP)，在不泄露数据集隐私的情况下，为RAG系统提供了高效的完整性保证。
>
> **达到效果:** 实验结果显示，VeriRAG能够高效地扩展至37GB的数据库规模，并实现了验证者时间为3秒、证明者时间为96秒的效果。
>
> **技术梗概:** 该框架采用了基于近似最近邻搜索(ANNS)的检索策略，并提出了一种创新协议来验证top-$k$排序，同时通过向量查找和块合并策略进行联合优化，以降低验证开销并保持高生成准确性。

---
### [2026/640] MIKE (Module Isogeny Key Exchange): An ἰχθύς introduction

- **作者:** Damien Robert

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/640) | [PDF](https://eprint.iacr.org/2026/640.pdf)


> **研究背景:** 本文介绍了基于Isogeny的密码协议MIKE，这是一种模块化椭圆曲线密钥交换方法。
>
> **主要贡献:** 作者通过直观且基础的方式阐述了该协议，旨在使非专家读者也能理解其核心概念和机制。
>
> **达到效果:** 通过这种方式，文章使得Isogeny基加密技术更加普及，并为相关研究提供了入门指导。
>
> **技术梗概:** 文章采用了简化的方法来解释复杂的数学概念，帮助读者更好地理解和应用MIKE协议。

---
### [2026/642] SoK: The Weakest-Link Principle in Public Key Infrastructures and Modern Mitigation Strategies

- **作者:** Kertis Mwanza, Carsten Köhn

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/642) | [PDF](https://eprint.iacr.org/2026/642.pdf)


> **研究背景:** 随着数字转型的加速，通过层次结构公钥基础设施（PKI）保护通信变得越来越关键。然而，这种基于中心化的信任架构本身存在固有的脆弱性。
>
> **主要贡献:** 本文系统地分析了层次PKI的安全威胁，并提出了基于最弱环节原则的主要贡献，强调整个生态系统仅由其最薄弱的部分决定其安全性。
>
> **达到效果:** 研究揭示了传统撤销机制（如CRL和OCSP）的显著操作性和隐私缺陷，并通过采用分散化的、可验证的协议来应对这些漏洞。
>
> **技术梗概:** 我们评估了证书透明度（CT）作为核心缓解策略，展示了如何使用附录式梅克尔树使错误发行公开可见并进行加密审计。

---
### [2026/644] Ordered Multi-Signatures from the DL Assumption

- **作者:** Keisuke Hara, Keisuke Tanaka, Masayuki Tezuka

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/644) | [PDF](https://eprint.iacr.org/2026/644.pdf)


> **研究背景:** 研究背景：有序多重签名允许多个签署者顺序签署共同消息，并且任何人都可以使用公钥列表验证签署者的签署顺序。现有方案的安全性证明基于更强的假设，旨在提供更可靠的安全保障。
>
> **主要贡献:** 主要贡献：提出了首个基于离散对数假设（DL）的有序多重签名方案，通过泛化Baum等人提出的方案并利用线性哈希函数族实现这一目标。
>
> **达到效果:** 达到的效果：该方案的安全性证明基于线性哈希函数的代数单次预象抗性属性，在随机预言模型中成立。使用满足此属性的特定线性哈希函数，实现了首个基于DL假设的有序多重签名方案。
>
> **技术梗概:** 技术梗概：通过泛化现有的有序多重签名方案，并利用线性哈希函数族和其代数单次预象抗性属性来证明安全性，最终构造了首个基于DL假设的安全方案。

---
### [2026/645] Toward Provable Security in Anamorphic Extension: New Constructions and Analysis

- **作者:** Nabanita Chakraborty, Ratna Dutta

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/645) | [PDF](https://eprint.iacr.org/2026/645.pdf)


> **研究背景:** 在接收方密钥可能被敌手获取的独裁环境下，anamorphic加密允许安全通信。其扩展（AE）增强了这一范式，提供了一种隐蔽通信的能力，同时接收方可以否认这种通信的存在。
>
> **主要贡献:** 作者提出了两种基于数论假设的AE构造：一种是基于Goldwasser-Micali PKE和另一种基于Benaloh PKE，并证明了它们在安全伪随机函数假设下的IND-NA安全性。
>
> **达到效果:** 这两种AE都实现了自然鲁棒性，具有较小的关键大小、较低的计算成本（主要涉及PRF和模运算）、较高的带宽率以及较低的anamorphic开销。
>
> **技术梗概:** 通过引入基于Goldwasser-Micali PKE和Benaloh PKE的具体构造，并证明在安全伪随机函数假设下的IND-NA安全性，作者展示了AE的有效性和效率。

---
### [2026/646] On Optimal Information-Theoretic Security in Symmetric Encryption under Low-Entropy Keys

- **作者:** Haibo Cheng, Haijie Su, Dongyi Li, Wenting Li, Ping Wang

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/646) | [PDF](https://eprint.iacr.org/2026/646.pdf)


> **研究背景:** 研究探讨了在低熵密钥（如密码和生物特征）下对称加密的信息论安全性水平，特别是在经典的安全性概念如完美秘密性和熵安全通常无法实现的情况下。
>
> **主要贡献:** 贡献在于提出了适用于低熵密钥的随机化加密方案，并确定了保证密钥保密性和消息保密性的必要及充分条件。
>
> **达到效果:** 研究结果表明，在密钥保密性方面，最优可实现的安全水平为$C$对密钥的信息量仅提供微不足道的信息；在消息保密性方面，攻击者成功概率的上限为$p_{\max}+\mathsf{negl}(|C|)$。
>
> **技术梗概:** 技术上采用了同态密码和蜜罐加密的方法，并通过构造特定方案来实现最优安全性。

---
### [2026/648] Synthesis of RTL-based Characterization Programs for Fault Injection

- **作者:** Jonah Alle Monne, Guillaume Bouffard, Damien Couroussé, Mathieu Jan

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/648) | [PDF](https://eprint.iacr.org/2026/648.pdf)


> **研究背景:** 故障注入攻击对嵌入式设备的安全构成了重大威胁，现有方法难以全面捕捉微架构层面的故障模型。
>
> **主要贡献:** 提出了一种自动化方法，通过模型检查算法合成特定于目标微架构故障模型的表征程序。
>
> **达到效果:** 该方法在两个RISC-V处理器内核上成功识别了约70%的微架构信号中的位翻转故障，并为CV32E40P的25%控制信号合成了精确归因程序。
>
> **技术梗概:** 采用模型检查算法合成表征程序，评估额外揭示的故障模型，提高微架构层面故障分析的精度和效率。

---
### [2026/652] Counting and recovering the quadratic relations of a vectorial function

- **作者:** Irene Villa

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/652) | [PDF](https://eprint.iacr.org/2026/652.pdf)


> **研究背景:** 研究旨在探讨如何利用CCZ变换掩盖多变量方案中的二次核心映射，并分析由此产生的四次系统。
>
> **主要贡献:** 作者提出了一种方法，用于研究掩码函数的输入与输出之间的二次关系，并将其推广到任何CCZ变换（任意二次映射）。
>
> **达到效果:** 该方法提供了判断一个函数是否能与二次映射CCZ等价以及两个函数之间是否存在CCZ等价性的必要条件。
>
> **技术梗概:** 通过分析掩码函数的输入输出之间的二次关系，作者提出了一种技术来检测和利用这些关系以研究函数间的CCZ等价性。

---
### [2026/653] Random Robust Secret Sharing with Perfect Privacy and its Applications

- **作者:** Mohammad Hassan Ameri, Jeremiah Blocki

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/653) | [PDF](https://eprint.iacr.org/2026/653.pdf)


> **研究背景:** 秘密共享方案允许多个参与者共同持有秘密信息的份额，任何指定数量的份额可以重建原始秘密，而不足此数量的份额则不提供关于秘密的信息。然而，现有的方案如Shamir秘密共享在面对随机份额损坏时缺乏鲁棒性。
>
> **主要贡献:** 作者提出了Random Robust Secret Sharing with Perfect Privacy (RRSS)，该方案同时保持了(t-1)-完美隐私和对随机损坏份额的鲁棒性。
>
> **达到效果:** 通过RRSS，即使多达n-t个独立随机损坏的份额也能以高概率恢复秘密，从而解决了Shamir秘密共享在面对随机损坏时的问题。
>
> **技术梗概:** 该方案通过引入新的构造方法来实现(t-1)-完美隐私和鲁棒性之间的平衡，确保了在部分份额损坏的情况下仍能正确重建秘密。

---
### [2026/654] Tighter Bounds for the Oblivious Bit-Fixing Inner Product Extractor on Biased Seeds

- **作者:** Jack Doerner, Lawrence Roy

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/654) | [PDF](https://eprint.iacr.org/2026/654.pdf)


> **研究背景:** 研究背景：内积提取器(IPE)是密码学中用于从种子和源向量生成共享随机性的重要工具。现有分析依赖于IPE的2-通用性，导致误差与种子偏差的平方根成正比。本文旨在通过改进分析方法减少这种依赖以获得更紧的误差边界。
>
> **主要贡献:** 主要贡献：作者提出了一个提升的一般剩余哈希引理，用于证明几乎n-通用函数的影响，并通过这种方法绕过了普遍哈希的应用，从而获得了更紧的误差界。
>
> **达到效果:** 达到的效果：相比现有结果，新的分析方法将误差与种子偏差的关系从平方根降低到了更低的幂次，为基于内积提取器的多方计算应用提供了更强的支持。
>
> **技术梗概:** 技术梗概：通过证明一个提升的一般剩余哈希引理，并结合对IPE不满足4-通用性的输入数量进行限制，作者成功地减少了误差与种子偏差之间的关系。

---
### [2026/655] Fast and Efficient Perfectly Secure Network-Agnostic Secure Computation

- **作者:** Gilad Asharov, Fatima Elsheimy, Gilad Stern

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/655) | [PDF](https://eprint.iacr.org/2026/655.pdf)


> **研究背景:** 现有的安全多方计算(MPC)协议在同步和异步网络模型中分别实现了高效的通信复杂性和快速的执行速度，但将两者结合在一起仍具有挑战性。
>
> **主要贡献:** 本文提出了第一个在网络无关场景下实现完美安全性且预期轮次为O(D)的安全多方计算协议。
>
> **达到效果:** 该协议在理想安全设置下的预期通信复杂度为O((Cn^2 + Dn^2 + n^4)log n)，相比现有最佳方案，对于小型电路的通信复杂性提高了约n^3倍。
>
> **技术梗概:** 通过引入新的技术方法，本文解决了网络无关性和高效性之间的冲突，实现了在同步和异步模型下同时保持安全性和效率。

---
### [2026/656] Improved Codes and Decoders for HQC

- **作者:** Sebastian Bitzer, Bharath Purtipli, Antonia Wachter-Zeh

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/656) | [PDF](https://eprint.iacr.org/2026/656.pdf)


> **研究背景:** HQC是一种基于汉明准循环码的公钥加密系统，已被NIST选中进行标准化。
>
> **主要贡献:** 研究提出了一个两级通用串联码，并开发了一种基于可靠性的外层解码框架。
>
> **达到效果:** 通过这两项改进，公钥和密文大小最多可以减少4.34%。
>
> **技术梗概:** 该研究利用了内部RM编码包含重复子代码的观察结果，并结合可靠性度量来优化解码过程。

---
### [2026/657] Game Theory Does Not Always Help: The Case of Statistical Multi-Party Coin Tossing

- **作者:** Chen-Da Liu-Zhang, Elisaweta Masserova, João Ribeiro, Sri AravindaKrishnan Thyagarajan

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/657) | [PDF](https://eprint.iacr.org/2026/657.pdf)


> **研究背景:** 研究探讨了多方掷硬币协议在统计安全下的可行性，该协议涉及多个具有潜在冲突利益的参与方共同生成一个公平的随机位。
>
> **主要贡献:** 作者证明，在$ t \geq n/2 $的恶意节点情况下，即使假设广播和有限轮次复杂度，也不存在统计安全性且基于博弈论的掷硬币协议（仅在$n=4$时例外）。此外，未广播的情况下，对于$t \geq n/3$和多项式轮次复杂度，同样没有计算安全性的博弈论掷硬币协议存在（仅当$n=6$时例外）。
>
> **达到效果:** 这些结果填补了统计可行性景观中的空白，并表明在某些恶意节点数量下，博弈论方法无法克服密码学下的不可能性。
>
> **技术梗概:** 通过改进现有的博弈论公平性框架来证明上述结论。

---
### [2026/658] Delegate: Coalition Proof Incentivized Outsourced Computation with Smart Contracts

- **作者:** Osman Biçer, Alptekin Küpçü

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/658) | [PDF](https://eprint.iacr.org/2026/658.pdf)


> **研究背景:** 现有激励外包计算方案通过将行为设为系统的唯一纳什均衡来激励所有承包商进行诚实计算，但这些方案要么仅适用于两承包商情况，要么在多承包商情况下缺乏对完全合作联盟的安全证明。
>
> **主要贡献:** 本文提出了一种基于智能合约的多承包商激励外包计算协议Delegate，并通过承诺机制提出了一个通用可组合的回应提交协议来解决复制攻击问题。
>
> **达到效果:** 该方案能够证明在面对联盟时的安全性，同时解决了之前解决方案仅能阻止但不能完全消除复制攻击的问题。
>
> **技术梗概:** Delegate利用智能合约管理和承包商提交，并结合承诺技术确保响应提交的安全性和完整性。

---
### [2026/659] Reformulating the SNOVA Signature Scheme

- **作者:** Jintai Ding, Hao Guo, Yen-Liang Kuan, Jan Adriaan Leegwater, Peigen Li, Po-En Tseng, Lih-Chung Wang

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/659) | [PDF](https://eprint.iacr.org/2026/659.pdf)


> **研究背景:** SNOVA签名方案的原始形式在不同语言中的表述存在差异，本次研究旨在统一和优化这些表达方式，以增强其安全性和灵活性。
>
> **主要贡献:** 作者提出了一种新的框架来重新构建SNOVA，并分析了新方案的安全性。该改革案允许更灵活地选择参数集，特别适用于奇数特征域，从而减小密钥大小并提高抗攻击能力。
>
> **达到效果:** 通过使用新框架，研究团队成功设计了多个参数集，这些参数集的证书大小低于一千字节，并且在某些方面具有竞争力。
>
> **技术梗概:** 研究采用了环方程形式、鞭打形式和张量形式来重新表述SNOVA，并基于此进行了安全分析。

---
### [2026/661] Pseudorandomness of UFLM: A Characterization via Its Linear Layer

- **作者:** Tingting Guo, Peng Wang, Gang Liu

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/661) | [PDF](https://eprint.iacr.org/2026/661.pdf)


> **研究背景:** 本文系统分析了在选择明文和选择密文攻击下，具有独立随机轮函数的双分支统一Feistel Lai Massey (UFLM)结构的安全性，特别关注其与随机置换的不可区分性。
>
> **主要贡献:** 研究者证明了当$A_{12}$满秩时，UFLM需要最少轮数以实现CPA和CCA安全，并且达到最高的查询上限。此外，对于非满秩的情况，通过增加轮数也可以实现CPA和CCA安全性。
>
> **达到效果:** 研究表明，对于具有足够轮数的UFLM，其查询界限主要由$A_{12}$的秩决定；而对于轮数不足的安全情况，则提出了最多需要四次查询的成功区分攻击。
>
> **技术梗概:** 研究采用了矩阵理论中的参数$T(A_{12}^{	op}, A_{11}^{	op})$和$T(A_{12}, A_{22})$来确定UFLM的安全轮数，并通过分析这些参数的值来区分攻击。

---
### [2026/664] Expanders Meet Reed--Muller: Easy Instances of Noisy k-XOR

- **作者:** Jarosław Błasiok, Paul Lou, Alon Rosen, Madhu Sudan

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/664) | [PDF](https://eprint.iacr.org/2026/664.pdf)


> **研究背景:** 研究背景：在噪声$k$-XOR问题中，给定一个向量$y \in \mathbb{F}_2^M$，需要区分它是均匀分布还是由线性约束和随机噪声生成。该问题的研究与图的扩张性质紧密相关，猜想良好的扩展性会导致计算复杂度下界。
>
> **主要贡献:** 主要贡献：作者通过结合伪随机性和编码理论中的两个重要方向，构建了一类具有接近最优扩展性的显式图结构，使得在恒定噪声率$\eta = 1/3$的情况下，噪声$k$-XOR问题可以在多项式时间内求解。
>
> **达到效果:** 达到的效果：证明了关于扩张性与计算复杂度下界之间关系的猜想是错误的，并提供了噪声$k$-XOR问题可多项式时间求解的具体实例。
>
> **技术梗概:** 技术梗概：通过使用Guruswami, Umans和Vadhan提出的无损扩展器构建图结构，结合Reed-Muller码的大规模随机错误校正方法，实现了上述结果。

---
### [2026/665] Applications of Bruhat-Chevalley-Renner Decomposition to Metric-Aware Code-Based Cryptography

- **作者:** Mahir Bilen Can, Eli Coe Naig

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/665) | [PDF](https://eprint.iacr.org/2026/665.pdf)


> **研究背景:** 本文旨在通过引入Niederreiter-Rosenbloom-Tsfasman (NRT) 和求和秩度量来扩展码基密码学的应用，超越传统的汉明度量，并利用Bruhat-Chevalley-Renner分解的线性等距群结构。
>
> **主要贡献:** 贡献在于提出了基于NRT度量的内-外Niederreiter密码系统设计，并通过不变距离测试和轨道结构分析来增强系统的安全性。
>
> **达到效果:** 结果证明了该矩阵码的距离保证，并提供了一种简单的两阶段解码器，同时保持了可解性并隐藏了结构信息。此外，将NRT和求和秩度量的综合解码问题归约为经典的汉明/秩解码问题，从而确保了公共综合征映射的一次性。
>
> **技术梗概:** 技术上利用了Bruhat-Chevalley-Renner分解来设计内-外Niederreiter密码系统，并通过不变距离测试和轨道结构分析来提高系统的安全性。

---

## 更新: 2026-03-27 19:08

*新增 9 篇论文 (编号 597--605)*

### [推荐] [2026/597] Efficiency Improvement of Deniable FHE: Tighter Deniability Analysis and TFHE-based Construction

- **匹配关键字:** homomorphic encryption

- **作者:** Towa Toyooka, Yohei Watanabe, Mitsugu Iwamoto

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/597) | [PDF](https://eprint.iacr.org/2026/597.pdf)


> **研究背景:** 研究背景：全同态加密（FHE）允许在不解密的情况下对密文进行计算，而可否认加密则使用户能够在被迫透露密文时撒谎。将这两种技术结合的可否认全同态加密（DFHE）旨在提供更高的隐私保护。
>
> **主要贡献:** 主要贡献：作者通过提供更紧的可否认性上界分析，减少了存储随机性和所需执行的启动验证次数，从而改进了DFHE的效率。
>
> **达到效果:** 达到的效果：该研究降低了存储的空间需求，并提高了执行速度，特别是在使用TFHE方案时效果显著。
>
> **技术梗概:** 技术梗概：通过改进可否认性分析方法，作者优化了基于BGV和TFHE方案的DFHE构造过程。

---
### [推荐] [2026/600] Hadal: Centralized Label DP Training without a Trusted Party

- **匹配关键字:** homomorphic encryption

- **作者:** James Choncholas, Stanislav Peceny, Amit Agarwal, Mariana Raykova, Baiyu Li, Karn Seth

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/600) | [PDF](https://eprint.iacr.org/2026/600.pdf)


> **研究背景:** 研究背景：在特征由一方持有、标签由另一方持有的分布式训练场景中，如何保护标签隐私并避免依赖可信第三方成为挑战。
>
> **主要贡献:** 主要贡献在于提出PostScale协议和Hadal框架，实现了高隐私设置下的模型训练，并显著减少了通信量和训练时间。
>
> **达到效果:** 达到的效果是，在保持与中心化DP相似的模型性能的同时，将每批次的通信量从1 TB减少到8 GB，训练时间缩短了99%。
>
> **技术梗概:** 技术梗概包括HE协议PostScale、多党采样噪声生成协议以及Hadal框架，该框架支持加密计算并优化执行效率。

---
### [推荐] [2026/603] Oblivious SpaceSaving: Heavy-Hitter Detection over Fully Homomorphic Encryption

- **匹配关键字:** homomorphic encryption

- **作者:** Sohaib .., Divyakant Agrawal, Amr El Abbadi

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/603) | [PDF](https://eprint.iacr.org/2026/603.pdf)


> **研究背景:** 在流数据分析中，重 hitter 检测是基础的计算原语之一，应用于网络监控、遥测和大规模数据系统。然而，在许多实际部署场景下，必须在提供更高可用性和集中运维控制的远程基础设施上持续进行此计算，即使底层流包含敏感标识符或专有活动模式。现有的隐私保护方法要么引入大量统计噪声，要么依赖多服务器信任假设。
>
> **主要贡献:** 我们提出了Oblivious SpaceSaving，这是一种对经典Space-Saving算法进行了隐私保护重构的方法，使其能够在单个未受信的服务器上进行完全加密执行。我们的核心思想是Moving Floor抽象，它利用摘要状态中的单调性不变量来用等式选择替换重复的大小比较，并结合并行受害者选择和分层异步摄取管道，从而实现端到端加密重 hitter 架构，同时保持原始算法的确定性准确性保证。
>
> **达到效果:** 我们的设计将加密更新的成本降低了最多2.74倍，相比朴素的方法，显著提高了效率。此外，该方法还能够精确地在未受信服务器上执行流处理任务，而不会泄露任何敏感信息。
>
> **技术梗概:** 我们通过引入Moving Floor抽象和结合并行受害者选择以及分层异步摄取管道来优化算法的实现。这种方法利用了加密数据上的单调性不变量，并减少了重复大小比较的开销，从而提高了整体性能。

---
### [推荐] [2026/604] CatCrypt: From Rust to Cryptographic Security in Lean

- **匹配关键字:** post-quantum

- **作者:** Bas Spitters

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/604) | [PDF](https://eprint.iacr.org/2026/604.pdf)


> **研究背景:** CatCrypt是一个在Lean中实现的库，用于机器验证密码学安全证明，从Rust参考实现到计算模型的安全证明。
>
> **主要贡献:** 该研究贡献了一种将Rust代码转换为Lean形式化证明的方法，并覆盖了172个加密协议和构造，其中110个具有完整的Rust-to-Lean流水线。
>
> **达到效果:** CatCrypt实现了从Rust到Lean的端到端管道，所有边界都系统地与已发布的来源进行了交叉引用，提高了对规格正确性的信心，并在两个月内完成了整个项目。
>
> **技术梗概:** 使用Hax工具进行从Rust到Lean的翻译，部分证明是从其他形式化验证工具如SSProve、EasyCrypt等移植过来的，大部分是独立的形式化实现。

---
### [2026/598] Triangulating Meet-in-the-Middle Attack

- **作者:** Boxin Zhao, Qingliang Hou, Lingyue Qin, Xiaoyang Dong

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/598) | [PDF](https://eprint.iacr.org/2026/598.pdf)


> **研究背景:** 本文旨在通过改进的三角化中间相遇攻击（Triangulating MitM）来降低内存复杂度，以突破更多轮次的AES等加密算法。
>
> **主要贡献:** 作者提出了一种基于改进三角化算法的新MitM攻击方法，并成功应用于多种加密算法，显著降低了攻击所需的内存复杂度。
>
> **达到效果:** 通过该方法，针对4/5轮AES-128的单密文密钥恢复攻击内存复杂度从$2^{80}$降至实践中的$2^{24}$或从$2^{96}$降至$2^{40}$；同时提出了针对减缩版AES-192/-256和Rijndael-EM的新攻击方法。
>
> **技术梗概:** 作者利用Khovratovich等人的三角化算法（TA）并结合LaMacchia等人和Bender等人的结构高斯消元法，改进了TA以处理仍有许多未处理方程但无变量仅存在于单一方程的情况。

---
### [2026/599] Proving modern code-based dual attacks with second-order techniques

- **作者:** Charles Meyer-Hilfiger

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/599) | [PDF](https://eprint.iacr.org/2026/599.pdf)


> **研究背景:** 研究背景在于代码基密码学中，最近的双重攻击通过将解码问题转化为LPN问题得到了改进，并且在某些情况下超越了信息集解码器。然而，这些攻击的分析目前仍依赖于启发式方法而非严格证明。
>
> **主要贡献:** 主要贡献是提出了一种无需使用任何模型即可完全证明的新变体双重RLPN算法。该算法与原始版本相比，在性能上仅相差多项式因子，并且其分析更为简单。
>
> **达到效果:** 结果表明，通过翻转噪声码字的坐标并观察相关LPN问题中噪音量的细微变化来重建整个错误，从而实现了这一目标。
>
> **技术梗概:** 技术梗概涉及利用第二阶技巧对双重RLPN算法进行改进，并基于傅里叶理论和随机线性代码权重枚举的泊松近似来进行分析。

---
### [2026/601] Cryptanalysis of the Lightweight Stream Cipher RRSC

- **作者:** Shivarama K. N., Susil Kumar Bishoi

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/601) | [PDF](https://eprint.iacr.org/2026/601.pdf)


> **研究背景:** 本文对RRSC轻量级流密码在64位和128位变体的安全性进行了评估，重点关注密钥更新过程、内部组件交互及初始化期间的扩散行为。
>
> **主要贡献:** 研究提出了针对RRSC的各种攻击场景，包括时间-内存-数据权衡攻击、已知明文设置下的完整密钥恢复攻击以及针对线性和非线性反馈移位寄存器部件的部分密钥恢复攻击。
>
> **达到效果:** 研究表明，128位变体的有效密钥空间从\(2^{128}\)减少到\(2^{96}\)，而64位变体则从\(2^{64}\)减少到\(2^{48}\)。
>
> **技术梗概:** 分析通过实施雪崩研究来检验组件间的交互，并基于观察结果探索了多种攻击场景。

---
### [2026/602] Confidential Transfers for Multi-Purpose Tokens on the XRP Ledger

- **作者:** Murat Cenk, Aanchal Malhotra, Joseph A. Akinyele

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/602) | [PDF](https://eprint.iacr.org/2026/602.pdf)


> **研究背景:** 该研究旨在为XRP Ledger上的多用途代币引入保密转移功能，以保护交易金额和账户余额的隐私性，同时保持供应量的公开验证。
>
> **主要贡献:** 贡献在于设计了一种基于EC-ElGamal加密和非交互式零知识证明的协议，使得转账正确、余额充足以及最大发行量不变，无需验证者解密即可实现保密转移。
>
> **达到效果:** 该协议成功实现了多用途代币的保密性与透明性的平衡，同时保持了现有功能的兼容性和可审计性，增强了XRP Ledger的安全性和灵活性。
>
> **技术梗概:** 通过使用EC-ElGamal加密来隐藏账户余额和交易金额，并利用非交互式零知识证明确保转账的有效性，同时设计了基于多密文余额表示和等式证明的选择披露模型以满足监管要求。

---
### [2026/605] Adaptively-Secure Proxy Re-Encryption with Tight Security

- **作者:** Chen Qian, Shuo Chen, Shuai Han

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/605) | [PDF](https://eprint.iacr.org/2026/605.pdf)


> **研究背景:** 现有的代理重新加密方案在适应性攻击下安全性会显著下降，仅少数方案实现了接近多项式的时间安全损失，且限制了重加密策略。
>
> **主要贡献:** 作者提出了四个基于MDDH假设的适应性安全代理重新加密方案，并引入了一种新的标签基语言可变归零知识证明。
>
> **达到效果:** 这些方案在单挑战和多挑战下分别实现了几乎紧致的安全性和适应性选择明文攻击下的紧致安全性。
>
> **技术梗概:** 通过引入标签基语言可变归零知识证明，确保了模拟声学的同时保留了一种受限形式的可变性。

---

## 更新: 2026-03-26 21:28

*新增 6 篇论文 (编号 591--596)*

### [推荐] [2026/592] Performance Analysis of Parameterizable HQC Hardware Architecture

- **匹配关键字:** post-quantum

- **作者:** Nishant Pandey, Sanjay Deshpande, Dixit Dutt Bohra, Debapriya Basu Roy, Dip Sankar Banerjee, Jakub Szefer

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/592) | [PDF](https://eprint.iacr.org/2026/592.pdf)


> **研究背景:** 本文针对NIST后量子密码学标准制定过程中选定的基于Hamming Quasi-Cyclic (HQC)码的密钥封装机制，在硬件实现上进行了性能分析，旨在克服现有实现中受限于面积而导致的低效问题。
>
> **主要贡献:** 作者提出了一种可参数化的、灵活的数据宽度硬件设计，该设计能够根据不同的性能目标和安全级别进行配置，并在Verilog中实现了HQC的关键生成、封装和解封装模块。
>
> **达到效果:** 通过优化稀疏多项式乘法器和固定权重向量生成器等模块，作者的设计显著提高了吞吐量并减少了面积-时间（AT）产品，在Xilinx Artix 7 FPGA上实现时，达到了比现有最高效统一HQC硬件设计更好的性能。
>
> **技术梗概:** 该设计通过共享SHAKE256哈希核心来最小化面积开销，并引入了针对稀疏多项式乘法器和固定权重向量生成器的优化技术。

---
### [推荐] [2026/595] Registration-Optimized Dynamic Group Time-based One-time Passwords for Mobile Access

- **匹配关键字:** post-quantum

- **作者:** Jiaqing Guo, Xuelian Cao, Zengpeng Li, Yong Zhou, Zheng Yang, Jianying Zhou

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/595) | [PDF](https://eprint.iacr.org/2026/595.pdf)


> **研究背景:** 针对公共金融和企业环境中轻量级匿名认证的需求，提出了Group Time-based One-Time Passwords（GTOTP），以实现用户在不泄露身份的情况下证明授权。然而，现有方案DGTOne存在动态组成员管理及容量浪费等问题，影响了移动访问中的离线验证需求。
>
> **主要贡献:** 本文提出NWDGT和LWDGT两种新方案，分别通过构建按需生成的VP树和使用多个小型一次性签名树来解决上述问题，提高了系统的灵活性和效率。
>
> **达到效果:** 实验结果表明，与DGTOne相比，NWDGT和LWDGT显著减少了容量浪费，并且能够在不牺牲安全性的前提下实现高效的离线验证。
>
> **技术梗概:** NWDGT通过动态构建VP树来避免过期节点的使用；而LWDGT则利用一次性签名树分批处理新成员的身份验证请求，从而减少延迟和提高资源利用率。

---
### [2026/591] A Note on HCTR++

- **作者:** Mustafa Khairallah

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/591) | [PDF](https://eprint.iacr.org/2026/591.pdf)


> **研究背景:** 本文指出了Öztürk等人提出的HCTR++构造中存在的基本正确性缺陷，该缺陷导致解密算法无法正确反转加密算法。
>
> **主要贡献:** 作者独立发现了这一漏洞，并通过提供算法给AI模型进行验证以展示其发现过程的透明度。
>
> **达到效果:** 研究揭示了HCTR++设计中的一个关键错误，使得方案不可逆。
>
> **技术梗概:** 通过对比分析加密和解密算法，识别出算法间的不一致性问题。

---
### [2026/593] Three-Move Blind Signatures in Pairing-Free Groups

- **作者:** Yanbo Chen

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/593) | [PDF](https://eprint.iacr.org/2026/593.pdf)


> **研究背景:** 该研究旨在设计一种既不依赖对数阶群模型（AGM），也不使用配对的三轮盲签名方案，以填补现有技术中的空白。
>
> **主要贡献:** 作者提出了一种同时满足无配对、非AGM标准假设下并发安全性的三轮盲签方案，并且是首次在无需AGM的情况下实现这一目标。
>
> **达到效果:** 该方案的公钥、签名以及通信量均仅由固定数量的群/域元素组成，显著提高了效率和实用性。
>
> **技术梗概:** 通过巧妙设计协议交互流程及利用随机预言机模型，在不依赖配对运算的前提下实现了并发安全性证明。

---
### [2026/594] Efficient Compilers for Verifiable Dynamic Searchable Symmetric Encryption

- **作者:** Chaya Ganesh, Sikhar Patranabis, Raja Rakshit Varanasi

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/594) | [PDF](https://eprint.iacr.org/2026/594.pdf)


> **研究背景:** 研究背景：本文旨在解决动态搜索加密（DSSE）在面对恶意服务器时的安全性问题，通过构建编译器将现有的半诚实服务器安全的DSSE方案转化为恶意服务器安全的验证型动态搜索加密（VDSSE）。
>
> **主要贡献:** 主要贡献在于提出了两个高效的编译器$\mathsf{FLASH}$和$\mathsf{BOLT}$，分别优化了通信开销和客户端存储需求。
>
> **达到效果:** 达到的效果是实现了在保持前向和后向隐私的同时，对现有半诚实DSSE方案进行转换，使其具备恶意服务器安全性，并且实验验证了这些编译器在实际数据库上的性能表现优异。
>
> **技术梗概:** 技术梗概：定义并实现了一种新的认证数据结构——集合承诺（Set Commitment），以此为基础构建高效的VDSSE方案。

---
### [2026/596] Gryphes: Hybrid Proofs for Modular SNARKs with Applications to zkRollups

- **作者:** Jiajun Xin, Samuel Cheung On Tin, Christodoulos Pappas, Yongjin Huang, Dimitrios Papadopoulos

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/596) | [PDF](https://eprint.iacr.org/2026/596.pdf)


> **研究背景:** 针对处理多种计算任务（如可扩展的zkRollup应用）的需求，现有SNARKs和zkVM在通用性和效率之间存在权衡。
>
> **主要贡献:** 提出Gryphes框架，结合矩阵查找与特定加密操作的SNARK解决方案，实现高效且灵活的证明系统。
>
> **达到效果:** 构建了一个基于Groth16签名和RSA累加器的zkRollup原型，实现了高效的证明、恒定大小的证明以及数千种交易类型的动态支持。
>
> **技术梗概:** Gryphes通过引入新型高效链接协议，将矩阵查找与Plonk等通用SNARKs无缝集成，优化了效率和适应性。

---

## 更新: 2026-03-25 20:20

*新增 9 篇论文 (编号 582--590)*

### [推荐] [2026/582] FrozenTRU: Cold Boot Attacks on NTRU-Based Hash-and-Sign Signatures

- **匹配关键字:** lattice

- **作者:** Hiroto Kaihara, Mehdi Tibouchi, Masayuki Abe

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/582) | [PDF](https://eprint.iacr.org/2026/582.pdf)


> **研究背景:** 冷启动攻击是一种恢复计算机关机后存储在易失性内存中的加密密钥的技术，即使在低温下内存内容也能部分保留。针对基于NTRU的签名方案Falcon及其前身DLP方案，研究了冷启动攻击的有效性。
>
> **主要贡献:** 提出了FrozenTRU方法，该方法利用浮点数表示的秘密密钥进行分析，并成功地展示了如何从冷启动攻击中恢复这些方案的私钥。
>
> **达到效果:** 在可实现的位翻转概率下，通过冷冻TRU方法能够部分或完全恢复NTRU基签名方案Falcon和DLP的私钥，证明了这些方案对于冷启动攻击的脆弱性。
>
> **技术梗概:** 该研究采用了一种新颖的方法来处理浮点数误差，并结合统计分析技术，以提高从冷启动数据中提取有效信息的能力。

---
### [2026/583] SoK: Updatable Public-Key Encryption

- **作者:** Mark Manulis, Daniel Slamanig, Federico Valbusa

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/583) | [PDF](https://eprint.iacr.org/2026/583.pdf)


> **研究背景:** 研究背景：可更新公钥加密是一种允许密钥随时间演变的广义概念，旨在支持安全的密钥轮换并限制密钥泄露的影响。这种机制在诸如安全外包存储、安全消息传递或低延迟前向保密密钥交换协议等多种应用场景中具有重要作用。
>
> **主要贡献:** 主要贡献：作者提供了一个分类体系，澄清了文献中使用的术语差异，并对比了现有定义、语法和形式安全性模型之间的异同，为该领域的研究提供了清晰的框架。
>
> **达到效果:** 达到的效果：通过系统化这一领域，作者帮助研究人员更好地理解当前术语的混乱状态，并促进了不同方案之间更为有效的比较与整合。
>
> **技术梗概:** 技术梗概：通过对文献进行深入分析和对比，作者识别并定义了多种可更新公钥加密方案的不同变体及其触发机制，强调了它们在实现前向保密性和后密钥泄露安全性方面的作用。

---
### [2026/584] Analyzing the WebRTC Ecosystem and Breaking Authentication in DTLS-SRTP

- **作者:** Martin Bach, Vukašin Karadžić, Lukas Knittel, Robert Merget, Jean Paul Degabriele

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/584) | [PDF](https://eprint.iacr.org/2026/584.pdf)


> **研究背景:** DTLS-SRTP被设计用于保护实时媒体通信，广泛应用于Zoom、Teams和Google Meet等主流音频和视频通话平台。然而，其复杂的系统结构使得全面审计变得极其困难，导致该核心技术的安全性研究不足。
>
> **主要贡献:** 本文开发了一种自动化中间人攻击测试框架（DTLS-MitM-Scanner (DMS)），用于检测DTLS-SRTP连接中的DTLS通道安全性，并对24个服务提供商的浏览器和移动应用进行了案例研究。
>
> **达到效果:** 研究发现，在33个测试的媒体服务器实现中，有19个存在漏洞，允许攻击者在DTLS层破解认证机制。对于其中9个影响数亿用户的系统，研究人员还证明了这些系统的可利用性。
>
> **技术梗概:** 通过使用自动化中间人攻击测试框架（DMS），对DTLS-SRTP的DTLS通道进行了全面的安全性评估，并特别关注了认证机制中的19种潜在漏洞。

---
### [2026/585] Format-Preserving Compression-Tolerating Authenticated Encryption for Images

- **作者:** Alexandra Boldyreva, Kaishuo Cheng, Jehad Hussein

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/585) | [PDF](https://eprint.iacr.org/2026/585.pdf)


> **研究背景:** 研究背景：针对图像的可压缩性认证加密方案，确保在图像经过压缩后仍能正确解密并保持视觉相似度，同时提供形式化的安全分析。
>
> **主要贡献:** 主要贡献：提出了一种格式保留、抗压缩的认证加密方案，并特别设计了适用于JPEG格式的构造方法，使用标准的对称密码工具和特殊预处理及后处理步骤。
>
> **达到效果:** 达到的效果：通过正式的安全评估，参数选择实验以及性能研究，实现了在图像经过压缩后仍能成功解密并保持视觉质量的目标。
>
> **技术梗概:** 技术梗概：采用形式化定义安全目标，结合JPEG格式特性设计加密方案，并通过实验证明了方案的有效性及效率。

---
### [2026/586] Bulletproofs*: Verifier-Efficient Arithmetic Circuit Proofs via Folding

- **作者:** Emanuele Scala, Daniele Bartoli

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/586) | [PDF](https://eprint.iacr.org/2026/586.pdf)


> **研究背景:** Bulletproofs* 是对 Bulletproofs 协议的改进，旨在提高验证器效率并适用于标准假设下的算术电路证明。
>
> **主要贡献:** 该研究通过适应 Bulletproofs 的代数验证器并设计折叠方案，实现了在无需预处理的情况下对算术电路满足性语言的支持。
>
> **达到效果:** 经过折叠转换后的验证成本分析表明，Bulletproofs* 达到了理论上的线性效率提升。
>
> **技术梗概:** 研究采用了折叠技术，并通过修改协议保持其安全性来实现高效的验证器设计。

---
### [2026/587] Speeding Up Sum-Check Proving (Extended Version)

- **作者:** Quang Dao, Zachary DeStefano, Suyash Bagad, Yuval Domb, Justin Thaler

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/587) | [PDF](https://eprint.iacr.org/2026/587.pdf)


> **研究背景:** sum-check协议作为现代密码学证明系统中的基础组件，其证明者的成本已成为实际应用中的瓶颈。
>
> **主要贡献:** 作者提出了三种互补的技术来显著减少sum-check证明的时间和内存消耗，特别是在零知识虚拟机(zkVM)的上下文中。
>
> **达到效果:** 通过这些技术，在Jolt zkVM中实现了超过一个数量级的运行时加速和内存减少，并在关键高阶度sum-check子协议上获得了1.7到2.2倍的速度提升。
>
> **技术梗概:** 第一种技术针对多项式乘积的应用，开发了一种新的算法以显著减少所需的字段乘法次数；第二种技术为小值sum-check证明者设计了算法，加速了常见的64或32位整数或小型子域元素的求和场景；第三种技术通过利用等式多项式的可分解张量结构，在一个因子是等式多项式的情况下几乎消除了证明者的开销。

---
### [2026/588] Tailored Limb Counts, Faster Arithmetic: Improved TMVP Decompositions for Curve5453 and Curve6071

- **作者:** Murat Cenk, N. Gamze Orhon Kılıç, Halil Kemal Taşkın, Oğuz Yayla

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/588) | [PDF](https://eprint.iacr.org/2026/588.pdf)


> **研究背景:** 研究了Montgomery曲线Curve5453和Curve6071在大素数域上的椭圆曲线密码学应用，旨在优化这些曲线上基于TMVP的字段乘法运算效率。
>
> **主要贡献:** 提出了针对特定曲线选择不同基数下的肢计数方法，以减少TMVP分解中的乘法次数。
>
> **达到效果:** 通过调整 limb 计数和使用分层块级 TMVP，实现了 Curve5453 和 Curve6071 的字段乘法运算速度分别提高了 22% 和 30%，并在 ARM64 和 x86-64 平台上验证了这些优化。
>
> **技术梗概:** 通过选择合适的 limb 计数来生成 $3 	imes 3$ Toeplitz 块，并利用大小为 3 的 TMVP 公式，每个块的乘积计算减少了所需的乘法次数。

---
### [2026/589] FROSTLASS: Flexible Ring-Oriented Schnorr-like Thresholdized Linkably Anonymous Signature Scheme

- **作者:** Joshua Babb, Brandon Goodell, Rigo Salazar, Freeman Slaughter, Luke Szramowski

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/589) | [PDF](https://eprint.iacr.org/2026/589.pdf)


> **研究背景:** FROST是一种实用的Schnorr签名阈值化方法，允许多个参与者共同签署消息。FROSTLASS在此基础上进一步增强了链上应用的安全性和匿名性。
>
> **主要贡献:** FROSTLASS引入了新颖的可追踪性和匿名性保证，并通过'Schnorr-shaped hole'技术证明了良好的安全性。
>
> **达到效果:** 该方案提高了Monero等区块链的安全性和实用性，能够在实际场景中有效防止恶意攻击并保护用户隐私。
>
> **技术梗概:** FROSTLASS利用Schnorr签名的特性设计了一种特殊的‘洞’结构来实现所需的安全属性。

---
### [2026/590] On the Security of Constraint-Friendly Map-to-Curve Relations

- **作者:** Youssef El Housni, Benedikt Bünz

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/590) | [PDF](https://eprint.iacr.org/2026/590.pdf)


> **研究背景:** 研究背景：Groth等人提出了一种新的映射到椭圆曲线关系，旨在减少约束系统中的电路大小，并在椭圆曲线上提供了安全证明。然而，该方案存在安全边界未明确分析、通用组模型不适用于实际部署的曲线以及对字段限制的要求等问题。
>
> **主要贡献:** 主要贡献：作者识别并解决了上述问题，提出了一个改进的y增量变体，消除了代数攻击，并放宽了对字段的限制，同时保持了与原方案相当的约束数量。
>
> **达到效果:** 达到的效果：通过实现在开源gnark库中的两种构造，并使用SageMath进行了自我包含的模拟验证，证明了改进方案的有效性。
>
> **技术梗概:** 技术梗概：采用y增量方法来消除代数攻击，同时放宽对椭圆曲线字段的要求，并在Go和Rust实现中进行了性能测试。

---

## 更新: 2026-03-24 21:23

*新增 6 篇论文 (编号 576--581)*

### [2026/576] Radical 3-isogenies for the ideal class group actions on $(2, \varepsilon)$-structures

- **作者:** Masaomi Shibata, Hiroshi Onuki, Tsuyoshi Takagi

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/576) | [PDF](https://eprint.iacr.org/2026/576.pdf)


> **研究背景:** 研究背景：Chenu和Smith引入了$(d,\varepsilon)$-结构的概念，这对椭圆曲线密码学中的理想类群作用提供了基础。针对$d=2$的情况，本文旨在提供高效的方法来评估上述作用。
>
> **主要贡献:** 主要贡献在于提出了利用$\mathbb{Q}$-曲线和Montgomery曲线的两种表示方法，设计了高效的根3-isogenies，以实现特定素理想类的作用。
>
> **达到效果:** 达到的效果是提出了一种新的算法，能够更高效地执行理想类群作用于$(2,\varepsilon)$-结构的操作，从而改进了Delfs-Galbraith算法。
>
> **技术梗概:** 技术梗概：本文通过利用$\mathbb{Q}$-曲线和Montgomery曲线的表示方法，设计并实现了根3-isogenies来评估理想类群作用，并展示了如何将任何$(2,\varepsilon)$-结构表示为一个曲线系数和单一符号。

---
### [2026/577] Two Decades of Identity-Based Identification Schemes- A Survey on Challenges and Advances

- **作者:** Apurva Kiran Vangujar, Paolo Palmieri, Ji-Jian Chin, Swee-Huay Heng

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/577) | [PDF](https://eprint.iacr.org/2026/577.pdf)


> **研究背景:** 身份基识别（IBI）方案因其高效的性能和可扩展性在密码学领域获得了广泛应用，但近年来提出的大量IBI方案使得有效比较和评估变得困难。
>
> **主要贡献:** 该综述首次提出了IBI方案的一般分类法，并基于其安全假设进行了系统分类和评价；同时分析了IBI方案的计算和通信成本，指出了实施过程中遇到的各种挑战和限制。
>
> **达到效果:** 通过对比不同类别的IBI方案的安全性、效率、优缺点，为研究人员和开发人员提供了深入理解该快速发展的领域的指导，并确定了当前的研究空白并提出了未来方向。
>
> **技术梗概:** 采用严格的综述方法，对各种硬度假设下的IBI方案进行了全面的文献回顾和分析，引入了一种新的分类法以系统地评估这些方案。

---
### [2026/578] How Much Verifier's Dilemma and Staking Pools Adversely Affect Decentralization of Ethereum PoS under Realistic Operational Costs? (Extended Version)

- **作者:** Ivan Homoliak, Martin Hruby, Martin Peresini, Kristian Kostal, Daria Smuseva

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/578) | [PDF](https://eprint.iacr.org/2026/578.pdf)


> **研究背景:** 研究探讨了验证者困境（VD）和质押池对以太坊PoS共识协议去中心化的影响，特别是在实际运营成本下的表现。
>
> **主要贡献:** 通过演化博弈理论和复制子方程模型，分析了三种验证者策略之间的竞争，并揭示了这些因素如何影响长期网络的去中心化程度。
>
> **达到效果:** 研究发现，由于VD和较低的操作成本，懒惰策略和加入质押池策略对网络去中心化的负面影响显著，而诚实策略则面临较高的硬件运营成本挑战。
>
> **技术梗概:** 利用演化博弈理论和复制子方程构建模型来模拟不同验证者策略之间的竞争，并量化其对网络去中心化的影响。

---
### [2026/579] PRIVADA: Private user-centric Data Aggregation

- **作者:** Betul Askin Ozdemir, Beyza Bozdemir, Ionut Groza, Melek Önen

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/579) | [PDF](https://eprint.iacr.org/2026/579.pdf)


> **研究背景:** 隐私保护的数据聚合已成为AI驱动和基于云系统的大型数据分析的基本工具，但现有解决方案在多重数据客户环境中难以同时确保用户匿名性、选择性披露和结果隐私。
>
> **主要贡献:** PRIVADA通过SPDZ框架下的MPC提供恶意安全的数据聚合方案，支持多个数据客户并防止推断用户的参与情况及抵制现实世界中的合谋行为。
>
> **达到效果:** PRIVADA在确保输入隐私的同时也保证了用户和结果的隐私性，并且相比现有最佳解决方案，在提供对参与方的安全性方面表现出色，实验结果显示性能提升了12-15倍。
>
> **技术梗概:** PRIVADA采用SPDZ框架下的MPC技术实现恶意安全的数据聚合，简化了聚合操作并增强了大规模部署中的强隐私保证。

---
### [2026/580] Exploiting noisy single-bit leakage in ML-DSA

- **作者:** Kaveh Bashiri, Jan Geuenich, Johannes Mittmann

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/580) | [PDF](https://eprint.iacr.org/2026/580.pdf)


> **研究背景:** ML-DSA实现中，部分泄露掩码向量$oldsymbol{y}$的单比特噪声信息构成严重威胁，即使在高噪声环境下累积少量签名的泄漏也能恢复密钥。
>
> **主要贡献:** 研究提出了新的攻击方法，能够在理论上所需的最小签名数附近成功恢复密钥，并分析了不同错误概率和泄露位数对攻击效果的影响。
>
> **达到效果:** 实验结果显示，在误差概率高达0.49的情况下，攻击仍能有效工作；对于指数不低于四或五的泄露比特位置，攻击比先前方法更具普适性。
>
> **技术梗概:** 通过建立随机模型精确计算所需签名数量，并开发了适用于高噪声环境的新攻击技术。

---
### [2026/581] vkproof: Succinct verification of indexed verifying keys using modular compilation and polynomial fingerprinting

- **作者:** Antonio Mejias Gil, Xueqin Zhao

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/581) | [PDF](https://eprint.iacr.org/2026/581.pdf)


> **研究背景:** vkproof旨在为Varuna验证密钥提供一种简洁的预处理SNARG方案，特别适用于包含复杂函数（如哈希）作为程序指令的情况。
>
> **主要贡献:** 该工作通过模块化编译和指纹技术实现了验证器成本与程序指令数量成线性关系，并扩展了Marlin模型以支持实例和查询中的多项式见证和线性组合验证。
>
> **达到效果:** vkproof能够保持常数级的证明大小，同时显著降低验证者成本，使其在处理复杂函数时更具优势。
>
> **技术梗概:** 通过模块化编译程序并利用指纹技术验证多项式的正确性，vkproof实现了验证器成本与程序指令数量成线性关系。

---

## 更新: 2026-03-23 22:07

*新增 18 篇论文 (编号 557--575)*

### [推荐] [2026/557] On Post-Quantum Signature with Message Recovery from Hash-and-Sign in QROM

- **匹配关键字:** post-quantum

- **作者:** Bohang Chen, Shuai Han, Shengli Liu

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/557) | [PDF](https://eprint.iacr.org/2026/557.pdf)


> **研究背景:** 传统的哈希签名方案在后量子时代面临效率低下问题，而具有消息恢复功能的签名方案能够嵌入部分消息而不增加签名长度，从而减少空间消耗。然而，在后量子安全环境中设计此类方案的研究较少。
>
> **主要贡献:** 本文提出了一种基于经典PSS-R方案并在量子随机预言机模型下证明其安全性的后量子签名方案。
>
> **达到效果:** 该方案在量子随机预言机模型下首次实现了具有消息恢复功能的PSS-R类似签名方案的安全性证明。
>
> **技术梗概:** 通过扩展紧适应重编程定理和测量与重编程定理，解决了两个相关输入/输出的随机预言机依次重新编程的问题。

---
### [推荐] [2026/562] New Approaches to Zero-Knowledge SNARG Constructions

- **匹配关键字:** LWE

- **作者:** Chaya Ganesh, Mor Weiss

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/562) | [PDF](https://eprint.iacr.org/2026/562.pdf)


> **研究背景:** 研究背景：零知识简洁非交互式论证(zkSNARGs)是SNARGs的一种，它证明除了声明的有效性外不泄露任何信息。现有的zkSNARG构造方法通常依赖于NIZK+SNARG的非黑盒方式实现。
>
> **主要贡献:** 主要贡献：提出了一种新的SNARG到zkSNARG转换方法，该方法与传统的NIZK+SNARG方法不同，采用了更简洁的信息论零知识证明系统，并且在一定程度上实现了SNARG的黑盒使用。
>
> **达到效果:** 达到的效果：通过这种方法，可以基于标准假设构造出针对子类NP问题的zbarg和zkSNARGs，从而为zkSNARGs提供了基于标准假设的新构建方法。
>
> **技术梗概:** 技术梗概：该转换利用了SNARG作为黑盒，并结合了哈希函数与概率可检验证明系统，实现了对SNARG的有效转化以适应特定子类NP问题。

---
### [推荐] [2026/564] TAPAS: Efficient Two-Server Asymmetric Private Aggregation Beyond Prio(+)

- **匹配关键字:** lattice, LWE

- **作者:** Harish Karthikeyan, Antigoni Polychroniadou

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/564) | [PDF](https://eprint.iacr.org/2026/564.pdf)


> **研究背景:** 隐私保护聚合对于不暴露个体记录即可从分布式数据中学习的AI系统至关重要，特别是在联邦学习和遥测领域。现有的双服务器协议虽然验证输入并防止任何单一方了解用户值，但它们在两个服务器上的成本是相同的，并且通信量与每个客户端输入维度L成比例增长，这限制了其在现代高维学习任务中的应用。
>
> **主要贡献:** TAPAS提出了一种新的双服务器非对称私有聚合方案，通过四个关键设计：无信任设置、独立于L的服务器端通信、基于标准格假设（LWE, SIS）的后量子安全性和更强的鲁棒性来解决这些问题。
>
> **达到效果:** 该方案显著降低了总成本，并允许次要服务器在普通硬件上运行，增强了服务器不串通的假设。此外，TAPAS还提供了一套新的高效格基零知识证明机制，确保了隐私和正确性。
>
> **技术梗概:** 通过设计一个具有计算复杂度与L相关的聚合和验证工作的主服务器以及一个轻量级辅助服务器来实现非对称性，并使用基于标准格假设的零知识证明技术增强了安全性。

---
### [推荐] [2026/569] Hybrid KEM Constructions from Classical PKEs and Post-Quantum KEMs

- **匹配关键字:** post-quantum

- **作者:** Biming Zhou, Yukai Zhang, Haodong Jiang, Yunlei Zhao

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/569) | [PDF](https://eprint.iacr.org/2026/569.pdf)


> **研究背景:** 随着量子计算的快速发展，RSA和Diffie–Hellman等经典公钥加密系统面临威胁，推动了向后量子密码学(PQC)的过渡。在此过程中，标准化机构和网络安全机构推荐使用结合经典和后量子密钥封装机制(KEMs)的混合设计以确保过渡期间的安全性。
>
> **主要贡献:** 本文提出了两种通用的混合构造$\mathsf{HybKEM}$和$\mathsf{HybKEM}^{*}$，将一个经典PKE方案与满足第二单行密文抗原像性的后量子KEM相结合，证明了这两种构造在标准模型中实现了IND-CCA安全性。
>
> **达到效果:** 通过引入新的安全属性部分第二单行密文抗原像性(PC2PRI)，$\mathsf{HybKEM}^{*}$能够仅从指定的PKE密文分量中推导出共享密钥，从而提高了效率并提供了对多个标准化经典加密方案PC2PRI性质的系统分析。
>
> **技术梗概:** 该研究通过设计满足特定安全属性的经典和后量子组件之间的组合来实现其目标，并证明了这些构造在理论上的安全性。

---
### [推荐] [2026/570] iToken: One-Time-Use Anonymous Token with Issuance Hiding

- **匹配关键字:** homomorphic encryption

- **作者:** Zengpeng Li, Xiangyu Su, Dongfang Wei, Guangyu Liao, Mei Wang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/570) | [PDF](https://eprint.iacr.org/2026/570.pdf)


> **研究背景:** iToken旨在增强隐私保护的KYC系统中的一次性匿名令牌（OTAT）的安全性和用户隐私，特别是在自主权身份框架中，如欧盟数字身份钱包、苹果私有访问令牌和W3C隐私保护广告提案。
>
> **主要贡献:** 该研究引入了一种新的盲环签名（BRS）原语，并提供了两种通用构造方法，从而实现了发行方在整个发行过程中的匿名性，增强了OTAT的鲁棒性和用户隐私。
>
> **达到效果:** 基于线性函数和同态加密或承诺证明求和论证的方法，iToken成功地实现了高效的签名带宽和竞争力的计算性能。
>
> **技术梗概:** 通过引入盲环签名（BRS）并采用盲签协议中的盲-环模式来确保从一开始就存在环结构，并由签署者在交互式盲签名协议中启动。

---
### [推荐] [2026/574] A Universal Blinder: One-round Blind Signatures from FHE

- **匹配关键字:** homomorphic encryption

- **作者:** Dan Boneh, Jaehyung Kim

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/574) | [PDF](https://eprint.iacr.org/2026/574.pdf)


> **研究背景:** 本文提出了一种通用盲签方案，通过任何安全签名方案生成单轮次盲签名，并保持格式一致以实现向后兼容性。
>
> **主要贡献:** 贡献了三种不同工作分配的编译器设计，利用全同态加密和零知识证明确保最终方案的安全性和匿名性。
>
> **达到效果:** 实现了与基础签名方案相同格式的单轮次盲签名，增强了现有签名方案的应用灵活性。
>
> **技术梗概:** 采用了全同态加密技术，并引入了新的验证型全同态加密概念，通过客户端、签发人或双方共同完成大部分工作来实现目标。

---
### [推荐] [2026/575] RoKoko: Lattice-based Succinct Arguments, a Committed Refinement

- **匹配关键字:** lattice, post-quantum

- **作者:** Michael Klooss, Russell W. F. Lai, Ngoc Khanh Nguyen, Michał Osadnik, Lorenzo Tucci

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/575) | [PDF](https://eprint.iacr.org/2026/575.pdf)


> **研究背景:** RoKoko 是一种基于格的简洁论证系统，旨在实现线性时间证明者和多项式对数通信及验证者复杂度。该研究改进了现有技术，并在实际应用中表现出色。
>
> **主要贡献:** 主要贡献在于引入了承诺折叠技术，允许更大的子证词数量 $
ho$，从而减小了证明大小并突破了常量障碍。
>
> **达到效果:** RoKoko 实现了约 200KB 的证明尺寸，并在验证速度上超越了 Greyhound 等现有方案，同时保持了相似的证明生成时间和竞争力的证明大小。
>
> **技术梗概:** 技术梗概包括承诺折叠和递归拆分与折叠范式，通过承诺机制减少了需要发送的消息数量，从而提高了效率。

---
### [2026/558] Cryptanalysis of four arbitrated quantum signature schemes

- **作者:** Pierre-Alain Jacqmin, Jean Liénardy

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/558) | [PDF](https://eprint.iacr.org/2026/558.pdf)


> **研究背景:** 本文研究了四种仲裁量子签名(AQS)方案的安全性，这些方案旨在通过仲裁者的帮助确保消息的真实性，并防止发送者和接收者的抵赖行为。
>
> **主要贡献:** 作者提出了一系列针对这四个AQS方案的攻击方法，揭示了它们在安全性方面的缺陷。
>
> **达到效果:** 研究发现，所有被分析的AQS方案都存在安全漏洞，包括签名伪造、虚假指控以及参与方的抵赖策略。
>
> **技术梗概:** 通过量子通信和信息理论分析，作者提出了一系列具体的攻击技术来验证其结论。

---
### [2026/560] High-Order Galois Automorphisms for TNFS Linear Algebra

- **作者:** Haetham Al Aswad, Cécile Pierrot, Emmanuel Thomé

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/560) | [PDF](https://eprint.iacr.org/2026/560.pdf)


> **研究背景:** 高阶Galois自同构对于TNFS线性代数步骤的加速是解决有限域离散对数问题的关键，尤其是在具有复合扩展度的配对基密码学中。
>
> **主要贡献:** 本文提出了针对$k=6$和$k=12$的新构造方法，使得在$\mathbb{F}_{p^6}$和$\mathbb{F}_{p^{12}}$中可以利用相应的Galois自同构加速线性代数步骤。
>
> **达到效果:** 通过引入新构造，本文实现了线性代数步骤约36倍（对于$k=6$）和144倍（对于$k=12$）的加速效果。
>
> **技术梗概:** 利用SageMath实现TNFS及其新构造，并在小规模实例上验证了结果的有效性。

---
### [2026/561] SynCirc: Efficient Synthesis of Depth-Optimized Circuits from High-Level Languages (Extended Version)

- **作者:** Arpita Patra, Joachim Schmidt, Thomas Schneider, Ajith Suresh, Hossein Yalame

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/561) | [PDF](https://eprint.iacr.org/2026/561.pdf)


> **研究背景:** SynCirc旨在通过优化硬件合成框架来提高多方计算(MPC)的实用性，特别是在电路表示方面，以减少乘法深度和在线轮数。
>
> **主要贡献:** 该研究贡献了一种基于Verilog和Yosys-ABC工具的定制化库和约束条件，特别针对多输入AND门进行优化，实现了显著的性能提升。
>
> **达到效果:** SynCirc在多输入AND门、比较器、多路复用器等构建块上取得了22.3%至66.7%的深度/在线轮数改进，并且与Trifecta协议相比，通信量减少了116倍。
>
> **技术梗概:** 通过引入XLS工具支持高级综合，SynCirc允许开发者使用C/C++编写安全函数，无需硬件定义语言的专业知识。

---
### [2026/563] Optimizing FROST for Message Capacity

- **作者:** Philipp Jovanovic, Ben Riva, Arnab Roy

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/563) | [PDF](https://eprint.iacr.org/2026/563.pdf)


> **研究背景:** FROST阈值签名方案通过双重随机数构造实现了圆最优Schnorr签名，但需要每个签名两个预签名，这在高吞吐量应用中产生了显著的开销。
>
> **主要贡献:** 作者证明了使用$k+1$个预签名来签署$k$条消息是安全的，并提出了改进后的FROST-core协议以提高消息容量。
>
> **达到效果:** 通过优化预签名的数量，该研究将消息容量从50%提升到接近100%，显著提高了FROST的安全性和效率。
>
> **技术梗概:** 研究采用了基于哈希重随机化的预签名协议，并分析了不同数量预签名对安全性的影响。

---
### [2026/565] Zeeperio: Verifying Governmental Elections with Ethereum

- **作者:** Aikamdeep Malhotra, Aleksander Essex, Jeremy Clark

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/565) | [PDF](https://eprint.iacr.org/2026/565.pdf)


> **研究背景:** Scantegrity II是首个采用加密端到端选举验证(E2E-V)协议的政府选举，但公众参与这一重要过程主要依赖于自愿和非正式的方式。
>
> **主要贡献:** Zeeperio是一种为Scantegrity选举设计的特殊用途zk-SNARK证明，可以通过智能合约自动验证，降低了成本并提高了效率。
>
> **达到效果:** 使用Zeeperio进行选举验证的成本低于30美元，并且与选票数量无关；证明生成时间在10万张选票的情况下不到5小时。
>
> **技术梗概:** Zeeperio通过特定应用的算术化构建了定制化的论证，相比通用zk-SNARK工具包实现了多个数量级的证明者效率提升。

---
### [2026/566] Secret-Shared Shuffle from Authenticated Correlations

- **作者:** Xiangfu Song, Xiaojian Liang, Ye Dong, Jianli Bai, Pu Duan, Changyu Dong, Tianwei Zhang, Ee-Chien Chang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/566) | [PDF](https://eprint.iacr.org/2026/566.pdf)


> **研究背景:** 秘密共享洗牌是一种在密文共享数据上实现盲排序的基本机制，广泛应用于基于秘密共享的安全计算中。然而，在高度敏感的应用场景下，需要提供恶意安全保证以确保实际安全性。
>
> **主要贡献:** 本文提出了一种新的两方恶意安全的秘密共享洗牌协议族，具有线性通信/计算成本和常数轮次通信，并通过认证关联提出了一个新的简单且高效的协议模板。
>
> **达到效果:** 该方法能够增强对恶意发送者的完全认证，避免了现有解决方案中的选择性失败攻击带来的主要开销。同时解决了来自恶意接收者的一致性问题，保持了预期的效率特性。
>
> **技术梗概:** 通过提出新的效率保留一致性检查以及一系列新技术、优化和分析，结合基于认证关联的框架，实现了恶意安全的秘密共享洗牌协议。

---
### [2026/567] Accurate Parameter Estimates for Punctured Key Recovery Linear Attacks

- **作者:** TIm Beyne, Antonio Flórez-Gutiérrez, Yosuke Todo

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/567) | [PDF](https://eprint.iacr.org/2026/567.pdf)


> **研究背景:** 该研究针对线性密钥恢复攻击中的穿孔技术，旨在通过修改评估线性逼近的映射来减少攻击的时间复杂性。
>
> **主要贡献:** 作者重新审视了数据复杂度估计模型，并澄清了一些假设，提高了模型的准确性。
>
> **达到效果:** 改进后的模型能够更精确地估算包含接近全码本数据复杂性的穿孔攻击的成本。
>
> **技术梗概:** 通过分析修改后的傅里叶变换坐标来优化线性逼近映射，从而调整数据和时间复杂度之间的权衡。

---
### [2026/568] Low-Depth Construction of Grover Oracles from Fully Functional Quantum Circuits

- **作者:** Behzad Abdolmaleki, Jiaqi Gu

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/568) | [PDF](https://eprint.iacr.org/2026/568.pdf)


> **研究背景:** 研究背景：Grover oracle是Grover搜索算法的核心组件。通常，构造Grover oracle需要从头开始设计量子电路，但本文提出了一种新的方法，即利用已有的完全功能量子电路（FFQC）来构建Grover oracle，以减少冗余并优化深度和宽度。
>
> **主要贡献:** 主要贡献：作者提出了一个低深度转换方法，将现有的FFQC转化为低深度的Grover oracle，并进一步减小了电路的宽度，同时保持低深度特性。
>
> **达到效果:** 达到的效果：通过该方法，AES量子电路的宽度从7280减少到7104，显著优化了Grover oracle的设计效率和资源利用率。
>
> **技术梗概:** 技术梗概：本文采用了一种低深度转换技术，通过对现有FFQC进行特定操作来构建Grover oracle，并通过分析实例验证了该方法的有效性。

---
### [2026/571] Playing Tag with Okamoto-Schnorr: Three-Move Pairing-Free Blind Signatures from DDH

- **作者:** Rutchathon Chairattana-Apirom, Michael Reichle, Stefano Tessaro

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/571) | [PDF](https://eprint.iacr.org/2026/571.pdf)


> **研究背景:** 该研究旨在设计一种无配对的盲签名方案，以解决现有解决方案在安全性或通信效率上的不足。
>
> **主要贡献:** 论文提出了首个仅需三轮交互且基于决策性Diffie-Hellman假设的安全无配对盲签名方案，并实现了统计意义上的匿名性。
>
> **达到效果:** 该方案达到了最优的通信复杂度和签名大小，同时提供了强的一次更多伪造抵抗性，并包含部分盲签名变体。
>
> **技术梗概:** 研究结合了传统的盲签名方案（如盲Okamoto-Schnorr方案）与精心设计的代数消息认证码，以实现所需的安全性和效率特性。

---
### [2026/572] Earpicks: Tightly Secure Two-Round Multi- and Threshold Signatures

- **作者:** Renas Bacho, Yanbo Chen

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/572) | [PDF](https://eprint.iacr.org/2026/572.pdf)


> **研究背景:** 多签名为分布式系统中的核心密码学原语，允许多方共同生成一条消息的紧凑签名。现有紧安全构造存在效率低下问题，特别是T-Spoon虽支持紧安全和密钥聚合但签名大小过大，限制了其应用范围。
>
> **主要贡献:** Earpick-MS提出了一种在非配对循环群上实现的两轮多签名称词，同时支持密钥聚合，并且实现了紧凑的签名形式。
>
> **达到效果:** 与T-Spoon相比，Earpick-MS显著减小了签名大小至仅三个字段元素和一个位，提升了实际应用中的效率和可部署性。
>
> **技术梗概:** 通过创新的设计方法，Earpick-MS在保持紧安全性和密钥聚合支持的同时优化了签名结构，减少了签名的字段数量。

---
### [2026/573] Two-Party BBS+ Signature in Two Passes

- **作者:** Xiaofei Wu, Tian Qiu, Guofeng Tang, Yuqing Niu, Bowen Jiang, Jun Zhou, Haiyang Xue, Guomin Yang

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/573) | [PDF](https://eprint.iacr.org/2026/573.pdf)


> **研究背景:** BBS+/BBS签名方案是匿名凭证和隐私保护认证的关键构建块，正被标准化并广泛部署。现有的阈值设计仍需至少三轮通信和大量数据传输。
>
> **主要贡献:** 提出了一种两方两遍BBS+签名协议，实现了减少交互次数的同时保持低计算和通信开销。
>
> **达到效果:** 该协议在双方设置下每签名仅需0.85KB的通信量，比现有最高效的方案少约27%，并能高效处理大消息向量，适合实际部署。
>
> **技术梗概:** 通过改进协议设计减少了通信轮次，并优化了计算效率以适应轻量级系统需求。

---

## 更新: 2026-03-22 20:49

*新增 19 篇论文 (编号 537--556)*

### [推荐] [2026/537] Cheap Digit Decomposition and Large Plaintext Spaces in FHEW using Phase Splitting

- **匹配关键字:** homomorphic encryption

- **作者:** Leonard Schild, Aysajan Abidin, Bart Preneel

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/537) | [PDF](https://eprint.iacr.org/2026/537.pdf)


> **研究背景:** 该研究聚焦于全同态加密算法，特别是基于累积器的方案（如FHEW和TFHE），这些方案通常适用于小数据集。然而，通过程序化的重新启动能力，可以将小型数据扩展到更大的明文域。
>
> **主要贡献:** 作者提出了新颖的方法来实现同态数字分解，即高效地将一个超出常规明文域大小的加密大数值拆分为基数表示形式。这种方法在计算上更为经济，并显著提高了性能。
>
> **达到效果:** 与之前的工作相比，该方法在理论上将性能提升了两倍，在实践中比Liu等人最新的技术快90%。此外，通过这种数字分解，作者展示了如何大幅增加明文域的大小，同时仅使计算复杂度翻倍，避免了超多项式级别的延迟问题。
>
> **技术梗概:** 研究采用了分相分裂的技术来实现高效的同态数字分解，无需实际拆分成数字片段即可组装回原始消息。

---
### [推荐] [2026/540] Ticket to Hide: Private, Practical Proofs of Provenance for TLS

- **匹配关键字:** post-quantum

- **作者:** Ryan Little, Daniel S. Roche, Mayank Varia

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/540) | [PDF](https://eprint.iacr.org/2026/540.pdf)


> **研究背景:** TLS协议确保了客户端与服务器之间的通信安全，但这种保证不能直接传递给第三方。现有研究如DECO协议旨在通过“TLS oracle”协议解决这一问题，允许客户端证明数据的来源并披露其属性。
>
> **主要贡献:** Ticket to Hide引入了一种适用于TLS 1.3的新协议，在多服务器环境中实现了数据源隐藏功能，并且比先前的工作更快更私密。此外，它是首个与后量子安全TLS密钥协商和证书兼容的TLS oracle协议。
>
> **达到效果:** 该协议通过利用TLS 1.3的新特性，实现了在不到3秒的时间内处理N=100个服务器的高效性能，并且能够证明数据来自特定服务器而不泄露其身份。
>
> **技术梗概:** Ticket to Hide采用了Garble-then-Prove框架，并结合了TLS 1.3的多服务器环境和新功能，从而实现了上述效果。

---
### [推荐] [2026/543] MTSF --- Market-Theoretic Security Framework: A Unified Paradigm For The Art Of Proving and Disproving Security

- **匹配关键字:** post-quantum

- **作者:** Basker Palaniswamy, Paolo Palmieri

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/543) | [PDF](https://eprint.iacr.org/2026/543.pdf)


> **研究背景:** 现有的加密安全证明分散在多个范式中，如博弈论证明、通用组成性（UC）、形式验证和自定义不安全性论证，各自有不同的语言、假设和局限性。
>
> **主要贡献:** MTSF通过将所有安全证明重新解释为经济市场来提供一个统一的框架，其中防御者作为卖家提供安全商品，而攻击者作为买家出价以破坏这些商品。
>
> **达到效果:** 这种统一范式为密码学家提供了一个严谨且富有表现力的框架，能够将四大主要证明范式统一到单一的形式语言中，并引入了扩展差分引理、基于竞价的归约等关键技术创新。
>
> **技术梗概:** MTSF通过处理多个同时失败事件的扩展差分引理、明确建模攻击者策略的基于竞价的归约以及在相同结构内对证明和反证进行对称处理的双方法论，实现了这些技术革新。

---
### [推荐] [2026/548] Post-Quantum Cryptography from Quantum Stabilizer Decoding

- **匹配关键字:** post-quantum

- **作者:** Jonathan Z. Lu, Alexander Poremba, Yihui Quek, Akshar Ramkumar

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/548) | [PDF](https://eprint.iacr.org/2026/548.pdf)


> **研究背景:** 后量子密码学依赖于少数几个假设，存在被破解的风险。因此，寻找新的、具有说服力的量子硬度假设成为必要。
>
> **主要贡献:** 作者提出了量子稳定码解码作为候选问题，并证明了其平均案例难度可以转化为经典密码学的核心构建块。
>
> **达到效果:** 该工作不仅提供了理论上有效的后量子安全方案，还展示了其实用性，与现有LPN基方案效率相当。
>
> **技术梗概:** 通过将随机量子稳定码解码归约到一个类似于LPN但带有额外辛代数结构的平均案例问题来证明其难度。

---
### [推荐] [2026/549] Look Ahead! Practical CCA-secure Steganography: Cover-Source Switching meets Lattice Gaussian Sampling

- **匹配关键字:** lattice

- **作者:** Russell W. F. Lai, Ivy K. Y. Woo, Hoover H. F. Yin

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/549) | [PDF](https://eprint.iacr.org/2026/549.pdf)


> **研究背景:** 研究背景：隐写术旨在保护消息的机密性并隐藏其传输行为。现有基于拒绝采样技术的证明安全隐写系统通常具有与覆盖信道最小熵成反比的编码率，且在具有记忆性的信道上实现标准选择明文攻击（CCA）安全性存在困难。
>
> **主要贡献:** 主要贡献：通过引入“部分可抽样信道”概念，并结合“覆盖源切换”技术，在随机预言模型中实现了高编码率的CCA安全隐写系统，特别适用于包含可显式采样分布如数字照片中的高斯噪声的信道。
>
> **达到效果:** 达到的效果：该工作突破了在具有记忆性的非前瞻模式信道上实现标准CCA安全性的一般不可能性，并通过结合覆盖源切换技术与格基预像采样方法，成功构建了适用于高斯信道的CCA安全隐写系统。
>
> **技术梗概:** 技术梗概：采用扩展后的隐写系统形式化定义，结合部分可抽样信道和覆盖源切换技术，利用来自格基的高斯预像采样方法实现了高效且安全的隐写方案。

---
### [推荐] [2026/551] Succinct Verification of Lattice-Based Compressed $\Sigma$-Protocols via Delegated Proofs of Correct Folding of Cryptographically Generated Public Parameters

- **匹配关键字:** lattice

- **作者:** Anders Kallesøe

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/551) | [PDF](https://eprint.iacr.org/2026/551.pdf)


> **研究背景:** 内积论证在密码学中广泛应用，尽管压缩$\Sigma$协议提供了高效的通信复杂度，但其验证复杂度仍为线性。
>
> **主要贡献:** 本文提出了通过委托证明正确折叠加密生成的公共参数来实现简洁可验证的压缩$\Sigma$协议的新途径。
>
> **达到效果:** 该方法显著降低了验证者的计算负担，并适用于基于格的结构化线性形式。
>
> **技术梗概:** 利用交互式证明整合承诺方案的设置函数，使得CRS可以通过小型种子加密生成。

---
### [推荐] [2026/556] TP-NTT: Batch NTT Hardware with Application to Relinearization

- **匹配关键字:** lattice, homomorphic encryption

- **作者:** Emre Koçer, Tolun Tosun, Beren Aydoğan, Erkay Savaş, Furkan Turan, Ingrid Verbauwhede

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/556) | [PDF](https://eprint.iacr.org/2026/556.pdf)


> **研究背景:** 全同态加密(FHE)允许在不解密的情况下对加密数据进行任意计算，为安全的云计算、加密数据分析和隐私保护机器学习提供了强大的隐私保证。然而，由于大模环上多项式算术的高度计算成本，FHE的实际部署仍然受到限制。
>
> **主要贡献:** TP-NTT 是一种可扩展且吞吐量优化的 NTT 架构，支持从 $2^{10}$ 到 $2^{16}$ 的广泛环维度。该设计在多个层面进行了优化，包括多维分解和自定义吞吐量配置。
>
> **达到效果:** TP-NTT 在 $n=2^{16}$ 时，在平均延迟上比之前最佳的设计快了 $8.03	imes$，同时实现了 $1.26	imes$ 更好的面积-时间积（ATP）。其高效的性能在 FHE 的重新线性化案例研究中得到了验证。
>
> **技术梗概:** TP-NTT 通过多维度分解和自定义吞吐量配置，在设计时支持 2-D、3-D 和 4-D 分解，每种分解都有其特定的优势。此外，该架构还结合了可扩展性和高吞吐量优化技术。

---
### [2026/538] Proof-Carrying Data via Holography Accumulation

- **作者:** Nikitas Paslis, Carla Ràfols, Alexandros Zacharakis

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/538) | [PDF](https://eprint.iacr.org/2026/538.pdf)


> **研究背景:** 研究背景：Succinct non-interactive arguments of knowledge (SNARKs) 使复杂的计算可以通过短证明进行验证。递归证明组合允许对长时间运行或分布式计算进行逐步验证，但现有方法存在根本性的权衡。
>
> **主要贡献:** 主要贡献：提出了一种基于 holography accumulation 的无状态递归 SNARK 证明框架，该框架结合了高效的递归和无状态性，同时避免了传统方法中的高证明者成本问题。
>
> **达到效果:** 达到的效果：通过引入 generalized bilinear forms (GBF)，实现了对多种现代 SNARKs 的验证过程的高效累积，并构造了一种通用的 PCD 方案，兼容单变量和多变量多项式承诺方案。
>
> **技术梗概:** 技术梗概：该方法利用了 lincheck 或可检查子空间论证，将验证分解为依赖于证人的检查和公共多项式的评估，从而实现了高效的递归证明累积。

---
### [2026/539] Orca And Dolphin: Efficient Bivariate And Multilinear Polynomial Commitment Schemes Under Standard Assumptions

- **作者:** Helger Lipmaa

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/539) | [PDF](https://eprint.iacr.org/2026/539.pdf)


> **研究背景:** 现有的多项式承诺方案要么证明者时间呈超线性增长，要么论证大小呈超常数增长。SamaritanPCS和Mercury通过利用高效的单变量多项式交互式检查协议（IOP），将单变量多项式承诺方案提升至多线性设置，从而实现基于求和检验的高效零知识内含论证系统（zk-SNARKs）并减小通信量。然而，这些方案仅在联合随机预言机和代数群模型下实现了知识诚实性。
>
> **主要贡献:** 作者提出了Orca和Dolphin两种优化后的多变量多项式承诺方案，分别对应二元和多元情况。这两种方案证明了其交互评估协议在标准模型下的计算特殊诚实性，并假设KZG满足绑定性和插值绑定性（两者均基于ARSDH安全假设）。
>
> **达到效果:** Orca和Dolphin不仅保证了知识诚实性在随机预言机模型下成立，还提供了一种更高效的评估阶段，在联合随机预言机和代数群模型下实现了知识诚实性。这使得它们成为构建高效zk-SNARKs的重要组成部分。
>
> **技术梗概:** 这两种方案通过利用KZG承诺的绑定性和插值绑定性，证明了其交互式评估协议在标准模型下的计算特殊诚实性，并且优化了证明者的时间复杂度和论证大小。

---
### [2026/541] Towards Verifiable AI with Lightweight Cryptographic Proofs of Inference

- **作者:** Pranay Anchuri, Matteo Campanelli, Paul Cesaretti, Rosario Gennaro, Tushar M. Jois, Hasan S. Kayman, Tugce Ozdemir

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/541) | [PDF](https://eprint.iacr.org/2026/541.pdf)


> **研究背景:** 在基于云的大型AI模型部署中，客户端无法保证响应的正确性或由预期模型产生。现有的加密证明系统虽然提供了强大的正确性保证，但验证者开销过高，使得大规模应用难以实现。
>
> **主要贡献:** 提出了一种轻量级的统计性质为基础的抽样验证框架和协议，替代了全量加密证明，并通过形式化条件确保功能上不相似模型之间的踪迹分离可以用于论证可验证推理协议的安全性。
>
> **达到效果:** 该方法将证明时间大幅降低几个数量级，从几分钟缩短到几毫秒，虽然证明大小略有增加，但适用于审计、大规模部署场景以及理性激励的验证者面临检测惩罚的情况。
>
> **技术梗概:** 通过默克尔树为基础的向量承诺机制，验证者仅沿随机采样的路径打开少量输出到输入的条目，从而实现了一种在精确性和效率之间权衡的协议。

---
### [2026/542] VERIDP: Verifiable Differentially Private Training

- **作者:** Behzad Abdolmaleki, Amir R. Asadi, Vahid R. Asadi, Stefan Köpsell, Bhavish Mohee, Nahid Roustaeifar, Maryam Zarezadeh

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/542) | [PDF](https://eprint.iacr.org/2026/542.pdf)


> **研究背景:** 传统的随机梯度下降(SGD)算法是现代机器学习的基础，但在隐私敏感的环境中，梯度可能泄露个体数据点的信息。现有的差分隐私(DP)框架假设参与者为半诚实类型，在对抗或联邦环境下，恶意行为者可以绕过或篡改噪声添加过程，从而破坏隐私保证。
>
> **主要贡献:** VERIDP框架通过结合零知识证明(ZKPs)、多项式承诺、和GKR基的证明以及增量可验证计算(IVC)，在不泄露私有数据或随机数的情况下，生成正确的梯度计算、裁剪、平均化和高斯噪声生成的有效证明。
>
> **达到效果:** 与仅验证最终隐私预算的系统不同，VERIDP能够在每次迭代中验证每个模型更新，即使在对抗性环境中也能提供强大的隐私保证。这为安全且可审计的机器学习建立了差分隐私和可验证计算的新颖统一框架。
>
> **技术梗概:** VERIDP采用了零知识证明、多项式承诺、和GKR基的证明以及增量可验证计算等技术，确保在不泄露任何私有数据或随机数的情况下，能够生成正确的梯度计算、裁剪、平均化和高斯噪声生成的有效证明。

---
### [2026/544] HARE: Compact HQC via Distance-Informed Erasure Decoding

- **作者:** Tianrui Wang, Qicheng Teng, Anyu Wang, Jun Zhang, Bo Pang, Chunhuan Zhao, Sihuang Hu, Xiaoyun Wang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/544) | [PDF](https://eprint.iacr.org/2026/544.pdf)


> **研究背景:** HARE 是基于 HQC 框架的一个 KEM 方案，旨在通过改进的编码技术减少公钥和密文的大小，以提高安全性与效率。
>
> **主要贡献:** HARE 引入了一种距离感知的擦除解码技术，结合了内层代码的距离信息来识别不可靠块，并使用外层代码进行纠正，从而降低了解密失败率。
>
> **达到效果:** 通过这种技术，HARE 较 HQC 实现了公钥和密文大小分别减少了 13.2%、12.3% 和 13.3%，适用于 NIST 安全级别 1、3 和 5。
>
> **技术梗概:** HARE 使用距离感知的擦除解码技术，结合 Bitzer 等人在 EUROCRYPT 2026 提出的密文压缩方法和参数优化，提高了编码效率并减少了数据传输量。

---
### [2026/545] Aggregator-Based Voting using proof of Partition

- **作者:** Marius Lombard-Platet, Doron Zarchy

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/545) | [PDF](https://eprint.iacr.org/2026/545.pdf)


> **研究背景:** 为了解决DAO等大规模频繁选举中投票存储成本高且隐私保护需求的问题，研究提出了一种基于聚合器的证明分割方案。
>
> **主要贡献:** 贡献在于设计并实现了Aggios系统及其核心组件Extended Partition Argument (EPA)，该组件能够高效地验证分组信息。
>
> **达到效果:** 实验结果表明，与传统投票方式相比，Aggios在证明大小上至少缩小了512倍，并且在最优情况下不依赖于投票人数，实现了大规模隐私保护选举的可行性。
>
> **技术梗概:** EPA通过零知识论证技术，允许证明者展示一个承诺向量可以被分解成多个互斥子向量形成分割，每个子向量可公开或保密。

---
### [2026/546] Hyperelliptic Gluing Isogeny Diffie–Hellman (HGIDH): A Genus-2 Gluing Isogeny Key-Exchange

- **作者:** Nouhou Abdou Idris, Mustapha Hedabou

- **分类:** Unknown

- **链接:** [论文](https://eprint.iacr.org/2026/546) | [PDF](https://eprint.iacr.org/2026/546.pdf)


> **研究背景:** 该研究旨在设计一种基于超椭圆曲线粘合态结构的密钥交换协议，以增强安全性并应对现有侧信道攻击。
>
> **主要贡献:** 提出了一种新的Hyperelliptic Gluing Isogeny Diffie–Hellman (HGIDH) 协议，利用两个超奇异椭圆曲线和一个超椭圆曲线雅可比的粘合态结构来构建密钥交换机制。
>
> **达到效果:** 该协议通过使用非循环二维核编码私钥，避免了SIDH类攻击中的结构性弱点，并且其安全性被置于标准超奇异态结构问题的复杂性框架中。
>
> **技术梗概:** 研究通过引入两个中间问题形式化计算任务，抽象出粘合内核恢复和计算超椭圆曲线态的问题，并证明任何有效解决这些问题的对手都可以转化为解决标准超奇异态问题的算法。

---
### [2026/547] Dialga: A Family of Low-Latency Tweakable Block Ciphers using Multiple Linear Layers (Full Version)

- **作者:** Subhadeep Banik, Tatsuya Ishikawa, Takanori Isobe, Ryoma Ito, Kazuhiko Minematsu, Kazuma Nakata, Mostafizar Rahman, Kosei Sakamoto

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/547) | [PDF](https://eprint.iacr.org/2026/547.pdf)


> **研究背景:** Dialga旨在提供低延迟的可调块密码，支持128/256位调整和256位密钥，通过创新策略显著减少延迟。
>
> **主要贡献:** 贡献在于提出了一种新的可调块密码设计方法，结合了多线性层和高效的单元置换，并优化S盒选择以进一步降低轮函数的延迟。
>
> **达到效果:** Dialga在硬件延迟上几乎减半至QARMAv2的一半，并且电路面积减少了约40%，同时保持相同的安全性水平。
>
> **技术梗概:** 技术包括使用多线性层和高效的单元置换，以及通过SAT等先进方法优化S盒选择，以减少轮函数的延迟。

---
### [2026/550] Solving the Linear Code Equivalence Problem from Single Codeword Matching

- **作者:** Magali Bardet, Charles Brion, Ayoub Otmani, Mohamed Saeed, Nicolas Sendrier

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/550) | [PDF](https://eprint.iacr.org/2026/550.pdf)


> **研究背景:** 研究背景：线性码等价问题（LCE）是在给定两个线性码之间寻找哈明空间$\mathbb{F}_q^n$的同构，被认为是计算上难以解决的问题。现有的匹配码字框架被广泛用于评估依赖于LCE难度的密码方案的安全性。
>
> **主要贡献:** 主要贡献：提出了一种基于逆向量Schur乘积的新方法来判断单对码字是否匹配，该方法能够更高效地识别线性等价关系。
>
> **达到效果:** 达到的效果：通过这种方法，可以显著减少计算复杂度，并且在某些参数范围内提供了更强的攻击能力。这为评估和改进基于LCE安全性的密码方案提供了新的工具。
>
> **技术梗概:** 技术梗概：该方法利用Schur乘积$\mathcal{C} \star \mathbf{v}^{-1}$来判断码字匹配性，通过证明线性等价的码在施瓦茨-齐默曼同构下的关系，从而简化了问题求解过程。

---
### [2026/553] Graph-based Asynchrony with Quasilinear Complexity for Any Linear Verifiable Secret Sharing Scheme

- **作者:** Hugo Delavenne, Lola-Baie Mallordy

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/553) | [PDF](https://eprint.iacr.org/2026/553.pdf)


> **研究背景:** 现有的线性VSS方案在同步通信假设下运行，但在实际网络中，由于数据包丢失或节点延迟，往往无法实现。
>
> **主要贡献:** 作者提出了一种新的方法，将任何线性VSS方案转化为统计意义上的AVSS，并构建了一个名为Bonneval-on-Arc的协议。
>
> **达到效果:** 该协议实现了经销商的准线性通信复杂度和每个参与者的小于亚线性复杂度，并且恶意节点的容忍阈值为$t < n/(d+2)$，从而降低了整体通信成本。
>
> **技术梗概:** 通过构建一个$d$-规则图模型，使得每个节点仅与$d$个邻居进行通信，作者实现了这一目标。

---
### [2026/554] PrivaLean: Low-Latency and High-Accuracy System for Secure 2PC Inference

- **作者:** Jinghao Zhao, Hongwei Yang, Bobo Wang, Lichunxi Yang, Juncheng Li, Xiangrui Zeng, Meng Hao, Desheng Wang, Hui He, Weizhe Zhang

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/554) | [PDF](https://eprint.iacr.org/2026/554.pdf)


> **研究背景:** 传统的安全多方计算虽然强大，但其高计算开销和通信延迟限制了其广泛应用。
>
> **主要贡献:** PrivaLean框架通过优化线性层和非线性层的评估方法，实现了低延迟和高准确度的安全双方推理。
>
> **达到效果:** 在广域网环境下，PrivaLean能够以125.02秒完成单次ResNet-50推理，并且其准确性超越了基于ReLU的基本模型。
>
> **技术梗概:** 通过局部随机密文生成机制和中间编码方法优化线性层；设计新型三角激活协议及数据分布感知训练策略来克服非线性评估瓶颈。

---
### [2026/555] Improved Issuer Hiding for BBS-based Anonymous Credentials

- **作者:** Nesrine Kaaniche, Seyni Kane, Maryline Laurent, Jacques Traoré

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/555) | [PDF](https://eprint.iacr.org/2026/555.pdf)


> **研究背景:** 现有基于属性的匿名凭证系统通常无法隐藏发行者身份，且近期尝试解决此问题的方法要么效率低下，要么存在关键策略漏洞。
>
> **主要贡献:** 本文提出了一种新的基于BBS的发行者隐藏匿名凭证系统，并采用签名策略方法来解决这些问题。
>
> **达到效果:** 该方案在代数组模型下证明安全，消除了秘密策略密钥的需求，允许验证无需秘密值；并实现了首个无对偶性的发行者隐藏匿名凭证，基于代数MACs。
>
> **技术梗概:** 通过引入签名策略和使用代数MACs技术，确保了系统在不依赖对偶性的情况下实现不可伪造性和永久的发行者隐藏匿名性。

---

## 更新: 2026-03-20 20:33

*新增 11 篇论文 (编号 524--536)*

### [推荐] [2026/527] QR-UOV without Rejection Sampling: Security Analysis and High-Speed Implementation

- **匹配关键字:** post-quantum

- **作者:** Hiroshi Amagasa, Hiroki Furue, Rei Ueno, Naofumi Homma

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/527) | [PDF](https://eprint.iacr.org/2026/527.pdf)


> **研究背景:** QR-UOV是一种基于UOV的多变量签名方案，通过利用商环结构实现紧凑的公钥，被认为是后量子数字签名的候选者。然而，其公钥扩展过程中的拒绝采样步骤引入了额外的数据移动和不规则的控制流，影响了验证速度。
>
> **主要贡献:** 本文提出了一种名为NoRS QR-UOV的新方案，去除了公钥扩展中的拒绝采样步骤，并通过确定性地将拒绝值映射为0简化了系数生成过程。
>
> **达到效果:** 理论和实证分析表明，在推荐的参数集下，NoRS QR-UOV保留了声称的安全水平。在x86处理器上实现了带有AES-NI和AVX2指令的支持，验证速度得到了显著提升。
>
> **技术梗概:** 通过确定性映射拒绝值为0来简化系数生成，并评估了这种修改对安全性的影响。

---
### [推荐] [2026/528] Full Secret Key Recovery of First-order Masked Crystals-Kyber implementation using multiple distinct chosen-ciphertexts

- **匹配关键字:** post-quantum

- **作者:** Souhayl Ben El Haj Soulami, Yann Connan, Sylvain Duquesne

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/528) | [PDF](https://eprint.iacr.org/2026/528.pdf)


> **研究背景:** 该研究针对第一级掩码实现的Crystals-Kyber进行侧信道攻击，旨在揭示后量子密码学中全秘密密钥恢复的技术挑战。
>
> **主要贡献:** 研究人员提出了一种新颖的区别器，并结合了多个不同的选择明文来提高攻击效果，这是在现有文献中的创新贡献。
>
> **达到效果:** 实验结果显示，在噪声较大的环境下（信噪比SNR为0.67），通过75000个样本成功恢复了全秘密密钥，成功率达到了95%，证明了该方法的有效性。
>
> **技术梗概:** 攻击技术基于对多个相同区别器实例的信息收集，并利用多次解密请求来增强攻击效果，展示了在复杂环境下的应用潜力。

---
### [推荐] [2026/533] A Maliciously-Secure Post-Quantum OPRF from Crypto Dark Matter

- **匹配关键字:** post-quantum

- **作者:** Diego F. Aranha, Aron van Baarsen, Adam Blatchley Hansen, Kent Nielsen, Peter Scholl

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/533) | [PDF](https://eprint.iacr.org/2026/533.pdf)


> **研究背景:** 本文构建了基于交替模数假设的恶意安全OPRF协议，采用Crypto Dark Matter范式。
>
> **主要贡献:** 通过结合新的向量模糊线性评估技术，实现了在零知识和安全两方计算中的相关随机数生成，从而获得恶意安全性。
>
> **达到效果:** 相比现有最先进的GOLD OPRF，在所有场景下在线阶段更快，并且在小批量设置中整体效率更高；支持秘密共享输出并可扩展处理秘密共享输入。
>
> **技术梗概:** 利用向量模糊线性评估技术进行模数转换，实现高效的零知识和安全两方计算中的相关随机数生成。

---
### [推荐] [2026/534] Ciphertext-Policy ABE for $\mathsf{NC}^1$ Circuits with Constant-Size Ciphertexts from Succinct LWE

- **匹配关键字:** lattice, LWE

- **作者:** Jiaqi Liu, Yuanyi Zhang, Fang-Wei Fu

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/534) | [PDF](https://eprint.iacr.org/2026/534.pdf)


> **研究背景:** 本文构建了一种基于格的细粒度属性加密方案，用于$\mathsf{NC}^1$访问策略，并实现了恒定大小的密文。
>
> **主要贡献:** 该方案在深度$d$和规模$s$为$\ell$位输入的$\mathsf{NC}^1$电路上实现了选择性安全性。
>
> **达到效果:** 此方案使得公钥和密文大小与$d$无关，而秘密密钥大小与$\ell$成正比，且在标准模型下安全假设为多项式精确线性LWE。
>
> **技术梗概:** 通过引入多项式精确线性LWE假设并结合$\mathsf{NC}^1$电路的特性来实现恒定大小的密文和高效的安全性证明。

---
### [2026/524] Distance of RAA Codes over Large Finite Fields (with Applications in zkSNARKs and PCGs)

- **作者:** Pariya Akhiani, Yupeng Zhang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/524) | [PDF](https://eprint.iacr.org/2026/524.pdf)


> **研究背景:** RAA码因其线性时间编码和良好的距离特性，在现代密码学中被广泛研究，尤其在零知识证明和安全多方计算等构建模块中发挥关键作用。然而，现有工作仅针对二进制域或较小的有限字段提供了可验证的距离保证。
>
> **主要贡献:** 本文首次证明了RAA码在大有限域上具有恒定相对距离，并解决了关于其距离随领域增大而改善的公开猜想。
>
> **达到效果:** 实验结果显示，在消息长度为$2^{15}$和重复因子为4的情况下，31位素数字段上的RAA码实现了相对距离$\frac{1}{2}$，失败概率仅为$2^{-16}$，优于二进制域上最佳证明的距离$\delta = 0.2$，失败概率为$2^{-7}$。
>
> **技术梗概:** 通过理论分析和实证证据，本文展示了大字段相较于二进制场能提供更优的距离保证，并显著降低了失败概率。

---
### [2026/526] Broken By Design: A Longitudinal Analysis of Cryptographic Failures in Alipay Mobile Payment Infrastructure

- **作者:** Jiqiang Feng

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/526) | [PDF](https://eprint.iacr.org/2026/526.pdf)


> **研究背景:** 本文对支付宝移动支付基础设施中的加密失败进行了系统性安全分析，重点关注其自2009年起使用MD5WithRSAEncryption和RSA-1024的APK签名证书，并将持续至2026年。
>
> **主要贡献:** 作者通过组织15个可复现的概念验证攻击，展示了支付宝加密基础设施每一层都存在可利用的安全弱点，包括证书、签名方案、密钥管理和生态系统层面的伪随机数生成器失败。
>
> **达到效果:** 研究揭示了生态系统级别的加密退化现象：123个证书中有38个（占比30.9%）使用RSA-1024，并且通过批处理GCD方法发现了28个RSA密钥中存在8个共享的素数。进一步测试确认，其中3台服务器仍处于运行状态并具有易受攻击的TLS配置。
>
> **技术梗概:** 研究采用了包括MD5碰撞生成、SHA-1碰撞可行性评估、Janus漏洞利用、v1签名绕过技术、硬编码DES密钥分析以及RSA密钥重复使用在内的多种已知技术和方法。

---
### [2026/529] Benchmarking Exported Key Material from Commercial QKD Systems Using SENTRY-Q: A Model-Based Output Validator

- **作者:** Darshit Suratwala, Matvey Romanowski, Orr Dunkelman, Elham Amini, Jean-Pierre Seifert

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/529) | [PDF](https://eprint.iacr.org/2026/529.pdf)


> **研究背景:** 该研究针对商用量子密钥分发(QKD)系统中导出密钥材料的实际应用需求，填补了现有协议级指标如量子比特错误率和秘密密钥速率与下游密钥管理系统(KMS)及加密应用对接验证之间的空白。
>
> **主要贡献:** 研究通过SENTRY-Q模型构建了一个可重复的测量工作流，评估三个商用QKD系统的导出密钥块，并提出了五个指标来衡量这些系统的行为稳定性。
>
> **达到效果:** 实验结果表明，这三个商用QKD系统在256位密钥导出方面均表现出稳定的块级分布特性，验证了它们在实际部署中的可靠性。
>
> **技术梗概:** 研究采用了一种基于模型的输出基准方法，通过计算哈明重量平衡、最小熵代理等五个指标，并结合NIST SP 800-22长序列一致性检查来评估导出密钥块的行为。

---
### [2026/531] A Review of IC Logical Reverse Engineering Techniques

- **作者:** Kevin Xu, Lucas Daudt Franck, Samuel Pagliarini

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/531) | [PDF](https://eprint.iacr.org/2026/531.pdf)


> **研究背景:** 本文综述了应用特定集成电路（ASIC）的逻辑逆向工程技术，从硬件安全角度定义了该问题，并回顾了早期相关技术的发展历程。
>
> **主要贡献:** 文章组织并总结了当前的逆向工程技术，按目标和方法分类，并指出了现有文献中的共同趋势和评估实践。
>
> **达到效果:** 研究结果为研究人员提供了关于逆向工程及其未来方向的基础知识，识别出未充分探索的问题领域及完全新颖的研究问题。
>
> **技术梗概:** 文章追溯了从手动评估和结构分析到图论和基于机器学习的解决方案的技术演变。

---
### [2026/532] S-two Whitepaper

- **作者:** Dan Carmon, Lior Goldberg, Ulrich Haböck, Leonardo Lerer, Ilya Lesokhin

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/532) | [PDF](https://eprint.iacr.org/2026/532.pdf)


> **研究背景:** S-two是基于Mersenne素数的圈STARK，旨在提供一种高效的零知识证明方案。
>
> **主要贡献:** 论文贡献了对扁平化代数指示关系（flat AIR）电路模型的形式化描述，并分析了其接近性证明的安全性。
>
> **达到效果:** 通过S-two，实现了在多表证明中控制正确性误差的突破，同时提出了关于Reed-Solomon码的可列表解性和线性解码性的猜想。
>
> **技术梗概:** 采用了跨域相关一致性的概念来改进STARK证明系统的性能，并结合圈FRI技术以增强证明的有效性和可靠性。

---
### [2026/535] Improved Related-Key Differential Neural Distinguishers for SPN Block Ciphers

- **作者:** Chuchu Ge, Qichun Wang

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/535) | [PDF](https://eprint.iacr.org/2026/535.pdf)


> **研究背景:** 近年来，相关密钥差分神经区分器在块密码分析中引起了广泛关注，但其构建仍主要依赖于手动设计。
>
> **主要贡献:** 本文提出了一种统一框架来系统地为轻量级SPN结构的块密码构建相关密钥差分神经区分器，并开发了特征增强和样本增强方法以提高准确性。
>
> **达到效果:** 实验结果表明，所提出的框架能够有效构建多轮相关密钥差分神经区分器，随着每样本明文对数量增加，准确率持续提升。
>
> **技术梗概:** 该方法通过利用SPN组件的可逆性来推导更丰富的最终内部状态表示，并通过在不同相关密钥下重用每个明文对来生成多个密文对关系以增强样本。

---
### [2026/536] Exploring the Boundary: Discriminative Model-based Parameter Search for Fault Injection

- **作者:** Ju-Hwan Kim, Dong-Guk Han

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/536) | [PDF](https://eprint.iacr.org/2026/536.pdf)


> **研究背景:** 故障注入（FI）攻击通过物理手段诱导目标设备产生特定的错误，精确调整故障参数是可靠触发预期故障的关键。然而，现有参数搜索策略往往在探索和利用之间存在不平衡，导致容易过早收敛或未能充分调查潜在高价值区域。
>
> **主要贡献:** 本文提出了一种新颖的参数搜索框架，结合了判别模型来高效生成具有高成功率的参数候选，并引入了Refining Successive Halving Algorithm (RSHA) 来统计学地识别发现的故障参数中的全局最优解。
>
> **达到效果:** 该方法在八个场景中表现优异，包括电压瞬变（VG）和电磁故障注入（EMFI），能够识别出多达42.2倍的独特预期故障参数，并将成功率提高20.3个百分点以上，超越了最先进的技术。
>
> **技术梗概:** 通过结合回归模型探索正常与静默判决之间的边界，并利用分类模型开发发现的预期故障样本进行优化，同时引入RSHA算法以统计学方式识别全局最优解。

---

## 更新: 2026-03-18 19:44

*新增 2 篇论文 (编号 522--523)*

### [推荐] [2026/523] RISC-V based Vectorization of Classic McEliece Key Generation

- **匹配关键字:** post-quantum

- **作者:** Mahnaz Namazi Rizi, Nusa Zidaric, Lejla Batina, Nele Mentens

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/523) | [PDF](https://eprint.iacr.org/2026/523.pdf)


> **研究背景:** 量子计算机可能通过Shor算法和Grover算法破解或削弱经典密码学，促使开发如Classic McEliece（CM）等后量子密码学（PQC）算法以抵抗量子攻击。然而，CM的复杂计算和大密钥尺寸使其在保持高效性能方面具有挑战性。
>
> **主要贡献:** 该研究首次全面探索并实现了基于RISC-V向量扩展（RVV）加速Classic McEliece密钥生成过程的方法，并提出了新的自定义RVV指令以进一步提高实现速度。
>
> **达到效果:** 通过评估使用RVV1.0的自动和手动向量化实现，结合多种向量寄存器配置，研究展示了在FPGA上利用RVV加速CM密钥生成的实际能力。
>
> **技术梗概:** 研究采用RISC-V Vector Extension Version 1.0（RVV1.0）进行评估，并提出了新的自定义RVV指令以进一步优化Classic McEliece密钥生成的实现。

---
### [2026/522] X3DH with Deniable Authentication without Trusted Third Parties

- **作者:** Stanislaw Jarecki, Phillip Nazarian, Apurva Rai

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/522) | [PDF](https://eprint.iacr.org/2026/522.pdf)


> **研究背景:** X3DH是一种广泛应用于即时通讯应用中的加密协议，旨在提供无第三方信任的密钥交换，并具有可否认性。然而，现有基于VRF的SAS-MA扩展破坏了X3DH的可否认性。
>
> **主要贡献:** 本文提出了一种基于私有VRF（PVRF）的新方案，该方案在保持与X3DH相同集成便利性的同时，几乎保留了X3DH的可否认性。
>
> **达到效果:** 通过引入PVRF机制，新方案能够在不牺牲性能的前提下，实现与X3DH兼容的SAS-MA认证过程，并提供类似X3DH的可否认性。
>
> **技术梗概:** 该技术利用PVRF的独特属性，允许仅由指定验证者进行正确性的验证，从而在保持协议效率的同时增强了安全性。

---

## 更新: 2026-03-16 20:25

*新增 13 篇论文 (编号 507--521)*

### [推荐] [2026/510] FHorgEt: A Cryptographic Solution for Secure Machine Unlearning

- **匹配关键字:** homomorphic encryption

- **作者:** David Balbás, Dario Fiore, Georgios Raikos, Damien Robissout, Claudio Soriente

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/510) | [PDF](https://eprint.iacr.org/2026/510.pdf)


> **研究背景:** 现有机器卸载方法假设服务器诚实执行所有卸载请求，但在实践中这一假设过于严格。即使卸载请求可验证，服务器仍可能保留数据副本或继续使用数据进行训练。因此，需要一种能够在模型生命周期中保护数据机密性的安全模型。
>
> **主要贡献:** 作者提出了一个形式化的安全模型，并设计了一个基于全同态加密（FHE）和安全多方计算（MPC）的机器学习框架，确保卸载请求被正确执行且用户的数据被遗忘。
>
> **达到效果:** 该框架能够在分布式环境中处理训练、卸载和推理请求，并在诚实但好奇的服务器模型下提供安全性保证。
>
> **技术梗概:** 通过结合全同态加密（FHE）和安全多方计算（MPC），作者实现了对卸载请求的加密验证，确保数据在整个生命周期中的机密性。

---
### [推荐] [2026/515] Privacy at your Fingertips: Enabling Rapid Client-Side Operations in Fully Homomorphic Encryption

- **匹配关键字:** homomorphic encryption

- **作者:** Aikata Aikata, Florian Krieger, Sujoy Sinha Roy

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/515) | [PDF](https://eprint.iacr.org/2026/515.pdf)


> **研究背景:** 全同态加密（FHE）允许用户在不泄露底层数据的情况下将大量计算任务外包给服务器，这使其在隐私保护机器学习等领域具有广泛应用前景。然而，现有的所有FHE方案都面临着加密/解密速度慢和密文膨胀率高的问题，导致其实用性受到极大限制。
>
> **主要贡献:** 本文提出了一种新颖的	onetwo方法来优化客户端侧同态加密操作，并通过利用启动过程减少了密文膨胀并降低了服务器及客户端的通信开销。此外，该技术还消除了对浮点数算术的要求，从而简化了FHE的实现流程。
>
> **达到效果:** 实验结果表明，所提出的技术将加密/解密计算和通信需求分别降低了97%。通过开发兼容软件和硬件平台的框架，并进行综合设计分析、FPGA原型制作以及ASIC合成和微控制器性能评估，证明了该方法的有效性。
>
> **技术梗概:** 该技术利用内置的FHE例行程序并保持安全性和精度保证，同时减少了客户端的编码和解码需求。

---
### [推荐] [2026/519] A Generalized Partial Exposure Lattice Attack Against an RSA variant Based on Cubic Pell Curves

- **匹配关键字:** lattice

- **作者:** Michel Seck, Hortense Boudjou Tchapgnouo

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/519) | [PDF](https://eprint.iacr.org/2026/519.pdf)


> **研究背景:** 该研究针对Nitaj和Seck基于立方佩尔方程的RSA变种进行攻击，旨在改进现有方法以处理更广泛的情况。
>
> **主要贡献:** 作者提出了一种新的部分暴露格攻击方法，可以应用于已知p或q的部分位值的情况。
>
> **达到效果:** 该攻击能够有效利用公钥和私钥之间的关系，即使在有限的密钥信息下也能提高破解效率。
>
> **技术梗概:** 通过分析关键方程eu_0 - (p-1)^2(q-1)^2 v_0 = w_0，并结合格理论技术实现攻击。

---
### [2026/507] Practically Efficient Linear-Time Protocols for Server-Aided Private Set Union and Third Party Private Set Operations

- **作者:** Foo Yee Yeo, Jason H. M. Ying

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/507) | [PDF](https://eprint.iacr.org/2026/507.pdf)


> **研究背景:** 本文提出了服务器辅助的私有集合并集（PSU）协议以及第三方私有集合差集（TP-PSD）和第三方私有对称差集（TP-PSymD）协议，旨在提高这些操作在实际应用中的效率。
>
> **主要贡献:** 该研究的主要贡献在于设计了更高效的第三方私有集合运算协议，相比前人工作，在计算复杂度和实用性上都有显著提升。
>
> **达到效果:** 实验结果显示，本文提出的服务器辅助的PSU协议比现有最先进的两方PSU协议快几倍，并且能够在更大的数据集上运行。
>
> **技术梗概:** 通过优化算法设计和采用高效的密码学技术，实现了快速执行和大规模应用的能力。

---
### [2026/508] Schnorr Blind Signatures and Signed ElGamal KEM in Algebraic Group Action Model

- **作者:** Dung Hoang Duong, Willy Susilo, Chuanqi Zhang

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/508) | [PDF](https://eprint.iacr.org/2026/508.pdf)


> **研究背景:** 研究背景：Schnorr盲签名是效率最高且应用最广泛的盲签名方案之一。CSI-Otter作为首个基于类Schnorr构造的密码学方案，尽管在OR关系上有所创新，但其并发安全性被证明存在漏洞。
>
> **主要贡献:** 主要贡献在于首次在代数群作用模型（AGAM）和随机预言机模型（ROM）下，严格证明了基于类Schnorr构造的签名方案的安全性，并提出了首个具备紧致安全性的类Schnorr盲签名。
>
> **达到效果:** 达到的效果是填补了CSI-Otter及其类似方案在并发安全性上的不足，为后续研究提供了坚实的理论基础。
>
> **技术梗概:** 技术梗概：通过证明基于类Schnorr构造的签名方案的安全性，并利用群作用离散对数假设（GADLOG）和一个更多组作用离散对数假设（OMGADLOG），实现了紧致并发安全性的证明。

---
### [2026/509] PUFF: Maximally Proactive Security for Free in Perfectly Secure MPC with Guaranteed Output Delivery

- **作者:** Jiarui Li, Mengzhen Zou, Guidong Li, Guoyan Zhang, Chen Qian

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/509) | [PDF](https://eprint.iacr.org/2026/509.pdf)


> **研究背景:** 在完美安全多方计算(MPC)中实现主动安全性并保证输出交付是一个重大挑战，因为传统协议要求所有参与者持续在线，这使得它们在许多应用场景中不可行。
>
> **主要贡献:** 本文提出了一种统一框架和基本构建块来构造层化模型下的协议，并使用Shamir和CNF秘密共享进行实例化，从而开发了高效的可验证秘密共享(VSS)和安全乘法协议以实现主动安全性。
>
> **达到效果:** 应用该框架，我们构建了层化MPC协议，显著降低了每门电路通信复杂度和所需的总层数。具体而言，基于Shamir的MPC实现了每门$O(n^6)$的通信复杂性，并且总层数为$D+13$，相比之前的工作在门级通信复杂度上从$O(n^9)$降低到了$O(n^6)$，并且总层数从$10D+8$减少到$D+13$。
>
> **技术梗概:** 该工作利用了层化MPC模型，并通过引入高效的VSS和安全乘法协议来实现主动安全性。

---
### [2026/512] Securely Scaling Autonomy: The Role of Cryptography in Future Unmanned Aircraft Systems (UAS)

- **作者:** Paul Rochford, William J Buchanan, Rich Macfarlane, Madjid Tehrani

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/512) | [PDF](https://eprint.iacr.org/2026/512.pdf)


> **研究背景:** 研究背景：无人驾驶航空系统（UAS）的去中心化带来了在受限资源和争议环境中建立安全通信和共识的重大挑战。
>
> **主要贡献:** 主要贡献在于评估了两种加密技术在UAS中的应用，即MLS用于组密钥交换，以及FROST和BLS阈值签名用于分散式共识。
>
> **达到效果:** 研究结果表明，MLSpp库不适用于动态环境，而OpenMLS则表现出高性能和可扩展性；Zcash FROST实现因其安全特性和高效的验证而在持续、高流量用例中表现最佳。
>
> **技术梗概:** 技术概要是通过一系列静态评估、网络模拟和新型批量签名基准测试来衡量这些开源库的计算效率和实际鲁棒性。

---
### [2026/514] Secure Matrix Invertibility Testing over Fields of Small Order or Characteristics

- **作者:** Seungwoo Han, Jooyoung Lee, Seungmin Park, Mincheol Son

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/514) | [PDF](https://eprint.iacr.org/2026/514.pdf)


> **研究背景:** 针对有限域的小阶数或特征下的多方矩阵可逆性测试是多变量二次(MQ)签名方案阈值化中的关键操作，但现有解决方案要么在安全性和效率上存在不足。
>
> **主要贡献:** 作者提出了两种新的协议来实现完美隐私的多方矩阵可逆性测试，分别适用于小阶数域和小特征域。
>
> **达到效果:** 这两种协议均实现了在线和离线轮次之间的权衡，在保证安全性的同时提高了计算和通信效率。
>
> **技术梗概:** 第一种协议通过扩展Cramer-Damgård协议并结合字段提升技术实现；第二种基于Samuelson-Berkowitz算法的多方计算，特别适用于小特征域。

---
### [2026/516] Towards Compact UOV-Based MQ Signatures: Rectangular and Lifted Whipping Structures

- **作者:** Quang-Duc Nguyen, Minh Hieu Nguyen

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/516) | [PDF](https://eprint.iacr.org/2026/516.pdf)


> **研究背景:** 多变量二次(MQ)签名方案提供了快速的签名和验证过程，并且具有较小的签名大小，但其实际应用受限于较大的公钥。
>
> **主要贡献:** 作者提出了两种改进技术：矩形乳化矩阵和提升乳化矩阵，以进一步减小UOV基MQ签名的公钥大小并提高性能。
>
> **达到效果:** 通过结合这两种方法，作者设计了一种新的变体MAYO$^−_L$，并在已知伪造和密钥恢复攻击中提供了详细的安全性分析，并提出了在相同安全性水平下改进的公钥和签名尺寸参数集。
>
> **技术梗概:** 矩形乳化矩阵减少了基础UOV实例所需的方程数量，而提升乳化矩阵则将其提升到扩展域以避免已知的提升系统攻击。

---
### [2026/517] Multi-Instance Security Degradation of Code-Based KEMs

- **作者:** Alexander May, Gabriel Sá Diogo

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/517) | [PDF](https://eprint.iacr.org/2026/517.pdf)


> **研究背景:** 大多数基于码的KEM的安全性依赖于综合解码问题的难度。现有的现代方案如HQC和BIKE在单实例设置中考虑了DOOM类型的$\sqrt{n}$加速，但未充分评估多实例设置下的安全性。
>
> **主要贡献:** 作者分析了使用相同公钥生成多个会话密钥的多实例设置，并展示了如何利用DOOM技术加速解码过程以攻击这些KEM方案。
>
> **达到效果:** 研究结果表明，在HQC和BIKE等多实例设置中，随着会话密钥数量$M$的增加，安全性显著下降，某些情况下甚至低于NIST的安全标准。
>
> **技术梗概:** 通过构造具有$nM$个综合解码问题实例的新DOOM实例，攻击者能够加速单个会话密钥的重建过程。

---
### [2026/518] ${{\mathsf{SMA}^2\mathsf{RT}}}$ : Secret-Metadata Attribute-based Anonymous Rate-limited Tokens

- **作者:** Anna Lysyanskaya, Eileen Nolan

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/518) | [PDF](https://eprint.iacr.org/2026/518.pdf)


> **研究背景:** 在高流量在线服务中，如隐私保护的验证码绕过或计量付费墙，服务提供商需要过滤恶意流量而不泄露用户隐私。现有的带有隐藏元数据的秘密属性凭证（ATPM）解决了这一问题，但它们存在通信复杂度高和缺乏细粒度策略支持的问题。
>
> **主要贡献:** $\mathsf{SMA}^2\mathsf{RT}$首次在隐藏元数据的上下文中支持选择性属性披露，结合了匿名凭证和匿名令牌的研究成果。
>
> **达到效果:** 该方案通过使用等价类签名（SEQ）实现了“一次发行，多次使用”的能力，用户可以仅与发行人交互一次获取主凭据，并随后本地生成多达N个不可链接的有效令牌，无需进一步的在线通信。这大大减少了服务器负载和网络延迟，使其非常适合实时Web应用程序。
>
> **技术梗概:** 该技术利用等价类签名（SEQ）来实现“发行一次，多次使用”的能力，允许用户仅与发行人交互一次获取主凭据，并在本地生成多达N个不可链接的有效令牌。

---
### [2026/520] Sparse optimisation and quantum-inspired encoding for ransomware detection

- **作者:** Elodie Mutombo Ngoie, Mike Wa Nkongolo

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/520) | [PDF](https://eprint.iacr.org/2026/520.pdf)


> **研究背景:** 针对高维网络流量和复杂混淆技术导致的勒索软件检测难题，现有特征选择方法常面临冗余、噪声及维度灾难的问题，影响了泛化能力和解释性。
>
> **主要贡献:** 提出了一种结合梯度优化与Minimax Concave Penalty (MCP)以强制稀疏性的BioSparse-MCP框架，并采用Rotated Circular Partitioning (RCP)策略提升特征选择的组织结构，同时融入Quantum Feature Mapping (QFM)-启发的空间变换。
>
> **达到效果:** 该方法在149,043个网络流量实例上实现了高检测精度，且具有较低的误报率。
>
> **技术梗概:** 通过经典模拟RCP和QFM操作，保持了与传统机器学习管道的兼容性，并确保实时部署无需专用硬件。

---
### [2026/521] UniMSM: An Efficient and Flexible Hardware Accelerator for Multi-Scalar Multiplication

- **作者:** Kaixuan Wang, Yifan Yanggong, Chenti Baixiao, Xiaoyu Yang, Lei Wang

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/521) | [PDF](https://eprint.iacr.org/2026/521.pdf)


> **研究背景:** 多标量乘法（MSM）是密码系统中的核心操作，涉及大量带有数百位模算术的项。
>
> **主要贡献:** UniMSM 设计了一种基于扩展雅可比坐标系统的流水线点加器，并采用时间复用数据通路来减少模乘成本并保持高吞吐量。
>
> **达到效果:** 相比之前的FPGA加速器，UniMSM 在面积-时间积上提高了2.12倍；在ASIC中，UniMSM 达到了现有最佳加速器的3.85倍性能提升。
>
> **技术梗概:** 通过引入冲突感知调度方案来解决桶更新冲突，并开发了一种硬件友好的Pippenger算法变体以减少中间存储开销和聚合中的串行依赖性。

---

## 更新: 2026-03-15 16:26

*新增 8 篇论文 (编号 499--506)*

### [推荐] [2026/499] Accelerating FAEST Signatures on ARM: NEON SIMD AES and Parallel VOLE Optimization

- **匹配关键字:** post-quantum

- **作者:** Seung-Won Lee, Ha-Gyeong Kim, Min-Ho Song, Si-Woo Eum, Hwa-Jeong Seo

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/499) | [PDF](https://eprint.iacr.org/2026/499.pdf)


> **研究背景:** FAEST是一种后量子数字签名候选方案，其性能主要受VOLE-in-the-Head阶段中重复的AES-CTR基PRG调用的影响。
>
> **主要贡献:** 作者提出了一种针对ARM优化的方法，利用通用NEON SIMD指令加速FAEST签名过程中的瓶颈问题，而不依赖于ARMv8 Crypto Extensions。
>
> **达到效果:** 该优化在Raspberry Pi 4和Apple M2上分别实现了最高136.9倍和330.1倍的速度提升，单线程NEON实现优于OpenSSL的软件AES，而全NEON加多线程配置则超越了所有测试参数的最佳参考配置。
>
> **技术梗概:** 优化结合了寄存器驻留256字节S-box、TBL/TBX基于四阶段SubBytes、4路和8路并行AES块处理、专为FAEST树结构设计的固定大小PRG路径以及基于pthread的独立VOLE任务批处理级并行化。

---
### [推荐] [2026/502] Efficient RLWE based Chosen-Ciphertext Secure Dual-Receiver Encryption and Sender-Binding KEM in the Standard Model

- **匹配关键字:** LWE

- **作者:** Laurin Benz, Robert Brede

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/502) | [PDF](https://eprint.iacr.org/2026/502.pdf)


> **研究背景:** 文章旨在解决在标准模型下实现具有IND-CCA2和IND-SB-CPA安全性的双接收者加密(DRE)和关键封装机制(KEM)，以提高效率并满足实际应用需求。
>
> **主要贡献:** 作者提出了基于RLWE的DRE和KEM方案，它们分别实现了IND-CCA2和IND-SB-CPA安全性，并且相比之前的工作在密钥大小和密文大小上有了显著改进。
>
> **达到效果:** 所提出的方案在标准模型下是安全的，其密钥大小为150 KB，密文大小为100 KB，比现有结果提高了10到100倍的效率。
>
> **技术梗概:** 该研究采用了基于RLWE的技术，并通过改进证明技术来确保在标准模型下的安全性，从而实现高效的安全通信方案。

---
### [推荐] [2026/504] Compression And Decompression Under FHE Using Error-Correcting Codes and Copy-And-Recurse

- **匹配关键字:** homomorphic encryption

- **作者:** Adi Akavia, Hayim Shaul, Ofer Shayevitz

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/504) | [PDF](https://eprint.iacr.org/2026/504.pdf)


> **研究背景:** 压缩作为计算机科学中的基本问题，已有数十年历史。在全同态加密(FHE)环境下，由于需要同时考虑压缩和解压的隐私性，使得该问题变得更加复杂且具有挑战性。
>
> **主要贡献:** 本文首次提出了能够在FHE环境中进行有效压缩与解压的非平凡算法，并结合了复制-递归技术与压缩与纠错码之间的已知对偶关系。
>
> **达到效果:** 实验结果表明，所提出的解压算法比传统方法更快，这在中间存在受限制代理且通信和计算受限的系统中尤为重要。
>
> **技术梗概:** 该研究利用了复制-递归技术和纠错码理论来设计压缩与解压算法，在FHE环境下实现了高效的数据处理。

---
### [2026/500] Expander properties of superspecial isogeny digraphs with level structure

- **作者:** Thomas Decru, Krijn Reijnders

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/500) | [PDF](https://eprint.iacr.org/2026/500.pdf)


> **研究背景:** 研究背景：Charles、Goren和Lauter证明了超奇异$\ell$-isogeny图是拉马努詹图，即最优扩展器。然而，Jordan和Zaytman指出这一结论在二维情况下不再成立，但Florit和Smith展示了这些图仍然表现出良好的扩展性质。
>
> **主要贡献:** 主要贡献：作者研究了具有$(\ell,\ell)$-级结构的$(\ell)^g$-isogeny有向图，并通过实证证据表明，在一维情况下它们是拉马努詹图，对于$\ell=2$在二维情况下的表现也非常好。
>
> **达到效果:** 达到的效果：作者的研究结果为超奇异isogeny图在不同维度和参数下是否仍能保持良好的扩展性质提供了新的见解，并提出了一个主要猜想来解释这些现象。
>
> **技术梗概:** 技术梗概：研究采用了对好扩展路径的限制，从而使得生成的有向图表现出优秀的扩展性能。

---
### [2026/501] More Brisés in Ballet: Extending Differential and Linear Cryptanalysis

- **作者:** Emanuele Bellini, Gabriele Bellini, Alessandro De Piccoli, Michela Gallone, David Gerault, Yun Ju Huang, Paul Huynh, Matteo Onger, Simone Pelizzola, Andrea Visconti

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/501) | [PDF](https://eprint.iacr.org/2026/501.pdf)


> **研究背景:** 该研究针对Ballet分组密码家族进行了新的密码分析，这是一个简化了的Lay-Massey ARX结构，具有线性密钥调度，曾在中国2018-2020年密码算法竞赛中获胜。
>
> **主要贡献:** 研究人员首次提供了古典密钥恢复攻击，并发现了新的差分和线性路径（分别达到15轮差分和16轮线性），改进了不可能差分路径（从7轮提高到8轮），并首次进行了Ballet的差分-线性分析（最多20轮）。
>
> **达到效果:** 研究结果导致对Ballet-128/128/46和Ballet-128/256/48分别进行到了16轮和17轮的密钥恢复攻击，扩展了对该ARX设计加密理解，并为该算法的安全余量提供了新的见解。
>
> **技术梗概:** 研究采用了差分密码分析、线性密码分析以及差分-线性联合分析等技术来评估Ballet的安全性。

---
### [2026/503] SwiftSNNI: Optimized Scheduling for Secure Neural Network Inference (SNNI) on Multi-Core Systems

- **作者:** Kanwal Batool, Saleem Anwar, Francesco Regazzoni, Andy Pimentel, Zoltán Ádám Mann

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/503) | [PDF](https://eprint.iacr.org/2026/503.pdf)


> **研究背景:** Secure Neural Network Inference (SNNI)旨在保护加密数据的隐私，但在实际部署中面临高预处理开销、显著的通信成本以及顺序执行的问题，导致吞吐量低、系统资源利用率低下、队列延迟长且可扩展性差。
>
> **主要贡献:** 	extit{SwiftSNNI}提出了一种统一的、资源感知的调度框架，通过结合离线和在线策略来最大化并行度，并将未来请求的预处理阶段与当前活动的推理任务重叠执行。
>
> **达到效果:** 在五种基准神经网络（M1, M2, HiNet, AlexNet, VGG-16）下的不同负载和随机到达率下进行评估，	extit{SwiftSNNI}相比并行化顺序基线(MS-SHARK)实现了高达97%的平均输入延迟减少、81%的工期缩短（约5.4倍加速）、吞吐量提高5.6倍，并且将平均等待时间减少了超过99%。
>
> **技术梗概:** 	extit{SwiftSNNI}通过优化离线和在线任务调度，利用约束优化问题模型重叠预处理阶段与推理阶段的执行，同时支持提前通知以实现主动预处理，从而提高整体性能。

---
### [2026/505] SCALE-FL: Scalable Cryptography-based Aggregation with Lightweight Enclaves for Federated Learning

- **作者:** Micah Brody, Antonia Januszewicz, Jiachen Zhao, Nirajan Koirala, Taeho Jung

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/505) | [PDF](https://eprint.iacr.org/2026/505.pdf)


> **研究背景:** 隐私保护联邦学习（PPFL）旨在确保在医疗保健、智能电网和物联网等场景中用户数据的安全性和隐私性。然而，维护跨多个周期的众多用户的复杂关系使得在整个PPFL过程中保证安全性和隐私性具有挑战性。
>
> **主要贡献:** SCALE-FL提出了一个创新方案，结合了最先进的私有流聚合（PSA）协议和可信执行环境（TEE），以实现近明文性能的安全联邦学习。
>
> **达到效果:** 通过使用PSA协议进行聚合，SCALE-FL能够在不需每个用户存储密钥或TEE使用的情况下保护信息隐私，并且TEE仅在明文中安全处理聚合结果，从而减少了每客户端每次周期的开销。
>
> **技术梗概:** 该方案采用了先进的PSA协议来收集用户信息，并利用TEE隐藏原始聚合的信息，实现了高效的安全联邦学习。

---
### [2026/506] Unclonable Encryption in the Haar Random Oracle Model

- **作者:** James Bartusek, Eli Goldin

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/506) | [PDF](https://eprint.iacr.org/2026/506.pdf)


> **研究背景:** 本文旨在构建在Haar随机算子模型下的不可克隆加密方案，该模型假设所有参与方可以访问一个Haar随机酉矩阵及其共轭转置、逆和转置操作。
>
> **主要贡献:** 我们首次证明了在micocrypt世界中（即可能不存在单向函数的世界），可重用的不可克隆加密是存在的，并且提出了路径记录框架下的单位元重新编程引理，这是我们的主要技术贡献之一。
>
> **达到效果:** 该方案满足标准的不可克隆区分安全性定义，支持密钥重用，并能加密任意长度的消息。
>
> **技术梗概:** 我们利用了最近引入的路径记录框架来证明一个自然的“单位元重新编程引理”，这可能具有独立的研究价值。

---

## 更新: 2026-03-11 19:53

*新增 13 篇论文 (编号 485--497)*

### [推荐] [2026/485] SIMD HSS and aHMAC from Interval Encoding with Application to One-Bit-Per-Gate Garbling

- **匹配关键字:** homomorphic encryption, LWE

- **作者:** Jaehyung Kim, Hanjun Li, Huijia Lin, Zeyu Liu

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/485) | [PDF](https://eprint.iacr.org/2026/485.pdf)


> **研究背景:** Homomorphic Secret Sharing (HSS)和代数同态MAC（aHMAC）作为高效替代方案，正在取代全同态加密（FHE）和属性基加密（ABE），用于秘密共享值上的同态计算。
>
> **主要贡献:** 首次提出了基于RLWE假设的变体，并结合新的区间系数编码方法，实现了SIMD评估技术，显著提高了HSS和aHMAC的效率。
>
> **达到效果:** 通过支持每环元素$\sqrt{n}$倍批处理加法和乘法，在$O(\log n)$环操作内实现，相比先前直接构造方案在累积效率上获得了约$\tilde O(\sqrt{n})$的改进。
>
> **技术梗概:** 采用新的区间系数编码方法嵌入了每环元素$\sqrt{n}$个整数值插槽，并支持$\sqrt{n}$倍批处理加法和乘法，仅需$O(\log n)$环操作实现SIMD评估技术。

---
### [推荐] [2026/487] Bootstrapping-Free Blind PCS: Achieving Constant Depth and Linear Prover

- **匹配关键字:** homomorphic encryption

- **作者:** Kexi Huang, Yanpei Guo, Wenjie Qu, Jiaheng Zhang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/487) | [PDF](https://eprint.iacr.org/2026/487.pdf)


> **研究背景:** 该研究旨在设计一种高效的安全多项式承诺方案（PCS），特别适用于处理加密系数，无需昂贵的重新归一化操作，突破了复杂度与深度之间的权衡。
>
> **主要贡献:** 贡献在于提出了首个在非二进制域上具有严格线性证明者复杂性的盲PCS，并且避免了昂贵的重新归一化操作，同时保持了常数倍的乘法深度。
>
> **达到效果:** 实验结果显示，在大规模电路规模下，该方案的证明者比现有的领先方案如phalanx和laminate更快。
>
> **技术梗概:** 技术上采用了广义RAA码，这是一种将二进制RAA结构扩展到任意非二进制素域F_p的高效纠错码，并结合了Ligero的IOPP框架。

---
### [推荐] [2026/489] Threshold Oblivious Pseudorandom Functions from Isogeny Group Actions

- **匹配关键字:** post-quantum

- **作者:** Robi Pedersen

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/489) | [PDF](https://eprint.iacr.org/2026/489.pdf)


> **研究背景:** 本文提出了一种基于Isogeny组动作的新颖可验证不可知伪随机函数（VOPRF），旨在提高安全性并实现阈值协议。
>
> **主要贡献:** 贡献在于设计了一个新的证明协议，将其集成到OPRF协议中以实现输出的可验证性，并且能够方便地转换为阈值协议。
>
> **达到效果:** 该构造在保持通信成本略有增加的情况下，比现有最佳方案快一倍，实现了首个基于Isogenies的阈值VOPRF，并且输入和输出大小与服务器方数量无关。
>
> **技术梗概:** 技术上，通过模块化设计不同的子程序，并使用模拟论证替换这些子程序以实现其阈值对应物。

---
### [2026/486] White-Box Attacks on PhotoDNA Perceptual Hash Function

- **作者:** Maxime Deryck, Diane Leblanc-Albarel, Bart Preneel

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/486) | [PDF](https://eprint.iacr.org/2026/486.pdf)


> **研究背景:** PhotoDNA是一种广泛部署的感知哈希函数，用于检测非法内容如儿童色情材料（CSAM）。然而，该研究揭示了其设计弱点，并展示了如何利用这些弱点进行白盒攻击。
>
> **主要贡献:** 作者首次提供了Allège PhotoDNA的数学描述，并识别出其算法是分段线性和可微的，哈希值仅依赖于每个像素RGB值之和。此外，还证明了基于梯度优化技术和二次规划可以利用这些弱点生成视觉上吸引人的精确碰撞和第二前象限。
>
> **达到效果:** 攻击成功率达到接近或等于100%，并在个人笔记本电脑上运行几秒到几分钟内即可完成；这表明PhotoDNA的不可逆性被推翻，并且能够产生与原始图像感知上相同的高质量图像，但哈希值却相差甚远以逃避检测。
>
> **技术梗概:** 研究采用了基于梯度优化技术和二次规划的方法来利用Allège PhotoDNA和PhotoDNA的设计弱点，生成视觉吸引力强的精确碰撞和第二前象限；并通过大量不同图像集实现了攻击效果。

---
### [2026/488] SoK: Offline Finding Protocols for Lightweight Location Tracking

- **作者:** Akshaya Kumar, Carolina Ortega Pérez, Joseph Jaeger, Thomas Ristenpart, Michael A. Specter

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/488) | [PDF](https://eprint.iacr.org/2026/488.pdf)


> **研究背景:** 研究背景：离线查找（OF）协议通过蓝牙追踪标签帮助数亿用户定位物品，但其规模和跟踪能力带来了隐私风险以及受害者被利用的风险。因此，学术界与实践者提出了多种加密及非加密的缓解措施以改善隐私保护和反骚扰防护。
>
> **主要贡献:** 主要贡献：作者系统化了OF协议的景观，通过分析49篇研究论文和技术规范开发了一个分类法，并对四大主流部署及六种学术构造进行了评估，明确了设计选择、已知攻击以及各设计之间的权衡。
>
> **达到效果:** 达到的效果：提供了一种简单但安全的OF协议，澄清了OF协议背后的必要加密组件；同时概述了物理层攻击和用户体验问题如何削弱保护效果。
>
> **技术梗概:** 技术梗概：通过构建分类法来指导评估，并综合分析了设计选择、已知攻击及各设计之间的权衡。

---
### [2026/490] Towards Modeling Cybersecurity Behavior of Humans in Organizations

- **作者:** Klaas Ole Kürtz

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/490) | [PDF](https://eprint.iacr.org/2026/490.pdf)


> **研究背景:** 本文旨在综合分析组织内人员（尤其是公司员工）在网络安全行为中的驱动力，并将意识、安全文化及可用性等关键概念整合进一个连贯的理论框架中。
>
> **主要贡献:** 作者通过对比多个相关的行为模型，提出了一个适用于组织内部人员行为的理论框架，为基于自然语言处理的自主AI安全提供了参考。
>
> **达到效果:** 该研究不仅深化了对人类网络安全行为的理解，还为开发针对AI代理操纵攻击的安全策略提供了理论基础。
>
> **技术梗概:** 通过构建结合意识、安全文化和可用性的综合模型，并将其与现有行为模型进行对比分析来实现上述贡献。

---
### [2026/491] SoK: Private Transformer-Based Model Inference

- **作者:** Yuntian Chen, Tianpei Lu, Zhanyong Tang, Bingsheng Zhang, Zhiying Shi, Yuxiang Luan, Zhuzhu Wang

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/491) | [PDF](https://eprint.iacr.org/2026/491.pdf)


> **研究背景:** 针对隐私保护的需求，出现了多种用于Transformer模型推理的协议，这些协议利用了不同的加密工具，并在计算、通信和准确性之间做出了各自的权衡。
>
> **主要贡献:** 本文系统地分析了现有方法，从多个性能角度出发，指出了它们的局限性和研究空白。
>
> **达到效果:** 通过标准化配置下的重新基准测试，我们为不同部署场景下平衡协议权衡提供了指导原则。
>
> **技术梗概:** 采用全面的评估方法，包括系统的文献回顾、实证分析和重新实现关键系统以确保可重复性。

---
### [2026/492] The Landscape of Reusable Garbling

- **作者:** Anasuya Acharya, Carmit Hazay, Rahul Satish

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/492) | [PDF](https://eprint.iacr.org/2026/492.pdf)


> **研究背景:** 研究背景：重用性是密码学中的一个核心主题，出现在多种不同的情境中，如不可区分的混淆（iO）、功能加密（FE）等。然而，尽管一次性混淆已成为广泛应用的基本原语，其重用变体却受到了较少的关注，通常仅作为FE的一个副产品进行研究。
>
> **主要贡献:** 主要贡献：作者重新审视了重用性混淆的基础，并构建了一个框架来明确与其他重用性原语的关系。他们展示了重用性混淆等价于单一密钥私钥功能加密的单钥变体，将其作为一个独立的原始概念进行隔离。
>
> **达到效果:** 达到的效果：这一发现进一步表明，重用性可以完全在私钥设置中实现，无需调用公钥机制，并且直接从几个固有的重用性原语展示了构建方法。
>
> **技术梗概:** 技术梗概：作者通过建立重用性混淆与单一密钥私钥功能加密之间的等价关系，提供了一种新的视角来理解重用性混淆的实现方式。

---
### [2026/493] The SQInstructor: a guide to SQIsign and the Deuring Correspondence with level structures

- **作者:** Giacomo Borin, Luca De Feo, Guido Maria Lido, Sina Schaeffler

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/493) | [PDF](https://eprint.iacr.org/2026/493.pdf)


> **研究背景:** 研究旨在通过引入层结构来扩展SQIsign签名方案，以增强其灵活性和安全性。
>
> **主要贡献:** 贡献在于提出了一个通用框架，并具体实例化为一维和二维正则性同态，从而实现了新的超奇异椭圆曲线与层结构之间的德林格对应关系。
>
> **达到效果:** 结果是成功设计并实现了一种新的约束范数方程的解法，并增强了SQIsign签名方案的安全性和实用性。
>
> **技术梗概:** 技术上采用了正则性同态和层结构的概念，通过数学方法解决了特定类型的约束规范方程。

---
### [2026/494] $\mathsf{GlueLUT}$: Generalized Lookup Table Arguments over Residue Rings via Auxiliary Fields

- **作者:** Yuanju Wei, Zhelei Zhou, Xinxuan Zhang, Songyu Wu, Binwu Xiang, Cheng Hong, Yi Deng

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/494) | [PDF](https://eprint.iacr.org/2026/494.pdf)


> **研究背景:** 现有的高效率查找表（LUT）论证大多针对大域，而越来越多的应用天然基于环结构，在剩余环$\mathbb{Z}_Q$上进行算术运算。直接将域上的LUT技术扩展到环上会遇到根本性的障碍。
>
> **主要贡献:** $\mathsf{GlueLUT}$框架提供了一种通用方法，用于在任意剩余环$\mathbb{Z}_Q$上构建支持任意表的查找表论证，并引入了交叉模数一致性（CMC）PIOP作为关键工具。
>
> **达到效果:** 通过使用$\mathsf{GlueLUT}$框架和优化实例化，解决了直接在环上构造LUT论证的问题，提高了效率并扩大了应用范围。实现了$\mathsf{GlueLUT}$-$\mathsf{v1}$和$\mathsf{GlueLUT}$-$\mathsf{v2}$作为独立的PIOP。
>
> **技术梗概:** 利用CMC PIOP将查找操作置于辅助域$\mathbb{F}_P$上，并验证两个模数下证人的一致性，从而绕过了直接在环上构建LUT论证的障碍。

---
### [2026/495] Linear Code Equivalence via Plücker Coordinates

- **作者:** Gessica Alecci, Giuseppe D'Alconzo

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/495) | [PDF](https://eprint.iacr.org/2026/495.pdf)


> **研究背景:** 研究背景：线性码等价问题（LCE）的假设难度是LESS签名方案及其他具有高级功能的签名方案安全性的核心。该问题要求确定两个线性码是否等价，即是否存在一个置换矩阵P和一个对角矩阵D使得Q=DP成立。
>
> **主要贡献:** 主要贡献：作者通过研究多项式矩阵对线性码的作用，并利用代数几何工具（如Plücker坐标和不变有理函数场），提出了确定不变函数生成元的方法，避免了Reynolds算子或Gröbner基计算的依赖。
>
> **达到效果:** 达到的效果：对于给定的等价码，作者能够为每个不变函数构造一个多项式作为置换矩阵P的根，但这些多项式的度数和单项式的数量在密码学相关参数下过高，使得实际操作不可行。
>
> **技术梗概:** 技术梗概：通过分析对角矩阵作用于线性码的过程（即坐标缩放），作者找到了不变有理函数场的代数独立生成元，并利用这些结果构造了多项式以表示置换矩阵P。

---
### [2026/496] On quadratic equations of $q$-regular tree and    their applications in Graph Theory and Cryptography.

- **作者:** Vasyl Ustimenko, Tymoteusz Chojecki

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/496) | [PDF](https://eprint.iacr.org/2026/496.pdf)


> **研究背景:** 研究了$q$-规则树图$D(n,q)$及其连通分量$CD(n,q)$在极值图论、谱图论、代数图论、对称密码学和低密度奇偶校验码理论中的应用。
>
> **主要贡献:** 提出了基于这些大周长的森林的新非交换密码算法，特别是修改了Diffie-Hellman协议，并提出了一种基于$F_q[x_1, x_2, \dots, x_n]$上的仿射Cremona同构半群共轭幂问题复杂性的安全方案。
>
> **达到效果:** 该方案允许用户在$O(n^2)$时间内从$(F_q)^n$中推导出碰撞向量，且逆协议具有El Gamal类型，可用于加密或创建数字签名。
>
> **技术梗概:** 通过引入基于$q$-规则树图的非交换密码算法，并利用共轭幂问题的复杂性来确保安全性。

---
### [2026/497] Trustworthy Agent Network: Trust in Agent Networks Must Be Baked In, Not Bolted On

- **作者:** Yixiang Yao, Yuhang Yao, Xinyi Fan, Jiechao Gao, Jie Wang, Minjia Zhang, Srivatsan Ravi, Carlee Joe-Wong

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/497) | [PDF](https://eprint.iacr.org/2026/497.pdf)


> **研究背景:** 随着大型语言模型的快速发展，自主运行的语言模型代理能够进行复杂的推理和执行任务。这些代理从孤立操作过渡到协作生态系统时，形成了代理间网络（A2A），其中异构代理自主协调解决多步骤任务。然而，这种网络引入了现有代理对齐技术无法解决的系统性漏洞，如对抗组合、语义不一致和级联运行失败等。
>
> **主要贡献:** 本文提出了一种全面的概念框架，通过四个设计支柱将信任嵌入到A2A系统中，以确保其安全性与可靠性。
>
> **达到效果:** 该框架能够从根本上解决现有协议在应对多代理协作时的局限性，从而提升整体系统的安全性和鲁棒性。
>
> **技术梗概:** 该研究采用了多层次的信任机制设计，包括但不限于身份验证、行为审计和动态信任评估等技术。

---

## 更新: 2026-03-09 21:07

*新增 7 篇论文 (编号 478--484)*

### [2026/478] A Hardware/Software Co-Optimization of HQC Using Tightly-Coupled Accelerators on a 32-bit Ibex Core

- **作者:** Seog Chung Seo, YoungBeom Kim

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/478) | [PDF](https://eprint.iacr.org/2026/478.pdf)


> **研究背景:** 本文研究了在32位Ibex RISC-V核心上通过紧密耦合的加速器实现Hamming Quasi-Cyclic (HQC)算法的硬件/软件协同优化，以提高其性能。
>
> **主要贡献:** 贡献在于提出了一个统一的乘法器，并设计了一个Keccak置换加速器来支持高效的随机数生成；同时优化了多项式乘法在Ibex核心上的实现方法。
>
> **达到效果:** 通过这些策略，实现了相对于参考实现几倍于原有性能的提升。
>
> **技术梗概:** 技术上采用了统一乘法器、Keccak置换加速器设计，并结合Toom–Cook和Karatsuba方法优化了多项式乘法执行过程中的内存访问次数。

---
### [2026/479] Strong Efficiency Lower Bounds for Byzantine Agreement

- **作者:** Clément Ducros, Julian Loss, Matthieu Rambaud

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/479) | [PDF](https://eprint.iacr.org/2026/479.pdf)


> **研究背景:** 研究背景：理解拜占庭共识（BA）的复杂性是分布式计算和密码学中的基本问题，现有的一些通信下界要么限制了协议的应用范围，要么只针对非常强大的适应式敌手。
>
> **主要贡献:** 主要贡献：本文提出了两个新的随机化拜占庭共识协议的通信复杂度下界，适用于标准的适应式敌手，并且在特定设置下改进了现有结果。
>
> **达到效果:** 达到的效果：这些新下界填补了理论与实际应用之间的差距，为设计更有效的拜占庭共识协议提供了指导。
>
> **技术梗概:** 技术梗概：通过重新审视现有的通信复杂度下界，并结合认证的通信信道假设，本文提出了改进的新下界。

---
### [2026/480] CHOPIN: Optimal Pairing-Based Multilinear Polynomial Commitments from Bivariate KZG

- **作者:** Juraj Belohorec, Pavel Hubáček, Aleksi Kalsta, Kristýna Mašková

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/480) | [PDF](https://eprint.iacr.org/2026/480.pdf)


> **研究背景:** CHOPIN是一种基于配对的多线性多项式承诺方案（PCS），旨在实现恒定大小的证明和线性时间验证者，通过模块化设计从双变量PCS构建。
>
> **主要贡献:** 该研究贡献了一种新的构造方法，将现有的单变量PCS编译器扩展到多线性PCS，并提供了直接的知识健全性证明。
>
> **达到效果:** 使用双变量KZG方案实例化时，CHOPIN在保持与MERCURY和Samaritan相似的证明大小的同时，实现了验证者时间的主要瓶颈两倍的速度提升。
>
> **技术梗概:** 技术上，CHOPIN通过减少验证者的计算复杂度来提高效率，并且只需要一个大型MSM操作，而之前的方案需要两个。

---
### [2026/481] Remise: Authorized Anonymous Communication Systems

- **作者:** Rohan Ravi, Paritosh Shukla, Adithya Vadapalli

- **分类:** Unknown

- **链接:** [论文](https://eprint.iacr.org/2026/481) | [PDF](https://eprint.iacr.org/2026/481.pdf)


> **研究背景:** Remise 是一种基于分布式透明RAM（DORAM）的双服务器授权匿名通信系统，旨在支持匿名公告板和匿名通信通道两种模式。
>
> **主要贡献:** 其主要贡献在于提出了一种轻量级且高效的访问控制机制，能够在至少有一个诚实服务器的情况下，防止服务器获取敏感信息，并提供内置审计功能。
>
> **达到效果:** 实验结果表明，在数据库大小为$22^{24}$的情况下，与PACL (Spectrum)相比，Remise的在线服务器时间提高了80倍。
>
> **技术梗概:** 通过在半诚实服务器内部生成标准基向量份额来实现内置审计，并保持授权证明以秘密共享形式分布在两个服务器上，从而实现在不泄露信息的前提下进行透明验证。

---
### [2026/482] Cryptanalysis of Two Alternating Moduli Weak PRFs

- **作者:** Kai Hu, Gregor Leander, Håvard Raddum, Arne Sandrib, Aleksei Udovenko

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/482) | [PDF](https://eprint.iacr.org/2026/482.pdf)


> **研究背景:** 本文针对近期提出的理论导向的弱伪随机函数（weak-PRFs）设计进行了新的密码分析攻击，揭示了初始安全论据中的不足之处。
>
> **主要贡献:** 作者提出了基于循环矩阵结构的新观察、Wagner广义生日技术的应用以及多项式系统转换的方法，展示了对这些弱-PRF候选者的更细致分析的必要性。
>
> **达到效果:** 通过这些方法，作者成功攻击了多个此类设计，证明了需要对它们的安全性进行显著改进。
>
> **技术梗概:** 研究采用了关于循环矩阵的新观察、Wagner广义生日技术的应用以及将问题转化为$\mathbb{F}_3$上的多项式系统的技术。

---
### [2026/483] Debt-Aware Bonding Curves: Non-Decreasing Floor Prices and Non-Liquidatable Borrowing

- **作者:** Ömer Demirel, Michael Lewkowitz, Tiago Santana

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/483) | [PDF](https://eprint.iacr.org/2026/483.pdf)


> **研究背景:** 去中心化借贷协议依赖于与波动的预言机价格绑定的清算机制，这在市场下跌时会导致系统性风险。
>
> **主要贡献:** 提出了一种债务感知离散债券曲线（DABC），这是一种具有特定地板段的价格非递减的分段线性债券曲线。
>
> **达到效果:** 这种机制确保了任何以或低于地板锚定的贷款抵押品价格下降都不会导致未偿清贷款的去抵押，从而消除了基于此借款模型的协议触发清算。
>
> **技术梗概:** 通过将发行、交易和借贷整合到一个合约中，并利用收益再投资于地板提升，实现了无清算风险的杠杆头寸。

---
### [2026/484] Signal Lost (Integrity): The Signal App is More than the Sum of its Protocols

- **作者:** Kien Tuong Truong, Noemi Terzo, Kenneth G. Paterson

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/484) | [PDF](https://eprint.iacr.org/2026/484.pdf)


> **研究背景:** Signal是一款提供端到端安全性的即时通讯应用，拥有数千万用户，并对其他安全消息应用的设计产生了重大影响。尽管被广泛分析，但其完整性属性在公开的威胁模型下仍存在未被发现的安全漏洞。
>
> **主要贡献:** 研究者发现了两个实际攻击方法，分别针对Signal的身份解析机制和密封发送功能，揭示了这些功能中的设计缺陷。
>
> **达到效果:** 第一个攻击使得恶意服务器可以在特定条件下注入消息，而用户难以察觉；第二个攻击则更为严重，允许恶意服务器在一对一及群组对话中注入任意消息。
>
> **技术梗概:** 研究通过详细分析Signal的协议实现和文档记录不全的功能来发现这些漏洞，并展示了具体的攻击流程以验证其可行性。

---

## 更新: 2026-03-08 10:34

*新增 26 篇论文 (编号 450--477)*

### [推荐] [2026/450] A flexible and polynomial framework for integer arithmetic in CKKS

- **匹配关键字:** homomorphic encryption

- **作者:** Lorenzo Rovida

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/450) | [PDF](https://eprint.iacr.org/2026/450.pdf)


> **研究背景:** 该研究旨在通过限制CKKS同态加密方案的明文空间，提出一种新的范式——discrete-CKKS，以牺牲近似计算为代价，实现更灵活和并行度更高的整数算术操作。
>
> **主要贡献:** 作者构建了一个基于多项式的简单计算设备来处理二进制向量表示的整数，并提出了与标准CKKS配置一致的参数化方法，支持在实数域$\mathbb{R}$中使用CKKS后再切换到整数域$\mathbb{Z}$。
>
> **达到效果:** 实验表明，该方案在所有操作（加法、乘法、比较和逻辑移位）上的延迟比当前最先进的技术低约三分之二。
>
> **技术梗概:** 通过利用多项式运算来实现标准模2算术操作，并避免了Kim和Noh提出的基于功能自举的模减法，从而实现了更灵活且与标准CKKS配置一致的参数化方法。

---
### [推荐] [2026/452] On the CCA security properties of a class of group-based linearly homomorphic encryption schemes

- **匹配关键字:** homomorphic encryption

- **作者:** Duong Hieu Phan, Renaud Sirdey, Jean Vacher

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/452) | [PDF](https://eprint.iacr.org/2026/452.pdf)


> **研究背景:** 研究背景：在Eurocrypt'25中，Libert解决了Damgard-ElGamal方案的CCA1安全性问题，并展示了其他几种方案也在特定假设下是CCA1安全的。然而，这些方案仅部分线性同态加密（LHE）。
>
> **主要贡献:** 主要贡献：作者提出了一种通用框架，用于设计在标准和可验证假设下实现真正线性同态加密且具有CCA1安全性的方案，并展示了新的Damgard-Paillier-ElGamal (DPEG) 方案。
>
> **达到效果:** 达到的效果：DPEG是首个仅在标准假设下证明其CCA1安全的真正线性同态加密方案。此外，该方案还能支持一次乘法操作并保持其CCA1安全性。
>
> **技术梗概:** 技术梗概：作者通过扩展Libert的方法，应用到一组基于群的公钥加密（PKE）方案中，并利用知识-of-指数模式来证明DPEG的安全性。

---
### [推荐] [2026/456] Libra: Pattern-Scheduling Co-Optimization for Cross-Scheme FHE Code Generation over GPGPU

- **匹配关键字:** homomorphic encryption

- **作者:** Song Bian, Yintai Sun, Zian Zhao, Haowen Pan, Mingzhe Zhang, Zhenyu Guan

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/456) | [PDF](https://eprint.iacr.org/2026/456.pdf)


> **研究背景:** 针对高性能计算架构如GPGPU上跨方案全同态加密(FHE)操作的高效代码生成面临挑战，已知结合多种FHE方案可提升整体效率。
>
> **主要贡献:** Libra框架通过集成FHE运算模式和硬件感知调度策略，实现了算法-硬件协同优化。
>
> **达到效果:** 实验结果显示，Libra在微基准测试中最高实现270倍加速，在应用层面则达到19倍加速，同时提高了计算单元利用率和内存带宽。
>
> **技术梗概:** Libra定义了跨方案FHE的新模式表示法，并基于多方案切换模式动态优化输出的FHE程序；引入了一种计算调度策略，将高层次运算特征与低层次执行计划相连接。

---
### [推荐] [2026/459] Naor-Yung Transform for IND-CCA Probing Security with Lattice Instantiations

- **匹配关键字:** lattice

- **作者:** Katharina Boudgoust, Laurent Imbert, Loïc Masure, Laz Panard

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/459) | [PDF](https://eprint.iacr.org/2026/459.pdf)


> **研究背景:** 本文提出了针对具有侧信道能力的对手的新安全概念，旨在模拟黑盒模型中的攻击者，并将IND-CPA安全的加密方案提升为IND-CCA安全的方案。
>
> **主要贡献:** 作者提出了一种扩展的Naor-Yung变换，用于在具有密钥敏感算法探针访问权限的情况下，从IND-CPA安全性提升到IND-CCA安全性。
>
> **达到效果:** 通过该方法，作者实现了Rutile和Topaz两个安全方案，分别对应于IND-CPA和IND-CCA安全性。
>
> **技术梗概:** 技术上，作者用统一分布替换掉了Kyber中不友好的遮罩部分，并应用了改进的Naor-Yung变换。

---
### [推荐] [2026/462] Semigroup Action Problems and Their Uses in Post-Quantum Cryptography

- **匹配关键字:** post-quantum

- **作者:** Joachim Rosenthal, Silvia Sconza

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/462) | [PDF](https://eprint.iacr.org/2026/462.pdf)


> **研究背景:** 文章回顾了Semigroup Action Problem (SAP) 作为离散对数问题 (DLP) 的关键推广，探讨其从2000年代初代数密码学到后量子密码学标准制定过程中的理论演变。
>
> **主要贡献:** 贡献在于详细阐述了SAP的数学框架及其与经典群论假设的区别，并分析了在这一更广泛背景下Diffie-Hellman和ElGamal协议的一般化形式。
>
> **达到效果:** 结果表明，SAP 在下一代数字签名设计中焕发新生，并为当前NIST竞赛中的候选方案提供了详细的代数分析。
>
> **技术梗概:** 技术上涉及对比群作用与半群作用的数学框架，并探讨了如何在后量子密码学背景下重新审视和利用这些结构。

---
### [推荐] [2026/463] Icefish: Practical zk-SNARKs for Verifiable Genomics

- **匹配关键字:** homomorphic encryption

- **作者:** Alexander Frolov, Maurice Shih, Rob Patro, Ian Miers

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/463) | [PDF](https://eprint.iacr.org/2026/463.pdf)


> **研究背景:** 针对个人基因组数据的敏感性，现有研究较少关注如何验证基因组计算结果的正确性和完整性，尤其是在多方协作的研究和个性化遗传治疗领域。
>
> **主要贡献:** 作者提出了一种基于零知识证明（zk-SNARKs）的方法Icefish，用于验证基因组学中的常见操作，并展示了其在全基因组关联研究和CRISPR有效性验证的应用。
>
> **达到效果:** 该系统能够在较短的时间内（<20分钟的证明时间）验证大规模基因组数据的研究结果，确保了数据集的完整性和研究结论的正确性。
>
> **技术梗概:** 通过构建支持基因组学常见操作的零知识证明模块，并优化zk-SNARKs模型以检测目标和非目标编辑事件，实现了高效的安全验证机制。

---
### [推荐] [2026/465] Advanced cryptography from lattice isomorphism—new constructions of IBE and FHE

- **匹配关键字:** lattice, homomorphic encryption, LWE

- **作者:** Huck Bennett, Zhengnan Lai, Noah Stephens-Davidowitz

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/465) | [PDF](https://eprint.iacr.org/2026/465.pdf)


> **研究背景:** 本文探讨了将基于LWE的高级加密技术应用于最近由Ducas和van Woerden提出的新框架——基于格同构的密码学，旨在构建身份基加密（IBE）与全同态加密（FHE）。
>
> **主要贡献:** 作者展示了如何使用通用且模块化的方法来构造这两种强大的密码原语，并证明了它们在假设Lattice Isomorphism Problem版本困难的情况下是安全的。
>
> **达到效果:** 通过这种方法，作者成功地将Gentry等人引入的构建IBE和Sahai等人用于构建FHE的技术扩展到了新的框架中。
>
> **技术梗概:** 该研究采用了一种通用且模块化的方法，利用任何足够“良好”的格来实现这些加密原语的安全构造。

---
### [推荐] [2026/468] Tighter Proofs for PKE-to-KEM Transformations under Average-Case Decryption Error and without $\gamma$-Spread

- **匹配关键字:** post-quantum

- **作者:** Jinrong Chen, Rongmao  Chen, Yi Wang, Haodong Jiang, Cong Peng, Xinyi Huang, Debiao He, Xiaofeng Chen

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/468) | [PDF](https://eprint.iacr.org/2026/468.pdf)


> **研究背景:** 研究背景：在NIST后量子标准制定过程中，Fujisaki-Okamoto类似（FO-like）变换已成为从公钥加密（PKE）构造IND-CCA安全的密钥封装机制（KEMs）的事实范式。然而，大多数后量子PKE方案存在解密错误问题，这对FO-like PKE-to-KEM变换的安全证明构成了重大挑战，特别是在量子可访问随机预言模型（QROM）中。
>
> **主要贡献:** 主要贡献：本文通过引入两种改进变体FOAC'_0和FOAC'，在随机预言机模型（ROM）和量子随机预言机模型（QROM）下提供了新的安全分析，并显著提高了QROM下的紧致性。
>
> **达到效果:** 达到的效果：与现有方案相比，新方法不仅消除了γ-扩展假设，还将QROM下的紧致性提高到O(q^4)，从而在保持设计者友好性的同时增强了安全性。
>
> **技术梗概:** 技术梗概：通过改进的分析方法和对FOAC变换的优化，本文解决了平均情况解密错误问题，并提高了安全证明的紧致性。

---
### [推荐] [2026/471] Lookup Arguments over Rings and Applications to Batch-Verification of RAM Programs

- **匹配关键字:** lattice, post-quantum

- **作者:** Jonathan Bootle, Julia Guskind, Sikhar Patranabis, Katerina Sotiraki

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/471) | [PDF](https://eprint.iacr.org/2026/471.pdf)


> **研究背景:** 现有的SNARKs中的查找论证主要针对域进行设计，但与基于环的后量子密码学方案不兼容。
>
> **主要贡献:** 本文首次在环上形式化了包含任意环元素的查找论证，并扩展了两种核心多项式IOP（Plookup和LogUp），并结合基于格假设的多项式承诺机制实现了简洁的后量子环查找论证。
>
> **达到效果:** 该工作使得基于环的查找论证成为可能，从而支持更广泛的计算验证场景，特别是批量验证RAM更新。
>
> **技术梗概:** 通过分析现有技术在环上的局限性，并提出改进措施，本文成功地将多项式IOP和多项式承诺机制结合应用于环上。

---
### [推荐] [2026/472] Descent into Broken Trust: Uncovering ML-DSA Subkeys with Scarce Leakage and Local Optimization

- **匹配关键字:** post-quantum

- **作者:** Carsten Schubert, Niklas Julius Müller, Jean-Pierre Seifert, Marian Margraf

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/472) | [PDF](https://eprint.iacr.org/2026/472.pdf)


> **研究背景:** ML-DSA作为NIST后量子签名标准，依赖于拒绝采样确保发布的签名与秘密密钥统计独立。然而，攻击者获得少量生成掩码随机性的信息即可通过线性回归恢复密钥，但需要大量样本限制其实用性。
>
> **主要贡献:** 作者提出了两种贡献：一是构造仅使用收集到的泄漏关系验证候选子密钥的检查程序；二是设计多级梯度上升算法以迭代优化候选者并最小化评分函数。
>
> **达到效果:** 在精确泄漏情况下，该攻击从5000至35000个信息关系中恢复了ML-DSA子密钥，显著降低了攻击成本。
>
> **技术梗概:** 通过将密钥恢复问题重新表述为可由局部优化求解的约束满足问题，并利用验证方法中的理论洞察设计多级梯度上升算法来逐步优化候选者。

---
### [推荐] [2026/473] PIKE: Faster Isogeny-Based Public Key Encryption with Pairing-Assisted Decryption

- **匹配关键字:** post-quantum

- **作者:** Shiping Cai, Mingjie Chen, Yi-Fu Lai, Kaizhan Lin

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/473) | [PDF](https://eprint.iacr.org/2026/473.pdf)


> **研究背景:** PIKE是基于Isogeny的公钥加密方案，改进了POKÉ设计以提高解密速度并选择更小的质数，从而进一步优化整体运行时间。
>
> **主要贡献:** 通过使用配对来直接加速解密过程，并放宽所需的规范形式，PIKE选择了较小的素数，提高了效率。
>
> **达到效果:** 在NIST~I设置下的基准测试显示，与POKÉ相比，PIKE在密钥生成、加密和解密方面分别实现了1.30倍、1.24倍和1.47倍的速度提升，同时保持了具有竞争力的公钥和密文大小。
>
> **技术梗概:** PIKE利用配对来直接获取共享秘密，并通过放宽规范形式的选择来减少所需的素数大小，从而提高整体性能。

---
### [2026/451] Oblivious Single Access Machines are Concretely Efficient

- **作者:** Sage Pia, Ananya Appan, Maryam Rezapour, Amey Shukla, Nikhil Date, Benjamin Fuller, Ling Ren, David Heath

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/451) | [PDF](https://eprint.iacr.org/2026/451.pdf)


> **研究背景:** 研究背景：Oblivious算法允许空间受限的客户端程序安全地将存储外包给不信任的服务器。尽管可以通过ORAM实现任何程序的安全编译，但其在理论上和实际应用中都过于昂贵。
>
> **主要贡献:** 主要贡献：本文通过改进OSAM模型中的指针管理技术，显著降低了基于OSAM的Oblivious算法的实际成本。
>
> **达到效果:** 达到的效果：与通用ORAM相比，在处理大型图数据结构时，使用本文方法编译的图算法性能提高了4倍以上。
>
> **技术梗概:** 技术梗概：通过设计指针友好的Path ORAM变体和新的指针管理算法，简化了OSAM中的指针处理过程。

---
### [2026/453] A Quantum-Safe Private Group System for Signal from Key Re-Randomizable Signatures

- **作者:** Graeme Connell, Sebastian Faller, Felix Günther, Julia Hesse, Vadim Lyubashevsky, Rolfe Schmidt

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/453) | [PDF](https://eprint.iacr.org/2026/453.pdf)


> **研究背景:** 即时通讯服务已成为现代通信的重要组成部分，其隐私性具有广泛的社会意义。尽管主流的即时通讯软件已采用端到端加密保护消息内容不被服务商截获，但群组聊天中的成员列表隐私仍是一个挑战。
>
> **主要贡献:** 本文重新设计了一个量子安全的私密群组系统，该系统在保持与现有系统相同的安全保证的同时，采用了更模块化的设计，并使用了更简单的基础构建块来实现更高的效率。
>
> **达到效果:** 通过这种方法，新方案不仅能够提供与Signal相同的隐私保护功能，还能够在量子计算时代下更加高效地运行。此外，这种设计允许逐步过渡到量子安全的组件。
>
> **技术梗概:** 该研究采用了重新设计整个群组系统的方法，并结合了匿名凭证、可验证加密和不经意伪随机函数等技术，以实现更高效的量子安全实例化。

---
### [2026/454] The principal ideal problem for endomorphism rings of superspecial abelian varieties

- **作者:** Wouter Castryck, Jonathan Komada Eriksen, Riccardo Invernizzi, Frederik Vercauteren

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/454) | [PDF](https://eprint.iacr.org/2026/454.pdf)


> **研究背景:** 研究提出了一个拉斯维加斯算法，用于矩阵环$M_g(O)$中的主要理想问题，其中$g \geq 2$，$O$是复数四元数代数$B_{p, \infty}$在$\infty$和素数$p$处分歧的极大订单。
>
> **主要贡献:** 贡献在于提供了一种预期多项式时间复杂度的方法，并且通过SageMath实现了高效的运行和紧凑的结果输出。
>
> **达到效果:** 结果表明，该算法在实际操作中表现良好，能够有效解决相关问题并产生简洁的结果。
>
> **技术梗概:** 技术上，方法基于寻找具有指定核的超特殊阿贝尔簇自同态，并应用于矩阵环的主要理想问题。

---
### [2026/455] Asynchronous MPC with Abort

- **作者:** Ananya Appan, David Heath, Ling Ren

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/455) | [PDF](https://eprint.iacr.org/2026/455.pdf)


> **研究背景:** 大多数关于异步网络中安全多方计算（MPC）的研究集中在保证输出交付（GOD），这使得所有参与者都能获得函数结果。然而，这样的协议通常只能容忍少于n/3的恶意行为者，并且允许对手排除最多t个诚实参与者的输入。
>
> **主要贡献:** 作者提出了对标准正确性概念的放松，以改进异步MPC协议的安全性和可靠性。他们定义了在部分参与者异步时仍能获得正确输出的新正确性标准。
>
> **达到效果:** 研究结果表明，在某些条件下可以实现选择性中止（selective abort），但要实现全体一致的中止则需要更严格的条件。此外，还提出了一种新的可识别中止概念。
>
> **技术梗概:** 通过定义新正确性和引入可识别中止的概念，作者探索了在异步网络中改进MPC协议的方法和限制。

---
### [2026/457] Adaptively Secure, Universally Composable Distributed Generation of Discrete-Logarithm Based Keys

- **作者:** Hanna Ek, Kelsey Melissaris, Lawrence Roy

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/457) | [PDF](https://eprint.iacr.org/2026/457.pdf)


> **研究背景:** 研究背景：分布式密钥生成（DKG）协议允许多方合作生成一个阈值共享的公私钥对，确保至少有t个参与者才能重构秘密。本文旨在设计一种同时具备适应性安全性与普遍组合性的离散对数基DKG协议，且无需使用擦除、不一致玩家、交互假设或预言机辅助模拟。
>
> **主要贡献:** 主要贡献：提出了一种在诚实多数情况下实现保证输出交付的三轮适应性安全和普遍组合性DKG协议；一种能够容忍全面腐败并在两轮中实现可识别终止的承诺型DKG功能；以及一种在诚实多数情况下实现保证输出交付的三轮适应性安全和普遍组合性承诺型DKG协议。
>
> **达到效果:** 达到的效果：这些贡献使得基于离散对数的阈值签名方案（如Schnorr）能够以更高的安全性与效率实现，包括全面腐败情况下的可识别终止以及诚实多数情况下的保证输出交付。
>
> **技术梗概:** 技术梗概：通过设计新的承诺型DKG功能和协议，在随机预言机模型下基于DDH假设证明了安全性和有效性。

---
### [2026/458] The Art of Linearization: From a KZG’s Trick to a General Commitment Framework

- **作者:** Janno Siim

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/458) | [PDF](https://eprint.iacr.org/2026/458.pdf)


> **研究背景:** 研究背景：在基于KZG多项式承诺的SNARK（简洁非交互式论证系统）中，引入了一种有效的线性化技巧，显著减少了证明者需要发送的KZG多项式承诺开销。
>
> **主要贡献:** 主要贡献：作者重新审视并形式化了这一技术，定义了一个线性化多项式承诺方案(LPCS)，并提出了LinKZG版本的KZG承诺方案，并在目标群假设下实现了弱可提取性。
>
> **达到效果:** 达到的效果：证明了Plonk在相同假设下的安全性，并展示了如何从任何同态多项式承诺方案构建LPCSs，从而扩展了线性化技术的应用范围，提高了其他SNARK系统的效率。
>
> **技术梗概:** 技术梗概：通过形式化和抽象化线性化技巧，作者提出了一个通用的LPCS框架，并展示了其在不同同态多项式承诺方案中的应用可能性。

---
### [2026/460] A Resource-Efficient Hardware Accelerator for Large-Size NTT via Algorithm–Architecture Co-Design

- **作者:** Kaixuan Wang, Yifan Yanggong, Xiaoyu Yang, Chenti Baixiao, Lei Wang

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/460) | [PDF](https://eprint.iacr.org/2026/460.pdf)


> **研究背景:** 现代零知识证明（ZKP）中的大尺寸数量论变换（NTT）是关键操作，但现有设计依赖于分步算法，在实际实现中仍面临效率问题。
>
> **主要贡献:** 提出了RENTT加速器，通过预计算因子管理方案、突发优化转置方法和解耦多银行片上存储层次结构来提高大尺寸NTT的资源效率。
>
> **达到效果:** RENTT在保持高PE利用率的同时，减少了芯片外数据传输延迟，并且配置灵活以支持不同大小的NTT操作。
>
> **技术梗概:** 通过预计算因子管理减少冲突、融合系数重排与元素级蝴蝶变换、设计解耦多银行存储层次结构来优化内存使用。

---
### [2026/461] Compact HQC with new (un)balance

- **作者:** Chaofeng Guan, Lan Luo, Haodong Jiang, Jianhua Hou, Tong Yu, Hong Wang, Kangquan Li, Longjiang Qu

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/461) | [PDF](https://eprint.iacr.org/2026/461.pdf)


> **研究背景:** HQC是一种基于纠错码的公钥加密机制，已在NIST标准中被选为候选方案之一。其性能平衡依赖于解码失败率（DFR）的直接配置和特定错误分布的选择。
>
> **主要贡献:** 作者提出了一种新的、更保守的方法来评估移除这些限制对已知攻击复杂度的影响，并找到了一种新的平衡点，以优化HQC的带宽、效率与安全性。
>
> **达到效果:** 通过这种方法，作者成功地量化了$(\mathbf{r}_1, \mathbf{r}_2, \mathbf{e})$权重分布对ISD攻击成本和DFR的具体影响，并提出了一种严格降低DFR而不牺牲性能的策略。
>
> **技术梗概:** 该研究通过正式化并分析最佳已知解密失败攻击，推导了解密失败事件概率的上界，并量化了$(\mathbf{r}_1, \mathbf{r}_2, \mathbf{e})$权重分布对ISD攻击成本和DFR的具体影响。

---
### [2026/464] Model Extraction of Convolutional Neural Networks with Max-Pooling

- **作者:** Haolin Liu, Adrien Siproudhis, Christina Boura, Thomas Peyrin

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/464) | [PDF](https://eprint.iacr.org/2026/464.pdf)


> **研究背景:** 研究背景：针对卷积神经网络（CNN）的模型提取攻击旨在通过黑盒查询恢复其内部参数，但现有技术主要集中在全连接ReLU网络上，对于包含卷积和最大池化层的结构化网络了解较少。
>
> **主要贡献:** 主要贡献在于提出了适用于结合ReLU激活函数和最大池化层的CNN模型提取方法，并重新定义了最大池化操作在软标签设置中的作用。
>
> **达到效果:** 达到的效果是成功地通过黑盒查询重构出卷积核，证明了最大池化关键点能够捕捉两个卷积神经元之间的差异，并且通过接收域分析优化了噪声过滤和关键点定位过程。
>
> **技术梗概:** 技术梗概：利用ReLU非线性操作与最大池化的自然扩展关系，结合卷积局部结构特性设计提取方法；通过接收域分析减少计算成本并提高准确性。

---
### [2026/466] Hashing in Generic Groups: Completing the AGM-to-GGM Transfer

- **作者:** Taiyu Wang, Cong Zhang, Hong-Sheng Zhou, Xin Wang, Keyu Ji, Zhihong Jia, Li Lin, Changzheng Wei, Ying Yan, Kui Ren, Chun Chen

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/466) | [PDF](https://eprint.iacr.org/2026/466.pdf)


> **研究背景:** 研究背景：针对代数群模型（AGM）与通用群模型（GGM）之间的关系，以及在随机预言机模型（ROM）下验证这些模型间转换的必要性进行了深入探讨。
>
> **主要贡献:** 主要贡献在于识别了一个特定的安全证明实例，并展示了Jaeger和Mohan框架无法涵盖所有已知AGM安全证明；同时提出了一个增强后的框架来弥补这一不足。
>
> **达到效果:** 达到的效果是提供了一种更全面的方法，使得更多基于AGM的安全性证明能够被准确地转换到GGM中，从而填补了现有理论研究中的空白。
>
> **技术梗概:** 技术梗概包括对特定加密方案的分析，以及通过构建黑盒分离来展示框架局限性的方法。

---
### [2026/467] A Note on the Equivalence Between Zero-knowledge and Quantum CSS Codes

- **作者:** Noga Ron-Zewi, Mor Weiss

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/467) | [PDF](https://eprint.iacr.org/2026/467.pdf)


> **研究背景:** 零知识码和量子CSS码分别在纠错编码和量子纠错领域有广泛应用，但它们之间的关系尚未明确。
>
> **主要贡献:** 本文首次证明了线性完美零知识码与量子CSS码的等价性，并利用此等价性构造了显式渐进良好且可局部检验的零知识码。
>
> **达到效果:** 通过这一理论上的突破，研究者们能够更有效地设计和实现具有特定属性的纠错码，从而推动相关领域的进一步发展。
>
> **技术梗概:** 作者采用代数编码理论中的方法来证明等价性，并结合量子信息论的技术构建所需的新码。

---
### [2026/469] A Note on ``Linear-Communication ACSS with Guaranteed Termination and Lower Amortized Bound''

- **作者:** Xiaoyu Ji, Junru Li, Yifan Song

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/469) | [PDF](https://eprint.iacr.org/2026/469.pdf)


> **研究背景:** 本文针对Qin等人在Eurocrypt 2026上发表的工作中提出的异步完全秘密共享（ACSS）协议的安全性进行了研究，指出其存在活锁问题并提出了攻击方法。
>
> **主要贡献:** 作者通过分析发现该协议的实现细节存在问题，并提出具体的攻击实例以证明其不具有预期的安全性和可靠性。
>
> **达到效果:** 研究表明，Qin等人提出的ACSS协议无法保证协议的正常终止，并且在某些情况下会导致协议失败。
>
> **技术梗概:** 研究采用了形式化的方法来验证协议的行为，并通过构造特定的消息序列揭示了协议中的漏洞。

---
### [2026/474] Scalable Compliant Privacy on Starknet

- **作者:** Lior Goldberg, Maya Dotan, Ittay Dror, Gideon Kaempfer, Nir Levi, Noa Oved, Arad Reder, Anat Veredgorn, Noa Wolfgor

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/474) | [PDF](https://eprint.iacr.org/2026/474.pdf)


> **研究背景:** 该研究旨在设计一种在Starknet区块链上实现可扩展且合规的隐私保护协议，以支持符合监管要求的同时保障用户交易信息的匿名性。
>
> **主要贡献:** 贡献包括开发了一种高效的笔记发现机制、一个实用的合规框架以及与现有Starknet DeFi合约的匿名集成方法。
>
> **达到效果:** 该协议能够在不泄露发送者、接收者和金额的情况下进行安全转账，并通过零知识证明确保交易的有效性，同时允许审计实体在合法监管请求下选择性地解密交易。
>
> **技术梗概:** 技术上采用了Cairo语言编写的证明逻辑和智能合约代码，结合Starknet的原生账户抽象功能来授权交易，并使用了高效的笔记发现机制以支持多种代币类型在同一池中流通。

---
### [2026/475] Scaling Fully Secure MPC via Robust Recursive Search and Gap Amplification

- **作者:** Matan Hamilis, Ariel Nof

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/475) | [PDF](https://eprint.iacr.org/2026/475.pdf)


> **研究背景:** 本文提出了一种新的框架，旨在通过稳健的递归搜索和间隙放大技术提升半诚实协议的安全性至完全恶意安全，在具有三分之二诚实多数的情况下安全计算算术电路。
>
> **主要贡献:** 该框架能够同时实现相对于电路大小的对数通信开销、与电路大小无关的额外轮次数量以及每个参与者的线性计算工作量，这是在静态对手限制下首次同时达到这三项指标。
>
> **达到效果:** 通过这种方法，实现了完全恶意安全下的高效多方计算，使得成本低于以往任何方法。
>
> **技术梗概:** 该技术基于一种新的验证机制——稳健的递归搜索，用于识别并移除计算中的作弊者。

---
### [2026/477] DAC-PRE: Practical Anonymous Data Access Scheme Control with Proxy Re-encryption for Implantable Medical Devices

- **作者:** Jayaprakash Kar, Xiaoguang Liu, Fagen Li

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/477) | [PDF](https://eprint.iacr.org/2026/477.pdf)


> **研究背景:** 针对植入式医疗设备的数据访问控制，研究如何在确保匿名性的前提下实现高效的数据访问管理。
>
> **主要贡献:** 提出了一种基于代理重加密的签密方法(DAC-PRE)，实现了对植入式医疗设备中数据的授权与认证。
>
> **达到效果:** 该协议能够在保证用户匿名性的同时，提供安全的数据访问控制，并且实验分析表明其具有较低的计算成本。
>
> **技术梗概:** 通过结合签密和代理重加密技术，实现数据的高效、匿名访问控制。

---

## 更新: 2026-02-28 12:30

*新增 41 篇论文 (编号 95--394)*

### [推荐] [2026/249] Have Your CKAKE and Eat it, Too: Efficient, Composable KEM-Authenticated Key Exchange

- **匹配关键字:** post-quantum

- **作者:** Myrto Arapinis, Christopher Battarbee, Mina Doosti

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/249) | [PDF](https://eprint.iacr.org/2026/249.pdf)


> **研究背景:** 在后量子时代，KEM（密钥封装机制）相比签名标准在带宽节省方面具有明显优势。然而，先前的基于KEM的身份认证密钥交换协议不具备可组合性。
>
> **主要贡献:** 本文提出了一种新的身份认证密钥交换协议，该协议不仅提供了与非可组合KEM基身份认证密钥交换协议相当的安全保证，还具备可组合性，并且在带宽使用上更为高效。
>
> **达到效果:** 通过构造性密码学框架（CC），证明了该协议的可组合性和前向安全性，同时引入了一种通用方法来证明CC中的前向安全性。
>
> **技术梗概:** 该协议采用了模块化设计，并结合了构造性密码学框架进行安全分析，确保了其在理论和实践上的双重优势。

---
### [推荐] [2026/272] On the Complexity of Interactive Arguments

- **匹配关键字:** lattice

- **作者:** Idan Baril, Iftach Haitner

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/272) | [PDF](https://eprint.iacr.org/2026/272.pdf)


> **研究背景:** 研究旨在探讨构建NP的简洁论证所需最小的安全假设，并关注证明者总通信量小于证人大小的简洁论证及弱零知识形式，如证人不可区分性。
>
> **主要贡献:** 贡献在于证明了在完全黑盒归约下，交互式论证不蕴含单向函数（OWFs），并提出了假设依赖的完全黑盒归约方法。
>
> **达到效果:** 结果表明，存在这样的归约意味着从单向函数到假设G的黑盒归约，超越了G所暗示的内容，简洁证人不可区分性的交互式论证与OWFs之间没有直接蕴含关系。
>
> **技术梗概:** 技术上，通过定义假设依赖的完全黑盒归约(f, R)来分析，并证明其存在性意味着从单向函数到假设G的黑盒归约可能性。

---
### [推荐] [2026/294] Post-Quantum Adaptor Signatures with Strong Security from Cryptographic Group Actions

- **匹配关键字:** post-quantum

- **作者:** Ryann Cartor, Nathan Daly, Giulia Gaggero, Jason T. LeGrow, Andrea Sanguineti, Silvia Sconza

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/294) | [PDF](https://eprint.iacr.org/2026/294.pdf)


> **研究背景:** 本文提出了一种新型高效的适应性签名方案One Round 'Cheating' Adaptor Signatures（OR-CAS），基于CSI-FiSh构建，旨在改进现有的基于群作用的适应性签名方案。
>
> **主要贡献:** 该研究的主要贡献在于设计了一种无需昂贵的非交互式零知识证明且不需修改基础数字签名方案的新颖构造方法。
>
> **达到效果:** 通过这种构造方法，OR-CAS实现了在保持安全性的同时提高效率的目标，并满足了强安全性的要求。
>
> **技术梗概:** 该技术利用CSI-FiSh作为基础构建块，结合群作用机制来实现适应性签名的高效与安全性。

---
### [推荐] [2026/318] Distributed Monotone-Policy Encryption for DNFs from Lattices

- **匹配关键字:** lattice

- **作者:** Jeffrey Champion, David J. Wu

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/318) | [PDF](https://eprint.iacr.org/2026/318.pdf)


> **研究背景:** 分布式单调策略加密通过在不可信环境中增强公钥加密，提供了细粒度的解密能力。该方案允许用户独立生成公私钥对并发布其公钥至公共目录，从而实现基于访问策略的消息加密与解密功能。
>
> **主要贡献:** 本文展示了如何构建适用于布尔公式（DNF公式）的分布式单调策略加密方案，并支持无限数量的用户。此方案的安全性依赖于分解的学习错误假设（LWE），并在随机预言模型下进行验证。
>
> **达到效果:** 该方案实现了透明设置，且密文大小为$\mathsf{poly}(\lambda, \log N)$，其中$N$表示DNF公式中的变量数量。这显著提高了系统的效率和实用性。
>
> **技术梗概:** 通过利用分解的学习错误假设（LWE），本文提出了一个基于随机预言模型的分布式单调策略加密方案，有效解决了信任问题并优化了密文大小。

---
### [推荐] [2026/366] Careful with the Ring: Enhanced Hybrid Decoding Attacks against Module/Ring-LWE

- **匹配关键字:** lattice, homomorphic encryption

- **作者:** Jianhua Hou, Haodong Jiang

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/366) | [PDF](https://eprint.iacr.org/2026/366.pdf)


> **研究背景:** 针对基于格的密码方案，现有研究通常忽略其代数结构带来的加速攻击机会。本文通过利用多项式环结构提出了一种增强型混合解码攻击方法。
>
> **主要贡献:** 作者首次结合环结构提出了针对Module/Ring-LWE问题的增强型混合解码攻击，并证明了在稀疏秘密设置下，新攻击相比先前方法能将复杂度降低一个数量级。
>
> **达到效果:** 实验结果表明，该方法在已知被破坏实例上比现有最佳方法快17至114倍。此外，作者还使用此新混合攻击估计了最新用于全同态加密方案的稀疏Ring-LWE参数集的实际安全性。
>
> **技术梗概:** 通过结合猜测和解码步骤，并利用多项式环结构的特点，该研究提出了一种新的加速攻击技术。

---
### [推荐] [2026/367] High-Precision Functional Bootstrapping for CKKS from Fourier Extension

- **匹配关键字:** homomorphic encryption

- **作者:** Song Bian, Yunhao Fu, Ruiyu Shen, Haowen Pan, Anyu Wang, Zhenyu Guan

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/367) | [PDF](https://eprint.iacr.org/2026/367.pdf)


> **研究背景:** 该研究旨在改进CKKS同态加密方案中的功能自举过程，通过Fourier扩展技术提高密文上函数计算的精度和效率。
>
> **主要贡献:** 作者提出了一种新的Fourier扩展方法，使得任何在$C^{\kappa}$光滑类中定义于有界域上的函数可以被四次多项式级数逼近，并且误差可达到$O(n^{-\kappa-2})$的高精度。
>
> **达到效果:** 通过将该自举框架集成到OpenFHE平台，研究实现了密文计算精度提升10-27位，并将平均自举延迟降低了1.1-2倍。
>
> **技术梗概:** 作者采用了一种新的Fourier扩展构造方法，使得扩展后的函数在Fourier近似意义上尽可能平滑，从而提高了整体的计算效率和准确性。

---
### [推荐] [2026/372] Distributed Monotone-Policy Encryption with Silent Setup from Lattices

- **匹配关键字:** lattice, post-quantum

- **作者:** Abtin Afshar, Rishab Goyal, Saikumar Yadugiri

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/372) | [PDF](https://eprint.iacr.org/2026/372.pdf)


> **研究背景:** 现有的分布式政策加密方案通常需要可信经销商或复杂的交互式设置协议，这限制了其在构建无信任系统中的应用。
>
> **主要贡献:** 本文提出了首个基于格的分布式单调策略加密方案，并实现了无声设置，无需交互即可生成联合公钥。
>
> **达到效果:** 该方案支持任意表示为析取范式的单调政策，并提供了后量子时代去中心化访问控制的安全基础。
>
> **技术梗概:** 通过利用格上的先进技术，如环签名和身份基密码系统，实现了一个安全且高效的无声设置过程。

---
### [推荐] [2026/378] Information-Theoretic Network-Agnostic MPC with Polynomial Communication

- **匹配关键字:** homomorphic encryption

- **作者:** Xiaoyu Ji, Chen-Da Liu-Zhang, Daniel Pöllmann, Yifan Song

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/378) | [PDF](https://eprint.iacr.org/2026/378.pdf)


> **研究背景:** 网络无感知的多方计算(MPC)协议在同步和异步网络中分别能容忍更高的同时故障数量，提供强健的安全性。然而，在最优抗毁性条件下，现有的多项式时间信息论解决方案缺失，而现有计算方案通信复杂度较高。
>
> **主要贡献:** 本文提出了首个具有二次通信复杂度的多项式门级信息论协议和首个基于签名和对称密钥加密的一次性通信复杂度的计算协议。
>
> **达到效果:** 这些贡献显著降低了MPC中的通信开销，使其在实际应用中更加可行。
>
> **技术梗概:** 通过引入新的信息论方法和改进的计算技术，实现了上述通信效率的提升。

---
### [推荐] [2026/379] Pairing-based Functional Commitments for Circuits with Shorter Parameters

- **匹配关键字:** lattice

- **作者:** David Balbás, Dario Fiore, Russell W. F. Lai

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/379) | [PDF](https://eprint.iacr.org/2026/379.pdf)


> **研究背景:** 研究背景：功能承诺（FCs）允许证明者对消息进行承诺，并在稍后提供其在任何给定可接受函数下的像的简洁证明。现有的基于配对的FC方案存在公共参数大小过大的问题，这限制了它们的实际应用。
>
> **主要贡献:** 主要贡献：提出了一种新的基于配对的FC方案，实现了对于宽度为w、深度为d的电路，其公共参数大小为O(λw^3)，同时保持了BCFL的所有良好属性。
>
> **达到效果:** 达到的效果：该方案在公共参数大小和证明大小方面取得了显著改进，特别适用于宽度有限但深度可变的电路场景。
>
> **技术梗概:** 技术梗概：核心在于一种针对二次函数的新链式FC方法，承诺基于幂基计算，并介绍了不同承诺基之间的切换技术。

---
### [推荐] [2026/380] Lattice HD Wallets: Post-Quantum BIP32 Hierarchical Deterministic Wallets from Lattice Assumptions

- **匹配关键字:** lattice, post-quantum

- **作者:** Conor Deegan, James Fitzwater, Kamil Doruk Gur, David Nugent

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/380) | [PDF](https://eprint.iacr.org/2026/380.pdf)


> **研究背景:** 现有的HD钱包依赖于椭圆曲线的代数结构，但在后量子时代，如何在不牺牲功能的前提下实现类似BIP32的非硬化派生仍然是一个挑战。
>
> **主要贡献:** 本文提出了两种后量子HD钱包构造：一种基于ML-DSA支持私钥相关的非硬化派生；另一种主要贡献是使用修改后的Raccoon-G签名方案，通过发布完整的高斯分布公钥实现非硬化公钥派生。
>
> **达到效果:** 这两种构造均证明了不可链接性和不可伪造性，并且在Rust中实现了。这是首次能够在后量子环境中恢复BIP32完整公共密钥衍生功能的HD钱包构建。
>
> **技术梗概:** 通过修改Raccoon-G方案发布完整的高斯分布公钥，保持线性特性；利用Gaussians的性质确保派生密钥与新生成的密钥统计上接近。

---
### [推荐] [2026/382] Multi-key Security in the Quantum World: Revisiting Tweakable Even-Mansour and FX

- **匹配关键字:** post-quantum

- **作者:** Rentaro Shiba, Tetsu Iwata

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/382) | [PDF](https://eprint.iacr.org/2026/382.pdf)


> **研究背景:** 本文研究了量子环境下对称密钥构造的安全性，特别是在Q1MK模型下的多密钥环境。
>
> **主要贡献:** 作者证明了在该模型下，可调Even-Mansour密码（TEM）和FX构造的安全性。
>
> **达到效果:** 对于TEM，在Q1MK模型下，破解需要至少$\Omega(2^{\kappa/3})$的经典与量子查询；对于FX，在Q1MK模型下使用$(\kappa + n)$位密钥时，破解需要至少$\Omega(2^{(\kappa + n - u)/3})$的经典与量子查询。
>
> **技术梗概:** 安全证明基于Alagic等人在EUROCRYPT 2022中引入的混合论证技术，并对FX构造的安全性进行了重新分析和加强。

---
### [推荐] [2026/390] Succinct Arguments for BatchQMA and Friends under 6 Rounds

- **匹配关键字:** post-quantum

- **作者:** Rishab Goyal, Aditya Jain, Shashwatha Mitra GB

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/390) | [PDF](https://eprint.iacr.org/2026/390.pdf)


> **研究背景:** 研究旨在降低量子计算简洁经典论证系统中交互轮次的数量，同时保持或提高安全性。
>
> **主要贡献:** 贡献在于设计了两种新的量子计算简洁论证系统：一种是4轮公共硬币（除第一消息外）的batchQMA语言论证系统；另一种是6轮私有硬币的单调策略batchQMA语言论证系统。
>
> **达到效果:** 结果表明，这些新系统在某些假设下实现了最优通信复杂度，且不依赖于批量大小或电路规模。
>
> **技术梗概:** 技术上，主要创新在于提出了一种新的证明诚实性方法，无需重放作弊证明者，并引入了量子计算论证系统的直线部分可提取性概念。

---
### [2026/95] Tropical cryptography IV: Digital signatures and secret sharing with arbitrary access structure

- **作者:** Dima Grigoriev, Chris Monico, Vladimir Shpilrain

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/095) | [PDF](https://eprint.iacr.org/2026/095.pdf)


> **研究背景:** 本文基于热带代数构建了高效的数字签名协议和具有任意访问结构的密钥共享方案，旨在通过解决特定问题的计算难度来确保安全性。
>
> **主要贡献:** 作者提出了利用热带矩阵分解难题作为安全基础的新颖加密技术，为数字签名和秘密分享提供了新的实现途径。
>
> **达到效果:** 该研究成功地将复杂计算问题应用于实际的安全协议中，并验证了其在效率和安全性上的优势。
>
> **技术梗概:** 通过定义特定的热带矩阵乘法运算及其分解难题，作者设计了一套基于此难题的加密机制。

---
### [2026/151] Non-Complete Set Coverings for Higher Order Threshold Implementations

- **作者:** Oriol Farràs, Óscar Fidalgo, Carlos Andres Lara-Nino

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/151) | [PDF](https://eprint.iacr.org/2026/151.pdf)


> **研究背景:** 针对侧信道攻击（SCAs）对密码算法实现构成的重要威胁，阈值实现（TIs）通过使用随机化共享的输入和中间值来保护算法，依赖于能够提供所需保护级数依赖结构的非完备集合覆盖（NCSCs）。
>
> **主要贡献:** 本文通过找到更小的NCSC并证明其基数的新理论界限，为高效阈值实现的研究做出了贡献。
>
> **达到效果:** 研究提出了适用于$t=3,d=2$的最优NCSC，并且对于$t=3,d=3$和$t=4,d=2$的情况也提供了接近下界大小的NCSCs。
>
> **技术梗概:** 通过引入新的组合性质并开发用于搜索小基数NCSC的新算法，实现了上述贡献。

---
### [2026/260] Investigating the Wedge Map on SNOVA

- **作者:** Po-En Tseng, Lih-Chung Wang, Peigen Li, Yen-Liang Kuan

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/260) | [PDF](https://eprint.iacr.org/2026/260.pdf)


> **研究背景:** 本文研究了NIST PQC Round 2候选方案SNOVA的代数结构，特别是楔形映射的核心维度。
>
> **主要贡献:** 通过提升技术将公钥从矩阵环$\mathbb{F}_q^{l \times l}$转换到扩展域$\mathbb{F}_{q^l}$的等效表示，并推导出一个生成函数明确地表征了楔形映射的核心维度。
>
> **达到效果:** 这项代数分析为SNOVA的空间几何提供了严格的理解，验证了特定参数集的安全性，并为进一步确保结构安全性提供依据。
>
> **技术梗概:** 采用提升技术将公钥从矩阵环转换到扩展域的等效表示，并通过生成函数明确表征楔形映射的核心维度。

---
### [2026/276] On the conversion of module representations for higher dimensional supersingular isogenies

- **作者:** Aurel Page, Damien Robert, Julien Soumier

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/276) | [PDF](https://eprint.iacr.org/2026/276.pdf)


> **研究背景:** 本文扩展了 quaternionic 理想与超奇异椭圆曲线之间的成熟工具箱，引入更高维度的版本，即 Hermite 模和极大超奇异主极化 abel 品体。
>
> **主要贡献:** 主要贡献在于提出了一种高效算法，用于根据模表示计算非极化同构 $A \simeq E_0^g$。
>
> **达到效果:** 该算法通过解决矩阵环上 quaternion 计划的理想主问题，并结合更高维度的 Clapotis 算法的推广实现。
>
> **技术梗概:** 技术梗概包括利用模表示计算同构和解决 Principal Ideal Problem 的子程序，以及对 KLPT$^2$ 算法输出度进行降低的技术。

---
### [2026/287] Network-Agnostic Multidimensional Approximate Agreement with Optimal Resilience

- **作者:** Diana Ghinea, Darya Melnyk, Tijana Milentijević

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/287) | [PDF](https://eprint.iacr.org/2026/287.pdf)


> **研究背景:** 研究背景：在网络未知的环境下，即同步或异步网络可能交替出现的情况下，多维近似一致问题(D-AA)的研究存在不确定性。
>
> **主要贡献:** 主要贡献在于证明了对于D>1的情况，先前确定性协议中的条件是紧致的，并识别出先前协议中差距的原因并非几何上的，而是由于通信原语产生的‘视图’不对称性。
>
> **达到效果:** 达到的效果是在网络-无关模型下，为多维近似一致问题(D-AA)提供了更严格的确定性协议边界条件，特别是在D>1的情况下。
>
> **技术梗概:** 技术梗概：通过强化网络-无关的Gather原语，并确保参与方值的数量具有全局结构性质来解决先前协议中的不对称性问题。

---
### [2026/320] Statistically Secure Asynchronous MPC with Linear Communication and $\mathcal{O}(n^5)$ Additive Overhead

- **作者:** Xiaoyu Ji, Yifan Song

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/320) | [PDF](https://eprint.iacr.org/2026/320.pdf)


> **研究背景:** 研究背景：安全多方计算（MPC）允许不信任的各方在保持输入隐私的情况下共同评估一个公共函数。现有最优弹性（$t < n/3$）的信息论异步MPC方案通信复杂度较高，与同步设置相比存在显著差距。
>
> **主要贡献:** 主要贡献：首次提出一种统计安全的异步MPC协议，实现了每门电路线性通信量且附加开销为$\mathcal{O}(n^{5})$，同时假设了共同集合一致性（ACS）功能。
>
> **达到效果:** 达到的效果：在最差情况下，该协议的附加开销为$\mathcal{O}((\kappa+n)n^4\log\kappa)$，甚至超越了最优同步结果当$n \geq \sqrt{\kappa\log\kappa}$时。
>
> **技术梗概:** 技术梗概：通过新方法生成Beaver三元组实现了每组线性通信量和$\mathcal{O}(n^{5})$附加开销。

---
### [2026/336] How to Build a Short-Input Random Oracle from Public Random Permutations

- **作者:** Ritam Bhaumik, Nilanjan Datta, Avijit Dutta, Ashwin Jha, Sougata Mandal, Bart Mennink, Hrithik Nandi, Yaobin Shen

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/336) | [PDF](https://eprint.iacr.org/2026/336.pdf)


> **研究背景:** 研究背景：现有大量工作探讨如何从伪随机置换（PRP）构建伪随机函数（PRF），并期望其在无密钥设置下也具有安全性，如用于承诺安全或替代短输入随机预言机。然而，近期发现几乎所有此类证明存在缺陷。
>
> **主要贡献:** 主要贡献在于分类所有双调用短输入/输出RP到RF构造，并引入“链接攻击”这一强大且广泛适用的区分性攻击。同时展示了仅Sum Of Permutations和Encrypted Davies-Meyer Dual在独立置换实例化下可实现超越生日边界的安全性。
>
> **达到效果:** 达到的效果包括重新评估现有证明的有效性，揭示其局限性，并提出潜在有效的构造方案，为构建并行化的短输入随机预言机提供了新的视角。
>
> **技术梗概:** 技术梗概：通过深入分析和分类所有双调用RP到RF构造，引入了“链接攻击”来评估它们的区分性。同时证明了某些构造在独立置换实例化下可实现超越生日边界的安全性。

---
### [2026/339] $\mathsf{Spectra}$: Interval-Agnostic Vector Range Argument for Unstructured Range Assertions

- **作者:** Hao Gao, Qianhong Wu, Bo Qin, Fudong Wu, Zhenyang Ding, Zhiguo Wan

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/339) | [PDF](https://eprint.iacr.org/2026/339.pdf)


> **研究背景:** 现有协议能够证明向量$\mathbf{v}$位于结构化的范围中，但无法处理更复杂的非成员资格声明等未结构化范围断言。
>
> **主要贡献:** $\mathsf{Spectra}$提出了$\mathsf{RangeLift}$编译器和基于$\mathsf{KZG}$矢量承诺方案的实现方法，支持任意区间组合的向量范围证明。
>
> **达到效果:** 该协议实现了简洁的通信量和验证者时间复杂度，并且其证明者的计算成本与单个区间的情况相当，即使每个$\mathsf{R}_i$包含多个区间。
>
> **技术梗概:** 通过引入$\mathsf{RangeLift}$编译器将结构化向量范围论证提升至支持未结构化范围断言，并基于$\mathsf{KZG}$矢量承诺方案设计了具体实现。

---
### [2026/358] Round-Based Approximation of (Higher-Order) Differential-Linear Correlation

- **作者:** Kai Hu, Zhongfeng Niu, Meiqin Wang

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/358) | [PDF](https://eprint.iacr.org/2026/358.pdf)


> **研究背景:** 该研究旨在通过几何方法精确估算差分-线性区分器的相关性，特别针对具有大非线性函数的密码算法。
>
> **主要贡献:** 作者提出了一种基于轮次的方法来近似差分-线性相关性，并首次为某些加密算法提供了更高阶的差分-线性区分器。
>
> **达到效果:** 这种方法显著提高了对\ascon等算法中差分-线性相关性的估计精度，同时发现了更长轮次的差分-线性区分器。
>
> **技术梗概:** 通过分析相关矩阵和2-wise形式来推导相关传播定理，并利用这些理论进行近似计算。

---
### [2026/368] Additions, Multiplications, and the Interaction In-Between: Optimizing MPC Protocols via Leveled Linear Secret Sharing

- **作者:** Andreas Brüggemann, Thomas Schneider, Maximilian Stillger

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/368) | [PDF](https://eprint.iacr.org/2026/368.pdf)


> **研究背景:** 在基于秘密共享的高效安全多方计算(MPC)协议中，局部乘法通常会产生一种中间表示形式，这种形式可以立即且互动地转换回产品共享。然而，这种中间表示形式往往被视为仅作为必要过渡步骤，其潜在价值尚未被充分利用。
>
> **主要贡献:** 作者提出了层次化线性秘密共享的范式，允许在原始秘密共享和先前仅为中间形式之间动态切换，并在此过程中实现了任意线性计算。
>
> **达到效果:** 这种方法使得可以在任何域中执行乘法运算，并且仅需在下一次乘法之前进行交互升级，从而提高了三方复制计算等场景下的性能。
>
> **技术梗概:** 非互动的乘法操作用于从一种秘密共享切换到另一种，而互动的升级过程则在必要时放置于后续乘法之前。

---
### [2026/369] Issuer-Hiding for BBS Anonymous Credentials via Randomizable Keys

- **作者:** Andrea Flamini, Karla Friedrichs, Anja Lehmann

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/369) | [PDF](https://eprint.iacr.org/2026/369.pdf)


> **研究背景:** 传统的匿名凭证（AC）虽然能够证明持证人的属性，但每次展示都会泄露发行者信息，这可能超出必要的披露范围。为了克服这一问题，研究提出了发行人隐藏的匿名凭证（IHAC），旨在保护用户隐私，仅揭示其持有来自某个信任集内发行者的凭证。
>
> **主要贡献:** 作者提出了一种基于BBS签名的发行人隐藏匿名凭证方案，并通过随机化BBS公钥和相应调整签名的方法实现了紧凑的展示信息，无需依赖验证者特定的秘密密钥对。
>
> **达到效果:** 该方案能够在保持展示信息紧凑的同时实现发行人的匿名性，提高了隐私保护水平并简化了密钥管理流程。
>
> **技术梗概:** 通过随机化BBS公钥和相应调整签名的方法来实现发行人隐藏功能，并认为这一技术具有独立的研究价值。

---
### [2026/370] Round-Optimal Byzantine Agreement without Trusted Setup

- **作者:** Diana Ghinea, Ivana Klasovitá, Chen-Da Liu-Zhang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/370) | [PDF](https://eprint.iacr.org/2026/370.pdf)


> **研究背景:** Byzantine Agreement（拜占庭共识）是密码学和分布式计算中的基本原语，降低其轮次复杂度至关重要。
>
> **主要贡献:** 该研究提出了首个无需信任设置的最优轮次拜占庭协议，分别为$t<\frac{3}{2}n$时提供统计安全性，并在$t<(1-\epsilon)n^2$时提供任意常数$\epsilon>0$的安全性假设Bulletin-board公钥基础设施。
>
> **达到效果:** 这些协议达到了与Karlin和Yao及Chor等人的下界匹配的轮次复杂度，显著减少了信任设置的需求。
>
> **技术梗概:** 研究采用了新颖的技术来实现无信任设置下的最优轮次拜占庭共识，包括基于Bulletin-board公钥基础设施的设计方法。

---
### [2026/371] A Modular Approach to Succinct Arguments for QMA

- **作者:** James Bartusek, Jiahui Liu, Giulio Malavolta

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/371) | [PDF](https://eprint.iacr.org/2026/371.pdf)


> **研究背景:** 本文探讨了量子计算背景下如何构建高效验证的量子证明系统，这是现代密码学中的核心问题。
>
> **主要贡献:** 作者提出了一种新的框架，仅基于无结构假设（如盲态准备协议和坍缩哈希函数）即可实现经典可验证的QMA简洁论证系统。
>
> **达到效果:** 该研究首次在无需依赖学习误差难题的前提下实现了量子证明系统的简洁性与高效性。
>
> **技术梗概:** 作者通过两步方法，首先设计基于盲态准备协议的经典验证QMA论证系统，然后引入通用通信压缩编译器以进一步优化系统。

---
### [2026/373] Partially Non-Interactive Two-Round Threshold and Multi-Signatures with Tighter and Adaptive Security

- **作者:** Yanbo Chen

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/373) | [PDF](https://eprint.iacr.org/2026/373.pdf)


> **研究背景:** 在无需对称加密的离散对数设置中，已有多轮次部分非交互式阈值和多重签名方案的研究。然而，这些方案的安全性属性与完全在线方案之间存在差距。
>
> **主要贡献:** 作者提出了一种新的构造方法，填补了这一空白，首次提供了具有标准假设下无回溯归约的两轮次部分非交互式多重签名方案，并实现了对非代数对手的完全适应安全性。
>
> **达到效果:** 该方案在对抗非代数对手时提供了更紧的安全保证，优于所有先前的部分非交互式方案。
>
> **技术梗概:** 通过将HBMS及其变体部分转换为非交互式方式来实现上述目标。

---
### [2026/375] Liquid Democracy With Two Opposing Factions

- **作者:** Krishnendu Chatterjee, Seth Gilbert, Stefan Schmid, Jakub Svoboda, Michelle Yeo

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/375) | [PDF](https://eprint.iacr.org/2026/375.pdf)


> **研究背景:** 研究背景：本文探讨了在没有明确正确答案且存在不确定性的情况下，liquid democracy机制如何运作。
>
> **主要贡献:** 主要贡献：提出了一个实用的分布式算法来决定投票代理策略，并提供了在完全了解对立阵营信息情况下的最优投票代理策略分析。
>
> **达到效果:** 达到的效果：该研究揭示了在不确定性和对抗性环境下，liquid democracy的有效性及局限性，并为实际应用提供理论指导。
>
> **技术梗概:** 技术梗概：通过假设n个选民进行二元议题投票，基于相同偏好的选民形成阵营，并设计了一个涉及最少互动和通信的分布式算法来决定近似最优的投票代理策略。

---
### [2026/376] Is PSI Really Faster Than PSU? Achieving Efficient PSU with Invertible Bloom Filters

- **作者:** Lucas Piske, Ni Trieu

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/376) | [PDF](https://eprint.iacr.org/2026/376.pdf)


> **研究背景:** 私有集合并集（PSU）协议允许双方计算其私有集合的并集，而不泄露任何超出并集之外的信息。现有的PSU协议通常比私有集合交集（PSI）慢得多，速度差距可达30倍左右。
>
> **主要贡献:** 本文提出了首个基于可逆布隆查找表（IBLTs）的PSU协议，引入了不同于传统方法的新框架，并通过直接从原始IBLT中恢复并集元素来高效计算并集。
>
> **达到效果:** 该协议在局域网设置下，对于集合大小从$2^{14}$到$2^{20}$范围内的数据，在运行时间上与最先进的PSI相当，同时在局域网和广域网场景中分别比之前的工作快了10倍以上，并且保持线性计算和通信复杂度。
>
> **技术梗概:** 该技术利用了每个参与者IBLT及其并集之间的结构不变量，仅通过Oblivious Transfer（OT）和Oblivious Pseudorandom Function（OPRF）进行等式检查来安全实现此功能，确保泄露的信息仅限于并集。

---
### [2026/377] Perfectly Secure Network-Agnostic MPC Comes for Free

- **作者:** Xiaoyu Ji, Chen-Da Liu-Zhang, Yifan Song

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/377) | [PDF](https://eprint.iacr.org/2026/377.pdf)


> **研究背景:** 研究背景：经典的多方计算（MPC）协议假设网络是同步或异步的，但各自存在局限性。网络无感知模型旨在结合两者优势，确保在未知网络类型情况下仍能提供完美安全性。
>
> **主要贡献:** 主要贡献：首次提出了在网络无感知设置下，在最优阈值条件下具有多项式通信和计算复杂度的完美安全MPC协议。
>
> **达到效果:** 达到的效果：该协议实现了期望通信复杂度为$\mathcal{O}((|C|n + (D+C_I)n^2 + n^6)\log n)$比特，其中$|C|$表示电路大小，$D$表示深度，$C_I$表示输入大小。
>
> **技术梗概:** 技术梗概：通过一个编译器，在黑盒方式下利用同步和异步三元组生成协议来生成网络无感知设置下的Beaver三元组。

---
### [2026/381] Multi-Committee MPC: From Unanimous to Identifiable Abort

- **作者:** Lichun Li, Hongqing Liu, Jiawei Ni, Chaoping Xing, Chen Yuan

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/381) | [PDF](https://eprint.iacr.org/2026/381.pdf)


> **研究背景:** 研究背景：在存在多数恶意参与者的安全多方计算(MPC)协议中，当有$(1-\epsilon)n$比例的参与者被欺骗时（$\epsilon\in (0,1/2)$），现有方案通常采用一致中断机制。
>
> **主要贡献:** 主要贡献在于提出了一种多委员会MPC协议，通过引入多个常规模块组成的委员会，并设计了手递门电路来安全地在委员会间传输信息，从而实现了在线和离线阶段的恒定通信复杂度。
>
> **达到效果:** 达到的效果是，在相同恶意参与者比例的情况下，该协议相比其他方案具有最小的实际总通信复杂度。进一步改进后，实现了可识别中断机制下的恒定通信复杂度MPC协议。
>
> **技术梗概:** 技术梗概：通过多委员会结构和手递门电路设计来平衡各参与者的通信负担，并结合电路依赖预处理和增量检查提高在线效率。

---
### [2026/383] HCTR$^{++}$ : A Beyond Birthday Bound Secure HCTR2 Variant

- **作者:** Gülnihal Öztürk, Onur Koçak, Oğuz Yayla

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/383) | [PDF](https://eprint.iacr.org/2026/383.pdf)


> **研究背景:** 当前的行业标准分组密码模式，如CBC和GCM，在高吞吐量、大数据量环境中受到生日界限的实践安全瓶颈限制。为解决这一问题，加密社区和NIST正优先考虑超越生日界限（BBB）的安全性，以扩展操作安全性至全块大小。
>
> **主要贡献:** 本文提出了一种HCTR2的简单BBB-安全变体，并解释了核心BBB方法和技术机制。
>
> **达到效果:** 该研究通过设计和实现一种新的BBB-安全模式，为标准制定工作做出了贡献，提高了现有加密算法的安全性边界。
>
> **技术梗概:** 文章首先介绍了XORP、TBCs和Fresh Rekeying等技术，并在此基础上对HCTR2的操作机制进行了讨论，最终提出了一个BBB-安全的构造方案。

---
### [2026/384] The Structured Generic-Group Model

- **作者:** Henry Corrigan-Gibbs, Alexandra Henzinger, David J. Wu

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/384) | [PDF](https://eprint.iacr.org/2026/384.pdf)


> **研究背景:** 该研究扩展了Shoup的通用群模型，以涵盖利用部分非通用群结构的算法。
>
> **主要贡献:** 作者提出了一个新模型，并证明了一类依赖特定结构的离散对数算法的时间下限。
>
> **达到效果:** 研究表明，此类算法在特定条件下必须运行时间至少为某个最小值。
>
> **技术梗概:** 通过精确定义结构利用方式并分析其复杂度来实现上述结果。

---
### [2026/385] Bridging Privacy and Utility: A Verifiable Framework for Data Valuation via Zero-Knowledge Proofs

- **作者:** Ruibang Liu, Minyu Chen, Dengji Ma, Guoqiang Li

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/385) | [PDF](https://eprint.iacr.org/2026/385.pdf)


> **研究背景:** 随着深度学习对高质量数据的需求增加，分散的数据市场正在兴起。然而，信任赤字阻碍了这一生态系统的发展：买家担心数据污染，卖家则担忧数据泄露。尽管Shapley值提供了一种公平补偿的经济框架，但其计算通常需要可信第三方访问原始数据，从而成为隐私的单点故障。
>
> **主要贡献:** 本文提出了ZK-DV系统，这是首个用于可验证、隐私保护的数据估值零知识证明系统。该系统允许卖家在不泄露任何信息的情况下，证明所声称的价值评分与底层私有数据和买家模型的一致性。
>
> **达到效果:** 实验结果表明，通过优化批量大小，ZK-DV实现了2.7倍的证明生成速度提升，同时保持了量化精度。
>
> **技术梗概:** ZK-DV的设计结合了模型训练和估值逻辑：构建了一个特殊的算术电路，将估值逻辑整合到反向传播中，从中间梯度中提取边际效用分数。该设计通过GKR协议与混合承诺策略实现，并通过批量处理摊薄了高昂的加密开销。

---
### [2026/386] Determining those Boolean functions whose restrictions to affine spaces are plateaued

- **作者:** Claude Carlet, Darrion Thornburgh

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/386) | [PDF](https://eprint.iacr.org/2026/386.pdf)


> **研究背景:** 研究探讨了布尔函数在仿射子空间上的限制性质，特别是当这些限制表现为平坦函数时。
>
> **主要贡献:** 作者确定了所有n变量布尔函数中，在任意k维仿射子空间上都表现为平坦函数的函数类。
>
> **达到效果:** 通过这一研究，作者将布尔函数按照其在不同维度仿射子空间上的表现进行了分类，并揭示了这些分类之间的包含关系。
>
> **技术梗概:** 利用代数度和仿射扩展的概念，作者证明并分类了满足特定条件的布尔函数。

---
### [2026/387] A Comprehensive Break of the Tropical Matrix-Based Signature Scheme

- **作者:** Sopan Chavhan, Shrikant Chaudhari

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/387) | [PDF](https://eprint.iacr.org/2026/387.pdf)


> **研究背景:** 该研究针对Grigoriev等提出的基于热带矩阵分解难题的数字签名方案进行系统性分析，揭示其潜在的安全漏洞。
>
> **主要贡献:** 作者提出了多项攻击方法，包括存在伪造攻击、可塑性攻击以及部分密钥恢复和全密钥恢复攻击。
>
> **达到效果:** 这些攻击表明该方案未能实现标准的不可伪造性和密钥保密性等安全属性。
>
> **技术梗概:** 通过利用签名方程式的代数性质而非直接求解NP难问题，作者设计了多项基于SMT的关键恢复攻击方法。

---
### [2026/388] Necessary and Sufficient Conditions for the Existence of Ideal Linear Secret Sharing Schemes for Arbitrary Access Structures

- **作者:** Zheng Chen, Qiuxia Xu, Chunming Tang

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/388) | [PDF](https://eprint.iacr.org/2026/388.pdf)


> **研究背景:** 研究旨在确定任意访问结构能否通过理想线性秘密共享方案实现，这是密码学领域的重要课题。
>
> **主要贡献:** 作者利用线性码构建了矩阵H和G，并证明了一个必要且充分的条件：存在满足特定方程$GH^{\mathsf{T}}=0$的解，则该访问结构可以被理想线性秘密共享方案实现。
>
> **达到效果:** 通过上述方法，研究者得出了一个等价命题：对于给定的$\Gamma_{\min}$，存在对应的理想线性码当且仅当其可由有限域$\mathbb{F}_q$上的可表示的丛结构所代表。
>
> **技术梗概:** 研究采用线性代数中的矩阵理论和线性码作为主要工具来构造实现特定访问结构的理想线性秘密共享方案。

---
### [2026/389] Towards Accountability for Anonymous Credentials

- **作者:** Shailesh Mishra, Martin Burkhart

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/389) | [PDF](https://eprint.iacr.org/2026/389.pdf)


> **研究背景:** 匿名凭证（ACs）允许用户在保护隐私的前提下证明声明，但缺乏问责机制可能导致凭证滥用问题，影响其在国家身份系统中的采用。
>
> **主要贡献:** 本文提出了一种框架以提供AC系统的问责制，并引入了加密法医轨迹(CFT)，结合执法和司法机构共同工作来追踪凭证的不当使用。
>
> **达到效果:** 该框架通过确保只有在有合理依据的情况下，警察才能请求法官颁发搜查令并获取更多信息，从而在保护隐私的同时实现问责制。
>
> **技术梗概:** CFT被附加到每个凭证展示中，当执法机构有合理依据时可申请法官签发搜查令以获取更多个人信息。

---
### [2026/391] Zero-Knowledge IOPPs for Constrained Interleaved Codes

- **作者:** Alessandro Chiesa, Giacomo Fenzi, Guy Weissenberg

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/391) | [PDF](https://eprint.iacr.org/2026/391.pdf)


> **研究背景:** 基于交互式公证证明(IOPs)的简洁论证已实现显著效率提升，并广泛应用于各种场景。然而，现有IOP构造缺乏隐私保护，这对于许多应用来说是必需的。
>
> **主要贡献:** 本文提出了一个满足诚实验证者零知识属性的交互式Oracle减少(IOR)定义，并通过构建和模块化组合多个轻量级零知识IORs实现了这一目标。
>
> **达到效果:** 该方法在保持与非零知识状态相同效率的同时，提供了隐私保护，使得验证者无法获取额外的信息。
>
> **技术梗概:** 通过设计并组合零知识求和检查IOR和代码切换IOR等关键技术，克服了多个挑战，并提出了新的概念和协议。

---
### [2026/392] Fast cube roots in Fp2 via the algebraic torus

- **作者:** Youssef El Housni

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/392) | [PDF](https://eprint.iacr.org/2026/392.pdf)


> **研究背景:** 在椭圆曲线点解压缩、哈希到曲线以及基于isogeny的协议中，计算二次扩张有限域上的立方根是一个子程序。
>
> **主要贡献:** 作者提出了一种新算法，通过代数 torus 和 Lucas 序列将 $\mathbb{F}_{p^2}$ 上的立方根运算转化为基域 $\mathbb{F}_p$ 中的操作。
>
> **达到效果:** 该方法在所有实际应用场景中都证明了有效性，并且在六个不同的素数上实现了 $1.6$ 到 $2.3$ 倍的速度提升。
>
> **技术梗概:** 算法利用了代数 torus 和 Lucas 序列，将 $\mathbb{F}_{p^2}$ 上的运算转换为 $\mathbb{F}_p$ 中的操作，并通过开源库 $\texttt{gnark-crypto}$ 实现。

---
### [2026/393] VROOM: Accelerating (Almost All) Number-Theoretic Cryptography Using Vectorization and the Residue Number System

- **作者:** Simon Langowski, Kaiwen He, Srini Devadas

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/393) | [PDF](https://eprint.iacr.org/2026/393.pdf)


> **研究背景:** 在数论密码学中，模算术运算尤其是使用大型素数模时，构成了主要的计算瓶颈。现有CPU实现依赖于代价高昂的进位操作和排列指令来对齐乘法数据路径，这抵消了向量化带来的并行化优势。
>
> **主要贡献:** 作者开发了矢量化算法以优化模加法和模乘法，并提出了一种适用于通用模数（素数或非素数）的新常时间复杂度模乘算法。这种方法利用剩余数系统(RNS)表示来自然地与宽向量单元对齐算术运算，从而战略性地消除不必要的指令。
>
> **达到效果:** 通过减少模算术的延迟，加速了RSA-4096签名验证和生成，分别提高了4.0倍和1.3倍，以及BLS签名验证速度提升了3.43倍。这些改进直接促进了实际应用中的TLS和其他密码学部署。
>
> **技术梗概:** 该方法结合了向量化技术和剩余数系统(RNS)，通过自然对齐算术运算与宽向量单元来优化模运算，并战略性地消除冗余指令，从而显著提高了效率。

---
### [2026/394] SQISign on ARM

- **作者:** Luca De Feo, Li-Jie Jian, Ting-Yuan Wang, Bo-Yin Yang

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/394) | [PDF](https://eprint.iacr.org/2026/394.pdf)


> **研究背景:** SQIsign作为一种具有紧凑密钥和签名大小的候选算法，在NIST On-Ramp Digital Signatures Call Round 2中表现出色，但其签名性能受限于理想到isogeny转换的速度瓶颈。
>
> **主要贡献:** 通过利用NEON指令集实现高效的有限域算术和批量椭圆曲线操作，首次展示了非平凡向量化加速SQIsign的方法，并实现了2.24倍的加速比。
>
> **达到效果:** 结合Qlapoti算法改进后，在NIST安全级别I下签名速度提升了超过2.24倍，为后续基于向量化的SQIsign优化提供了参考。
>
> **技术梗概:** 针对二维isogeny链计算进行了特定的有限域算术和椭圆曲线操作实现，并通过NEON指令集进行加速。

---

## 更新: 2026-03-01 16:48

*新增 7 篇论文 (编号 396--403)*

### [推荐] [2026/396] Anonymity of X-Wing and its Variants

- **匹配关键字:** post-quantum

- **作者:** Jiawei Bao, Jiaxin Pan

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/396) | [PDF](https://eprint.iacr.org/2026/396.pdf)


> **研究背景:** X-Wing是一种结合了经典和后量子加密技术的KEM机制，被考虑用于标准化并应用于确保向后量子密码学的安全过渡。
>
> **主要贡献:** 研究首次分析了X-Wing及其变体的匿名性，并证明在随机Oracle模型下，在某些条件下可以实现弱匿名性。
>
> **达到效果:** 通过改进现有IND-CCA安全性的证明，论文提高了X-Wing机制的安全性和可靠性。
>
> **技术梗概:** 采用标准模型和随机Oracle模型进行分析，提出了记忆紧致的减少方法并设计了新的变体以保持记忆紧致性。

---
### [推荐] [2026/397] Bittersweet Signatures: Bringing LWR to a Picnic for Hardware-Friendly MPC-in-the-Head

- **匹配关键字:** post-quantum

- **作者:** Brieuc Balon, Gianluca Brian, Sebastian Faust, Carmit Hazay, Elena Micheli, François-Xavier Standaert

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/397) | [PDF](https://eprint.iacr.org/2026/397.pdf)


> **研究背景:** 后量子签名方案因量子计算机对经典密码学的威胁而变得日益重要，其中MPC-in-the-head范式通过利用多方计算（MPC）提供了一种创新的零知识证明解决方案。
>
> **主要贡献:** 作者引入了Bittersweet签名方案，这是一种基于LWR假设的新类签名方案，通过使用几乎同态伪随机函数（PRF），实现了简洁的设计并提供了良好的并行实现机会。
>
> **达到效果:** 理论上分析Bittersweet签名需要应对与几乎同态操作相关的重大挑战，如泄漏问题。实际上，该方案能够提供具有竞争力的签名大小，并在硬件性能上有所提升。
>
> **技术梗概:** 通过利用几乎同态伪随机函数，作者设计了一种基于LWR假设的新类签名方案，实现了简洁的设计并提供了良好的并行实现机会。

---
### [推荐] [2026/398] Orthus: Practical Sublinear Batch-Verification of Lattice Relations from Standard Assumptions

- **匹配关键字:** lattice

- **作者:** Madalina Bolboceanu, Jonathan Bootle, Vadim Lyubashevsky, Antonio Merino-Gallardo, Gregor Seiler

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/398) | [PDF](https://eprint.iacr.org/2026/398.pdf)


> **研究背景:** 近年来，基于格的零知识证明系统因其线性大小的特点在许多量子安全隐私协议中占据重要地位。然而，这些系统的验证时间通常比其他类型的证明系统慢得多，这成为其广泛应用的主要障碍。
>
> **主要贡献:** 作者提出并实现了Orthus，一种具有亚线性验证时间的证明系统，专门针对自然出现在基于格构造中的关系。
>
> **达到效果:** 对于聚合Falcon签名的具体例子，实现后的验证运行时间减少了9倍，当聚合2^17个签名时效果尤为显著。
>
> **技术梗概:** 该技术通过使验证时间与证词大小的平方根成正比来提高效率，从而在保持证明系统有效性的同时大幅缩短了验证时间。

---
### [推荐] [2026/402] Conditionally Linkable Attribute-Based Signatures

- **匹配关键字:** lattice, post-quantum

- **作者:** Minh Pham, Khoa Nguyen, Slim Bettaieb, Mukul Kulkarni, Willy Susilo

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/402) | [PDF](https://eprint.iacr.org/2026/402.pdf)


> **研究背景:** 现有的属性基签名（ABS）方案通常将链接性视为静态的系统属性，要么始终不可链接，要么全局可链接。这种二元划分无法适应仅在显式声明条件下才应产生关联的情景。
>
> **主要贡献:** 该研究提出了条件可链接属性基签名（CLABS），这是一种扩展了ABS框架的方法，允许根据公共上下文空间中的特定条件实现程序化的、上下文相关的链接性。
>
> **达到效果:** 通过这种机制，CLABS能够在不依赖中心信任的情况下实现选择性的、可验证的关联，并且隐私泄露仅限于参与者的同意。
>
> **技术梗概:** CLABS通过定义每个属性认证用户与公共上下文空间中的链接集之间的关系来实现其目标，使用公钥函数指定如何在特定上下文中比较属性。

---
### [2026/399] What a Wonderful World: zkSNARKs in the Algebraic Group Model are Universally Composable

- **作者:** Gaspard Anthoine, Dario Fiore, Mahak Pancholi

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/399) | [PDF](https://eprint.iacr.org/2026/399.pdf)


> **研究背景:** zkSNARKs是零知识简洁非交互式知识论证，对于许多实际应用至关重要。然而，现有研究要么不具有模块性，需要针对新的证明系统进行单独分析，要么主要集中在随机预言模型中，忽略了大量高效的、常量大小的zkSNARKs。
>
> **主要贡献:** 本文通过识别简单且基本的标准属性来解决未修改的AGM（代数群模型）+ROM中的zkSNARKs的UC安全性问题，并观察这些属性对于现有zkSNARKs的验证是相对简单的任务。
>
> **达到效果:** 该研究提供了模块化的方法，确保了在任意并发执行环境中zkSNARKs的安全性分析，涵盖了Plonk和Marlin等多项式交互预言证明编译的zkSNARKs。
>
> **技术梗概:** 通过定义并验证几个基本属性来实现UC安全性，这些属性适用于多种现有的zkSNARKs系统，简化了安全性的验证过程。

---
### [2026/400] Non-interactive Blind Signatures with Threshold Issuance

- **作者:** Foteini Baldimtsi, Lucjan Hanzlik, Aayush Yadav

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/400) | [PDF](https://eprint.iacr.org/2026/400.pdf)


> **研究背景:** 研究背景：非交互式盲签名（NIBS）允许签署者在无需先前交互的情况下预计算预签名，同时确保只有指定的接收者能够生成有效的盲签名。本文旨在解决NIBS的阈值发行问题。
>
> **主要贡献:** 主要贡献：提出了非交互式阈值盲签名（NITBS）的概念，并通过修改Pointcheval-Sanders (PS) 签名方案首次实现了这一构造，定义了相关安全属性并证明其安全性。
>
> **达到效果:** 达到的效果：该构造在预签名和签名大小上最小，并且发行速度最快，优于所有现有NIBS方案。
>
> **技术梗概:** 技术梗概：通过修改Pointcheval-Sanders (PS) 签名方案来实现非交互式阈值盲签名，并证明其安全性。

---
### [2026/403] On the Need for (Quantum) Memory with Short Outputs

- **作者:** Zihan Hao, Zikuan Huang, Qipeng Liu

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/403) | [PDF](https://eprint.iacr.org/2026/403.pdf)


> **研究背景:** 研究建立了有界空间计算与无界空间计算之间在具有短输出问题上的第一个分离，无论是经典还是量子计算环境。
>
> **主要贡献:** 引入了嵌套碰撞查找问题，并证明了没有指数级内存就无法达到最优查询复杂性。
>
> **达到效果:** 通过新颖的‘两Oracle记录’技术，将短输出问题的时间-空间权衡转化为长输出问题的时间-空间权衡，从而实现了这一结果。
>
> **技术梗概:** 该方法涉及一个Oracle记录计算的长期输出在另一个Oracle下，有效减少了短输出问题的时间-空间权衡到长期输出问题的时间-空间权衡。

---

## 更新: 2026-03-03 06:54

*新增 12 篇论文 (编号 404--415)*

### [推荐] [2026/404] Ultra short signatures with Dragon $HFE_{LL'}$

- **匹配关键字:** post-quantum

- **作者:** Jacques Patarin, Jan Vacek

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/404) | [PDF](https://eprint.iacr.org/2026/404.pdf)


> **研究背景:** 本文介绍了两种新的后量子多变量签名方案，旨在提高安全性与效率。这两种方案是对HFE方案的改进版本，后者特别引入了LL'扰动以增强抵抗现有攻击的能力。
>
> **主要贡献:** 贡献在于提出了一种短签名方案$HFE_{LL'}$和一种更短的签名方案$D-HFE_{LL'}$，后者显著减少了签名长度，同时保持了安全性。
>
> **达到效果:** 结果表明，通过使用特定的LL'扰动，这两种新方案能够有效抵抗包括MinRank攻击在内的多种已知攻击方法。
>
> **技术梗概:** 技术上采用了多变量多项式变换和LL'扰动来设计签名方案，以增强其对抗性。

---
### [推荐] [2026/405] Group Encryption with Oblivious Traceability

- **匹配关键字:** post-quantum

- **作者:** Khoa Nguyen, Yanhong Xu, Nam Tran, Willy Susilo, Huaxiong Wang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/405) | [PDF](https://eprint.iacr.org/2026/405.pdf)


> **研究背景:** 该研究重新审视了组加密（GE）——一种由Kiayias等人引入的组签名的加密对应物，旨在同时提供接收者的匿名性和可追溯性。然而，关于为何需要对密文进行可追溯性的讨论尚未充分展开。
>
> **主要贡献:** 本文提出了组加密与模糊可追踪性（GEOT），这是一种增强形式的GE系统，在此系统中，密文$\psi$是否可追踪由公开的追踪策略$P(\mathsf{id},\mathbf{w}) \in {0,1}$决定。该研究进一步支持消息过滤和动态成员身份。
>
> **达到效果:** 通过正式化GEOT模型，并设计了相应的安全性和有效性证明，确保了在非追踪情况下开销机构无法得知接收者信息的同时，实现了对密文的可追踪性控制。
>
> **技术梗概:** 本文采用形式化的安全性定义来描述GEOT的安全属性，并结合零知识证明和同态加密技术实现消息过滤和动态成员身份功能。

---
### [推荐] [2026/407] On the Binding Security of KEMs based on RSA and DH

- **匹配关键字:** post-quantum

- **作者:** Juliane Krämer, Maximiliane Weishäupl, Stefan Winderl

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/407) | [PDF](https://eprint.iacr.org/2026/407.pdf)


> **研究背景:** 针对KEM的安全性新威胁，引入了绑定安全性框架，并广泛用于分析后量子方案。然而，基于经典方案的KEM尚未进行此类分析。
>
> **主要贡献:** 研究者们分析了从Diffie-Hellman、RSA及其变种等经典方案构建的KEM的绑定安全性，包括CSIDH。
>
> **达到效果:** 研究表明，所考虑的KEMs在绑定安全方面表现不一，既有攻击也有证明。建议对某些方案进行微调以提升其绑定安全性。
>
> **技术梗概:** 通过形式化分析和修改现有方案来评估并增强绑定安全性。

---
### [2026/406] Putting the OPTI in Round Optimal IA-MPC in the Plain Model

- **作者:** Yashvanth Kondi, Divya Ravi, Jure Sternad, Sophia Yakoubov

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/406) | [PDF](https://eprint.iacr.org/2026/406.pdf)


> **研究背景:** 研究背景：探讨在标准模型下实现两轮多方计算的最佳安全保证，特别是在超过一半参与者诚实的情况下。
>
> **主要贡献:** 主要贡献：首次提出了一种能够在超过一半参与者诚实时实现可识别中止的两轮通用多方计算构造。
>
> **达到效果:** 达到的效果：证明了在诚实超半数情况下，两轮即可实现可识别中止和选择性可识别中止，并且当有三分之一以上参与者可能被攻击时，实现选择性可识别中止需要三轮。
>
> **技术梗概:** 技术梗概：通过引入新的中间体不知情公开传输（OPTI）作为核心组件，设计了一种编译器将具有全体一致中止的协议提升为可识别中止的协议。

---
### [2026/408] Smoothing the degree of regularity for polynomial systems

- **作者:** Samuel Jaques, Lars Ran, Simona Samardjiska, Melvin Seitner

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/408) | [PDF](https://eprint.iacr.org/2026/408.pdf)


> **研究背景:** 在有限域上的非线性多项式系统求解中，XL算法等代数算法的复杂度由所谓的正则度决定。然而，正则度是一个粗略参数，可能导致过度确定的马卡尤矩阵，从而增加时间和内存需求。
>
> **主要贡献:** 作者提出了一种‘平滑’正则度的技术，可以在两个整数值之间操作，并通过考虑特定子矩阵来减少复杂性，而无需构建完整的马卡尤矩阵。
>
> **达到效果:** 在实验中验证了该方法的有效性，表明它能够降低XL算法的复杂度，从而提高效率并节省资源。
>
> **技术梗概:** 该技术基于一个温和假设，即广义半正则性的概念，并通过分析特定子矩阵来实现正则度的平滑化。

---
### [2026/409] Cryptanalysis of Poseidon-Based Fiat-Shamir Protocols

- **作者:** Hayk Hovhannisyan, Nerses Asaturyan, Gohar Hovhannisyan

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/409) | [PDF](https://eprint.iacr.org/2026/409.pdf)


> **研究背景:** 本文研究了基于Poseidon的Fiat-Shamir协议的安全性，探讨了将减少轮数的Poseidon与Fiat-Shamir变换结合使用是否能引发新的攻击。
>
> **主要贡献:** 作者设计并实现了多种候选攻击方案，这些方案将验证者检查和基于Poseidon的挑战生成编码为显式的多项式系统，并利用Gröbner基方法进行评估。
>
> **达到效果:** 尽管尝试了多种方法，但在代表性参数设置下，Gröbner基计算并未找到随机构造系统的解，未能获得有意义的伪造实例，这为几种自然的代数攻击提供了负面证据。
>
> **技术梗概:** 研究采用了将验证者检查和减少轮次的Poseidon挑战生成编码为多项式系统的方法，并使用Gröbner基技术进行评估。

---
### [2026/410] Collaborative Incrementally Verifiable Computation

- **作者:** Eden Aldema Tshuva, Sanjam Garg, Abhiram Kothapalli, Rotem Oshman, Omkant Pandey, Bhaskar Roberts

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/410) | [PDF](https://eprint.iacr.org/2026/410.pdf)


> **研究背景:** 现有的协作零知识论证系统在处理大规模数据集时存在内存和通信开销过大的问题，且缺乏可更新性。
>
> **主要贡献:** 该研究提出了协作增量验证计算方案，允许多个互不信任的参与方在保持隐私的同时共同验证计算结果，并能随着计算的每一步进行实时更新证明。
>
> **达到效果:** 该方案实现了每个步骤中各参与方仅需常数通信开销和与单步内存成本成比例的内存开销。
>
> **技术梗概:** 通过设计增量更新机制，结合广播信道优化了通信效率，并确保了系统的可扩展性和实用性。

---
### [2026/411] A Built-in Crypto Expert for Artificial Intelligence: How Far is the Horizon?

- **作者:** Jiasi Weng, Jian Weng, Ming Li

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/411) | [PDF](https://eprint.iacr.org/2026/411.pdf)


> **研究背景:** 本文提出了一种将专用“Crypto Expert”嵌入大型语言模型（LLMs）架构中的内置框架，旨在初步探索如何在深度学习中融合形式化的加密保证。
>
> **主要贡献:** 贡献在于设计了一个针对AES算法的可微分代理，并通过定制化神经元单元实现了功能等效性，同时支持反向传播。
>
> **达到效果:** 实验结果显示，该方法显著减少了神经元数量和延迟，缓解了连续差分攻击，并在不损害下游任务性能的情况下确保端到端的数据保护。
>
> **技术梗概:** 技术上采用了SoftXOR、SoftLUT和GF conv等定制化神经元单元，提供AES算法的功能等效性，同时保证梯度的稳定性。

---
### [2026/412] VisualDedup: Visual Fuzzy Deduplication for Secure Batch Duplicates Detection without Server Aided

- **作者:** Shengke Zeng, Zehui Tang, Song Han, Mingxing He

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/412) | [PDF](https://eprint.iacr.org/2026/412.pdf)


> **研究背景:** 针对云存储中加密数据的重复检测问题，现有方法往往在安全性和效率上存在不足。
>
> **主要贡献:** 提出了Visual Fuzzy Deduplication方案，用于隐匿敏感多媒体数据，并仅保留一份副本以优化隐私保护的云存储。
>
> **达到效果:** 实验结果显示该方案能有效实现批量重复检测和抵御暴力攻击，且具有较高的实用性和效率。
>
> **技术梗概:** 通过视觉模糊技术处理图像数据，结合哈希函数进行重复性检查，无需服务器辅助。

---
### [2026/413] On Best-Possible One-Time Programs

- **作者:** Aparna Gupte, Jiahui Liu, Luowen Qian, Justin Raizes, Bhaskar Roberts, Mark Zhandry

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/413) | [PDF](https://eprint.iacr.org/2026/413.pdf)


> **研究背景:** 研究背景：经典和量子环境中的一次性程序（OTPs）旨在保护单次执行的安全性，但现有方案在随机功能性和最强安全性方面存在局限。
>
> **主要贡献:** 主要贡献：证明了一般意义上的最佳一次性编译器不可能存在，并定义了可测试一次性程序编译器的新类别。
>
> **达到效果:** 达到的效果：揭示了最佳安全性的理论极限，并为特定子类别的最优安全性提供了解决方案。
>
> **技术梗概:** 技术梗概：通过假设损失性加密方案的存在，证明了一般编译器的不可能性；引入可测试一次性程序编译器的概念并进行形式化定义。

---
### [2026/414] Towards Practical Registered ABE: More Efficient, Non-monotone, and CCA-secure

- **作者:** Yannis Rouselakis, Junichi Tomida

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/414) | [PDF](https://eprint.iacr.org/2026/414.pdf)


> **研究背景:** 注册属性基加密（Reg-ABE）旨在解决属性基加密（ABE）中的关键托管问题，通过让用户自行生成公私钥对来实现公共密钥基础设施模型和灵活的访问控制功能。
>
> **主要贡献:** 该研究提出了一种高效的空间非单调注册属性基加密方案，并支持非单调策略和选择性不可伪造性（CCA-安全），这两者都是GLWW方案所不具备的特性。
>
> **达到效果:** 与GLWW方案相比，该方案的主密钥和密文大小分别减少了约2000倍和5倍，在实际参数设置下其他元素如辅助密钥和系统维护的状态也减少了超过40倍。加密性能优于GLWW方案，解密时间大约为几秒。
>
> **技术梗概:** 通过优化密钥结构和采用高效的加密算法实现了上述效果，并在通用组模型中证明了其安全性。

---
### [2026/415] Separating Non-Interactive Classical Verification of Quantum Computation from Falsifiable Assumptions

- **作者:** Mohammed Barhoush, Tomoyuki Morimae, Ryo Nishimaki, Takashi Yamakawa

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/415) | [PDF](https://eprint.iacr.org/2026/415.pdf)


> **研究背景:** 该研究旨在探讨无交互式经典验证量子计算（Non-Interactive Classical Verification of Quantum Computation）是否可以从可验证假设中分离出来，特别是在量子计算与复杂性类之间的关系上。
>
> **主要贡献:** 作者证明了在存在QMA-QCMA间隙问题的情况下，无法通过任何可验证假设来实现无交互式的经典验证量子计算。
>
> **达到效果:** 这一结果表明，在当前的理论框架下，无交互式经典验证量子计算可能需要更强的安全性假设才能实现。
>
> **技术梗概:** 研究采用了相对构造的方法，并借助量子酉算子作为辅助工具，以支持QMA-QCMA间隙问题的存在性。



## 更新: 2026-03-04 07:21

*新增 10 篇论文 (编号 416--425)*

### [推荐] [2026/416] An Ultra-Robust Privacy Preserving Scheme for Federated Learning using Distributed Homomorphic Encryption

- **匹配关键字:** homomorphic encryption

- **作者:** Ikhlas Mastour, Layth Sliman, Boussad Ait Salem, Balthazar Bauer, Raoudha Ben Djemaa, Kamel Barkaoui

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/416) | [PDF](https://eprint.iacr.org/2026/416.pdf)


> **研究背景:** 联邦学习是一种新兴的机器学习范式，它允许在数据源处直接进行模型训练，并仅传输模型更新，从而减少通信瓶颈并减轻与原始数据暴露相关联的风险。然而，最近的研究表明，在联邦学习中隐私仍然有限且容易受到推断攻击的影响。
>
> **主要贡献:** 本文提出了一种结合分布式同态加密方案和阈值线性秘密共享的鲁棒性和抗毁联邦学习框架（RRFL-DHE），以解决现有隐私保护不足的问题。
>
> **达到效果:** 通过严格的半诚实服务器模型安全证明以及在非独立同分布MNIST和Fashion MNIST数据集上的实证评估，表明该框架能够保持与FedAvg方法相当的模型性能，并且在准确率方面优于xMK-CKKS方法约15%。
>
> **技术梗概:** RRFL-DHE通过客户端加密其模型更新来实现安全聚合，同时引入了一种断线管理协议以确保训练连续性和全局模型重建准确性。

---
### [推荐] [2026/417] Tweed: Adaptively Secure Lattice-Based Two-Round Threshold Signatures

- **匹配关键字:** lattice, LWE

- **作者:** Kaijie Jiang, Stefano Tessaro, Hoeteck Wee, Chenzhi Zhu

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/417) | [PDF](https://eprint.iacr.org/2026/417.pdf)


> **研究背景:** 该研究旨在设计一种适应性安全的基于格的两轮门限签名方案，以提高签名效率并增强安全性。
>
> **主要贡献:** 论文提出了首个能够容忍最多$T-1$个适应性腐败签名者（共$N$个）的基于格的两轮门限签名方案。
>
> **达到效果:** 与现有五轮构造相比，该方案显著提高了效率，并在相同的假设下提供了更强的安全保障。
>
> **技术梗概:** 设计采用了MLWE和MSIS假设为基础的技术路线，通过优化协议流程实现了两轮目标。

---
### [推荐] [2026/418] A White-Box Bootstrapping Approach for High Precision Comparison Over Homomorphic Encryption

- **匹配关键字:** homomorphic encryption

- **作者:** Deokhwa Hong, Heesoo Lee, Young-Sik Kim, Yongwoo Lee

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/418) | [PDF](https://eprint.iacr.org/2026/418.pdf)


> **研究背景:** 该研究针对Cheon–Kim–Kim–Song (CKKS)同态加密(HE)方案中的符号评估提出了一个高效且数值稳定的解决方案，旨在改进比较、排序和机器学习等应用。
>
> **主要贡献:** 作者提出了一种新的白盒bootstrapping方法，用于符号评估，并证明了该方法能够减少噪声，从而加速收敛并提高精度。
>
> **达到效果:** 实验结果表明，所提出的方案在相同参数下实现了约40位的精度，是现有技术的两倍左右。
>
> **技术梗概:** 通过借鉴bootstrapping bits的方法，作者设计了一种新的白盒bootstrapping技术，该技术能够减少噪声并提高数值稳定性。

---
### [推荐] [2026/419] Hermine: An Efficient Lattice-based FROST-like Threshold Signature

- **匹配关键字:** lattice, post-quantum

- **作者:** Giacomo Borin, Sofía Celi, Rafael del Pino, Thomas Espitau, Shuichi Katsumata, Guilhem Niot, Thomas Prest, Kaoru Takemure

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/419) | [PDF](https://eprint.iacr.org/2026/419.pdf)


> **研究背景:** 随着对量子安全需求的增加，现有的FROST等经典阈值签名方案因其提供部分非交互式签名、可识别中止和主动安全性而受到关注。然而，当前没有方案能够同时具备这些特性。
>
> **主要贡献:** Hermine通过引入无处不在的短秘密共享机制，首次在格基上实现了具有FROST全部特性的阈值签名方案。
>
> **达到效果:** Hermine能够在支持中等规模参与者（$N \le 64$）的情况下，生成大小仅为11KB的小型签名，显著提高了效率和安全性。
>
> **技术梗概:** 通过设计无处不在的短秘密共享机制，并提供一种简洁的线性重构算法来实现高效安全的阈值签名。

---
### [推荐] [2026/420] FALCON with message recovery, a specification

- **匹配关键字:** lattice

- **作者:** Felix Gunther, Vadim Lyubashevsky, Rolfe Schmidt

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/420) | [PDF](https://eprint.iacr.org/2026/420.pdf)


> **研究背景:** FALCON是一种基于格的数字签名方案，旨在由NIST标准化为FN-DSA。尽管其签名和公钥尺寸较小，但实现较为复杂，因此仅在特别需要小密钥和签名尺寸的情况下推荐使用。
>
> **主要贡献:** 本文详细说明了FALCON的消息恢复模式，这是一种减少总签名加消息长度的方法，相比FALCON-512可节省最多226字节，相比FALCON-1024可节省最多434字节。
>
> **达到效果:** 通过使用FALCON的消息恢复模式，可以在保持相同安全级别的前提下显著减小签名和消息的总长度，从而优化资源有限的应用场景。
>
> **技术梗概:** 该技术涉及对FALCON进行较小的修改以实现消息恢复功能，并详细规定了公钥恢复过程中的具体步骤。

---
### [推荐] [2026/421] Cryptanalysis of Polynomial Learning With Errors (PLWE): A Survey

- **匹配关键字:** lattice, post-quantum, LWE

- **作者:** Rahinatou Yuh Njah Nchiwo

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/421) | [PDF](https://eprint.iacr.org/2026/421.pdf)


> **研究背景:** Lattice-based cryptography通过其强大的安全性保证，在后量子密码学领域展现出巨大潜力，但传统的Learning With Errors问题效率较低。为了提高实用性，发展了Ring-LWE和Polynomial-LWE等变体。
>
> **主要贡献:** 该综述论文系统地回顾了PLWE的脆弱实例，并探讨了这些攻击可能如何扩展到RLWE的情况。
>
> **达到效果:** 通过分析PLWE的安全性弱点，研究者们能够更好地理解其潜在风险，并为设计更安全的密码学方案提供指导。
>
> **技术梗概:** 该综述采用文献回顾的方法，总结了现有针对PLWE的有效攻击技术及其局限性。

---
### [2026/422] Threshold Traitor Tracing Revisited: Insider Attacks and Multi-Traitor Tracing

- **作者:** Jan Bormet, Sebastian Faust, Hussien Othman

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/422) | [PDF](https://eprint.iacr.org/2026/422.pdf)


> **研究背景:** 该研究针对阈值密文解密中的篡改追踪机制，特别是在外部买家与内部成员（即解密委员会成员）之间的攻击场景下，现有方案存在漏洞。
>
> **主要贡献:** 作者提出了新的定义来描述被内部成员购买的解码器，并展示了现有技术对这种攻击是脆弱的。随后，他们提出了一种多篡改追踪的新方法以实现内部成员的防御能力。
>
> **达到效果:** 通过所提出的编译器，研究成功地提高了可识别篡改者的数量，实现了在参数有效的情况下，特别是子线性密文大小下的内部成员防护。
>
> **技术梗概:** 该研究利用了多篡改追踪技术，并设计了编译器来放大能被追踪的篡改者数量，从而增强了系统的安全性。

---
### [2026/423] Coppersmith's Method for Solving Modular Inversion Hidden Number Problem via Determinant-Based Elimination

- **作者:** Zhaopeng Ding, Zhaopeng Dai, Baofeng Wu, Rundong Wang, Yanshuo Zhang

- **分类:** Attacks and cryptanalysis

- **链接:** [论文](https://eprint.iacr.org/2026/423) | [PDF](https://eprint.iacr.org/2026/423.pdf)


> **研究背景:** 研究聚焦于改进Coppersmith方法以解决模逆隐藏数字问题，通过选择合适的移位多项式来提高计算效率和准确性。
>
> **主要贡献:** 提出了一种基于行列式的新型策略来生成这些多项式，并据此优化了Coppersmith方法。
>
> **达到效果:** 该方法在解决模逆隐藏数字问题和预测逆同余发生器方面表现优异，理论和实践上均优于先前的方法。此外，证明了模逆双隐藏数字问题并不比单个问题更难。
>
> **技术梗概:** 通过引入行列式为基础的消元法来选择移位多项式，从而提高了Coppersmith方法在特定多变量模方程中的应用效果。

---
### [2026/424] CRISP: Circuit-pRivate Single-Image Steganography with Permutations

- **作者:** Shahzad Ahmad, Stefan Rass

- **分类:** Foundations

- **链接:** [论文](https://eprint.iacr.org/2026/424) | [PDF](https://eprint.iacr.org/2026/424.pdf)


> **研究背景:** 现有方法在电路隐私和图像冗余方面存在不足，CRISP旨在解决这些问题。
>
> **主要贡献:** $CRISP$ 提出了一种新的同态隐写方案，实现了单图像嵌入并保护电路隐私。
>
> **达到效果:** 该方案显著减少了所需图像的数量，并且能够防止云服务提供商推断逻辑门结构。
>
> **技术梗概:** 通过在单一图像中使用置换技术重新分配输入和输出通道角色来实现电路的隐私性。

---
### [2026/425] Committing Security of BBB Secure MACs

- **作者:** Sougata Mandal, Hrithik Nandi, Amlan Sinha

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/425) | [PDF](https://eprint.iacr.org/2026/425.pdf)


> **研究背景:** 随着端到端加密消息系统中滥用报告等应用的需求增加，传统的MAC安全属性如不可伪造性和伪随机性变得不足，促使研究者们提出了更强的安全概念。
>
> **主要贡献:** 本文扩展了BBB安全MAC的研究范围，并分析了Chen等人提出的双密码分组密码和单散列函数构造的类别的安全性。
>
> **达到效果:** 研究表明，尽管某些构造容易受到攻击，但其他构造表现出一定的抗性，表明BBB安全MAC中的承诺与上下文发现安全依赖于其结构设计选择。
>
> **技术梗概:** 通过分析基于DbHtS范式的几个已知BBB安全MAC构造，本文揭示了这些构造在面对特定攻击时的表现差异。

---

## 更新: 2026-03-05 21:59

*新增 24 篇论文 (编号 426--449)*

### [推荐] [2026/426] Post-Quantum Security of Keyed Sum of Permutations and Its Siblings

- **匹配关键字:** post-quantum

- **作者:** Nilanjan Datta, Avijit Dutta, Sougata Mandal, Hrithik Nandi, Amlan Sinha

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/426) | [PDF](https://eprint.iacr.org/2026/426.pdf)


> **研究背景:** 随着量子计算的快速发展，现有密码构造的安全性面临严峻挑战。在经典模型下被认为是安全的某些构造，在量子模型下可能变得脆弱。
>
> **主要贡献:** 本文研究了Keyed Sum of Permutations及其两个变体在Q1模型下的安全性，并证明了它们可以提供$n/3$比特的安全性。
>
> **达到效果:** 对于使用相同密钥的变体，我们展示了具有匹配复杂度的关键恢复攻击，从而确立了安全边界的紧致性。对于其他两种构造，我们推导出了关键恢复攻击，其复杂度为$2^{2n/3}$。
>
> **技术梗概:** 通过形式化分析和构建特定类型的攻击来确定这些密码学构造在限制条件下所能提供的安全性边界。

---
### [推荐] [2026/427] StarHunters— Secure Hybrid Post-Quantum KEMs From IND-CCA2 PKEs

- **匹配关键字:** post-quantum

- **作者:** Deirdre Connolly, Mike Ounsworth, Sophie Schmieg, Douglas Stebila

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/427) | [PDF](https://eprint.iacr.org/2026/427.pdf)


> **研究背景:** 该研究旨在设计一种安全的混合后量子公钥加密机制，结合传统和后量子密码学的优点以抵抗量子计算攻击。
>
> **主要贡献:** 论文提出了CK构造方法，通过使用伪随机函数（PRF）将两种不同的KEM组合起来，并展示了如何从一个IND-CCA2 PKE方案中安全地构建出IND-CCA KEM。
>
> **达到效果:** 研究证明了CK在标准模型下是IND-CCA安全的，即使传统部分被完全破坏，后量子部分仍能提供安全性保证。
>
> **技术梗概:** 该方法通过结合C2PRI-安全的后量子KEM和IND-CCA2的传统PKE方案，并利用伪随机函数进行封装，实现了混合加密机制的安全性。

---
### [推荐] [2026/428] Defending Against Backdoor Attacks in Homomorphically Encrypted Federated Learning

- **匹配关键字:** homomorphic encryption

- **作者:** Ikhlas Mastour, Imane Haidar, Layth Sliman, Raoudha Ben Djemaa

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/428) | [PDF](https://eprint.iacr.org/2026/428.pdf)


> **研究背景:** 联邦学习系统的分布式特性使其容易受到后门攻击，恶意客户端通过触发依赖行为操纵本地训练数据以实现目标误分类。
>
> **主要贡献:** 提出了一种在推理时识别全局模型异常内部激活模式的防御策略，无需检查加密的单个客户端更新。
>
> **达到效果:** 该方法能够有效检测并拒绝可疑预测，同时保持较低的训练开销并在非独立同分布数据设置下仍具鲁棒性。
>
> **技术梗概:** 通过构建使用少量干净数据集推导出类特定阈值的统计激活基线，来识别和拒绝异常预测。

---
### [推荐] [2026/432] Finite Field Arithmetic for ML-KEM Using Zech's Logarithm

- **匹配关键字:** post-quantum

- **作者:** Masaaki Shirase

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/432) | [PDF](https://eprint.iacr.org/2026/432.pdf)


> **研究背景:** ML-KEM的处理涉及在有限域${\mathbb F}_{3329}$中进行多项式的乘法、加法和减法操作，通常使用Number Theoretic Transform (NTT)来减少这些操作的数量。
>
> **主要贡献:** 论文提出了一种基于Zech's Logarithm的对数表示方法，用于在${\mathbb F}_{3329}$中实现乘法、加法和减法运算，并解决了0参与操作时的特殊情况处理问题。
>
> **达到效果:** 通过使用该对数表示法，论文实现了${\mathbb F}_{3329}^*$中的乘法可以转化为$\mathbb{Z}_{3328}$中的加法，同时加法和减法可以在对数域中计算，从而提高了效率。
>
> **技术梗概:** 通过引入Zech's Logarithm的对数表示法，并针对0参与操作的情况进行了特殊处理，论文提供了一种新的${\mathbb F}_{3329}$上算术运算的实现方法。

---
### [推荐] [2026/436] Post-Quantum Anonymous Signatures from the Lattice Isomorphism Group Action

- **匹配关键字:** lattice, post-quantum

- **作者:** Chris van Noorden, Paola de Perthuis

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/436) | [PDF](https://eprint.iacr.org/2026/436.pdf)


> **研究背景:** 该研究针对后量子匿名签名方案，旨在克服经典密码学中依赖于寻找秘密子群的局限性，并探索更通用的组作用假设。
>
> **主要贡献:** 作者通过引入零知识证明OR语句的方法，首次构建了适用于Lattice Isomorphism Problem (LIP) 的通用盲签和强指定验证者签名方案。
>
> **达到效果:** 该研究成功地实现了匿名性和不可伪造性的双重保障，并且这些方案基于标准假设下的广义组作用逆问题。
>
> **技术梗概:** 通过利用零知识证明技术，作者设计了一种新的构造方法，能够在非紧致、非交换的无限作用群上实现匿名签名功能。

---
### [推荐] [2026/440] Performance Analysis of a Thread Pool-Based Parallel Execution Model for Hybrid Post-Quantum TLS 1.3 Handshakes

- **匹配关键字:** post-quantum

- **作者:** Si-Woo Eum, Min-Ho Song, Hwa-Jeong Seo

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/440) | [PDF](https://eprint.iacr.org/2026/440.pdf)


> **研究背景:** 后量子密码学（PQC）的过渡显著增加了TLS 1.3握手过程中的计算成本，而混合PQC TLS 1.3握手则因需同时执行经典和PQC算法而面临更大的开销。
>
> **主要贡献:** 该研究提出了一种基于POSIX线程池的并行执行模型来分析混合PQC TLS 1.3握手性能，并评估了多种组合以优化其效率。
>
> **达到效果:** 通过比较串行与并行执行时间，研究实现了1.08至1.40倍的速度提升，特别是在使用P-384配置时效果最佳。
>
> **技术梗概:** 采用POSIX线程池技术，并对135种组合进行了评估，涵盖3种经典KEM、3种ML-KEM变体、3种经典DSAs和5种PQC DSAs。

---
### [推荐] [2026/442] Memory-Efficient Implementation of SMAUG-T and HAETAE

- **匹配关键字:** lattice, post-quantum

- **作者:** Yulim Hyoung, Subeen Cho, Uijae Kim, Minwoo Lee, Hwajeong Seo, Minjoo Sim

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/442) | [PDF](https://eprint.iacr.org/2026/442.pdf)


> **研究背景:** SMAUG-T和HAETAE被选为韩国后量子密码标准算法，但在ARM Cortex-M4微控制器上运行时，峰值堆栈使用量成为关键限制。
>
> **主要贡献:** 提出了一套针对SMAUG-T和HAETAE的内存优化技术，使其能够在Cortex-M4严格的内存预算内运行。
>
> **达到效果:** 与KpqClean_ver2基准相比，优化后的SMAUG-T5峰值堆栈使用量减少了73-83%，而HAETAE5在签名时减少了约90%。
>
> **技术梗概:** 应用了无分支的常时间间设计以确保优化实现能够抵御侧信道威胁如定时攻击。

---
### [推荐] [2026/445] Implementation of a post-quantum hybrid group key exchange protocol

- **匹配关键字:** post-quantum

- **作者:** Tomáš Fabšič, Samuel Klement, Zoltán Raffay, Pavol Zajac

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/445) | [PDF](https://eprint.iacr.org/2026/445.pdf)


> **研究背景:** 后量子密码学致力于研究能够抵抗量子计算机攻击的加密原语，如公钥加密和签名。Steinwandt 和 Gonzales Vasco 提出了一种结合了传统后量子密码学与量子密钥交换的安全协议。
>
> **主要贡献:** 本文详细描述了该协议的具体实现细节，并提供了一个可作为科学界参考的原型应用架构。
>
> **达到效果:** 通过实施该协议，作者成功地展示了其在实际应用中的可行性，并讨论了相关挑战和开放问题。
>
> **技术梗概:** 采用混合组密钥交换技术，结合后量子密码学与量子物理原理来保护通信链路的安全性。

---
### [推荐] [2026/446] Survey of isogeny-based signature schemes resistant to Castryck–Decru attack

- **匹配关键字:** post-quantum

- **作者:** J. S. Bobrysheva, A. S. Zelenetsky, V. V. Davydov

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/446) | [PDF](https://eprint.iacr.org/2026/446.pdf)


> **研究背景:** 2022年，Castryck和Decru提出了一种攻击方法，破解了包括SIKE在内的多种基于曲率的方案。尽管如此，由于这些方案提供了紧凑的密钥大小，研究工作仍在继续。
>
> **主要贡献:** 本文对抵抗Castryck-Decru攻击的基于曲率的签名方案进行了系统性回顾，分为CSIDH群作用类和SQIsign家族两类，并讨论了它们的设计原理、安全假设及具体构造。
>
> **达到效果:** 通过比较不同方案的性能与紧凑性，文章指出了在实际应用中特别有效的代表方案，并将这些方案与其他后量子签名方案进行了对比分析。
>
> **技术梗概:** 研究采用了分类的方法，分别探讨了基于CSIDH群作用和SQIsign家族两类签名方案的设计原理、安全假设及具体构造，并通过性能比较展示了其优劣。

---
### [2026/429] Efficient Private Range Queries on Public Data

- **作者:** Pranav Shriram Arunachalaramanan, Ananya Appan, David Heath, Ling Ren

- **分类:** Applications

- **链接:** [论文](https://eprint.iacr.org/2026/429) | [PDF](https://eprint.iacr.org/2026/429.pdf)


> **研究背景:** 范围查询可以过滤、聚合和检索多维矩形内的数据库条目。私有范围查询允许客户端在保持其多维矩形隐藏的情况下，对服务器的公共数据库进行查询。
>
> **主要贡献:** RangeR是一种常数轮次的私有范围查询方案，支持任何关联聚合函数，并适用于任意数量的服务器。
>
> **达到效果:** 在单服务器设置中，RangeR比VLDB 2025年的先驱方案HADES快得多，且通信量减少50%-90%。使用OpenStreetMaps数据估计，用户可以在2秒内找到距离其位置一公里内的最高评分餐厅，同时仅透露用户的地理位置在美国。
>
> **技术梗概:** RangeR通过创新的协议设计实现了高效性和隐私性，在保持查询私密性的前提下提升了性能和通信效率。

---
### [2026/430] An attack on the CFS scheme and on TII McEliece challenges

- **作者:** Magali Bardet, Axel Lemoine, Jean-Pierre Tillich

- **分类:** Unknown

- **链接:** [论文](https://eprint.iacr.org/2026/430) | [PDF](https://eprint.iacr.org/2026/430.pdf)


> **研究背景:** 研究背景：CFS签名方案的安全性基于高率二进制Goppa码的McEliece方案，长期以来人们一直不确定是否可以攻击这种方案。尽管有初步的区分器结果和多次尝试，但针对高率二进制Goppa码的McEliece方案至今仍未找到有效的攻击方法，仅在特定情况下（如Goppa多项式度数为2）有所突破。
>
> **主要贡献:** 主要贡献：本文通过结合Pfaffian建模、短化技巧和寻找理想中的平方项的方法，提出了一种针对CFS签名方案的多项式时间攻击方法，成功破解了这一已存在25年的签名方案。
>
> **达到效果:** 达到的效果：该研究展示了新方法的有效性，能够恢复TII McEliece挑战中声称具有最高210位密钥安全性的私钥。
>
> **技术梗概:** 技术梗概：利用Couvreur等人在Asiacrypt 2023中的Pfaffian建模方法，并结合短化技巧和寻找理想中的平方项，提出了针对高率二进制Goppa码的McEliece方案的新攻击策略。

---
### [2026/431] Revisiting the Security of Sparkle

- **作者:** Ojaswi Acharya, Georg Fuchsbauer, Adam O'Neill, Marek Sefranek

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/431) | [PDF](https://eprint.iacr.org/2026/431.pdf)


> **研究背景:** 研究重新审视了Crites等人在CRYPTO 2023提出的Sparkle和其变体Sparkle+的三轮门限Schnorr签名方案的安全性，前者声称具有完全自适应安全性但存在分析缺口，后者则缺乏静态安全性的证明。
>
> **主要贡献:** 主要贡献在于首次为Sparkle提供了静态安全性证明，并在纯随机预言机模型中给出了首个紧致的安全性证明，无需依赖代数群模型。
>
> **达到效果:** 研究解决了上述方案的安全性问题，通过引入新的Vandermonde循环离散对数（VCDL）假设，克服了自适应设置下回放论证失效的问题，并且该分析还强调了使用循环风格的假设作为在自适应安全性等场景中确保安全性的通用方法。
>
> **技术梗概:** 技术上，通过将VCDL假设归约到Crites等人提出的低维向量表示（LDVR）问题来证明其有效性；反之亦然，VCDL假设蕴含了LDVR问题的解决。

---
### [2026/433] Round-Optimal Threshold Blind Signatures without Random Oracles

- **作者:** Georg Fuchsbauer, Fabian Regen, Hoeteck Wee

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/433) | [PDF](https://eprint.iacr.org/2026/433.pdf)


> **研究背景:** 本文解决了在不依赖随机Oracle的情况下构建圆最优阈值盲签名的问题，这是该领域的一个重要突破。
>
> **主要贡献:** 作者提出了首个无需随机Oracle的圆最优阈值盲签名方案，并且改进了现有技术以减少假设依赖和通信成本。
>
> **达到效果:** 此方案实现了在不对称配对群中的代数组模型安全性，并能容忍至多$t-1$个签名者被适应性破坏，同时将通信和计算成本降至盲BLS签名的两倍。
>
> **技术梗概:** 该技术基于2-DL假设，在代数组模型中构建了新的基于配对的圆最优盲签名方案。

---
### [2026/434] Secure Cloud Storage: Modularization, Network Adversaries and Adaptive Corruptions

- **作者:** Jonas Janneck, Doreen Riepel

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/434) | [PDF](https://eprint.iacr.org/2026/434.pdf)


> **研究背景:** 针对大规模部署的端到端云存储解决方案，近期研究揭示了严重的保密性和完整性攻击问题。为了应对这些挑战，BDGHP在CRYPTO 2024提出了首个形式化的安全云存储处理方法，定义了语法和安全性概念，并提供了一个基于Two-Hash Diffie-Hellman (2HDH) OPRF的高效构造方案。
>
> **主要贡献:** 本文在此基础上进行了扩展和完善：首先证明其构造在适应性破坏下仍可安全；其次通过引入认证过程的模块化，明确了2HDH的作用并提供了替代实现；最后提出了一个更弱的模型来捕捉网络控制型对手，并证明了在线密码猜测攻击的具体保证。
>
> **达到效果:** 这些改进使得云存储方案在面对更广泛的攻击场景时也能提供更强的安全保障，特别是在文件共享和网络控制方面取得了突破性进展。
>
> **技术梗概:** 研究采用了形式化方法定义安全概念，通过引入模块化设计和弱化模型来增强安全性证明的灵活性与实用性。

---
### [2026/435] Information-Theoretic Strong Traceable Secret Sharing Schemes

- **作者:** Oriol Farràs, Miquel Guiot

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/435) | [PDF](https://eprint.iacr.org/2026/435.pdf)


> **研究背景:** 该研究旨在改进通用访问结构下的可追踪秘密共享方案，通过引入新的模型和方法解决现有方案的限制。
>
> **主要贡献:** 主要贡献在于提出了首个完全基于信息论的秘密共享方案，适用于空强可追踪性模型，并解决了先前工作中的开放问题。
>
> **达到效果:** 该方案成功消除了对强密码假设的需求，实现了在无需加密技术的情况下进行有效可追踪秘密共享的目标。
>
> **技术梗概:** 研究采用了新的无标签重建框和隐藏访问结构的技术方法，结合信息论原理设计了全新的秘密共享机制。

---
### [2026/437] Efficient Single-Server Stateful PIR Using Format-Preserving Encryption

- **作者:** Pranav Shriram Arunachalaramanan, Ling Ren

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/437) | [PDF](https://eprint.iacr.org/2026/437.pdf)


> **研究背景:** Stateful PIR解决了传统PIR中服务器状态更新的问题，但现有方案在通信、计算和客户端存储效率上仍有待提高。
>
> **主要贡献:** 作者提出了HarmonyPIR方案，通过引入新的提示组织方式，仅使用单一随机置换实现了高效性。
>
> **达到效果:** HarmonyPIR相比现有最佳方案，在平均计算成本和通信开销上分别提高了两个数量级和五倍的效率。
>
> **技术梗概:** 该技术利用AES或FF1格式保留加密实现单随机置换实例化，构建了两种变体的HarmonyPIR方案。

---
### [2026/438] Updatable Private Set Intersection from Symmetric-Key Techniques

- **作者:** Junxin Liu, Peihan Miao, Mike Rosulek, Xinyi Shi, Jifeng Wang

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/438) | [PDF](https://eprint.iacr.org/2026/438.pdf)


> **研究背景:** 私有集合交集（PSI）已成为极其实用的工具，主要得益于现代协议几乎完全依赖于廉价的对称密钥密码技术。然而，在可更新PSI（UPSI）中，参与方的输入集合会随时间变化，重新计算交集的成本仅取决于其集合的变化量，这使得现有协议中的公钥操作数量与项目数量成正比，效率较低。
>
> **主要贡献:** 本文提出了首个主要避免使用公钥操作的可更新私有集合交集（UPSI）协议。通过利用对称密钥原语，我们的实现相比之前的工作取得了数个数量级的性能提升。此外，我们还观察到现有UPSI的安全证明未考虑选择性输入攻击者，即根据前一时期对手视图选择当前周期要添加的项目。
>
> **达到效果:** 我们的协议在面对适应性选择输入的攻击者时仍能保持安全性，并且通过使用一种新的、更清晰的无感知键值存储（OKVS）抽象提高了UPSI的安全性和实用性。
>
> **技术梗概:** 该工作利用了对称密钥原语，引入了一种新颖的、更简洁的无感知键值存储（OKVS）抽象来实现上述目标。

---
### [2026/439] The OCH Authenticated Encryption Scheme

- **作者:** Sanketh Menda, Mihir Bellare, Viet Tung Hoang, Julia Len, Thomas Ristenpart

- **分类:** Secret-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/439) | [PDF](https://eprint.iacr.org/2026/439.pdf)


> **研究背景:** 针对现有广泛部署的认证加密方案存在的多用户安全性不足、上下文承诺安全性和非随机性 nonce 的局限，本文提出了一种新的 OCH 认证加密方案。
>
> **主要贡献:** OCH 方案首次实现了 128 位多用户认证加密和 128 位上下文承诺安全性，并支持 256 位非随机性 nonce 选项，增强了现有方案的安全性和灵活性。
>
> **达到效果:** 在 Intel Raptor Lake CPU 上，使用 Areion 分组族的 OCH 方案峰值加密速度达到每字节 0.62 循环次数（cpb），接近 AES128-GCM 的性能，并优于 ChaCha20/Poly1305 和 TurboSHAKE128-Wrap。
>
> **技术梗概:** OCH 通过模块化构造和形式分析，使用了可广泛适用的转换方法来实现上述安全性和性能目标。

---
### [2026/441] Fuzzy Private Set Intersection for Real-World Datasets

- **作者:** Satvinder Singh, Yanxue Jia, Aniket Kate

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/441) | [PDF](https://eprint.iacr.org/2026/441.pdf)


> **研究背景:** 模糊私有集合交集(Fuzzy Private Set Intersection, Fuzzy PSI)允许双方在不泄露额外信息的情况下计算其私人集合的交集，适用于密码学中的重要应用如密码匹配、面部识别和接触追踪。然而，现有Fuzzy PSI方案基于强假设，导致理论与实际数据集不符。
>
> **主要贡献:** 作者提出了一种新的假设，该假设基于集合稀疏性，并设计了一个编译器将基于强假设的Fuzzy PSI构造转换为基于新假设的构造。
>
> **达到效果:** 通过结合当前的Fuzzy PSI协议和新型编译器，实现了在实际数据集上更有效的隐私保护应用。
>
> **技术梗概:** 核心思想是高维提升和着色技术，用于将强假设下的Fuzzy PSI方案转换为基于新假设的方案。

---
### [2026/443] PRISM with a pinch of salt: Simple, Efficient and Strongly Unforgeable Signatures from Isogenies

- **作者:** Andrea Basso, Giacomo Borin, Wouter Castryck, Maria Corte-Real Santos, Riccardo Invernizzi, Antonin Leroux, Luciano Maino, Frederik Vercauteren, Benjamin Wesolowski

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/443) | [PDF](https://eprint.iacr.org/2026/443.pdf)


> **研究背景:** 研究背景：基于超奇异椭圆曲线的isogeny难题被假设为对经典和量子计算机都难以解决，本文利用此难题构建了一种安全的身份验证协议，并进一步开发了高效的签名方案。
>
> **主要贡献:** 主要贡献在于提出了一个两轮身份认证协议及相应的签名方案，该方案在标准模型下证明是安全的，并且具有简洁灵活的签名过程。
>
> **达到效果:** 达到的效果包括：签名速度比现有SQIsign实现快1.4到1.6倍；验证时间根据安全性级别不同，从慢1.2倍到快0.99倍不等；公钥和签名大小与现有方案相当。
>
> **技术梗概:** 技术梗概：通过哈希和签名的范式，结合isogeny难题构建了高效的签名机制，并证明其安全性和效率。

---
### [2026/444] Leakage-Diagrams, Importance Sampling, and Composition  in the Random Probing Model

- **作者:** Vahid Jahandideh, Bart Mennink, Lejla Batina

- **分类:** Implementation

- **链接:** [论文](https://eprint.iacr.org/2026/444) | [PDF](https://eprint.iacr.org/2026/444.pdf)


> **研究背景:** 在低噪声环境下，提高屏蔽级数并不总是意味着更高的实际抗侧信道攻击能力。现有方法将有噪泄漏简化为随机探针模型（RPM），但这些简化往往过于宽松，无法提供实用的泄漏率估计，并且当前的RPM分析通常依赖于昂贵的模拟或数值传播边界。
>
> **主要贡献:** 作者开发了用于估算和上界屏蔽组件及其组合在RPM下的安全性的分析和算法工具。具体包括：基于二进制内积实现更紧致的$\mathbb{F}_2$线性减少，提供信噪比与探针率之间的直接联系；利用向量空间表示法将$\mathbb{F}_q$线性电路中的RPM泄漏视为擦除事件，并与局部度量建立直接联系；改进重要性采样以估计罕见泄漏事件，从而在低速率高阶数情况下进行评估。
>
> **达到效果:** 通过上述工具和方法，作者能够更准确地评估屏蔽技术的安全性，并提供实际操作中更有意义的泄漏率估计。此外，还重新审视了泄漏图示技术并为刷新组件提供了明确边界。
>
> **技术梗概:** 研究采用了$\mathbb{F}_2$线性减少、向量空间表示法和重要性采样等技术来改进RPM分析，并结合泄漏图示技术提供更精确的安全评估方法。

---
### [2026/447] Trace: Complete Client-Side Account Access Logging

- **作者:** Paul Gerhart, Carolina Ortega Pérez, Thomas Ristenpart

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/447) | [PDF](https://eprint.iacr.org/2026/447.pdf)


> **研究背景:** 尽管认证机制有所改进，账户被攻破的情况仍然频繁发生，用户需要一种可信赖的方式来确定哪些设备访问过其账户。然而，这与现代网络隐私要求相矛盾，后者规定网络服务不得学习静态设备标识符。
>
> **主要贡献:** Trace 提出了一种新的客户端加密访问日志系统（CSAL），实现了完整的日志记录同时保持隐私性。
>
> **达到效果:** 该系统通过独立的日志服务存储可验证的证据来记录每次认证，确保只有用户可以检查这些日志，并且网络服务对此不知情，从而保持与现有认证基础设施的兼容性。
>
> **技术梗概:** Trace 通过在加密日志中记录每次认证的可验证证据实现这一目标，同时保证了设备归属的可验证性、向后兼容性和对恶意对手的正式安全分析。

---
### [2026/448] Interactive Proofs for Batch Polynomial Evaluation

- **作者:** Gal Arnon, Alessandro Chiesa, Giacomo Fenzi, Eylon Yogev

- **分类:** Cryptographic protocols

- **链接:** [论文](https://eprint.iacr.org/2026/448) | [PDF](https://eprint.iacr.org/2026/448.pdf)


> **研究背景:** 多项式是理论计算机科学中基本的数学对象，验证者在证明系统中的常见任务之一是对一个度数为d的多项式在m个不同的点进行评估。
>
> **主要贡献:** 作者提出了一种具体的高效MA协议，在这种协议中，验证者的运行时间呈线性增长：作图者发送一条消息，包含d-1个字段元素，而验证者仅需执行O(m+d)次字段操作。
>
> **达到效果:** 该协议在多个交互证明中提高了验证者的时间效率，特别是在大求和域上的sumcheck协议以及依赖多项式商化的协议中。此外，通过直接应用这些结果，作者将STIR协议（CRYPTO 2024）的验证时间减少到与WHIR（EUROCRYPT 2025）相同。
>
> **技术梗概:** 该研究采用了一种新的方法来优化多项式的批量评估过程，通过减少验证者的工作量和提高协议效率，实现了在保持安全性的前提下进行高效的批量验证。

---
### [2026/449] Short Signatures from DDH without Pairings or Random Oracles

- **作者:** Dario Catalano, Valentina Frasca, Emanuele Giunta

- **分类:** Public-key cryptography

- **链接:** [论文](https://eprint.iacr.org/2026/449) | [PDF](https://eprint.iacr.org/2026/449.pdf)


> **研究背景:** 本文旨在设计基于DDH问题的短签名方案，不依赖对数配对或随机预言机，以克服现有方案在效率和安全性证明上的局限。
>
> **主要贡献:** 作者提出了两个基于多项式DDH难题的短签名构造，第一个保证选择性安全，第二个实现完全存在不可伪造性。
>
> **达到效果:** 所提出的方法能够在标准素阶数群中实现，并且无需对数配对或随机预言机即可证明安全性。
>
> **技术梗概:** 通过巧妙利用DDH问题的性质，作者设计了一种新的签名算法结构，确保了方案的安全性和效率。

---
