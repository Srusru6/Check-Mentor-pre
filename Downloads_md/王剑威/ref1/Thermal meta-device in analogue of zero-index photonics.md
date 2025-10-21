# Thermal meta-device in analogue of zero-index photonics

Ying Li $^{1,8}$ , Ke-Jia Zhu $^{1,2,8}$ , Yu-Gui Peng $^{1,3,8}$ , Wei Li $^{4}$ , Tianzhi Yang $^{5,6}$ , He-Xiu Xu $^{1,7}$ , Hong Chen $^{2}$ , Xue-Feng Zhu $^{3}$ , Shanhui Fan $^{4*}$  and C.-W. Qiu $^{1*}$

Inspired by the developments in photonic metamaterials, the concept of thermal metamaterials has promised new avenues for manipulating the flow of heat. In photonics, the existence of natural materials with both positive and negative permittivities has enabled the creation of metamaterials with a very wide range of effective parameters. In contrast, in conductive heat transfer, the available range of thermal conductivities in natural materials is far narrower, strongly restricting the effective parameters of thermal metamaterials and limiting possible applications in extreme environments. Here, we identify a rigorous correspondence between zero index in Maxwell's equations and infinite thermal conductivity in Fourier's law. We also propose a conductive system with an integrated convective element that creates an extreme effective thermal conductivity, and hence by correspondence a thermal analogue of photonic near-zero-index metamaterials, a class of metamaterials with crucial importance in controlling light. Synergizing the general properties of zero-index metamaterials and the specific diffusive nature of thermal conduction, we theoretically and experimentally demonstrate a thermal zero-index cloak. In contrast with conventional thermal cloaks, this meta-device can operate in a highly conductive background and the cloaked object preserves great sensitivity to external temperature changes. Our work demonstrates a thermal metamaterial which greatly enhances the capability for molding the flow of heat.

In recent years, great interest has been focused on the manipulation of heat $^{1}$ , as a novel approach to harvest energy $^{2}$  or a new medium to transfer and process information $^{3}$ . A major impetus behind this is the emerging field of thermal metamaterials $^{4-11}$  inspired by their successful counterparts in photonics $^{12}$ . Thermal metamaterials have the capability to achieve unusual temperature profiles for given boundary conditions. A remarkable example being the demonstration of a thermal cloak $^{4,5}$ , which effectively achieves the thermal version of invisibility and inspires many other thermal management functions $^{3,11,13}$ . The capability of thermal metamaterials arises from the ability to engineer a specific anisotropy or spatial distributions of effective thermal conductivity in a given device $^{6-11}$ . However, in practice, the capability of thermal metamaterials is severely limited by the narrow range of effective thermal conductivities that can be engineered. Thermal metamaterials need to be constructed from naturally existing materials. In practice, commonly used materials for this purpose have thermal conductivities ranging from  $0.03 \, \text{W} \, \text{m}^{-1} \, \text{K}^{-1}$  (plastic foam or air) to  $400 \, \text{W} \, \text{m}^{-1} \, \text{K}^{-1}$  (copper). Other values or any anisotropy of effective thermal conductivity must then be achieved through the combination of different materials based on the effective-medium approximation $^{7}$ . However, the effective parameter cannot exceed the range of natural materials, since it is an average over its constituents. Despite recent efforts using temperature-dependent $^{13}$  or multi-physical $^{14}$  effects to extend this field, the fundamental parameter space of effective thermal conductivities in thermal metamaterials remains highly restricted. This is in contrast to photonic metamaterials, where a much wide range of effective permittivities and permeabilities has been constructed $^{15,16}$ , resulting

in a much richer set of fundamental phenomena and engineering capabilities.

As a specific example of a class of photonic metamaterials whose thermal analogue has not been proposed and demonstrated, we consider zero-index metamaterials $^{15}$ , which have found wide applications in photonics ranging from guiding light through arbitrary channels $^{17-21}$ , enhancement of nonlinear effects $^{22}$ , to manipulation of thermal emission $^{23}$ . In photonics, there are naturally occurring materials with zero index $^{24}$ . Moreover, effective zero-index metamaterials can be achieved with dielectric photonic crystals $^{25,26}$  or by combining materials with positive and negative permittivity $^{27}$ . However, neither zero nor negative index has a natural analogue in heat conduction.

In this paper, we prove an exact equivalence between a zero index  $(n\to 0)$  in photonics and an infinite thermal conductivity  $(\kappa \rightarrow \infty)$  in heat transfer. We also show that an effective thermal conductivity that is far higher than that of typical solid-state materials can be achieved by integrating a convective element in a thermal conductive system. Convective heat transfer is the most efficient and widely used method for traditional cooling or heating purposes. The difficulty in using convective heat transfer in the field of thermal metamaterials is partly due to the incompatibility of the typical aim in applications of thermal metamaterials to achieve a precise temperature distribution, and the complexity of the details of the fluid field. Here, we study a hybrid system of a solid conductor embedded with circulating fluid. We theoretically prove the equivalence between the integrated high-speed fluid field and a thermal near-zero-index material, insensitive to details of the fluid fields. As a

![](images/e3cd6b7f3b111251b1fe8f0cad4e878781635439a90b957748244f94f0be7a98.jpg)  
a

![](images/0c47f9a31503d9a4148a6cfa12555f9fff25c3567d2a66298c2475c04d5a9b59.jpg)  
b

![](images/7cb24bfecde104d970d01d2438a529ac5e83c54e521f8fe993afa5646c189053.jpg)

![](images/79e7777f8a8d0e417c88f75d21af183f02d8ddca9eae6af0aa7ab3229c31b23e.jpg)  
d

