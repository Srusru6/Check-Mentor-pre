Received May 9, 2016, accepted June 9, 2016, date of publication June 21, 2016, date of current version November 18, 2016.

Digital Object Identifier 10.1109/ACCESS.2016.2582836

# A Commercial Video-Caching System for Small-Cell Cellular Networks Using Game Theory

JUN LI $^{1}$ , (Senior Member, IEEE), JINSHAN SUN $^{1}$ , YUWEN QIAN $^{1}$ , FENG SHU $^{1}$ , (Member, IEEE), MING XIAO $^{2}$ , (Senior Member, IEEE), AND WEI XIANG $^{3}$ , (Senior Member, IEEE)

$^{1}$ School of Electronic and Optical Engineering, Nanjing University of Science and Technology, Nanjing 210094, China  
$^{2}$ School of Electrical Engineering, Royal Institute of Technology, Stockholm 114 28, Sweden  
$^{3}$ College of Science and Engineering, James Cook University, Cairns, QLD 4811, Australia

Corresponding author: J. Li (jun.li@njust.edu.cn)

This work was supported in part by the National Natural Science Foundation of China under Grant 61501238, Grant 61271230, and Grant 61472190, in part by the Jiangsu Provincial Science Foundation under Project BK20150786, in part by the Specially Appointed Professor Program in Jiangsu Province, 2015, in part by the Fundamental Research Funds for the Central Universities under Grant 30916011205, in part by the Open Research Fund of National Key Laboratory of Electromagnetic Environment under Grant 201500013, and in part by the Open Research Fund of National Mobile Communications Research Laboratory, Southeast University under Grant 2013D02.

![](images/db272a54c6cb4af0d726ba5d34e06ad2d83427aa8a462562649f8491d6ecb5b3.jpg)

ABSTRACT Evidence indicates that requesting video clips on demand accounts for a dramatic increase in data traffic over cellular networks. Caching part of popular videos in the storage of small-cell base stations (SBS) in cellular networks is an efficient method to reduce transmission latency and mitigate redundant transmissions. In this paper, we propose a commercial caching system consisting of a video retailer (VR) and multiple network service providers (NSPs). Each NSP leases its SBSs, with some price, to the VR for the purpose of making profits, and the VR, after storing popular videos in the rented SBSs, can provide better local video services to the mobile users, thereby gaining more profits. We conceive this system within the framework of a Stackelberg game by treating the SBSs as a specific type of resources. Then, we establish the profit models for both the NSPs and the VR based on stochastic geometry. We further investigate the Stackelberg equilibrium by solving the optimization problems in two cases, i.e., whether or not the VR has a budget plan on renting the SBSs. Numerical results are provided for quantifying the proposed framework by showing its efficiency on pricing and resource allocation.

![](images/dfe22abdadcc3ce314998c2b008bd3c3d8999a6a8b51dcfc597a0110a400eb06.jpg)

INDEX TERMS Wireless caching, content-centric communications, small-cell networks, stochastic geometry, Stackelberg game.

# I. INTRODUCTION

Wireless data traffic is expected to increase exponentially in the next few years, driven by a dramatic growth of mobile users (MU) and their bandwidth-hungry applications. There is evidence that MUs' downloading of on-demand videos is the major reason for the data avalanche over cellular networks [1]. There are numerous repetitive requests on the same videos from the MUs, such as online movies, leading to redundant transmissions. Fortunately, this redundancy can be reduced by locally storing popular videos, known as caching, into the memory of intermediate network nodes, effectively forming a local caching system [1]–[5]. This local caching brings video content closer to the MUs and alleviates redundant data transmissions via

redirecting the downloading requests to the intermediate nodes.

Generally, wireless data caching consists of two stages: data placement and data delivery [6]. In the data placement stage, popular videos are cached into local storages during off-peak time, while in the data delivery stage, requested videos are delivered from the local caching system to the MUs. Recent works advance the caching technology in device-to-device (D2D) networks and wireless sensor networks [7]-[9]. Specifically in [7], a caching scheme is proposed for a D2D based cellular network on the MUs' caching of popular video content. In this scheme, the D2D cluster size is optimized for reducing the downloading delay. In [8] and [9], the authors propose novel caching schemes for

wireless sensor networks, where the protocol model of [10] is adopted.

As small-cell embedded architectures will be prevailing in future cellular networks [11]–[16], caching relying on small-cell base stations (SBS), namely, small-cell caching, is a promising trend. The advantages brought about by the small-cell caching are threefold. First, popular videos are pushed closer to the MUs when cached in SBSs, reducing the transmission latency. Second, redundant data transmissions over SBSs' back-haul channels are mitigated, which are usually expensive [17]. Third, the majority of video traffic is offloaded from macro-cell base stations to SBSs.

In [18], a small-cell caching scheme, called 'Femtocaching', is proposed for a cellular network embedded with SBSs, where the data placement at the SBSs is optimized in a centralized manner for reducing the transmission delay imposed. In [19], the small-cell caching is investigated in the context of stochastic networks. The average performance is developed via stochastic geometry [20], [21], where the distribution of network nodes are modeled by Poisson point process (PPP).

From above discussions, current studies on wireless caching usually consider a specific aspect of caching, e.g., data placement optimization. However, a practical caching system should be coupled with many issues other than data placement. From a commercial or financial perspective, it will be more interesting to consider a comprehensive system, including the issues such as pricing on video streaming, renting local storages, and so on. Such a system may consist of video retailers (VR), network service providers (NSP) and MUs. The VRs, e.g., Youtube, purchase copyrights from video producers and publish the videos on their web-sites. The NSPs are typically operators of cellular networks, who are in charge of network facilities, such as macro-cell base stations and SBSs.

In such a commercial caching system, the VRs make profits by providing video streaming services to the MUs. As the central servers of the VRs, which store the popular videos, are usually located at backbone networks and far away from the MUs, an efficient solution is to locally cache these videos for reducing the transmission latency, thereby attracting more customers. These local-caching demands raised by the VRs offer the NSPs profitable opportunities from leasing their resources, i.e., the SBSs. In this sense, both the VRs and NSPs are the beneficiaries from the local caching system. However, each entity is selfish and wishes to maximize its own benefit, raising a competition and optimization problem, which can be effectively solved under the game theory framework.

We note that game theory has been successfully applied to wireless communications for solving competition problems on network resources [22], [23]. Stackelberg game is a commonly-used strategic game that consists of leaders and followers competing with each other for certain resources [24]. The leader moves first and the followers move subsequently.

In this paper, we will develop a commercial caching prototype, consisting of a video retailer (VR) and multiple network service providers (NSP), drawing upon a Stackelberg game framework. We consider the NSPs to be the leaders and the VR the follower, while treat the SBSs in the charge of the NSPs as a specific type of resources. The NSPs set the prices of leasing their SBSs, while the VR decides on renting a fraction of the SBSs based on the prices charged.

Specifically, we first follow the theory of stochastic geometry [20], [21], and model the MUs and SBSs in the network as two different ties of a Poisson point process (PPP) [25]. Under this network model, we define the concept of a successful video downloading event when an MU obtains the requested video directly from the storage of an SBS. Then we derive the probability of this event with a closed-form expression. Next, we establish the profit models for both the NSPs and the VR based on the probability derived. Furthermore, we investigate the Stackelberg equilibrium by solving the optimization problems in two cases, i.e., whether or not the VR has a deliberate budget plan on spending how much money in renting the SBSs. Numerical results are finally provided to quantify the proposed framework by showing its efficiency on pricing and resource allocation.

The rest of this paper is organized as follows. We describe the system model in Section II and investigate the caching procedure in Section III. The profit models and a Stackelberg game framework are formulated in Section IV. In Section V and VI, we investigate Stackelberg equilibriums for the two cases via solving a series of optimization problems. Our numerical results are detailed in Section VII, while our conclusions are provided in Section VIII.

# II. SYSTEM MODEL

We focus our attention on a commercial small-cell caching system consisting of  $L$  NSPs, one VR, and multiple MUs, where each NSP is in charge of a number of SBSs. Denote by  $\mathcal{V}$  the VR and by  $\mathcal{L} = \{\mathcal{L}_1,\mathcal{L}_2,\dots ,\mathcal{L}_L\}$  the set of the NSPs.

# A. NETWORK MODEL

Let us consider a small-cell network composed of SBSs owned by the  $L$  NSPs, where the SBSs owned by the  $l$ -th NSP  $\mathcal{L}_l$ ,  $l = 1,\dots ,L$ , equipped with a transmission power  $P_{l}$  are spatially distributed as a homogeneous PPP (HPPP)  $\Phi_l$  of intensity  $\lambda_{l}$ . Here, the intensity represents the average number of SBSs in per unit area. The VR  $\mathcal{V}$  rents a fraction  $\tau_{l}\in [0,1]$  of SBSs from  $\mathcal{L}_l$  for the purpose of caching its video files. We assume that the rented SBSs of  $\mathcal{L}_l$  are uniformly selected by the VR, and thus the distribution of these SBSs can be modeled as a "thinned" HPPP with the intensity of  $\tau_{l}\lambda_{l}$ . Each MU is affiliated with an NSP and connects to one of its SBSs for accessing network services. We model the distribution of the MUs that are affiliated with  $\mathcal{L}_l$  as an independent HPPP  $\Psi_{l}$  of intensity  $\zeta_l$ ,  $\forall l$ .

The wireless down-link channels spanning from the SBSs to the MUs are independent and identically distributed (i.i.d.),

and modeled as the combination of path-loss and Rayleigh fading. Without a loss of generality, we conduct our analysis on a typical MU  $\mathcal{M}$  located at the origin. The path-loss between  $\mathcal{M}$  and an SBS located at  $x$  is denoted by  $\| x\|^{-\alpha}$ , where  $\alpha$  is the path-loss exponent. The channel power of the Rayleigh fading between them is denoted by  $h_x$ , where  $h_x\sim \exp (1)$ . The noise at each MU is Gaussian distributed with variance  $\sigma^2$ .

We assume that the SBSs from the same NSP transmit on the same channel, causing mutual interferences. At the same time, different NSPs are allocated with orthogonal channels. Hence, there are no interferences across NSPs. To simplify the notation, we utilize the location  $x$  of a rented SBS from  $\mathcal{L}_l$  to represent a point in the HPPP  $\Phi_l$ ,  $\forall l$ . The received signal-to-interference-plus-noise ratio (SINR) at a typical MU  $\mathcal{M}$  in  $\Psi_l$  from an SBS  $\mathcal{B}$  in  $\Phi_l$ , located at  $x_l$ , can be expressed as

