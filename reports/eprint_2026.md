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