![](images/b0a17a415423d84e43a0c5712579cab616e1b955751610c5e76dec8787a4fcb4.jpg)  
Fig. 1 | The origin of thermal NZIM and its effect in thermal cloaking. a, Top, electromagnetic wave (blue line) transported through a NZIM (A). (Bottom) heat conduction (blue line represents temperature) through an infinite-conductivity material (A). The correspondence between  $\varepsilon^{-1}(\mu^{-1})$  and  $\kappa$  is obvious under the mapping from E (H) to  $T$ , both uniform across region A. b, A bilayer thermal cloak in a copper background (left and right sides at constant temperatures  $T_{\mathrm{L}}$  and  $T_{\mathrm{R}}$ ). The outer layer should be much more conductive than copper. c, With silver the most conductive common material, bilayer thermal cloaking is not realizable in the shaded region. d, A thermal zero-index cloak has an inner layer with extreme effective thermal conductivity achieved through heat convection (dark blue arrows represent fluid motion). With a suitable outer layer that is less conductive than copper, the cloaking effect can be achieved and is realizable with common materials.

demonstration, the concept of a thermal zero-index cloak is proposed and designed. The meta-device constitutes an easily realizable structure with high tunability. Its performance is confirmed numerically and experimentally, showing a high sensitivity that is lacking in traditional devices.

# Origin and effects of thermal near-zero-index materials

First, recall the frequency-domain wave equation in a source-free matter:  $(\nabla^{2} + \mu \varepsilon \omega^{2})[\mathbf{E}\mathbf{H}]^{\mathrm{T}} = 0$  where  $\omega$  is the angular frequency,  $\varepsilon$  and  $\mu$  are the permittivity and permeability of the material, and  $\mathbf{E}$  and  $\mathbf{H}$  are the electric and magnetic fields, respectively. This Helmholtz equation has a form similar to that of the Fourier-transformed heat conduction equation  $(\nabla^{2} - i\omega \rho c_{p} / \kappa)T = 0$  where  $\rho$  is density,  $c_{p}$  is the heat capacity at constant pressure and  $T$  is the temperature. In the limit of  $n = c.\sqrt{\mu\varepsilon}\rightarrow 0$  ( $c$  is the speed of light in vacuum, we focus on the case where  $\varepsilon$  and  $\mu$  are both near zero) and  $\rho c_{p} / \kappa \rightarrow 0$  both equations reduce to the same Laplacian equation  $\nabla^2 [\mathbf{E}\mathbf{H}]^{\mathrm{T}} = 0$  ( $\nabla^2 T = 0$ ). It seems that both  $\rho c_{p}\rightarrow 0$  and  $\kappa \rightarrow \infty$  correspond to near-zero index, but we should further consider the matching condition at an interface between a near-zero index metamaterial (NZIM) (A) and an ordinary material (B), as shown in Fig. 1a. In photonics, since the incident and outcoming waves are always normal to the interface,  $\mathbf{E}$  and  $\mathbf{H}$  should be parallel to the interface and satisfy  $[\mathbf{E}^{\mathrm{A}}\mathbf{H}^{\mathrm{A}}] = [\mathbf{E}^{\mathrm{B}}\mathbf{H}^{\mathrm{B}}]$ . According to the Maxwell equation, the matching condition for  $\mathbf{H}$  can be written as  $-(i\omega \mu_{\mathrm{A}})^{-1}(\nabla \times \mathbf{E})^{\mathrm{A}} = -(i\omega \mu_{\mathrm{B}})^{-1}(\nabla \times \mathbf{E})^{\mathrm{B}}$ , which is

further simplified to  $\mathbf{n} \cdot \mu_{\mathrm{A}}^{-1}(\nabla \mathbf{E})^{\mathrm{A}} = \mathbf{n} \cdot \mu_{\mathrm{B}}^{-1}(\nabla \mathbf{E})^{\mathrm{B}}$  with  $\mathbf{n}$  the normal vector of the interface. The same argument applied to  $\mathbf{E}$  gives  $\mathbf{n} \cdot \varepsilon_{\mathrm{A}}^{-1}(\nabla \mathbf{H})^{\mathrm{A}} = \mathbf{n} \cdot \varepsilon_{\mathrm{B}}^{-1}(\nabla \mathbf{H})^{\mathrm{B}}$ . For heat conduction across the interface, both the temperature and the normal heat flux should match:  $T^{\mathrm{A}} = T^{\mathrm{B}}$ ,  $\mathbf{n} \cdot \kappa_{\mathrm{A}}(\nabla T)^{\mathrm{A}} = \mathbf{n} \cdot \kappa_{\mathrm{B}}(\nabla T)^{\mathrm{B}}$ . Hence, we confirm the correspondence between  $n \to 0$  and  $\kappa \to \infty$ . Inside the NZIM there is a uniform field according to the Maxwell equation ( $\nabla \times \mathbf{E})^{\mathrm{A}} = i\omega \mu_{\mathrm{A}}\mathbf{H}^{\mathrm{A}} = 0$ ,  $(\nabla \times \mathbf{H})^{\mathrm{A}} = i\omega \varepsilon_{\mathrm{A}}\mathbf{E}^{\mathrm{A}} = 0$ , which leads to the tunnelling effect of a zero phase difference across the region. Similarly, the finite heat flux  $\mathbf{q}^{\mathrm{A}}$  ensures a tunnelling of temperature across region A when  $\kappa_{\mathrm{A}} \to \infty$ :  $(\nabla T)^{\mathrm{A}} = \kappa_{\mathrm{A}}^{-1}\mathbf{q}^{\mathrm{A}} = 0$ .

As mentioned above, the conductivity of conventional thermal metamaterials is limited by the effective-medium approximation. A direct consequence is that almost no existing thermal metamaterial concepts can operate in a high-conductivity background. As a typical example, consider a thermal cloak that protects its interior object from being thermally detected by restoring its exterior background temperature profile. The structure of a thermal cloak can be designed according to the transformation theory $^{6-8,28,29}$  or scattering-cancellation method $^{9-11,30}$ . For the former, an infinite anisotropy of  $\kappa$  is theoretically required and can only be approximately realized using alternative layers of thermal conductor and insulator $^{7}$ . The conductivity of the conductive layer should be much larger than that of the background ( $\kappa_{\mathrm{b}}$ ) for a good approximation, but no common bulk material satisfies the condition when the background is copper