$$
\rho \left(x _ {l}\right) = \frac {P _ {l} h _ {x _ {l}} \left\| x _ {l} \right\| ^ {- \alpha}}{\sum_ {x \in \Phi_ {l} \backslash x _ {l}} P _ {l} h _ {x} \left\| x \right\| ^ {- \alpha} + \sigma^ {2}}, \tag {1}
$$

where  $\sum_{x\in \Phi_l\backslash x_l}P_lh_x\| x\|^{-\alpha}$  represents the interference from the SBSs of  $\Phi_l$  except for  $\mathcal{B}$ .

Definition 1 (Coverage): An MU is defined to be "covered" by an SBS located at  $x$  as long as  $\rho(x)$  is no lower than a pre-set SINR threshold  $\delta$ .

Generally, an MU can be covered by multiple SBSs.

# B. VIDEO POPULARITY

We now model the popularity distribution, i.e., the distribution of request probabilities, among video files. Denote by  $\mathcal{F} = \{\mathcal{F}_1,\mathcal{F}_2,\dots ,\mathcal{F}_F\}$  a video set, which consists of  $F$  popular video files to be possibly cached in the SBSs and then requested frequently by the MUs. The popularity distribution among  $\mathcal{F}$  is represented by a vector  $q = [q_{1},q_{2},\dots ,q_{F}]$ . That is, the MUs make independent requests of the  $f$ -th video file  $\mathcal{F}_f,f = 1,\dots ,F$ , with the probability of  $q_{f}$ .

Generally, the vector  $q$  can be modeled by a Zipf distribution [26], i.e.,

$$
q _ {f} = \frac {1 / f ^ {\beta}}{\sum_ {i = 1} ^ {F} 1 / i ^ {\beta}}, \quad \forall f, \tag {2}
$$

where the exponent  $\beta$  is a positive value, characterizing the file popularity. A larger  $\beta$  corresponds to a higher content reuse, i.e., the most popular files account for the majority of requests. From Eq. (2), we can see that  $\mathcal{F}_1$  has the highest popularity, while  $\mathcal{F}_F$  has the lowest one.

# III. CACHING PROCEDURE

There are three stages in our caching system. In the first stage, the VR  $\mathcal{V}$  purchases the copyrights of popular videos in  $\mathcal{F}$  from video producers. In the second stage, the VR negotiates with the  $L$  NSPs on renting their SBSs for caching its popular videos. In the third stage, the MUs connect to the SBSs to obtain their desired videos.

We now explain the last two stages with more details. In the second stage, upon obtaining popular videos, the VR

negotiates with the NSPs on renting their SBSs and then caches these video clips into the memories of the rented SBSs. We assume that the SBSs owned by  $\mathcal{L}_l$  are equipped with a specified storage of  $Q_{l}$ , i.e., each SBS of  $\mathcal{L}_l$  can store  $Q_{l}$  video files. Meanwhile, each SBS of  $\mathcal{L}_l$  is required to cache the most popular  $Q_{l}$  files  $\mathcal{F}_1,\dots ,\mathcal{F}_{Q_l}$ . Based on the prices offered by the NSPs, the VR then decides to rent a fraction  $\tau_{l}$  of SBSs from  $\mathcal{L}_l$ . In the third stage, the MUs start to download videos on demand. Generally, an MU will connect to the nearest SBS that caches the requested files. To evaluate the downloading performance, we first introduce the following definition.

Definition 2 (Successfully Download Event  $\mathcal{E}_{l,f}$ ): When an MU  $\mathcal{M}$  affiliated with  $\mathcal{L}_l$  demands  $\mathcal{F}_f$ , the request will be redirected to the nearest SBS  $\mathcal{B}$  in  $\Phi_l$  that caches  $\mathcal{F}_f$ . If  $\mathcal{M}$  is covered by  $\mathcal{B}$ , the requested video can be obtained directly from  $\mathcal{B}$ , and we define such an event by  $\mathcal{E}_{l,f}$ .

In the case that the event  $\mathcal{E}_{l,f}$  does not occur, the MU  $\mathcal{M}$  will connect to the central server of  $\nu$ , posited at backbone networks, for the requested video clip, causing a high transmission latency. Regarding the probability  $\operatorname*{Pr}(\mathcal{E}_{l,f})$  of the event  $\mathcal{E}_{l,f}$ , we have the following theorem based on the stochastic geometry theory.

Theorem 1: The probability  $\operatorname{Pr}(\mathcal{E}_{l,f}), \forall l, f$ , can be expressed as

