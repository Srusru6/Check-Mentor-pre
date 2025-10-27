# Quantum random number generators

Miguel Herrero-Collantes*

Instituto Nacional de Ciberseguridad, Avenida Jose Aguado,

41, Edificio INCIBE 24005, León, Spain

and El Telecomunicación, Department of Signal Theory and Communications,

University of Vigo, Campus Universitario Lagoas-Marcosende, E-36310 Vigo, Spain

Juan Carlos Garcia-Escartin

Universidad de Valladolid, Dpto. Teoria de la Senal e Ing. Telemática,

Paseo Belén no 15, 47011 Valladolid, Spain

(published 22 February 2017)

Random numbers are a fundamental resource in science and engineering with important applications in simulation and cryptography. The inherent randomness at the core of quantum mechanics makes quantum systems a perfect source of entropy. Quantum random number generation is one of the most mature quantum technologies with many alternative generation methods. This review discusses the different technologies in quantum random number generation from the early devices based on radioactive decay to the multiple ways to use the quantum states of light to gather entropy from a quantum origin. Randomness extraction and amplification and the notable possibility of generating trusted random numbers even with untrusted hardware using device-independent generation protocols are also discussed.

DOI: 10.1103/RevModPhys.89.015004

# CONTENTS

I. Motivation 1

II. Random Numbers and Their Applications 2

A. Pseudorandom number generators and true random number generators 2  
B. Random numbers in simulation 4  
C. Random numbers in cryptography 5  
D. Random numbers in fundamental science 6

III. Block Description 7

IV. Entropy Estimation 8

V. Quantum Random Number Generators Based on Radioactive Decay 9

A. The first quantum random number generators 9  
B. Evolution 10  
C. Limitations 11

VI. Random Number Generators Based on Noise 12

VII. Optical Quantum Random Number Generators 12

A. Quantum optics in random number generators 12  
B. Branching path generators 13  
C. Time of arrival generators 15  
D. Photon counting generators 17  
E. Attenuated pulse generators 18  
F. Generators based on quantum vacuum fluctuations 18  
G. Generators based on the phase noise of lasers 19  
H. Generators based on amplified spontaneous emission 20  
I. Generators based on Raman scattering 22  
J. Generators based on optical parametric oscillators 24

VIII. Nonoptical Quantum Random Number Generators 25

IX. Random Numbers Certified by Quantum Mechanics 26

A. Self-testing in quantum random number generators 26

B. Device-independent quantum random number generators 28  
C. Other forms of quantum certification 30

X.Postprocessing 30

A. Randomness extractors 31  
1. Deterministic extractors 31  
2. Seeded extractors 32

XI. Quantum Randomness Extractors: Randomness Expansion and Randomness Amplification 33

A.Quantum randomness expansion 33  
B.Quantum randomness amplification 34

XII. Randomness Testing 34  
XIII. Discussion 35  
Acknowledgments 36  
References 36

# I. MOTIVATION

Quantum mechanics offers interesting new protocols in the intersection between computer science, telecommunications, information theory, and physics. Results such as the protocols for quantum key distribution (Bennett and Brassard, 1984; Ekert, 1991) and efficient algorithms for problems that are thought or known to be hard for classical computers (Ekert and Jozsa, 1996; Childs and van Dam, 2010) show quantum physics can have a profound impact on the way we think about security, cryptography, and computation.

Despite the impressive experimental achievements of the last decades, the current state of technology is still not advanced enough for a full-scale universal quantum computer. Quantum key distribution, on the other hand, has already become an established technology and the first commercial

systems have been demonstrated in practical scenarios (Peev et al., 2009; Sasaki et al., 2011).

Another important well-established quantum technology is quantum random number generation. Quantum random number generators (QRNGs) are devices that use quantum mechanical effects to produce random numbers and have applications that range from simulation to cryptography. They are usually simpler than other quantum devices and are mature enough to be applied. QRNGs using different quantum phenomena have gone from the lab to the shelves with at least eight existing commercial products (ID Quantique, 2014; Micro Photon Devices, 2014; PicoQuant, 2014; QRB121, 2014; Quintessence Labs, 2014; Qutools, 2014; Wilber, 2014; Hughes and Nordholt, 2016) and online servers that provide quantum random numbers on demand (Walker, 1996; University of Geneva, 2004; Stevanovic et al., 2008; ANU, 2016; Humboldt-Universität, 2016b), as well as many patents (Kim and Klass, 2001; Dultz et al., 2002; Dultz, Hildebrandt, and Deutsche Telekom Ag, 2002; Klass, 2003, 2005; Lutkenhaus, Cohen, and Lo, 2007; Trifonov, Vig, and Magiq Technologies, Inc., 2007; Beausoleil, Munro, and Spiller, 2008; Ribordy, Guinnard, and ID Quantique, 2009; Vartsky et al., 2011; Sartor, Zimmermann, and Sony Corporation, 2015). In the last few years there has also been a large number of proposals, experiments, improvements, and exciting theoretical results in randomness extraction and randomness certification.

The aim of this review is to collect the most important proposals for quantum random number generation and give an introduction to the new advanced protocols that use quantum physics to process, certify, or otherwise deal with random strings. This paper complements previous surveys on the topics of physical and quantum random number generation (Stipčević, 2012; Stipčević and Koc, 2014; Ma et al., 2016) with a focus on QRNGs based on quantum optics.

Section II gives a brief description of the most important applications of randomness in science and computers. We review the differences between algorithmic methods to produce random looking numbers and physical methods to produce true random numbers and discuss when each method is more appropriate. Because of their importance, we concentrate on applications to simulation and cryptography.

Section III describes the main functional elements of quantum random number generators and their roles. In Sec. IV we present some mathematical measures of randomness which are particularly useful to analyze the amount of available random bits and the security of quantum random number generators.

Section V discusses QRNGs based on radioactive decay, which were the first proposed QRNGs and are still in use today. Section VI introduces random number generators based on electronic noise and analyses when they can be said to be quantum.

Section VII discusses how optics has modernized QRNGs. Most present-day QRNGs are based on quantum optics and we review the multiple implementations that work with the quantum states of light.

Section VIII covers alternative QRNGs based on nonoptical quantum phenomena and Sec. IX is centered on those QRNGs whose randomness is backed by quantum mechanics.

Section X gives a brief review on the available classical randomness extraction methods and Sec. XI introduces the quantum protocols for randomness expansion and amplification that allow to produce good-quality random outputs from weak randomness sources.

Section XII is an introduction to the statistical tests that are usually employed to assess the quality of the final random bit stream.

Finally, in Sec. XIII, we give an overview on the current state of quantum random number generation and the challenges and opportunities for the next generation of quantum devices in the field of randomness.

# II. RANDOM NUMBERS AND THEIR APPLICATIONS

Random numbers are an essential resource in science, technology, and many aspects of everyday life (Hayes, 2001). Randomness is required to different extents in applications such as cryptography, simulation, coordination in computer networks or lotteries. Some applications require a small amount of random numbers and still use manual and mechanical methods to generate randomness, such as tossing a coin, throwing a die, spinning a roulette wheel, or drawing a ball from a lottery machine. Here we concern ourselves with the generation of random numbers for computers.

Defining randomness is a deep philosophical problem and we will not attempt to solve it here. In this section, we give common operational definitions of randomness that fit the different purposes the random numbers must fulfil. For instance, in simulation, a method that generates numbers simulating the statistics of the desired distribution can be considered to be "random enough," even if it produces a predictable sequence.

# A. Pseudorandom number generators and true random number generators

In computing, it is important to distinguish between algorithmically generated numbers that mimic the statistics of random distributions and random numbers generated from unpredictable physical events.

Generating random numbers directly from a computer seems like a particularly attractive idea. Methods that produce random numbers from a deterministic algorithm are called pseudorandom number generators (PRNGs). While it is clear that any algorithmically generated sequence cannot be truly random, for many applications the appearance of randomness is enough. $^{1}$

PRNGs normally start from a small string of bits called the seed that is used as the input of a procedure that outputs a long sequence of bits following the statistics of the uniform distribution. In principle, an RNG could produce numbers obeying any random distribution, but the standard practice is

trying to provide a uniform distribution, from which we can obtain the most commonly used distributions using well-known transformations (Hörmann, Leydold, and Derflinger, 2004). Knuth (1997) gave an excellent survey on PRNGs and how to transform uniform random numbers into other types of random quantities in his second book of the series "The Art of Computing Programming."

A large number of PRNGs are based on number theory. Linear congruential generators have been particularly popular since Lehmer introduced them in 1951 (Lehmer, 1951). Linear congruential generators produce random numbers from the recursive formula

$$
X _ {n + 1} = \left(a X _ {n} + c\right) \mod m, \quad n \geq 0, \tag {1}
$$

where  $X_{i}$  is the  $i$ th digit in the sequence of random numbers,  $m > 0$  is the modulus,  $0 \leq a < m$  is called the multiplier, and  $0 \leq c < m$  the increment. The properties of the output depend heavily on the correct choice of these parameters. A poor choice can create an output sequence with a short period.

Its period is one of the most important properties of any PRNG. The next number in a pseudorandom sequence is determined from the internal state of a generator. For a finite memory, the internal state will at some point be the same and the output sequence will begin to repeat itself. PRNGs are chosen to have large periods so that the repetition does not appear during the intended operation time.

Apart from congruential linear generators, there is another large family of PRNGs based on linear shift feedback registers and their generalizations. The most notable generator in this class is the Mersenne Twister (Matsumoto and Nishimura, 1998), which belongs to the family of twisted generalized linear shift feedback registers. The Mersenne Twister has a period which is a Mersenne prime of the form  $2^{n} - 1$ , for an integer  $n$ . The most widely used pseudorandom number generator is the MT19937, the standard implementation of the Mersenne Twister with a period  $2^{19937} - 1$ . It is the default generator in many programming languages and popular scientific software.

L'Ecuyer (2012) gives a good review of these and other alternative PRNGs based on different principles.

Pseudorandom numbers have certain advantages that make them popular. They can be much faster than alternative random number generation methods and their results are reproducible. For instance, we can repeat the exact same simulation if we know the seed. However, for many applications, unpredictability is an important requisite. Clearly, a predictable lottery is not acceptable, even if all the resulting numbers are uniformly distributed. Some pseudorandom generators are designed to be unpredictable (see Sec. II.C), but applications that need an output that cannot be guessed usually turn to true random number generators (TRNGs), if only to renew the seed of a PRNG.

True random number generators measure some unpredictable or, at least, difficult to predict physical process and use the results to create a sequence of random numbers. They either rely on unpredictable values that can be accessed from the software inside the computer or create the sequence in a special-purpose device that feeds it into the operating system.

The process of collecting unpredictable data is usually called entropy gathering. Some of the standard entropy sources the operating system can access include data from the sound card, disk access times, the timing of interrupts, or user interaction data, such as mouse motion or keystrokes, to name a few. The way the Linux operating systems collect entropy and convert it into random bits (Gutterman, Pinkas, and Reinman, 2006) is an illustrative example of many of the most usual methods. Some call these generators that use nondeterministic events, nonphysical nondeterministic RNGs (Killmann and Schindler, 2008) that stand in contrast to physical TRNGs based in nondeterministic physical effects in electronic circuits or in the result of some physical experiment. There are physical TRNGs based on different principles, such as chaotic systems (Stojanovski and Kocarev, 2001; Stojanovski, Pihl, and Kocarev, 2001), thermal noise in electronic circuits (Murry, 1970; Petrie and Connelly, 2000), free running oscillators (Kohlbrenner and Gaj, 2004), or biometric parameters (Szczepanski et al., 2004) to name a few examples.

Some vendors include integrated physical random number generators in their processors. Intel has included in its recent processors a digital RNG based on a metastable latch that, due to thermal noise, suffers jumps in its state at around a 3 GHz rate. This integrated RNG can be directly accessed from a processor instruction, RdRand (Taylor and Cox, 2011; Hamburg, Kocher, and Marson, 2012). Similarly, the VIA Technologies Nehemiah processor core includes an on-chip random number generator which is based on a series of oscillators where thermal noise alters the jitter so that the combination of the oscillators' output is random (Cryptography Research Inc., 2003). These integrated RNGs include conditioning circuits that process the output to remove biases.

With an integrated physical random number generator there is always an available source of entropy, and we are not limited to other sources of randomness that might not provide fresh entropy in a reliable and steady fashion. For instance, many servers are connected to a limited number of peripherals and do not have access to many random events like mouse motions. These servers can gather entropy only slowly and under severe constraints.

An integrated physical generator is a convenient addition, but it can also be complemented with the use of external RNGs. This can be a good solution if we do not trust the mechanism in the implementation, the vendor has not released it, or we suspect the chip might have a back door either by design or by sabotage (Becker et al., 2014).

Quantum random number generators are a particular case of physical TRNGs in which the data are the result of a quantum event. As opposed to other physical systems where uncertainty is a result of an incomplete knowledge of the system, true randomness is an essential part of quantum mechanics as we know it.

At first sight, physical RNGs seem more desirable than deterministic methods. However, there are inconveniences that have impeded their wider adoption. Some of the problems in physical RNGs are as follows:

(1) Limited generation rate: Physical RNG usually produce random numbers at a much smaller rate than

software methods. In many cases, there is a fundamental limitation in the rate of change of the sampled physical parameter. If the system is sampled at a high rate, there is not enough time for the system to change and the random numbers are not independent.

(2) It is difficult to give a convincing argument for the randomness of the data. There can be reasonable doubts about the randomness of the chosen physical phenomenon. Many physical random number generators rely on our ignorance to describe a physical process rather than in its intrinsic randomness.  
(3) Adding an external device is usually inconvenient.  
(4) Failures are difficult to detect. If a hardware random number generator fails during operation, it can be difficult to notice. Official recommendations suggest introducing a startup test, a total failure test, and an online test to check errors during operation (Schindler and Killmann, 2003; Killmann and Schindler, 2011).

The advanced quantum random number generators that have appeared with the impulse of quantum information research try to solve some of these shortcomings of traditional TRNGs. They offer a solution based on a trusted randomness source and many from the different implementations achieve fast generation rates, normally above the megabit per second, as seen in the multiple optical implementations described in Sec. VII. This faster rate allows new applications for TRNGs, such as online casinos and Internet gambling, which require a constant stream of random data and cannot use the slower methods of traditional daily or weekly lotteries (ID Quantique, 2011; PokerStars, 2016).

An important distinction between pseudorandom number generators and physical random number generators is the focus on product or process randomness (Eagle, 2005; Calude, 2015). For pseudorandom number generators we can evaluate only the output strings. We focus on the product of the ultimately deterministic algorithm and try to determine whether the string has all the properties of a random sequence. In order to determine if we have product randomness our options are limited to checking the output strings and submitting them to certain statistical test (see Sec. XII).

In physical random number generators we concentrate on process randomness. We look for a process that produces a random output and seek to obtain true random numbers from fundamentally random physical phenomena. Here randomness is usually taken as unpredictability.

While properly classical phenomena cannot be considered truly random, in common use, the terms physical and true random number generator are used interchangeably. Usually, it is fine to use an unpredictable physical system as a randomness source. However, there remains doubt whether the backing physical process is truly random or, at least, presents serious difficulties to be predicted, as it happens in a chaotic system, or we simply have a poor model and a better one could destroy the illusion of randomness. Quantum random number generators excel in that aspect: they use very well-defined inherently random processes as the source of their bits.

In the remainder of this section we consider how algorithmic and physical random number generation methods are employed in two of the most important families of applications for RNGs, simulation and cryptography. We go through

the particular requirements of randomness of each application and discuss the RNGs that are currently used in each case and the dangers of choosing a wrong randomness generation method. We then discuss random number generation in fundamental science experiments.

# B. Random numbers in simulation

Random numbers play an essential role in many scientific fields. They are fundamental ingredients in randomized algorithms, which have a wide range of applications in simulation, computing, number theory, and other branches of science and engineering (Karp, 1991; Motwani and Raghavan, 1996).

Simplified models of the reality are indispensable tools when we want to predict the behavior of complex systems that cannot be accurately described with a closed formula or when the computational needs for a full numerical analysis are too high. These models turn to random numbers to incorporate the combined effect of all that is left out. Thus, random number generation is needed in simulations in engineering, network, manufacturing, business, and computer science problems (Fishman, 1978; Bratley, Fox, and Schrage, 1987; Law and Kelton, 2000). The usual hypothesis is that we can obtain accurate results if we study enough cases chosen uniformly at random. These results, while probabilistic, are usually representative. We need, nevertheless, good random numbers. For instance, in the social sciences it is crucial to have a sound random sampling method to be confident that the study group is a faithful proxy for the whole population that we want to describe (Lohr, 2010).

A particularly important area is Monte Carlo and quasi Monte Carlo methods (Metropolis and Ulam, 1949; Niederreiter, 1978; Gentle, 2009) in which we can find the solution to a complex problem by averaging many random instances. These methods are effective in solving problems in statistical physics and numerical integration, where they are extensively used. If we sample the state space really at random, the result is likely to be correct, but, due to the high volume of data they require, these algorithms usually get their random numbers from a PRNG. When correctly done, this is enough. In simulation we only need a generator following the right statistics. However, certain generators that seem reliable under the usual tests (see Sec. XII) have undetected long range correlations that can result in a wrong solution. This is a general problem for congruential generators. Marsaglia (1968) showed that, choosing the right coordinates, consecutive random numbers from multiplicative congruential generators cluster into clear patterns. There are ways to correct this bias (Bauke and Mertens, 2007), but there exist many examples of simulations using faulty PRNG that gave results that, when compared to a known solution, were proved to be wrong, while a different, better PRNG gave the correct answer. There are numerous recorded cases of such failures for the Ising model (Kalle and Wansleben, 1984; Hoogland, Compagner, and Blöte, 1985; Parisi and Rapuano, 1985; Milchev, Binder, and Heermann, 1986; Ferrenberg, Landau, and Wong, 1992; Schmid and Wilding, 1996; Ossola and Sokal, 2004) and related problems (Grassberger, 1993; Shchur, Heringa, and Blöte, 1997; Ziff, 1998; Hongo, Maezono, and Miura, 2010).

Choosing a bad seed during initialization can also result in a correlated output (Matsumoto et al., 2007).

Because of these issues, there are some that have proposed to test PRNGs with the practical problems they are going to solve in addition to the standard statistical tests (Coddington, 1994; Vattulainen, Ala-Nissila, and Kankaala, 1994, 1995; Coddington, 1996). For Monte Carlo methods it is also a generally good idea contrasting the results of the same algorithm with different PRNGs, which are unlikely to have the same kind of bias.

True RNG are seldom used for simulation apart from seeding the PRNG. They face several challenges. They are slow when compared to the fastest PRNGs and their results are not easy to reproduce. This is a problem during debugging and replication. The only way to repeat the results of a TRNG is storing the sequence, which can be extremely large for a Monte Carlo run. They also need a fast method to interface with the processor. Anyway, true random number generators are adequate for simulation. While the generation rates of present quantum RNGs are still a few orders of magnitude below those of good-quality PRNGs, they are growing and QRNGs have shown they can be used, at a speed disadvantage, in Monte Carlo simulation (du Preez et al., 2011). Improvements in the generation speed could make them a viable alternative in certain applications.

# C. Random numbers in cryptography

Randomness is also a basic cryptographic primitive. Most of modern cryptography follows Kerckhoffs's principle (Kerckhoffs, 1883) and assumes any cryptographic system can fall into the hands of the adversary and that all the details of the system are perfectly known. Cryptographic systems are therefore open and all the security rests in the choice of a secret key. That way if a channel is compromised, the users just need to change that key. This has many advantages and is generally considered good practice.

In that context, it is of the utmost importance to choose a random key, which usually means choosing an  $n$ -bit string uniformly at random from all the key space. Similarly, random numbers with sometimes more relaxed randomness requisites are needed in other cryptographic protocols (Gennaro, 2006). Random numbers are required in nonces (numbers that must be used only once), in initialization vectors, in sequence numbers (Networking Working Group, 1996), in salt² to avoid dictionary attacks in hashed password lists and in digital

signatures, as well as in many interactive protocols (Goldreich, 1999).

Quantum cryptography also needs a reliable randomness source. Quantum key distribution is open to attacks if the measurement bases and the states are not chosen in a truly random way, as has been shown for the BB84 protocol (Bouda et al., 2012; Li et al., 2015).

In cryptography it is not enough that the random numbers are uniform. They must also be unpredictable and the generator should limit the damage of any compromised key. There are at least two new conditions for random numbers to be used in cryptography:

(1) Unpredictability (forward security): an attacker that knows the whole sequence cannot guess the next bit with a probability better than one-half.  
(2) Backward security: knowledge of a part of the sequence shall not permit an attacker to compute the previous values of the generator with better accuracy than guessing.

For practical purposes, both requisites of unpredictability can be reduced to polynomial-time unpredictability: that no algorithm can take a subsequence from the generator and guess efficiently (in polynomial time) any previous or following subsequences with better results than total random guessing. This concept is based on Yao's definition of indistinguishable sources (Yao, 1982).

Most PRNGs are not up to the task of generating cryptographically secure random numbers. For instance, the internal state in the Mersenne Twister can be deduced from a long enough output sequence (Matsumoto and Nishimura, 1998) and the output of a large class of general congruential generators can be predicted without even knowing the parameters in the generator (Krawczyk, 1990).

There are, however, established ways to use pseudorandom number generators in cryptographic applications. Algorithmic generators that fulfil the additional criteria are called cryptographically secure pseudorandom number generators (CSPRNGs). Two examples based on number theory are the Blum and Micali (1984) and the Blum, Blum, and Shub (1986) generators. We use the Blum-Blum-Shub generator as an illustration. The output bits come from the recursive formula

$$
X _ {i + 1} = X _ {i} ^ {2} \mod N \tag {2}
$$

for  $N = pq$  the product of two primes  $p$  and  $q$  congruent to 3 mod 4.  $X_{i}$  is the  $i$ th number used as the internal state. The algorithm has  $N$  and  $X_0$  as inputs and the  $i$ th output bit is the parity of  $X_{i}$  (or, in some variations, a few least significant bits). The initial state  $X_0$  should come from a TRNG. This generator has some desirable properties as long as certain common computational complexity assumptions hold. For instance, even if an attacker learned the internal state  $X_{i}$  at stage  $i$ , we keep unpredictability to the left (the preceding bits of the binary string are not compromised). Guessing  $X_{i-1}$  from  $X_{i}$  is computationally hard unless the quadratic residuosity problem can be solved in polynomial time. Later work showed that breaking the Blum-Blum-Shub generator is equivalent to factoring (Vazirani and Vazirani, 1985a). This is considered computationally secure in many cryptographic protocols. However, an attacker with a quantum computer that knows

$N$  could use Shor's algorithm for integer factorization to break the security of the generator (Shor, 1997).

There are also variations of the Mersenne Twister intended to make it secure for cryptographic use (Matsumoto et al., 2005, 2008). Other approaches to CSPRNGs use cryptographic protocols such as data encryption standard (DES) or advanced encryption standard (AES) as blocks that transform a string of bits using as their secret key a processed seed from the computer's entropy pool. An example is the random number generation recommendation for banking in the ANSI X9.17 key management standard (American National Standards Institute, 1985).

There are different standards and recommendations for the cryptographic use of random number generators in key generation (National Institute of Standards and Technology, 2001; Barker and Roginsky, 2012) and in financial systems (American National Standards Institute, 2006), with instructions on how to treat the sources of entropy for seeding PRNGs (International Organization for Standardization, 2011; Turan et al., 2016).

Cryptographical random number generators, as any critical part in a cryptographic protocol, can be subject to different cryptanalytic attacks (Kelsey et al., 1998). There are also some quantum attacks that offer a moderate advantage with respect to classical strategies (Guedes, de Assis, and Lula, 2013).

Certain generators are specifically designed for cryptography and are built to avoid common attacks. An example is the Fortuna pseudorandom number generator that uses multiple sources of entropy to reseed as frequently as possible so that, if the generator is compromised at some time, the previous output remains unguessable (Ferguson, Schneier, and Kohno, 2010). This and similar cryptographic generators are configurable and allow one to replace the protocols inside their constituent blocks.

The design of cryptographically secure RNGs is far from trivial. There are multiple cases of faulty implementations of RNGs that have led to serious vulnerabilities. One common pitfall is the failure to properly seed the generator. Even if the transformation on the seed is secure and cannot be inverted, if there is not enough entropy an attacker can launch a brute force attack and try all the possible seeds. The outputs can then be compared to the output of the generator and the attacker can predict which keys the user has generated. This has happened many times since the early attacks on the secure sockets layer (SSL) keys generated in the Netscape browser, which used predictable sources like the time of the day or process numbers to seed its generator (Goldberg and Wagner, 1996; Shepherd, 1996). Similarly, a bug in the OpenSSL library resulted in a seed of limited entropy that used as its only randomness source process identifiers, which have only  $2^{15}$  possible values (Ahmad, 2008). The resulting possible keys could be generated by brute force in a few hours. Poor initialization can also weaken the random numbers in operating systems like Windows 2000 (Dorrendorf, Gutterman, and Pinkas, 2009). A few more examples of vulnerabilities due to initialization problems or other bad quality random number generators are weak Rivest-Shamir-Adleman (RSA) key generation in network devices (Heninger et al., 2012; Lenstra et al., 2012), repeated or guessable keys produced inside smart

cards (Nohl et al., 2008; Bernstein et al., 2013; Courtois et al., 2013), and the predictable random sequences that are used for cryptographic purposes in Android (Kim, Han, and Lee, 2013; Michaelis, Meyer, and Schwenk, 2013).

In this respect, physical RNGs, including QRNGs, can serve as way to seed CSPRNGs, preferably as an additional source of entropy. There are still some important precautions. Certain attacks specifically target TRNGs (Zheng and Matsumoto, 1997; Soucarros et al., 2013) and they can be sensitive to environmental variables (Soucarros et al., 2011). There are already some proposals to test QRNG (Walenta et al., 2015) under the online test of the BSI AIS 20/31 standard from the German Federal Office for Information Security (Killmann and Schindler, 2011) to make sure they do not fail during operation. As long as these aspects are taken into account, the relatively high rate of QRNGs makes them also a viable option to directly generate keys, probably after some kind of postprocessing.

In fact quantum key distribution (QKD) (Bennett and Brassard, 1984; Ekert, 1991; Gisin et al., 2002; Scarani et al., 2009; Lo, Curty, and Tamaki, 2014) can be seen as nothing more than a sophisticated distributed secure random number generator that includes a physical method to generate entropy and a randomness amplification algorithm that weeds out the bits that could have been compromised (Owens, Hughes, and Nordholt, 2008).

In that interpretation, many quantum hacking methods can be considered as attacks to an RNG or to the randomness generation block inside the QKD system (Stipčević, 2014). For instance, in detector blinding attacks (Lydersen et al., 2010; Gerhardt et al., 2011), an attacker can selectively disable the detectors in the receiver and eliminate any randomness in the measurement, determining the result. Similarly, time shift attacks take advantage of different detection efficiencies with time to make measurement in a chosen basis more or less likely introducing a bias (Zhao et al., 2008) and attacks based on imperfect beam splitters perform a similar feat by introducing unbalances in the way the quantum states are directed to each measurement configuration (H.-W. Li et al., 2011).

QKD protocols assume they have access to true randomness and QRNGs are quite adequate for that purpose. We will see they are faster than alternative TRNGs, produce random numbers of good quality, and suppose small deviations from the usual configuration of the equipment (they can be built with the same technology and their cost is only a small fraction of the total).

# D. Random numbers in fundamental science

Finally, truly random numbers play a special role in experiments that try to determine the nature of the world. For philosophical reasons, in some proof of principle experiments we need to remove any possible bias when choosing a measurement or when making other decision. In this respect, quantum random number generators stand in a privileged position. Quantum mechanics is the only theory that, according to our understanding, offers true randomness.

This is particularly important in many experiments on the foundations of quantum mechanics, where many of the thought experiments that helped to shape our understanding

of the quantum theory have entered the lab and can be tested experimentally (Shadbolt et al., 2014). Quantum random numbers can also appear in any experiment where we want to be sure there is no hidden bias or that our decisions are independent from previous states of the system. Curiously, one of the early quantum random number generators based on radioactive decay, described in Sec. V, was designed as a way to remove bias in parapsychology experiments (Schmidt, 1970a, 1970b). Later, QRNGs have become part in experiments where randomness is a philosophical necessity.

Quantum random number generators are a good solution in experiments that test the predictions of the quantum theory. They can be built with equipment similar to that of the experiment or even be integrated into the experimental setup. While we must trust the inherent randomness of quantum effects, they can be instrumental in exploring other aspects of quantum mechanics like complementarity or nonlocality that are not directly dependent on the randomness of quantum measurement. Experimental tests of properties like the wave-particle duality usually require one to take random decisions in a short time and quantum random number generators can fulfil that mission.

Experimental tests of Bell's inequality (Brunner et al., 2014) need a random choice of basis which can be done with an external QRNG connected to a switch as in the experiments of Weihs et al. (1998) and Scheidl et al. (2010) that used the QRNG in Jennewein et al. (2000) or with a passive choice, where the quantum randomness comes from separating the paths of the photons in the experiment in a balanced beam splitter (Tittel et al., 1999), which can be equivalent in the right conditions (Gisin and Zbinden, 1999).

We also need true randomness for Wheeler's delayed-choice experiment in which a photon inside an interferometer can behave like a wave or a particle depending on whether we close the interferometer or not (Wheeler, 1978). If the choice is delayed to after the photon is inside the interferometer, the photon must be able to behave as both a wave and a particle<sup>3</sup> as the complete setup had not been decided when the photon entered it. From a fundamental point of view, it is crucial that the decision is made after the photon enters the interferometer. We need a fast and truly random number generator. The experiment in Alley, Jakubowicz, and Wickes (1984) used a single photon from a weak light source with a  $50\%$  probability of firing a detector connected to a switch and the experiments in Jacques et al. (2007, 2008) made this decision using a QRNG based on the measurement of the amplified shot noise of white light.

Other delayed-choice experiments are the ones based on entanglement swapping (Yurke and Stoler, 1992; Zukowski et al., 1993) following the proposal by Peres (2000) in which whether two photons are entangled or not is decided after they have been measured (Ma et al., 2012) and the quantum erasure experiments that erase path information (X.-S. Ma et al., 2013), in both cases using the QRNG of Jennewein et al. (2000).

# III. BLOCK DESCRIPTION

Physical random number generators can be divided into separate blocks with well-defined subtasks. The two most important blocks are the entropy source and the postprocessing stage. The entropy source consists of a physical system with some random physical quantity and the measurement equipment that reads these random variables. In digital random number generators we usually need to convert analog measurements into bit strings with the help of analog-to-digital converters. Measurement and quantization are noisy processes and there will be some contamination in what is called the raw bit string even if the measured quantity is truly random and free from correlations. The postprocessing block takes the raw bits and distills a shorter sequence without correlations.

The most important phase in postprocessing is randomness extraction. Randomness extractors are functions that transform the bits from the raw sequence into a uniform random sequence at the output with most or all of the randomness available in the input.

Figure 1 shows the block diagram of a typical physical random number generator. The exact parts vary from device to device. For instance, some physical random number generators are designed to produce raw sequences with negligible bias and forgo the postprocessing phase. There is a delicate balance in choosing an adequate postprocessing system. More involved randomness extraction methods usually allow one to minimize the amount of random bits that are thrown away, but are slower. The overall bit rate depends on whether the increased production of bits compensates or not for the slower processing circuit or if it is justified to use a faster but more complex hardware to remove biases from the raw bit sequence.

In this review, we concentrate on the different quantum systems that can work as an entropy source. Section V describes measurements of radioactive decay. Section VII explains the many possible sources of entropy available in quantum optics. Section VIII discusses alternative quantum systems that do not use light.

Section X gives a brief review on some classical post-processing algorithms used to remove existing biases and Sec. XI introduces different quantum protocols that can be combined with imperfect randomness sources to obtain uniform output strings.

![](images/b5928eeb491b670483180592de5e00f56dc83eaf0b7241996c3004f21764ff47.jpg)  
FIG. 1. Block diagram of a typical physical random number generator. A measurement system registers an unpredictable magnitude from a well-characterized physical system and converts the results into a binary raw bit sequence, which can still show some bias. The postprocessing stage extracts a smaller, ideally bias-free, random sequence assuming some bound to the amount of randomness of the raw sequence. The estimation usually comes from a thorough analysis of the original random physical system and the measurement errors.

Before describing the particular systems from which quantum random number generators obtain randomness, in Sec. IV we comment on the most common ways to measure entropy and the contexts in which each entropy measure can be applied. Some choose different criteria that will be mentioned when we describe the corresponding quantum random number generator.

In certain quantum random number generators, such as device-independent generators (Sec. IX.B), the physical measurement process and randomness estimation and extraction are intimately linked and we discuss them together.

# IV. ENTROPY ESTIMATION

Entropy in its many forms offers a convenient way to measure randomness. The different entropies give a mathematical measure for surprise (how unexpected a value is). We express entropy in bits, in the information theory sense, which is closely related to the concept of thermodynamic entropy but takes it to a more natural formulation for information processing and communications.

A simple interesting measure is the Shannon entropy (Shannon, 1948). For a random variable  $X$  with a probability distribution  $P_{X}$  so that  $P_{X}(x)$  is the probability of getting the outcome  $x$  from a discrete set  $\mathcal{A}$  (an alphabet) with  $N$  possible values for  $x$ , the Shannon entropy of  $X$ ,  $H(X)$ , is defined as

$$
H (X) = - \sum_ {x \in \mathcal {A}} P _ {X} (x) \log_ {2} P _ {X} (x). \tag {3}
$$

