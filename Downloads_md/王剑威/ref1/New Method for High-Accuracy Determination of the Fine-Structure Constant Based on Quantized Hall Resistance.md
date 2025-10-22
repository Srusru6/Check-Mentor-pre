# New Method for High-Accuracy Determination of the Fine-Structure Constant Based on Quantized Hall Resistance

K. v. Klitzing

Physikalisches Institut der Universität Würzburg, D-8700 Würzburg, Federal Republic of Germany, and Hochfeld-Magnetlab des Max-Planck-Instituts für Festkörperforschung, F-38042 Grenoble, France

and

G. Dorda

Forschungs laboratorien der Siemens AG, D-8000 München, Federal Republic of Germany

and

M. Pepper

Cavendish Laboratory, Cambridge CB3 0HE, United Kingdom

(Received 30 May 1980)

Measurements of the Hall voltage of a two-dimensional electron gas, realized with a silicon metal-oxide-semiconductor field-effect transistor, show that the Hall resistance at particular, experimentally well-defined surface carrier concentrations has fixed values which depend only on the fine-structure constant and speed of light, and is insensitive to the geometry of the device. Preliminary data are reported.

PACS numbers: 73.25.+i, 06.20.Jr, 72.20.My, 73.40.Qv

In this paper we report a new, potentially high-accuracy method for determining the fine-structure constant,  $\alpha$ . The new approach is based on the fact that the degenerate electron gas in the inversion layer of a MOSFET (metal-oxide-semiconductor field-effect transistor) is fully quantized when the transistor is operated at helium temperatures and in a strong magnetic field of order 15 T. The inset in Fig. 1 shows a schematic diagram of a typical MOSFET device used in this work. The electric field perpendicular to the surface (gate field) produces subbands for the motion normal to the semiconductor-oxide interface, and the magnetic field produces Landau quantization of motion parallel to the interface. The density of states  $D(E)$  consists of broadened  $\delta$  functions; minimal overlap is achieved if the magnetic field is sufficiently high. The number of states,  $N_{\mathrm{L}}$ , within each Landau level is given by

$$
N _ {\mathrm {L}} = e B / h, \tag {1}
$$

where we exclude the spin and valley degeneracies. If the density of states at the Fermi energy,  $N(E_{\mathrm{F}})$ , is zero, an inversion layer carrier cannot be scattered, and the center of the cyclotron orbit drifts in the direction perpendicular to the electric and magnetic field. If  $N(E_{\mathrm{F}})$  is finite but small, an arbitrarily small rate of scattering cannot occur and localization produced by the long lifetime is the same as a zero scattering rate, i.e., the same absence of current-carrying states occurs. Thus, when the Fermi level is between

![](images/9a006ef4f4b542a86dc0d234b1fe8e366d13df65d46658f5455a811b6df72c6c.jpg)  
FIG. 1. Recordings of the Hall voltage  $U_{\mathrm{H}}$ , and the voltage drop between the potential probes,  $U_{pp}$ , as a function of the gate voltage  $V_{g}$  at  $T = 1.5 \mathrm{~K}$ . The constant magnetic field  $(B)$  is 18 T and the source drain current,  $I$ , is 1 μA. The inset shows a top view of the device with a length of  $L = 400 \mu \mathrm{m}$ , a width of  $W = 50 \mu \mathrm{m}$ , and a distance between the potential probes of  $L_{pp} = 130 \mu \mathrm{m}$ .

Landau levels the device current is thermally activated and the minima in  $\sigma_{xx},\sigma_{xx}^{\min}$  can be less than  $10^{-7}\sigma_{xx}^{\max .4}$  Increasing the magnetic field and decreasing the temperature, further decreases  $\sigma_{xx}^{\min}$  . The Hall conductivity  $\sigma_{xy}$  which is usually a complicated function of the scattering process, becomes very simple in the absence of scattering and is given by2

$$
\sigma_ {x y} = - N e / B, \tag {2}
$$

where  $N$  is the carrier concentration.

The correction term to the above relation,  $\Delta \sigma_{xy}$ , is of the order of  $\sigma_{xx} / \omega \tau$ , where  $\omega$  is the cyclotron frequency and  $\tau$  is the relaxation time of the conduction electrons;  $\omega \tau >> 1$  in strong magnetic fields. When the Fermi energy is between Landau levels, and  $\sigma_{xx}^{\min} \sim 10^{-7} \sigma_{xx}^{\max}$ , the correction  $\Delta \sigma_{xy} / \sigma_{xy} < 10^{-8}$ . Subject to any error imposed by  $\Delta \sigma_{xy}$ , when a Landau level is fully occupied and  $N = N_{\mathrm{L}} i (i = 1,2,3,\ldots)$ ,  $\sigma_{xy}$  is immediately given from Eqs. (1) and (2):