$$
\begin{array}{l} \Pr (\mathcal {E} _ {l, f}) \\ = \left\{ \begin{array}{l l} \int_ {0} ^ {\infty} \exp \left(- \pi \left(1 - \tau_ {l}\right) \lambda_ {l} C (\delta , \alpha) z ^ {2}\right) & \\ \pi \tau_ {l} \lambda_ {l} \exp \left(- \pi \tau_ {l} \lambda_ {l} A (\delta , \alpha) z ^ {2}\right) & \\ \exp \left(- \frac {z ^ {\alpha} \delta}{P _ {l}} \sigma^ {2}\right) \exp \left(- \pi \tau_ {l} \lambda_ {l} z ^ {2}\right) d z ^ {2} & f \leq Q _ {l}, \\ 0 & F \geq f > Q _ {l}, \end{array} \right. \tag {3} \\ \end{array}
$$

where we have

$$
\begin{array}{l} A (\delta , \alpha) \triangleq \frac {2 \delta}{\alpha - 2} _ {2} F _ {1} \left(1, 1 - \frac {2}{\alpha}; 2 - \frac {2}{\alpha}; - \delta\right), \\ C (\delta , \alpha) \triangleq \frac {2}{\alpha} \delta^ {\frac {2}{\alpha}} B \left(\frac {2}{\alpha}, 1 - \frac {2}{\alpha}\right). \tag {4} \\ \end{array}
$$

Furthermore,  $_{2}F_{1}(\cdot)$  in the function  $A(\delta ,\alpha)$  is the hypergeometric function and the Beta function in  $C(\delta ,\alpha)$  is formulated as  $B(x,y) = \int_0^1 t^{x - 1}(1 - t)^{y - 1}\mathrm{d}t.$

Proof: Please refer to Appendix A.

Generally, the power of interference in a network is much greater than that of the noises. By assuming that  $\frac{\sigma^2}{P_l}$  goes to zero, we further simplify Eq. (3) in the following corollary.

Corollary 1: In the case that  $\frac{\sigma^2}{P_l}$  goes to zero and  $f\leq Q_{l}$ , we have

$$
\Pr (\mathcal {E} _ {l, f}) = \frac {\tau_ {l}}{(1 - \tau_ {l}) C (\delta , \alpha) + \tau_ {l} A (\delta , \alpha) + \tau_ {l}}. \tag {5}
$$

Proof: Please refer to Appendix B.

Remark 1: According to Corollary 1, when interference is dominant, the probability  $\operatorname{Pr}(\mathcal{E}_{l,f})$  is independent of both the transmission power  $P_{l}$  and the intensity  $\lambda_{l}$ .

# IV. PROBLEM FORMULATION

In our commercial caching system, the VR  $\mathcal{V}$  intends to rent a fraction  $\tau_{l}$  of SBSs from the NSP  $\mathcal{L}_l$ ,  $\forall l$ , for caching its popular videos, since it can make profit from providing the MUs with faster downloading services and mitigating unnecessary data traffic caused by MUs' repetitive downloading requests. At the same time, the NSPs will also be able to gain profits from renting their SBSs. Both the VR and the NSPs try to maximize their gains.

We first model the profits of the VR and the NSPs obtained from the caching system. Average profit is developed based on the stochastic geometry in terms of per unit area and per unit period  $(/UAP)$ , e.g., /month  $\cdot km^2$ . Then we present the Stackelberg game formulation for the caching system. The equilibrium of the proposed game will also be investigated.

# A. PROFIT MODELING

# 1) AVERAGE PROFIT OF VR

For the VR  $\mathcal{V}$ , the revenue gained, with the help of local caching, is from  $\mathcal{V}$ 's providing fast downloading services as well as mitigating the traffic from its central server. We denote by  $s$  the profit acquired by the VR when an MU downloads a video clip from the local caching system, and denote by  $K$  the number of video requests from each MU on average within an unit period. Then the overall income/  $UAP$  of  $\mathcal{V}$  is calculated as

$$
S ^ {\text {c a c h e}} = \sum_ {l = 1} ^ {L} \sum_ {n = 1} ^ {Q _ {l}} K \zeta_ {l} q _ {n} \Pr \left(\mathcal {E} _ {l, n}\right) s. \tag {6}
$$

Meanwhile, the VR needs to pay for renting the SBSs. We denote by  $s_l$  the price for renting an SBS from  $\mathcal{L}_l$  during an unit period. Then the overall payment/  $UAP$  made by the VR can be expressed as

$$
S ^ {r e n t} = \sum_ {l = 1} ^ {L} \tau_ {l} \lambda_ {l} s _ {l}. \tag {7}
$$

We assume that the VR may make a budget on how much payment it will make in renting the SBSs. The budget is defined by  $S / UAP$ , i.e.,  $S = S^{rent}$ .

Then the net profit/UAP obtained by the VR is

$$
S ^ {V R} = S ^ {\text {c a c h e}} - S ^ {\text {r e n t}}. \tag {8}
$$

# 2) AVERAGE PROFIT OF NSPs

The income of the NSPs comes from leasing their SBSs. Meanwhile, the NSPs need to pay for the cost of maintaining the local caching system. We denote by  $c_{l}$  such cost on each rented SBS of  $\mathcal{L}_l$  during a unit period. Then the net-profit of  $\mathcal{L}_l$  can be expressed as

$$
S _ {l} ^ {N S P} = \left(s _ {l} - c _ {l}\right) \tau_ {l} \lambda_ {l}. \tag {9}
$$

# B. STACKELBERG GAME FORMULATION

Stackelberg game is a strategic game consisting of leaders and followers competing with each other for certain

resources [24]. The leaders move first and the followers move subsequently. In our small-cell caching system, we model the NSPs as the leaders, and the VR as the follower. The NSP  $\mathcal{L}_l$ ,  $\forall l$ , imposes a price  $s_l$  for leasing one of its SBSs to the VR during a unit period. We thus define the price vector  $s \triangleq [s_1, s_2, \dots, s_L]$ . After the vector  $s$  is set, the VR updates the fraction  $\tau_l$  of the SBSs that it tends to rent from  $\mathcal{L}_l$ .

# 1) OPTIMIZATION FORMULATION OF THE LEADERS

Observe from the above game model that the objective of the NSP  $\mathcal{L}_l$  is to maximize its profit  $S_l^{NSP}$  formulated in Eq. (9). Note that the fraction  $\tau_{l}$  is a function of the price  $s_l$  under the Stackelberg game formulation. This means that the fraction of the SBSs that the VR is willing to rent depends on the specific price charged for renting an SBS. If the price  $s_l$  is too high, the VR will choose not to rent any SBS from  $\mathcal{L}_l$ . At the same time, if  $s_l$  is set too low,  $\mathcal{L}_l$  cannot make any profit. Since the maximum payment made by the VR is  $S$ , the NSPs have to compete with each other on the price such that they can be selected by the VR whilst keep their profit maximized.

The optimization problem for each NSP can be summarized as follows.

Problem 1: The optimization problem of maximizing  $\mathcal{L}_l$ 's profit can be formulated as

$$
\max  _ {s _ {l} \geq 0} S _ {l} ^ {N S P} \left(s _ {l}, \tau_ {l}\right), \quad \forall l. \tag {10}
$$

# 2) OPTIMIZATION FORMULATION OF THE FOLLOWER

We adopt the expression of  $\operatorname{Pr}(\mathcal{E}_{l,f})$  in Eq. (5). Then the profit gained by the VR in Eq. (8) can be further written as

$$
\begin{array}{l} S ^ {V R} = \sum_ {l = 1} ^ {L} \sum_ {f = 1} ^ {F} K s \zeta_ {l} q _ {f} \operatorname * {P r} (\mathcal {E} _ {l, f}) - \sum_ {l = 1} ^ {L} \tau_ {l} \lambda_ {l} s _ {l} \\ = \sum_ {l = 1} ^ {L} \frac {K s \zeta_ {l} \tau_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\left(1 - \tau_ {l}\right) C (\delta , \alpha) + \tau_ {l} A (\delta , \alpha) + \tau_ {l}} - \sum_ {l = 1} ^ {L} \tau_ {l} \lambda_ {l} s _ {l}. \tag {11} \\ \end{array}
$$

We can see from Eq. (11) that once the price vector  $s$  is fixed, the profit of  $\mathcal{V}$  depends on  $\tau_l$ ,  $\forall l$ , i.e., the fraction of SBSs that are rented by  $\mathcal{V}$ . If  $\mathcal{V}$  increases the fraction  $\tau_l$ , it will gain more profit, while at the same time,  $\mathcal{V}$  have to pay for renting more SBSs. Therefore,  $\tau_l$  needs to be optimized for maximizing the profit of  $\mathcal{V}$ . By defining the fraction vector  $\boldsymbol{\tau} \triangleq [\tau_1, \dots, \tau_L]$ , this optimization can be formulated as follows.

Problem 2: The optimization problem of maximizing  $\mathcal{V}$ 's profit can be written as

$$
\max  _ {1 \succeq \tau \succeq 0} S ^ {V R} (s, \tau). \tag {12}
$$

Furthermore, in the case that the VR has a budget plan, there is the constraint  $\sum_{l=1}^{L} \tau_l \lambda_l s_l = S$ .

Problem 1 and Problem 2 together form a Stackelberg game. The objective of this game is to find the Stackelberg Equilibrium (SE) points from which neither the leaders (NSPs) nor the follower (VR) have incentives to deviate.

In the following, we investigate the SE points for the proposed game.

# C. STACKELBERG EQUILIBRIUM

For our Stackelberg game, the SE is defined as follows.

Definition 3: Let us define  $s^{\star} \triangleq [s_1^{\star}, s_2^{\star}, \dots, s_L^{\star}]$ , where  $s_l^{\star}, \forall l$ , is a solution for Problem 1, and define  $\pmb{\tau}^{\star} \triangleq [\tau_1^{\star}, \tau_2^{\star}, \dots, \tau_L^{\star}]$  a solution for Problem 2. Then the point  $(s^{\star}, \pmb{\tau}^{\star})$  is an SE for this Stackelberg game if for any  $(s, \pmb{\tau})$  with  $s \geq 0$  and  $\pmb{\tau} \geq 0$ , the following conditions are satisfied:

$$
S _ {l} ^ {N S P} \left(s _ {l} ^ {\star}, \tau_ {l} ^ {\star}\right) \geq S _ {l} ^ {N S P} \left(s _ {l}, \tau_ {l} ^ {\star}\right), \quad \forall l
$$

$$
S ^ {V R} \left(s ^ {\star}, \tau^ {\star}\right) \geq S ^ {V R} \left(s ^ {\star}, \tau\right). \tag {13}
$$

Generally speaking, the SE of a Stackelberg game can be obtained by finding its perfect Nash Equilibrium (NE). In our proposed game, we can see that the NSPs strictly compete in a non-cooperative fashion. For a non-cooperative game, the NE is defined as the operating points at which no players can improve utility by changing its strategy unilaterally.

At the NSPs' side, the best response of each NSP is to solve Problem 1. To achieve this, we need to first find the best response function of the follower VR, based on which, we further solve the best response functions for the leaders. Therefore, in our game, we first solve Problem 2 given a price vector  $s$ . Then with the obtained best response function  $\tau^{\star}$  of the VR, we solve Problem 1 for the optimum price vector  $s^{\star}$ .

In the following, we will have an in-depth investigation on this game-theoretic optimization. Specifically, we consider two cases in the optimization. In the first case, we assume that the VR does not have a concrete budget plan. That is, the VR will not take into account how much money it spends in renting SBSs. Thus the constraint  $\sum_{l=1}^{L} \tau_l \lambda_l s_l = S$  is released during the optimization. In the second case, we assume that the VR has a budget by setting  $\sum_{l=1}^{L} \tau_l \lambda_l s_l = S$  in the optimization.

# V. OPTIMIZATION WITHOUT PAYMENT CONSTRAINT

In this section, we will solve the optimization problem in our game by assuming that the constraint  $\sum_{l=1}^{L} \tau_l \lambda_l s_l = S$  is released. We first present the following lemma.

Lemma 1: Given a price vector  $s = [s_1, \dots, s_L]$ , the optimum solution of Problem 2, without considering the constraint  $\sum_{l=1}^{L} \tau_l \lambda_l s_l = S$ , can be expressed as

$$
\tau_ {l} ^ {\star} (s _ {l}) = \left[ \frac {\sqrt {\frac {K s C (\delta , \alpha) \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l} s _ {l}}} - C (\delta , \alpha)}{A (\delta , \alpha) - C (\delta , \alpha) + 1} \right] ^ {\pm}, \quad \forall l, \tag {14}
$$

where  $[w]^{\pm}$  represents  $0\leq w\leq 1$

Proof: The optimum solution  $\tau_l^\star$  can be obtained by deriving  $S^{VR}$  with respect to  $\tau_{l}$  and solving  $\frac{\mathrm{d}S^{VR}}{\mathrm{d}\tau_l} = 0$  under the constraint that  $1\geq \tau_{l}\geq 0$

We can see from Lemma 1 that  $\tau_{l}^{\star}(s_{l})\propto s_{l}^{-\frac{1}{2}}$  . If the price  $s_l$  is too high such that

$$
s _ {l} \geq s _ {l} ^ {\text {u p p e r}} \triangleq \frac {K s \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l} C (\delta , \alpha)}, \tag {15}
$$

where  $s_l^{\text{upper}}$  is calculated by letting  $\tau_l^\star = 0$ , then there is  $\tau_l^\star \leq 0$ . This means that, given the price  $s_l \geq s_l^{\text{upper}}$ , the VR will opt out renting any SBS from  $\mathcal{L}_l$  due to the high price charged. In this case, the NSP  $\mathcal{L}_l$  may need to lower the price  $s_l$  to some extent for ensuring  $\tau_l^\star(s_l) > 0$ . Meanwhile, considering the cost  $c_l$ ,  $\mathcal{L}_l$  will opt out leasing any SBS to the VR if there is  $s_l \leq c_l$ . Based on the above discussions, we have the following remark.

Remark 2: A necessary condition that the NSP  $\mathcal{L}_l$  participates in the game is  $c_{l} < s_{l} < s_{l}^{upper}$ .

On the other hand, if the price  $s_l$  given is too low such that

$$
s _ {l} \leq s _ {l} ^ {\text {l o w e r}} \triangleq \frac {K s C (\delta , \alpha) \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l} (A (\delta , \alpha) + 1) ^ {2}}, \tag {16}
$$

where  $s_l^{lower}$  is calculated by letting  $\tau_l^{\star} = 1$ , then there is  $\tau_l^{\star} \geq 1$ . This means that the price given is too low such that the VR is willing to rent all the SBSs of  $\mathcal{L}_l$ . In this case, the NSP  $\mathcal{L}_l$  may need to increase the price  $s_l$  for acquiring more profit. Substitute  $\tau_l^{\star}(s_l)$  of Lemma 1 into Eq. (9), and we have the following lemma regarding the optimum price  $s_l^{\star}$ .

Lemma 2: Given the expression of  $\tau_l^\star$  in Eq. (14), the optimum solution of Problem 1 can be expressed as

$$
s _ {l} ^ {\star} = \max  \left\{\frac {1}{\left(x ^ {\frac {1}{3}} - \frac {1}{3 c _ {l}} x ^ {- \frac {1}{3}}\right) ^ {2}}, s _ {l} ^ {\text {l o w e r}} \right\}, \quad \forall l, \tag {17}
$$

where

$$
x = \frac {C (\delta , \alpha)}{c _ {l} U _ {l}} + \sqrt {\left(\frac {C (\delta , \alpha)}{c _ {l} U _ {l}}\right) ^ {2} + \frac {1}{2 7 c _ {l} ^ {3}}},
$$

$$
U _ {l} \triangleq \sqrt {\frac {\operatorname {K s C} (\delta , \alpha) \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l}}}. \tag {18}
$$