The Shannon entropy gives the average number of bits of information we can extract from a single outcome. For an alphabet of cardinality  $N = |\mathcal{A}|$  and a uniform probability distribution, all the results are equally likely and we need  $\log_2N$  bits to describe them. Imagine we place all the possible outcomes in a table and assign a  $\log_2N$ -bit string to each of them. In a uniform random process all the outcomes are equally "surprising" and we need to use all the bits. Less surprising distributions where some results are more likely than others would need, on average, less bits to be described. Table I shows an example of bit representations for the results of throwing a balanced and an unbalanced four-sided die (a tetrahedron).

The Shannon entropy offers a rough estimation of randomness. Ideally, we want to generate an almost uniform distribution with a Shannon entropy as close to  $\log_2N$  as possible. A higher Shannon entropy means we have a distribution closer to uniform and that we can extract more random bits from the process, but there are other entropy measures that can give us a more useful figure when deciding how to use a randomness extractor to make the most efficient use of the available randomness, as described in Sec. X.

An interesting generalization of the Shannon entropy is the family of Rényi entropies (Rényi, 1961). The Rényi entropy of order  $\alpha$  is defined as

$$
H _ {\alpha} (X) = \frac {1}{1 - \alpha} \log_ {2} \sum_ {x \in A} P _ {X} (x) ^ {\alpha}. \tag {4}
$$

TABLE I. Entropy calculation example for a fair and a loaded four-sided die. For each possible outcome of a throw (first column) there is an associated probability shown in the second column. The third column shows a possible way to assign a bit sequence to each outcome. For a balanced die (upper table) we have 2 bits of entropy  $H(X) = -4(1/4)\log_2(1/4) = 2$ . For a loaded die (lower table), we have an entropy  $H(X) = -(1/2)\log_2(1/2) - (1/4)\log_2(1/4) - 2(1/8)\log_2(1/8) = 1.75$ . For the given encoding, we need an average of  $1(1/2) + 2(1/4) + 2 \times 3(1/8) = 1.75$  bits to describe the result.

<table><tr><td colspan="3">Fair die</td></tr><tr><td>x</td><td>P(x)</td><td>Sequence</td></tr><tr><td>1</td><td>1/4</td><td>00</td></tr><tr><td>2</td><td>1/4</td><td>01</td></tr><tr><td>3</td><td>1/4</td><td>10</td></tr><tr><td>4</td><td>1/4</td><td>11</td></tr><tr><td colspan="3">Loaded die</td></tr><tr><td>x</td><td>P(x)</td><td>Sequence</td></tr><tr><td>1</td><td>1/2</td><td>0</td></tr><tr><td>2</td><td>1/4</td><td>10</td></tr><tr><td>3</td><td>1/8</td><td>110</td></tr><tr><td>4</td><td>1/8</td><td>111</td></tr></table>

The Shannon entropy corresponds to the Rényi entropy in the limit  $\alpha \rightarrow 1$ . For any distribution, Rényi entropies obey the inequality

$$
H _ {\alpha} (X) \geq H _ {\beta} (X) \tag {5}
$$

for  $\alpha \leq \beta$ . Entropies of a different orders appear in many security proofs and randomness bounds (Cachin, 1997).

A particularly useful quantity is the min-entropy  $H_{\infty}(X)$ , which comes from taking the Rényi entropy when  $\alpha \to \infty$ . Alternatively, it can be defined as

$$
H _ {\infty} = - \log_ {2} \left[ \max  _ {x \in A} P _ {X} (x) \right], \tag {6}
$$

where we take the logarithm of the probability of the most likely outcome. The min-entropy gives a lower, worst-case bound to all the Rényi entropies.  $2^{-H_{\infty}(X)}$  corresponds to the probability of guessing at the first attempt the outcome from measuring a random variable  $X$  with a known distribution. The optimal strategy is guessing the result is the most likely one. In the example given in Table I, for the uniform distribution the min-entropy is 2, but for the loaded die we have a value  $-\log_2(1/2) = 1$ . If we guess an outcome of 1 we are right half of the time.

In a distribution with min-entropy  $k$ , every possible outcome  $x$  has a bounded probability  $P_{X}(x) \leq 2^{-k}$ . Any probability distribution of min-entropy  $k$  can be written as a convex combination of distributions that are uniform for  $k$  bits. This gives an important interpretation of min-entropy as the number of uniform bits that can be extracted from a given distribution. Intuitively, if no single string is too likely, for every random outcome we can extract about  $k$  bits of "surprise," but no more (Chor and Goldreich, 1988; Zuckerman, 1990).

There are explicit constructions, like Trevisan's extractor (Trevisan, 2001) and derived functions (Shaltiel, 2004), that can give almost  $k$  bits with a probability distribution as close

to uniform as desired, provided there are some ancillary random bits of good quality. There are different kinds of randomness extractors (see Sec. X) in which min-entropy or derived quantities offer an upper bound on the number of available random bits.

Renyi entropies, including Shannon entropy and min-entropy, can be generalized to study joint distributions where part of the system is in the power of a legitimate user  $A$  and part of the system, which can be correlated to the first part, is in the possession of an eavesdropper  $B$ . In random number generation, the most useful quantity is conditional min-entropy. In the most general case, we can include distributions that come from quantum systems if we consider the density matrix  $\rho_{AB}$  of a state in the joint Hilbert space  $\mathcal{H}_{AB} = \mathcal{H}_A \otimes \mathcal{H}_B$  with a subspace that is restricted to  $A$ ,  $\mathcal{H}_A$ , and a subspace only  $B$  can access,  $\mathcal{H}_B$ . The conditional min-entropy of  $\rho_{AB}$  related to a reduced density state  $\sigma_B$  in  $\mathcal{H}_B$  is defined as

$$
H _ {\infty} (A | B) _ {\rho} = \sup  _ {\sigma_ {B}} (- \log_ {2} \lambda), \tag {7}
$$

where  $\lambda$  is the smallest real number for which

$$
\lambda I _ {A} \otimes \sigma_ {B} - \rho_ {A B} \tag {8}
$$

is non-negative (Renner, 2005) when  $I_{A}$  is the identity matrix corresponding to  $\mathcal{H}_A$  and we maximize over the density matrices  $\sigma_B$  with trace 1 describing the subsystem in  $\mathcal{H}_B$ . Conditional min-entropy gives how much information about the results of a measurement by  $A$  can be inferred from measurements on  $B$  alone. For classical distributions,  $2^{-H_{\infty}(A|B)}_{\rho}$  gives the probability of guessing the outcomes of  $A$  from our knowledge of  $B$  using the optimal strategy (König, Renner, and Schaffner, 2009). If there is no side information (the systems of  $A$  and  $B$  are uncorrelated), we recover the definition and interpretation of the min-entropy in Eq. (6).

When considering randomness extractors, it is also interesting to speak of the smooth min-entropy

$$
H _ {\infty} ^ {\epsilon} (A | B) _ {\rho} = \sup  _ {\tilde {\rho}} H _ {\infty} (A | B) _ {\tilde {\rho}} \tag {9}
$$

with a supremum taken over all the non-negative operators  $\tilde{\rho}_{AB}$  of trace 1 that are close to  $\rho_{AB}$  in the sense that  $\| \tilde{\rho}_{AB} - \rho_{AB}\| \leq \epsilon$  for the  $L_{1}$  norm  $\| A\| = \mathrm{tr}\sqrt{A^{\dagger}A}$  (König and Renner, 2011).

Instead of giving asymptotic parameters, such as traditional entropies, smooth entropies give results valid for a single sample of a distribution. In random number generators, smooth min-entropy is useful as an estimator of the amount of random bits we can extract from a randomness source that might be correlated with an external attacker. Smooth min-entropy gives a tight bound on the length of the bits that a randomness extractor can produce from a given joint distribution and still give an output as close to uniform as desired and uncorrelated to any external system (Renner, 2005; König, Renner, and Schaffner, 2009).

For a general unknown source, estimating the min-entropy is far from trivial. The problem is intractable for

any reasonable sampling circuit with limited size (Lyngsø and Pedersen, 2002; Watson, 2016). We can only determine min-entropy from measurement inefficiently. If our randomness source is stable and faraway bits are independent, this cost can be paid just once during characterization. Normally, physical random number generators use conservative, worst-case bounds for the min-entropy based on a deep analysis of the physical origin of the randomness and there are standardized methods for online estimation (Turan et al., 2016). In that respect, quantum random number generators offer a clear advantage: their source of randomness is usually a well-defined quantum phenomenon. Quantum theory gives very accurate predictions. When compared to other random number generators that gather noise from complex processes such as atmospheric noise, quantum random number generators have the virtue of a precise description of the randomness source which can be used to derive limits to the available min-entropy, even accounting for additional classical noise or the presence of eavesdroppers.

Nevertheless, even for these well-characterized quantum randomness sources, hidden correlations remain a challenge. There might be memory effects or correlations between consecutive runs of the quantum experiment that gives our random numbers and we must take due care to ensure independence and the lack of any experimental bias.

# V. QUANTUM RANDOM NUMBER GENERATORS BASED ON RADIOACTIVE DECAY

# A. The first quantum random number generators

With the rise of computer simulation during the second half of the 20th century, there was a growing need for electronic random number generators (Hull and Dobell, 1962). At that time, it was common to find tables of random numbers. The most famous of such compilations is probably the book "A million random digits with 100 000 normal deviates" from the RAND Corporation (RAND Corporation, 1955). The numbers in the book were generated using an electronic roulette wheel and were available in punched card format to allow easy interfacing with computers. There also appeared many electronic random number generators designed to be connected to computers or output devices like teleprinters (Sowey, 1972).

It was only natural for some researchers to turn to the intrinsic source of randomness of quantum phenomena (Isida and Ikeda, 1956; Manelis, 1961; Schmidt, 1970b; Vincent, 1970). Radioactive decay was a particularly accessible source of true randomness. Geiger-Muller (GM) tubes were already sensitive enough to capture and amplify  $\alpha$ ,  $\beta$ , and  $\gamma$  radiation and reliable, well-characterized radioactive samples were available. For simplicity, most radioactivity-based quantum random number generators were based on the detection of  $\beta$  radiation (emitted electrons).

In a GM detector a single particle produces an ionization event that is amplified in a Townsend avalanche (Friedman, 1949). The result is a device that, when correctly configured, produces a pulse for each detected particle. The probability of any given atom to decay in a time interval  $(t,t + dt)$  is given by an exponential random variable so that  $P(t)dt = \lambda_{m}e^{-\lambda_{m}t}dt$  for a material with a decay constant  $\lambda_{m}$ . If the sample retains

many of its original atoms (we are in times much smaller than the half-life) and the sample-detector system undergoes practically no change during our time interval (the position of the sample is constant, the gas in the GM tube does not become contaminated, etc.), the time between detected pulses is also an exponential random variable. The times are independent from previous results and the number of pulses that arrive in a fixed time period follows a Poisson distribution. The exact rate depends on many factors, but it can be determined experimentally and we can be satisfied that the pulses arrive at independent times (Silverman et al., 1999). The probability of finding  $m$  pulses in an observation period of  $T$  seconds is

$$
P _ {m} (T) = \frac {(\lambda T) ^ {m}}{m !} e ^ {- \lambda T},
$$

where  $\lambda$  gives the mean number of pulses we detect in 1 s for our source and corresponds to the parameter of the exponential distribution.

The QRNGs we describe in this section are the forerunners of the present day optical QRNGs we will see in Sec. VII that use similar concepts and circuits, but replace the radioactive source and the GM counter with photon sources and detectors.

The first QRNGs based on radioactive decay share many common elements. Most use digital counters to convert the pulses from the detector into random digits. A digital counter increases its output value by 1 when it receives a pulse at its input and can be reset to start the count from 0. Another key element is timing with a digital clock. These QRNGs can be best explained if we speak in terms of fast and slow clocks to describe clocks with a frequency  $\nu$  that is significantly greater or smaller than the mean rate of detection. A fast clock, with  $\nu >\lambda$ , generates many pulses between Geiger counts and when a slow clock, with  $\nu < \lambda$ , produces a pulse, there has been enough time to have registered many counts in the GM detector.

With these elements, the randomness in the time of arrival can be converted into random digits in a few different ways. The generators of Isida and Ikeda (1956) and Vincent (1970) use a counter driven by a fast clock that is read and then reset to zero every time we get a count on the detector. The value of the counter at the moment of the detection is used to produce the random number. Figure 2 gives a graphical description of the method. The distribution of values is not uniform and some correction is necessary. If we are producing decimal digits, we can take the least significant figure (Isida and Ikeda, 1956). The equivalent method for binary sequences is looking

![](images/bdb9b1fdf807ecf856e337ce7ecdf290d35ff589ab1fc80900b8c725278ac99d.jpg)  
FIG. 2. Fast clock method: A fast clock (down) is used to increase a counter. Whenever a detection is made (up), the counter is read and reset, generating one random number.

![](images/b12f50209538d7c566d111cfec466ff0331d854a2cd72303d369517f64453594.jpg)  
FIG. 3. Slow clock method: The Geiger detector is read at fixed intervals, generating a random number that equals the number of detections during the period.

at the parity of the value of the counter, checking if the number of counted pulses is even or odd (Vincent, 1970). This kind of correction draws from previous results for true random number generators that face similar problems (Thomson, 1959).

A second option is to use a slow clock to determine when to read the counter. In the generator of Schmidt (1970b), the pulses from the GM detector increase the value of a counter. When the slow clock produces a new pulse, the value of the counter is used as a random digit and the count starts again from 0. The output corresponds to the number of particle counts in each clock period. We restrict to a counter that generates values from 0 to  $M - 1$ , a modulo  $M$  counter. When  $M = 2$  we have a binary random number generator. The distribution of the sampled digits is not uniform, but if we take the modulo  $M$  addition of multiple outputs, we can obtain a distribution with as small a bias as desired. This is called "contraction" and was discussed in detail by Schmidt (1970b). Figure 3 shows an example of this generation method.

Radioactive decay has also been used to generate white noise for analog computers (Goodyear Aircraft Corporation, 1954; Howe, 1961; Manelis, 1961). Random noise generation was important, among others, in the analog calculations in airplane design simulations. It also has applications as a test signal and, generally, in communications and simulation problems where a broadband signal is necessary (Gupta, 1975). In this case, the pulses from the GM detector trigger a change of state in a voltage signal. Whenever a particle is detected the signal goes from high to low voltage or from low to high. The resulting random signal is called random telegraph noise (Rice, 1944). In this case we do not want a binary signal, but Gaussian noise. Instead of sampling, the signal is directed to a low pass filter to complete the noise generator.

# B. Evolution

After the initial proposals, there have been different refinements to the basic concept. QRNGs based on radioactive decay are still popular. A good example is the web-based random number server HotBits (Walker, 1996) that has been working since 1996. In the HotBits generator, the random times of arrival of the radiation to the Geiger counter give pairs of intervals of random length. The time between two consecutive pulses is stored as  $t_1$  and compared to the time between the next two pulses  $t_2$ . The random bits come from comparing the times. If  $t_1 > t_2$  we output a 0 bit and if  $t_1 < t_2$  we output a 1. The generator reverses the criterion for 0 and 1 for every time pair in order to compensate for small systematic biases that might favor slightly unbalanced intervals. This

provides a crude correction for small problems like, for instance, the loss of radioactive material due to radioactive disintegration that makes the second interval shorter on average by a very short time. Figure 4 gives a graphical description of the method.

Some modern proposals replace Geiger counters with semiconductor detectors. Semiconductor devices such as positive-intrinsic-negative photodiodes can also capture the radiation from radioactive decay (Lutz, 2007; Knoll, 2010). Semiconductor detectors are convenient, as they do not require the same high voltage as Geiger tubes. The resulting signal is weaker than that of GM counters, but there are low noise amplifiers that can produce output pulses of a few volts of amplitude. While they can have different sensitivities and need calibration, for the generation of random numbers the important property is not as much determining the actual rate of the particles coming out of the source as it is registering random events.

Using off-the-shelf semiconductor devices can simplify the design of random number generators. One example of such generators was given by Alkassar, Nicolay, and Rohe (2005) with a variation of the time interval method. Instead of comparing the time between pulses, the system reads a fast clock every time a pulse arrives. If the clock is in a high state (in the high voltage level of the clock cycle) at the moment of arrival the generator outputs a 1. If it is low it outputs a 0. For a good time resolution, the least significant bit of the digitized time should be random and there is no need for postcorrection.

Two other proposals for QRNGs that use semiconductor detectors with radioactive decay appear in Duggirala, Lal, and Radhakrishnan (2010). The first proposal tries to address the problem that in QRNG we have access to an exponential random variable, the time of arrival, or a Poisson random variable, the number of pulses in a fixed time interval. But, in many occasions, RNGs are required to produce uniform random numbers. An exponential random variable of parameter  $\lambda$  can be converted to a uniform random variable if we compute

$$
U = e ^ {- \lambda E}, \tag {10}
$$

where  $U$  is the uniform distribution and  $E$  is the exponential distribution. The first proposal of Duggirala, Lal, and Radhakrishnan (2010) addresses this with an  $RC$  circuit. They use a semiconductor detector whose output pulses trigger the fast discharge of a capacitor. The voltage at the  $RC$  circuit when a pulse arrives is the output variable. This approach has several limitations. It needs specialized

![](images/d9bc1595a4a770be95661b3d710cabf749490bafffb2b860b541a631f9c4a7c9.jpg)  
FIG. 4. Time difference method: This method compares the time between two events in the Geiger detector. If  $t_i < t_{i+1}$  then a bit with value of 1 is generated. Otherwise, the bit generated will be zero.

hardware to transform the voltage to the output and has problems with noise. For that reason there is an alternative proposal with an approach similar to Isida and Ikeda (1956) and Vincent (1970), where a fast clock  $\nu \gg \lambda$  drives an  $N$ -bit counter which is read when a pulse arrives. Here the clock is supposed to be fast enough to guarantee the samples are uniform in the  $2^{N}$  values.

# C. Limitations

While QRNGs based on radioactive decay are a good way to obtain high quality true random numbers, they have some drawbacks that limit their practical use. An important barrier is the low bit rate they can achieve, usually below a few hundred kilobits per second.

The first problem is the need for a radioactive source. In principle, all decay-based QRNGs could work on background radiation. Unless it is isolated, a detector will count stray cosmic rays, radiation from radium, thorium, or other radioactive materials in the Earth's crust or particles from radon on air. However, natural activity rarely produces enough particles to cause more that a few counts per second. This poses a fundamental problem for the widespread use of radioactive decay QRNGs. In order to achieve a fast rate, the QRNG needs a highly radioactive source. The reviewed generators used cobalt-60 (Isida and Ikeda, 1956), strontium-90 (Schmidt, 1970b), cesium-137 (Walker, 1996), americium-241 (Alkassar, Nicolay, and Rohe, 2005), or nickel-63 (Duggirala, Lal, and Radhakrishnan, 2010). This is highly inconvenient and requires improved safety measures. While  $\alpha$  sources like americium are easier to isolate and are common in smoke alarms, the additional precautions prevent straightforward computer integration and this approach works well only for dedicated isolated servers like HotBits (Walker, 1996).

A second limitation to the generated bit rate is the dead time of the detectors. In Geiger counters the avalanche that amplifies each count ionizes the gas inside the GM tube. The avalanche stops when the positive ions surround the cathode inside the tube. These ions prevent further avalanches until they have returned to their normal state (Friedman, 1949). The dead time is the minimum time for the GM tube to recover its full detection capability and can go from tens of nanoseconds to a few microseconds. This limits the count rate to the MHz range. Semiconductor detectors also need to replenish the carriers after each detection and have dead times in the microsecond range.

Dead time and other sources of nonuniformity need to be corrected when generating random bits. Vincent (1971) described some important cautions in a follow-up paper to his original generator proposal. In general, the quality of the generated bits will be good and, when there is some residual bias, there exist simple postprocessing methods to recover a random output.

A final problem specific to semiconductor detectors is the damage they suffer from radiation. Geiger tubes also degrade with time, but the effect of radiation on them has been extensively studied, while semiconductors used specifically for radiation detection are relatively new. As long as the damage gives a progressive and slow reduction in efficiency, the output would retain randomness, but more studies on the long term behavior of these detectors are needed.

Despite these constraints, radioactive decay is a suitable source of randomness for low speed applications. It can, for instance, be used to provide entropy for the seed of pseudorandom number generators. For more demanding systems that require high bit rates or when we want to avoid radioactive sources, the recent optical QRNGs described in Sec. VII are good substitutes.

# VI. RANDOM NUMBER GENERATORS BASED ON NOISE

Noise in electronic circuits is one of the preferred sources of entropy in classical physical random number generators. Noise appears as an unwanted effect in electronic systems of all kinds and it is readily available. A typical random number generator using noise is shown in Fig. 5.

The noise source is represented as a resistor, but other elements can take its place. A Zener diode operated in the reverse breakdown region is another popular choice. In this scheme, voltage fluctuations due to noise are amplified and compared to a threshold to generate random bits. For a threshold of  $0\mathrm{V}$ , we can sample the amplified noise periodically and assign a 0 if we find a negative voltage and a 1 to a positive voltage.

If, instead of sampling, we generate a pulse every time the voltage from a white noise source crosses the threshold, the output will be a series of pulses with times of arrival that correspond to a Poisson distribution and we can use any of the methods described in Sec. V to produce random sequences. The electronic noise circuit replaces the Geiger counter in an otherwise unchanged system. In fact, many proposals for QRNG based on radioactive decay discuss both methods in parallel (Vincent, 1970; Gude, 1985).

There are multiple examples of true random number generators based on this electronic noise such as those in Holman, Connelly, and Dowlatabadi (1997) and Petrie and Connelly (2000) to name a few.

Noise in those systems comes fundamentally from two sources, shot, or Schottky, noise (Schottky, 1918) and thermal, or Johnson-Nyquist, noise (Johnson, 1928; Nyquist, 1928), with flicker noise contributing sometimes at low frequencies. Shot noise generates from quantum effects due to the granularity of the current. Currents are formed by discrete carriers and show quantum fluctuations. Thermal noise comes

![](images/1a941ff1141c253bcd703ed603441741f00575cc2a6650d872a8786817e4b081.jpg)  
FIG. 5. Conceptual representation of a typical noise-based random number generator. The voltage coming from a source of white noise is amplified and compared to a threshold in a comparator to produce a digital signal with random transition times. This signal can be sampled or processed later to give a random bit sequence.

from thermal agitation of the carriers and is produced by statistical motion that depends on the temperature. In practice, both noises tend to appear side by side and are difficult to isolate. In many cases the frontier between shot and thermal fluctuations is blurry (Landauer, 1993).

In this review, we will not discuss in detail random number generators based on electronic noise. While electronic noise coming from shot fluctuations can be rightfully said to be quantum (Reznikov et al., 1998), it is usually not well characterized and separated from thermal noise, it is subject to many environmental fluctuations, and can show memory effects (Stipčević, 2012). Somewhat arbitrarily, we choose to concentrate on generators where the quantum effects are well isolated and we have a higher degree of control. Unless there is some interesting effect, we will not discuss true random number generators where quantum noise is only an unquantified part of the total available randomness.

There are a few interesting exceptions. Certain commercial quantum random number generators use electronic noise in semiconductors. For ComScire's QRNG there is a detailed estimation of the quantum entropy gathered from shot noise in metal-oxide-semiconductor (MOS) transistors (Wilber, 2014). Likewise, under the right conditions, Zener diodes can be operated in a regime where quantum shot noise dominates (Somlo, 1975; Stipčević, 2004).

# VII. OPTICAL QUANTUM RANDOM NUMBER GENERATORS

Most of the existing QRNGs are based on quantum optics. The inherent randomness in many parameters of the quantum states of light allows for a rich choice of implementations. Light from lasers, light emitting diodes, or single-photon sources is a convenient and affordable substitute for radioactive material as a source of quantum randomness and there are many available detectors. In this section, we study some of the most common ways to harness quantum light to produce random bits.

First, we give an overview of the concepts of quantum optics that appear in the generators. Then, we propose a classification of optical quantum random number generators (OQRNGs) based on the generation mechanism. Table II gives a summary of the covered optical generators with some representative examples, the typical bit rates, and the limitations of each kind of generator.

# A. Quantum optics in random number generators

The optical field can be described at the quantum level in terms of photons (Klauder and Sudarshan, 1968; Loudon, 2001). From the many possible families of quantum states, Fock states and coherent states give the most relevant description of the quantum states of light in random number generators. Fock states, or number states, are described as states  $|n\rangle$  that contain  $n$  photons sharing a mode (they have the same frequency, polarization, temporal profile, and a common path). Coherent states, which share many properties with classical light, can be written as a superposition of number states

TABLE II. Summary of the optical methods for quantum random number generation. The table gives the section where we describe the details of each implementation, the principle of operation, a few representative examples, the order of magnitude of the typical bit rates of each generator, and a list of the most important limitations.  

<table><tr><td>Type (Sec.)</td><td>Physical principle</td><td>Representative examples</td><td>Rate (order)</td><td>Challenges</td></tr><tr><td>Branching path (VII.B)</td><td>Path superposition + measurement</td><td>Jennewein et al. (2000)</td><td>Mbps</td><td>- Unbalanced detectors.
- Detector dead time.</td></tr><tr><td>Time of arrival (VII.C)</td><td>Time of arrival statistics</td><td>Stipčević and Rogina (2007), Wayne et al. (2009), and Wahl et al. (2011)</td><td>Mbps</td><td>- Time precision.
- Detector dead time.</td></tr><tr><td>Photon counting (VII.D)</td><td>Photon number statistics</td><td>Fürst et al. (2010) and Ren et al. (2011)</td><td>Mbps</td><td>- Photon resolving capability.
- Detector dead time.</td></tr><tr><td>Attenuated pulse (VII.E)</td><td>Binary measurement of coherent states</td><td>Wei and Guo (2009a)</td><td>Mbps</td><td>- Source instability.
- Detector dead time.</td></tr><tr><td>Vacuum fluctuations (VII.F)</td><td>Shot-noise measurement</td><td>Gabriel et al. (2010), Shen, Tian, and Zou (2010), and Symul, Assad, and Lam (2011)</td><td>Mbps-Gbps</td><td>- Classical noise.
- Postprocessing.</td></tr><tr><td>Phase noise (VII.G)</td><td>Laser phase noise</td><td>Guo et al. (2010), Qi et al. (2010), and Jofre et al. (2011)</td><td>Gbps</td><td>- Phase drift.
- Pulse repetition rate.</td></tr><tr><td>Amplified spontaneous emission (ASE) (VII.H)</td><td>Amplitude fluctuations in ASE noise</td><td>Williams et al. (2010) and Argyris et al. (2012)</td><td>Gbps</td><td>- Sampling or digitization.
- Postprocessing.</td></tr><tr><td>Raman scattering (VII.I)</td><td>Interaction with phonon fluctuations</td><td>Bustard et al. (2011) and Collins et al. (2015)</td><td>kbps-Mbps</td><td>- Raman gain (stimulated).
- Detector dead time (spontaneous).</td></tr><tr><td>Optical parametric oscillators (OPOs) (VII.J)</td><td>Bistability in optical parametric oscillators</td><td>Marandi et al. (2011) and Marandi, Leindecker, Vodopyanov, and Byer (2012)</td><td>kbps</td><td>- Cavity decay time.
- Pump repetition rate.</td></tr></table>

$$
| \alpha \rangle = e ^ {- | \alpha | ^ {2} / 2} \sum_ {n = 0} ^ {\infty} \frac {\alpha^ {n}}{\sqrt {n !}} | n \rangle , \tag {11}
$$

where  $\alpha$  is a complex number. The amplitude  $|\alpha|^2$  corresponds to the mean photon number of the state. Weak laser light is an excellent approximation to a coherent state. We can also use the coherent states from a laser to produce a proxy for single-photon states by choosing a low enough intensity, as is usual, for instance, in quantum key distribution with typical values of  $\alpha$  around 0.1.

In many applications we are interested only in producing uncorrelated single photons. In that case, attenuated light from a light emitting diode (LED) can be valid as long as we generate photons with a separation larger than the coherence time of the source.

There are many different technologies that can generate single photons and detect them (Buller and Collins, 2010; Eisaman et al., 2011). Photomultiplier tubes (PMTs), single-photon avalanche photodiodes (SPADs) operating in the Geiger mode or superconducting nanowire detectors are some of the most popular detectors, but there is a growing number of alternatives (Hadfield, 2009). For instance, there have been important advances in silicon detectors (Ghioni et al., 2007) that open the door to integration in electronic circuits and in superconducting nanowire single-photon detectors that extend the high-efficiency detection wavelengths to the near infrared (Marsili et al., 2013).

Traditionally, while binary decisions between no photons and one or more photons are relatively easy to take, single-photon detectors have limited photon counting capabilities. There are new improved detectors, but their cost is still high and most applications use a binary approach to photon detection. Another limitation to most single-photon detectors is the time they need to recover after a detection, known as dead time. We later see how these limitations affect our quantum random number generators.

# B. Branching path generators

OQRNGs take advantage of the random nature of quantum measurement. In a large number of quantum random number generators this measurement is taken over photons in a superposition of two or more paths. For instance, if we define a state  $|1\rangle_1|0\rangle_2$  which represents one photon in the first of two possible paths and a state  $|0\rangle_1|1\rangle_2$  with the photon in the second path, we can prepare a superposition

$$
\frac {\left| 1 \right\rangle_ {1} \left| 0 \right\rangle_ {2} + \left| 0 \right\rangle_ {1} \left| 1 \right\rangle_ {2}}{\sqrt {2}}. \tag {12}
$$

Measuring that state with a detector at the end of each path will result in a click in just one of the detectors with a probability one-half for each path. There are many quantum optics experiments that generate similar states in Mach-Zehnder interferometers and related optical setups.

![](images/b2ec59822b0525ac95f60258cd59e05dc3c97cdc4c9cc279c3cf14f6532dbcb6.jpg)  
FIG. 6. A weak light source sends a state with one photon to a balanced beam splitter. The path the photon takes at the output is random and there will be a detection with the same probability at each detector. We consider that a click on detector  $D_0$  is recorded as a 0 bit and a detection in  $D_1$  is a 1.

Figure 6 shows the archetypal QRNG that uses quantum measurement with detectors in different positions as proposed for the choice of basis in  $\mathrm{QKD}^4$  (Rarity, Owens, and Tapster, 1994). In this configuration, we have a balanced beam splitter with equal transmissivity and reflectivity  $T = R = 1/2$  so that classical light entering any of the two input ports would be divided into two streams of the same optical power, half going through and half reflecting. If we have a single photon in one input and the vacuum in the second, we cannot divide the power and we have the desired path superposition. Conceptually, the simplest way to produce random numbers from this path division is placing two detectors  $D_0$  and  $D_1$ , one for each output, and generate a bit every time we detect a photon. Clicks in  $D_0$  would produce a 0 bit and clicks in  $D_1$  would produce a 1. Optical QRNGs using spatial superpositions usually apply variations on this basic scheme. In fact, in the original QKD application (Rarity, Owens, and Tapster, 1994) the random number generator was not fully implemented as a separate device controlling the measurement basis in the receiver. Instead, they used a passive implementation where the beam splitter took the input state and sent it with equal probability to one of two measurement setups, one for each possible basis. A complete implementation with a beam splitter and two photomultiplier tubes as detectors was first deployed as a subsystem in the experimental implementation of a Bell test (Weihs et al., 1998) and later developed as a standalone device (Jennewein et al., 2000) with some modifications. The most important difference is the way the random sequence is created, with a random digital signal as an intermediate step. In the modified model, detections in  $D_1$  take a digital signal to a high level and detections in  $D_0$  to a low level. The result is a random signal with changes in a time scale of the order of the inverse of the mean photon detection rate. If we sample this signal with a clock with a frequency sufficiently below the photon detection rate,

assigning a binary 0 when the state is low and 1 for a high state, we obtain a constant stream of random bits. The same procedure was tested with polarized photons in a linear  $45^{\circ}$  state and a polarizing beam splitter with essentially the same results. Wang, Longo, and Li (2006) took an alternative on polarization to path conversion with a weak laser source with linear polarization attenuated to the single-photon level and a Fresnel prism that separates the positive and negative circular polarization components and directs them to two avalanche photodiodes. This kind of polarization generator can be modified to provide adjustable probabilities for each bit value if we include an electronically controlled polarizer at the source, such as in the fiber-based QRNG of Xu et al. (2015) or the decision making system in Naruse et al. (2015), which adapts the probability to previous results.

Other generators are implemented in optical fiber systems where a weak light pulse is directed to a balanced fiber coupler connected to two detectors. Two examples are the generators in Soubusta, Haderka, and Hendrych (2001) and Soubusta et al. (2003), which use a pulsed laser source that produces, after a tunable attenuation circuit, a coherent state with an amplitude greater than 1 that maximizes the random bit generation rate.[5]

There are also implementations based on polarization inside optical fiber, with sources that are either single-photon states or polarization entangled states

$$
\frac {\left| H \right\rangle_ {1} \left| V \right\rangle_ {2} - \left| V \right\rangle_ {1} \left| H \right\rangle_ {2}}{\sqrt {2}} \tag {13}
$$

that are a superposition of horizontally polarized photon states  $|H\rangle$  and vertically polarized photons  $|V\rangle$  (Fiorentino and Beausoleil, 2006; Fiorentino et al., 2006, 2007; Bronner et al., 2009). The generators with entangled states produce the photons in nonlinear crystals and use coincidence detectors. One of the photons can be used as a herald or we can watch for anticorrelated polarization measurements in the different paths.