with  $\kappa_{\mathrm{b}} = 400\mathrm{Wm}^{-1}\mathrm{K}^{-1}$ . A bilayer cloak based on scattering-cancellation is more practical. It consists simply of two concentric shells (Fig. 1b). The inner layer is a thermal insulator whose conductivity  $\kappa_{2}\rightarrow 0$ . This layer blocks heat flux from entering the interior region, and therefore creates a uniform temperature distribution inside the cloak. Since there is no heat flux or temperature gradient inside the cloak, the temperature profile outside the cloak is not influenced by any interior object. The outer layer of the cloak restores the distortion introduced by the inner layer if its conductivity  $\kappa_{3} = \kappa_{\mathrm{b}}(R_{3}^{2} + R_{2}^{2}) / (R_{3}^{2} - R_{2}^{2})$  in two dimensions (or  $\kappa_{3} = \kappa_{\mathrm{b}}(2R_{3}^{3} + R_{2}^{3}) / 2(R_{3}^{3} - R_{2}^{3})$  in three dimensions). This relation is plotted in Fig. 1c for a ratio  $R_{3} / R_{2} = 1.5$ . For a copper background,  $\kappa_{3} = 1,040\mathrm{Wm}^{-1}\mathrm{K}^{-1}$ , which is far beyond the reach of common materials. On the other hand, taking the conductivity of silver  $(430\mathrm{Wm}^{-1}\mathrm{K}^{-1})$  as the upper limit of  $\kappa_{3}$ , the maximum value of  $\kappa_{\mathrm{b}}$  is only  $165\mathrm{Wm}^{-1}\mathrm{K}^{-1}$ . It means that many common metallic materials (for example, silver, copper and aluminum) have been excluded from the choices of background, as indicated by the shaded region of Fig. 1c.

Using the thermal near-zero-index material, here we develop a thermal cloak. It is well known in photonics that any scatterer inside a NZIM (more strictly, with  $\varepsilon$  and  $\mu$  both near zero) does not affect the outcoming waves $^{18,21}$ . Inspired by this feature, we design the structure as shown in Fig. 1d with  $\kappa_{2} \rightarrow \infty$  (in practice it means  $\kappa_{2} \gg \kappa_{\mathrm{b}}, \kappa_{1}$  and  $\kappa_{3}$ ). It is expected that the temperature profile outside the device will also become independent of the interior object, just like the cases in photonics.

The device also has a substantial advantage over photonic NZIM-based cloaking devices[21]. A common problem of NZIM is the total reflection of any obliquely incident light. As a result, almost all related applications have flat interfaces between the NZIM and its surroundings and use normally incident waves[15]. Since cloaks are expected to function for omnidirectional incidence, it is still challenging to achieve free-space cloaking with the NZIM despite its promising tunnelling effects. The problem is naturally resolved for heat transfer, where the concepts of reflection or dispersion are absent, thanks to its diffusive nature. Just like in photonics, where the outcoming wave from the NZIM will be shaped normal to the interface, the temperature profile will also be deformed according to the shape of the near-zero-index region. However, we will show that the deformation can be easily restored with the outer shell, whose thermal conductivity  $\kappa_{3}$  is found by the scattering-cancellation approach.

The problem is how to achieve such an extreme value of  $\kappa_{2}$ , especially when the background is already a good thermal conductor. We propose that efficient thermal convection can be employed for this purpose. The two-dimensional heat convection equation in fluid is<sup>31</sup>:

$$
\frac {\partial T}{\partial t} = D \nabla^ {2} T - \mathbf {v} (\mathbf {r}) \cdot \nabla T \tag {1}
$$

where  $\mathbf{r}$  is the position vector,  $D = \kappa / (\rho c)$  is the diffusivity and  $\mathbf{v}(\mathbf{r})$  is the velocity field of the fluid. The temperature dependency of  $D$  is ignored for simplicity. To be integrated into certain conductive systems, the fluid field should be closed without a source or a drain. One natural candidate for such a field is the circulating field; thus, we focus on the field  $\nu_{r} = 0$ ,  $\nu_{\theta} = \nu(r)$  in polar coordinates  $(r,\theta)$ . At steady state, equation (1) can be written as:

$$
D \left(\frac {\partial^ {2} T}{\partial r ^ {2}} + \frac {1}{r} \frac {\partial T}{\partial r} + \frac {1}{r ^ {2}} \frac {\partial^ {2} T}{\partial \theta^ {2}}\right) = \frac {\nu (r)}{r} \frac {\partial T}{\partial \theta} \tag {2}
$$

To proceed, consider the entire system in Fig. 1d, where the upper and lower boundaries are thermally insulated, and the left and right boundaries are held at constant temperatures  $T_{\mathrm{L}}$  and  $T_{\mathrm{R}}$ ,

respectively. Now instead of solid material, circulating fluid is placed in region  $R_{1} \leq r \leq R_{2}$  as the inner layer of the cloak. The temperature distribution in this region satisfies equation (2).

It is noticed that when  $\nu (r)\rightarrow \infty$ ,  $\partial T / \partial \theta \to 0$ . Therefore, the temperature distribution preserves rotational symmetry. For any constant  $R$  between  $R_{1}$  and  $R_{2}$ , we can calculate the total heat  $Q_{R}$  generated in the region  $r\leq R$  as:

$$
Q _ {R} = \int_ {0} ^ {2 \pi} \kappa_ {2} \frac {\partial T}{\partial r} \Bigg | _ {r = R} R \mathrm {d} \theta = 2 \pi R \kappa_ {2} \frac {\partial T}{\partial r} \Bigg | _ {r = R} \tag {3}
$$

where  $\kappa_{2}$  is the thermal conductivity of the fluid. In our setting,  $Q_{R}$  should be zero since no heat source is present inside (we ignore viscous heat generation, which is comparably small based on numerical calculations, as explained in Methods and Supplementary Fig. 5). It follows that the radial temperature gradient  $\partial T / \partial r$  should also vanish; thus, the temperature of the inner layer is uniform. This is equivalent to having a solid inner layer with infinitely large conductivity  $\kappa_{2}^{\mathrm{eff}}$ . When assuming a simple distribution of  $\nu(r) = \Omega r$ , it is also possible to obtain an asymptotic solution to equation (2) at the large-speed limit  $\Omega \to \infty$ . According to the solution we found that  $\kappa_{2}^{\mathrm{eff}}$  is proportional to the square root of the Peclet number  $\mathrm{Pe} = \Omega R_{2}^{2} / D$ :