Proof: Please refer to Appendix C.

Remark 3: The optimum solution  $s^{\star}$  in Eq. (18), combined with the solution of  $\pmb{\tau}^{\star}$  given by Eq. (14), constitutes the SE for the Stackelberg game.

From the above discussions, there exist no competitions among the NSPs when no payment constraint is imposed by the VR, since  $s_l^\star$  and  $\tau_l^\star$  only depend on the parameters of  $\mathcal{L}_l$ .

# VI. OPTIMIZATION UNDER BUDGET PLAN

We now focus our attention on the game theoretic optimization with the budget plan  $\sum_{l=1}^{L} \tau_l \lambda_l s_l = S$ . Usually, in this case, the VR does not have a sufficient  $S$  to rent enough SBSs. Thus, the money spent by the VR needs to be deliberately planned for renting the SBSs from those competent NSPs.

We first solve the optimization problem at the VR and NSPs. Thereafter, a distributed price-updating mechanism is proposed and investigated.

![](images/4fd887a0e3b54416bfca0ee5b51f8e6102c7d5e55df030018249a2c5731222f1.jpg)  
(a)

![](images/d3890f71f8fea67a87bf2591814f1df2f58a93aafa59a69e26a7cb3bea08a70e.jpg)  
FIGURE 1. The optimal prices and fractions on each SBS versus the storage size  $Q$  in the symmetric 2-NSP scenario. In specific, sub-figure (a) depicts the prices change with  $Q$ , while sub-figure (b) depicts the fractions change with  $Q$ . We consider the budget plans  $S = 10, 50, 200, 500$ , and the case without budget.  
(b)

# A. OPTIMIZATION AT VR

Regarding the optimum solution at the VR's side, we have the following theorem.

Theorem 2: Given a price vector  $s = [s_1, \dots, s_L]$ , the optimum solution  $\tau_l^\star, \forall l$ , of Problem 2 can be expressed as

$$
\tau_ {l} ^ {\star} (s) = \left\{ \begin{array}{l l} 0 & \xi > \frac {K s \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l} s _ {l} C (\delta , \alpha)} - 1, \\ 1 & \xi <   \frac {K s C (\delta , \alpha) \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l} s _ {l} (A (\delta , \alpha) + 1) ^ {2}} - 1, \\ \frac {\sqrt {\frac {K s C (\delta , \alpha) \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l} s _ {l} (1 + \xi)}} - C (\delta , \alpha)}{A (\delta , \alpha) - C (\delta , \alpha) + 1} & \text {o t h e r w i s e}, \end{array} \right. \tag {19}
$$

where

$$
\xi = \left(\frac {\sum_ {j \in \mathcal {S} _ {2}} \sqrt {K s C (\delta , \alpha) \lambda_ {j} s _ {j} \zeta_ {j} \sum_ {f = 1} ^ {Q _ {j}} q _ {f}}}{(A - C + 1) (S - \sum_ {j \in \mathcal {S} _ {1}} \lambda_ {j} s _ {j}) + \sum_ {j \in \mathcal {S} _ {2}} \lambda_ {j} s _ {j} C (\delta , \alpha)}\right) ^ {2} - 1, \tag {20}
$$

where  $S_{1}$  and  $S_{2}$  are two sets of the subscripts of  $\tau_{l}$ . For  $S_{1}$ , we have  $\tau_{j} = 1$ ,  $\forall j \in S_{1}$ . For  $S_{2}$ , we have  $0 < \tau_{j} < 1$ ,  $\forall j \in S_{2}$ .

Proof: Please refer to Appendix D.

The calculation of Theorem 2 can be implemented in the following procedure. First, we utilize the conventional waterfilling algorithm to optimize  $\tau_{l},\forall l$  , without considering the constraint  $\tau_{l}\leq 1$  . Second, we check the optimization result. If, for example, there exists  $l^{\prime}$  such that  $\tau_{l^{\prime}} > 1$  , then we set  $\tau_{l^{\prime}} = 1$  , and modify the original payment constraint to  $\sum_{l = 1,l\neq l^{\prime}}^{L}\tau_{l}\lambda_{l}s_{l} = S - \lambda_{l^{\prime}}s_{l^{\prime}}$  Next, we execute a second round water-filling process on  $\tau_{l},\forall l,l\neq l^{\prime}$  with the

updated constraint. By conducting this procedure iteratively, we finally achieve the optimum solution in Theorem 2.

Remark 4: From Theorem 2 we can see that the optimum  $\tau_{l}$  depends on the price vector  $s$ , which is contrasted by the result in Lemma 1, where the optimum  $\tau_{l}$  only depends on  $s_{l}$ . This also means that VR's budget plan will cause a competition among the NSPs.

# B. OPTIMIZATION AT NSPs

Substituting Eq. (19) into Eq. (9), Problem 1 can be rewritten as

$$
\max  _ {s _ {l} \geq 0} S _ {l} ^ {N S P} = \left(s _ {l} - c _ {l}\right) \lambda_ {l} \tau_ {l} ^ {\star} (s), \quad \forall l. \tag {21}
$$

Note that Eq. (21) is a non-cooperative game by the NSPs. Due to the insufficient payment of the VR, the optimal pricing strategy of  $\mathcal{L}_l$  depends on other NSPs' pricing strategies, causing competitions among the NSPs.

By taking the derivation of  $S_{l}^{NSP}$  to  $s_l$  and equating it to zero, we have

$$
\frac {\partial S _ {l} ^ {N S P}}{\partial s _ {l}} = \lambda_ {l} \tau_ {l} ^ {\star} (s) + \left(s _ {l} - c _ {l}\right) \lambda_ {l} \frac {\partial \tau_ {l} ^ {\star} (s)}{\partial s _ {l}} = 0, \quad \forall l. \tag {22}
$$

Solving the above equations, we obtain the optimal price  $s_l^{\star}$ . However, we can see that there is no closed-form for  $s_l^{\star}$ , since each optimal price is related to other prices. One NSP needs to update its own price after the other NSPs change their prices. As such, the optimization process for the NSPs and the VR has to be conducted in an iterative manner.

# C. ITERATIVE PROCESS

The iterative process can be summarized as follows. First, after rearranging (21), we have

$$
s _ {l} = \Gamma_ {l} (s) \triangleq c _ {l} - \frac {\tau_ {l} ^ {\star} (s)}{\partial \tau_ {l} ^ {\star} (s) / \partial s _ {l}}. \tag {23}
$$

![](images/1acb165bda6f663f97365e52f50fc6e09fdb46dfab06a31d8c1d6243b26d12eb.jpg)  
(a)

![](images/d09d164f1bf97f6a0e678fde6c77bff51a70cca44ebd8549883d7673a58a4111.jpg)  
FIGURE 2. The various profits versus the storage size  $Q$  in the symmetric 2-NSP scenario. In specific, sub-figure (a) depicts the profit of the VR versus  $Q$ , while sub-figure (b) depicts the profit of each NSP versus  $Q$ . We consider the budget plans  $S = 10, 50, 200, 500$ , and the case without budget.  
(b)

![](images/7e79884c2654ee8f0ae182b067fff40c09e8a6e1839f1a089123cc20544fbf20.jpg)  
FIGURE 3. Profits of the VR and each NSP with and without budget plans. The storage size is set to  $Q = 50$ . Solid lines represent the profit of the VR, while dashed lines represent the profit of each NSP.

In order to calculate  $s_l$  in Eq. (23), each NSP communicates with the VR to obtain the values of  $\tau_l^\star(s)$  and  $\partial \tau_l^\star(s)/\partial s_l$ . Then the updating of the NSPs' prices can be described by a vector of the form  $s = \Gamma(s)$ , where  $\Gamma(s) = [\Gamma_1(s), \dots, \Gamma_L(s)]$ . Consequently, an iterative method can be utilized to achieve the optimal solutions, expressed as

$$
s ^ {(t + 1)} = \Gamma^ {(t)} (s ^ {(t)}), \tag {24}
$$

where the superscription  $t$  represents the  $t$ -th iteration.

Note that  $\Gamma^{(t)}$  may change in different iterations, since the two sets  $S_{1}$  and  $S_{2}$  can vary. To be specific in the optimization of  $\pmb{\tau}$  at the VR in the  $t$ -th iteration, if, for example, there is  $\tau_l > 1$ , the value of  $\tau_{l}$  will be set to one and  $s_l^\star$  will be set to  $s_l^{(t)}$ . In this case, it is considered that the NSP  $\mathcal{L}_l$

![](images/bbb70df3b19f3c83ccf99224f8ba82040d5312e2aa65d9e9dd4876236fe5dcdf.jpg)  
FIGURE 4. The updating of the prices for the two NSPs versus the number of iterations. The budget plans are set to  $S = 10, 50, 200, 500$ .

achieves its equilibrium and will quit the iteration for price update.

Remark 5: Once the iterative optimization process converges, the optimum solution  $s^{\star}$ , combined with the solution of  $\pmb{\tau}^{\star}$  given by Eq. (19), constitutes the SE for the game.

# VII. NUMERICAL RESULTS

In our numerical results, we investigate the system performance versus some key parameters. Although there are lots factors in our system, the storage size  $Q_{l}$  and budget constraint  $S$  are two important ones. Other factors, such as the Zipf parameter  $\beta$  and path-loss  $\alpha$ , are usually not controlled by the game participants. Therefore, throughout this section, we set the  $F = 500$ ,  $\beta = 0.8$ ,  $s = 1$ ,  $K = 50$ ,  $\alpha = 3$ , and  $\delta = 0.1$ .

![](images/6ef5cc62129de44e33bf5bab9a303cfd40eb2ec76258558f08dc299b2cb11d29.jpg)  
(a)

![](images/2c688bfe1adf9be28860d2118983845df49e83d979e2833ba5eb6f549959f470.jpg)  
FIGURE 5. System performance versus the storage size  $Q_{2}$  in the asymmetric 2-NSP scenario. In specific, sub-figure (a) depicts the optimal prices versus  $Q_{2}$  without budget plans and with a budget  $S = 500$ , while sub-figure (b) depicts various profits versus  $Q_{2}$  with the budget plan  $S = 500$ .  
(b)

![](images/b7300f70560266e9df37e99868d8003c7bceb5d094c32c4cc247743a23f42e74.jpg)  
FIGURE 6. Profits of the VR and each NSP versus budget S. The storage size is set to  $Q_{1} = 30$  and  $Q_{2} = 10$ .