QRNGs with optical path branching can show a few problems. All types of photodetectors have some kind of dead time after a click. This can generate anticorrelation of neighboring bits. A detection at some time makes it less likely to find a photon immediately after due to the "blunted" sensitivity of the detector before full recovery. Also, for real detectors and beam splitters we find slightly different detection efficiencies and coupling ratios that can introduce some bias. There are a few other concerns: afterpulsing can create correlated bits, pulses with multiple photons can produce simultaneous detections, and the presence of dark counts means there will be occasional clicks when there are no photons. In practice, these effects, particularly dead time, limit

the maximum generation rate to a few Mbps, which could be improved with detectors with a smaller recovery time.

There are many ways to counteract these problems. For instance, the generator in Jennewein et al. (2000) includes a setup phase in which the tube voltage and the detection threshold of the photodetectors can be adjusted to compensate detection efficiency and path coupling differences. Another popular method is applying an unbiased algorithm that distills a random sequence at the cost of losing some bits. We discuss unbiaseding in more detail in Sec. X.

If we convert path superpositions into time superpositions we can use one detector instead of two, or more, detectors, and avoid problems caused by having different detection efficiencies and dark count numbers. That is the approach in Stefanov et al. (2000) where weak light from a timed pulsed laser inside an optical fiber is coupled into two fibers of different length connected to the same detector. The additional delay in one path permits one to distinguish the route of the photon. The whole attenuation is designed to make each path equally likely.

The random bit generation rates can improve if the generator measures more than two possible paths. Each measurement then gives more than one random bit.  $W$  states of the form

$$
\left| W _ {n} \right\rangle = \frac {\left| 1 0 \cdots 0 0 \right\rangle + \left| 0 1 \cdots 0 0 \right\rangle + \cdots + \left| 0 0 \cdots 0 1 \right\rangle}{\sqrt {n}} \tag {14}
$$

can be created by branching the photon path many times and giving the desired statistics. This approach takes more complex devices, but integrated optical circuits inside silicon chips can offer an economical and scalable alternative. Integrated circuits show less variability and the optical couplers that replace the beam splitters show smaller deviations from a perfectly balanced device. There have been experimental demonstrations of integrated generators with eight outputs that can produce 3 bits per each measurement, with potential for straightforward extension to 16 outputs (Gräfe et al., 2014).

Another important point is the choice of photon sources. In many of the reviewed generators, the photons come from LEDs. In order to guarantee independent photons, the rate is limited to be much smaller than the coherence time, which is usually not a problem as the limiting factor tends to be the dead time of the detectors. A common alternative is using weak laser light. However, it can be interesting to study other photon sources. The effect of a beam splitter on the different quantum states of light is well known (Fearn and Loudon, 1987; Ou, Hong, and Mandel, 1987; Prasad, Scully, and Marthienssen, 1987) and the resulting counting statistics can be used in a variety of generation schemes. There are results that suggest that true single-photon sources, which show photon antibunching, can increase the rate of random bits when compared to coherent light from lasers. Brighter sources have a faster photon rate and, in those conditions and once all the effects are considered, single-photon sources offer the best overall random bit rates (Oberreiter and Gerhardt, 2016).

Finally, there are QRNGs that give up beam splitters altogether. These generators use the natural spatial uncertainty

in the generation process. For instance, the commercial Quantis RNG has two integrated detectors placed in positions where the spatial profile of a light source has an equal amplitude (Ribordy, Guinnard, and ID Quantique, 2009).

A detector array allows a higher generation rate with more than 1 bit per detection. In that case, there must be some compensation for the nonuniform spatial profile of most photon sources. An early incarnation of this concept was the optical random number generator of Martino and Morris (1991) that used photon counting detectors with levels around the thousands of photons and needed involved calibration procedures. More recent OQRNGs use detectors with single-photon precision. One of such generators uses a microchannel plate detector and a wedge and strip anode to assign two coordinates to the place where a photon from an attenuated LED reaches a photocathode (Qiurong et al., 2014). Then, the random bit sequence is extracted from the position using Huffman coding to compensate for nonuniformities.

Other implementations use an integrated array of SPADs, combined with postprocessing (Burri and Stucki, 2013; Stucki et al., 2013; Burri et al., 2014). A weak light source produces clicks in random positions of the array. We can assign a 1 to the pixels that find a photon and a 0 to the pixels that do not click. Even if the distribution of bits in the discrete 2D grid of the detectors is not uniform, we can extract a random sequence if we compare two neighboring pixels, which should have almost the same probability of detecting a photon, and then only accept results that are different for each pixel, giving one of them as the output. Alternatively, we can use the whole string from the array as the input of a randomness extraction algorithm. In these generators, apart from the usual dead time, afterpulsing and dark count concerns, we have to contemplate the possibility of crosstalk between detectors. However, the effects of crosstalk can be minimized with a proper design.

# C. Time of arrival generators

There are also multiple ways to use the randomness in photon detection times to generate random bits. The OQRNGs in this and the following section are usually based on the same principles as the QRNGs that detect radioactive decay we discussed in Sec. V. In fact, one of the earliest proposals for this kind of quantum random number generator was a random pulser that tried to simulate the arrival of radioactive counts in order to calibrate nuclear instruments (Takeuchi and Nagai, 1983). Some methods are essentially the same as their Geiger counter predecessors but replace radioactive materials with light sources, which can achieve much higher bit rates. Photon production is faster and less problematic and the maximum bit rate is now limited by the capabilities of the detectors instead of the generation speed.

The basic QRNG using time has a weak source of photons, a detector, and timing circuitry that registers either the precise time of each detection or the number of clicks in a fixed period of time. In short time periods with one or only a few photons on average, the photons coming both from LED incoherent light and from the coherent states from a laser arrive at the detector following an exponentially distributed time  $\lambda e^{-\lambda t}$  for an average number of photons per second  $\lambda$ . The time between two photodetections is the difference of two exponential

random variables, which is also exponential. In that case, we can compare the time differences between the arrival of consecutive pulses and compare two time differences  $t_1$  and  $t_2$ . We can assign a 1 if  $t_2 > t_1$  and a 0 if  $t_1 > t_2$ . This gives a uniform random bit.

In time of arrival generation, precise time tagging becomes important. Measurement will always have a limited precision and the effects of digitizing the time intervals can be noticeable. Instead of having real times  $t_1$  and  $t_2$ , we have integers with the number of the counted clock periods  $n_1$  and  $n_2$ . For instance, the possibility  $t_1 = t_2$ , with a negligible probability for an ideal continuous time measurement, must be taken into account. Now we can find two consecutive measures for which we read the same time  $n_1 = n_2$ . In our basic scheme that generates a 0 or a 1 depending on whether the second interval is shorter than the first one or not, the output is not defined and we must discard these results. Considering the equality as a valid result would require a different analysis of the probabilities of each outcome and how we assign them to a binary bit.

Figure 7 shows two potential approaches to timing with resettable and nonresettable clocks.

The fine details have been explained by Stipčević and Rogina (2007), who provided the first optical quantum random number generators that uses time detection. This generator takes the photons from an LED arriving at a PMT and compares the times of detection in a scheme similar to the method that compares the time of arrival of two particles at a Geiger counter shown in Fig. 4. As expected, a fast clock with many ticks per click gives better results as we have a higher resolution. A second conclusion is that using a resettable clock eliminates many biases coming from imprecise time measurement.

A similar generator where the source of the photons, an LED, and the detector, a SPAD, are integrated side by side in the same chip was described by Khanmohammadi et al. (2015).

The random time of arrival can also be used as a signal that chooses a time bin from a clock, following the template of the

![](images/f54f29ce4ee33a21eca86c20ce289fd20b007681a257ee86e3f633ee2c090147.jpg)  
FIG. 7. Generation scheme where the arrival of the rising edge of a detection pulse (up) starts a count of the rising edges of a clock. The clock can be independent from the pulses (bottom) or be reset with every incoming pulse (middle). In the example,  $t_2 > t_1$  and  $t_4 > t_3$  and the output should be 11. Using a resettable clock we find discrete times  $n_1 = 1$ ,  $n_2 = 2$ ,  $n_3 = 2$ , and  $n_4 = 3$  that produce the sequence 11 ( $n_2 > n_1$  and  $n_4 > n_3$ ), while for a fixed clock we read  $n_1 = 1$ ,  $n_2 = 2$ ,  $n_3 = 3$ , and  $n_4 = 2$ , and the output is 10.

radioactive decay generators summarized in Fig. 2. The generator of Dynes et al. (2008) uses a gated avalanche photodiode detector and outputs a 1 if a photon is found in an even clock cycle and a 0 if it is found in an odd cycle. The scheme also adds a self-differentiating circuit to avoid biases from the capacitive response of the detector. An interesting variation on the even-odd generation method was given by Ma, Xie, and Wu (2005), where a pulsed laser produces attenuated states with a small probability of having one or more photons in each time bin. The bins are grouped into pairs and output 0 is assigned to an empty bin with no detection followed by a detection and output 1 to a detection followed by an empty bin. This is basically equivalent to using the parity of the time bin where a photon is found, but discards occasional consecutive counts and can be extended to different ways of grouping the time bins (Yu et al., 2010).

There are many other proposals that try to generate random bits from time measurements. In principle, each time difference  $t_i$  is a real number and it would seem we can extract an infinite amount of entropy from two pulses. However, time precision limits how many usable bits we have. If our timing information has  $p$  bits of precision, the time bin in which we find a photon is a random variable with  $N = 2^p$  possible values and we can compute the probability of a photon arrival in each bin. We can then compute the relevant entropy measure (Sec. IV) for our discrete probability distribution to see how many bits of randomness are available.

Certain OQRNGs use digitized time differences with  $k$  bits and distill the available entropy into a random bit string with a mathematical function. Wayne et al. (2009) detected the photons from a laser diode with an avalanche photodiode and collected the least significant bits of the measured time until they reached 432 bits, which were then whitened with the SHA-256 algorithm (National Institute of Standards and Technology, 2012). Similarly, Wahl et al. (2011, 2012) sent an attenuated LED photon to a photomultiplier tube and processed the bits from the time of arrival with a resilient function (Bose and Ray-Chaudhuri, 1960; Sunar, Martin, and Stinson, 2007) chosen to take the maximum advantage of the available entropy while doing the processing with a function that can be efficiently implemented in hardware. The generator of Kravtsov et al. (2015) also tries to optimize extraction from quantized time differences with hardware designed to work with minimal computation that includes a lookup table that implements Elias's deterministic randomness extraction algorithm [see Sec. X.A.1 and Elias (1972)].

All these processing algorithms try to convert most of the randomness available in the exponential distribution into a uniform bit sequence and require additional hardware and processing effort.

There are also ways to generate photons with a more uniform time of arrival. The counting statistics at a detector are a function of the photon flux variation at the source (Klauder and Sudarshan, 1968). For a laser diode with a nonuniform current, we have an inhomogeneous Poisson process and the waiting time at the detector can be adjusted. The generator in Wayne and Kwiat (2010) has a circuit that reshapes the exponential time of arrival distribution into an almost uniform one. For a variable photon flux  $\lambda(t)$ , the time of arrival is a distribution

$$
\lambda (t) e ^ {- \int_ {a} ^ {b} \lambda \left(t ^ {\prime}\right) d t ^ {\prime}}. \tag {15}
$$

Ideally, we want a uniform distribution, which can be approximated by driving a laser with a current that repeats periodically a finite approximation to the function

$$
\frac {1}{T - t}, \tag {16}
$$

where  $T$  is a reset parameter that determines when to restart the pulse cycle at the source. The current goes back to the initial value when  $T$  finishes or when a pulse is detected, whichever happens first.

An alternative way to "flatten" the exponential distribution is taking short time bins from an external time reference and consider the time of arrival within those bins (Nie et al., 2014). The time when the photon arrives with respect to the origin of a particular bin is a random variable in a short, almost flat, part of the exponential time distribution, which gives a distribution closer to that of a uniform random variable.

There are also mixed generators that use both time and space uncertainty. For instance, the generator in Li et al. (2013) uses detectors in two paths to start and stop a timer, in a method similar to the intermediate signal generator in Jennewein et al. (2000), and uses the resulting time to generate random numbers. In order to have a uniform probability, the scheme assigns a binary string to nonuniform ranges of time measurements that have the same probability. The generator in Thamrin et al. (2008) works with the same kind of intermediate signal. It uses polarized photons combined with a fast clock sampling method (Fig. 2). The value of a counter is measured with the falling edge of a signal with its transitions controlled by two spatially separated detectors, although there seems to be no postprocessing to avoid correlation in the most significant bits. The generator in Stipčević and Bowers (2015) combines a branching path configuration at a beam splitter with the time difference method. There is one random bit associated with the detector that finds the photon and a bit associated to the difference between times of arrival at the detectors. The generator combines both bits to provide a random stream without the biases of the two independent generation methods.

# D. Photon counting generators

Another large group of generators based on time effects use the number of registered detections in a fixed time  $T$ . For an exponential time random variable, the number of photons that arrive in a fixed time  $T$  follows a Poisson distribution. The probability of finding  $n$  photons in that interval is

$$
P (n) = \frac {(\lambda T) ^ {n}}{n !} e ^ {- \lambda T}. \tag {17}
$$

For instance, the generator in Furst et al. (2010) follows an approach similar to the radioactive decay generator of Schmidt (1970b) (see Fig. 3) and generates bits from the parity of the total counts registered in a fixed period. The source of light is

an LED and, as in many other time-based QRNG, they turn to PMTs for faster detection. Interestingly, the generator takes advantage of the dead time of the detector. For the parity method, the random variable that describes the true rate of photocounts when the detector has a small dead time gives a smaller final bias when compared to a pure Poisson process. This approach of taking the least significant bit of the photon count is also followed by Lopes Soares, Mendonça, and Ramos (2014), where thermal and weak coherent state sources are compared.

Certain generators use an approach similar to the time difference comparisons of the previous section. If the first measurement gives  $n_1$  photons and there are  $n_2$  photons in the next time bin, we can generate a 1 when  $n_1 > n_2$  and a 0 if  $n_1 < n_2$  (Ren et al., 2011).

With these methods we are generating just 1 bit for each measurement. But, depending on  $\lambda T$ , our measurements can have a higher entropy. There are some ways to take a fuller advantage of the data we already have.

Certain generators assign more than 1 bit per detection depending on the counted photon number. The possible results are grouped into sets with equal total probability, which usually requires adjusting the mean photon level of the source to make sure all the sets are really equally, or almost equally, likely (Jian et al., 2011).

Depending on the exact photon rate  $\lambda T$  in the observed period  $T$ , the second, third, or further least significant bits of the number of counted photons might also be uniform. This is taken into account dynamically in the generator of Tisa et al. (2015) which has an array of integrated complementary metal-oxide-semiconductor (CMOS) SPAD detectors that receive light from an LED to generate random numbers in parallel in a  $32\times 32$  detector matrix. This is the principle behind the commercial generator of Micro Photon Devices (Micro Photon Devices, 2014). In this approach it is important to properly characterize the dead time, as the rate that registers at the detector  $\lambda_{\mathrm{det}}$  is affected by dead time. The corrected rate

$$
\lambda_ {\mathrm {d e t}} = \frac {\lambda}{1 + \lambda t _ {\mathrm {d e a d}} / T} \tag {18}
$$

helps to adjust the choice of how many bits from the counted number of photons should be used.

There are also generators that use everyday devices. Certain commercial cameras that are not designed for quantum detection can, nevertheless, offer good enough precision for quantum random number generation. There have been demonstrations of random numbers generated on a mobile phone (Sanguinetti et al., 2014) from the variations in the count statistics of a state with around 410 photons. In that implementation, the results are taken to a randomness extractor to eliminate correlations and noise effects. This approach is related to the shot-noise generators of Sec. VII.F.

Other photon counting methods take bins of length  $T$ , subdivide them into smaller bins where we are likely to have zero or one photons, and then use more involved procedures to convert the nonuniform Poisson statistics of the large bin into a uniform random variable (F.-X. Wang et al., 2015; J.-M. Wang et al., 2015; Yan et al., 2015).

# E. Attenuated pulse generators

Certain generators are based on a simplified version of the previous methods with more relaxed requirements for the detectors. Most current single-photon detectors have a limited photon number resolving capability and have a binary response of click (one or more photons are detected) or no click (no photon has been found). Photon counting methods usually rely on multiple clicks in a long time period that is divided into a concatenation of smaller bins in the time resolution of the detector. These methods assume a weak source that produces zero or one photons in that bin and that there is a small or ideally negligible probability of generating two or more photons in that shorter time period.

We call an attenuated pulse generator to the OQRNG with a weak source that has the same probability of generating a photon or not. More precisely, we require the complete system to give a detection probability of one-half. We can imagine a superposition of the empty and single-photon states in the same spatiotemporal mode (the path that goes to a certain detector in a certain time) so that the quantum state of our photon pulse is

$$
\frac {\left| 0 \right\rangle_ {1} + \left| 1 \right\rangle_ {1}}{\sqrt {2}}. \tag {19}
$$

We can associate a 0 to a no-detection event and a 1 to a click. The occupied state does not need to have exactly one photon. Any superposition

$$
\frac {1}{\sqrt {2}} | 0 \rangle_ {1} + \sum_ {k = 1} ^ {\infty} \alpha_ {k} | k \rangle_ {1} \tag {20}
$$

with

$$
\sum_ {k = 1} ^ {\infty} | \alpha_ {k} | ^ {2} = \frac {1}{2}
$$

is valid. Externally, we just take the 1's from clicks and do not care if they are triggered by one or more photons.

Coherent states provide such a superposition and are easy to produce. For a coherent state of amplitude  $\alpha$  the probability of finding zero photons is

$$
p (n = 0) = e ^ {- | \alpha | ^ {2}} \tag {21}
$$

and the complementary probability of finding one or more photons (and finding a click in the detector) is

$$
p (n \geq 1) = 1 - e ^ {- | \alpha | ^ {2}}, \tag {22}
$$

as can be seen from Eq. (11). The simplest idea would be to find the  $\alpha$  for which  $p(n = 0) = p(n\geq 1)$ , which happens for  $\alpha = \sqrt{\ln 2}$ . Equation (17) shows any Poissonian source with  $\lambda T = \ln 2\approx 0.693$  also gives the desired detection probability.

In practice, the generator works with an effective mean photon number at the detector  $\eta \lambda T$ , with an efficiency  $\eta$  that depends on many factors such as detector efficiency or path losses. The OQRNG can be adjusted by fine tuning of a

variable attenuator. This is the model of the generator in Wei and Guo (2009a). Alternatively, the generator can act on the light source. The OQRNG in Bisadi et al. (2015) and Bisadi, Meneghetti et al. (2015) adjusts the current of an LED in order to have the desired balance. The OQRNG of Stipčević and Ursin (2015) also has an adjustable source to guarantee a  $50\%$  probability of detection, this time inside an on-demand circuit that produces the photon pulses after a trigger signal has arrived.

Even after tuning, there can be residual bias and the system can drift out of the tuned state during operation. The generator in Wei and Guo (2009b) uses von Neumann extraction to address the problem (see Sec. X). For two detections with photon numbers  $n_1$  and  $n_2$ , it outputs a 1 if  $n_1 > 0$  and  $n_2 = 0$  (a click followed by an empty pulse) and a 0 if  $n_1 = 0$  and  $n_2 > 1$  (no click followed by a detection). The results with two successive empty pulses or two successive clicks are discarded. For a Poissonian source, both bit values are equally likely with a probability  $P(n > 0)P(n = 0) = e^{-\eta \lambda T}(1 - e^{-\eta \lambda T})$ . The resulting bit rate is at least 4 times slower, but free from bias. Greater biases result in smaller rates, but the bits still present balanced probabilities.

# F. Generators based on quantum vacuum fluctuations

Another group of quantum generators exploits the fluctuations in the quantum vacuum state. The vacuum state can be written as a superposition of amplitude quadrature states  $|x\rangle$

$$
| 0 \rangle = \int_ {- \infty} ^ {\infty} \psi (x) | x \rangle d x, \tag {23}
$$

where  $\psi (x)$  is the ground-state wave function. The wave function is a Gaussian around  $x = 0$  so that

$$
| \psi (x) | ^ {2} = \frac {1}{\sqrt {\pi}} e ^ {- x ^ {2}}. \tag {24}
$$

Homodyne measurement (Collett, Loudon, and Gardiner, 1987) offers a simple way to measure the  $X$  quadrature. The balanced homodyne detection scheme of Fig. 8 has an output proportional to the quadrature amplitude of the vacuum field and gives an amplified reading of the basic uncertainty in the vacuum state.

The homodyne detector mixes the vacuum state with a reference laser field from a local oscillator and subtracts the current measurements of two amplitude detectors. The resulting signal can then be processed and digitized to produce the random numbers. Depending on the digitizer that receives the values from the optical detectors, the choice of the local oscillator, the detectors' bandwidth, noise factors, and other problems, we might have a different amount of available random bits. With an adequate treatment, the uncertainty in the final measurement can be mostly attributed to the intrinsic quantum fluctuations of the observed vacuum state and not to the shot noise from the local oscillator or other noise sources (Yuen and Chan, 1983). This random signal can be digitized and sent to a comparator or an entropy extraction circuit to produce random sequences (Trifonov, Vig, and Magiq Technologies, Inc., 2007). The generator in Shen, Tian, and

![](images/d0dad82b41be1f7f7ef3a87cae193fbe7769ca8acb6541871b7ed93cf4196251.jpg)  
FIG. 8. Homodyne measurement of the vacuum: A laser acting as a local oscillator (LO) is mixed with the vacuum state in a balanced beam splitter. The readings of two detectors at the output of the beam splitter are subtracted and processed to give a current output proportional to the  $X$  quadrature of the vacuum field. The proportionality constant is a function of the reference field in the local oscillator.

Zou (2010) implements this method by sampling the filtered shot-noise signal periodically and taking the last bit of its digitized amplitude.

We can also take the quadrature measurement, divide the range of possible values of  $x$  into boxes from  $x_{i}$  to  $x_{i + 1}$ , and then assign to each box different random bit values. The continuous quadrature value  $x$  is in box  $i$  with a probability

$$
\int_ {x _ {i}} ^ {x _ {i + 1}} | \psi (x) | ^ {2} d x. \tag {25}
$$

The QRNG of Gabriel et al. (2010) implements this method. It takes 5 bits per measurement (32 bins) and hashes the resulting sequence to remove residual correlations.

QRNGs that measure the vacuum fluctuations can go beyond the Mbps rates of single-photon detection methods and reach rates in the Gbps range. They can use fast classical detectors and we can optimize the speed of the electronic part of the generator and concentrate on reducing the technical noise, like the generator of Symul, Assad, and Lam (2011), which discards the least significant bits as a fast method of randomness extraction after noticing that the most significant bits of the digitized homodyne measurement carry most of the quantum noise.

The method can also be used with the squeezed vacuum state. The generator of Zhu, He, and Zeng (2012) uses second harmonic generation in a parametric oscillator with no input signal to produce a squeezed vacuum state that presents a larger uncertainty in the measured quadrature. In the squeezed vacuum state, the Gaussian wave function

$$
| \psi (x) | ^ {2} = \sqrt {\frac {s}{\pi}} e ^ {- s x ^ {2}} \tag {26}
$$

is wider by a squeezing parameter  $0 < s < 1$ . Homodyne measurement produces a larger range of voltages and makes conversion to digital strings easier. We can define more voltage ranges and reduce the effects of classical noise. With more squeezing (a smaller  $s$ ) the entropy due to quantum noise increases and the bit rate after randomness extraction

can be higher. The generation of squeezed vacuum states is described in more detail in Sec. VII.J in relation to QRNGs with optical parametric oscillators.

# G. Generators based on the phase noise of lasers

The output of a laser has a random phase of quantum origin that can be used to produce random bits. Inside the cavity of a single-mode semiconductor laser, spontaneous emission causes fluctuations in the output field (Henry, 1982). This phase noise, also known as phase diffusion, comes from a combination of different quantum effects. Direct phase measurement is not technologically feasible for optical signals, but an unbalanced Mach-Zehnder interferometer (MZI) (see Fig. 9) can translate phase differences into amplitude variations.

In an unbalanced MZI one of the arms introduces a delay  $\tau$  with respect to the other arm. Assuming a constant or slowly varying amplitude in each arm, the output has a constant mean level and a variation proportional to  $\cos[\phi(t) - \phi(t + \tau)]$  for a random phase difference  $\Delta \phi(t) = \phi(t) - \phi(t + \tau)$ . The amplitude at the output ports of the interferometer can be measured with high speed standard optical detectors.

If the introduced delay is far above the coherence time of the laser,  $\tau \gg \tau_{\mathrm{coh}}$ , the phase difference  $\Delta \phi (t)$  is a Gaussian random variable of a mean that tends to 0 (Lax, 1967). If we sample the amplitude of the detector with a time difference between samples  $\Delta t\gg \tau +\tau_{\mathrm{coh}}$ , the resulting amplitudes are independent (Guo et al., 2010; Qi et al., 2010). These amplitudes are the random variable in many OQRNGs. While the voltages at the detectors carry many classical sources of noise, the quantum phase noise is known to be inversely proportional to the laser output power (Henry, 1982) and, if we operate the laser at a low intensity close the lasing threshold, we can make the quantum uncertainty the dominant noise.

The generators in Guo et al. (2010) and Qi et al. (2010) use the basic configuration in Fig. 9 and sample at a fixed period the voltage in one of the detectors. After processing, the voltages  $V_{k}$  measured at times  $t_k = t_0 + k\Delta t$  are independent Gaussian random variables.

To generate the random bits, the OQRNG of Guo et al. (2010) takes the least significant bit of the voltage measurement or the least significant bit from the difference  $V_{k + 1} - V_{k}$  between two results if we want to remove biases from the digitization of the voltage amplitudes.

The generator in Qi et al. (2010) adds a phase compensation system in the interferometer to avoid classical phase drift

![](images/6c282f89b2d660a3c3a927cb3bc91a926f37de3f5bfa3344d27c902bd44b8f19.jpg)  
FIG. 9. If we divide the light coming from a laser in a beam splitter and make it interfere with a delayed version of itself, the quantum phase noise will produce a random amplitude at the output. Choosing an adequate delay and sampling rate, we can process these amplitudes to generate random numbers.

effects that might mask the quantum signal. Its random bits come from comparing each measured voltage with a threshold at the mean voltage value 0. For the Gaussian voltage signal of interest, we can produce random bits if we choose an output 1 for  $V_{k} > 0$  and a 0 for  $V_{k} < 0$ .

The voltage distribution is Gaussian and we cannot directly use all the digitized bits, which are correlated. However, we can feed them to a randomness extraction algorithm to generate uncorrelated bits. This is the approach of the generators of Liu, Zhu, and Guo (2010) and Xu et al. (2012) which use the same optical delay circuit as the previous implementations and the generator of Nie et al. (2015), which uses a modified interferometer with advanced phase drift correction to achieve rates of tens of Gbps. We can also use Faraday mirrors to correct phase jitter (Zhu et al., 2011).

For all these generators, we can try to maximize the rate by increasing either the sampling rate or the number of bits we take. However, faster sampling means higher correlations and digitizers have a limited precision. For any given system the randomness rate can be optimized by acting on the sampling rate (Zhou, Yuan, and Ma, 2015). Increasing the sampling rate increases the generated random bit rate until  $\Delta t = \tau$ . After that point, the bits we read have a higher correlation. The additional samples produce a smaller number of uniform bits and the overall speed decreases. We should choose a delay that maximizes the final bit rate

$$
R _ {s} = - \frac {1}{\tau} \log_ {2} \left[ 2 \Phi \left(\frac {\lambda}{\sqrt {\tau}}\right) - 1 \right], \tag {27}
$$

for a parameter  $\lambda$  that depends on the laser power, the length of the measured voltage interval, and other constants of our system.  $\Phi (x)$  is the cumulative distribution function of the standard Gaussian distribution.

An interesting alternative implementation of phase noise quantum random number generators uses pulsed lasers to avoid phase correlations in the optical field. In the generator demonstrated in Jofre et al. (2011), a laser is driven by short pulses that take it rapidly from below the threshold to lasing levels. The time the laser is below the threshold, any previous coherence is attenuated and amplified spontaneous emission introduces a new random field. When the laser is suddenly taken above threshold, it amplifies the cavity field to a classical level. After the short amplification stage, the

![](images/44d6a59760ece5c4e583760c4d5594be265b57e11b4c2da8aa9c4d6ba3a7ebf5.jpg)  
FIG. 10. Using a pulsed laser we can generate individual pulses with a random phase due to quantum phase noise. If we introduce a delay in one arm of an interferometer, we have the interference of two pulses with independent phases and the output will have a random amplitude.

resulting field has a known amplitude due to gain saturation, but the phase is random.

The resulting output has a series of pulses with a random phase. The phase is converted into amplitude with the usual unbalanced Mach-Zehnder interferometer, this time with a delay  $\tau$  that matches the repetition rate at the laser so that two consecutive pulses interfere at the output beam splitter (Fig. 10).

The phase of each pulse  $\phi_{i}$  is uniformly random in  $[- \pi, \pi)$  and so is the phase difference between neighboring pulses. The interferometer converts the phase into an amplitude variation that, after detection and filtering, provides energy measurements that are almost uniformly distributed in a restricted range.

The same configuration with a pulsed laser has been refined later adding passive phase compensation to reduce classical phase drift (Tang et al., 2013) and tuning the system to achieve a faster rate up to 43 Gbps (Abellán et al., 2014).

Quantum noise inside semiconductor lasers also plays a role in classical random number generators based on chaos. Many random number generators have appeared that have one or more semiconductor lasers with optical feedback. The lasers produce a chaotic signal with pulses of a random amplitude and time position (Uchida et al., 2008; Reidler et al., 2009; Hirano et al., 2010; Kanter et al., 2010). Quantum noise in the laser is the origin of a random variation in the cavity that is then amplified in a chaotic process. While these generators have some entropy due to quantum effects, most of the unpredictability of the final sequence rests on chaotic evolution, which is deterministic. In a sense, they work as physical pseudorandom number generators that take a random quantum seed and expand these small fluctuations at the quantum level into a fast changing physical process to achieve generation rates up to hundreds of Gbps.

# H. Generators based on amplified spontaneous emission

Fiber communication systems owe their fast long range data rates to optical amplification. There are different technologies for optical amplification, such as erbium-doped fiber amplifiers (EDFAs) and semiconductor optical amplifiers, both popular alternatives in optical communication systems. These optical amplifiers work on variations of the same principle: the

light is directed into a medium with population inversion so that the photons in the signal stimulate the coherent emission of new photons that increase the signal's power. However, any excited medium capable of stimulated emission also shows spontaneous emission. That means there appear spontaneously emitted photons inside the gain medium that are amplified by stimulated emission just like the signal is. The random quantum phenomenon of spontaneous emission is thus amplified to a measurable signal with a random amplitude.

This noise, known as ASE noise, is a major limitation to optical gain in communication systems. Larger gains introduce larger noise powers and there is a maximum amplification that can be obtained without degrading the signal-to-noise ratio. Amplified spontaneous emission, either alone or in its beats with the signal or itself, is a strong source of noise that dominates over thermal noise in the detector or the optical shot noise. ASE noise is a first rate challenge in optical communication systems, but can be turned into a good source of entropy in quantum random number generators. Amplified spontaneous emission gives a readily available strong signal with a quantum origin that can be measured with existing optical equipment at fast rates. Sampling random amplitudes of the ASE field in different frequency bands gives statistically independent random variables, even at high sampling rates. The rate of change is usually much faster than the detection mechanism and the speed of the detectors is the limiting factor to the rate in most QRNGs that sample ASE noise. These devices can achieve generation rates of Gbps.

The first proposed quantum random number generators using amplified spontaneous emission work with commercial equipment from optical fiber communications. The generator of Williams et al. (2010) uses as a source of random light a pumped erbium and ytterbium co-doped fiber with no input that generates photons by spontaneous emission and amplifies them on their way to a processing stage with a bandpass filter and a second low noise amplifier. The filter limits the signal in the detector to help it work correctly. The signal is then split into its two polarization components, which are independent, and sent to two square-law photodetectors. The resulting voltage signal is mostly what is known as ASE-ASE beat noise, a signal of a random amplitude, with some residual noise from other sources. These voltages have a known distribution that depends on the shape of the filter. The difference of the voltages is a random variable of mean 0. The random bits come from comparing the voltages after each detector  $v_{1}(t)$  and  $v_{2}(t)$ , generating a 1 when  $v_{1}(t_{i}) > v_{2}(t_{i})$  at the sampling time  $t_i$  and a 0 otherwise. The resulting sequence still has some small correlation between bits. To correct that, the generator outputs the exclusive or of the raw bit sequence with a delayed version of itself.

The generator in Martin et al. (2015) also uses a filtered ASE source, a back-pumped erbium-doped fiber, but instead of two detectors it works with direct detection in a single avalanche photodiode. For the chosen filter, the spectral bandwidth of the optical signal is larger than the detector bandwidth by a factor of  $m$ . In that case, the intensity distribution that gives the probability of finding  $n$  photons for a source with an average of  $\lambda$  photons in the time of

detection (the inverse of the detection bandwidth) is (Wong et al., 1998)

$$
p _ {B E} (n, \lambda , m) = \frac {\Gamma (n + m)}{\Gamma (n + 1) \Gamma (m)} \left(1 + \frac {1}{\lambda}\right) ^ {- n} (1 + \lambda) ^ {- m}. \tag {28}
$$