$$
\kappa_ {2} ^ {\text {e f f}} = \frac {R _ {2} ^ {2} + R _ {1} ^ {2}}{R _ {2} ^ {2} - R _ {1} ^ {2}} \kappa_ {2} \sqrt {2 \mathrm {P e}} = \frac {R _ {2} ^ {2} + R _ {1} ^ {2}}{R _ {2} ^ {2} - R _ {1} ^ {2}} \kappa_ {2} R _ {2} \sqrt {2 \Omega / D} \tag {4}
$$

(see Supplementary Note 1 for details). According to the boundary condition, there is no temperature gradient inside the cloak either, regardless of the properties of the cloaked object. The outer layer is then used to restore the temperature distribution outside the cloak. Under the boundary conditions of the system and in the limit of  $\kappa_{2}^{\mathrm{eff}}\rightarrow \infty$ , we have

$$
\kappa_ {3} = \kappa_ {b} \left(R _ {3} ^ {2} - R _ {2} ^ {2}\right) / \left(R _ {3} ^ {2} + R _ {2} ^ {2}\right) \tag {5}
$$

For transient behaviour, in a traditional thermal cloak, heat flux can hardly reach its interior because the conductivity in the radial direction is very low, due to the high anisotropy of a transformational design or the insulating inner layer of a bilayer design. Therefore, the temperature of the cloaked region changes slowly to reach its steady-state value, so it is difficult to keep track of the environmental temperature change from inside the cloak. Looking back at equation (1) suggests that, with a varying thermal environment, a considerably faster temperature change can be expected for the cloaked region in our design, because of the convective term with high fluid speed. Therefore, in contrast to the traditional design, an object inside the cloak can sense the environmental temperature change quickly without exposing itself. The unique property of the device can thus be used for heat/cooling purposes that require high uniformity and minimal influence on the surroundings.

# Numerical demonstration of thermal zero-index cloaking

We first perform steady-state heat convection simulations with COMSOL Multiphysics for the above two-dimensional system with a copper background. The steady-state simulated results are shown in Fig. 2, where for comparison, the results for a bare object (Fig. 2a) and for a traditional bilayer thermal cloak with the same dimensions (Fig. 2b) are also presented. As discussed above, a realizable bilayer cloak will not function in such a high-conductivity background. To illustrate this, we choose silver, the most conductive common material, as the outer layer to observe the best effects a bilayer cloak can actually give. As Fig. 2b shows, such a device still does not present any cloaking effect. The temperature profile is just

![](images/4d8fb87bb363145bec3c4dee37c2c89b743bdcf4d39868292ba8f784b96247bd.jpg)

![](images/622806531c0c040466b979532eb86417b87bfaf932a1f433a3e01547538a6d30.jpg)

![](images/f4130efa2da3ac3a4fd28a0ec506fd07fafae9b8c25ba3267506228132662dad.jpg)  
Fig. 2 | Steady-state temperature profiles. a, A bare object (stainless-steel plate) is put inside a copper background and distorts the profile. b, A traditional bilayer thermal cloak with silver (best available) as the outer layer still cannot function. c, The object is successfully protected by the thermal zero-index cloak, where the inner layer is a channel filled with water circulating through the object at angular speed  $\Omega$ , which is the thermal analogue of a NZIM. Cloaking is achieved through the combined NZIM tunnelling effect and the complementary outer layer of normal material. d, Effective thermal conductivity of the fluid layer at different fluid rotation speeds (blue squares), with the analytical asymptotic relation (blue curve) as in equation (4), as well as the relative deviation of the temperature profile (black circles).

![](images/4066771510d60e0407c4ca327752296d6d13c21d990b4a86612cdaede10cac09.jpg)

like that surrounding the bare object in Fig. 2a with large distortion. The reason is that the conductivity of silver  $(430\mathrm{Wm}^{-1}\mathrm{K}^{-1})$  is still far from the required conductivity  $(1040\mathrm{Wm}^{-1}\mathrm{K}^{-1})$  of the outer layer for an ideal bilayer cloak. We also note that it is not practical to realize this large conductivity of the outer layer with convective effects, because of the difficulty in reaching exactly this particular effective value  $(\kappa_{3}^{\mathrm{eff}} = 1040\mathrm{Wm}^{-1}\mathrm{K}^{-1})$  instead of an extreme value which just needs to satisfy  $\kappa_{2}^{\mathrm{eff}}\gg \kappa_{\mathrm{b}}$ . In addition, since this value is not sufficiently larger than the background conductivity, the effective approximation is not accurate enough to ignore the non-reciprocal distortions induced by convection<sup>33</sup> (see Supplementary Fig. 3 for such deviation).

The thermal zero-index cloak (Fig. 2c) performs well in restoring the distorted temperature profile in Fig. 2a. It makes use of the tunnelling effect of the NZIM, which renders a uniform temperature distribution on the fluid field and the object, irrespective of the position, size and shape of the object (see Supplementary Fig. 2 for simulation results with elliptical and square objects). We also present the temperature profile for the device without the outer layer (Supplementary Fig. 1a) and at the 'off' state (Supplementary Fig. 1b). Obviously, the field is strongly distorted when the fluid is moving rapidly but directly contacts the background, or when the fluid is at rest. The isothermal lines perturbed by the near-zero-index region as in Supplementary Fig. 1a are then restored by the outer layer according to equation (3).

