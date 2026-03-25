# IACR ePrint 论文摘要 - 2026

> 密码学论文自动摘要，来源：[IACR ePrint Archive](https://eprint.iacr.org/2026/)
> 由 [ePrint Summary Tool](https://github.com/lym/ePrintSummary) 生成

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