$$
- \sigma_ {x y} = e ^ {2} i / h. \tag {3}
$$

The Hall resistivity  $\rho_{xy} = -\sigma_{xy} / (\sigma_{xx}^2 +\sigma_{xy}^2)\approx -\sigma_{xy}^{-1}$  is defined by  $E_{\mathrm{H}} / j$  ( $E_{\mathrm{H}} = \text{Hall field}, j = \text{current density}$ ) and can be rewritten  $R_{\mathrm{H}} / I$ , where  $R_{\mathrm{H}}$  is the Hall resistance,  $U_{\mathrm{H}}$  the Hall voltage and  $I$  the current. Thus,  $R_{\mathrm{H}} = h / e^{2}i$ , which may finally be written as<sup>5</sup>

$$
R _ {\mathrm {H}} = \alpha^ {- 1} \mu_ {0} c / 2 i, \tag {4}
$$

where  $\mu_0$  is the permeability of vacuum and exactly equal to  $4\pi \times 10^{-7}\mathrm{Hm}^{-1}$ ,  $c$  is the speed of light in vacuum and equal to 299792458 m s $^{-1}$  with a current uncertainty $^5$  of 0.004 ppm and  $\alpha \approx \frac{1}{137}$  is the fine-structure constant. It is clear from Eq. (4) that a high-accuracy measurement of the Hall resistance in SI units will give a value of  $\alpha$  with essentially the same accuracy. Since resistances can be determined in SI units to a few parts in  $10^8$  by means of the so-called calculable cross capacitor by Thompson and Lampard, $^6$  the question of absolute units versus as-maintained units is much less of a problem than in the determination of  $e / h$  from the ac Josephson effect. Furthermore, the magnitude of  $R_{\mathrm{H}}$  falls within a relatively convenient range:  $R_{\mathrm{H}} \approx (25813\Omega) / i$ , with  $i$  typically between 2 and 8. Finally, we note that if  $\alpha$  is assumed to be known from some other experiment (for example, from  $2e / h$  and the proton gyromagnetic ratio  $\gamma_p$ ), Eq. (4) may be used to derive a known standard resistance.

Two well-known corrections in the low-field Hall effect become unimportant. The first is the

correction due to the shorting of the Hall voltage by the source and drain contacts. This is important at low fields for samples with length-towidth ratio,  $L / W$  , less than 4, but becomes negligible when the Hall angle is  $90^{\circ}$  , i.e.,  $\sigma_{xx} = 0.$  The second correction which becomes unimportant is that due to an inexact alignment of the Hall probes, i.e., they are not exactly opposite: This is irrelevant, as the voltage drop along the sample vanishes when  $\sigma_{xx} = 0$

The experiments were carried out on MOS devices with a range of oxide thicknesses  $(d_{\mathrm{ox}} = 100$  nm-400 nm), and length-to-width ratios ranging from  $L / W = 25$  to  $L / W = 0.65$ . All the transistors were fabricated on the (100) surface orientation and, typically, the  $p$ -type substrate had room temperature resistivity of  $10\Omega$  cm. The resistivity at helium temperature was higher than  $10^{13}$ $\Omega$  cm, and no current flow between source and drain around the channel could be measured. The long devices  $(L / W > 8)$  had potential probes in addition to the Hall probes.

A typical recording of the measured Hall voltage  $U_{\mathrm{H}}$ , and the voltage between the potential probes  $U_{pp}$ , as a function of the gate voltage is shown in Fig. 1. These results were obtained at a constant magnetic field of  $B = 18$  T, a temperature of  $1.5$  K and a constant source drain current of  $I = 1$  μA. Relevant device parameters were  $L = 400$  μm,  $W = 50$  μm and the distance between potential probes was about  $130$  μm.