Additional simulations were performed to quantitatively determine the effective thermal conductivity  $\kappa_{2}^{\mathrm{eff}}$  of the fluid layer at rotation speed  $\Omega$ . The value is found by minimizing the root-mean-square deviation (RMSD) between the temperature fields outside the zero-index cloak  $(T)$  and when the fluid layer is replaced with solid  $(T^{\mathrm{solid}})$ : RMSD  $(T) = \sqrt{(T^{\mathrm{solid}} - T)^{2}}$ . As plotted in Fig. 2d, the value of  $\kappa_{2}^{\mathrm{eff}}(\Omega)$  thus found is in good agreement with the asymptotic solution of equation (4). A broad range of  $\Omega$  is used to show the accuracy of the effective model over a large parameter range. The deviation shows a peak at small rotation speeds, where the temperature fields cannot be approximated as generated in a pure conductive system because of the convective non-reciprocal effects[33] (see Supplementary Fig. 3 for the temperature fields at various rotation speeds).

Another potential deficiency of the traditional thermal cloaks is that the interior temperature is insensitive to environmental changes, since this region is well insulated. This problem is naturally solved for the thermal zero-index cloak since the inner layer has extreme effective thermal conductivity and the conductivity of the outer layer is of the same level of magnitude as the background. Therefore, the interior region is not thermally separated from the environment. Its temperature will follow the environmental changes. To illustrate this effect, we perform transient heat transfer simulations for the same three models as used for steady-state simulations. The snapshots of their temperature profiles taken at  $t = 500$  s

![](images/5efc00ce8007ae6a9703acdf3d14d8a8f447742819c4d03ff8058b08aa5875c5.jpg)

![](images/4cbaaa0c2d03c2299ab63978613687d68a40c377571939d390fc91cbc3cf817a.jpg)

![](images/f7835abd42ae1d1a0946ea73cab98c8f3ed869c3c048d18b119a77c42e1499c4.jpg)  
Fig. 3 | Transient temperature profiles at 500 s and the central temperature evolution with time. a, Bare object (a stainless-steel plate). b, Bilayer thermal cloak with silver as the outer layer. c, Thermal zero-index cloak. d, Evolution of the central temperature  $T^*$  (brown dots) with time. The lines are obtained from the simulated results in a-c. The scatter points are obtained from measured infrared images in transient experiments. In contrast with the bilayer cloak, the zero-index cloak not only functions properly, but also retains good sensitivity. The cloaked object is uniformly heated up as quickly as the bare object.

![](images/008d5f2455ce5419564a906d5db4c3209717341eee792d49ea77a6808ae3196b.jpg)

are shown in Fig. 3a-c. In addition to the cloaking effect, it is easy to see the contrast between the temperature inside a traditional bilayer thermal cloak (Fig. 3b) and that inside a thermal zero-index cloak (Fig. 3c). The former remains close to the initial value whereas the latter follows the average temperature of the environment.

To quantify this transient performance, we plot the evolution of temperature  $T^*$  at the centre of the model with time  $t$  in Fig. 3d. The temperature rises rapidly inside the thermal zero-index cloak almost the same as the reference curve when the cloak is absent. On the other hand, the temperature inside a traditional bilayer cloak changes slowly and is still far from the equilibrium value at the end of the simulation. We also performed transient experiments to verify this unique behaviour using a set-up that will be introduced in the following section. The central temperatures measured by an infrared camera are plotted as the scatter points in Fig. 3d, which agree well with the simulated curve. We note that this good transient performance of the thermal zero-index cloak enables its use as a temperature sensor and an invisible uniform heater/ cooler. Compared with previous similar proposals[14,34], this design does not require negative thermal conductivity (the design in ref. has not been experimentally realized) and is irrespective of the interior object (the design in ref. requires the same material of the object as the background).

Experimental demonstration of thermal zero-index cloaking To realize the thermal zero-index cloak, we adopt the experimental set-up schematically drawn in Fig. 4a. The background is a pure

copper plate. The core part is a water channel surrounding the object as the inner layer of the cloak. The water flow in the channel is driven by a disc that spins under an electric motor. The outer layer is directly built on the copper plate by drilling holes in the corresponding region to effectively achieve the required conductivity. The performance of this system can be checked by measuring the temperature profile at the bottom side of the sample with an infrared camera (photo shown in Fig. 4b). A high contrast can be observed in Fig. 4c and d for the stationary and circulating fluid fields in the water channel, respectively. The results are very close to the simulated results in Fig. 2a and b (see Supplementary Figs. 3 and 4 for the numerical and experimental results, respectively, of the temperature profile change with increasing fluid speed and see Supplementary Fig. 5 for numerical results following the experimental set-up with viscous heat generation included; the performance is not influenced by viscous heat). It is worth noticing the temperature at the central object in each state. The infrared image in Fig. 4c was taken  $10\mathrm{min}$  after the water baths were established, but the central temperature still remains at the initial value because of the insulating stationary water channel. The central channel is filled with cold water that is driven by the spin disc, so it exhibits a low temperature. The water tank on the right-hand side (Fig. 4a) is also filled with cold water as the cold source, but it is beyond the viewing range of the infrared image shown in Fig. 4c. The right edge of Fig. 4c is already outside the right water tank, so its temperature is slightly higher than that of the cold source, as well as the central region. A similar result is expected for the object inside a traditional

![](images/2d6255f4d02dc012c031ab94c022b390aae79904ecd9345bcfa7ddfca88e3382.jpg)  
a

![](images/5348a65a60dc83f39e918149bcedbd1a83a016fb502b137ca5983f8663edbbf9.jpg)  
b

![](images/3a3470fcb7684ef145f84d4e01ca1dc04a15931a73dd4bbceb589bcdb7e32cd1.jpg)  
c  
Stationary water  
Fig. 4 | Experimental verification of a convective thermal zero-index cloak. a, Schematic of the experimental set-up. b, Photo of the bottom of the sample. Scale bar is  $2\mathrm{cm}$ . c,d, Temperature profile of the bottom of the sample measured with an IR camera, when the water in the central channel is at rest (c) and when it is circulating the object (a stainless-steel plate) (d). Dashed lines indicate the device.

![](images/0614dfd43131dc781e187f9414ed9fc8bfc07845766a57ccdf20d00dcca57b70.jpg)  
1  
Circulating water