For high enough values of  $n$  and  $m$ , the distribution has a large standard deviation and most of the uncertainty in the measured voltage comes from the ASE noise and not from electrical noise. We can generate random numbers comparing the results to a threshold value that gives equal probabilities for values below and above it (0 for values below the threshold, 1 for values above). The necessary threshold can vary during operation due to power changes in the source or a drift in environmental conditions during the time of generation. The resulting bias can be corrected with a randomness extractor.

Each measurement can give more than one random bit. The quantum random number generator in Argyris et al. (2012) also uses a single detector but extracts the random bits from a statistical analysis of the random distribution of the detected voltage. The device generates amplified spontaneous emission in two different implementations, one with an erbium-doped fiber amplifier and another with a semiconductor optical amplifier. In both cases, the signal is directed to an optical attenuator. The whole unfiltered noise signal reaches the photodetector where the noise beats give a Gaussian voltage distribution that is digitized. Discarding the few first most significant bits gives a good-quality random signal.

Another group of QRNGs uses superluminescent LEDs as the light source. Superluminescent light diodes are incoherent semiconductor sources with internal optical gain that offer an alternative broadband source of ASE. Their output shows a flat spectrum in a wide frequency range. The noise in separate parts of the spectrum is independent and can be used to increase the random bit rate. The generator of X. Li et al. (2011) can generate multiple bit streams using a wavelength multiplexed configuration where the light from the superluminescent diode is divided into many channels with bandpass filters for different frequency bands. Each channel ends in a single detector whose output is compared to a threshold to generate the random bits. Each output is then processed by taking the XOR of the bit sequence with a delayed version of itself. The experiment is for a two channel system, but the method can be extended to multiple parallel streams.

The QRNG in Li et al. (2014) also uses a superluminescent diode in a refined version of the comparison method in Williams et al. (2010). The filtered ASE noise from the diode is amplified in an EDFA and taken to a balanced detection scheme where the optical output is split in two parts and sent to two detectors, one of which receives a delayed signal. This self-differencing takes part of the processing to the optical signal and gives a more symmetric voltage distribution for which it is easier to define a threshold at voltage 0.

As in other generators, we can also try and use all the samples of the digitized voltage and then use postprocessing with delayed versions of the signal to remove residual correlations (Yamazaki and Uchida, 2013). In that case, the final bit rate can be improved by oversampling. If we use a sampling rate above the spectrum linewidth of the detected

noise, which is limited by the detector, the resulting bits are correlated, but adequate postprocessing can restore a good-quality sequence (Liu et al., 2013).

A curious alternative is the RNG of Wei, Tang, and Guo (2010) that uses the spontaneous emission from a regular light emitting diode without amplification. With no amplifier, the random directions of emission of an LED makes detection difficult. In order to collect enough light, the light source and the detector are placed in the focal points of an ellipsoidal cavity so that the emitted light is collected into the photodiode's sensitive area. The amplitude fluctuations due to the randomness in the emission times come from many independent events and tend to a Gaussian distribution. The voltage at the detector is then sampled and the bits from the digitizer are unbiased to give a random bit string at the output.

# I. Generators based on Raman scattering

The interaction between photons and the quantum vibrational states of certain materials is also a good source of randomness. Some quantum RNG resort to Raman scattering phenomena to obtain the entropy for random bit generation.

There are two important Raman scattering effects. The first is spontaneous Raman scattering (SpRS). In SpRS a photon is scattered when it interacts with a molecular lattice that absorbs or creates a phonon to produce a new photon of a higher or lower frequency. If the scattered photon has a larger wavelength and the energy difference is converted into a phonon we speak of a Stokes photon and when there is an energy gain and an incoming photon and an existing phonon produce a scattered photon of a smaller wavelength we speak of an anti-Stokes photon. Anti-Stokes transitions usually produce a smaller field, as they need an established phonon population of the right excited levels of the medium, which in thermal equilibrium is smaller than the population of the ground state (Boyd, 2008).

Another Raman effect is stimulated Raman scattering (SRS). In stimulated Raman scattering a photon of the frequency  $\omega_{S}$  corresponding to the energy difference between a pump photon and the matching phonon in a spontaneous Raman scattering event stimulates the production of a new photon of the same frequency  $\omega_{S}$ . This process can be used to obtain optical amplification. If we have a strong optical pump and a signal at the frequency  $\omega_{S}$ , the photons of the signal stimulate the emission of new photons that join the signal pulse consuming phonons and the photons from the pump. This mechanism is used in many photonic devices for amplification and wavelength conversion (Islam, 2002; Jalali et al., 2006) as well as in multiple applications in spectroscopy (Colthup, Daly, and Wiberley, 1990). While SpRS is almost isotropic and happens at many frequencies, the resulting field in stimulated Raman scattering is mostly contained in a narrow spatial direction and consists primarily of Stokes photons (Boyd, 2008).

Some of the QRNGs based on Raman scattering work on principles similar to those of the amplified spontaneous emission noise generators of Sec. VII.H, but, instead of employing quantum spontaneous emission events that are amplified through stimulated emission, they have a strong pump with no input signal so that the spontaneous Raman

scattering photons that are produced at random from quantum noise are amplified in a stimulated Raman scattering process (Penzkofer, Laubereau, and Kaiser, 1979). The process starts from spontaneous emission to the Stokes field that comes from the fluctuations of the phonon field (Raymer and Walmsley, 1990). The spontaneously generated photons induce new Raman scattering processes and the field is amplified to a macroscopic level in what is known as spontaneously initiated stimulated Raman scattering (SISRS). The quantum fluctuations at the initiating process show at the output field as an uncertainty in the optical phase (Kuo, Smithey, and Raymer, 1991; Smithey et al., 1991; Belsley et al., 1993) and amplitude (photon number) (Raymer, Rzaçewski, and Mostowski, 1982; Walmsley and Raymer, 1983).

The first proposal for random number generation with stimulated Raman scattering (Bustard et al., 2011) is based on measurement of the random phase in the field out of an optically pumped diamond (Fig. 11). Diamonds are a good material for Raman experiments due to their high Raman gain and their transparency at a wide range of wavelengths. A pulsed laser signal is focused into the diamond and produces a Stokes field with a random phase that is uniformly random in the  $[0,2\pi)$  range. An optical bandpass filter takes away the pump, which is in a different frequency band than the Stokes field. The random phases are converted into interference patterns at a charge-coupled device (CCD) camera by combining the Stokes field and a reference pulse in a beam splitter. The beam splitter is tilted so that there appear intensity fringes at the detector. The random phase is recovered by fitting the interference pattern to a cosine model and then it is assigned to a bin out of 64 possible phase ranges. The resulting 6 bits are then taken to a bit extraction algorithm to remove any remaining bias.

The random fluctuations in the amplitude of the field permit a simpler detection scheme without phase to amplitude conversion. Direct detection gives a straightforward amplitude measurement. There is, however, a new problem. Power fluctuations in the pump pulses can mask the quantum effect we want to measure. The generator in Bustard et al. (2013) monitors the pump power to solve this problem (see Fig. 12). The basic setup is essentially the same as in the phase Raman

![](images/dfe36f37b2f996dec4b0fe4f152fdd0097cc1497ad8bd208a206dc0c5517248b.jpg)  
FIG. 11. Generation of random numbers based on Raman scattering by measuring the phase in the field out of a pumped diamond. In this method, the phase is measured using the interference pattern of the scattered field and a reference. The pattern comes from a tilted beam splitter.

![](images/27871c77814238b42173d2dc32ca9a29d954218b6d2d9dc6764100f845732a82.jpg)  
FIG. 12. We can use the amplitude fluctuations in Raman scattering as a randomness source. In order to correct for the fluctuations of the pump, which do not have a quantum origin, we must include an amplitude correction method.

random number generator we have just covered. The pump starts an SIRS process in a diamond and the Stokes field is filtered from the pump background. Now we can directly use a detector with the output field. During normal operation, the amplitude fluctuations can reach up to multiple times the mean energy. The exact amplitude distribution has no known analytic expression and depends on the Raman gain, the focusing geometry and the effects of phonon decay, among others (Raymer et al., 1985). The output field has also small contributions due to pump coupling to more than one spatial mode and other masking effects. The amount of available entropy can be estimated deconvolving the Stokes energy distribution from the detection noise, as measured without a signal. The results show only a small effect of electrical detection in the total noise. In order to extract the entropy, the measured intensity values are corrected with the power values of the monitored reference and the compensated amplitude measurements are binned into intensity ranges that are assigned a bit string. As a last step, the sequence is applied Toeplitz hashing to remove bias and classical noise.

In both cases we described, Raman interaction has a potential for fast generation rates. The system dephases in times of the order of a few picoseconds, resetting the vacuum phonon state before the new random field is generated. The pulses come with a period much longer than the dephasing time for the phonons in the diamond. In these random number generators, the rate limit comes from the repetition rate of the laser. Stimulated Raman scattering requires large powers in order to produce a strong output signal. In the free-space configuration of the discussed generators the available lasers limited the rate to the range of kbps. These rates can be improved with faster lasers.

An alternative way to measure phase differences with a higher rate was given by England et al. (2014), where Raman interaction happens inside a highly nonlinear potassium titanyl phosphate  $\mathrm{KTiOPO_4}$  waveguide. Waveguides offer tight confinement and the guided pump field has a stronger interaction with the medium that allows us to use power levels in the range of faster repetition lasers, such as the titanium: sapphire oscillator with a repetition rate of  $80\mathrm{MHz}$  of this generator. The random numbers come from converting the random phase into an amplitude variation in an interferometer with a delayed arm, as in the schemes for quantum random number generators based on phase noise discussed in Sec. VII.G.

The quantum effects in SpRS can also serve as a randomness source in schemes without amplification at the cost of adding single-photon detectors. By improving the detector, we

can have a continuous wave laser pump of relatively low power. If we only observe the scattered photons with large frequency shifts, this interaction is mostly between the input photons and the vacuum noise phonon fluctuations instead of interactions with the thermal phonon field. The quantum randomness from phonon vacuum fluctuations is the principle behind the QRNG of Collins et al. (2014,2015) where a strong pump inside a highly nonlinear  $\mathrm{As}_2\mathrm{S}_3$  fiber generates spontaneous Raman photons in different frequency bands. The pump photons interact with phonons of different energies. The scattered photons occupy the spectrum following a known probability distribution with two separate regions. One part of the spectrum is associated with thermal phonons and, in a time  $T$ , it has an expected scattered photon detection rate (Kobliska and Solin, 1973; Lin, Yaman, and Agrawal, 2007; Collins et al., 2015)

$$
R (\nu , T) = C \eta \Delta \nu P L [ 1 + n _ {B E} (\nu , T) ] g (\nu) \tag {29}
$$

that depends on different experimental parameters like the Raman coupling efficiency  $C$ , the experimental loss factor  $\eta$ , the measurement bandwidth  $\Delta \nu$ , the laser power  $P$ , or the effective scattering length of the device  $L$ . Two particularly interesting factors are the gain profile of the medium with frequency  $g(\nu)$ , which includes both polarizations, and the thermal phonon occupation number

$$
n _ {B E} (\nu , T) = \frac {1}{e ^ {h \nu / \left(k _ {B} T\right)} - 1} \tag {30}
$$

that gives the Bose-Einstein distribution of the population of phonons with energy  $h\nu$  for a thermal energy  $k_{B}T$ . This distribution is close to the smaller detunings with respect to the pump. The photon distribution in frequency is concentrated a few THz above the pump frequency.

The spectrum has a second peak at higher detunings due to the quantum vacuum fluctuations of the phonon field. In the discussed  $\mathrm{As}_2\mathrm{S}_3$  fiber, the distribution peaks around 10.4 THz above the pump (Collins et al., 2012). At room temperature, the distributions of quantum and thermal origin are centered around different parts of the spectrum. While both distributions are random, the thermal component shows the same problems as the thermal noise generators discussed in Sec. VI and we prefer the more stable random distribution from the quantum part of the spectrum. There is still some contribution from thermal scattering events, but this and other biases can be corrected with postprocessing.

Once we have selected the most adequate frequencies, we can use a coarse wavelength division multiplexer to measure two slices of the spectrum with an equal probability of having a spontaneously scattered photon. The multiplexer converts the spectrum distribution into a spatial separation. The rest of the scheme basically follows the model of the spatial separation generators discussed in Sec. VII.B. In these experiments, two detectors  $D_{0}$  and  $D_{1}$  measure the photons in the paths of the two spectrum slices during a time  $T$ . The output bit is a 0 if there is a click only in  $D_{0}$  and a 1 if only  $D_{1}$  clicks. Two simultaneous detections and empty time bins are discarded. The differences in the collection efficiencies of the two detector channels and the nonflat shape of the Raman

spectrum introduces biases in the sequence. In order to correct the bias, there is a postprocessing stage that XORs the sequence with a 16-bit delayed version of itself.

The experiment gave raw generation rates of 1 Mbps, 650 kbps after postprocessing. The ultimate limit for the random bit generation rate depends on the decay time of the Raman response function. Spontaneous Raman scattering photons that are generated with a time separation less than the Raman response time can have frequency correlations. The photon generation rate can be controlled with the power of the pump laser to avoid correlations. In the studied fiber, the medium reacts in less than 100 fs (Asobe et al., 1995). Generation rates up to 1 GHz would still show a small two photon probability of the order of  $5 \times 10^{-3}$  in that response interval.

In the experiment, the generation rate is limited by the detectors. The detector limitations are the same as in the generators based on single-photon detection discussed in Secs. VII.B and VII.C. Most single-photon detectors are limited to a MHz rate, but more advanced detector technologies can bring the rate closer to the Raman physical limit. Additionally, the rates can be improved by dividing the spectrum into more than two channels. A wavelength division multiplexer can take the photons into multiple paths that allow to extract more than 1 bit per measurement.

# J. Generators based on optical parametric oscillators

Binary phase selection in degenerate optical parametric oscillators offers a further way to amplify quantum randomness from the microscopic level to a macroscopic optical field. In an OPO, the photons that appear from spontaneous parametric downconversion of the light from a pump start an oscillation inside a cavity, even without any input at the resonant lower frequencies (Louisell, Yariv, and Siegman, 1961; Harris, Oshman, and Byer, 1967). The zero-point fluctuations alone can initiate the gain in the cavity. The principle is similar to the amplification of quantum noise inside a laser discussed in Sec. VII.G.

In spontaneous parametric downconversion, the nonlinear response of a medium converts the photons from a pump at a frequency  $\omega_{p}$  into two photons: a signal photon with frequency  $\omega_{s}$  and an idler photon at  $\omega_{i}$  so that  $\omega_{p} = \omega_{s} + \omega_{i}$ . This phenomenon has applications in entanglement generation and in parametric amplifiers. In a medium with type I degenerate downconversion each photon from the pump produces two photons with the same frequency and polarization. Different pump photons give different polarizations, but all the generated photons have the same frequency. In these conditions, an optical parametric oscillator with no input but the pump amplifies the uncertainty in the vacuum fluctuations and the output is a squeezed vacuum state where the uncertainty at the quantum level can be measured from a macroscopic optical signal (Wu et al., 1986; Wu, Xiao, and Kimble, 1987).

The cavity of an optical parametric oscillator has losses and there is a gain threshold below which spontaneous parametric downconversion cannot be amplified to the macroscopic level (Yariv and Yeh, 2007). In a continuous wave type I degenerate OPO, where both the signal and idler fields are

indistinguishable, the gain mechanism is phase dependent and has a period of  $\pi$  for the signal phase (Nabors et al., 1990; Marandi, Leindecker, Pervak et al., 2012). For an adequate pumping power, there are only two stable oscillation states where the gain is greater than the oscillator losses. These states show a phase with respect to the pump around  $\theta_{s} = 0$  in one state and around  $\theta_{s} = \pi$  in the other.

The optical parametric oscillator quantum random number generators of Marandi et al. (2011) and Marandi, Leindecker, Vodopyanov, and Byer (2012) use as their randomness source the phase of the macroscopic field inside the cavity, which is inherited from the vacuum fluctuations. In this process, classical noise effects are negligible and do not change the phase state. In order to convert the phase variations into a binary random number, we can take two independent cavities of the same output power and make their output fields interfere at a beam splitter (see Fig. 13). If both cavities have a state around the same phase, there will be a constructive interference and the signal will have close to double the original power. If the phase states are around opposite values, there is a destructive interference and the output power is close to 0.

For the right cavity parameters, the phase distribution can be quite narrow around the central values  $\theta_{s} = 0$  and  $\pi$ , and the output power of the interferometer has two distinguishable optical power values that can be told apart using a threshold in the middle of the expected detector voltages corresponding to a totally constructive interference and a totally destructive one. The value of the comparison can be used to generate random bits. A low voltage state (destructive interference) can be interpreted as a 0 and a high voltage state (constructive interference) as 1.

The bit rate depends on the time it takes for the cavity to generate a new random phase. Once a stable state is established inside the cavity, it will feed itself. We need to restart the oscillation to generate a new random value. In the generator of Marandi et al. (2011) and Marandi, Leindecker, Vodopyanov, and Byer (2012) the cavity is detuned by blocking and unblocking the pump.

There is a minimum time before we have a fresh source of randomness. We must first allow the field inside the cavity to decay to the quantum noise level before a new oscillation

![](images/25b1e8e51e91abf864f17a44cdc15b4ed1b156c5ff25a28a0ba2b99984dc7068.jpg)  
FIG. 13. Quantum random number generation with two optical parametric oscillators. A pulsed laser creates an oscillation in each OPO in one out of two possible stable states with a phase centered around 0 or  $\pi$  with respect to the pump. The final stable phase depends on the initial conditions of the quantum fluctuations in the cavity and when the pulses from both OPOs interfere we will have close to totally destructive or close to totally constructive interference. The resulting amplitudes can be easily distinguished and be assigned to the 0- and 1-bit values.

builds up. Otherwise, when we establish the oscillation, the residual field dominates over quantum fluctuations and the new phase state is correlated to the previous phase value. This is the limiting factor in the speed of OPO-based QRNGs. The exact time for regeneration depends on the cavity and the pump power. If we pump well above threshold, like in the described generators, it can take from 10 to 20 times the  $1/e$  decay time of the cavity to go back to the quantum noise level (Marandi, Leindecker, Vodopyanov, and Byer, 2012). The intensity decay time can be estimated from the oscillator parameters as

$$
\tau_ {\text {o f f}} = \frac {T}{2 \delta_ {E} - 2 \delta_ {E} \sqrt {P _ {\text {o f f}} / P _ {\text {t h}}}} \tag {31}
$$

for a cavity with an electric field fractional round-trip loss  $\delta_{E}$ , a cavity round-trip time  $T$ , and pump powers at the threshold and "off" levels of  $P_{\mathrm{th}}$  and  $P_{\mathrm{off}}$ , respectively (Marandi, Leindecker, Vodopyanov, and Byer, 2012).

In the described QRNGs the bit rate is on the order of tens of kbps before serious correlation problems appear. Shorter cavities can have lower buildup times and, when combined with pumps at higher repetition rates, would allow rates in the Gbps range (Lecomte et al., 2005).

There are also interesting variations of the method with other parametric processes. This generation method is not necessarily restricted to second-order nonlinear materials. Instead, we could use  $\chi^{(3)}$  effects in integrated optical parametric oscillators (Liu et al., 2010; Razzari et al., 2010).

Apart from optical parametric oscillators, there are other bistable optical systems where quantum effects can produce jumps between stable states. For instance, the quantum random number generator in Sunada et al. (2011) uses a semiconductor ring laser that is driven from a monostable to a bistable state. The amplified spontaneous emission noise in the counterpropagating laser modes that appears during switching defines the final stable state from the two possible options and gives a random macroscopic bit that has a quantum origin.

Competition between optical modes is also the source of randomness in the generator proposal of Shenoy, Srikanth, and Sriniva (2013), in which spontaneously emitted photons in two possible competing modes are amplified in a laser setup so that there is a macroscopic winning mode that amplifies the quantum uncertainty at the single-photon level.

# VIII. NONOPTICAL QUANTUM RANDOM NUMBER GENERATORS

While quantum light offers a simple source of quantum randomness, there have also been proposals for quantum random number generators based on other physical systems.

For historical reasons, we already discussed the quantum random number generators based on the random behavior of radioactive decay (Sec. V). They were the first quantum random number generators well before the explosion of quantum information theory and remain in use. While they are based on the detection of particles, they are in many aspects equivalent to the optical schemes based on photon counting, time of arrival and position (in fact, in the case of  $\gamma$

radiation we can say we have an optical system, just with photons of a very high frequency).

A second family of nonoptical random number generators with a quantum contribution is the group of electronic RNGs covered in Sec. VI. In general, their source of randomness is not so clearly defined as in the rest of the quantum random number generators described, but noise generation with Zener diodes when implemented properly can be taken to an almost purely quantum regime (Stipčević, 2004), and electronic shot noise is the source of randomness in certain commercial quantum random number generators of ComScire (Wilber, 2014).

In a reverse-biased Zener diode with a low breakdown voltage, the dominant source for the current that appears is the completely quantum tunnel effect (Pierret, 1996). The  $p-n$  junction of the diode presents a potential energy barrier that is thin enough to allow random quantum tunneling of some of the electrons from the valence band of the  $p$  side to the conduction band of the  $n$  side of the junction. This creates a random reverse current that is the basis for many electronic noise physical random number generators.

Similarly, the tunnel effect at the  $p$ - $n$  junctions in MOS transistors creates a leakage current formed by the electrons that tunnel through the insulating layer under the gate. This tunneling introduces a varying current that suffers from shot noise due to the discrete nature of the electrons. These changes can be converted into a variable jitter in ring oscillators and processed to produce random numbers (Wilber, 2014). The origin of the noise is similar to that of the optical random number generators discussed in Sec. VII.F, but replacing discrete elements of light (photons) with discrete elements of current (electrons).

The shot noise in  $p$ - $n$  junctions of different semiconductor devices is a usual source of randomness in homemade electronic random number generators. An example is the random number generator based on reverse-biased  $p$ - $n$  junctions in transistors of Platt and Logue (2015).

Quantum tunneling is the basic principle behind these and many additional nonoptical random number generators. Apart from shot noise in  $p$ - $n$  junctions, tunneling explains among others cold emission of electrons from metallic surfaces or alpha decay (Razavy, 2014). From that point of view, we can say a QRNG based on radioactive alpha decay is also based on tunneling. Similarly, the random number generator that amplifies the electrons coming from nanosize emitters under an electric field in Vartsky et al. (2011) is a QRNG based on tunneling.

Other quantum random number generators measure the state of atomic quantum systems, such as trapped ions. QRNGs based on measurements on trapped ions, while slower than their optical counterparts, have an interesting application to device-independent quantum random number generation (Pironio et al., 2010) and other certified generators that are based on experimental tests of quantum mechanics (Um et al., 2013). Trapped ion systems are more complex to implement than most optical measurement setups, but they offer almost perfect detection efficiencies, which is paramount in certification. Because of the special interest of this generation method, we give a more detailed description in Sec. IX.B.

There are also more exotic proposals related to the certification of the produced random bits, such as generating random numbers with Majorana fermions (Deng and Duan, 2013). A Majorana fermion is a particle predicted by Majorana (1937) for which there is convincing experimental support (Nadj-Perge et al., 2014) and which would have desirable properties against noise and imperfections in certain implementations of quantum information protocols.

Another curious proposal is the QRNG of Katsoprinakis et al. (2008) that measures the quantum fluctuations of the collective spin of an alkali-metal vapor. Spin noise is a random magnetic moment that appears when we have a collection of atoms, even in the absence of an external magnetic field, and is proportional to the number of involved atoms. Spin noise allows one to probe the properties of the system efficiently with experiments imitating magnetic resonance methods and its measurement has applications among others to spectroscopy in semiconductors (Katsoprinakis, Dellis, and Kominis, 2007; Hübner et al., 2014).

Spin noise is an Ornstein-Uhlenbeck stochastic process that appears from the quantum uncertainty of the spin degrees of freedom combined with measurement-induced noise coming from atomic collisions. The spin state can be probed optically due to optical selection rules that permit to map the varying spin polarization onto the intensity of a probe light beam. With a proper setup, the fluctuations in the optical power due to spin noise dominate over the electronic noise and the photon shot noise and the optical power gives a precise measurement of the global magnetic field.

The QRNG in Katsoprinakis et al. (2008) measures the spin noise by analyzing the polarization of a probe beam after traversing an alkali-metal vapor under a magnetic field. Spin noise produces a random change in the polarization that can be monitored by measuring the amplitude in the horizontal and vertical components of the light after a polarizing beam splitter. Comparing the level in one branch to a threshold that includes the presence of background noise, we can generate a random binary sequence assigning a 0 or a 1 depending on whether we stay below the threshold or not.

The generation rate reaches the kbps range and is limited by the relaxation time of the system. In this case, it is desirable that the coherence of the system is short lived so that a new random state can be created as fast as possible. Samples generated below the relaxation time would be correlated. Nevertheless, there are systems with lower relaxation times, particularly solid state systems like GaAs structures, which could allow dephasing rates on the order of 1 GHz (Oestreich et al., 2005; Stich et al., 2007).

# IX. RANDOM NUMBERS CERTIFIED BY QUANTUM MECHANICS

Cryptographic random number generators face a problem of trust. Users must ultimately trust the algorithm of a pseudorandom number generator or the device that implements a true random number generation method. The alternative, which is devising a random number generation from scratch, is highly undesirable. The cryptographic maxim "Don't roll your own crypto" sums up the collected experience of the security community and warns against nontested

systems. Trusted algorithms and devices have resisted years of cryptoanalysis and attempted attacks and public inspection vouches for their robustness.

Unfortunately, this means that at some point users must trust the device or the algorithm they are given. The question, which might seem academic or for the paranoid minded, is not trivial. The events in the last years have shown RNGs are a tempting target for hidden attacks. For instance, the pseudo random number generation algorithm DUAL_EC_DBRG, which was proposed as a NIST standard (Barker and Kelsey, 2007), allows back doors that permit an attacker to recover the whole random sequence with minimal information (Shumow and Ferguson, 2007; Checkoway et al., 2014; Hales, 2014; Bernstein, Lange, and Niederhagen, 2016), which has had practical consequences in the Juniper network attack (Common Vulnerabilities and Exposures, 2015). At the hardware level, there are demonstrations of how a rogue manufacturer or any attacker with access to the device can insert very hard to detect errors in real world RNGs by introducing dopants in certain parts of the circuit (Becker et al., 2014). This is an example of the more general threat of hardware trojans, which are different kinds of malicious modifications that are inserted at the hardware level (Tehranipoor and Koushanfar, 2010).

For physical random number generators there is also the possibility of spontaneous failure. If a component from the device stops working or degrades, the quality of the output bits might suffer. Subtle hardware failures can be hard to notice, especially if the device still produces an output. For that reason, security recommendations like the AIS 31 standard of the German Bundesamt für Sicherheit in der Informationstechnik (Killmann and Schindler, 2011) or the draft of NIST SP 800-90B (Turan et al., 2016) ask for some kind of self-testing inside true random number generators. A subsystem should monitor the state of the device at all times (Bucci and Luzzi, 2005; Fischer, 2012).

In this section, we review three quantum-inspired ways of working with untrusted devices. The first method is using some properties associated to quantum phenomena to observe the quality of the produced bits. The second section gathers the proposals collectively known as device-independent quantum random number generators, which are based on the realization that there are quantum correlations that guarantee certain statistical independence unless some trusted physical principle, such as causality, is wrong. The third part describes quantumness certification methods that are inspired by device-independent generators, but use less stringent experimental tests of different aspects of the quantum theory and provide a limited certification under more relaxed security assumptions.

# A. Self-testing in quantum random number generators

Most quantum random number generators do not fully characterize their source of randomness. For instance, while a photon at a beam splitter (Fig. 6) should produce perfectly random bits, there can be problems with detector efficiency, unbalances in the splitting process, imperfections in the source, and many unsuspected sources of correlation. For that reason, there have appeared different methods to check

the quality of the random numbers produced in physical random number generators. This is not exclusive to quantum random number generators. In classical physical random number generators there are different ways to check the output to detect failures, such as including hardware versions of the NIST and Diehard randomness tests we describe in Sec. XII (Santoro, Sentieys, and Roy, 2009a,2009b; Hotoleanu et al., 2010; Vaskova et al., 2010,2011; Suresh, Antonioli, and Burleson, 2013; Yang et al., 2015). Here we discuss only the self-testing approaches that are directly related to the quantum properties of the random number generator.

There are also self-testing methods that can work with both classical noise and quantum sources of entropy. The self-testing circuit described by Saito et al. (2010) compares the time of arrival of random pulses coming either from thermal noise or from the detection of radioactive decay with a Geiger counter (Sec. V) and tests the resulting distribution against the expected Poisson time of arrival. Only the random numbers passing the tests are put forward to the output, filtering out obvious failures.

While there is still a risk from a malicious attacker that modifies the output to produce predictable sequences that will pass the tests, these self-checking systems can detect spontaneous failures and less sophisticated attacks and they are a good addition to security. Tests can serve as a canary to detect operation errors and alert that something is wrong.

Testing must be done with due care. Accurate entropy estimation is a hard problem and a system that evaluates the available entropy with a poor implementation can be vulnerable to attacks (Dodis et al., 2013).

The first mention to self-testing in a quantum setting was presented in the optical QRNG of Fiorentino et al. (2007) that is designed to work either with a single photon in a polarization superposition

$$
| \psi \rangle = \frac {| H \rangle + | V \rangle}{\sqrt {2}} \tag {32}
$$

or with an entangled state

$$
| \psi \rangle = \frac {\left| H \right\rangle_ {1} | V \rangle_ {2} + | V \rangle_ {1} | H \rangle_ {2}}{\sqrt {2}}. \tag {33}
$$

The quantum random number generator works on the principles of path branching discussed in Sec. VII.B.

The device includes a testing phase in which it performs full tomography of the input state (James et al., 2001) from a set of measurements in order to determine the  $2 \times 2$  matrix that describes the photonic two level system for a single photon or the effective two-dimensional Hilbert space of interest in the case of the photon pair. From the measurement results, the generator estimates the minimum possible min-entropy  $\tilde{H}_{\infty}(\hat{\rho})$  for the joint state of the user and an eavesdropper  $\hat{\rho}$  for the worst case over all the possible decompositions. Then the raw bits are fed to a randomness extractor (Barak, Shaltiel, and Tromer, 2003) that, for the estimated bound on the available entropy, produces a shorter unbiased random string.

This method offers protection against an adversary that can control the quantum state from which we obtain the entropy as long as we can take repeated measurements on the same state. In order to perform state tomography correctly, we need to assume the measured state is preserved throughout the process. This can be interesting when the attacker can only alter the photon source or when there is a physical problem with the generator. While this kind of self-testing offers a limited protection against advanced attackers, it is an effective way to detect accidental errors in the device.

Tomography offers a reasonable entropy estimation in models where we assume honest errors in implementation or failures during operation instead of a collection of components from untrusted colluding manufactures. Such a model is put forward in the self-testing QRNG of Lunghi et al. (2015), where randomness from a quantum origin is separated from technical noise using the dimension witness of Bowles, Quintino, and Brunner (2014) defined as

$$
W = \left| \begin{array}{l l} p (1 | 0, 0) - p (1 | 1, 0) & p (1 | 2, 0) - p (1 | 3, 0) \\ p (1 | 0, 1) - p (1 | 1, 1) & p (1 | 2, 1) - p (1 | 3, 1) \end{array} \right|, \tag {34}
$$

where  $p(b|x,y)$  gives the conditional probability of finding an outcome  $b$  (from  $\pm 1$ ) for a state prepared in one out of four  $x = 0, 1, 2, 3$  possibilities in a measurement setting  $y$  that can be 0 or 1. In the discussed generator, the four states correspond to the circular right and left polarizations or the diagonal and antidiagonal polarizations of the second photon from an entangled pair, which is measured in the diagonal or the circular polarization basis. The first photon acts as a herald.

$W$  gives an idea of "how quantum" is the combination of preparation and measurement. Any  $W > 0$  shows that some measurements are incompatible and there is some quantum randomness that allows to give a bound on the guessing probability. The result can be used to decide the level of compression in a randomness extractor. For smaller values of  $W$  (a more classical behavior) the raw input bits produce a smaller number of clean random bits. The experimental test of this method in Lunghi et al. (2015) gave a final bit rate around tens of bits per second and showed a correct response to environmental changes, like the alignment problems resulting from turning off the air conditioning in the laboratory.

A similar approach to self-testing with a Faraday-Michelson quantum key distribution system (Mo et al., 2005) was given by Song et al. (2015).

An alternative is to take advantage of the uncertainty principle to ensure any adversary has a limited amount of information. As in the previous methods, our goal is not only to generate random bits, but to be sure they are private (no external attacker can learn our sequence). For instance, if we measure the polarization of the first photon in the entangled state of Eq. (33) in the horizontal-vertical basis, we would get perfectly random numbers, but an adversary that captures the second half would know the exact sequence we obtain by taking the same measurement. This can be acceptable in applications like simulation, but in cryptography we need to avoid any information leakage. The certification method in Vallone et al. (2014) is designed to ensure privacy without full tomography by switching between two mutually unbiased

bases (Bandyopadhyay et al., 2002; Durt et al., 2010). Instead of a full tomographic measurement, two bases are enough. The conditional min-entropy with respect to an eavesdropper (Sec. IV) gives a bound to the amount of randomness we can safely extract from a measurement (König, Renner, and Schaffner, 2009; De et al., 2012). The uncertainty principle guarantees there is a limited correlation with the environment for any possible input state (we can prove a bound on the conditional min-entropy from our measurement results). This implementation requires a small random seed to choose between the bases. The original randomness in the seed is expanded after the measurements into a reliable private bit string. The seed needs to be uniform and cannot be taken from the same weak randomness source as the rest of the bits (see Sec. X for a more detailed description of randomness extraction and the role of uniform seeds). The method was demonstrated with entangled photon pairs generated from parametric downconversion and measurement in the diagonal and antidiagonal and the horizontal and vertical polarization bases.

