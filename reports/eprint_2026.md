# IACR ePrint 论文摘要 - 2026

> 密码学论文自动摘要，来源：[IACR ePrint Archive](https://eprint.iacr.org/2026/)
> 由 [ePrint Summary Tool](https://github.com/lym/ePrintSummary) 生成

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