thermal cloak, as shown in Fig. 3b. On the other hand, the infrared image in Fig. 4d was taken within 60 s after the disc started to spin, but the central temperature had already reached close to the steady-state value in that short time. The object senses the environmental temperature quickly without exposing itself. The temperature of the object should be almost the same as its surrounding fluid, but it appears slightly higher in Fig. 4d due to the different emissivities of the two regions. The surrounding fluid is held by a clear acrylic ring, with an emissivity of around 0.94. The object is covered by a frosted polypropylene film, whose emissivity is 0.97. For the infrared camera we used, the entire image must be taken at one preset uniform emissivity (0.95). Therefore, the apparent temperatures of the two regions in the infrared camera are slightly different.

# Outlook

We have shown that by integrating moving fluid inside a conductive system, an extreme effective thermal conductivity can be achieved. This element can be regarded as the thermal counterpart of NZIM in photonics, and then used to design a thermal zero-index cloak. The meta-device is tunable and works for any background, including highly conductive materials. It also serves as a good transient temperature sensor by quickly adjusting its interior temperature to the environmental temperature. None of these features can be found in traditional cloaking devices. This work provides a route for thermal manipulation with almost no limitation on materials. It is expected to be applied in a variety of smart control applications for high-efficiency heat transfer.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, statements of data availability and associated accession codes are available at https://doi.org/10.1038/s41563-018-0239-6.

Received: 13 June 2018; Accepted: 1 November 2018; Published online: 3 December 2018

# References

1. Narayana, S. & Sato, Y. Heat flux manipulation with engineered thermal materials. Phys. Rev. Lett. 108, 214303 (2012).  
2. Han, T. et al. Theoretical realization of an ultra-efficient thermal-energy harvesting cell made of natural materials. Energy Environ. Sci. 6, 3537-3541 (2013).  
3. Han, T., Bai, X., Thong, J. T. L., Li, B. & Qiu, C.-W. Full control and manipulation of heat signatures: Cloaking, camouflage and thermal metamaterials. Adv. Mater. 26, 1731-1734 (2014).  
4. Fan, C. Z., Gao, Y. & Huang, J. P. Shaped graded materials with an apparent negative thermal conductivity. Appl. Phys. Lett. 92, 251907 (2008).  
5. Guenneau, S., Amra, C. & Veynante, D. Transformation thermodynamics: cloaking and concentrating heat flux. Opt. Express 20, 8207-8218 (2012).  
6. Vemuri, K. P. & Bandaru, P. R. Geometrical considerations in the control and manipulation of conductive heat flux in multilayered thermal metamaterials. Appl. Phys. Lett. 103, 133111 (2013).  
7. Schittny, R., Kadic, M., Guenneau, S. & Wegener, M. Experiments on transformation thermodynamics: molding the flow of heat. Phys. Rev. Lett. 110, 195901 (2013).  
8. Xu, H., Shi, X., Gao, F., Sun, H. & Zhang, B. Ultrathin three-dimensional thermal cloak. Phys. Rev. Lett. 112, 054301 (2014).  
9. Han, T. et al. Experimental demonstration of a bilayer thermal cloak. Phys. Rev. Lett. 112, 054302 (2014).  
10. Ma, Y., Liu, Y., Raza, M., Wang, Y. & He, S. Experimental demonstration of a multiphysics cloak: manipulating heat flux and electric current simultaneously. Phys. Rev. Lett. 113, 205501 (2014).  
11. Li, Y., Bai, X., Yang, T., Luo, H. & Qiu, C.-W. Structured thermal surface for radiative camouflage. Nat. Commun. 9, 273 (2018).  
12. Schurig, D. et al. Metamaterial electromagnetic cloak at microwave frequencies. Science 314, 977-980 (2006).  
13. Li, Y. et al. Temperature-dependent transformation thermotics: from switchable thermal cloaks to macroscopic thermal diodes. Phys. Rev. Lett. 115, 195503 (2015).  
14. Yang, T. Z. et al. Invisible sensors: Simultaneous sensing and camouflaging in multiphysical fields. Adv. Mater. 27, 7752-7758 (2015).  
15. Liberal, I. & Engheta, N. Near-zero refractive index photonics. Nat. Photon. 11, 149-158 (2017).  
16. Shalaev, V. M. Optical negative-index metamaterials. Nat. Photon. 1, 41-48 (2007).  
17. Silveirinha, M. & Engheta, N. Tunneling of electromagnetic energy through subwavelength channels and bends using epsilon-near-zero materials. Phys. Rev. Lett. 97, 157403 (2006).  
18. Mahmoud, A. M. & Engheta, N. Wave-matter interactions in epsilon-and-mu-near-zero structures. Nat. Commun. 5, 5638 (2014).  
19. Suchowski, H. et al. Phase mismatch-free nonlinear propagation in optical zero-index materials. Science 342, 1223-1226 (2013).  
20. Liberal, I., Mahmoud, A. M., Li, Y., Edwards, B. & Engheta, N. Photonic doping of epsilon-near-zero media. Science 355, 1058-1062 (2017).  
21. Chu, H. et al. A hybrid invisibility cloak based on integration of transparent metasurfaces and zero-index materials. Light Sci. Appl. 7, 50 (2018).  
22. Alam, M. Z., Schulz, S. A., Upham, J., Leon, I. D. & Boyd, R. W. Large optical nonlinearity of nanoantennas coupled to an epsilon-near-zero material. Nat. Photon. 12, 79-83 (2018).  
23. Liberal, I. & Engheta, N. Manipulating thermal emission with spatially static fluctuating fields in arbitrarily shaped epsilon-near-zero bodies. Proc. Natl Acad. Sci. USA 115, 2878-2883 (2018).  
24. Alam, M. Z., De Leon, I. & Boyd, R. W. Large optical nonlinearity of indium tin oxide in its epsilon-near-zero region. Science 352, 795-797 (2016).  
25. Huang, X., Lai, Y., Hang, Z. H., Zheng, H. & Chan, C. T. Dirac cones induced by accidental degeneracy in photonic crystals and zero-refractive-index materials. Nat. Mater. 10, 582-586 (2011).  
26. Li, Y. et al. On-chip zero-index metamaterials. Nat. Photon. 9, 738-742 (2015).  
27. Maas, R., Parsons, J., Engheta, N. & Polman, A. Experimental realization of an epsilon-near-zero metamaterial at visible wavelengths. Nat. Photon. 7, 907-912 (2013).  
28. Leonhardt, U. Optical conformal mapping. Science 312, 1777-1780 (2006).  
29. Pendry, J. B., Schurig, D. & Smith, D. R. Controlling electromagnetic fields. Science 312, 1780-1782 (2006).