# A. 2 SYMMETRIC NSPs

First, we study a symmetric 2-NSP scenario with the two NSPs  $\mathcal{L}_1$  and  $\mathcal{L}_2$ . In this symmetric scenario, we set  $c_{1} = c_{2} = 10$ ,  $\lambda_1 = \lambda_2 = 10 / km^2$  and  $\zeta_1 = \zeta_2 = 80 / km^2$ . Also, we assume the storage size  $Q \triangleq Q_1 = Q_2$ , i.e., the SBSs of the two NSPs always have the same storage size. Furthermore, we consider the cases with and without budget plans. Particularly in the case with budget plans, we set  $S = 10, 50, 200, 500$ . Due to the symmetric settings, we have  $s_1^\star = s_2^\star$ ,  $\tau_1^\star = \tau_2^\star$ , and  $S_1^{NSP} = S_2^{NSP}$ .

Fig. 1 depicts the prices and the fractions on the rented SBSs versus the storage size  $Q$ . From the two sub-figures, we can see that in the case that there are budget plans, the optimal price and optimal fraction of the resources keep constant to  $Q$ . That is, the NSPs are unable to claim a higher price for renting their SBSs in the budget-planning case by deploying

![](images/76f2f18441030002c9b8e37aac3126f42483fef5cc21e5787f294b39fb321ecc.jpg)  
FIGURE 7. The updating of the prices for the two NSPs versus the number of iterations. The budget plans are set to  $S = 200, 500$ .

a higher storage volume in these SBSs. This is due to the competition between the two symmetric NSPs under a strict budget imposed by the VR. Also from the figure, a higher budget of the VR leads to a higher price charged by the NSPs and a higher fraction of rented SBSs by the VR.

On the other hand, in the non-budget case, the optimal price and fraction are increasing functions of  $Q$ . Obviously in this case, the price charged by the NSP and the rented fraction by VR are much higher than those in the case with budget plans. That is, without a compulsory constraint on the budget, the VR needs to pay a much higher rent, i.e.,  $S^{rent} > S = 500$ , to achieve the Stackelberg Equilibrium. However, this does not imply that the VR can gain a higher profit compared to the budget-planning case, as discussed in the following.

Fig. 2(a) and Fig. 2(b) illustrate the profits gained by the VR and each NSP versus  $Q$ , respectively. It is interesting to

![](images/ba26b0237974841cc63647e0048a5389789b831b192c74e70504f6535c54fe25.jpg)  
(a)

![](images/1f774457f35eb3463b04e9f418fbb23f3a28ce5abf9df39ee85b2f514f597ce1.jpg)  
FIGURE 8. The updating of the prices in the 4-NSP scenario and the 6-NSP scenario versus the number of iterations.  
(b)

observe that in the budget-planning case, the profit of each NSP keeps constant to  $Q$ , due to the constant  $s_l^\star$  and  $\tau_l^\star$ , as shown in Fig. 1. Although each NSP's profit increases with the growth of VR's budget, they can gain a much higher profit in the non-budget case. As to the VR's profit, we can see from the figure that when the VR has the budge plans  $S = 200, 500$ , it can gain a higher profit than that in the non-budget case, even though in the latter case the VR pays more rent  $S^{rent} > S = 500$ . In this sense, the VR may need to select an appropriate budget  $S$  to maximize its profit.

Fig. 3 shows the profits of the VR and each NSP with and without budget plans, where the storage size is fixed to  $Q = 50$ . We can see that when the budget  $S = 500$ , the VR can achieve the maximum profit around 1620, which is much higher than the non-budget case with the profit around 1250. Additionally, the profit of each NSP is almost linearly increase with  $S$ , while it is always lower than the one in the non-budget case. Since the VR and the NSPs are competing with each other, a proper budget  $S$  is generally helpful for the VR to maximize its profit.

Fig. 4 depicts the price updating versus the number of iterations for the two symmetric NSPs, where the storage size is set to  $Q = 50$ . It is observed that for a small budget, the iterative process converges quickly, generally around four or five iterations. In the case  $S = 500$ , it takes around 10 iterations before converging. Also, since the two NPSs are symmetric, the updated prices in each iteration for the two NSPs are the always the same.

# B. 2 ASYMMETRIC NSPs

Then we focus on an asymmetric 2-NSP scenario, where  $c_{1} = 10$ ,  $c_{2} = 15$ ,  $\lambda_{1} = 10 / km^{2}$ ,  $\lambda_{2} = 40 / km^{2}$ ,  $\zeta_{1} = 50 / km^{2}$ ,  $\zeta_{2} = 120 / km^{2}$ . Fig. 5 shows the optimal prices and various profits versus the storage size  $Q_{2}$  with the fixed  $Q_{1} = 30$ . In Fig. 5(a), we can see that for the non-budget case without a payment constraint, the optimal price  $s_{1}^{\star}$  is constant to  $Q_{2}$ , since there is no competitions

between the two NSPs, while  $s_2^\star$  increases with the growth of  $Q_2$ , meaning that increasing  $Q_2$  will be beneficial to  $\mathcal{L}_2$  for charging a higher price. Furthermore, in the budget-planning case with  $S = 500$ , the optimal price  $s_1^\star$  is decreasing but  $s_2^\star$  is increasing with the growth of  $Q_2$ . This is because the budget plan leads to competitions between the two NSPs:  $\mathcal{L}_2$  becomes more and more competent when increasing the storage size of its SBSs in contrast to the fixed storage  $Q_1$  of  $\mathcal{L}_1$ .

In Fig. 5(b), we consider various profits with  $S = 500$ . The profit of  $\mathcal{L}_1$  is decreasing but the profit of  $\mathcal{L}_2$  is increasing with  $Q_2$ . This is consistent with the trends of their prices with  $Q_2$  in Fig. 5(a): A higher price charged by  $\mathcal{L}_2$  leads to its higher profit. We also decompose the VR's profit into two parts, with one contributed by  $\mathcal{L}_1$ , and the other one contributed by  $\mathcal{L}_2$ . We can see that both parts of the profits increase with regard to  $Q_2$ . However, the profit contributed by  $\mathcal{L}_2$  improved much more rapidly when  $Q_2$  increases. Fig. 6 illustrates the profits of the VR and each NSP with and without budget plans, where the storage size is fixed to  $Q_1 = 30$  and  $Q_2 = 10$ . We can see that when the budget is around  $S = 300$ , the VR can achieve the maximum profit 540, which is even higher than the non-budget case with the profit around 510. Additionally, the profit of each NSP is almost linearly increasing with  $S$ .

Fig. 7 demonstrates the price updating of the NSPs with budget plans  $S = 200, 500$ . From the figure, we can see that convergence generally occurs within about 6 iterations.

# C. MULTIPLE ASYMMETRIC NSPs

To demonstrate the convergence of the iterative optimization process with budget plans, we investigate the price updating for a 4-NSP scenario and a 6-NSP scenario.

In the 4-NSP scenario, based on the settings of the above asymmetric 2-NSP scenario, we add two more NSPs, with  $c_{3} = 8$ ,  $c_{4} = 12$ ,  $\lambda_{3} = 15 / km^{2}$ ,  $\lambda_{4} = 25 / km^{2}$ ,  $\zeta_{3} = 80 / km^{2}$ ,  $\zeta_{4} = 90 / km^{2}$ . Also, in the 6-NSP scenario, based on the

settings of the 4-NSP scenario, we further add two more NSPs, with  $c_{5} = 15$ ,  $c_{6} = 7$ ,  $\lambda_{5} = 20 / km^{2}$ ,  $\lambda_{6} = 22 / km^{2}$ ,  $\zeta_{5} = 70 / km^{2}$ ,  $\zeta_{6} = 85 / km^{2}$ . The storage sizes for the four NSPs in the 4-NSP scenario are  $Q_{1} = 15$ ,  $Q_{2} = 20$ ,  $Q_{3} = 25$ ,  $Q_{4} = 30$ , while for the 6-NSP scenario, we further add  $Q_{5} = 35$  and  $Q_{6} = 40$ .

Fig. 8 shows the price updating process for the two scenarios. In specific, Fig. 8(a) depicts the price updating for the 4 NSPs in the 4-NSP scenario with budget  $S = 400$ , 800. Fig. 8(b) depicts the price updating for the 6 NSPs in the 6-NSP scenario with budget  $S = 500$ , 1200. In both scenarios, we can see that the iterative optimization between the NSPs and the VR can converge quickly within no more than 6 iterations. This demonstrates the effectiveness of the proposed optimization algorithm in multiple-NSP asymmetric scenarios with arbitrary chosen parameters.

# VIII. CONCLUSIONS

In this paper, we have considered a commercial small-cell caching system consisting of multiple NSPs and one VR, where the NSPs lease their SBSs to the VR for gaining profits, while the VR, after storing popular videos to the rented SBSs, can provide faster transmissions to the MUs, hence gaining more profits. We proposed a Stackelberg game theoretic framework by viewing the SBSs as a type of resources. We first modeled the MUs and SBSs using two independent PPPs with the aid of stochastic geometry, and developed the probability expression of successful downloading. Then, based on the probability derived, we set up the profit models and formulated a Stackelberg game for maximizing the average profit of the NSPs as well as the VR. We also investigated the Stackelberg Equilibrium for the two cases by solving a series of optimization problems. Finally, we provided several numerical results for showing that the proposed schemes are effective in both pricing and SBSs allocation.

# APPENDIX A

# PROOF OF THEOREM 1

It is obvious that if  $F \geq f > Q_{l}$ , we have  $\operatorname{Pr}(\mathcal{E}_{l,f}) = 0$ , since each SBS of  $\Phi_{l}$  only caches the most popular  $Q_{l}$  video files. Then we consider the case when  $f \leq Q_{l}$ . We assume that the SBSs of  $\mathcal{L}_l$  rented by  $\mathcal{V}$  and caching  $\mathcal{F}_f$  follow the HPPP  $\Phi_l'$  having the intensity of  $\tau_{l}\lambda_{l}$ . We consider a typical MU  $\mathcal{M}$  affiliated with  $\mathcal{L}_l$  who tries to connect to the nearest SBS  $\mathcal{B}$  in  $\Phi_l'$ . The event  $\mathcal{E}_{l,f}$  represents that this SBS can support  $\mathcal{M}$  with an SINR no lower than  $\delta$ .