The measured voltage  $U_{pp}$  is proportional to the resistivity component  $\rho_{xx} = \sigma_{xx}\left[\rho_{xx}^2 +\rho_{xy}^2\right]$ . At gate voltages where the  $E_{\mathrm{F}}$  is in the energy gap between Landau levels, minima in both  $\sigma_{xx}$  and  $\rho_{xx}$  are observed. Such minima are clearly visible, and are identified, in Fig. 1; the minima due to the lifting of the spin and the (twofold) valley degeneracy are also apparent. The Hall voltage clearly levels off at those values of carrier concentration where  $\sigma_{xx}$  and  $\rho_{xx}$  are zero. The values of  $U_{\mathrm{H}}$  obtained in the regions are in good agreement with the predicted values, Eq. (4), if the error due to the 1-MΩ input impedance of the  $X - Y$  recorder is taken into account. It was found that the value of  $U_{\mathrm{H}}$  in the "steps" was, for instance current, independent of sample geometry and direction of magnetic field, provided that  $\sigma_{xx}$  was zero.

An area of possible criticism of the theoretical basis of this experiment, is the role of carriers which are localized outside the main Landau level. Here we do not specify the localization mechanism, but the presence of localized carriers will

invalidate both the relation  $N = N_{\mathrm{L}}$  and Eq. (4). However, the experimental results strongly suggest that such carriers do not invalidate Eq. (4). At present there is both theoretical and experimental investigation of this type of localization.3,4,9-12 Ando has suggested that the electrons in impurity bands, arising from short range scatterers, do not contribute to the Hall current; whereas the electrons in the Landau level give rise to the same Hall current as that obtained when all the electrons are in the level and can move freely. Clearly this process must be occurring but its range of validity must be carefully examined as an accompaniment to highly accurate measurements of Hall resistance.

For high-precision measurements we used a normal resistance  $R_0$  in series with the device. The voltage drop,  $U_0$ , across  $R_0$ , and the voltages  $U_{\mathrm{H}}$  and  $U_{\mathbf{pp}}$  across and along the device was measured with a high impedance voltmeter ( $R > 2 \times 10^{10}$ )

![](images/9ce42e6e5f4e12f2c0ebabfb63b6d780447d8bab486b20dcd5438c445f13915a.jpg)

![](images/961c35b120f0fdad377538b49b08a84f80f93dd656f62f406dc00a1814ce0b53.jpg)  
FIG. 2. Hall resistance  $R_{\mathrm{H}}$ , and device resistance,  $R_{pp}$ , between the potential probes as a function of the gate voltage  $V_{g}$  in a region of gate voltage corresponding to a fully occupied, lowest  $(n = 0)$  Landau level. The plateau in  $R_{\mathrm{H}}$  has a value of  $6453.3 \pm 0.1 \Omega$ . The geometry of the device was  $L = 400 \mu \mathrm{m}$ ,  $W = 50 \mu \mathrm{m}$ , and  $L_{pp} = 130 \mu \mathrm{m}$ ;  $B = 13 \mathrm{T}$ .

$\Omega$  ). The resistance  $R_{0}$  was calibrated by the Physikalisch Technische Bundesanstalt, Braunschweig, and had a value of  $R_{0} = 9999.69\Omega$  at a temperature of  $20^{\circ}\mathrm{C}$ . A typical result of the measured Hall resistance  $R_{\mathrm{H}} = U_{\mathrm{H}} / I = U_{\mathrm{H}}R_{0} / U_{0}$ , and the resistance,  $R_{pp} = U_{pp}R_0 / U_0$ , between the potential probes of the device is shown in Fig. 2 ( $B = 13\mathrm{T}$ ,  $T = 1.8\mathrm{K}$ ). The minimum in  $\sigma_{xx}$  at  $V_{g} = 23.6\mathrm{V}$  corresponds to the minimum at  $V_{g} = 8.7\mathrm{V}$  in Fig. 1, because the thicknesses of the gate oxides of these two samples differ by a factor of 3.6. Our experimental arrangement was not sensitive enough to measure a value of  $R_{pp}$  of less than 0.1  $\Omega$  which was found in the gate-voltage region  $23.40\mathrm{V} < V_{g} < 23.80\mathrm{V}$ . The Hall resistance in this gate voltage region had a value of  $6453.3 \pm 0.1\Omega$ . This inaccuracy of  $\pm 0.1\Omega$  was due to the limited sensitivity of the voltmeter. We would like to mention that most of the samples, especially devices with a small length-to-width ratio, showed a minimum in the Hall voltage as a function of  $V_{g}$  at gate voltage close to the left side of the plateau. In Fig. 2, this minimum is relatively shallow and has a value of  $6452.87\Omega$  at  $V_{g} = 23.30\mathrm{V}$ .