We can also follow the methods of precision measurement (Maddaloni, Bellini, and De Natale, 2013; Bloom et al., 2014) and propose a complete model of the generator where all the sources of uncertainty are rigorously characterized and all the experimental imperfections are taken into account in the most conservative way. The experimental standards followed in precision measurement have been put to test in atomic clocks with impressive results and can be adapted to quantum random number generation. This characterization based on metrology was followed by Mitchell, Abellán, and Amaya (2015) to vouch for the randomness in a phase noise QRNG. The chosen device, described by Abellán et al. (2014), is based in the random phase in a laser, as explained in Sec. VII.G. A physical model can give a strict bound for the average min-entropy, which is used to choose a randomness extractor. The method works with theoretical considerations alone, but also gives room to introduce constraints based on auxiliary measurements or on the data that has been generated. This kind of estimation was also done by Haw et al. (2015) for the initial configuration of the QRNG based on the measurement of vacuum fluctuations of Symul, Assad, and Lam (2011) (see Sec. VII.F).

# B. Device-independent quantum random number generators

A second approach to certifying random numbers is ignoring the details inside the quantum random number generator and judge the results based only on the output. In particular, we want to prove that the output must be random or otherwise some physical law must be broken. This is the basic model behind device-independent quantum information processing, which started in the context of quantum key distribution with Mayers and Yao (1998) and Barrett, Hardy, and Kent (2005) with multiple further developments (Colbeck, 2006; Magniez et al., 2006; Acin et al., 2007; Colbeck and Kent, 2011).

In the case of random number generation, it tries to address the worst imaginable case where an adversary has generated genuinely random numbers, for instance with a quantum random number generator, and then has hidden them inside a

manipulated device. If we check the output of that device, the sequence will pass all randomness tests and we trust the results. This problem is difficult to avoid, but has a quantum solution.

Device-independent quantum random number generators solve the problem of trusting the device with schemes based on Bell tests. The ideas of Bell violation stem from the discussion of an apparent discordance of quantum theory and relativity known as the Einstein-Podolsky-Rosen paradox (Einstein, Podolsky, and Rosen, 1935). In an entangled state, measurement of one of the particles immediately sets the state of the other particle. This seems to contradict the no-signaling principle that forbids faster than light communication. Bell (1964) showed that the contradiction could be settled experimentally. The statistics of measurement on spacelike separated entangled particles would be different in a realistic local world with no interaction faster than light and in a world where the laws of quantum mechanics hold. Both alternatives are incompatible. The experiment of Aspect, Grangier, and Roger (1982) showed support for the quantum description. There are, however, experimental loopholes that could still allow a hidden variable theory that is local or realistic. A series of ever more sophisticated experiments is closing alternative explanations and confirms the predictions of quantum theory (Giustina et al., 2015; Hensen et al., 2015; Shalm et al., 2015). A detailed description of Bell inequalities and nonlocality can be found in Brunner et al.(2014).

In the experimental QRNG of Pironio et al. (2010) the chosen version of Bell's inequalities is the Clauser-Horne-Shimony-Holt formulation (Clauser et al., 1969), which is particularly elegant, simple, and intuitive. We study the correlations in measurements from two devices and define two variables  $x$  and  $y$ , one for each device. The variables can take two values, 0 and 1, that correspond to a choice between two binary measurements. Both measurement devices are identical. The measurement in the  $x$  configuration gives a binary output  $a$  and the measurement defined by  $y$  gives an outcome  $b$ . We are interested in the correlation function

$$
I = \sum_ {x, y} (- 1) ^ {x y} [ P (a = b | x y) - P (a \neq b | x y) ], \tag {35}
$$

where  $P(a = b|xy)$  and  $P(a \neq b|xy)$  are the probabilities that  $a = b$  or  $a \neq b$  when the settings are  $x$  and  $y$ . For a realistic local theory we should always find  $I \leq 2$ . Any value above 2 indicates nonlocality.

The function  $I$  can be experimentally approximated by estimating the probabilities after taking a series of measurements. As long as the systems are separated and do not interact, if the laws of quantum mechanics hold and the inputs  $x_{i}$  and  $y_{i}$  at any stage  $i$  are generated by independent random processes, the estimation of  $I, \tilde{I}$ , gives after some work a lower bound to the min-entropy of the outputs. The original derivation of the bound on min-entropy in Pironio et al. (2010) had a technical error, but in Fehr, Gelles, and Schaffner (2013) and Pironio and Massar (2013) there are restored correct proofs of the main results as well as demonstrations of some additional properties of the protocol, such as its

composability<sup>8</sup> and its fitness to generate random bits for their use in cryptography.

If the system admits a classical description  $\tilde{I} \leq 2$ , the bound is zero and the system could be deterministic. If the measurements are done on states showing some entanglement the produced random bits are guaranteed to have some randomness. The resulting bit sequence is not necessarily uniformly random, but the bound in its min-entropy means it can be converted into a random uniform string with an appropriate randomness extractor (see Sec. X).

For quantum devices with spacelike separated parts with access to independent random sources, there are no additional constraints on the devices or the input states as long as  $\tilde{I} > 2$ . The only additional requisite is that the chosen measurement settings  $x_{i}$  and  $y_{i}$  at each stage of the protocol have some randomness (are not perfectly predictable). In that respect, the described generator is a randomness expansion scheme, similar to what happens in Ekert's proposal for quantum key distribution (Ekert, 1991; Vazirani and Vidick, 2014). Starting from a random seed, the protocol gives a longer output random string whose randomness is certified by quantum mechanics. The protocol in Pironio et al. (2010) is quadratic: in order to produce  $n$  certified random bits it consumes a previously existing random sequence of the order of  $\sqrt{n}$  bits. The protocol of Vazirani and Vidick (2012) creates strings with  $n$  random bits certified to be secure against quantum adversaries starting from a seed of a length of the order of  $\log_3^n$  bits, offering an exponential expansion.

Physically, the QRNG in Pironio et al. (2010) was implemented with trapped ion qubits (Olmschenk et al., 2007) in order to close the detection loophole. Ion systems result in slower generation when compared to optical implementations, but offer almost perfect detection efficiency. Each atom first emits a photon with which it is entangled and then interference between the photons entangles the ions. This is a probabilistic heralded process. Experimental violation of Bell's inequality is a delicate task and the generation process was excruciatingly slow, giving only 42 certified random bits with a  $99\%$  confidence level after around a month of continuous running.

Later proposals relax some of the requisites to allow for optical implementations and faster generation rates. Most optical detectors have a low efficiency, but transition-edge-sensor detectors (Lita, Miller, and Nam, 2008) have been shown to offer a high enough efficiency to close the detection

loophole in some modified versions of Bell's inequality (Giustina et al., 2013) and have been used to generate certified quantum random numbers at a rate of about one-half bit per second (Christensen et al., 2013).

The QRNG of Canas et al. (2014) takes an alternative model that permits lower detection efficiencies with a semi-device-independent approach (Pawlowski and Brunner, 2011), where we still do not trust the device but suppose we work with a quantum system with a bounded dimension. The experiment encodes the quantum data in the linear transverse momentum of single photons using spatial light modulators. While in the mentioned demonstration there are only two paths available, including spatial light modulators permits to control the spatial profile of single photons to encode higher dimensional quantum states. This optical system reaches bit rates of 0.28 certified bits per second.

Other optical implementations focus on optimizing device-independent random bit generation in experiments with entangled photon pairs. This is the approach in Măttar et al. (2015) and Vivoli et al. (2015) and in the NIST randomness beacon (National Institute of Standards and Technology, 2011).

The ideas of device-independent quantum random number generators can be extended to an even more general model where quantum mechanics needs not to be true, following the example of the device-independent quantum key distribution protocols (Barrett, Hardy, and Kent, 2005; Barrett, Colbeck, and Kent, 2012) that only require the no-signaling principle to hold. The no-signaling principle forbids the transmission of information faster than the speed of light. A faster than light communication device would allow sending messages to the past and produces a conflict with causality (Tolman, 1917), as exemplified by the grandfather paradox<sup>10</sup> The no-signaling principle is subtle. In entangled states, while there is nonlocality and there are correlations that seem to travel faster than the speed of light, it is in fact impossible to use them to send information (Bussey, 1982; Dieks, 1982; Jordan, 1983).

In the device-independent quantum random number generators of Pironio et al. (2010) and Vazirani and Vidick (2012) the bounds are also given for the nonsignaling restriction. The exact bound on the conditional min-entropy changes, but the general results hold. In this new model, the protocols still work as randomness amplification schemes that need a uniform random seed.

All the commented device-independent random number generators, quantum and nonsignaling alike, are, in fact, implementations of protocols that use the results from physical experiments to expand randomness. They start from a small random seed and produce a longer bit sequence guaranteed to be random. We give a more detailed description of this quantum randomness expansion in Sec. XI.

# C. Other forms of quantum certification

Instead of testing locality with Bell inequalities, we can try to design certified quantum random number generators based on other experimental tests of the basic features of quantum theory. The Kochen-Specker theorem shows that there are states for which no noncontextual hidden variable model can reproduce the predictions of quantum mechanics (Kochen and Specker, 1967). Contextuality in quantum mechanics is related to the existence of noncommutable observables where the order of measurement is important and there is no predefined model that can give the outcomes of two successive incompatible measurements. Contextuality implies nonlocality (Einstein, 1948).

Quantum random number generators based on tests of contextuality are designed to make sure we are accessing quantum randomness and not classical noise. In this model, we still work with untrusted devices but in a less adversarial setting. We assume the manufacturer of the random number generator is not actively trying to fool us, but we admit the device can be faulty or poorly designed. A test of contextuality shows whether we are truly reading bits from a quantum source or not. One of the advantages of quantum random number generators is that we can clearly trace the origin of our random bits to a defined quantum phenomenon. These certified generators can help to detect the randomness due to classical noise, imperfections or failures in the device and take only the randomness from quantum origin. Contextuality tests can work without spacelike separation of the devices. This is both the merit and the disadvantage of the method. These tests do not required complex nonlocal entangled states, but we cannot count on causality to guarantee the bits must be random. Unlike in device-independent protocols, a rogue manufacturer can feed us pregenerated bits without being detected.

The quantum random number generators of Deng et al. (2013) and Um et al. (2013) produce certified random bits based on contextuality tests through the violation of the Klyachko-Can-Binicioglu-Shumovsky (KCBS) inequality (Klyachko et al., 2008), which does not require entangled states. The basic principle follows the model of Pironio et al. (2010). A violation of the KCBS inequality guarantees a lower bound in the entropy of the output string, which can then be fed to a randomness extractor. The results serve as a certificate of quantumness, with a minimum amount of randomness that can be safely said to be of quantum origin.

The physical implementation can be optical (Deng et al., 2013), with a qutrit<sup>11</sup> encoded in a photon in a superposition of three possible paths, or use a three-level trapped ion (Um et al., 2013), which permits one to close the detection efficiency loophole and avoids the problems of obtaining a single photon on demand. In the ion system, the random bits come from registering or not fluorescence during a measurement that takes around  $10\mathrm{ms}$ . In both cases, under the tested experimental conditions, the devices could only provide a net gain in randomness, i.e., generate more random bits

than they consumed, when using nonuniform measurement settings.

Along the same lines, there are also theoretical proposals for random number generators based on contextuality tests in settings similar to the previous experiment (Abbott et al., 2012) and with entangled states (Abbott, Calude, and Svozil, 2014) that highlight the relationship of randomness and incomputability (Calude and Svozil, 2008).

# X. POSTPROCESSING

Standard random number generators are designed to produce a random uniform string. The postprocessing stage takes care of converting the raw bit sequence into a good-quality output as close as possible to a uniform bit distribution. Postprocessing can include tasks such as buffering to accumulate samples before generating the output strings or health tests that check the generator is working properly (Schindler and Killmann, 2003). For instance, the commercial quantum random number generator based on path branching Quantis includes hardware to check for inconsistencies following the AIS31 standard (ID Quantique, 2014).

Apart from these tasks, which vary from generator to generator, the main purpose of postprocessing is randomness extraction. Most physical RNGs include one form or another of randomness extraction to correct for biases and correlations that appear due to imperfections in the measurement and generation devices even for good randomness sources with a high entropy.

Some hardware random number generators mix different randomness sources by taking the logical XOR of their bits or feed the strings to a cryptographic hash function (Networking Working Group, 2005). von Neumann proposed a simple debiasing method in which, for every pair of generated bits, we discard the results 00 and 11 and assign a 0 to 01 and a 1 to 10 (von Neumann, 1951). If we have a systematic bias this method will remove it at the cost of throwing away at least one-half of our bits and reducing our bit rate at least by one-fourth (discarding more bits the more biased our original sequence was). The basic method can be refined to improve its efficiency (Elias, 1972; Peres, 1992).

A high entropy is not enough to guarantee the generated random sequence is fit for any purpose. While there are methods that can fix weak sources for their use in randomized algorithms (Zuckerman, 1996), where randomness brings efficiency, not all protocols can work with imperfect randomness. In particular, many cryptographic protocols for tasks like bit commitment, encryption, zero knowledge or secret sharing are not secure unless they use an almost uniform random sequence (Dodis et al., 2004).

Before proceeding to describe randomness extraction in more detail, it is important to define what is considered as an "acceptably" uniform output. A useful concept is that of distance between distributions. For two probability distributions  $X$  and  $Y$  defined in the same support (they can take the same values in a finite alphabet  $\mathcal{A}$ ), we can define a statistical distance

$$
d (X, Y) = \max  _ {a \in \mathcal {A}} | P _ {X} (a) - P _ {Y} (a) |. \tag {36}
$$

This metric gives the maximum difference in the probability of getting a particular result in the compared distributions. We say two distributions  $X$  and  $Y$  are  $\epsilon$  close if

$$
d (X, Y) \leq \epsilon . \tag {37}
$$

In randomness extraction the goal is to produce an output sequence which is as close to uniform as possible. That usually means taking the  $n$  bits of the raw output and transforming them into strings of  $m$  bits with a distribution which is  $\epsilon$  close to  $U_{m}$  (a distribution uniform in  $\{0,1\}^{m}$ ) for a small  $\epsilon$  that depends on our requisites.

Ideally, we want extractors that give as many output bits as possible with the smallest use of additional resources like computation time or additional randomness. In that respect, the randomness measures we discussed in Sec. IV serve as a design guide. In particular, the min-entropy of the distribution of the raw sequence gives a limit on how many bits we can extract. If we take  $n$ -bit strings from the raw sequence with a distribution  $X$  of min-entropy  $H_{\infty}(X) = k$ , we can extract at most  $k$  random bits that are close to uniform, irrespective of the original length. A random process is called an  $(n,k)$  source if it produces  $n$  bits with a distribution  $X$  of min-entropy  $H_{\infty}(X) \geq k$ .

In the following section we discuss different methods to generate bit sequences as close to uniform as desired for rates close to the min-entropy limit and the advantages and limitations of different randomness extraction approaches.

# A. Randomness extractors

Randomness extractors are functions that convert a weak source of entropy into a uniform bit generator. They were originally introduced in the study of randomized algorithms, but have become a basic tool in many areas of theoretical computer science. Randomness extractors and related concepts like dispersers, condensers, and expander graphs have multiple applications and appear in the fields of pseudorandom number generators, error-correcting codes, samplers, expander graphs, and hardness amplifiers, among others (Vadhan, 2007).

In this section, we discuss only the few concepts about extractors most relevant to QRNGs and refer the interested reader to the extensive literature on the subject, ranging from introductory tutorials (Shaltiel, 2011) to detailed surveys (Nisan, 1996; Nisan and Ta-Shma, 1999; Shaltiel, 2004). There are many available options for randomness extraction and the final choice is usually influenced by the speed and hardware requirements of each method. Here we just comment on some particularly interesting extractors.

In order to have an efficient method and preserve as many bits as necessary, we need to have a good estimation of our available entropy and then choose an adequate randomness extractor (X. Ma et al., 2013). Otherwise, the output of the extraction function will not have the desired properties.

In the following, we assume we have a well-characterized randomness source. The relevant entropy measures were discussed in Sec. IV. The raw sequence is assumed to have a known min-entropy or, in some cases, at least some known

properties such as independence between bits or that it comes from a Markov process.

In the next sections, we also assume by default that we want an  $(n,m,k,\epsilon)$  extractor: a function that converts  $n$  bits of an  $(n,k)$  source into  $m$  output bits with a distribution that is  $\epsilon$  close to uniform, with  $m$  as close to  $k$  as possible.

# 1. Deterministic extractors

Deterministic extractors are functions

$$
\operatorname {E x t}: \{0, 1 \} ^ {n} \rightarrow \{0, 1 \} ^ {m} \tag {38}
$$

that take input strings of  $n$  bits  $\{0,1\}^n$  into  $m$  output bits. They are particularly attractive as they are deterministic algorithms that need only an input sequence to work. However, they have some limitations that prevent their use with certain randomness sources.

As in all extractors, we can only produce an output close to uniform if the input sequence already has enough intrinsic entropy. If the input sequence is an  $(n,k)$  source, a necessary condition for the output sequence to be close to uniform is that  $m\leq k$ . Unfortunately, the necessary condition is not sufficient and we can find only deterministic extractors for certain limited input distributions.

An elementary argument shows the impossibility of general deterministic extractors. Imagine a function from  $\{0,1\}^n$  to  $\{0,1\}$ . We can divide all possible inputs into one set of all the input  $n$ -bit strings that give a 0,  $\operatorname{Ext}^{-1}(0)$ , and another set that is taken to 1,  $\operatorname{Ext}^{-1}(1)$ , and at least one of them has a size  $2^{n-1}$  or larger. An input that is a uniform distribution in the larger set has at least min-entropy  $n-1$  but produces always the same output showing there is no one-size-fits-all extractor valid for any input distribution (Chor and Goldreich, 1988).

There are, however, valid extractors for input distributions belonging to certain families of processes that describe reasonable sources. Among others, there are practical deterministic extractors for samplable distributions that can be generated by an efficient sampling algorithm (Trevisan and Vadhan, 2000), for bit-fixing sources where an adversary can set as part of the bits (Gabizon, Raz, and Shaltiel, 2006; Kamp and Zuckerman, 2007) and generalizations for affine sources (Gabizon and Raz, 2005; Bourgain, 2007) or sources with an output that is distributed uniformly over an unknown algebraic variety (Dvir, 2012).

Variable length deterministic extractors form another group of interesting deterministic extractors which deviate slightly from the description of Eq. (38). They are exemplified in the von Neumann algorithm: a deterministic method that works for an unknown distribution and gives an output of a length that is not known before the extraction. In the von Neumann randomness extractor described at the beginning of this section the only requisite is that each input bit is independent from the previous and following bits. Refined versions of von Neumann's method reduce the discarded entropy and give efficiencies close to the information theory limit given by the Shannon entropy of the source (Elias, 1972; Peres, 1992). Further modifications give algorithms that produce unbiased sequences on the more general condition that the input sequence comes from a Markov chain (Blum, 1986; Zhou and Bruck, 2012).

The main appeal of the original method is its simplicity. It requires minimal computing power, it can be implemented with just basic hardware, and the distribution at the source needs not be perfectly known. However, it has some important limitations. If we have an external attacker that can alter the bias from bit to bit, even slightly, the von Neumann extractor no longer works. In fact, there is no deterministic algorithm that can give a uniform output for a random variable  $X = (X_{1},X_{2},\dots,X_{n})$  with  $n$  bits if the bias of the input bits can vary so that the probability of finding a 1 for the  $n$ th bit conditioned on the measured string for the previous bit values  $s$  is

$$
\delta \leq P _ {X _ {i}} \left(1 \mid x _ {1} x _ {2} \dots x _ {n - 1} = s\right) \leq 1 - \delta \tag {39}
$$

for  $0 < \delta \leq 1/2$ . This is called a Santha-Vazirani source and was described as a model for weak randomness sources by Santha and Vazirani (1986) together with an impossibility proof for a deterministic extractor.

Despite this limitation, there are deterministic algorithms that permit one to use a weak Santha-Vazirani source to simulate randomized algorithms (Vazirani and Vazirani, 1985b; Andreev et al., 1999). The requisites for randomization are less stringent than for other applications, such as cryptography, and weak sources that fail to produce nearly uniform outputs are sometimes valid.

Even if we use a deterministic extractor, a single weak source is not good enough for many cryptographic protocols. While weak randomness can be used securely with signature schemes, encryption and other related protocols need a high quality key or they become vulnerable (McInnes and Pinkas, 1991; Dodis and Spencer, 2002; Dodis et al., 2004; Austrin et al., 2014).

For applications where we need an output close to uniform, Santha and Vazirani (1986) offered a simple solution: combining the output of two independent Santha-Vazirani weak sources we can produce output sequences that cannot be distinguished by any polynomial-time algorithm from a uniform distribution. As long as we have access to a physical method that produces some randomness, we can generate bit strings that cannot be distinguished from a random string with any efficient algorithm. This is just as good as true randomness for the vast majority of applications of randomness, including cryptography.

Multiple source extractors follow this model and take the output of two or more weak sources and process them to generate a sequence that is close to uniform. There are many methods that depend on the concrete input distributions, the number of sources we have, and the desired properties of the output sequence.

A simple extractor valid for two  $n$ -bit blocks from two independent weak sources, both with min-entropy at least  $n/2$ , is taking the  $GF(2)$  inner product of the  $n$ -bit blocks, which reduces to computing the parity of the bitwise AND of the two sequences (U. Vazirani, 1987; U. V. Vazirani, 1987; Chor and Goldreich, 1988).

Other representative methods to combine different randomness sources can be found in Dodis et al. (2004), Bourgain (2005), Raz (2005), Barak, Impagliazzo, and Wigderson (2006), Shaltiel (2008), and Rao (2009).

The idea of combining sources is also behind the second main group of randomness extractors, seeded extractors. We consider them a special case of multiple source extractors with one weak source and a perfectly uniform source that only produces a small amount of bits.

# 2. Seeded extractors

As we have seen, for many raw bit distributions, we can only achieve an output close to uniform with the help of some additional randomness. In seeded extractors we have a function

$$
\operatorname {E x t}: \{0, 1 \} ^ {n} \times \{0, 1 \} ^ {d} \rightarrow \{0, 1 \} ^ {m} \tag {40}
$$

that takes as its input  $n$  bits from the raw sequence and a uniform random seed of  $d$  bits to produce  $m$  output bits. We assume  $d$  is much smaller than  $m$ . With the addition of the seed, which plays a role similar to the seed in pseudorandom number generators, we can guarantee that there exist extractors that produce an almost uniform output close to the maximum possible length. We call a  $(k,\epsilon)$  extractor to a function that, for any input  $k$  source (a raw sequence of, at least, min-entropy  $k$ ), produces an output sequence that is  $\epsilon$  close to uniform. The seed acts as a catalyst that permits one to find general methods that will always work.

Seeded randomness extractors were first defined by Nisan and Zuckerman (1996) in the context of randomized algorithms. Using the probabilistic method Radhakrishnan and Ta-Shma (2000) and Alon and Spencer (2016) showed that extractors always exist with an output that contains almost all of the available hidden entropy in an input raw sequence coming from any  $k$  source. For input blocks of  $n$  bits from a  $k$  source, we can build extractors with an output of size  $m \approx k + d$  that is  $\epsilon$  close to uniform using only a seed of a length  $d$  of the order of  $\log_2(n)$ . There are different explicit constructions for these seeded extractors, such as the ones in Ta-Shma (1996) and Lu et al. (2003).

The need for a uniform seed seems a contradiction: we require the resource we are trying to produce. However, the requisites on the seed are less restrictive than it seems. In many explicit extractors the seed has a length logarithmic in the size of the input string. For a small enough  $d$ , we can even replace the requisite of randomness by an exhaustive enumeration of all the  $2^{d}$  possible sequences. In randomized algorithms, enumeration followed by majority voting permits to simulate a good uniform source (Goldreich and Wigderson, 2002). However, this approach is clearly not valid for cryptography, where we need unpredictability.

In quantum random number generators, seeded extractors provide protection against external attackers. There are constructions for which there exist proofs of security against quantum attackers of different power (Ben-Aroya and Ta-Shma, 2012).

The first notable result is the Trevisan extractor (Trevisan, 2001), an explicit construction which has some nice properties such as its resistance against quantum adversaries (De and Vidick, 2010; Ta-Shma, 2011; De et al., 2012) and the way it preserves the randomness of its seed (Mauerer, Portmann, and Scholz, 2012). The Trevisan extractor is built on the

Nisan-Widgerson pseudorandom number generator (Nisan and Wigderson, 1994). It can be seen as a random function whose truth table is given by the bits from the weak source. The random function expands the  $d$  bits of a uniform random seed, in both the PRNG and the extractor sense. Different variations of the Trevisan extractor have been implemented for their use with quantum random number generators and in quantum key distribution (Mauerer, Portmann, and Scholz, 2012; X. Ma et al., 2013). Their main advantage is that the size of the random uniform seed is only polylogarithmic in the size of the input blocks. However, practical implementations can slow down the bit generation process due to the involved calculations required during the extraction.

A second general method of particular interest is two-universal hashing. The leftover hash lemma (Impagliazzo, Levin, and Luby, 1989; Håstad et al., 1999) shows that the output of a two-universal hash function with an input with high enough entropy is almost uniformly random. Two-universal hash functions, such as the families introduced in Carter and Wegman (1979) and Wegman and Carter (1981), can extract the randomness in a weak source in a secure way in the presence of an eavesdropper. If we have a good estimation or a conservative bound on the correlation of our weak random source with the eavesdropper, using the conditional entropies described in Sec. IV, it is possible to use a generalization of the leftover hash lemma with side information (Tomamichel et al., 2011). In the most general case, the side information can also be quantum. In a quantum random number generator with technical noise, we can assume that all the randomness that comes from imperfections or otherwise does not adjust to our model of the quantum system that produces the raw bits is due to an eavesdropper. In those conditions it is still possible to design a seeded extractor that gives an almost uniform output that is independent from external systems (König and Terhal, 2008; König and Renner, 2011). These methods are also applied in privacy amplification in quantum key distribution (Bennett, Brassard, and Robert, 1988; Bennett et al., 1995; König, Maurer, and Renner, 2005; Renner and König, 2005).

Randomness extraction with two-universal or, more generally,  $l$ -universal hashing forces us to use a relatively long seed, comparable to the size of the block  $n$ , but it can be recycled. A randomly chosen public uniform seed can be reused and permits a secure seeded extractor in the presence of an imperfect randomness source under partial influence of an attacker (Barak, Shaltiel, and Tromer, 2003; Skorski, 2015).

When compared to implementations of the Trevisan extractor, this method offers a fast extractor function that takes less computational resources at the cost of a larger seed (X. Ma et al., 2013). Some implementations, like hashing with Toeplitz random binary matrices (Mansour, Nisan, and Tiwari, 1990; Krawczyk, 1994), are particularly efficient. We can define one such extractor where the seed is used as a rectangular matrix that is multiplied to  $n$ -bit vectors from the source to produce an output of almost independent bits (Frauchiger, Renner, and Troyer, 2013). This approach is used in some commercial devices which include the extraction function as a precomputed random matrix that acts as the seed and is distributed coded into the device (Troyer and Renner, 2012). While ensuring the seed is uniformly random to a high degree is a painstaking task, it needs to be done only once.

Long unsophisticated methods, like repeatedly taking the XOR of multiple independent generators, are acceptable.

# XI. QUANTUM RANDOMNESS EXTRACTORS: RANDOMNESS EXPANSION AND RANDOMNESS AMPLIFICATION

Quantum mechanics does not only offer new sources of entropy for random number generators, but also new protocols related to randomness extraction. We will consider physical randomness extractors which use untrusted ancillary systems either to expand the random output of a uniform source or to turn a weak randomness source into strong one (Chung, Shi, and Wu, 2014).

There are two interesting families of protocols: quantum randomness expansion and quantum randomness amplification. In quantum randomness expansion, we start from small random seed and, with the help of a quantum protocol, we produce a longer bit sequence with strong guarantees of randomness. In randomness amplification we take a weak source, either classical or quantum, and use a quantum system to amplify the randomness in the weak source and give an arbitrarily close to uniform output.

Related to these ideas is also privacy amplification, where we take a bit string which is partially known to an adversary and produce a smaller sequence for which no external attacker can have any statistically significant information. There are known classical (Bennett, Brassard, and Robert, 1988; Bennett et al., 1995) and quantum (Deutsch et al., 1996) algorithms for this task, but we can also use methods related to randomness extraction protocols that can guarantee the output is uncorrelated to any causally preceding events and, therefore, must be private.

In this section, we give an overview of the main ideas behind these concepts. One can also find a good review of all the mathematics involved in Pivoluska et al. (2014).

# A. Quantum randomness expansion

Quantum randomness expansion protocols follow the model of seeded randomness extractors (see Sec. X.A.2): assisted by a random seed, we process the bits from a weak randomness source and give an output that is as close to uniform as desired.

All the device-independent generators discussed in Sec. IX.B are, indeed, implementations of some kind of randomness expansion protocol working on the weak randomness produced in the nonlocality experiments of different Bell tests. The quantum system serves both as a weak source of randomness and as a way to guarantee the privacy of the results. The random seed serves as a starting point to take the randomness in the quantum devices into a uniform output.

Randomness expansion protocols can be concatenated using a limited number of devices (Miller and Shi, 2014). By repetition of simple protocols with a finite number of quantum devices, we can increase the size of the output arbitrarily to produce sequences certified against quantum adversaries (Coudron and Yuen, 2014).

If we relax our requirements and trust part of the system, we can also find semi-device-independent randomness expansion

protocols. For instance, for untrusted devices but a trusted quantum state with a bounded dimension, the protocol in Bouda et al. (2014) gives an expansion scheme that does not require entanglement, which makes it easier to implement in practice. If we consider an adversary that does not directly control our device, but can characterize it better than us and has a complete model of its inner workings, we can also produce a private output string if we make full use of all the data taken from a series of Bell tests instead of restricting to the usual inequalities (Bancal, Sheridan, and Scarani, 2014).

A different kind of extractor without Bell tests is the source-independent seeded extractor in Cao et al. (2016), which is designed to work with imperfect quantum sources and addresses many problems of optical quantum random number generators such as losses, multiphoton pulses, or unbalanced beam splitters.

Similarly, there are also quantum-to-classical randomness extractors that give a procedure to measure a quantum state from a source that can be correlated to an eavesdropper so that we maximize the amount of random bits we get without giving away information to the adversary (Berta, Fawzi, and Wehner, 2014).

Finally, the concepts of randomness expansion can also be formulated as a privacy amplification problem where we want to extend the length of a private string while keeping it secret under the usual assumptions of the device independence scenario with untrusted equipment (Colbeck and Kent, 2011). The task is possible and efficient against quantum attackers, but, unlike other protocols, there are severe limitations if we consider attackers that are only restricted by nonsignaling constraints (Arnon-Friedman and Ta-Shma, 2012). Anyway, while considering nonsignaling attackers gives quite general security results, quantum mechanics seems to be the nonlocal theory that best describes the physical world and a quantum secure protocol can be safely considered as valid.

# B. Quantum randomness amplification

The need for a uniform seed in device-independent protocols comes from two parts of the procedure. First, in Bell tests we assume we have uniform random bits to choose the measurement settings. Second, the generated bit sequence is only guaranteed to have a lower bound on min-entropy, but we need to use some seeded randomness extractor to obtain a uniform output bit string.

Quantum randomness amplification protocols eliminate these previous uniform randomness requisites and give a way to use a weak source in combination with quantum devices to produce uniform random bits. In Sec. X.A.1 we have seen it is impossible to find a general deterministic method to extract randomness from any limited min-entropy source, even from restricted weak origins of entropy like Santha-Vazirani sources. With the help of quantum mechanics, we can solve this problem and find methods to extract almost uniform randomness in those situations. From a certain point of view, these protocols are not so much deterministic randomness extractors as multiple source extractors where we prove how to combine the randomness in the quantum devices with the randomness of a weak source to produce a

good-quality output. While the exact details vary from protocol to protocol, the quantum part is usually limited to simple measurements on the different subsystems of an entangled state. From an experimental point of view, the hardest requisite to satisfy is making sure the quantum devices are independent, which can be a problem in protocols that require multiple devices.

A remarkable contribution to quantum randomness amplification is the randomness amplification protocol of Colbeck and Renner (2012), which shows there are deterministic protocols that can amplify the randomness in Santha-Vazirani sources using ancillary physical systems. The result rests only on nonlocality and is robust against attackers that can go beyond quantum mechanics. This protocol needs a large supply of imperfect randomness. One natural application would be using quantum randomness amplification only to provide the random seed for the quantum randomness expansion protocols of the previous section and then use the less involved quantum randomness expansion protocols to generate the final random bit stream.

While the original protocol works only for small biases  $\delta$  in the definition of the source [see Eq. (39)], Gallego et al. (2013) gave a quantum randomness amplification protocol that is valid for arbitrarily weak sources of entropy. Further protocols can take any input weak source with a bounded nonzero min-entropy (Bouda et al., 2014; Chung, Shi, and Wu, 2014; Plesch and Pivoluska, 2014) and give practical ways to use Santha-Vazirani sources, requiring only a limited number of independent devices (Brandão et al., 2016).