30. Alù, A. & Engheta, N. Achieving transparency with plasmonic and metamaterial coatings. Phys. Rev. E 72, 016623 (2005).  
31. Bejan, A. Convection Heat Transfer (Wiley, Hoboken, 2013).  
32. Olver, F. W. J. & Maximon, L. C. in NIST Digital Library of Mathematical Functions Ch. 10 (Version 1.0.18, release date 27 March 2018); http://dlmf.nist.gov/10release1.0.18 of 2018-03-27.  
33. Torrent, D., Poncelet, O. & Batsale, J.-C. Nonreciprocal thermal material by spatiotemporal modulation. Phys. Rev. Lett. 120, 125501 (2018).  
34. Shen, X. Y. & Huang, J. P. Thermally hiding an object inside a cloak with feeling. Int. J. Heat Mass Trans. 78, 1-6 (2014).

# Acknowledgements

Y.L. and C.-W.Q. acknowledge financial support from the Ministry of Education, Singapore (Project No. R-263-000-C05-112). K.-J.Z. and H.C. are supported by National Key Research Program of China (2016YFA0301101), National Natural Science Foundation of China (61621001), and Natural Science Foundation of Shanghai (18JC1410900). Y.-G.P. and X.-F.Z. are supported by the National Natural Science Foundation of China (Grant Nos. 11690030, 11690032 and 11674119). W.L. and S.F. are supported by Department of Energy Grant No. DE-FG-07ER46426.

# Author contributions

Y.L. and C.-W.Q. conceived the idea. Y.L. designed and performed numerical simulations and theoretical derivations. Y.L., K.-J.Z. and Y.-G.P. performed the experiments. Y.L., W.L., S.F. and C.-W.Q. analysed the numerical results. C.-W.Q. supervised the project. All the authors contributed to the manuscript writing.

# Competing interests

The authors declare no competing financial interests.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41563-018-0239-6.

Reprints and permissions information is available at www.nature.com/reprints.

Correspondence and requests for materials should be addressed to S.F. or C.-W.Q.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2018

# Methods

Steady-state simulations. The coefficients of the cloak are set as:  $R_{1} = 4.8\mathrm{cm}$ ,  $R_{2} = 5.8\mathrm{cm}$  and  $R_{3} = 8.8\mathrm{cm}$ . The thermal conductivity of the cloaked object is  $\kappa_{1} = 17\mathrm{Wm}^{-1}\mathrm{K}^{-1}$  (stainless steel). The background is of size  $30\mathrm{cm} \times 25\mathrm{cm}$  and with thermal conductivity  $\kappa_{\mathrm{b}} = 394\mathrm{Wm}^{-1}\mathrm{K}^{-1}$  (copper). The left and right boundaries are maintained at temperature  $T_{\mathrm{L}} = 323.2\mathrm{K}$  and  $T_{\mathrm{R}} = 293.2\mathrm{K}$ , respectively. The upper and lower boundaries are thermally insulated. The initial temperature of the entire system is set to be the same as  $T_{\mathrm{R}}$ .

For the thermal zero-index cloak, the coefficients are set as:  $\kappa_{2} = 0.6\mathrm{Wm}^{-1}\mathrm{K}^{-1}$  (water) and  $\kappa_{3} = 156\mathrm{Wm}^{-1}\mathrm{K}^{-1}$  (calculated according to equation (5)). For the bilayer thermal cloak, the coefficients are set as:  $\kappa_{2} = 0.042\mathrm{Wm}^{-1}\mathrm{K}^{-1}$  (expanded polystyrene (EPS) foam as a good thermal insulator) and  $\kappa_{3} = 429\mathrm{Wm}^{-1}\mathrm{K}^{-1}$  (silver). At high fluid velocity the thermal boundary layer is very thin and requires a special meshing configuration. Here we employ a mesh convergence study for each rotation speed to determine the thickness of boundary layers as small as  $2\mu \mathrm{m}$ , which is discretized with a mapped mesh.

For simplicity, we assume that the physical properties of the fluid are independent of temperature, thus the velocity field of the fluid is not affected by its temperature distribution. (It is easy to see that the results should be the same when temperature dependence is considered, since the velocity is fast enough to wipe out all temperature gradients except in the thermal boundary layer.) We also assume a simple velocity field  $\nu(r) = \Omega r$  for the convenience of theoretical analysis (see Supplementary Note 1). We found that for the above settings,  $\Omega = 2\pi \times 100\mathrm{rad s^{-1}}$  is sufficient to approach a near-zero temperature gradient (smaller  $\Omega$  leads to larger deviation from the ideal effects, see Supplementary Fig. 3). It actually does not matter which specific velocity field is present as long as the speed is large enough. In order to confirm the arguments on temperature dependency and velocity field, three-dimensional simulations with a more realistic set-up based on the experiments were also performed using a non-isothermal turbulent flow model and temperature-dependent material parameters (see Supplementary Fig. 5). The temperature distributions are found to be similar to those in the simplified two-dimensional simulations. We also examined the effects of viscous heat generation, which has been ignored in our discussion. The turbulence dissipation rate integrated in the entire fluid field is found to be  $0.02\mathrm{W}$ , much smaller than the conductive heat that passes through the fluid field (18.77 W).