In order to demonstrate the insensitivity of the Hall resistance on the geometry of the device, measurements on two samples with a length-to-width ratio of  $L / W = 0.65$  and  $L / W = 25$ , respectively, are plotted in Fig. 3. The gate-voltage scale

![](images/571b0fcbdb71a2e4e2ee0bdd11720daaaf737355539237a0f0af6007fb761b4f.jpg)  
FIG. 3. Hall resistance  $R_{\mathrm{H}}$  for two samples with different geometry in a gate-voltage region  $V_{g}$  where the  $n = 0$  Landau level is fully occupied. The recommended value  $h / 4e^{2}$  is given as 6453.204 Ω.

is given in arbitrary units, and is different for the two samples because the thicknesses of the gate oxides are different. A gate voltage  $V_{g} = 1.00$  corresponds, approximately, to a surface carrier concentration where the first fourfold-degenerate Landau level,  $n = 0$ , is completely filled. Within the experimental accuracy of  $0.1\Omega$ , the same value for the plateau in the Hall resistance is measured. The value for  $h / 4e^{2} = 6453.204 \pm 0.005\Omega$  based on the recommended value for the fine-structure constant is plotted in this figure, too. The decrease of the Hall resistance with decreasing gate voltage for the sample with  $L / W = 0.65$  originates mainly from the shorting of the Hall voltage at the contacts. This effect is most pronounced when the Hall angle becomes smaller than  $90^{\circ}$ . In the limit of small Hall angles, the Hall voltage is reduced by a factor of 2 for the sample with  $L / W = 0.65$ .

The mean value of the Hall resistance for all samples investigated was  $6453.22 \pm 0.10\Omega$  for measurements in the energy gap between the Landau levels  $n = 0$  and  $n = 1$  (corresponding to  $i = 4$  in Eq. 4),  $3226.62 \pm 0.10\Omega$  for measurements in the energy gap between Landau levels  $n = 1$  and  $n = 2$  ( $i = 8$ ), and  $12906.5 \pm 1.0\Omega$  for measurements in the energy gap between the spin split levels with  $n = 0$  ( $i = 2$ ). These resistances agree very well with the calculated values  $h / e^2 i$  based on the recently reported<sup>13</sup> highly accurate value of  $\alpha^{-1} = 137.035963(15)$  (0.11 ppm).

Measurements with a voltmeter with higher resolution and a calibrated standard resistor with a vanishing small temperature coefficient at  $T = 25^{\circ} \mathrm{C}$  yield a value of  $h / 4e^{2} = 6453.17 \pm 0.02 \Omega$

corresponding to a fine-structure constant of  $\alpha^{-1} = 137.0353 \pm 0.0004$ .

We would like to thank the Physikalisch Technische Bundesanstalt, Braunschweig, for experimental support and E. R. Cohen, Th. Englert, V. Kose, G. Landwehr, and B. N. Taylor for valuable discussions. One of us (M.P.) would like to thank the European Research Office of the U. S. Army for partial support.

For a review see for example: F. Stern, Crit. Rev. Solid State Sci. 5, 499 (1974); G. Landwehr, in Advances in Solid State Physics: Festkörperprobleme, edited by H. J. Queisser (Pergamon, New York-Vieweg, Braunschweig, 1975), Vol. 15, p. 48.  
$^{2}$ T. Ando, J. Phys. Soc. Jpn. 37, 622 (1974).  
$^{3}$ H. Aoki and H. Kamimura, Solid State Commun. 21, 45 (1977).  
$^{4}$ R. J. Nicholas, R. A. Stradling, and R. J. Tidey, Solid State Commun. 23, 341 (1977).  
$^{5}$ E. R. Cohen and B. N. Taylor, J. Phys. Chem. Ref. Data 2, 633 (1973).  
$^{6}$ A. M. Thompson and D. G. Lampard, Nature (London) 177, 888 (1956).  
$^{7}$ I. Isenberg, B. R. Russel, and F. R. Greene, Rev. Sci. Instrum. 19, 685 (1948).  
$^{8}$ R. F. Wick, J. Appl. Phys. 25, 741 (1954).  
9Th. Englert and K. V. Klitzing, Surf. Sci. 73, 71 (1978).  
10S. Kawaji and J. Wakabayashi, Surf. Sci. 58, 238 (1976).  
11M. Pepper, Philos. Mag. 37B, 83 (1978).  
12S.Kawaji,Surf.Sci.73,46 (1978).  
13E. R. Williams and P. T. Olsen, Phys. Rev. Lett. 42, 1575 (1979).