We carry out the analysis on  $\operatorname{Pr}(\mathcal{E}_{l,f})$  for the typical MU  $\mathcal{M}$  located at the origin. We denote by  $z$  the distance between  $\mathcal{M}$  and  $\mathcal{B}$ , by  $x_Z$  the location of  $\mathcal{B}$ , and by  $\rho(x_Z)$  the received SINR at  $\mathcal{M}$  from  $\mathcal{B}$ . Then the average probability that  $\mathcal{M}$  can download the desired video from  $\mathcal{B}$  is

$$
\begin{array}{l} \Pr \left(\mathcal {E} _ {l, f}\right) = \Pr \left(\rho \left(x _ {Z}\right) \geq \delta\right) \\ = \int_ {0} ^ {\infty} \Pr \left( \right.\frac {P _ {l} h _ {x _ {Z}} z ^ {- \alpha}}{\sum_ {x \in \Phi_ {l} \backslash x _ {Z}} P _ {l} h _ {x} \| x \| ^ {- \alpha} + \sigma^ {2}} \geq \delta \left. \right| z\left. \right) f _ {Z} (z) d z \\ \end{array}
$$

$$
\begin{array}{l} = \int_ {0} ^ {\infty} \Pr \left(h _ {x _ {Z}} \geq u (I + \sigma^ {2}) | z\right) f _ {Z} (z) d z \\ = \int_ {0} ^ {\infty} \mathbb {E} _ {I} \left(\exp (- s I) \exp (- u \sigma^ {2})\right) f _ {Z} (z) d z, \tag {25} \\ \end{array}
$$

where we have

$$
I \triangleq \sum_ {x \in \Phi_ {l} \backslash x _ {z}} P _ {l} h _ {x} \| x \| ^ {- \alpha}, \quad u \triangleq \frac {z ^ {\alpha} \delta}{P _ {l}}, \tag {26}
$$

and  $f_{Z}(z)$  is the probability density function of  $z$ . The derivation of  $f_{Z}(z)$  is based on the null probability of the HPPP  $\Phi_l'$  with the intensity of  $\tau_l\lambda_l$ . More specifically in  $\Phi_l'$ , since the number of the SBSs  $k$  in an area of  $A$  follows the Poisson distribution, the probability of the event that there is no SBS in the area with the radius of  $z$  can be calculated as  $\operatorname{Pr}(k = 0 \mid A = \pi z^2) = e^{-A\tau_l\lambda_l}\frac{(A\tau_l\lambda_l)^k}{k!}$  [20].

By using the derivation of the above expression, we arrive at  $f_{Z}(z) = 2\pi \tau_{l}\lambda_{l}z\exp \left(-\pi \tau_{l}\lambda_{l}z^{2}\right)$ . Note that the interference  $I$  consists of two parts. The first part, denoted by  $I_{1}$ , comes from the SBSs in  $\Phi_l$  but not in  $\Phi_l'$ , and the second part, denoted by  $I_{2}$ , comes from the SBSs in  $\Phi_l'$  excluding the nearest SBS  $\mathcal{B}$ . We have the expressions of the two interference as

$$
I _ {1} = \sum_ {x \in \Phi_ {l} \backslash \Phi_ {l} ^ {\prime}} P _ {l} h _ {x} \| x \| ^ {- \alpha}, \quad I _ {2} = \sum_ {x \in \Phi_ {l} ^ {\prime} \backslash x Z} P _ {l} h _ {x} \| x \| ^ {- \alpha}. \tag {27}
$$

Since the two parts of interference are independent, there is

$$
\mathbb {E} _ {I} (\exp (- u I)) = \prod_ {t = 1} ^ {2} \mathbb {E} _ {I _ {t}} (\exp (- u I _ {t})). \tag {28}
$$

For  $\mathbb{E}_{I_1}(\exp (-uI_1))$ , we have

$$
\begin{array}{l} \mathbb {E} _ {I _ {1}} \left(\exp (- u I _ {1})\right) \\ \stackrel {(a)} {=} \mathbb {E} \left(\prod_ {x \in \Phi_ {l} \backslash \Phi_ {l} ^ {\prime}} \int_ {0} ^ {\infty} \exp \left(- u P _ {l} h _ {x} \| x \| ^ {- \alpha}\right) \exp (- h _ {x})   \mathrm {d} h _ {x}\right) \\ = \mathbb {E} \left(\prod_ {x \in \Phi_ {l} \backslash \Phi_ {l} ^ {\prime}} \frac {1}{1 + u P _ {l} \| x \| ^ {- \alpha}}\right) \\ \stackrel {(b)} {=} \exp \left(- (1 - \tau_ {l}) \lambda_ {l} \int_ {\mathbb {R} ^ {2}} \left(1 - \frac {1}{1 + u P _ {l} \| x \| ^ {- \alpha}}\right) d \| x \|\right) \\ = \exp \left(- 2 \pi \frac {\delta^ {\frac {2}{\alpha}}}{\alpha} \left(1 - \tau_ {l}\right) \lambda_ {l} B \left(\frac {2}{\alpha}, 1 - \frac {2}{\alpha}\right) z ^ {2}\right), \tag {29} \\ \end{array}
$$

where  $(a)$  is based on the independence of channel fading, while  $(b)$  follows from  $\mathbb{E}\left(\prod_{x}v(x)\right) = \exp \left(-\lambda \int_{\mathbb{R}^2}\left(1 - v(x)\right)\mathrm{d}x\right)$ , where  $x\in \Phi$  and  $\Phi$  is an PPP in  $\mathbb{R}^2$  with the intensity  $\lambda$  [25].

Furthermore, since the interference  $I_{2}$  is imposed by the SBSs outside the circle with radius  $z$ . Then we arrive at

$$
\begin{array}{l} \mathbb {E} _ {I _ {2}} \left(\exp (- u I _ {2})\right) \\ = \mathbb {E} _ {\Phi_ {l}} \left(\prod_ {x \in \Phi_ {l} ^ {\prime} \backslash x _ {Z}} \int_ {0} ^ {\infty} \exp \left(- u P _ {l} h _ {x} \| x \| ^ {- \alpha}\right) \exp (- h _ {x}) d h _ {x}\right) \\ \end{array}
$$

$$
\begin{array}{l} = \mathbb {E} _ {\Phi_ {l}} \left(\prod_ {x \in \Phi_ {l} ^ {\prime} \backslash x _ {\mathrm {Z}}} \frac {1}{1 + z ^ {\alpha} \delta \| x \| ^ {- \alpha}}\right) \\ = \exp \left(- \tau_ {l} \lambda_ {l} \int_ {z} ^ {\infty} 2 \pi \left(1 - \frac {1}{1 + z ^ {\alpha} \delta r ^ {- \alpha}}\right) r d r\right) \\ = \exp \left(- 2 \pi \frac {\delta}{\alpha - 2} \tau_ {l} \lambda F _ {1} \left(1, 1 - \frac {2}{\alpha}; 2 - \frac {2}{\alpha}; - \delta\right) z ^ {2}\right). \tag {30} \\ \end{array}
$$

Based on Eqs. (29) and (30), we obtain  $\mathbb{E}_I(\exp (-uI))$  in Eq. (28). We further substitute Eq. (28) into (25). According to the definitions of the functions  $A(\delta, \alpha)$  and  $C(\delta, \alpha)$ , we have

$$
\begin{array}{l} \Pr (\rho (x _ {Z}) \geq \delta) = \pi \tau_ {l} \lambda_ {l} \int_ {0} ^ {\infty} \exp \left(- \pi (1 - \tau_ {l}) \lambda_ {l} C (\delta , \alpha) z ^ {2}\right) \\ \exp \left(- \pi \tau_ {l} \lambda_ {l} A (\delta , \alpha) z ^ {2}\right) \exp (- u \sigma^ {2}) \exp \left(- \pi \tau_ {l} \lambda_ {l} z ^ {2}\right) d z ^ {2}. \tag {31} \\ \end{array}
$$

This completes the proof.

# APPENDIX B

# PROOF OF COROLLARY 1

In the case that  $\frac{\sigma^2}{P_l}$  goes to zero, we have

$$
\lim  _ {\frac {\sigma^ {2}}{P _ {l}} \rightarrow 0} \exp \left(- \frac {z ^ {\alpha} \delta \sigma^ {2}}{P _ {l}}\right) = 1. \tag {32}
$$

Then we rewrite Eq. (3) when  $f \leq Q_{l}$  as

$$
\begin{array}{l} \lim  \Pr (\mathcal {E} _ {l, f}) \\ \frac {\sigma^ {2}}{P _ {l}} \rightarrow 0 \\ = \int_ {0} ^ {\infty} \exp \left(- \pi (1 - \tau_ {l}) \lambda_ {l} C (\delta , \alpha) z ^ {2}\right) \\ \exp \left(- \pi \tau_ {l} \lambda_ {l} A (\delta , \alpha) z ^ {2}\right) \pi \tau_ {l} \lambda_ {l} \exp \left(- \pi \tau_ {l} \lambda_ {l} z ^ {2}\right) d z ^ {2} \\ = \frac {\tau_ {l}}{\left(1 - \tau_ {l}\right) C (\delta , \alpha) + \tau_ {l} A (\delta , \alpha) + \tau_ {l}}. \tag {33} \\ \end{array}
$$

This completes the proof.

# APPENDIX C

# PROOF OF LEMMA 2

The optimum solution  $s_l^\star$  can be obtained by deriving  $S_l^{NSP}$  with respect to  $s_l$  and solving  $\frac{\mathrm{d}S_l^{NSP}}{\mathrm{d}s_l} = 0$ . We have

$$
\begin{array}{l} \frac {\partial S _ {l} ^ {N S P}}{\partial s _ {l}} = \frac {\lambda_ {l}}{A (\delta , \alpha) - C (\delta , \alpha) + 1} \\ \left(\sqrt {\frac {K s C (\delta , \alpha) \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l} s _ {l}}} - C (\delta , \alpha)\right. \\ \left. - \frac {1}{2} \left(s _ {l} - c _ {l}\right) \sqrt {\frac {K s C (\delta , \alpha) \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l}}} s _ {l} ^ {- \frac {3}{2}}\right). \tag {34} \\ \end{array}
$$