To find the magnitude of effective thermal conductivity  $\kappa_{2}^{\mathrm{eff}}$ , we first performed the convective simulation at fluid rotation speed  $\Omega$  and obtained a temperature field  $T(r,\theta)$ . Then a series of simulations were performed by replacing the fluid layer with solids of various conductivity  $\kappa_{2}^{\mathrm{solid}}$ . The corresponding temperature field  $T^{\mathrm{solid}}(r,\theta)$  is compared with  $T(r,\theta)$  by evaluating  $\mathrm{RMSD}(T) = \sqrt{(T^{\mathrm{solid}} - T)^2}$ , where the average is performed over the region outside the cloak. We then find  $\kappa_{2}^{\mathrm{eff}}(\Omega)$  as the value of  $\kappa_{2}^{\mathrm{solid}}$  that minimizes  $\mathrm{RMSD}(T)$  and renders a temperature field closest to that outside the zero-index cloak.

Transient simulations. The same models as for the steady-state simulations were adopted. In addition, the densities and heat capacities of the background and object are set as:  $\rho_{\mathrm{b}} = 8,900\mathrm{kg}\mathrm{m}^{-3}$  and  $c_{\mathrm{b}} = 390\mathrm{Jkg^{-1}K^{-1}}$  (copper);  $\rho_{1} = 7,930\mathrm{kg}\mathrm{m}^{-3}$  and  $c_{1} = 500\mathrm{Jkg^{-1}K^{-1}}$  (stainless steel). For the bilayer cloak,  $\rho_{2} = 30\mathrm{kg}\mathrm{m}^{-3}$  and  $c_{2} = 1,380\mathrm{Jkg^{-1}K^{-1}}$  (EPS foam);  $\rho_{3} = 10,490\mathrm{kg}\mathrm{m}^{-3}$  and  $c_{3} = 240\mathrm{J / (kgK)}$  (silver). For the zero-index cloak,  $\rho_{2} = 1,000\mathrm{kg}\mathrm{m}^{-3}$  and  $c_{2} = 4,200\mathrm{Jkg^{-1}K^{-1}}$  (water);  $\rho_{3} = 8,900\mathrm{kg}\mathrm{m}^{-3}$  and  $c_{3} = 390\mathrm{Jkg^{-1}K^{-1}}$  (copper).

Experimental demonstration. The dimensions of the device are same as those in the simulations. A pure copper plate of size  $40\mathrm{cm}\times 25\mathrm{cm}$  and thickness  $3\mathrm{mm}$  is used as the background. The two ends of the longer side are immersed in water baths for a distance of  $5\mathrm{cm}$ . A hole of radius  $R_{2}$ $(5.8\mathrm{cm})$  is made at the centre of the background to place the object of radius  $R_{1}$ $(4.8\mathrm{cm})$  and the surrounding water channel  $(R_{1}$  to  $R_{2})$ . A plastic disc is connected to a d.c. electric motor and located just above the water channel to drive the fluid motion when it is spinning. The disc was fabricated out of polylactic acid (PLA) using a 3D-printer (Replicator 2X, MakerBot). The infill density is  $100\%$ .

The object and water channel are supported by an acrylic base (with an emissivity of 0.94) connected to the bottom of the copper plate. An acrylic ring is put on top of the copper plate surrounding the water channel as a wall. An acrylic plate is put on top of the wall to cover the object, water channel and PLA disc for protection. The acrylic base, wall and cover are connected to the copper plate with nuts and bolts. For the second layer of the zero-index cloak  $(R_{2}$  to  $R_{3})$ , we drill small holes on the copper plate to achieve the required thermal conductivity  $\kappa_{3}$ . The small holes of radius  $1.75\mathrm{mm}$  form square lattices of size  $4.8\mathrm{mm} \times 4.8\mathrm{mm}$ . According to the Maxwell-Garnett formula<sup>35</sup>

$$
\kappa_ {3} = \kappa_ {\mathrm {b}} \left[ 1 + \frac {2 \left(\kappa_ {\mathrm {a i r}} - \kappa_ {\mathrm {b}}\right) f}{\kappa_ {\mathrm {a i r}} + \kappa_ {\mathrm {b}} - \left(\kappa_ {\mathrm {a i r}} - \kappa_ {\mathrm {b}}\right) f} \right] \tag {6}
$$

where  $\kappa_{\mathrm{air}} = 0.03\mathrm{Wm}^{-1}\mathrm{K}^{-1}$  is the thermal conductivity of air and  $f$  is the area fraction of the small holes:  $f = \pi \times (1.75 / 4.8)^2 = 0.42$ . It follows from equation (6) that  $\kappa_{3} = 160\mathrm{Wm}^{-1}\mathrm{K}^{-1}$ , close to the simulation setting. To build a stable temperature boundary condition, the two ends of the copper plate are slotted in two acrylic boxes filled with hot  $(323\mathrm{K})$  and cold  $(293\mathrm{K})$  water.

The motor has a no-load speed of 12,000 r.p.m. at  $12\mathrm{V}$ . In the experiments, the motor is connected to a voltage transformer with the input voltage tuned from 0 to  $4.5\mathrm{V}$ . At  $4\mathrm{V}$  a nice cloaking effect is already observable through a FLIR i60 IR camera (with a resolution of  $0.1\mathrm{K}$ ). The results of temperature evolution (scatter points in Fig. 3d) and steady-state profiles (Fig. 4d) were obtained at  $4\mathrm{V}$  input. The corresponding rotation speed of the fluid would be smaller than the no-load speed of 4,000 r.p.m. as well as that used in simulations (6,000 r.p.s.), but the performance of the device is satisfactory. The transient experiments were performed by first driving fluid into motion and then adding hot water as heat bath. The steady-state experiments were performed by first adding the heat bath and then driving the fluid into motion. The infrared camera is placed  $1\mathrm{m}$  under the copper plate to measure the temperature profile of the bottom of the sample, which is covered by a frosted polypropylene film with an emissivity of 0.97 to reduce reflection and enhance emission of the infrared signal.

# Data availability

The data that support the findings of this study are available from the corresponding author C.-W.Q. upon reasonable request.

# References

35. Garnett, J. C. M. Colours in metal glasses, in metallic films, and in metallic solutions. II. Phil. Trans. R. Soc. A 205, 238-288 (1906).