There are also interesting ramifications for fundamental science experiments. Many of the concepts of quantum randomness amplification can be traced back to the study of randomness in Bell inequalities. These results are interesting in themselves as they determine which random number generators can be used in the foundational experiments on nonlocality in Bell tests. In Bell experiments there is a "free will" loophole: if the settings in the measurement are correlated, the violation of a Bell inequality cannot be used as a guarantee against an eavesdropper (Koh et al., 2012). Fortunately, even in the usual experiments, there is a certain tolerance for small correlations (Hall, 2010), but general minentropy sources are not valid for the selection of the settings in Bell experiments (Thinh, Sheridan, and Scarani, 2013).

# XII. RANDOMNESS TESTING

Once we generated a raw random sequence, we need to do some quality checks to be sure the device is working correctly. Unfortunately, there is no way to check a finite sequence is truly random. Taken to its most absurd extreme, it is like asking whether a 0 bit is fundamentally more random than a 1. Apart from the uncomputable Kolmogorov complexity (Li and Vitányi, 2008), there is no way to deduce that a random string is really random, but there are methods to detect suspicious sequences. While the bit string 111111111 is just as likely as 0100110111, if we have a generator that consistently outputs more ones than zeros we have reason to suspect it is not acting randomly.

The customary approach to randomness testing is using a series of statistical tests. Knuth (1997) covered some of the