Since we have  $U_{l} = \sqrt{\frac{KsC(\delta,\alpha)\zeta_{l}\sum_{f = 1}^{Q_{l}}q_{f}}{\lambda_{l}}}$ , we shall obtain  $s_l^\star$  from solving the following equation:

$$
s _ {l} ^ {- \frac {3}{2}} + \frac {1}{c _ {l}} s _ {l} ^ {- \frac {1}{2}} - \frac {2 C (\delta , \alpha)}{c _ {l} U _ {l}} = 0. \tag {35}
$$

Let  $s_l^{-\frac{1}{2}} = x^{\frac{1}{3}} - \frac{1}{3c_l} x^{-\frac{1}{3}}$ , and Eq. (35) can be converted to

$$
x ^ {2} - \frac {2 C (\delta , \alpha)}{c _ {l} U _ {l}} x - \frac {1}{2 7 c _ {l} ^ {3}} = 0. \tag {36}
$$

Adopt the positive  $x$ , and we arrive at

$$
x = \frac {C (\delta , \alpha)}{c _ {l} U _ {l}} + \sqrt {\left(\frac {C (\delta , \alpha)}{c _ {l} U _ {l}}\right) ^ {2} + \frac {1}{2 7 c _ {l} ^ {3}}}. \tag {37}
$$

Substitute  $x$  to  $s_l^{-\frac{1}{2}} = x^{\frac{1}{3}} - \frac{1}{3c_l} x^{-\frac{1}{3}}$ , we obtain the optimum  $s_l$ . Also, since there is

$$
\begin{array}{l} \frac {\partial^ {2} S _ {l} ^ {N S P}}{\partial s _ {l} ^ {2}} = \frac {\lambda_ {l}}{A (\delta , \alpha) - C (\delta , \alpha) + 1} \\ \times \left(- \frac {3}{4} c _ {l} u _ {l} s _ {l} ^ {- \frac {5}{2}} - \frac {1}{4} u _ {l} s _ {l} ^ {- \frac {3}{2}}\right) <   0, \tag {38} \\ \end{array}
$$

the function  $S_{l}^{NSP}$  is a concave function of  $s_{l}$ . There exists a unique optimum price  $s_{l}^{\star}$  that maximizes  $S_{l}^{NSP}$ . Furthermore, in the case of  $s_{l}^{\star} < s_{l}^{lower}$  which leads to  $\tau_{l} > 1$ , we adopt  $s_{l}^{\star} = s_{l}^{lower}$  to ensure  $\tau_{l} = 1$ . This completes the proof.

# APPENDIX D

# PROOF OF THEOREM 2

We obtain the optimum solution by proposing a modified water-filling algorithm with extra constraints. First, we rewrite Problem 2 as

$$
\begin{array}{l} \max  \sum_ {l = 1} ^ {L} \frac {K s \zeta_ {l} \tau_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{(1 - \tau_ {l}) C (\delta , \alpha) + \tau_ {l} A (\delta , \alpha) + \tau_ {l}} - \sum_ {l = 1} ^ {L} \tau_ {l} \lambda_ {l} s _ {l} \\ s. t. ① \sum_ {l = 1} ^ {L} \tau_ {l} \lambda_ {l} s _ {l} \leq S, \quad ② \tau_ {l} \geq 0, \quad ③ \tau_ {l} \leq 1, \quad \forall l. \tag {39} \\ \end{array}
$$

Note that 1 and 2 are the traditional constrains for waterfilling principle, while the constraints in 3 are particular to our model. Using the Lagrangian function

$$
\begin{array}{l} \mathbb {L} (\boldsymbol {\tau}, \boldsymbol {\mu}, \boldsymbol {v}, \kappa) = - \sum_ {l = 1} ^ {L} \left(\frac {K s \zeta_ {l} \tau_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{(1 - \tau_ {l}) C (\delta , \alpha) + \tau_ {l} A (\delta , \alpha) + \tau_ {l}} \right. \\ \left. - \tau_ {l} \lambda_ {l} s _ {l} + \mu_ {l} \tau_ {l} - v _ {l} \tau_ {l} - \xi \tau_ {l} \lambda_ {l} s _ {l}\right), \tag {40} \\ \end{array}
$$

where  $\pmb{\mu} \triangleq [\mu_1, \dots, \mu_L]$ ,  $\pmb{v} \triangleq [\nu_1, \dots, \nu_L]$ , and  $\xi$  are the Lagrangian multipliers. We obtain the necessary and sufficient Karush-Kuhn-Tucker (KKT) conditions as

$$
\begin{array}{l} \frac {\partial \mathbb {L} (\boldsymbol {\tau} , \boldsymbol {\mu} , \boldsymbol {v} , \kappa)}{\partial \tau_ {l}} = 0, \\ \mu_ {l} \geq 0, \\ \mu_ {l} \tau_ {l} = 0, \\ v _ {l} \geq 0, \\ v _ {l} \left(\tau_ {l} - 1\right) = 0, \quad \forall l. \tag {41} \\ \end{array}
$$

The condition  $\mu_l\tau_l = 0$  results in  $\tau_{l} = 0$  or

$$
\tau_ {l} = \frac {\left(\sqrt {\frac {K s C (\delta , \alpha) \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l} s _ {l} (1 + \xi) + v _ {l}}} - C (\delta , \alpha)\right)}{A (\delta , \alpha) - C (\delta , \alpha) + 1}, \tag {42}
$$

while the condition  $\nu_{l}(\tau_{l} - 1) = 0$  results in  $\tau_{l} = 1$  or

$$
\tau_ {l} = \frac {\left(\sqrt {\frac {K s C (\delta , \alpha) \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l} s _ {l} (1 + \xi) - \mu_ {l}}} - C (\delta , \alpha)\right)}{A (\delta , \alpha) - C (\delta , \alpha) + 1}. \tag {43}
$$

Then we arrive at

$$
\tau_ {l} = \left\{ \begin{array}{l l} 0 & \xi > \frac {K s \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l} s _ {l} C (\delta , \alpha)} - 1, \\ 1 & \xi <   \frac {K s C (\delta , \alpha) \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l} s _ {l} (A (\delta , \alpha) + 1) ^ {2}} - 1, \\ \frac {\sqrt {\frac {K s C (\delta , \alpha) \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l} s _ {l} (1 + \xi)}} - C (\delta , \alpha)}{A (\delta , \alpha) - C (\delta , \alpha) + 1} & \text {o t h e r w i s e}, \end{array} \right. \tag {44}
$$

Finally, the unknown variable  $\xi$  is chosen such that the constraint  $\sum_{l=1}^{L} \tau_l \lambda_l s_l \leq S$  is fulfilled. In the case  $\xi = 0$ , which means  $\sum_{l=1}^{L} \tau_l \lambda_l s_l < S$ , the problem degrades to that in Section V, i.e.,  $S$  is sufficiently large such that this constraint can be neglected.

In the case  $\xi > 0$ , which means  $\sum_{l=1}^{L} \tau_l \lambda_l s_l = S$ , we first consider the two sets  $S_1$  and  $S_2$ . For  $S_1$ , we have  $\tau_l = 1$ ,  $\forall l \in S_1$ . For  $S_2$ , we have  $0 < \tau_l < 1$ ,  $\forall l \in S_2$ . Then we arrive at

$$
\xi = \left(\frac {\sum_ {j \in \mathcal {S} _ {2}} \sqrt {K s C (\delta , \alpha) \lambda_ {j} s _ {j} \zeta_ {j} \sum_ {f = 1} ^ {Q _ {j}} q _ {f}}}{(A - C + 1) (S - \sum_ {j \in \mathcal {S} _ {1}} \lambda_ {j} s _ {j}) + \sum_ {j \in \mathcal {S} _ {2}} \lambda_ {j} s _ {j} C (\delta , \alpha)}\right) ^ {2} - 1, \tag {45}
$$

Note that the sets  $S_{1}$  and  $S_{2}$  are determined such that

$$
\frac {K s C (\delta , \alpha) \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l} s _ {l} (A (\delta , \alpha) + 1) ^ {2}} - 1 <   \xi <   \frac {K s \zeta_ {l} \sum_ {f = 1} ^ {Q _ {l}} q _ {f}}{\lambda_ {l} s _ {l} C (\delta , \alpha)} - 1. \tag {46}
$$

This completes the proof.

# REFERENCES