most usual ones. The main suites available to perform these statistical tests are the NIST (Rukhin et al., 2010), TestU01 (L'Ecuyer and Simard, 2007), and the DieHard and DieHarder (Marsaglia, 1996; Brown, 2016) suites. There are also special-purpose randomness testing batteries, like the one included with the SPRNG software (Srinivasan, Mascagni, and Ceperley, 2003), which is designed to check for problems in parallel implementations of pseudorandom number generators.

These suites include different tests. In the following list, we present some of the most relevant tests to provide the kind of hidden correlations that can appear.

(1) The frequency (monobit) test, which calculates the proportion between ones and zeroes and how close that proportion is to  $1 / 2$ , and frequency tests within a block, similar to the previous one, but testing for the expected probabilities for the specified block sizes.  
(2) The runs test, which checks if the number of runs<sup>12</sup> in a bit string corresponds to that in a random sequence and if the oscillation between zeroes and ones is too fast or too slow.  
(3) The spectral test, which tries to detect periodic features in the sequence that would indicate a deviation from the assumption of randomness.  
(4) Maurer's universal statistical test (Maurer, 1992), which detects whether or not the sequence can be significantly compressed without loss of information.  
(5) Autocorrelation tests which check the correlation of the sequence with shifted versions of itself.

Most tests apply statistical analyses similar to the standard chi-squared test. The result is a  $p$  value that indicates how likely it is for a purely random number generator to produce the tested sequence. Each test suite has different threshold values to determine if a given  $p$  value is compatible with randomness or not.

These tests, while useful to detect faulty generators, cannot prove a generator produces truly random outputs. Deterministic pseudorandom number generators like the Mersenne Twister can pass the tests but are predictable. Likewise, there can be false positives for correlations and the tests should be run multiple times for each generator. Statistically, even a perfect random number generator would fail a test from time to time.

Testing is also vulnerable to an active attacker that feeds us pregenerated random sequences that pass the tests. In Sec. IX.B we described some quantum protocols to solve this issue.

Apart from that, the tests are usually designed with pseudorandom number generators in mind and do not include physical models into account. Some correlations due to implementation-related problems, like afterpulsing in photon detectors, are not specifically checked.

All these problems notwithstanding, any good quantum random number generator should be able to pass all the tests in any given suite and using some form of randomness testing

during operation can help to detect sudden failures or faulty components.

# XIII. DISCUSSION

Quantum random number generation is probably the most mature quantum technology. We have seen the multiple ways we can harness the randomness in quantum mechanics to produce random bit strings. Physical phenomena such as radioactive decay, photon splitting, noise in Raman amplification, laser phase noise, or amplified spontaneous emission can serve as reliable entropy sources.

We have reached a point where optical quantum random number generators routinely reach generation rates on the order of megabits per second with promises of gigabit rates and new generation methods are still being suggested every year. While there is a race to announce the highest possible generation rates, in many cases, the actual implementation is limited by practical hurdles in the speed of the electronic systems and the postprocessing methods.

Many proposals focus on the generation principle, on making sure the quantum phenomenon of interest produces fresh entropy at a fast rate, but do not deal with making full use of the available bits and give random bit rates which are only true as an extrapolation. In the research phase, it is perfectly acceptable to leave all the processing details for later and work on a limited collection of stored samples, but, at this point of development, there is a need for better and faster production of the final, usable random bits.

Commercial devices, by necessity, have these aspects covered but they still offer bit rates with a gap around 2 orders of magnitude with respect to the fastest possible laboratory rates. In some applications, such as simulation, this is important, as quantum random number generators have to compete against fast pseudorandom number generators that work essentially at the speed of the available processor.

Concerning the bit rate, there are two relevant issues. One is the communication bottleneck. External devices will always need a communication channel with the computer that uses the random bits. The fastest USB protocols (USB 3.0 and 3.1) and PCI Express components can reach communication rates on the order of tens of Gbps that is enough for many generators. Alternatively, many optical implementations can be adapted or have been demonstrated to work in integrated silicon setups that could be included as part of future processors.

Communication at those rates is challenging, but it is an engineering problem that can be solved with current technology with the right systems. A second more interesting limitation is randomness extraction. In Sec. X we described different ways to turn the raw bits coming from measurement and the first simple conditioning into good-quality random bits. While some quantum random number generators are claimed to directly produce random enough raw sequences, in some applications like cryptography, less than perfect uniformity can pose serious problems. In general, quantum random number generators should include a well-designed postprocessing phase.

Seeded extractors like Trevisan's or two-universal hashing have good security properties against quantum attackers. That should be the standard that postprocessing methods should aspire to. At the moment, postprocessing is relatively slow

when compared to the potential generation rates of the fastest optical generators. The most efficient implementations use postprocessing based on two-universal hashing with binary matrix multiplication. There is a large open area of research on identifying and constructing new extractors that are resistant against quantum attacks and can be fast enough to sustain output bit rates on the order of Gbps.

Self-testing is another area for future improvement. Physical random number generators can fail due to component degradation or even external attacks. In Sec. IX we described many possible approaches to quality control. In particular, device-independent protocols offer reliable random numbers even if we do not trust our hardware. Device-independent randomness generation and quantum randomness expansion and amplification are quite active areas of research and the last years have seen many interesting results, including new protocols based on nonlocality that can perform classically impossible tasks, such as physically assisted deterministic randomness extraction from weak sources.

Device-independent quantum random number generators are still experimentally challenging and produce bits at sluggish rates. In Sec. IX we also commented on more relaxed approaches to certification, but this is likely to be an active area for the next years, both in technological development research to make better device-independent QRNGs and in the theoretical search for simpler paths to certification.

Currently, both pure and applied research have reached an interesting point where there are new fundamental results and, at the same time, there appear different quantum random number generators in the market.

With this review, we hope we have introduced the interested reader to the existing technologies and hinted at some future directions.

# ACKNOWLEDGMENTS

This work has been funded by Project No. TEC2015-69665-R (MINECO/FEDER, UE).

# REFERENCES

Abbott, A. A., C. S. Calude, J. Conder, and K. Svozil, 2012, "Strong Kochen-Specker theorem and incomputability of quantum randomness," Phys. Rev. A 86, 062109.  
Abbott, A. A., C. S. Calude, and K. Svozil, 2014, "A quantum random number generator certified by value indefiniteness," Math. Struct. Comput. Sci. 24, e240303.  
Abellán, C., W. Amaya, M. Jofre, M. Curty, A. Acín, J. Capmany, V. Pruneri, and M. W. Mitchell, 2014, "Ultra-fast quantum randomness generation by accelerated phase diffusion in a pulsed laser diode," Opt. Express 22, 1645.  
Acín, A., N. Brunner, N. Gisin, S. Massar, S. Pironio, and V. Scarani, 2007, "Device-independent security of quantum cryptography against collective attacks," Phys. Rev. Lett. 98, 230501.  
Ahmad, D., 2008, "Two Years of Broken Crypto: Debian's Dress Rehearsal for a Global PKI Compromise," IEEE Security Privacy Magazine 6, 70-73.  
Alkassar, A., T. Nicolay, and M. Rohe, 2005, "Obtaining true-random binary numbers from a weak radioactive source," Computational Science and Its Applications—ICCSA 2005, Pt II,

Lecture Notes in Computer Science, Vol. 3481 (Springer, Berlin), pp. 634-646.  
Alley, C. O., O. G. Jakubowicz, and W. C. Wickes, 1984, "Results of the delayed-random-choice quantum mechanics experiment with light quanta," in Proceedings of the 2nd International Symposium on Foundations of Quantum Mechanics, Tokyo (Physical Society of Japan, Tokyo, Japan), pp. 158-164.  
Alon, N., and J.H. Spencer, 2016, The Probabilistic Method, Wiley Series in Discrete Mathematics and Optimization (Wiley, New York), 4th ed.  
American National Standards Institute, 1985, ANSI X9.17- Financial Institution Key Management (Wholesale) standard, Tech. Rep.  
American National Standards Institute, 2006, ANSI X9.82 (Parts 1-4)—Random Number Generation, Tech. Rep.  
Andreev, A. E., A. E. F. Clementi, J. D. P. Rolim, and L. Trevisan, 1999, "Weak random sources, hitting sets, and BPP simulations," SIAM J. Comput. 28, 2103-2116.  
ANU, 2016, "ANU Quantum Random Numbers Server," Australian National University, https://qrng.anu.edu.au/.  
Argyris, A., E. Pikasis, S. Deligiannidis, and D. Syvridis, 2012, "Sub-Tb/s Physical Random Bit Generators Based on Direct Detection of Amplified Spontaneous Emission Signals," J. Lightwave Technol. 30, 1329-1334.  
Arnon-Friedman, R., and A. Ta-Shma, 2012, "Limits of privacy amplification against nonsignalling memory attacks," Phys. Rev. A 86, 062333.  
Asobe, M., T. Kanamori, K. Naganuma, H. Itoh, and T. Kaino, 1995, "Third-order nonlinear spectroscopy in  $\mathrm{As}_2\mathrm{S}_3$  chalcogenide glass fibers," J. Appl. Phys. 77, 5518-5523.  
Aspect, A., P. Grangier, and G. Roger, 1982, "Experimental Realization of Einstein-Podolsky-Rosen-Bohm Gedankenexperiment: A New Violation of Bell's Inequalities," Phys. Rev. Lett. 49, 91-94.  
Austrin, P., K.-M. Chung, M. Mahmoody, R. Pass, and K. Seth, 2014, "On the impossibility of cryptography with tamperable randomness," in Advances in Cryptology—CRYPTO 2014, Part I, Lecture Notes in Computer Science Vol. 8616 (Springer, Berlin), pp. 462-479.  
Bancal, J.-D., L. Sheridan, and V. Scarani, 2014, "More randomness from the same data," New J. Phys. 16, 033011.  
Bandyopadhyay, S., P. O. Boykin, V. Roychowdhury, and F. Vatan, 2002, "A New Proof for the Existence of Mutually Unbiased Bases," Algorithmica 34, 512-528.  
Barak, B., R. Canetti, J. B. Nielsen, and R. Pass, 2004, "Universally composable protocols with relaxed set-up assumptions," in Proceedings of the 45th Annual IEEE Symposium on Foundations of Computer Science, FOCS '04 (IEEE Computer Society, Washington, DC), pp. 186-195.  
Barak, B., R. Impagliazzo, and A. Wigderson, 2006, "Extracting randomness using few independent sources," SIAM J. Comput. 36, 1095-1118.  
Barak, B., R. Shaltiel, and E. Tromer, 2003, "True Random Number Generators Secure in a Changing Environment," Cryptographic Hardware and Embedded Systems—CHES 2003, Lecture Notes in Computer Science Vol. 2779 (Springer, Berlin), pp. 166-180.  
Barker, E., and J. Kelsey, 2007, "Recommendation for random number generation using deterministic random bit generators (revised)," NIST Spec. Publ. 800-90A, 90 [https://dx.doi.org/10.6028/NIST.SP.800-90Ar1].  
Barker, E., and A. Roginsky, 2012, "Recommendation for Cryptographic Key Generation," NIST Spec. Publ. 800-133, 90 [http://dx.doi.org/10.6028/NIST.SP.800-133].

Barrett, J., R. Colbeck, and A. Kent, 2012, "Unconditionally secure device-independent quantum key distribution with only two devices," Phys. Rev. A 86, 062326.  
Barrett, J., L. Hardy, and A. Kent, 2005, "No signalling and quantum key distribution," Phys. Rev. Lett. 95, 010503.  
Bauke, H., and S. Mertens, 2007, "Random numbers for large-scale distributed Monte Carlo simulations," Phys. Rev. E 75, 066701.  
Beausoleil, R.G., W.J. Munro, and T.P. Spiller, 2008, "Self-authenticating quantum random number generator," U.S. Patent 7428562 B2.  
Becker, G. T., F. Regazzoni, C. Paar, and W. P. Burleson, 2014, "Stealthy dopant-level hardware Trojans: Extended version," Journal of Cryptographic Engineering 4, 19-31.  
Bell, J. S., 1964, "On the Einstein-Podolsky-Rosen paradox," Physics, 1, 195 [https://cds.cern.ch/record/111654].  
Belsley, M., D. T. Smithey, K. Wedding, and M. G. Raymer, 1993, "Observation of extreme sensitivity to induced molecular coherence in stimulated Raman scattering," Phys. Rev. A 48, 1514-1525.  
Ben-Aroya, A., and A. Ta-Shma, 2012, "Better short-seed quantum-proof extractors," Theor. Comput. Sci. 419, 17-25.  
Bennett, C. H., and G. Brassard, 1984, "Quantum cryptography: Public key distribution and coin tossing," in Proceedings of the IEEE International Conference on Computers, Systems and Signal Processing, Bangalore, India (IEEE, New York), p. 175.  
Bennett, C. H., G. Brassard, C. Crepeau, and U. M. Maurer, 1995, "Generalized privacy amplification," IEEE Trans. Inf. Theory 41, 1915-1923.  
Bennett, C.H., G. Brassard, and J.-M. Robert, 1988, "Privacy amplification by public discussion," SIAM J. Comput. 17, 210-229.  
Bernstein, D. J., Y. A. Chang, C. M. Cheng, L. P. Chou, N. Heninger, T. Lange, and N. van Someren, 2013, "Factoring RSA keys from certified smart cards: Coppersmith in the wild," Advances in Cryptology—ASIACRPT 2013, Lecture Notes in Computer Science Vol. 8270 (Springer-Verlag, Berlin), pp. 341–360.  
Bernstein, D. J., T. Lange, and R. Niederhagen, 2016, "Dual EC: A Standardized Back Door," in The New Codebreakers, Lecture Notes in Computer Science Vol. 9100 (Springer, Berlin), pp. 256-281.  
Berta, M., O. Fawzi, and S. Wehner, 2014, "Quantum to classical randomness extractors," IEEE Trans. Inf. Theory 60, 1168-1192.  
Bisadi, Z., A. Meneghetti, G. Fontana, G. Pucker, P. Bettotti, and L. Pavesi, 2015, "Quantum random number generator based on silicon nanocrystals LED," Proc. SPIE Int. Soc. Opt. Eng. 9520, 952004.  
Bisadi, Z., et al., 2015, "Silicon nanocrystals for nonlinear optics and secure communications," Phys. Status Solidi (a) 212, 2659-2671.  
Bloom, B. J., T. L. Nicholson, J. R. W. s, S. L. Campbell, M. Bishop, X. Zhang, W. Zhang, S. L. Bromley, and J. Ye, 2014, "An optical lattice clock with accuracy and stability at the  $10^{-18}$  level," Nature (London) 506, 71-75.  
Blum, L., M. Blum, and M. Shub, 1986, “A Simple Unpredictable Pseudo-Random Number Generator,” SIAM J. Comput. 15, 364-383.  
Blum, M., 1986, "Independent unbiased coin flips from a correlated biased source—a finite state Markov chain," Combinatorica 6, 97-108.  
Blum, M., and S. Micali, 1984, "How to Generate Cryptographically Strong Sequences of Pseudorandom Bits," SIAM J. Comput. 13, 850-864.  
Bose, R. C., and D. K. Ray-Chaudhuri, 1960, "On a class of error correcting binary group codes," Inf. Control 3, 68-79.  
Bouda, J., M. Pawlowski, M. Pivoluska, and M. Plesch, 2014, "Device-independent randomness extraction from an arbitrarily weak min-entropy source," Phys. Rev. A 90, 032313.

Bouda, J., M. Pivoluska, M. Plesch, and C. Wilmott, 2012, "Weak randomness seriously limits the security of quantum key distribution," Phys. Rev. A 86, 062308.  
Bourgain, J., 2005, "More on the sum-product phenomenon in prime fields and its applications," Int. J. Number Theory 01, 1-32.  
Bourgain, J., 2007, "On the construction of affine extractors," GAFA Geometric And Functional Analysis 17, 33-57.  
Bowles, J., M. T. Quintino, and N. Brunner, 2014, "Certifying the dimension of classical and quantum systems in a prepare-and-measure scenario with independent devices," Phys. Rev. Lett. 112, 140407.  
Boyd, R. W., 2008, "Chapter 9—Stimulated Brillouin and Stimulated Rayleigh Scattering," in *Nonlinear Optics* (Academic Press, Burlington), 3rd ed., pp. 429-471.  
Brandão, F. G. S. L., R. Ramanathan, A. Grudka, K. Horodecki, M. Horodecki, P. Horodecki, T. Szarek, and H. Wojewódka, 2016, "Realistic noise-tolerant randomness amplification using finite number of devices," Nat. Commun. 7, 11345.  
Bratley, P., B. L. Fox, and L. E. Schrage, 1987, A Guide to Simulation (Springer-Verlag, New York).  
Bronner, P., A. Strunz, C. Silberhorn, and J.-P. Meyn, 2009, "Demonstrating quantum random with single photons," Eur. J. Phys. 30, 1189-1200.  
Brown, R.G., 2016, "Dieharder: A random number test suite," https://www.phy.duke.edu/~rgb/General/dieharder.php.  
Brunner, N., D. Cavalcanti, S. Pironio, V. Scarani, and S. Wehner, 2014, "Bell nonlocality," Rev. Mod. Phys. 86, 419-478.  
Bucci, M., and R. Luzzi, 2005, "Design of Testable Random Bit Generators," in Cryptographic Hardware and Embedded Systems 3659-CHES2005, Lecture Notes in Computer Science Vol. 3659 (Springer, Berlin), pp. 147-156.  
Buller, G. S., and R. J. Collins, 2010, "Single-photon generation and detection," Meas. Sci. Technol. 21, 012002.  
Burri, S., and D. Stucki, 2013, "Jailbreak imagers: Transforming a single-photon image sensor into a true random number generator," in Image Sensor, EPFL-CONF-191217, pp. 5-8 [http://www/imagesensors.org/Past%20Workshops/2013%20Workshop/2013%20Papers/07-20_099_regazzoni_paper_revised.pdf].  
Burri, S., D. Stucki, Y. Maruyama, C. Bruschini, E. Charbon, and F. Regazzoni, 2014, "SPADs for quantum random number generators and beyond," in Design Automation Conference (ASP-DAC), 2014, 19th Asia and South Pacific (IEEE, New York), pp. 788-794.  
Bussey, P.J., 1982, "Super-luminal communication" in Einstein-Podolsky-Rosen experiments, Phys. Lett. A 90, 9-12.  
Bustard, P.J., D.G. England, J. Nunn, D. Moffatt, M. Spanner, R. Lausten, and B.J. Sussman, 2013, "Quantum random bit generation using energy fluctuations in stimulated Raman scattering," Opt. Express 21, 29350.  
Bustard, P.J., D. Moffatt, R. Lausten, G. Wu, I.A. Walmsley, and B.J. Sussman, 2011, "Quantum random bit generation using stimulated Raman scattering," Opt. Express 19, 25173-25180.  
Cachin, C., 1997, "Entropy Measures and Unconditional Security in Cryptography," Ph.D. thesis (ETH Zürich), http://dx.doi.org/10.3929/ethz-a-001806220.  
Calude, C. S., 2015, "Indeterminism and Randomness", CDMTCS Research Reports CDMTCS-485, http://hdl.handle.net/2292/27854.  
Calude, C. S., and K. Svozil, 2008, “Quantum Randomness and Value Indefiniteness,” Adv. Sci. Lett. 1, 165–168.  
Cañas, G., J. Caríne, E. S. Gómez, J. F. Barra, A. Cabello, G. B. Xavier, G. Lima, and M. Pawlowski, 2014, "Experimental quantum randomness generation invulnerable to the detection loophole," arXiv:1410.3443.

Canetti, R., 2001, "Universally composable security: A new paradigm for cryptographic protocols," in Proceedings of the 42nd IEEE Symposium on Foundations of Computer Science, FOCS '01 (IEEE Computer Society, Washington, DC), p. 136. Updated version available at https://eprint.iacr.org/2000/067.pdf.  
Cao, Z., H. Zhou, X. Yuan, and X. Ma, 2016, "Source-independent quantum random number generation," Phys. Rev. X 6, 011020.  
Carter, J. L., and M. N. Wegman, 1979, “Universal classes of hash functions,” J. Comput. Syst. Sci. 18, 143–154.  
Checkoway, S., M. Fredrikson, W. Madison, and R. Niederhagen, 2014, "On the Practical Exploitability of Dual EC in TLS Implementations," USENIX Security 2014.  
Childs, A. M., and W. van Dam, 2010, "Quantum algorithms for algebraic problems," Rev. Mod. Phys. 82, 1-52.  
Chor, B., and O. Goldreich, 1988, "Unbiased bits from sources of weak randomness and probabilistic communication complexity," SIAM J. Comput. 17, 230-261.  
Christensen, B. G., et al., 2013, “Detection-Loophole-Free Test of Quantum Nonlocality, and Applications,” Phys. Rev. Lett. 111, 130406.  
Chung, K.-M., Y. Shi, and X. Wu, 2014, "Physical Randomness Extractors: Generating Random Numbers with Minimal Assumptions," arXiv:1402.4797v3.  
Clauser, J. F., M. A. Horne, A. Shimony, and R. A. Holt, 1969, "Proposed Experiment to Test Local Hidden-Variable Theories," Phys. Rev. Lett. 23, 880-884.  
Coddington, P. D., 1994, "Analysis of random number generators using Monte Carlos simulation," Int. J. Mod. Phys. C 05, 547-560.  
Coddington, P. D., 1996, "Tests of random number generators using Ising model simulations," Int. J. Mod. Phys. C 07, 295-303.  
Colbeck, R., 2006, "Quantum And Relativistic Protocols For Secure Multi-Party Computation," Ph.D. thesis (University of Cambridge), arXiv:0911.3814 [https://arxiv.org/abs/0911.3814].  
Colbeck, R., and A. Kent, 2011, "Private randomness expansion with untrusted devices," J. Phys. A 44, 095305.  
Colbeck, R., and R. Renner, 2012, “Free randomness can be amplified,” Nat. Phys. 8, 450–453.  
Collett, M.J., R. Loudon, and C.W. Gardiner, 1987, “Quantum Theory of Optical Homodyne and Heterodyne Detection,” J. Mod. Opt. 34, 881–902.  
Collins, M. J., A. Clark, Z. Yan, C. Xiong, M. J. Steel, and B. J. Eggleton, 2014, "Quantum Random Number Generation using Spontaneous Raman Scattering," in CLEO: 2014 (OSA, Washington, DC), p. JTh2A.123.  
Collins, M. J., A. S. Clark, C. Xiong, E. Magi, M. J. Steel, and B. J. Eggleton, 2015, "Random number generation from spontaneous Raman scattering," Appl. Phys. Lett. 107, 141112.  
Collins, M. J., A. C. Judge, A. S. Clark, S. Shahnia, E. C. Magi, M. J. Steel, C. Xiong, and B. J. Eggleton, 2012, "Broadband photon-counting Raman spectroscopy in short optical waveguides," Appl. Phys. Lett. 101, 211110.  
Colthup, N. B., L. H. Daly, and S. E. Wiberley, 1990, Introduction to Infrared and Raman Spectroscopy (Elsevier, San Diego), 3rd ed.  
Common Vulnerabilities and Exposures, 2015, "Vulnerability Report No. CVE-2015-7755," http://CVE.mitre.org/cgi-bin/cvename.cgi? name=CVE-2015-7755.  
Coudron, M., and H. Yuen, 2014, "Infinite Randomness Expansion with a Constant Number of Devices," in Proceedings of the 46th Annual ACM Symposium on Theory of Computing, STOC '14 (ACM, New York), pp. 427-436.  
Courtois, N. T., D. Hulme, K. Hussain, J. A. Gawinecki, and M. Grajek, 2013, "On Bad Randomness and Cloning of Contactless

Payment and Building Smart Cards," in 2013 IEEE Security and Privacy Workshops (242497) (IEEE, New York), pp. 105-110.  
Cryptography Research Inc., 2003, "Evaluation of VIA C3 Nehemiah Random Number Generator," technical report, https://www.rambus.com/ via-technologies-random-number-generator/.  
De, A., C. Portmann, T. Vidick, and R. Renner, 2012, "Trevisan's Extractor in the Presence of Quantum Side Information," SIAM J. Comput. 41, 915-940.  
De, A., and T. Vidick, 2010, "Near-optimal extractors against quantum storage," in Proceedings of the Forty-second ACM Symposium on Theory of Computing, STOC '10 (ACM, New York), pp. 161-170.  
de Jesus Lopes Soares, E., F. A. Mendonça, and R. V. Ramos, 2014, "Quantum Random Number Generator Using Only One Single-Photon Detector," IEEE Photonics Technol. Lett. 26, 851-853.  
Deng, D.-L., and L.-M. Duan, 2013, “Fault-tolerant quantum random-number generator certified by Majorana fermions,” Phys. Rev. A 88, 012323.  
Deng, D.-L., C. Zu, X.-Y. Chang, P.-Y. Hou, H.-X. Yang, Y.-X. Wang, and L.-M. Duan, 2013, "Exploring Quantum Contextuality to Generate True Random Numbers," arXiv:1301.5364.  
Deutsch, D., A. Ekert, R. Jozsa, C. Macchiavello, S. Popescu, and A. Sanpera, 1996, "Quantum privacy amplification and the security of quantum cryptography over noisy channels," Phys. Rev. Lett. 77, 2818-2821.  
Dieks, D., 1982, "Communication by EPR devices," Phys. Lett. A 92, 271-272.  
Dodis, Y., A. Elbaz, R. Oliveira, and R. Raz, 2004, "Improved randomness extraction from two independent sources," in Approximation, Randomization, and Combinatorial Optimization. Algorithms and Techniques, Lecture Notes Notes in Computer Science Vol. 3122 (Springer, Berlin), pp. 334-344.  
Dodis, Y., S.J. Ong, M. Prabhakaran, and A. Sahai, 2004, "On the (im)possibility of cryptography with imperfect randomness," in Proceedings of the 45th Annual IEEE Symposium on Foundations of Computer Science, 2004 (IEEE, New York), pp. 196-205.  
Dodis, Y., D. Pointcheval, S. Ruhault, D. Vergnaud, and D. Wichs, 2013, "Security analysis of pseudo-random number generators with input: /dev/random is not robust," 2013 ACM SIGSAC Conference on Computer and Communications Security, CCS'13, Berlin, Germany (ACM, New York), 647-658.  
Dodis, Y., and J. Spencer, 2002, "On the (non)universality of the onetime pad," in Foundations of Computer Science, 2002, Proceedings (IEEE Computer Society, Los Alamitos, CA), pp. 376-385.  
Dorrendorf, L., Z. Gutterman, and B. Pinkas, 2009, "Cryptanalysis of the random number generator of the Windows operating system," ACM Transactions on Information and System Security 13, 1-32.  
Duggirala, R., A. Lal, and S. Radhakrishnan, 2010, "Radioisotope Decay Rate Based Counting Clock," in MEMS Reference shelf 6 (Springer-Verlag, New York), pp. 127-170.  
Dultz, W., G. Dultz, E. Hildebrandt, and H. Schmitzer, and Deutsche Telekom Ag, 2002, "Method for generating a random number on a quantum-mechanics basis and random generator," Patents EP 1029394 B1 and WO 1999/066641 A1.  
Dultz, W., and E. Hildebrandt, and Deutsche Telekom Ag, 2002, "Optical random-number generator based on single-photon statistics at the optical beam splitter," Patents U.S. 6393448 B1 and EP 0940010 B1.  
du Preez, V., M. G. B. Johnson, A. Leist, and K. A. Hawick, 2011, "Performance and Quality of Random Number Generators," in International Conference on Foundations of Computer Science (FCS'11), FCS4818, pp. 16-21.

Durt, T., B.-G. Englert, I. Bengtsson, and K. Žyzkowski, 2010, "On mutually unbiased bases," Int. J. Quantum. Inform. 08, 535-640.  
Dvir, Z., 2012, “Extractors for varieties,” Comput. Complex. 21, 515-572.  
Dynes, J.F., Z.L. Yuan, A.W. Sharpe, and A.J. Shields, 2008, "A high speed, postprocessing free, quantum random number generator," Appl. Phys. Lett. 93, 031109.  
Eagle, A., 2005, "Randomness is unpredictability," Br. J. Philos. Sci. 56, 749-790.  
Einstein, A., 1948, “Quanten-Mechanik und Wirklichkeit,” Dialectica 2, 320-324.  
Einstein, A., B. Podolsky, and N. Rosen, 1935, “Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?” Phys. Rev. 47, 777-780.  
Eisaman, M. D., J. Fan, A. L. Migdall, and S. V. Polyakov, 2011, "Single-photon sources and detectors," Rev. Sci. Instrum. 82, 071101.  
Ekert, A.K., 1991, "Quantum cryptography based on Bell's theorem," Phys. Rev. Lett. 67, 661-663.  
Ekert, A. K., and R. Jozsa, 1996, "Quantum computation and Shor's factoring algorithm," Rev. Mod. Phys. 68, 733-753.  
Elias, P., 1972, "The efficient construction of an unbiased random sequence," Ann. Math. Stat. 43, 865-870.  
England, D. G., P. J. Bustard, D. J. Moffatt, J. Nunn, R. Lausten, and B. J. Sussman, 2014, "Efficient Raman generation in a waveguide: A route to ultrafast quantum random number generation," Appl. Phys. Lett. 104, 051117.  
Fain, B., 1982, "Spontaneous emission vs. vacuum fluctuations," Nuovo Cimento Soc. Ital. Fis. B 68, 73-78.  
Fearn, H., and R. Loudon, 1987, "Quantum theory of the lossless beam splitter," Opt. Commun. 64, 485-490.  
Fehr, S., R. Gelles, and C. Schaffner, 2013, "Security and compositability of randomness expansion from Bell inequalities," Phys. Rev. A 87, 012335.  
Ferguson, N., B. Schneier, and T. Kohno, 2010, "Generating Randomness," in Cryptography Engineering: Design Principles and Practical Applications (Wiley Publishing, Inc., Indianapolis), pp. 137-161.  
Ferrenberg, A. M., D. P. Landau, and Y. J. Wong, 1992, "Monte Carlo simulations: Hidden errors from 'good' random number generators," Phys. Rev. Lett. 69, 3382-3384.  
Fiorentino, M., and R. G. Beausoleil, 2006, "A quantum random bit generator for secure communication," SPIE Newsroom 3, 1-2.  
Fiorentino, M., W. J. Munro, C. M. Santori, S. M. Spillane, and R. G. Beausoleil, 2006, "All-fiber-optic quantum random number generator," in 2006 Conference on Lasers and Electro-Optics and 2006 Quantum Electronics and Laser Science Conference (IEEE, New York), pp. 1-2.  
Fiorentino, M., C. M. Santori, S. M. Spillane, R. G. Beausoleil, and W. J. Munro, 2007, "Secure self-calibrating quantum random-bit generator," Phys. Rev. A 75, 032334.  
Fischer, V., 2012, “A closer look at security in random number generators design,” Lect. Notes Comput. Sci. 7275, 167-182.  
Fishman, G. S., 1978, Principles of Discrete Event Simulation (Wiley, New York).  
Frauchiger, D., R. Renner, and M. Troyer, 2013, "True randomness from realistic quantum devices," arXiv:1311.4547.  
Friedman, H., 1949, "Geiger Counter Tubes," Proc. IREE Aust. 37, 791-808.  
Fürst, M., H. Weier, S. Nauerth, D. G. Marangon, C. Kurtsiefer, and H. Weinfurter, 2010, "High speed optical quantum random number generation," Opt. Express 18, 13029-13037.

Gabizon, A., and R. Raz, 2005, "Deterministic extractors for affine sources over large fields," in 46th Annual IEEE Symposium on Foundations of Computer Science (FOCS'05) (IEEE Computer Society, Los Alamitos, CA), pp. 407-416.  
Gabizon, A., R. Raz, and R. Shaltiel, 2006, "Deterministic extractors for bit-fixing sources by obtaining an independent seed," SIAM J. Comput. 36, 1072-1094.  
Gabriel, C., C. Wittmann, D. Sych, R. Dong, W. Mauerer, U. L. Andersen, C. Marquardt, and G. Leuchs, 2010, "A generator for unique quantum random numbers based on vacuum states," Nat. Photonics 4, 711-715.  
Gallego, R., L. Masanes, G. de la Torre, C. Dhara, L. Aolita, and A. Acín, 2013, “Full randomness from arbitrarily deterministic events, Nat. Commun. 4, 2654.  
Gea-Banacloche, J., M. O. Scully, and M. S. Zubairy, 1988, "Vacuum Fluctuations and Spontaneous Emission in Quantum Optics," Phys. Scr. T21, 81-85.  
Gennaro, R., 2006, “Randomness in cryptography,” IEEE Security and Privacy 4, 64–67.  
Gentle, J. E., 2009, Computational Statistics (Springer, New York), 1st ed.  
Gerhardt, I., Q. Liu, A. Lamas-Linares, J. Skaar, C. Kurtsiefer, and V. Makarov, 2011, "Full-field implementation of a perfect eavesdropper on a quantum cryptography system, Nat. Commun. 2, 349.  
Ghioni, M., A. Gulinatti, I. Rech, F. Zappa, and S. D. Cova, 2007, "Progress in Silicon Single-Photon Avalanche Diodes," IEEE J. Sel. Top. Quantum Electron. 13, 852-862.  
Ginzburg, V.L., 1983, "The nature of spontaneous radiation," Sov. Phys. Usp. 26, 713-719.  
Gisin, N., G. Ribordy, W. Tittel, and H. Zbinden, 2002, “Quantum cryptography,” Rev. Mod. Phys. 74, 145–195.  
Gisin, N., and H. Zbinden, 1999, “Bell inequality and the locality loophole: Active versus passive switches,” Phys. Lett. A 264, 103–107.  
Giustina, M., et al., 2013, “Bell violation using entangled photons without the fair-sampling assumption,” Nature (London) 497, 227-230.  
Giustina, M., et al., 2015, "Significant-Loophole-Free Test of Bell's Theorem with Entangled Photons," Phys. Rev. Lett. 115, 250401.  
Goldberg, I., and D. Wagner, 1996, "Randomness and the Netscape Browser," Dr. Dobb's Journal January, pp. 66-70.  
Goldreich, O., 1999, Modern Cryptography, Probabilistic Proofs and Pseudorandomness, Algorithms and Combinatorics, Vol. 17 (Springer-Verlag, Berlin).  
Goldreich, O., and A. Wigderson, 2002, "Derandomization that is rarely wrong from short advice that is typically good," in Proceedings of RANDOM 2002, Lecture Notes in Computer Science Vol. 2483 (Springer, Berlin), pp. 209-223.  
Goodyear Aircraft Corporation, 1954, "Random Noise Generator for Simulation Studies," Report No. GER-6436, 791-808.  
Grafe, M., R. Heilmann, A. Perez-Leija, R. Keil, F. Dreisow, M. Heinrich, H. Moya-Cessa, S. Nolte, D. N. Christodoulides, and A. Szameit, 2014, "On-chip generation of high-order single-photon W-states," Nat. Photonics 8, 791-795.  
Grassberger, P., 1993, "On correlations in "good" random number generators," Phys. Lett. A 181, 43-46.  
Gude, M., 1985, "Concept for a High Performance Random Number Generator Based on Physical Random Phenomena," Frequenz 39, 187-190.  
Guedes, E. B., F. M. de Assis, and B. Lula, 2013, “Quantum attacks on pseudorandom generators,” Math. Struct. Comput. Sci. 23, 608-634.

Guo, H., W. Tang, Y. Liu, and W. Wei, 2010, "Truly random number generation based on measurement of phase noise of a laser," Phys. Rev. E 81, 051137.  
Gupta, M. S., 1975, "Applications of electrical noise," Proc. IEEE 63, 996-1010.  
Gutterman, Z., B. Pinkas, and T. Reinman, 2006, "Analysis of the Linux Random Number Generator," 2006 IEEE Symposium on Security and Privacy (S&P'06) (IEEE, New York), 370-385.  
Hadfield, R. H., 2009, "Single-photon detectors for optical quantum information applications," Nat. Photonics 3, 696-705.  
Hales, T. C., 2014, “The NSA Back Door to NIST,” Not. Am. Math. Soc. 61, 1.  
Hall, M. J. W., 2010, "Local deterministic model of singlet state correlations based on relaxing measurement independence," Phys. Rev. Lett. 105, 250404; 116, 219902(E), 2016.  
Hamburg, M., P. Kocher, and M. E. Marson, 2012, analysis of "Intel's Ivy Bridge Digital Random Number Generator," white paper by Cryptography Research Inc., https://www.rambus.com/intel-ivy-bridge-random-number-generator/.  
Harris, S. E., M. K. Oshman, and R. L. Byer, 1967, "Observation of Tunable Optical Parametric Fluorescence," Phys. Rev. Lett. 18, 732-734.  
Håstad, J., R. Impagliazzo, L. A. Levin, and M. Luby, 1999, “A pseudorandom generator from any one-way function,” SIAM J. Comput. 28, 1364-1396.  
Haw, J. Y., S. M. Assad, A. M. Lance, N. H. Y. Ng, V. Sharma, P. K. Lam, and T. Symul, 2015, "Maximization of Extractable Randomness in a Quantum Random-Number Generator," Phys. Rev. Applied 3, 054004.  
Hayes, B., 2001, "Randomness as a resource," Am. Sci. 89, 300-304.  
Heninger, N., Z. Durmeric, E. Wustrow, and J. A. Halderman, 2012, "Mining your Ps and Qs: detection of widespread weak keys in network devices," Proceedings of the 21st USENIX Security Symposium (USENIX Association, Berkeley, CA), pp. 205-220.  
Henry, C., 1982, “Theory of the linewidth of semiconductor lasers,” IEEE J. Quantum Electron. 18, 259–264.  
Henry, C., and R. F. Kazarinov, 1996, "Quantum noise in photonics," Rev. Mod. Phys. 68, 801-853.  
Hensen, B., et al., 2015, "Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres," Nature (London) 526, 682-686.  
Hirano, K., T. Yamazaki, S. Morikatsu, H. Okumura, H. Aida, A. Uchida, S. Yoshimori, K. Yoshimura, T. Harayama, and P. Davis, 2010, "Fast random bit generation with bandwidth-enhanced chaos in semiconductor lasers," Opt. Express 18, 5512.  
Holman, W. T., J. A. Connelly, and A. B. Dowlatabadi, 1997, "An integrated analog/digital random noise source," IEEE Trans. Circuits Syst. I 44, 521-528.  
Hongo, K., R. Maezono, and K. Miura, 2010, "Random number generators tested on quantum Monte Carlo simulations," J. Comput. Chem. 31, 2186-2194.  
Hoogland, A., A. Compagner, and H. W. J. Blöte, 1985, "Smooth finite-size behaviour of the three-dimensional Ising model," Physica A (Amsterdam) 132, 593-596.  
Hörmann, W., J. Leydold, and G. Derflinger, 2004, Automatic Nonuniform Random Variate Generation, Statistics and Computing No. 1 (Springer, Berlin).  
Hotoleanu, D., O. Cret, A. Suciu, T. Gyorfi, and L. Vacariu, 2010, "Real-Time Testing of True Random Number Generators Through Dynamic Reconfiguration," 2010 13th Euromicro Conference on Digital System Design: Architectures, Methods and Tools (IEEE Computer Society, Los Alamitos, CA), pp. 247-250.

Howe, R.M., 1961, Design fundamentals of analog computer components (Van Nostrand, Princeton, NJ).  
Hübner, J., F. Berski, R. Dahbashi, and M. Oestreich, 2014, "The rise of spin noise spectroscopy in semiconductors: From acoustic to GHz frequencies," Phys. Status Solidi B 251, 1824-1838.  
Hughes, R., and J. Nordholt, 2016, "Strengthening the Security Foundation of Cryptography With Whitewood's Quantum-Powered Entropy Engine," http://www.whitewoodencryption.com.  
Hull, T. E., and A. R. Dobell, 1962, "Random Number Generators," SIAM Rev. 4, 230-254.  
Humboldt-Universität, 2016, "High Bit Rate Quantum Random Number Generator Service," https://qrng.physik.hu-berlin.de/.  
ID Quantique, 2011, "User Case White Paper, Loterie Romande," technical report, http://www.idquantique.com.  
ID Quantique, 2014, “QUANTIS random number generator,” http://www.idquantique.com/random-number-generation.  
Impagliazzo, R., L. A. Levin, and M. Luby, 1989, “Pseudo-random generation from one-way functions,” in Proceedings of the Twenty-first Annual ACM Symposium on Theory of Computing, STOC '89 (ACM, New York), pp. 12-24.  
International Organization for Standardization, 2011, "Random bit generation," Report No. ISO/IEC 18031.  
Isida, M., and H. Ikeda, 1956, "Random number generator," Ann. Inst. Stat. Math. 8, 119-126.  
Islam, M. N., 2002, "Raman amplifiers for telecommunications," IEEE J. Sel. Top. Quantum Electron. 8, 548-559.  
Jacques, V., E. Wu, F. Grosshans, F. Treussart, P. Grangier, A. Aspect, and J.-F. Roch, 2007, "Experimental Realization of Wheeler's Delayed-Choice Gedanken Experiment, Science 315, 966-968.  
Jacques, V., E. Wu, F. Grosshans, F. Treussart, P. Grangier, A. Aspect, and J.-F. Roch, 2008, "Delayed-Choice Test of Quantum Complementarity with Interfering Single Photons," Phys. Rev. Lett. 100, 220402.  
Jalali, B., V. Raghunathan, D. Dimitropoulos, and O. Boyraz, 2006, "Raman-based silicon photonics," IEEE J. Sel. Top. Quantum Electron. 12, 412-421.  
James, D. F. V., P. G. Kwiat, W. J. Munro, and A. G. White, 2001, "Measurement of qubits," Phys. Rev. A 64, 052312.  
Jennewein, T., U. Achleitner, G. Weihs, H. Weinfurter, and A. Zeilinger, 2000, "A Fast and Compact Quantum Random Number Generator," Rev. Sci. Instrum. 71, 1675-1680.  
Jian, Y., M. Ren, E. Wu, G. Wu, and H. Zeng, 2011, "Two-bit quantum random number generator based on photon-number-resolving detection," Rev. Sci. Instrum. 82, 073109.  
Jofre, M., M. Curty, F. Steinlechner, G. Anzolin, J. P. Torres, M. W. Mitchell, and V. Pruneri, 2011, "True random numbers from amplified quantum vacuum," Opt. Express 19, 20665-20672.  
Johnson, J. B., 1928, "Thermal agitation of electricity in conductors," Phys. Rev. 32, 97.  
Jordan, T. F., 1983, "Quantum correlations do not transmit signals," Phys. Lett. A 94, 264.  
Kalle, C., and S. Wansleben, 1984, "Problems with the random number generator RANF implemented on the CDC Cyber 205," Comput. Phys. Commun. 33, 343-346.  
Kamp, J., and D. Zuckerman, 2007, "Deterministic extractors for bit-fixing sources and exposure-resilient cryptography," SIAM J. Comput. 36, 1231-1247.  
Kanter, I., Y. Aviad, I. Reidler, E. Cohen, and M. Rosenbluh, 2010, "An optical ultrafast random bit generator," Nat. Photonics 4, 58-61.  
Karp, R. M., 1991, "An introduction to randomized algorithms," Discrete Appl. Math. 34, 165-201.

Katsoprinakis, G. E., A. T. Dellis, and I. K. Kominis, 2007, "Measurement of transverse spin-relaxation rates in a rubidium vapor by use of spin-noise spectroscopy," Phys. Rev. A 75, 042502.  
Katsoprinakis, G. E., M. Polis, A. Tavernarakis, A. T. Dellis, and I. K. Kominis, 2008, "Quantum random number generator based on spin noise," Phys. Rev. A 77, 054101.  
Kelsey, J., B. Schneier, D. Wagner, and C. Hall, 1998, "Cryptanalytic Attacks on Pseudorandom Number Generators," in Fast Software Encryption, Lecture Notes in Computer Science Vol. 1372 (Springer, Berlin), pp. 168-188.  
Kerckhoffs, A., 1883, "La cryptographie militaire," Journal des sciences militaires IX, 5-83 [http://www.petitcolas.net/kerckhoffs/crypto_militaire_1.pdf].  
Khanmohammadi, A., R. Enne, M. Hofbauer, and H. Zimmermanna, 2015, "A Monolithic Silicon Quantum Random Number Generator Based on Measurement of Photon Detection Time," IEEE Photonics J. 7, 1-13.  
Killmann, W., and W. Schindler, 2008, "A design for a physical RNG with robust entropy estimators," in CHES 2008: Cryptographic Hardware and Embedded Systems, Lecture Notes in Computer Science Vol. 5154 (Springer, Berlin), pp. 146-163.  
Killmann, W., and W. Schindler, 2011, a proposal for "Functionality classes for random number generators," AIS 20 / AIS 31 standard, https://www.bsi.bund.de.  
Kim, H. J., and M. J. Klass, 2001, "Random number generator," U.S. Patent 6249009 B1.  
Kim, S. H., D. Han, and D. H. Lee, 2013, "Predictability of Android OpenSSL's pseudo random number generator," in Proceedings of the 2013 ACM SIGSAC Conference on Computer & Communications Security—CCS '13 (ACM, New York), pp. 659-668.  
Klass, M.J., 2003, “Random number generator,” U.S. Patent 6539410 B1.  
Klass, M. J., 2005, "Apparatus for generating random numbers," U.S. Patent 6965907 B2.  
Klauder, J. R., and E. C. G. Sudarshan, 1968, Fundamentals of Quantum Optics, The Mathematical Physics Monographs Series (Benjamin, New York).  
Klyachko, A. A., M. A. Can, S. Binicioglu, and A. S. Shumovsky, 2008, "Simple Test for Hidden Variables in Spin-1 Systems," Phys. Rev. Lett. 101, 020403.  
Knoll, G.F., 2010, Radiation Detection and Measurement (Wiley, New York), 4th ed.  
Knuth, D.E., 1997, The Art of Computer Programming, Seminumerical Algorithms (Addison-Wesley Longman Publishing Co., Inc., Boston, MA), Vol. 2, 3rd ed.  
Kobliska, R. J., and S. A. Solin, 1973, "Temperature Dependence of the Raman Spectrum and the Depolarization Spectrum of Amorphous  $\mathrm{As}_2\mathrm{S}_3$ ," Phys. Rev. B 8, 756.  
Kochen, S., and E. P. Specker, 1967, “The Problem of Hidden Variables in Quantum Mechanics,” The Logico-Algebraic Approach to Quantum Mechanics, The University of Western Ontario Series in Philosophy of Science, Vol. 5a (Springer, Netherlands), pp. 293–328.  
Koh, D. E., M. J. W. Hall, Setiawan, J. E. Pope, C. Marletto, A. Kay, V. Scarani, and A. Ekert, 2012, "Effects of reduced measurement independence on Bell-based randomness expansion," Phys. Rev. Lett. 109, 160404.  
Kohlbrenner, P., and K. Gaj, 2004, "An Embedded True Random Number Generator for FPGAs," in Proceedings of the 2004 ACM/ SIGDA 12th International Symposium on Field Programmable Gate Arrays, FPGA '04 (ACM, New York), pp. 71-78.  
König, R., U. Maurer, and R. Renner, 2005, "On the power of quantum memory," IEEE Trans. Inf. Theory 51, 2391-2401.

König, R., and R. Renner, 2011, "Sampling of Min-Entropy Relative to Quantum Knowledge," IEEE Trans. Inf. Theory 57, 4760-4787.  
König, R., R. Renner, and C. Schaffner, 2009, “The Operational Meaning of Min- and Max-Entropy,” IEEE Trans. Inf. Theory 55, 4337–4347.  
König, R. T., and B. M. Terhal, 2008, "The bounded-storage model in the presence of a quantum adversary," IEEE Trans. Inf. Theory 54, 749-762.  
Kravtsov, K. S., I. V. Radchenko, S. P. Kulik, and S. N. Molotkov, 2015, "Minimalist design of a robust real-time quantum random number generator," J. Opt. Soc. Am. B 32, 1743-1747.  
Krawczyk, H., 1990, "How to Predict Congruential Generators," in Advances in Cryptology, Lecture Notes in Computer Science Vol. 435 (Springer, New York), pp. 138-153.  
Krawczyk, H., 1994, “LFSR-based hashing and authentication,” in Advances in Cryptology, CRYPTO '94, Lecture Notes in Computer Science Vol. 839 (Springer, Berlin), pp. 129-139.  
Kuo, S.J., D.T. Smithey, and M.G. Raymer, 1991, "Spatial interference of macroscopic light fields from independent Raman sources," Phys. Rev. A 43, 4083-4086.  
Landauer, R., 1993, “Solid-state shot noise,” Phys. Rev. B 47, 16427-16432.  
Law, A. M., and D. W. Kelton, 2000, Simulation modeling and analysis, McGraw Hill Series in Industrial Engineering and Management Science (McGraw-Hill, New York), 3rd ed.  
Lax, M., 1967, "Classical Noise. V. Noise in Self-Sustained Oscillators," Phys. Rev. 160, 290-307.  
Lecomte, S., R. Paschotta, S. Pawlik, B. Schmidt, K. Furusawa, A. Malinowski, D. J. Richardson, and U. Keller, 2005, "Synchronously pumped optical parametric oscillator with a repetition rate of  $81.8\mathrm{GHz}$ ," IEEE Photonics Technol. Lett. 17, 483-485.  
L'Ecuyer, P., 2012, "Random Number Generation," in Handbook of Computational Statistics, edited by J. E. Gentle, W. K. Hardle, and Y. Mori (Springer, Berlin/Heidelberg), pp. 35-71.  
L'Ecuyer, P., and R. Simard, 2007, "A C Library for Empirical Testing of Random Number Generators," ACM Trans. Math. Softw. 33, 22.  
Lehmer, D. H., 1951, "Mathematical Methods in Large-scale Computing Units," Proceedings of a Second Symposium on Large-Scale Digital Calculating Machinery, Annals of the Computation Laboratory of Harvard Vol. XXVI (Harvard University Press, Cambridge, MA), pp. 141-146.  
Lenstra, A. K., J. P. Hughes, M. Augier, J. W. Bos, T. Kleinjung, and C. Wachter, 2012, "Public Keys," in Crypto 2012, Lecture Notes in Computer Science Vol. 7417 (Springer, Berlin), pp. 626-642.  
Li, H.-W., Z.-Q. Yin, S. Wang, Y.-J. Qian, W. Chen, G.-C. Guo, and Z.-F. Han, 2015, "Randomness determines practical security of BB84 quantum key distribution," Sci. Rep. 5, 16200.  
Li, H.-W., et al., 2011, "Attacking a practical quantum-key-distribution system with wavelength-dependent beam-splitter and multiwavelength sources," Phys. Rev. A 84, 062308.  
Li, L., A. Wang, P. Li, H. Xu, L. Wang, and Y. Wang, 2014, "Random Bit Generator Using Delayed Self-Difference of Filtered Amplified Spontaneous Emission," IEEE Photonics J. 6, 1-9.  
Li, M., and P. M. B. Vitányi, 2008, An Introduction to Kolmogorov Complexity and Its Applications (Springer, New York), 3rd ed.  
Li, S., L. Wang, L.-A. Wu, H.-Q. Ma, and G.-J. Zhai, 2013, “True random number generator based on discretized encoding of the time interval between photons,” J. Opt. Soc. Am. A 30, 124.  
Li, X., A. B. Cohen, T. E. Murphy, and R. Roy, 2011, "Scalable parallel physical random number generator based on a superluminescent LED," Opt. Lett. 36, 1020.

Lin, Q., F. Yaman, and G. P. Agrawal, 2007, "Photon-pair generation in optical fibers through four-wave mixing: Role of Raman scattering and pump polarization," Phys. Rev. A 75, 023803.  
Lita, A. E., A. J. Miller, and S. W. Nam, 2008, “Counting near-infrared single-photon with  $95\%$  efficiency,” Opt. Express 16, 3032.  
Liu, X., R. M. Osgood, Y. Vlasov, and W. M. J. Green, 2010, "Mid-infrared optical parametric amplifier using silicon nanophotonic waveguides," Nat. Photonics 4, 557-560.  
Liu, Y., M. Zhu, and H. Guo, 2010, "Truly random number generation via entropy amplification," arXiv:1006.3512.  
Liu, Y., M.-Y. Zhu, B. Luo, J.-W. Zhang, and H. Guo, 2013, "Implementation of  $1.6\mathrm{Tbs}^{-1}$  truly random number generation based on a super-luminescent emitting diode," Laser Phys. Lett. 10, 045001.  
Lo, H.-K., M. Curty, and K. Tamaki, 2014, "Secure quantum key distribution," Nat. Photonics 8, 595-604.  
Lohr, S. L., 2010, Sampling: Design and Analysis (Brooks/Cole, Boston, MA), 2nd ed.  
Loudon, R., 2001, The Quantum Theory of Light (Oxford University Press, Oxford, UK), 3rd ed.  
Louisell, W.H., A. Yariv, and A.E. Siegman, 1961, “Quantum Fluctuations and Noise in Parametric Processes. I,” Phys. Rev. 124, 1646–1654.  
Lu, C.-J., O. Reingold, S. Vadhan, and A. Wigderson, 2003, "Extractors: Optimal up to constant factors," in Proceedings of the Thirty-fifth Annual ACM Symposium on Theory of Computing, STOC '03 (ACM, New York), pp. 602-611.  
Lunghi, T., J. B. Brask, C. C. W. Lim, Q. Lavigne, J. Bowles, A. Martin, H. Zbinden, and N. Brunner, 2015, "Self-Testing Quantum Random Number Generator," Phys. Rev. Lett. 114, 150501.  
Lutkenhaus, N., J.L. Cohen, H.-K. Lo, and Magiq Technologies, Inc., 2007, "Efficient use of detectors for random number generation," U.S. Patent 7197523 B2.  
Lutz, G., 2007, Semiconductor Radiation Detectors (Springer-Verlag, Berlin/Heidelberg).  
Lydersen, L., C. Wiechers, C. Wittmann, Dominique Elser, J. Skaar, and V. Makarov, 2010, "Hacking commercial quantum cryptography systems by tailored bright illumination," Nat. Photonics 4, 686-689.  
Lyngsø, R. B., and C. N. S. Pedersen, 2002, "The consensus string problem and the complexity of comparing hidden Markov models," J. Comput. Syst. Sci. 65, 545-569.  
Ma, H.-Q., Y. Xie, and L.-A. Wu, 2005, "Random number generation based on the time of arrival of single photons," Appl. Opt. 44, 7760.  
Ma, X., F. Xu, H. Xu, X. Tan, B. Qi, and H.-K. Lo, 2013, "Postprocessing for quantum random-number generators: Entropy evaluation and randomness extraction," Phys. Rev. A 87, 062327.  
Ma, X., X. Yuan, Z. Cao, B. Qi, and Z. Zhang, 2016, "Quantum random number generation," npj Quantum Inf. 2, 16021.  
Ma, X.-S., S. Zotter, J. Kofler, R. Ursin, T. Jennewein, C. Brukner, and A. Zeilinger, 2012, "Experimental delayed-choice entanglement swapping," Nat. Phys. 8, 480-485.  
Ma, X.-S., et al., 2013, "Quantum erasure with causally disconnected choice," Proc. Natl. Acad. Sci. U.S.A. 110, 1221-1226.  
Maddaloni, P., M. Bellini, and P. De Natale, 2013, Laser-based Measurements for Time and Frequency Domain Applications: A Handbook (CRC Press, Boca Raton, FL).  
Magniez, F., D. Mayers, H. Ollivier, and M. Mosca, 2006, "Self-testing of quantum circuits," in Automata, Languages and Programming, Lecture Notes in Computer Science Vol. 4051 (Springer, Berlin), pp. 72-83.

Majorana, E., 1937, "Teoria simmetrica dell'elettrone e del positrone," Nuovo Cimento 14, 171-184.  
Manelis, B., 1961, "Generating random noise," Electronics 8, 66-69.  
Mansour, Y., N. Nisan, and P. Tiwari, 1990, "The computational complexity of universal hashing," in Proceedings of the Twenty-second Annual ACM Symposium on Theory of Computing, STOC '90 (ACM, New York), pp. 235-243.  
Marandi, A., N.C. Leindecker, V. Pervak, R.L. Byer, and K.L. Vodopyanov, 2012, "Coherence properties of a broadband femtosecond mid-IR optical parametric oscillator operating at degeneracy," Opt. Express 20, 7255.  
Marandi, A., N. C. Leindecker, K. L. Vodopyanov, and R. L. Byer, 2011, "Twin Degenerate OPO for Quantum Random Bit Generation," in Nonlinear Optics (Optical Society of America), paper NME4.  
Marandi, A., N. C. Leindecker, K. L. Vodopyanov, and R. L. Byer, 2012, "All-optical quantum random bit generation from intrinsically binary phase of parametric oscillators," Opt. Express 20, 19322-19330.  
Marsaglia, G., 1968, "Random numbers fall mainly in the planes," Proc. Natl. Acad. Sci. U.S.A. 61, 25-28.  
Marsaglia, G., 1996, "DIEHARD: a battery of tests of randomness," http://www.csis.hku.hk/cisc/download/index2.htm.  
Marsili, F., et al., 2013, "Detecting single infrared photons with  $93\%$  system efficiency," Nat. Photonics 7, 210.  
Martin, A., B. Sanguinetti, C. C. W. Lim, R. Houlmann, and H. Zbinden, 2015, "Quantum Random Number Generation for 1.25-GHz Quantum Key Distribution Systems," J. Lightwave Technol. 33, 2855-2859.  
Martino, A. J., and G. M. Morris, 1991, "Optical random number generator based on photoevent locations," Appl. Opt. 30, 981-989.  
Matsumoto, M., and T. Nishimura, 1998, "Mersenne Twister: a 623-dimensionally equidistributed uniform pseudo-random number generator," ACM Trans. Model. Comput. Simul. 8, 3-30.  
Matsumoto, M., T. Nishimura, M. Hagita, and M. Saito, 2005, "Cryptographic Mersenne Twister and Fubuki stream/block cipher," Cryptographic ePrint http://eprint.iacr.org/2005/165.  
Matsumoto, M., M. Saito, T. Nishimura, and M. Hagita, 2008, "CryptMT3 Stream Cipher," in New Stream Cipher Designs, Lecture Notes in Computer Science Vol. 4986 (Springer, Berlin), pp. 7-19.  
Matsumoto, M., I. Wada, A. Kuramoto, and H. Ashihara, 2007, "Common defects in initialization of pseudorandom number generators," ACM Trans. Model. Comput. Simul. 17, 15.  
Màttar, A., P. Skrzypczyk, J. B. Brask, D. Cavalcanti, and A. Acín, 2015, "Optimal randomness generation from optical Bell experiments," New J. Phys. 17, 022003.  
Mauerer, W., C. Portmann, and V. B. Scholz, 2012, “A modular framework for randomness extraction based on Trevisan's construction,” arXiv:1212.0520.  
Maurer, U., 1992, “A Universal Statistical Test for Random Bit Generators,” J. Cryptol. 5, 89-105.  
Mayers, D., and A. Yao, 1998, "Quantum cryptography with imperfect apparatus," in Proceedings of the 39th Annual Symposium on Foundations of Computer Science, FOCS '98 (IEEE Computer Society, Washington, DC), pp. 503-509.  
McInnes, J.L., and B. Pinkas, 1991, "On the impossibility of private key cryptography with weakly random keys," in Advances in Cryptology-CRYPTO'90, Lecture Notes in Computer Science Vol. 537 (Springer, Berlin), pp. 421-435.  
Metropolis, N., and S. Ulam, 1949, "The Monte Carlo Method," J. Am. Stat. Assoc. 44, 335-341.

Michaelis, K., C. Meyer, and J. Schwenk, 2013, "Randomly Failed! The State of Randomness in Current Java Implementations," in Topics in Cryptology CT-RSA 2013, Lecture Notes in Computer Science Vol. 7779 (Springer, Berlin), pp. 129-144.  
Micro Photon Devices, 2014, "Quantum random number generator," http://www.micro-photon-devices.com/Products/Instrumentation/ Quantum-Random-Number.  
Milchev, A., K. Binder, and D. W. Heermann, 1986, “Fluctuations and lack of self-averaging in the kinetics of domain growth,” Z. Phys. B 63, 521–535.  
Miller, C. A., and Y. Shi, 2014, "Universal security for randomness expansion," arXiv:1411.6608.  
Mitchell, M. W., C. Abellán, and W. Amaya, 2015, "Strong experimental guarantees in ultrafast quantum random number generation," Phys. Rev. A 91, 012314.  
Mo, X.-F., B. Zhu, Z.-F. Han, Y.-Z. Gui, and G.-C. Guo, 2005, "Faraday-Michelson system for quantum cryptography," Opt. Lett. 30, 2632-2634.  
Motwani, R., and P. Raghavan, 1996, "Randomized algorithms," ACM Comput. Surv. 28, 33-37.  
Murry, H.F., 1970, "A General Approach for Generating Natural Random Variables," IEEE Trans. Comput. C-19, 1210-1213.  
Nabors, C. D., S. T. Yang, T. Day, and R. L. Byer, 1990, "Coherence properties of a doubly resonant monolithic optical parametric oscillator," J. Opt. Soc. Am. B 7, 815.  
Nadj-Perge, S., I. K. Drozdov, J. Li, H. Chen, S. Jeon, J. Seo, A. H. MacDonald, B. A. Bernevig, and A. Yazdani, 2014, "Observation of Majorana fermions in ferromagnetic atomic chains on a superconductor," Science 346, 602-607.  
Nahin, P. J., 1999, Time Machines (Springer, New York).  
Naruse, M., M. Berthel, A. Drezet, S. Huant, M. Aono, H. Hori, and S.-J. Kim, 2015, "Single-photon decision maker," Sci. Rep. 5, 13253.  
National Institute of Standards and Technology, 2001, "Security Requirements for Cryptographic Modules," Federal Information Processing Standards Publication FIPS PUB 140-2.  
National Institute of Standards and Technology, 2011, "NIST Randomness Beacon," http://www.nist.gov/itl/csd/ct/nist beacon.cfm.  
National Institute of Standards and Technology, 2012, FIPS PUB 180-4, Secure Hash Standard.  
Networking Working Group, 1996, RFC 1948, Defending Against Sequence Number Attacks [https://tools.ietf.org/html/rfc1948].  
Networking Working Group, 2005, RFC 4086, Randomness Requirements for Security [https://tools.ietf.org/html/rfc4086].  
Nie, Y.-Q., L. Huang, Y. Liu, F. Payne, J. Zhang, and J.-W. Pan, 2015, "The generation of 68 Gbps quantum random number by measuring laser phase fluctuations," Rev. Sci. Instrum. 86, 063105.  
Nie, Y.-Q., H.-F. Zhang, Z. Zhang, J. Wang, X. Ma, J. Zhang, and J.-W. Pan, 2014, "Practical and fast quantum random number generation based on photon arrival time relative to external reference," Appl. Phys. Lett. 104, 051110.  
Niederreiter, H., 1978, "Quasi-Monte Carlo methods and pseudorandom numbers," Bull. Am. Math. Soc. 84, 957-1041.  
Nisan, N., 1996, "Extracting randomness: how and why. A survey," in Proceedings of Computational Complexity (IEEE Computer Society Press, New York), pp. 44-58.  
Nisan, N., and A. Ta-Shma, 1999, "Extracting Randomness: A Survey and New Constructions," J. Comput. Syst. Sci. 58, 148-173.  
Nisan, N., and A. Wigderson, 1994, "Hardness vs randomness," J. Comput. Syst. Sci. 49, 149-167.  
Nisan, N., and D. Zuckerman, 1996, "Randomness is linear in space," J. Comput. Syst. Sci. 52, 43-52.

Nohl, K., D. Evans, Starbug, and H. Plötz, 2008, "Reverse-engineering a Cryptographic RFID Tag," in Proceedings of the 17th Conference on Security Symposium, SS'08 July (USENIX Association, Berkeley, CA), pp. 185-193.  
Nyquist, H., 1928, "Thermal Agitation of Electric Charge in Conductors," Phys. Rev. 32, 110-113.  
Oberreiter, L., and I. Gerhardt, 2016, "Light on a beam splitter: More randomness with single photons," Laser Photonics Rev. 10, 108-115.  
Oestreich, M., M. Römer, R. J. Haug, and D. Hagele, 2005, "Spin noise spectroscopy in GaAs," Phys. Rev. Lett. 95, 216603.  
Olmschenk, S., K. C. Younge, D. L. Moehring, D. N. Matsukevich, P. Maunz, and C. Monroe, 2007, "Manipulation and detection of a trapped  $\mathrm{Yb^{+}}$  hyperfine qubit," Phys. Rev. A 76, 052314.  
Ossola, G., and A. D. Sokal, 2004, "Systematic errors due to linear congruential random-number generators with the Swendsen-Wang algorithm: A warning," Phys. Rev. E 70, 027701.  
Ou, Z. Y., C. K. Hong, and L. Mandel, 1987, “Relation between input and output states for a beam splitter,” Opt. Commun. 63, 118-122.  
Owens, I. J., R. J. Hughes, and J. E. Nordholt, 2008, "Entangled quantum-key-distribution randomness," Phys. Rev. A 78, 022307.  
Parisi, G., and F. Rapuano, 1985, "Effects of the random number generator on computer simulations," Phys. Lett. B 157, 301-302.  
Pawlowski, M., and N. Brunner, 2011, "Semi-device-independent security of one-way quantum key distribution," Phys. Rev. A 84, 010302.  
Peev, M., et al., 2009, "The SECOQC quantum key distribution network in Vienna," New J. Phys. 11, 075001.  
Penzkofer, A., A. Laubereau, and W. Kaiser, 1979, "High intensity Raman interactions," Prog. Quantum Electron. 6, 55-140.  
Peres, A., 2000, "Delayed choice for entanglement swapping," J. Mod. Opt. 47, 139-143.  
Peres, Y., 1992, "Iterating von Neumann's Procedure for Extracting Random Bits," Ann. Stat. 20, 590-597.  
Petrie, C. S., and J. A. Connelly, 2000, "A noise-based IC random number generator for applications in cryptography," IEEE Trans. Circuits Syst. I 47, 615-621.  
PicoQuant, 2014, "PQRNG 150 Quantum Random Number Generator," http://www.picoquant.com/products/category/quantum-random-number-generator/pqrng-150-quantum-random-number-generator.  
Pierret, R. F., 1996, Semiconductor device fundamentals (Addison-Wesley, Reading, MA), 2nd ed.  
Pironio, S., and S. Massar, 2013, "Security of practical private randomness generation," Phys. Rev. A 87, 012336.  
Pironio, S., et al., 2010, "Random numbers certified by Bell's theorem," Nature (London) 464, 1021-1024.  
Pivoluska, M., M. Plesch, M. Pivoluskaa, and M. Plesch, 2014, "Device Independent Random Number Generation," Acta Phys. Slovaca 64, 601-664 [http://www.physics.sk/aps/pub.php? y=2014&pub=aps-14-06].  
Platt, C., and A. Logue, 2015, "Really, really random number generator," Make Magazine 45, 78-81 [http://makezine.com/projects/really-really-random-number-generator/].  
Plesch, M., and M. Pivoluska, 2014, "Device-independent randomness amplification with a single device," Phys. Lett. A 378, 2938-2944.  
PokerStars, 2016, "Data Privacy for our Software," Description of the shuffling method retrieved from https://www.pokerstars.com/poker/room/features/security/ (2016-8-19).  
Prasad, S., M. O. Scully, and W. Marthienssen, 1987, “A quantum description of the beam splitter,” Opt. Commun. 62, 139–145.

Qi, B., Y.-M. Chi, H.-K. Lo, and L. Qian, 2010, "High-speed quantum random number generation by measuring phase noise of a single-mode laser," Opt. Lett. 35, 312.  
Qiurong, Y., Z. Baosheng, L. Qinghong, and Z. Nanrun, 2014, "Multi-bit quantum random number generation by measuring positions of arrival photons," Rev. Sci. Instrum. 85, 103116.  
QRB121, 2014, "QRBG121 Quantum Random Number Generator," http://qrbg.ird.hr.  
Quintessence Labs, 2014, "Fast Quantum Random Number Generation," http://www.quintessencelabs.com/quantum-cybersecurity/?tab=random-number.  
Qutools, 2014, "quRNG—Quantum Random Number Generator," http://www.qutools.com/products/quRNG/index.php.  
Radhakrishnan, J., and A. Ta-Shma, 2000, "Bounds for dispersers, extractors, and depth-two superconcentrators," SIAM J. Discrete Math. 13, 2-24.  
RAND Corporation, 1955, "A million random digits with 100,000 normal deviates," http://www.rand.org/pubs/monograph Reports/ MR1418.html.  
Rao, A., 2009, "Extractors for a constant number of polynomially small min-entropy independent sources," SIAM J. Comput. 39, 168-194.  
Rarity, J. G., P. C. M. Owens, and P. R. Tapster, 1994, "Quantum Random-number Generation and Key Sharing," J. Mod. Opt. 41, 2435-2444.  
Raymer, M.G., K. Rzaczewski, and J. Mostowski, 1982, "Pulse-energy statistics in stimulated Raman scattering," Opt. Lett. 7, 71-73.  
Raymer, M. G., and I. A. Walmsley, 1990, "The Quantum Coherence Properties of Stimulated Raman Scattering," in Progress in Optics XXVIII, edited by E. Wolf (North-Holland Publishing Company, Amsterdam), pp. 181-270.  
Raymer, M. G., I. A. Walmsley, J. Mostowski, and B. Sobolewka, 1985, "Quantum theory of spatial and temporal coherence properties of stimulated Raman scattering," Phys. Rev. A 32, 332.  
Raz, R., 2005, "Extractors with weak random seeds," in Proceedings of the Thirty-seventh Annual ACM Symposium on Theory of Computing, STOC '05 (ACM, New York), pp. 11-20.  
Razavy, M., 2014, Quantum theory of tunneling (World Scientific, Singapore), 2nd ed.  
Razzari, L., D. Duchesne, M. Ferrera, R. Morandotti, S. Chu, B. E. Little, and D. J. Moss, 2010, "CMOS-compatible integrated optical hyper-parametric oscillator," Nat. Photonics 4, 41-45.  
Reidler, I., Y. Aviad, M. Rosenbluh, and I. Kanter, 2009, "Ultrahigh-speed random number generation based on a chaotic semiconductor laser," Phys. Rev. Lett. 103, 024102.  
Ren, M., E. Wu, Y. Liang, Y. Jian, G. Wu, and H. Zeng, 2011, "Quantum random-number generator based on a photon-number-resolving detector," Phys. Rev. A 83, 023820.  
Renner, R., 2005, "Security of quantum key distribution," Ph.D. thesis, ETH Zürich, http://dx.doi.org/10.3929/ethz-a-005115027.  
Renner, R., and R. König, 2005, "Universally composable privacy amplification against quantum adversaries," in Theory of Cryptography, TCC 2005, Lecture Notes in Computer Science, Vol. 3378 (Springer, Berlin/Heidelberg), pp. 407-425.  
Renyi, A., 1961, "On Measures of Entropy and Information," in Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability, Vol. 1: Contributions to the Theory of Statistics (University of California Press, Berkeley, CA), pp. 547-561.  
Reznikov, M., R. de Picciotto, M. Heiblum, D. C. Glattli, A. Kumar, and L. Saminadayar, 1998, "Quantum shot noise," Superlattices Microstruct. 23, 901-915.

Ribordy, G., O. Guinnard, and ID Quantique, 2009, "Method and apparatus for generating true random numbers by way of a quantum optics process," Patent US7519641.  
Rice, S. O., 1944, “Mathematical Analysis of Random Noise,” Bell Syst. Tech. J. 23, 282-332.  
Rukhin, A., et al., 2010, "A statistical test suite for random and pseudorandom number generators for cryptographic applications," NIST Special Publication 800-22, Revision 1.a.  
Saito, T., K. Ishii, I. Tatsuno, S. Sukagawa, and T. Yanagita, 2010, "Randomness and Genuine Random Number Generator With Self-testing Functions," in Joint International Conference on Supercomputing in Nuclear Applications and Monte Carlo 2010 (SNA+MC2010).  
Sanguinetti, B., A. Martin, H. Zbinden, and N. Gisin, 2014, "Quantum Random Number Generation on a Mobile Phone," Phys. Rev. X 4, 031056.  
Santha, M., and U. V. Vazirani, 1986, "Generating quasi-random sequences from semi-random sources," J. Comput. Syst. Sci. 33, 75-87.  
Santoro, R., O. Sentieys, and S. Roy, 2009a, "On-line monitoring of Random Number Generators for embedded security," in 2009 IEEE International Symposium on Circuits and Systems (IEEE, New York), pp. 3050-3053.  
Santoro, R., O. Sentieys, and S. Roy, 2009b, "On-the-Fly Evaluation of FPGA-Based True Random Number Generator," in 2009 IEEE Computer Society Annual Symposium on VLSI (IEEE, New York), pp. 55-60.  
Sartor, P., K. Zimmermann, and Sony Corporation, 2015, "Optical random number generator and method for generating a random number," U.S. Patent 2015/0261502 A1.  
Sasaki, M., et al., 2011, "Field test of quantum key distribution in the Tokyo QKD Network," Opt. Express 19, 10387.  
Scarani, V., A. Acín, G. Ribordy, and N. Gisin, 2004, "Quantum cryptography protocols robust against photon number splitting attacks for weak laser pulse implementations," Phys. Rev. Lett. 92, 057901.  
Scarani, V., H. Bechmann-Pasquinucci, N. J. Cerf, M. Dusek, N. Lütkenhaus, and M. Peev, 2009, "The security of practical quantum key distribution," Rev. Mod. Phys. 81, 1301-1350.  
Scheidl, T., et al., 2010, “Violation of local realism with freedom of choice,” Proc. Natl. Acad. Sci. U.S.A. 107, 19708-19713.  
Schindler, W., and W. Killmann, 2003, "Evaluation Criteria for True (Physical) Random Number Generators Used in Cryptographic Applications," in Cryptographic Hardware and Embedded Systems—CHES 2002, Lecture Notes in Computer Science Vol. 2523 (Springer, Berlin), pp. 431-449.  
Schmid, F., and N.B. Wilding, 1996, "Errors in Monte Carlo simulations using shift register random number generators," Int. J. Mod. Phys. C 06, 781.  
Schmidt, H., 1970a, "A PK test with electronic equipment," J. Parapsychology 34, 175-181.  
Schmidt, H., 1970b, "Quantum Mechanical Random Number Generator," J. Appl. Phys. 41, 462-468.  
Schottky, W., 1918, "Über spontane Stromschwankungen in verschiedenen Elektrizitätsleitern," Ann. Phys. (Berlin) 362, 541-567.  
Scully, M. O., and S. Stenholm, 1988, "The Role of Vacuum Fluctuations and Spontaneous Emission in the Laser Linewidth," Phys. Scr. T21, 119.  
Shadbolt, P., J. C. F. Mathews, A. Laing, and J. L. O'Brien, 2014, "Testing foundations of quantum mechanics with photons," Nat. Phys. 10, 278-286.  
Shalm, L. K., et al., 2015, "Strong Loophole-Free Test of Local Realism," Phys. Rev. Lett. 115, 250402.

Shaltiel, R., 2004, "Recent developments in explicit constructions of extractors," Bulletin of the EATCS 77, 10.  
Shaltiel, R., 2008, "How to get more mileage from randomness extractors," Random Structures & Algorithms 33, 157-186.  
Shaltiel, R., 2011, "An Introduction to Randomness Extractors," in Automata, languages and programming, Lecture Notes in Computer Science Vol. 6756 (Springer, Berlin), pp. 21-41.  
Shannon, C. E., 1948, “A Mathematical Theory of Communication,” The Bell System's Technical Journal 27, 379-423.  
Shchur, L. N., J. R. Heringa, and H. W. J. Blöte, 1997, "Simulation of a directed random-walk model The effect of pseudo-random-number correlations," Physica A (Amsterdam) 241, 579-592.  
Shen, Y., L. Tian, and H. Zou, 2010, "Practical quantum random number generator based on measuring the shot noise of vacuum states," Phys. Rev. A 81, 063814.  
Shenoy, H. A., R. Srikanth, and T. Sriniva, 2013, "Efficient quantum random number generation using quantum indistinguishability," Fluct. Noise Lett. 12, 1350020.  
Shepherd, S.J., 1996, "Lessons learned from security weaknesses in the Netscape World Wide Web browser," in IEE Colloquium on Public Uses of Cryptography, Vol. 1996 (IEE, Savoy Place, London, UK), pp. 7(1)-7(6).  
Shor, P. W., 1997, "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer," SIAM J. Comput. 26, 1484.  
Shumow, D., and N. Ferguson, 2007, "On the possibility of a back door in the NIST SP800-90 Dual EC PRNG," CRYPTO 2007 Rump Session [http://rump2007.cr.yp.to/15-shumow.pdf].  
Silverman, M. P., W. Strange, C. R. Silverman, and T. C. Lipscombe, 1999, "Tests of alpha-, beta-, and electron capture decays for randomness," Phys. Lett. A 262, 265-73.  
Skorski, M., 2015, "True random number generators secure in a changing environment: Improved security bounds," in SOFSEM 2015: Theory and Practice of Computer Science, Lecture Notes in Computer Science Vol. 8939 (Springer, Berlin), pp. 590-602.  
Smithey, D. T., M. Belsley, K. Wedding, and M. G. Raymer, 1991, "Near quantum-limited phase memory in a Raman amplifier," Phys. Rev. Lett. 67, 2446-2449.  
Somlo, P. I., 1975, “Zener-diode noise generators,” Electron. Lett. 11, 290.  
Song, X.-T., H.-W. Li, Z.-Q. Yin, W.-Y. Liang, C.-M. Zhang, Y.-G. Han, W. Chen, and Z.-F. Han, 2015, "Phase-Coding Self-Testing Quantum Random Number Generator," Chin. Phys. Lett. 32, 080302.  
Soubusta, J., O. Haderka, and M. Hendrych, 2001, "Quantum random number generator," in Proc. SPIE, 12th Czech-Slovak-Polish Optical Conference on Wave and Quantum Aspects of Contemporary Optics, Vol. 4356 (SPIE-International Society for Optical Engineering, Bellingham, WA), pp. 54-60.  
Soubusta, J., O. Haderka, M. Hendrych, and P. Pavlicek, 2003, "Experimental realization of Quantum random number generator," in Proc. SPIE, 13th Czech-Slovak-Polish Optical Conference on Wave and Quantum Aspects of Contemporary Optics, Vol. 5259 (SPIE-International Society for Optical Engineering, Bellingham, WA), pp. 7-13.  
Soucarros, M., C. Canovas-Dumas, J. Clédière, P. Elbaz-Vincent, and D. Réal, 2011, "Influence of the temperature on true random number generators," in 2011 IEEE International Symposium on Hardware-Oriented Security and Trust (HOST) (IEEE, New York), pp. 24-27.  
Soucarros, M., J. Clédière, C. Dumas, and P. Elbaz-Vincent, 2013, "Fault Analysis and Evaluation of a True Random Number

"Generator Embedded in a Processor," Journal of Electronic Testing: Theory and Applications 29, 367-381.  
Sowey, E. R., 1972, “A Chronological and Classified Bibliography on Random Number Generation and Testing,” Int. Stat. Rev. **40**, No. 3, 355–371 [http://www.jstor.org/stable/1402472].  
Srinivasan, A., M. Mascagni, and D. Ceperley, 2003, "Testing parallel random number generators," Parallel Comput. 29, 69-94.  
Stefanov, A., N. Gisin, O. Guinnard, L. Guinnard, and H. Zbinden, 2000, "Optical quantum random number generator," J. Mod. Opt. 47, 595-598.  
Stevanovic, R., G. Topic, K. Skala, M. Stipcevic, and B. M. Rogina, 2008, "Quantum Random Bit Generator Service for Monte Carlo and Other Stochastic Simulations," in Large-Scale Scientific Computing, Lecture Notes in Computer Science, Vol. 4818 (Springer, Berlin), pp. 508-515.  
Stich, D., J. Zhou, T. Korn, R. Schulz, D. Schuh, W. Wegscheider, M. W. Wu, and C. Schüller, 2007, "Effect of initial spin polarization on spin dephasing and the electron  $g$  factor in a high-mobility two-dimensional electron system," Phys. Rev. Lett. 98, 176401.  
Stipčevic, M., 2004, "Fast nondeterministic random bit generator based on weakly correlated physical events," Rev. Sci. Instrum. 75, 4442.  
Stipčević, M., 2012, "Quantum random number generators and their applications in cryptography," in Proc. SPIE, Advanced Photon Counting Techniques VI, 837504, Vol. 8375 (SPIE-International Society for Optical Engineering, Bellingham, WA), pp. 837504.  
Stipčević, M., 2014, "Preventing detector blinding attack and other random number generator attacks on quantum cryptography by use of an explicit random number generator," arXiv:1403.0143.  
Stipčević, M., and J. E. Bowers, 2015, "Spatio-temporal optical random number generator," Opt. Express 23, 11619.  
Stipčevic, M., and C. K. Koç, 2014, "True Random Number Generators," Open Problems in Mathematics and Computational Science (Springer International Publishing, Switzerland), pp. 275-315.  
Stipčević, M., and B. M. Rogina, 2007, "Quantum random number generator based on photonic emission in semiconductors," Rev. Sci. Instrum. 78, 045104.  
Stipčević, M., and R. Ursin, 2015, "An On-Demand Optical Quantum Random Number Generator with In-Future Action and Ultra-Fast Response," Sci. Rep. 5, 10214.  
Stojanovski, T., and L. Kocarev, 2001, "Chaos-based random number generators-part I: analysis," IEEE Trans. Circuits Syst. I 48, 281-288.  
Stojanovski, T., J. Pihl, and L. Kocarev, 2001, “Chaos-based random number generators. Part II: practical realization,” IEEE Trans. Circuits Syst. I 48, 382-385.  
Stucki, D., S. Burri, E. Charbon, C. Chunnilall, A. Meneghetti, and F. Regazzoni, 2013, "Towards a high-speed quantum random number generator," in Proc. SPIE, Emerging Technologies in Security and Defence; and Quantum Security II; and Unmanned Sensor Systems X, 88990R Vol. 8899 (SPIE-International Society for Optical Engineering, Bellingham, WA), pp. 837504.  
Sunada, S., T. Harayama, K. Arai, K. Yoshimura, K. Tsuzuki, A. Uchida, and P. Davis, 2011, "Random optical pulse generation with bistable semiconductor ring lasers," Opt. Express 19, 7439.  
Sunar, B., W. J. Martin, and D. R. Stinson, 2007, "A Provably Secure True Random Number Generator with Built-In Tolerance to Active Attacks," IEEE Trans. Comput. 56, 109-119.  
Suresh, V. B., D. Antonioli, and W. P. Burleson, 2013, "On-chip lightweight implementation of reduced NIST randomness test suite," in Proceedings of the 2013 IEEE International Symposium

on Hardware-Oriented Security and Trust, HOST 2013 (IEEE, New York), pp. 93-98.  
Symul, T., S. M. Assad, and P. K. Lam, 2011, "Real time demonstration of high bitrate quantum random number generation with coherent laser light," Appl. Phys. Lett. 98, 231103.  
Szczepanski, J., E. Wajnryb, J.M. Amigo, M.V. Sanchez-Vives, and M. Slater, 2004, "Biometric random number generators," Computers & Security 23, No. 1, 77-84.  
Takeuchi, S., and T. Nagai, 1983, "Random pulser based on photon counting," Nucl. Instrum. Methods Phys. Res. 215, 199-202.  
Tang, G.-Z., M.-S. Jiang, S.-H. Sun, X.-C. Ma, C.-Y. Li, and L.-M. Liang, 2013, "Quantum Random Number Generation Based on Quantum Phase Noise," Chin. Phys. Lett. 30, 114207.  
Ta-Shma, A., 1996, "On extracting randomness from weak random sources (extended abstract)," in Proceedings of the Twenty-eighth Annual ACM Symposium on Theory of Computing, STOC '96 (ACM, New York), pp. 276-285.  
Ta-Shma, A., 2011, "Short seed extractors against quantum storage," SIAM J. Comput. 40, 664-677.  
Taylor, G., and G. Cox, 2011, "Digital randomness," IEEE Spectrum 48, 32-58.  
Tehranipoor, M., and F. Koushanfar, 2010, "A Survey of Hardware Trojan Taxonomy and Detection," IEEE Design and Test of Computers 27, 10-25.  
Thamrin, N. M., G. Witjaksono, A. Nuruddin, and M. S. Abdullah, 2008, "A Photonic-based Random Number Generator for Cryptographic Application," in 2008 Ninth ACIS International Conference on Software Engineering, Artificial Intelligence, Networking, and Parallel/Distributed Computing (IEEE, New York), pp. 356-361.  
Thinh, L. P., L. Sheridan, and V. Scarani, 2013, "Bell tests with min-entropy sources," Phys. Rev. A 87, 062121.  
Thomson, W.E., 1959, "ERNIE-A Mathematical and Statistical Analysis," Journal of the Royal Statistical Society Series A (General) 122, 301-333.  
Tisa, S., F. Villa, A. Giudice, G. Simmerle, and F. Zappa, 2015, "High-Speed Quantum Random Number Generation Using CMOS Photon Counting Detectors," IEEE J. Sel. Top. Quantum Electron. 21, 23-29.  
Tittel, W., J. Brendel, N. Gisin, and H. Zbinden, 1999, "Long-distance Bell-type tests using energy-time entangled photons," Phys. Rev. A 59, 4150-4163.  
Tolman, R.C., 1917, The Theory of the Relativity of Motion (University of California Press, Berkeley, CA).  
Tomamichel, M., C. Schaffner, A. Smith, and R. Renner, 2011, "Leftover hashing against quantum side information," IEEE Trans. Inf. Theory 57, 5524-5535.  
Trevisan, L., 2001, "Extractors and pseudorandom generators," J. ACM 48, 860-879.  
Trevisan, L., and S. Vadhan, 2000, "Extracting randomness from sample distributions," in Proceedings of the 41st Annual Symposium on Foundations of Computer Science, 2000 (IEEE Computer Society, Los Alamitos, CA), pp. 32-42.  
Trifonov, A., H. Vig, and Magiq Technologies, Inc., 2007, "Quantum noise random number generator," Patent US7284024.  
Troyer, M., and R. Renner, 2012, "A randomness extractor for the quantis device," ID Quantique Technical Report http:// www.idquantique.com/wordpress/wp-content/uploads/quantis-rndextract-techpaper.pdf.  
Turan, M. S., E. Barker, J. Kelsey, K. A. McKay, M. L. Baish, and M. Boyle, 2016, "Recommendation for the Entropy Sources Used

for Random Bit Generation," (Second DRAFT) NIST Special Publication 800-90B.  
Uchida, A., et al., 2008, "Fast physical random bit generation with chaotic semiconductor lasers," Nat. Photonics 2, 728-732.  
Um, M., X. Zhang, J. Zhang, Y. Wang, S. Yangchao, D.-L. Deng, L.-M. Duan, and K. Kim, 2013, "Experimental certification of random numbers via quantum contextuality," Sci. Rep. 3, 1627.  
University of Geneva, 2004, "Online randomness source," http:// www.randomnumbers.info/.  
Vadhan, S., 2007, “The unified theory of pseudorandomness: Guest column,” ACM SIGACT News 38, 39-54.  
Vallone, G., D. G. Marangon, M. Tomasin, and P. Villoresi, 2014, "Quantum randomness certified by the uncertainty principle," Phys. Rev. A 90, 052327.  
Vartsky, D., D. Bar, P. Gilad, A. Schon, and Soreq Nuclear Research Center, El-Mul Technologies Ltd., 2011, "High-speed, true random-number generator," U.S. Patent 7930333 B2.  
Vaskova, A., C. López-Ongil, A. Jiménez-Horas, E. San Millán, and L. Entrena, 2010, "Robust cryptographic ciphers with on-line statistical properties validation," in Proceedings of the 2010 IEEE 16th International On-Line Testing Symposium, IOLTS 2010 (IEEE, New York), pp. 208-210.  
Vaskova, A., C. López-Ongil, E. San Millán, A. Jiménez-Horas, and L. Entrena, 2011, "Accelerating secure circuit design with hardware implementation of diehard battery of tests of randomness," in Proceedings of the 2011 IEEE 17th International On-Line Testing Symposium, IOLTS 2011 IEEE, New York), pp. 179-181.  
Vattulainen, I., T. Ala-Nissila, and K. Kankaala, 1994, "Physical tests for random numbers in simulations," Phys. Rev. Lett. 73, 2513-2516.  
Vattulainen, I., T. Ala-Nissila, and K. Kankaala, 1995, "Physical models as tests of randomness," Phys. Rev. E 52, 3205-3214.  
Vazirani, U., 1987, "Efficiency considerations in using semi-random sources," in Proceedings of the Nineteenth Annual ACM Symposium on Theory of Computing, STOC '87 (ACM, New York), pp. 160-168.  
Vazirani, U., and T. Vidick, 2012, "Certifiable Quantum Dice," Phil. Trans. R. Soc. A 370, 3432-3448.  
Vazirani, U., and T. Vidick, 2014, "Fully device-independent quantum key distribution," Phys. Rev. Lett. 113, 140501.  
Vazirani, U. V., 1987, "Strong communication complexity or generating quasi-random sequences from two communicating semirandom sources," Combinatorica 7, 375-392.  
Vazirani, U. V., and V. V. Vazirani, 1985a, "Efficient and Secure Pseudo-Random Number Generation (Extended Abstract)," in Advances in Cryptology -CRYPTO'84, Lecture Notes in Computer Science Vol. 196 (Springer, Berlin/Heidelberg), pp. 193-202.  
Vazirani, U. V., and V. V. Vazirani, 1985b, "Random polynomial time is equal to slightly-random polynomial time," in 26th Annual Symposium on Foundations of Computer Science, 1985 (IEEE Computer Society Press, Washington, DC), pp. 417-428.  
Vincent, C.H., 1970, "The generation of truly random binary numbers," J. Phys. E 3, 594.  
Vincent, C. H., 1971, "Precautions for accuracy in the generation of truly random binary numbers," J. Phys. E 4, 825-828.  
Vivoli, V. C., P. Sekatski, J.-D. Bancal, C. C. W. Lim, A. Martin, R. T. Thew, H. Zbinden, N. Gisin, and N. Sangouard, 2015, "Comparing different approaches for generating random numbers device-independently using a photon pair source," New J. Phys. 17, 023023.

von Neumann, J., 1951, "Various techniques used in connection with random digits," republished in Collected works, Vol. 5, Design of computers, theory of automata and numerical analysis (Pergamon Press, Oxford).  
Wahl, M., M. Leifgen, M. Berlin, and O. Benson, 2012, "Addendum: An ultrafast quantum random number generator with provably bounded output bias based on photon arrival time measurements," Appl. Phys. Lett. 101, 159901.  
Wahl, M., M. Leifgen, M. Berlin, T. Röhlicke, H.-J. Rahn, and O. Benson, 2011, "An ultrafast quantum random number generator with provably bounded output bias based on photon arrival time measurements," Appl. Phys. Lett. 98, 171105.  
Walenta, N., et al., 2015, "Practical aspects of security certification for commercial quantum technologies," in Proc. SPIE, ElectroOptical and Infrared Systems: Technology and Applications XII; and Quantum Information Science and Technology (SPIE-International Society for Optical Engineering, Bellingham, WA), Vol. 9648, p. 96480U.  
Walker, J., 1996, "HotBits: Genuine random numbers, generated by radioactive decay," http://www.fourmilab.ch/hotbits/.  
Walmsley, I. A., and M. G. Raymer, 1983, "Observation of Macroscopic Quantum Fluctuations in Stimulated Raman Scattering," Phys. Rev. Lett. 50, 962-965.  
Wang, F.-X., C. Wang, W. Chen, S. Wang, F.-S. Lv, D.-Y. He, Z.-Q. Yin, H.-W. Li, G.-C. Guo, and Z.-F. Han, 2015, "Robust quantum random number generator based on avalanche photodiodes," J. Lightwave Technol. 33, 3319-3326.  
Wang, J.-M., T.-Y. Xie, H.-F. Zhang, D.-X. Yang, C. Xie, and J. Wang, 2015, "A Bias-Free Quantum Random Number Generation Using Photon Arrival Time Selectively," IEEE Photonics J. 7, No. 2, 1-8.  
Wang, P. X., G. Longo, and Y. S. Li, 2006, "Scheme for a quantum random number generator," J. Appl. Phys. 100, 056107.  
Watson, T., 2016, "The complexity of estimating min-entropy," Comput. Complex. 25, 153-175.  
Wayne, M. A., E. R. Jeffrey, G. M. Akselrod, and P. G. Kwiat, 2009, "Photon arrival time quantum random number generation," J. Mod. Opt. 56, 516-522.  
Wayne, M. A., and P. G. Kwiat, 2010, "Low-bias high-speed quantum random number generator via shaped optical pulses," Opt. Express 18, 9351-9357.  
Wegman, M. N., and J. L. Carter, 1981, "New hash functions and their use in authentication and set equality," J. Comput. Syst. Sci. 22, 265-279.  
Wei, W., and H. Guo, 2009a, “Bias-free true random-number generator,” Opt. Lett. 34, 1876.  
Wei, W., and H. Guo, 2009b, "Quantum random number generator based on the photon number decision of weak laser pulses," in 2009 Conference on Lasers & Electro Optics & The Pacific Rim Conference on Lasers and Electro-Optics (IEEE, New York), pp. 1-2.  
Wei, W., W. Tang, and H. Guo, 2010, "High speed true random number generation using chaotic light," in 2010 Conference on Lasers and Electro-Optics (CLEO) and Quantum Electronics and Laser Science Conference (QELS) (Optical Society of America), p. 1-2.  
Weihs, G., T. Jennewein, C. Simon, H. Weinfurter, and A. Zeilinger, 1998, "Violation of Bell's Inequality under Strict Einstein Locality Conditions," Phys. Rev. Lett. 81, 5039.  
Wheeler, J. A., 1978, “The ‘Past’ and the ‘Delayed-Choice’ Double-Slit Experiment,” in Mathematical Foundations of Quantum Theory (Academic Press, New York), pp. 9–48.

Wilber, S. A., ComScire, 2014, "Entropy Analysis and System Design for Quantum Random Number Generators in CMOS Integrated Circuits," https://comscire.com/files/whitepaper/Pure_Quantum_White_Paper.pdf.  
Williams, C. R. S., J. C. Salevan, X. Li, R. Roy, and T. E. Murphy, 2010, "Fast physical random number generator using amplified spontaneous emission," Opt. Express 18, 23584-23597.  
Wong, W. S., H. A. Haus, L. A. Jiang, P. B. Hansen, and M. Margalit, 1998, "Photon statistics of amplified spontaneous emission noise in a 10-Gbit/s optically preamplified direct-detection receiver," Opt. Lett. 23, 1832.  
Wu, L.-A., H. J. Kimble, J. L. Hall, and H. Wu, 1986, "Generation of Squeezed States by Parametric Down Conversion," Phys. Rev. Lett. 57, 2520-2523.  
Wu, L.-A., M. Xiao, and H. J. Kimble, 1987, "Squeezed states of light from an optical parametric oscillator," J. Opt. Soc. Am. B 4, 1465.  
Xu, F., B. Qi, X. Ma, H. Xu, H. Zheng, and H.-K. Lo, 2012, "Ultrafast quantum random number generation based on quantum phase fluctuations," Opt. Express 20, 12366.  
Xu, M., J. Huang, W. Liang, C. Zhang, S. Wang, Z. Yin, W. Chen, and Z. Han, 2015, "Adjustable unbalanced quantum random-number generator," Chin. Optic. Lett. 13, 021405.  
Yamazaki, T., and A. Uchida, 2013, "Performance of Random Number Generators Using Noise-Based Superluminescent Diode and Chaos-Based Semiconductor Lasers," IEEE J. Sel. Top. Quantum Electron. 19, 0600309.  
Yan, Q., B. Zhao, Z. Hua, Q. Liao, and H. Yang, 2015, "High-speed quantum-random number generation by continuous measurement of arrival time of photons," Rev. Sci. Instrum. 86, 073113.  
Yang, B., V. Rožić, N. Mentens, and I. Verbauwhede, 2015, “On-the-fly tests for non-ideal true random number generators,” in Proceedings—IEEE International Symposium on Circuits and Systems (IEEE, New York), pp. 2017–2020.  
Yao, A. C., 1982, “Theory and application of trapdoor functions,” in 23rd Annual Symposium on Foundations of Computer Science (SFCS 1982) (IEEE, New York), pp. 80–91.  
Yariv, A., and P. Yeh, 2007, Photonics: Optical Electronics in Modern Communications (Oxford University Press, New York), 6th ed.  
Yu, L. M., M. J. Yang, P. X. Wang, and S. Kawata, 2010, "Note: A sampling method for quantum random bit generation," Rev. Sci. Instrum. 81, 046107.  
Yuen, H. P., and V. W. S. Chan, 1983, "Noise in homodyne and heterodyne detection," Opt. Lett. 8, 177-179.  
Yurke, B., and D. Stoler, 1992, "Bells-inequality experiments using independent-particle sources," Phys. Rev. A 46, 2229-2234.  
Zhao, Y., C.-H. F. Fung, B. Qi, C. Chen, and H.-K. Lo, 2008, "Quantum hacking: Experimental demonstration of time-shift attack against practical quantum-key-distribution systems," Phys. Rev. A 78, 042333.  
Zheng, Y., and T. Matsumoto, 1997, "Breaking real-world implementations of cryptosystems by manipulating their random number generation," in Proceedings of the 1997 Symposium on Cryptography and Information Security, Fukuoka, Japan, pp. 6B1-6.  
Zhou, H., and J. Bruck, 2012, "Efficient generation of random bits from finite state Markov chains," IEEE Trans. Inf. Theory 58, 2490-2506.  
Zhou, H., X. Yuan, and X. Ma, 2015, "Randomness generation based on spontaneous emissions of lasers," Phys. Rev. A 91, 062316.  
Zhu, Y., G. He, and G. Zeng, 2012, "Unbiased Quantum Random Number Generation Based on Squeezed Vacuum State," Int. J. Quantum. Inform. 10, 1250012.

Zhu, Y., Y. Lu, J. Zhu, and G. Zend, 2011, "High speed quantum-random-number generation via measurement on phase noise of laser," Int. J. Quantum. Inform. 09, 1113-1122.  
Ziff, R. M., 1998, "Four-tap shift-register-sequence random-number generators," Comput. Phys. 12, 385.  
Zuckerman, D., 1990, "General weak random sources," in Proceedings of the 31st Annual IEEE Symposium on

Foundations of Computer Science, 1990 (IEEE, New York), Vol. 2, pp. 534-543.  
Zuckerman, D., 1996, "Simulating BPP using a general weak random source," Algorithmica 16, 367-391.  
Zukowski, M., A. Zeilinger, M. A. Horne, and A. K. Ekert, 1993, "Event-ready-detectors" Bell experiment via entanglement swapping," Phys. Rev. Lett. 71, 4287-4290.