[1] N. Golrezaei, A. F. Molisch, A. G. Dimakis, and G. Caire, "Femtocaching and device-to-device collaboration: A new architecture for wireless video distribution," IEEE Commun. Mag., vol. 51, no. 4, pp. 142-149, Apr. 2013.  
[2] E. Bastug, M. Bennis, and M. Debbah, “Living on the edge: The role of proactive caching in 5G wireless networks,” IEEE Commun. Mag., vol. 52, no. 8, pp. 82–89, Aug. 2014.  
[3] M. Deghel, E. Bastug, M. Assaad, and M. Debbah, "On the benefits of edge caching for MIMO interference alignment," in Proc. IEEE 16th Int. Workshop Signal Process. Adv. Wireless Commun. (SPAWC), Jun. 2015, pp. 655-659.  
[4] J. Zhang, F. Engelmann, and P. Elia, "Coded caching for reducing CSIT feedback in wireless communications," in Proc. 53rd Annu. Allerton Conf. Commun., Control, Comput. (Allerton), Sep. 2015, pp. 1099-1105.  
[5] X. Wang, M. Chen, T. Taleb, A. Ksentini, and V. C. M. Leung, "Cache in the air: Exploiting content caching and delivery techniques for 5G systems," IEEE Commun. Mag., vol. 52, no. 2, pp. 131-139, Feb. 2014.  
[6] M. A. Maddah-Ali and U. Niesen, "Decentralized coded caching attains order-optimal memory-rate tradeoff," in Proc. 51st Annu. Allerton Conf. Commun., Control, Comput. (Allerton), Oct. 2013, pp. 421-427.  
[7] N. Golrezaei, P. Mansourifard, A. F. Molisch, and A. G. Dimakis, “Base-station assisted device-to-device communications for high-throughput wireless video networks,” IEEE Trans. Wireless Commun., vol. 13, no. 7, pp. 3665–3676, Jul. 2014.  
[8] M. Ji, G. Caire, and A. F. Molisch, "Wireless device-to-device caching networks: Basic principles and system performance," IEEE J. Sel. Areas Commun., vol. 34, no. 1, pp. 176-189, Jan. 2016.  
[9] M. Ji, G. Caire, and A. F. Molisch, “Optimal throughput-outage tradeoff in wireless one-hop caching networks,” in Proc. IEEE Int. Symp. Inf. Theory (ISIT), Jul. 2013, pp. 1461–1465.  
[10] P. Gupta and P. R. Kumar, “The capacity of wireless networks,” IEEE Trans. Inf. Theory, vol. 46, no. 2, pp. 388–404, Mar. 2000.  
[11] F. Boccardi, R. W. Heath, A. Lozano, T. L. Marzetta, and P. Popovski, “Five disruptive technology directions for 5G,” IEEE Commun. Mag., vol. 52, no. 2, pp. 74–80, Feb. 2014.  
[12] A. Damnjanovic et al., “A survey on 3GPP heterogeneous networks,” IEEE Wireless Commun., vol. 18, no. 3, pp. 10–21, Jun. 2011.  
[13] J. Akhtman and L. Hanzo, “Heterogeneous networking: An enabling paradigm for ubiquitous wireless communications,” Proc. IEEE, vol. 98, no. 2, pp. 135–138, Feb. 2010.  
[14] S. Bayat, R. H. Y. Louie, Z. Han, B. Vucetic, and Y. Li, "Distributed user association and femtocell allocation in heterogeneous wireless networks," IEEE Trans. Commun., vol. 62, no. 8, pp. 3027-3043, Aug. 2014.  
[15] M. Mirahmadi, A. Al-Dweik, and A. Shami, "Interference modeling and performance evaluation of heterogeneous cellular networks," IEEE Trans. Commun., vol. 62, no. 6, pp. 2132-2144, Jun. 2014.  
[16] A. K. Gupta, H. Dhillon, S. Vishwanath, and J. Andrews, "Downlink multi-antenna heterogeneous cellular network with load balancing," IEEE Trans. Commun., vol. 62, no. 11, pp. 4052-4067, Nov. 2014.  
[17] M. Liebsch, S. Schmid, and J. Awano, “Reducing backhaul costs for mobile content delivery—An analytical study,” in Proc. IEEE Int. Conf. Commun. (ICC), Jun. 2012, pp. 2895–2900.  
[18] K. Shanmugam, N. Golrezaei, A. G. Dimakis, A. F. Molisch, and G. Caire, “FemtoCaching: Wireless content delivery through distributed caching helpers,” IEEE Trans. Inf. Theory, vol. 59, no. 12, pp. 8402–8413, Dec. 2013.  
[19] E. Bastug, M. Bennis, and M. Debbah, "Cache-enabled small cell networks: Modeling and tradeoffs," in Proc. 11th Int. Symp. Wireless Commun. Syst. (ISWCS), Aug. 2014, pp. 649-653.  
[20] D. Stoyan, W. Kendall, and M. Mecke, Stochastic Geometry and Its Applications, 2nd ed. New York, NY, USA: Wiley, 2003.  
[21] M. Haenggi, J. G. Andrews, F. Baccelli, O. Dousse, and M. Franceschetti, "Stochastic geometry and random graphs for the analysis and design of wireless networks," IEEE J. Sel. Areas Commun., vol. 27, no. 7, pp. 1029-1046, Sep. 2009.  
[22] X. Kang, R. Zhang, and M. Motani, “Price-based resource allocation for spectrum-sharing femtocell networks: A Stackelberg game approach,” IEEE J. Sel. Areas Commun., vol. 30, no. 3, pp. 538–549, Apr. 2012.  
[23] B. Wang, Z. Han, and K. J. R. Liu, "Distributed relay selection and power control for multiuser cooperative communication networks using Stackelberg game," IEEE Trans. Mobile Comput., vol. 8, no. 7, pp. 975-990, Jul. 2009.

[24] D. Fudenberg and J. Tirole, Game Theory. Cambridge, MA, USA: MIT Press, 1993.  
[25] D. J. Daley and D. Vere-Jones, An Introduction to the Theory of Point Processes: Elementary Theory and Methods, vol. 1. New York, NY, USA: Springer, 1996.  
[26] M. Cha, H. Kwak, P. Rodriguez, Y.-Y. Ahn, and S. Moon, "I tube, you tube, everybody tubes: Analyzing the world's largest user generated content video system," in Proc. 7th ACM SIGCOMM Conf. Internet Meas., 2007, pp. 1-14.

![](images/a2d5071a62b00a2f7a55f1bc1d98d6e959d815e28f15a5938d267158ab81c18f.jpg)

JUN LI (M'09-SM'16) received the Ph.D. degree in electronics engineering from Shanghai Jiao Tong University, Shanghai, China, in 2009. From 2009 to 2009, he was with the Department of Research and Innovation, Alcatel Lucent Shanghai Bell, as a Research Scientist. From 2009 to 2012, he was a Post-Doctoral Fellow with the School of Electrical Engineering and Telecommunications, University of New South Wales, Australia. From 2012 to 2015, he is currently a Researchbreak

Fellow with the School of Electrical Engineering, the University of Sydney, Australia. Since 2015, he has been a Professor with the School of Electronic and Optical Engineering, Nanjing University of Science and Technology, Nanjing, China. His research interests include network information theory, channel coding theory, wireless network coding, and resource allocations in cellular networks.

![](images/05f433914e56332c4d81ef499c0270d5591309758f8bb695744448166d9de984.jpg)

JINSHAN SUN received the B.S. degree in electronic science and technology from the Nanjing University of Science and Technology, Nanjing, China, in 2014, where she is currently pursuing the M.S. degree in electronic and communication engineering. Her current research interests include opportunistic scheduling in PLC and wireless caching strategy in heterogeneous cellular network.

![](images/066c7bbfee1bfcb22e1a2fead410a731ef95461d07669572c3c9d58fdd0f965b.jpg)

YUWEN QIAN received the Ph.D. degree in automatic engineering from the Nanjing University of Science and Technology, Nanjing, China, in 2011. From 2002 to 2011, he was a Lecturer with the Automation School, Nanjing University of Science and Technology. Since 2011, he has been a Lecturer with the School of Electronic and Optical Engineering, Nanjing University of Science and Technology. His main research interests are information security, smart grid, and power line

communications.

![](images/2f0518f3a8d6356f757b69fc48d0153fd457daf6a66eb0f15c11f52119d839d5.jpg)

FENG SHU was born in 1973. He received the B.S. degree from Fuyang teaching College, Fuyang, China, in 1994, the M.S. degree from Southeast University, Nanjing, in 2002, and the Ph.D. degree from Xidian University, Xi'an, China, in 1997. From 2009 to 2010, he held a visiting post-doctoral position with the University of Texas at Dallas. In 2005, he joined the School of Electronic and Optical Engineering, Nanjing University of Science and Technology, Nanjing,

China, where he is currently a Professor and a Supervisor of Ph.D. and graduate students. He is also with Fujian Agriculture and Forestry University and awarded with the Mingjian Scholar Chair Professor in Fujian Province. His research interests include wireless networks, wireless location, and array signal processing. He has authored over 200 papers, of which more than 80 are in archival journals including 14 papers in the IEEE Journals and 35 SCI-indexed papers. He holds two Chinese patents.

![](images/a9c57e9133d8a6461d90640569e764ed06e08c71c01cf23c26e741a9309c1b68.jpg)

MING XIAO (S'02-M'07-SM'12) received the bachelor's and master's degrees in engineering from the University of Electronic Science and Technology of China, Chengdu, in 1997 and 2002, respectively, and the Ph.D. degree from the Chalmers University of Technology, Sweden, in 2007. From 1997 to 1999, he was as a Network and Software Engineer in ChinaTelecom. From 2000 to 2002, he also held a position with the Sichuan Communications Administration.

Since 2007, he has been with Communication Theory, School of Electrical engineering, Royal Institute of Technology, Sweden, where he is currently an Associate Professor with Communications Theory. He received the best paper awards in the International Conference on Wireless Communications and Signal Processing in 2010 and the IEEE International Conference on Computer Communication Networks in 2011. He received the Chinese Government Award for Outstanding Self-Financed Students Studying Abroad in 2007. He got the Hans Werthen Grant from the Royal Swedish Academy of engineering science (IVA) in 2006. He received Ericsson Research Funding from Ericsson in 2010. Since 2012, he has been an Associate Editor of the IEEE TRANSACTIONS on COMMUNICATIONS, the IEEE COMMUNICATIONS LETTERS (Senior Editor Since 2015) and the IEEE WIRELESS COMMUNICATIONS LETTERS.

![](images/e542005bed83305aa00bdaca69d37dc415d262d2ce353f135b1d6448e7329342.jpg)

WEI XIANG (S'00-M'04-SM'10) received the B.Eng. and M.Eng. degrees in electronic engineering from the University of Electronic Science and Technology of China, Chengdu, China, in 1997 and 2000, respectively, and the Ph.D. degree in telecommunications engineering from the University of South Australia, Adelaide, Australia, in 2004. He is currently the Foundation Professor and the Head of Discipline Internet of Things Engineering with the College of Science and Engi

neering, James Cook University, Cairns, Australia. From 2004 to 2015, he was with the School of Mechanical and Electrical Engineering, University of Southern Queensland, Toowoomba, Australia. He is an IET Fellow, a fellow of Engineers Australia, and an Editor of the IEEE COMMUNICATIONS LETTERS. He was a co-recipient of three best paper awards at the 2015 WCSP, the 2011 IEEE WCNC, and the 2009 ICwMC. He has been awarded several prestigious fellowship titles. He was named a Queensland International Fellow (2010-2011) by the Queensland Government of Australia, an Endeavour Research Fellow (2012-2013) by the Commonwealth Government of Australia, a Smart Futures Fellow (2012-2015) by the Queensland Government of Australia, and a JSPS Invitational Fellow by the Australian Academy of Science and Japanese Society for Promotion of Science (2014-2015). In 2008, he was a Visiting Scholar with Nanyang Technological University, Singapore. From 2010 to 2011, he was a Visiting Scholar with the University of Mississippi, Oxford, MS, USA. From 2012 to 2013, he was an Endeavour Visiting Associate Professor with the University of Hong Kong. He has authored over 160 papers in peer-reviewed journal and conference papers. His research interests are in the broad area of communications and information theory, particularly coding and signal processing for multimedia communications systems.