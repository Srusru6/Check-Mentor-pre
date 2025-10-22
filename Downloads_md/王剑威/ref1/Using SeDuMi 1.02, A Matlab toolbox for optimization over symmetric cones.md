This article was downloaded by: [Laurentian University]  
On: 20 March 2013, At: 23:11  
Publisher: Taylor & Francis  
Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office: Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](images/ef73367817adff360b2578793b827e56440a551598d16a6fa674cf84fad3ac43.jpg)

# Optimization Methods and Software

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/goms20

# Using SeDuMi 1.02, A Matlab toolbox for optimization over symmetric cones

Jos F. Sturm a

$^{a}$  Research performed at Communications Research Laboratory, Supported by Netherlands Organization for, McMaster University, Hamilton, Canada Version of record first published: 30 Jan 2008.

To cite this article: Jos F. Sturm (1999): Using SeDuMi 1.02, A Matlab toolbox for optimization over symmetric cones, Optimization Methods and Software, 11:1-4, 625-653

To link to this article: http://dx.doi.org/10.1080/10556789908805766

# PLEASE SCROLL DOWN FOR ARTICLE

Full terms and conditions of use: http://www.tandfonline.com/page/terms-and-conditions

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden.

The publisher does not give any warranty express or implied or make any representation that the contents will be complete or accurate or up to date. The accuracy of any instructions, formulae, and drug doses should be independently verified with primary sources. The publisher shall not be liable for any loss, actions, claims, proceedings, demand, or costs or damages whatsoever or howsoever caused arising directly or indirectly in connection with or arising out of the use of this material.

# USING SeDuMi 1.02, A MATLAB* TOOLBOX FOR OPTIMIZATION OVER SYMMETRIC CONES

JOS F. STURM†

Research performed at Communications Research Laboratory, McMaster University, Hamilton, Canada. Supported by Netherlands Organization for Scientific Research (NWO)

(Received 1 August 1998; Revised 1 July 1999; In final form 16 March 1999)

SeDuMi is an add-on for MATLAB, which lets you solve optimization problems with linear, quadratic and semidefiniteness constraints. It is possible to have complex valued data and variables in SeDuMi. Moreover, large scale optimization problems are solved efficiently, by exploiting sparsity. This paper describes how to work with this toolbox.

Keywords: Symmetric cone, semidefinite programming, second order cone programming, self-duality, MATLAB, SeDuMi

SeDuMi stands for Self-Dual-Minimization: it implements the self-dual embedding technique for optimization over self-dual homogeneous cones. The self-dual embedding technique as proposed by Ye, Todd and Mizuno [29], essentially makes it possible to solve certain optimization problems in a single phase, leading either to an optimal solution, or a certificate of infeasibility. Optimization over self-dual homogeneous cones, or more concisely, optimization over symmetric cones, was first studied by Nesterov and Todd [20], and is currently an active area of research.

Semidefinite programming is a special case of optimization over symmetric cones. The popular package SP by Vandenberghe and Boyd

* MATLAB is a registered trademark of The MathWorks, Inc.

† Corresponding Author: Department Quitative Economics, Maastricht University, P.O. Box 616, 6200 MD Maastricht, The Netherlands. E-mail: j.sturm@ke.unimaas.nl; Web: http://www.unimaas.nl/~sturm

[27] is one of the first software tools that was developed for semidefinite programming. Some control theorists use SP indirectly via LMITOOL, by El Ghaoui, Nikoukhah and Delebecque [8], or MRCT, by Dussy and El Ghaoui [6], which are user-friendly front-ends for SP. A more recent and faster solver for semidefinite programming is SDPA, by Fujisawa, Kojima and Nakata [11]. Other solvers for semidefinite programming are CSDP by Borchers [2], SDPHA by Brixius and Potra [3] and SDPT3 by Toh, Todd and Tütuncü [26]. See Mittelmann [18] for a comparison of the performance of various solvers (including SeDuMi) on semidefinite programming problems of the SDPLIB test set.

For optimization over symmetric cones, there are currently two software tools available, viz. SDPPack, by Alizadeh et al. [1], and SeDuMi. Both operate under the MATLAB environment, so that they can easily be used within specific applications. SeDuMi has some features that are not available in SDPPack, namely it

- allows the use of complex valued data,  
- generates Farkas-dual solutions for infeasible problems,  
- takes full advantage of sparsity, leading to significant speed benefits,  
- has a theoretically proven  $O(\sqrt{n} \log(1 / \varepsilon))$  worst-case iteration bound,  
- can import linear programs in MPS format (via a link with LIPSOL [30]), and semidefinite programs in SDPA [11] format.

It is also possible to convert optimization problems from SDPPack [1] format into SeDuMi. Notice that the semidefinite programming solver SDPT3 is also able to handle complex valued data [26]. The issue of exploiting sparsity in semidefinite programming was studied by Fujisawa, Kojima and Nakata [10]. Unlike the approach of [10], SeDuMi uses always the same sparsity exploiting procedure to form the normal equations; this procedure is efficient regardless of the degree of sparsity. See Ross [22] for a comparison between SDPPack and SeDuMi.

The remainder of this document is a step-by-step tutorial for SeDuMi. The on-line help pages serve as a reference to the toolbox. In addition, the Appendix to this document has the details of the calling sequence for the main function, sedumi.

# 1 INTRODUCTION TO SEDUMI

Throughout this document, we assume that SeDuMi is correctly installed, and that you are working under MATLAB Version 5. Entering the

MATLAB command 'help' should produce a list of all installed MATLAB Toolboxes, including the following lines:

```txt
>> help
```

HELP topics:

```txt
matlab/SeDuMi - SeDuMi 1.02 (3AUG1998)
```

```txt
SeDuMi/conversion - Conversion to SeDuMi.
```

For more help on directory/topic, type "help topic".

The command help conversion produces a list of functions for importing data into SeDuMi. This includes an 'umbrella' script, getproblem, which works as follows:

```txt
>> pname = 'truss2'; getproblem, who
```

Your variables are:

```txt
At MATNAME b pname
```

```txt
K PROBDIR c
```

This imports problem 'truss2', and places it in the variables At, b, c and K. To do this, SeDuMi must be able to find the requested problem somewhere on your disk. It can locate sparse SDPA problems, if you have assigned a UNIX environment variable 'SDPLIB' to the directory path where SDPA problems are stored. (SDPLIB and SeDuMi have a different canonical form; if  $y$  is a dual optimal solution calculated by SeDuMi, then  $-y$  is an optimal solution in the SDPLIB canonical form.) If LIPSOL is installed, it uses LIPSOL's function findprob to locate linear programming problems in MPS format. Finally, if SDPPack is installed, and the environment variable SDPPACK points to the SDPPack directory, then SDPPack problems are searched for in the directory 'SDPPACK/problems'.

Typing 'help SeDuMi' produces a list of the functions that you can use to build and solve optimization models over symmetric cones. They are: sedumi, eigK, vec, mat and eyeK. Online help is provided by help sedumi, help eigK, and so on. The following sections give a more detailed explanation of these functions, with some illustrating examples.

# 2 LINEAR PROGRAMMING

With the current version of SeDuMi, it is necessary to formulate your linear programming model in either the primal standard form,

$$
\text {m i n i m i z e} c ^ {\mathrm {T}} x
$$

$$
\text {s u c h} A x = b \tag {1}
$$

$$
x _ {i} \geq 0 \quad \text {f o r} \quad i = 1, 2, \ldots , n,
$$

or the dual standard form,

$$
\underset {\mathbf {T}} {\text {m a x i m i z e}} b ^ {\mathbf {T}} y \tag {2}
$$

$$
\text {s u c h} c _ {i} - a _ {i} ^ {\mathrm {T}} y \geq 0 \quad \text {f o r} \quad i = 1, 2, \dots , n.
$$

Suppose that you want to solve the following linear programming problem:

$$
\text {m i n i m i z e} x _ {1} - x _ {2}
$$

$$
\text {s u c h} 1 0 x _ {1} - 7 x _ {2} \geq 5
$$

$$
x _ {1} + x _ {2} / 2 \leq 3 \tag {3}
$$

$$
x _ {1} \geq 0, \quad x _ {2} \geq 0.
$$

In order to formulate this LP problem in the primal standard form, we have to add slack variables, say  $x_{3}$  and  $x_{4}$ . In MATLAB, we can then enter the  $b$  and  $c$  vectors, and the  $A$  matrix as follows:

$$
\gg c = [ 1; - 1; 0; 0 ];
$$

$$
\gg A = [ 1 0, - 7, - 1, 0; 1, 1 / 2, 0, 1 ];
$$

$$
\gg b = [ 5; 3 ];
$$

We can now solve problem (3) in the primal form (1) by invoking the function sedumi. Remark that MATLAB is case sensitive, and it is therefore essential to write sedumi in lower case.

$$
\gg \text {s e d u m i} (A, b, c)
$$

$$
\text {S e D u M i} \text {b y} \text {J o s F . S t u r m , 1 9 9 8 .}
$$

$$
A l g = 2: x z - c o r r e c t o r, \text {t h e t a} = 0. 2 5 0, \text {b e t a} = 0. 5 0 0
$$

$$
e q s m = 2, o r d e r n = 5, d i m = 5, b l o c k s = 1
$$

$$
i t: \quad c x \quad \text {g a p} \quad d e l t a \quad r a t e \quad t / m a x t \quad f e a s
$$

$$
0: \quad 5. 0 0 E + 0 0 \quad 0. 0 0 0
$$

```txt
1: 7.81E-01 9.79E-01 0.000 0.1959 0.9000 0.77  
2: -5.52E-02 9.40E-02 0.000 0.0959 0.9900 0.93  
*3: -1.25E-01 5.70E-04 0.000 0.0061 0.9990 1.08  
iter seconds digits c*x b*y  
3 0.1 15.1 -1.2500000000e-01 -1.2500000000e-01  
|Ax - b| = 1.8e-15, |x| = 2.9e+00, |y| = 2.8e-01
```

```javascript
ans  $=$  1.958 2.083
```

This shows that the optimal value is  $-0.125$ , as listed under  $c * x$ . The function sedumi returns an optimal solution, which in this case is  $x_1 = 1.9583$  and  $x_2 = 2.0833$ . Notice that  $x$  is indeed feasible for (1), because all its components are nonnegative, and  $Ax = b$ , as can be checked by the commands  $\min(x)$  and  $\text{norm}(Ax - b)$ , respectively. Of course, some round-off errors may occur, as can be seen from the following MATLAB output:

```txt
>>A=sparse(A) ;norm(A\*x-b) ans  $=$  1.7764e-15   
>>norm(A\*24\*x)-24\*b) ans  $=$  0
```

The first quantity is listed as  $|Ax - b| = 1.8e - 15$  in the output of SeDuMi. The second line shows that the reported value of  $|Ax - b|$  does not only contain the residual, but also errors in computing the residual. The meaning of the other parts in the output of SeDuMi is explained in Section 5.

Using dual solutions, it is possible to check also optimality. Namely, if we let  $z := c - A^{\mathrm{T}}y$ , then if  $x$  and  $y$  are feasible to (1) and (2) respectively, we have

$$
0 \leq z ^ {\mathrm {T}} x = c ^ {\mathrm {T}} x - y ^ {\mathrm {T}} A x = c ^ {\mathrm {T}} x - b ^ {\mathrm {T}} y.
$$

Thus, if  $c^{\mathrm{T}}x - b^{\mathrm{T}}y = 0$ , then  $c^{\mathrm{T}}x$  must be minimal, and  $b^{\mathrm{T}}y$  must be maximal, over all feasible solutions. The dual solution  $y$  to (2) is assigned to the second output argument of sedumi, as in

$$
\gg [ x, y ] = \text {s e d u m i} (A, b, c)
$$

In this example, we have  $y_{1} = 0.125$  and  $y_{2} = 0.25$ . Issueing the command

$$
\begin{array}{l} \gg z = c - A ^ {\prime} * y \\ z = \\ \end{array}
$$

0

0

$$
\begin{array}{l} 0. 1 2 5 0 \\ 0. 2 5 0 0 \\ \end{array}
$$

we see that  $z_{i}x_{i} = 0$  for all  $i$ , proving optimality. However, due to some round-off errors,  $c^{\mathrm{T}}x - b^{\mathrm{T}}y$  is positive in this case. The quantity digits = 15.1 in the output of SeDuMi, is defined as follows:

$$
\text {d i g i t s} = \left\{ \begin{array}{l l} - \log_ {1 0} \left(\left(c ^ {\mathrm {T}} x - b ^ {\mathrm {T}} y\right) / \left(\left| b ^ {\mathrm {T}} y \right| + 1 0 ^ {- 1 0}\right)\right) & \text {i f} c ^ {\mathrm {T}} x - b ^ {\mathrm {T}} y > 0 \\ \infty \text {o t h e r w i s e .} \end{array} \right. \tag {4}
$$

As is well known,  $y$  is a subgradient of the optimal value function in terms of changes in  $b$ . If the optimal value function is locally not differentiable in  $b$ , i.e. if there are multiple dual optimal solutions, then it is said to be primal degenerate. SeDuMi usually generates a solution  $y$  in the relative interior of the subgradient set, because it uses a Mehrotra-Ye [17] type termination procedure for linear programs. For a detailed treatment of sensitivity analysis based on such solutions, we refer to Monteiro and Mehrotra [19] and the book of Roos, Terlaky and Vial [21].

For large problems, it is usually not feasible to store  $A$  as a full matrix, due to memory limitations. In this case,  $A$  should be stored in sparse format; type help sparfun for details. Internally, SeDuMi always converts  $A$  to sparse format. The  $b$  and  $c$  vectors can also be in sparse format, if desired.

In the preceding, we defined  $b$  and  $c$  in MATLAB as column vectors, but this is not essential; SeDuMi produces the same output if  $b$  and/or  $c$  are defined as row vectors. Similarly, SeDuMi is not picky about the orientation of  $A$ : it will detect the correct orientation based on the  $b$  and  $c$  vectors (except in the unrealistic case that  $A$  is square). In fact, it is good practice to store  $A$  in such a way that it has more rows than columns, which is the transpose orientation of the  $A$  matrices that we have seen so far. Namely, if  $A$  is stored in sparse format, then it is stored as a set of sparse column vectors. Hence, if there are fewer columns, it will occupy less space.

There is a third output argument of SeDuMi, called info. In our example,

```javascript
>>[x,y,info]  $\equiv$  sedumi(A,b,c);info info  $=$  cpusec:0.0600 iter:3 numerr:0 pinf:0 dinf:0
```

This is a compound output argument, or structure, with a field cpusec for the solution time, iter for the number of iterations, a field numerr which is nonzero in case of numerical problems (1 means premature termination: results are inaccurate, 2 means failure), and two fields, pinf and dinf, for the detected feasibility status of the optimization problem. If pinf = 1, then the primal problem (1) is infeasible, and  $y$  is a Farkas dual solution.

For instance, if we change the  $b$  vector in the preceding example to  $b = [5,0.4]$ , then SeDuMi yields info.pinf = 1,  $b^{\mathrm{T}}y = 0.0955 > 0$ ,  $\max_{i=1,2,3,4} a_i^{\mathrm{T}}y = -0.1866 \leq 0$ . Notice that for any  $x$  with  $Ax = b$ , we have  $y^{\mathrm{T}}Ax = b^{\mathrm{T}}y = 0.0955 > 0$ , whereas  $y^{\mathrm{T}}Ax \leq 0$  for nonnegative  $x$ , because all components of  $A^{\mathrm{T}}y$  are nonpositive. A Farkas dual solution thus provides a certificate of infeasibility. In this example, there appears to be a Farkas dual solution for which all entries of  $A^{\mathrm{T}}y$  are strictly negative. In general though, they are merely nonpositive. For numerical reasons,  $A^{\mathrm{T}}y$  can then contain some small positive components, and in this case we have an approximate Farkas dual solution. Loosely speaking, such

solutions demonstrate that there cannot be any reasonably sized primal feasible solution; see Todd and Ye [25] for details.

Suppose now that we want to solve a problem in the dual standard form (2). In this case,  $y$  with  $b^{\mathrm{T}}y > 0$  and  $A^{\mathrm{T}}y \leq 0$  has the interpretation of an improving direction. Namely, if there exists a feasible solution  $\bar{y}$ , i.e. if  $c - A^{\mathrm{T}}y \geq 0$ , then  $\bar{y} + ty$  is feasible for all  $t \geq 0$ , and  $\lim_{t \to \infty} b^{\mathrm{T}}y = \infty$ . In this case, we say that the problem is unbounded. The other possibility is that there does not exist any feasible solution  $\bar{y}$ , i.e. the problem is infeasible. To distinguish between an infeasible and an unbounded problem, we have to go through a second stage, by solving a feasibility problem:

$$
\gg [ x, y, \text {i n f o} ] = \text {s e d u m i} (A, \text {z e r o s} (\text {l e n g t h} (b), 1), c)
$$

In our previous example, the dual problem is feasible, and the above command yields a feasible solution  $\bar{y}$ . The need for this second stage feasibility problem is typical for interior point methods with the self-dual embedding technique of Ye, Todd and Mizuno [29].

The interpretation of info.dinf is analogous to that of info.pinf. Namely, if info.dinf = 1 then the dual problem (2) is infeasible, and this claim is certified by a Farkas solution  $x$  with

$$
c ^ {T} x <   0, A x = 0, x _ {i} \geq 0 \quad \text {f o r} \quad i = 1, 2, \dots , n.
$$

To distinguish between primal unboundedness and primal infeasibility, we would then solve the feasibility problem

$$
>> [ x, y, \text {i n f o} ] = \text {s e d u m i} (A, b, \text {z e r o s} (\text {l e n g t h} (c), 1))
$$

SeDuMi can also generate Gordan-Stiemke dual solutions. For instance, if we restore the vector  $b$  to  $b^{\mathrm{T}} = [5,3]$ , and solve the feasibility problem  $\mathbf{x} = \text{sedumi}(\mathbf{A}, \mathbf{b}, \text{zeros}(4,1))$ , we obtain a strictly positive vector  $x$ . This is because interior point methods try to find a solution in the relative interior of the solution set. To see what happens if feasible solutions can merely be nonnegative, consider the following example:

```txt
>>b=[5，1/2]；  
>>[x,y,info]=sedumi(A,b,zeros(4,1));  
>>[x -A'*y]
```

```txt
ans  $= 0.5000$  0 1.1875 0 0.0990 0 0.9895   
>>b*y   
ans  $= 1.3878\mathrm{e} - 17$
```

In this example, the primal does not have an interior solution, i.e. it is weakly feasible, and this is demonstrated by a Gordan-Stiemke dual solution  $y$ . Namely,  $0 \neq A^{\mathrm{T}}y \leq 0$ , and  $b^{\mathrm{T}}y = 0$ , which clearly implies that there cannot be any  $x > 0$  such that  $A * x = b$ .

SeDuMi treats the primal and dual in a symmetric way, i.e. it does not favor one over the other. From a modeling point of view however, the primal standard form and the dual standard form are quite different, and it depends on the application which one is more favorable. The primal form has the advantage of explicit equality constraints. In principle, equality constraints can be constructed in the dual form also, simply by means of two inequality constraints, such as  $a_i^{\mathrm{T}}y \leq c_i$  and  $a_i^{\mathrm{T}}y \geq c_i$ . However, this technique is not recommended, since such constraint pairs tend to get a pair of very large primal multipliers  $x_i$ , hence leading to numerical difficulties. It may be better to enforce an equality constraint by eliminating a  $y$  variable. However, the latter technique may destroy the sparsity structure of the  $A$ -matrix, thus leading to longer solution times.

Exactly the same problems arise in modeling a free (i.e. unrestricted in sign) variable in the primal standard form. Splitting such a variable into two, its positive part and its negative part, often results in numerical difficulties. One may also try to eliminate such a variable by removing an equality constraint, but this usually causes an increase in the number of nonzeros in the  $A$ -matrix. A promising alternative is to model all free variables in a quadratic cone. Quadratic cones are discussed in Section 3. To prevent numerical difficulties with this technique, it is desirable to fix a -possibly large -upper bound on the norm of the vector of free variables, which is easily done in a quadratic cone.

# 3 QUADRATIC AND SEMIDEFINITE CONSTRAINTS

In SeDuMi, it is possible to impose quadratic or semidefinite constraints, by restricting variables to a quadratic cone or the cone of positive semidefinite matrices, respectively. Such a restriction then replaces the nonnegativity restriction in linear programming. Thus, instead of requiring  $x \in \mathfrak{R}_+^n$  as in (1), we will now require  $x \in \mathcal{K}$ , where  $\mathcal{K}$  is a so-called symmetric cone. A symmetric cone is a Cartesian product of a nonnegative orthant, quadratic cones and cones of positive semidefinite matrices. The standard primal form for such optimization problems is

$$
\text {m i n i m i z e} c ^ {\mathrm {T}} x
$$

$$
\text {s u c h} A x = b \tag {5}
$$

$$
x \in \mathcal {K}
$$

and the dual standard form is

$$
\text {m a x i m i z e} b ^ {\mathrm {T}} y \tag {6}
$$

$$
\text {s u c h} c - A ^ {\mathrm {T}} y \in \mathcal {K}.
$$

# 3.1 The Quadratic Cone

A quadratic cone is by definition a cone of the form

$$
\mathbf {Q} \text {c o n e :} = \left\{\left(x _ {1}, x _ {2}\right) \in \Re \times \Re^ {N - 1} | x _ {1} \geq \| x _ {2} \| \right\}, \tag {7}
$$

where  $\| \cdot \|$  denotes the Euclidean norm (the function norm in MATLAB). The quadratic cone is also known as the second order cone or Lorentz cone. As an example, consider the following optimization problem:

$$
\min  \left\{y _ {1} + y _ {2} | y _ {1} \geq \| q - P y _ {3} \|, y _ {2} \geq \sqrt {1 + \| y _ {3} \| ^ {2}} \right\}, \tag {8}
$$

where  $P$  is a given matrix, and  $q$  a given vector. The above is a robust least squares problem, see El Ghaoui and Lebret [7]. The decision variables are the scalars  $y_{1}$  and  $y_{2}$ , and the vector  $y_{3}$ . This problem has two quadratic constraints, viz.

$$
\left(y _ {1}, q - P y _ {3}\right) \in \mathrm {Q c o n e}, \quad \left(y _ {2}, \left[ \begin{array}{l} 1 \\ y _ {3} \end{array} \right]\right) \in \mathrm {Q c o n e}. \tag {9}
$$

Given  $P$  and  $q$ , the following MATLAB function (r1s.m) constructs problem (8) in the standard dual form (6). The  $A$  matrix will be in transposed orientation, and is hence denoted as At.

```matlab
1  $\% [At,b,c,K] = rls(P,q)$    
2  $\%$  Creates dual standard form for robust least squares problem "Pu=q".   
3 function  $[\mathsf{At},\mathsf{b},\mathsf{c},\mathsf{K}] = \mathsf{rls}(\mathsf{P},\mathsf{q})$    
4   
5  $[m,n] = size(P)$    
6  $\%$  minimize  $y_{-1} + y_{-2}$    
7 b  $=$  sparse([1; 1; zeros(n,1)]);   
8  $\%$  (y_1,q-Py_3) in Qcone   
9 At  $=$  sparse ([-1, zeros(1, 1+n); ...   
10 zeros(m,2), P]);   
11 c  $= [0;q]$    
12 K.q  $= [1 + m]$    
13  $\%$  (y_2,(1,y_3)) in Qcone   
14 At  $= [At;0,-1,zeros(i,n);\ldots$    
15 zeros(1,2+n);...   
16 zeros(n,2), -eye(n)];   
17 c  $=$  sparse([c; 0;1;zeros(n,1)]);   
18 K.q  $= [\mathrm{K}.q,2 + n]$
```

Notice first that the above function uses sparse data types, in order to save memory. Furthermore, a structure  $\mathbf{K}$  is defined, with a field  $\mathbf{K}. \mathbf{q}$  that lists the dimensions of the quadratic cones. (The 'q' in  $\mathbf{K}. \mathbf{q}$  stands for 'quadratic').) The  $\mathbf{K}$ -structure will be used to tell SeDuMi that the components of  $c - A^{\mathrm{T}}y$  are not restricted to be nonnegative as they would be in linear programming. Instead, the first  $\mathbf{K}. \mathbf{q}(1)$  entries are restricted to a quadratic cone, and the last  $\mathbf{K}. \mathbf{q}(2)$  entries are restricted to another quadratic cone. This is the way in which we model the symmetric cone  $\mathcal{K}$  in (5) and (6), and hence construct the two quadratic constraints in (9).

As a numerical example, we solve a  $4 \times 3$  robust least squares problem with dependent columns in  $P$ . The example is from [7].

```csv
>>P=[314;011;-253;145];q=[0;2;1;3];  
>>[At,b,c,K]=rls(P,q);  
>>[x,y,info]=sedumi(At,b,c,K);  
SeDuMi by Jos F. Sturm, 1998.  
Alg=1:v-corrector,theta=0.250,beta=0.500  
eqs m=5,order n=5,dim=11,blocks=3  
it: cx gap delta rate t/maxt feas  
0: 5.00E+00 0.000  
1:-1.23E+01 1.30E+00 0.000 0.2605 0.9000 -0.18  
2:-5.94E+00 3.34E-01 0.000 0.2568 0.9000 0.54  
3:-3.60E+00 6.14E-02 0.116 0.1838 0.9000 0.86
```

<table><tr><td>4: -3.34E+00</td><td>1.80E-03</td><td>0.000</td><td>0.0293</td><td>0.9900</td><td>1.10</td></tr><tr><td>*5: -3.33E+00</td><td>4.00E-06</td><td>0.000</td><td>0.0022</td><td>0.9990</td><td>1.00</td></tr><tr><td>*6: -3.33E+00</td><td>9.59E-09</td><td>0.000</td><td>0.0024</td><td>0.9990</td><td>1.00</td></tr><tr><td>*7: -3.33E+00</td><td>6.06E-10</td><td>0.153</td><td>0.0632</td><td>0.9900</td><td>1.00</td></tr><tr><td>*8: -3.33E+00</td><td>1.24E-10</td><td>0.000</td><td>0.2037</td><td>0.9000</td><td>1.00</td></tr><tr><td colspan="2">iter seconds digits</td><td colspan="2">c*x</td><td colspan="2">b*y</td></tr><tr><td>8</td><td>0.1</td><td>11.3</td><td>-3.3329085968e+00</td><td colspan="2">-3.3329085968e+00</td></tr><tr><td colspan="6">|Ax-b| = 2.8e-16, |x| = 2.0e+00, |y| = 2.5e+00</td></tr></table>

In the above call to SeDuMi, we see a new input argument, viz. K. This argument makes SeDuMi solve an optimization problem in the form (5)-(6), where the symmetric cone  $\kappa$  is described by the structure  $\kappa$ . Without the fourth input argument (K), SeDuMi would solve a linear programming problem of the form (1)-(2).

To check that (9) is indeed satisfied by the solution  $y$ , it is in principle possible to verify the inequality in definition (7) directly. However, it is more convenient to use the function eigK, which is part of SeDuMi. This function returns the eigenvalues (or spectral values) of a vector with respect to a symmetric cone. A symmetric cone consists of those vectors which have nonnegative eigenvalues, see e.g. the book by Faraut and Korányi [9]. For a quadratic cone (7), there are merely two eigenvalues, viz. given a vector  $(x_{1}, x_{2}) \in \Re \times \Re^{N-1}$ , we have  $\lambda_{1}(x_{1}, x_{2}) = (x_{1} - \|x_{2}\|)/\sqrt{2}$  and  $\lambda_{2}(x_{1}, x_{2}) = (x_{1} + \|x_{2}\|)/\sqrt{2}$ .

We can thus check feasibility and optimality as follows:

<table><tr><td colspan="2">&gt;&gt; [eigK(x, K), eigK(c-At*y, K)]</td></tr><tr><td>ans =</td><td></td></tr><tr><td>0.0000</td><td>-0.0000</td></tr><tr><td>1.4142</td><td>3.2307</td></tr><tr><td>0.0000</td><td>-0.0000</td></tr><tr><td>1.4142</td><td>1.4827</td></tr><tr><td colspan="2">&gt;&gt; x&#x27;*(c-At*y)</td></tr><tr><td>ans =</td><td></td></tr><tr><td colspan="2">1.5807e-11</td></tr></table>

For symmetric cones  $\mathcal{K}$ , it holds that  $x^{\mathrm{T}}z\geq 0$  for all  $x\in \mathcal{K}$  and  $z\in \mathcal{K}$ . Therefore,  $x$  provides an optimality certificate for  $y$  just as in the case of linear programming. The interpretation of Farkas dual solutions extends in the same way. See the survey paper of Luo, Sturm and Zhang [15] for the details. However, a paradoxical phenomenon can occur, viz. that  $x$  and  $y$  are almost feasible, whereas  $c^{\mathrm{T}}x - b^{\mathrm{T}}y$  is considerably negative ( $\| x\|$  and/or  $\| y\|$  must then obviously be very large). SeDuMi will then report an infinite number of digits in accuracy, according to formula (4). This phenomenon was explained by Luo, Sturm and Zhang [14] and Sturm [23].

It is possible that an optimization model has both nonnegativity and quadratic cone constraints. For instance, we may extend the above example with the restriction that  $y_{3}[1] \leq -0.1$ , where  $y_{3}[1]$  denotes the first component in the vector  $y_{3}$ . This restriction can be added to the model as follows:

$$
\begin{array}{l} \gg a 1 = \text {z e r o s} (1, \text {l e n g t h} (\mathrm {y})); a 1 (3) = 1; \\ \gg c = [ - 0. 1; c ]; \quad A t = [ a 1; A t ]; \\ \gg K. l = 1; \\ \gg [ x, y, \text {i n f o} ] = \text {s e d u m i} (A t, b, c, K); \\ \gg e i g K (c - A t * y, K) ^ {\prime} \\ \end{array}
$$

ans =

0.0000 -0.0000 3.2307 -0.0000 1.4904

The field K.1 is the number of nonnegative variables, which in this case is one. (The 'l' in K.1 stands for 'linear'). By convention, the nonnegative variables are always the first components, so that  $\mathcal{K} = \mathfrak{R}_{+} \times \mathrm{Qcone} \times \mathrm{Qcone}$  in our case. As can be seen from the output of eigK, there are 5 eigenvalues for this cone: 1 for each nonnegativity constraint, and 2 for each quadratic constraint. We say that  $\mathcal{K}$  is a symmetric cone of order 5. (SeDuMi reports 'order  $n = 6'$ , because of its internal self-dual reformulation.)

SeDuMi supports an alternative form of the quadratic cone, viz.

$$
\operatorname {R c o n e}: = \left\{\left(x _ {1}, x _ {2}, x _ {3}\right) \in \Re \times \Re \times \Re^ {N - 2} \mid x _ {1} x _ {2} \geq \frac {1}{2} \| x _ {3} \| ^ {2}, x _ {1} + x _ {2} \geq 0 \right\}. \tag {10}
$$

Geometrically, Rcone is simply a rotation of Qcone. The specific form of Rcone is convenient for modeling convex quadratic functions. Namely, by

adding the linear equality constraint  $x_{1} = 1$  to the model, we obtain the restriction

$$
x _ {2} \geq \frac {1}{2} \| x _ {3} \| ^ {2}.
$$

Throughout the model, we can then use  $x_{2}$  as a tight upper bound on  $\| x_{3}\|^{2} / 2$ . Fractions are also conveniently modeled by Rcone constraints. For instance, we may minimize  $1 / x_{1}$  for  $x_{1} > 0$  by solving the model

$$
\min  \left\{x _ {2} \mid x _ {1} x _ {2} \geq 1, x _ {1} + x _ {2} \geq 0 \right\}.
$$

Notice that this problem does not have a solution: the infimum of  $1 / x_{1}$  is zero, for  $x_{1} \to \infty$ .

```erlang
>> clear K;  
>> c = [0, 1, 0]; b = sqrt(2); A = [0, 0, 1]; K.r = 3;  
>> [x,y.info] = sedumi(A,b,c,K);  
>> x(2), x(1)*x(2)
```

```txt
ans  $=$  1.5360e-05 ans  $=$
```

1.0147

You may find that  $x_{2}$  is not yet close enough to zero, and that  $x_{1}$  is not equal to  $\infty$  either. However, the primal solution is feasible, the dual solution is almost feasible, and the duality gap is even negative. This illustrates an error bound difficulty, which is usual for this type of irregular problems. In Section 5, we will see how to obtain a more accurate solution, by setting an optional parameter, pars.eps.

As illustrated by the above example, the field  $\mathbf{K} \cdot \mathbf{r}$  serves to list the dimensions of Rcone constraints, analogously to the definition of Qcone constraints by  $\mathbf{K} \cdot \mathbf{q}$ . (The 'r' in  $\mathbf{K} \cdot \mathbf{r}$  stands for 'rotated quadratic cone').) Setting both  $\mathbf{K} \cdot 1$ ,  $\mathbf{K} \cdot \mathbf{q}$  and  $\mathbf{K} \cdot \mathbf{r}$  fields yields a symmetric cone of the form

$$
\mathcal {K} = \Re_ {+} ^ {\mathrm {K}, 1} \times (\mathrm {Q c o n e} \times \dots \times \mathrm {Q c o n e}) \times (\mathrm {R c o n e} \times \dots \times \mathrm {R c o n e}).
$$

For instance, we can add a bound  $x_1 \leq 10^7$  to the model as follows:

$$
\begin{array}{l} \gg c = [ 0, 0, 1, 0 ]; b = [ \operatorname {s q r t} (2); 1 E 7 ]; A = [ 0, 0, 0, 1; 1, 1, 1, 0, 0 ]; \\ \gg K. 1 = 1; K. r = 3; \\ \gg [ x, y, \text {i n f o} ] = \text {s e d u m i} (A, b, c, K); \\ \end{array}
$$

Some applications of Qcone and Rcone constraints are discussed in Lobo et al. [13].

# 3.2 The Positive Semidefinite Cone

Semidefiniteness constraints are an important class of restrictions that can be modeled with SeDuMi. As an example, consider the following problem:

$$
\begin{array}{l} \min  \left\{\sum_ {i = 1} ^ {m} (m - i) x _ {i i} \left| \sum_ {i = 1} ^ {m - k} x _ {i, i + k} = b _ {k} \quad \text {f o r} \quad k = 0, \dots , m - 1, \right. \right. \\ X \text {i s} \left. \operatorname {p s d} \right\}. \tag {11} \\ \end{array}
$$

Here,  $X$  is an  $m \times m$  symmetric matrix, and  $x_{ij}$  denotes the entry on row  $i$  and column  $j$ . The length  $m$  vector  $b$  is given. The abbreviation 'psd' stands for 'positive semidefinite'. The above optimization problem yields a minimal phase spectral factorization of an autocorrelation vector  $b$ , see Davidson, Luo and Sturm [4]. Problem (11) is stated in terms of an  $m \times m$  symmetric matrix of decision variables, whereas SeDuMi works with a vector of decision variables, as in (5)-(6). This small issue is resolved by using the well known technique of vectorization. Vectorization is implemented by the functions vec and mat, which are part of SeDuMi. The function vec(X) creates a long vector, by stacking the columns of the matrix  $X$ , as in:

$$
\gg x = \operatorname {v e c} ([ 1, 5, - 3; 5, 2, - 9; - 3, - 9, 4 ])
$$

$$
x =
$$

$$
\begin{array}{c c c c c c c c c} 1 & 5 & - 3 & 5 & 2 & - 9 & - 3 & - 9 & 4 \end{array}
$$

The inverse of vec is mat. Thus, if  $x$  is a vector of length  $n^2$ , then  $\mathbf{mat}(x)$  constructs an  $n \times n$  matrix, and fills it with the entries of the vector  $x$ ,

starting at the first column.

```txt
>>mat(x) ans  $=$  1 5 -3
```

The following MATLAB function produces a standard primal form for problem (11).

```matlab
1  $\%$  [At,b,c,K]  $=$  specfac(b)   
2  $\%$  Creates primal standard form for minimal phase spectral factorization.   
3 function [At,b,c,K]  $=$  specfac(b)   
4   
5 m  $=$  length(b);   
6  $\%$  - minimize sum (m-i)\*X(i,i)   
7 c  $=$  vec(spdiags((m-1:-1:0),0,m,m));   
8  $\%$  - Let e be all-1, and allocate space for the A-matrix -   
9 e  $=$  ones(m,1);   
10 At  $=$  sparse([],[],[m2,m,m\*(m+1)/2);   
11  $\%$  -sum(diag(X,k))  $=$  b(k)   
12 for k = 1:m   
13 At(:,k)  $=$  vec(spdiags(e,k-1,m,m));   
14 end   
15 K.s  $=$  [m];
```

The field  $\mathbf{K.s} = [m]$  tells SeDuMi that we want the  $m\times m$  matrix  $\mathbf{mat}(\mathbf{x})$  to be symmetric positive semidefinite. (The 's' in K.s stands for 'semidefinite'). We can now solve problem (11) as follows:

```csv
>> b = [2; 0.2; -0.3];  
>> [At,b,c,K] = specfac(b);  
>> [x,y,info] = sedumi(At,b,c,K);  
SeDuMi by Jos F. Sturm, 1998.  
Alg = 1: v-corrector, theta = 0.250, beta = 0.500  
eqs m = 3, order n = 4, dim = 10, blocks = 2  
it: cx gap delta rate t/maxt feas  
0: 4.00E+00 0.000  
1: 8.14E+00 1.40E+00 0.000 0.3497 0.9000 0.32  
2: 2.29E+00 4.68E-01 0.000 0.3346 0.9000 0.59  
3: 3.42E-01 1.12E-01 0.337 0.2391 0.9000 0.84  
4: 1.26E-01 1.92E-03 0.000 0.0172 0.9900 1.24
```

* 5 : 1.23E-01 3.97E-06 0.000 0.0021 0.9990 1.00

* 6 : 1.23E-01 8.88E-10 0.000 0.0002 0.9990 1.00

* 7 : 1.23E-01 2.27E-12 0.000 0.0026 0.9900 1.00

iter seconds digits c\*x b\*y

7 0.1 10.7 1.2273256502e-01 1.2273256502e-01

$|Ax - b| = 0.0e + 00, |x| = 2.0e + 00, |y| = 7.6e - 01$

To check positive semidefiniteness, we can either use the function eig that is part of MATLAB, or the function eigK, which comes with SeDuMi.

$$
\gg [ \operatorname {e i g} (\operatorname {m a t} (x)), \operatorname {e i g K} (x, K) ]
$$

$$
\text {a n s} =
$$

$$
\begin{array}{c c} 0. 0 0 0 0 & 0. 0 0 0 0 \end{array}
$$

$$
\begin{array}{c c} 0. 0 0 0 0 & 0. 0 0 0 0 \end{array}
$$

$$
\begin{array}{c c} 2. 0 0 0 0 & 2. 0 0 0 0 \end{array}
$$

The use of eigK is more convenient, especially if there are multiple semidefiniteness constraints, or if there are also nonnegativity or quadratic cone constraints. SeDuMi will always produce symmetric matrix variables, i.e.  $\mathbf{mat}(\mathbf{x})$  is symmetric. Do not add symmetry constraints explicitly, as in  $x_{ij} - x_{ji} = 0$ . At best, such constraints will be removed by SeDuMi from the  $A$  matrix.

However, the dual solution  $c - A^{\mathrm{T}}y$  need not be symmetric, as can be seen in the numerical example that we are dealing with:

$$
\gg \operatorname {m a t} (c - A t * y)
$$

$$
\text {a n s} =
$$

$$
2. 0 7 2 7 - 0. 3 1 3 0 \quad 0. 6 8 4 9
$$

$$
0 \quad 1. 0 7 2 7 \quad - 0. 3 1 3 0
$$

$$
0 \quad 0 \quad 0. 0 7 2 7
$$

In this case, the dual solution is upper triangular, because  $\mathbf{mat}(\mathbf{c})$  is diagonal, and  $\mathbf{mat}(\mathbf{At}(:,\mathbf{k}))$  is upper triangular for all  $k = 1,2,\ldots,m$ . Letting  $Z = \mathbf{mat}(c - A^{\mathrm{T}}y)$ , SeDuMi restricts the symmetric part of  $Z$ , which is  $(Z + Z^{\mathrm{T}}) / 2$ , to be positive semidefinite. The function eigK yields

the eigenvalues of the symmetric part. Thus,

>>eigK(c-At\*y,K) ans  $=$  1.0583 2.1597 -0.0000

produces the same result as

$$
>> Z = \operatorname {m a t} (c - A t * y); e i g \left(Z + Z ^ {\prime}\right) / 2
$$

Notice that problem (11) is equivalent to

$$
\min  \left\{\sum_ {i = 1} ^ {m} (m - i) x _ {i i} \left| \sum_ {i = 1} ^ {m - k} \frac {x _ {i , i + k} + x _ {i + k , i}}{2} = b _ {k} \quad \text {f o r} \quad k = 0, \dots , \right. \right.
$$

$$
m - 1, \quad X \text {i s} \left. \operatorname {p s d} \right\}. \tag {12}
$$

Namely,  $x_{i,i+k} = (x_{i,i+k} + x_{i+k,i}) / 2$ , because  $X$  is symmetric. Thus, we may change the  $A$  matrix as follows:

$$
\gg \text {f o r} k = 1: \text {s i z e} (A t, 2), A k = \operatorname {m a t} (A t (:, k)); A t (:, k) = \operatorname {v e c} (A k + A k ^ {\prime}) / 2; \text {e n d}
$$

The solutions  $x$  and  $y$ , as produced by SeDuMi, will be exactly the same. However, since the constraints in the  $A$  matrix have been symmetrized, we find that  $\mathbf{mat}(\mathbf{c} - \mathbf{At} * \mathbf{y})$  is now symmetric; it is the matrix  $(Z + Z') / 2$ .

For SeDuMi, it does not make any difference whether the constraints in  $A$  and the objective  $c$  are symmetrized or not. However, when modeling in the primal standard form, you will probably find it more natural to work with upper or lower triangular matrices in  $A$  and  $c$ ; your model will also use less memory like this. On the other hand, symmetric matrices are more natural when modeling in the dual form.

There can be multiple positive semidefiniteness constraints, in which case K.s lists the orders of the respective matrices. This is analogous to the definition of multiple quadratic constraints in K.q and/or K.r. The positive semidefinite variables are always the last components of  $x$  and  $c - A^{\mathrm{T}}y$ , i.e.

$$
\begin{array}{l} \mathcal {K} = \Re_ {+} ^ {\mathrm {K}. 1} \times (\mathrm {Q c o n e} \times \dots \times \mathrm {Q c o n e}) \times (\mathrm {R c o n e} \times \dots \times \mathrm {R c o n e}) \\ \times (\text {S c o n e} \times \dots \times \text {S c o n e}), \\ \end{array}
$$

where Scone denotes the cone of positive semidefinite matrices. It is easy to remember the above arrangement, by noting the alphabetical order of 'l', 'q', 'r' and 's'.

# 4 COMPLEX VALUES

In some application areas, such as signal processing, optimization problems may involve complex valued data. An example is the Toeplitz Hermitian covariance estimation problem, which is discussed in Wu, Luo and Wong [28]. Other structured covariance estimation problems, such as discussed in Deng and Hu [5], can be treated similarly. Given a Hermitian matrix  $P$ , the goal is to find a Hermitian positive definite matrix  $Z$  with a Toeplitz structure, such that  $\| P - Z \|_F$  is minimal. Thus, the optimization problem is:

$$
\text {m i n i m i z e} \sum_ {i = 1} ^ {m} \left(\left(z _ {i i} - p _ {i i}\right) ^ {2} + 2 \sum_ {j = i + 1} ^ {m} \left| z _ {i j} - p _ {i j} \right| ^ {2}\right)
$$

such that  $Z$  is Toeplitz, i.e.  $z_{i,j} = z_{i + 1,j + 1}$  for all  $i,j = 1,2,\ldots$ ,

$$
m - 1, \quad Z \text {i s} \tag {13}
$$

If the matrix  $P$  has complex entries, then we will usually also see complex entries in the optimal solution  $Z$ . Notice that the Toeplitz property is better modeled in the dual form, than in the primal form. In fact, mat (At * y) in (11) is an upper triangular real Toeplitz matrix, and in (12), it is a symmetric Toeplitz matrix. The MATLAB formulation of (13) therefore resembles the MATLAB formulation of (11).

```matlab
1  $\%$  [At,b,c,K]  $=$  toepest(P)   
2  $\%$  Creates dual standard form for Toeplitz-covariance estimation   
3 function [At,b,c,K]  $=$  toepest(P)   
4   
5  $\mathbf{m} = \mathbf{size}(\mathbf{P},\mathbf{l})$    
6  $\%$  - maximize y(m+1)   
7 b  $=$  [sparse(m,1); 1];   
8  $\%$  - Let e be all-1,and allocate space for the A-matrix   
9 e  $=$  ones(m,1);   
10 K.q  $= [1 + m^{*}(m + 1) / 2]$    
11 At  $=$  sparse([, [], [], K.q(1)  $+$  m'2,m+1,1+2*m'2);   
12  $\%$  constraints   
13  $\%$  -y(m+1)>=norm vec(P)-sum(y_i*i*Ti） (Qcone)   
14  $\%$  sum(y_i*i*Ti) is psd (Scone)   
15  $\%$    
16 At(:,1)  $=$  [sparse(2:(m+1),1,1,K.q(1),1); -vec(spyee(m));
```

```matlab
17  $c = [0;\mathrm{diag}(P)]$    
18 firstk  $\equiv$  m+2;   
19 for  $\mathbf{k} = 1$  ..(m-1)   
20 lastk  $\equiv$  firstk  $^+$  m-k-1;   
21 Ti  $\equiv$  spdiags(e,k,m,m);   
22 At(:,k+1)  $=$  [sqrt(2)\*sparse(firstk:lastk,1,1,K.q(1),1);  $-2^{*}$  vec(Ti)];   
23 c=[c;sqrt(2)\*diag(P,k)];   
24 firstk  $\equiv$  lastk + 1;   
25 end   
26 At(:,m+1)  $=$  [1;sparse(K.q(1)+m2-1,1)]; % "objective"variable y(m+1)   
27 c=[c;zeros(m^2,1)]; % all-0 in the psd-part   
28 K.s=[m];   
29  $\%$  -y(2:m) complex, y(1) and y(m+1) real -   
30 K.ycomplex  $= 2:\mathrm{m};$
```

We have modeled the objective function by means of an artificial variable,  $y_{m+1}$ , and  $y_{m+1}^2$  is bounded from below by the original quadratic objective function, using a  $1 + m(m+1)/2$ -dimensional quadratic cone. The Toeplitz matrix is modeled as

$$
y _ {1} I + 2 \sum_ {i = 1} ^ {m - 1} y _ {i + 1} T _ {i}, \tag {14}
$$

where  $T_{i}$  is all-1 along the  $k$ -th upper diagonal, and zero everywhere else. Recall from problem (11) in Section 3.2, that in the real case, SeDuMi restricts the symmetric part of  $\mathfrak{mat}(c - A^{\mathrm{T}}y)$  to be positive semidefinite. In the complex case, SeDuMi restricts the Hermitian part, i.e.  $\mathfrak{mat}(c - A^{\mathrm{T}}y) + \mathfrak{mat}(c - A^{\mathrm{T}}y)'$ , to be positive semidefinite. Letting  $Z$  denote the Hermitian part of (14), we have

$$
Z = y _ {1} I + \sum_ {i = 1} ^ {m - 1} (y _ {i + 1} T _ {i} + \bar {y} _ {i + 1} T _ {i} ^ {\mathrm {T}}),
$$

where  $\bar{y}_{i+1}$  denotes the complex conjugate of  $y_{i+1}$ . Thus, we have indeed modeled  $Z$  as a Hermitian Toeplitz matrix, and SeDuMi further restricts it to be positive semidefinite, because of the field K.s. Furthermore, we tell SeDuMi to allow complex values for  $y_2, y_3, \ldots, y_m$ , by setting K.ycomplex = 2:m. Remark that unlike K.l, K.q, K.r and K.s, the field K.ycomplex is not involved in the definition of the symmetric cone  $\mathcal{K}$  in (5)-(6).

The following lines show how to solve problem (13), for a particular  $3 \times 3$  Hermitian matrix  $P$ , which is neither Toeplitz, nor positive semidefinite.

```txt
>>i=sqrt(-1);  
>>P=[4, 1+2*i, 3-i;1-2*i, 3.5, 0.8+2.3*i;3+i, 0.8-2.3*i, 4]
```

P =

```txt
4.0000 1.0000 + 2.0000i 3.0000 - 1.0000i  
1.0000 - 2.0000i 3.5000 0.8000 + 2.3000i  
3.0000 + 1.0000i 0.8000 - 2.3000i 4.0000
```

```matlab
>> [At, b, c, K] = toepest(P);  
>> [x, y, info] = sedumi(At, b, c, K);  
>> z = c - At*y; Z = mat(z(K.q+1:length(z))); Z = (Z + Z') / 2
```

Z=

```txt
4.2827 0.8079 + 1.7342i 2.5574 - 0.7938i  
0.8079 - 1.7342i 4.2827 0.8079 + 1.7342i  
2.5574 + 0.7938i 0.8079 - 1.7342i 4.2827
```

```txt
>>eigK(z,K),
```

ans =

```csv
-0.0000 2.0517 0.0000 7.2810 5.5670
```

We have found the optimal positive semidefinite Toeplitz matrix  $Z$ , which has eigenvalues 0, 7.281 and 5.567. Checking the objective values reveals a new phenomenon:

```txt
>> [c' * x; b' * y]
```

```txt
ans
```

```txt
-1.4508 - 0.2428i
```

```txt
-1.4508
```

The value of  $c^{\mathrm{H}}x$ , where  $^\mathrm{H}$  means complex conjugate transpose, may no longer be real, and the same is true for  $b^{\mathrm{H}}y$  in general. Obviously, we cannot minimize or maximize complex valued functions. Instead, SeDuMi minimizes  $\operatorname{Re} c^{\mathrm{H}}x$  in the primal, and maximizes  $\operatorname{Re} b^{\mathrm{T}}y$  in the dual. Here, Re stands for real part. In the sequel, we will also use the notation Im, to denote the imaginary part.

If we make K.ycomplex  $= \left\lbrack  \right\rbrack$  ,then all dual multipliers  $y$  are restricted to be real.

```txt
>>K.ycomplex  $= \left[\right]$  .   
[x2,y2,info2]=sedumi(At,b,c,K);   
[c'*x2；b'*y2]
```

$$
\text {a n s} =
$$

$$
\begin{array}{l} - 4. 5 5 9 2 - 0. 3 8 1 6 i \\ - 4. 5 5 9 2 \\ \end{array}
$$

Clearly, by restricting  $y$  to be real, the dual optimal value  $\operatorname{Re} b^{\mathrm{H}}y = -y_{m+1}$  gets worse. Apparently, something has changed in the primal problem as well, since the primal optimal value has improved from  $-1.4508$  to  $-4.5592$ . The difference is in the  $Ax = b'$  restriction, as the following lines show:

$$
\begin{array}{l l} \gg [ b - A t ^ {\prime} * x b - A t ^ {\prime} * x 2 ] \\ \text {a n s} = \\ 0. 0 0 0 0 - 0. 0 0 0 0 \\ 0. 0 0 0 0 + 0. 0 0 0 0 i - 0. 0 0 0 0 + 1. 8 8 6 3 i \\ - 0. 0 0 0 0 - 0. 0 0 0 0 - 0. 4 3 8 7 i \\ 0 \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

The restriction  $Ax = b$  is interpreted by SeDuMi as

$$
\left\{ \begin{array}{l} a _ {i} ^ {\mathrm {H}} x = b _ {i} \text {i f} \operatorname {I m} b _ {i} \neq 0 \text {o r} i \in \mathrm {K}. \mathrm {y c o m p l e x} \\ \operatorname {R e} a _ {i} ^ {\mathrm {H}} x = b _ {i} \quad \text {o t h e r w i s e .} \end{array} \right. \tag {15}
$$

By making K.ycomplex = [], we therefore removed the restrictions on Im  $Ax$ . Complex  $y$ -variables in the dual form correspond with complex equality constraints in the primal form. In the preceding, we have defined the complex  $y$ -variables explicitly, by means of K.ycomplex. They can also be defined implicitly, by specifying a nonzero imaginary part in the corresponding  $b$ -components. However, to avoid confusion, it is recommended that you always specify the complex  $y$ -variables (or equivalently, complex primal equality constraints) in K.ycomplex, even when  $b$  has nonzero imaginary components.

For sensitivity analysis, it is interesting to note that  $\operatorname{Re}(\Delta c)^{\mathrm{H}}x$  is a supergradient for the optimal value function, under perturbations of the form  $c + t\Delta c$ , whereas  $\operatorname{Re}(\Delta b)^{\mathrm{H}}y$  is a subgradient of the optimal value function under perturbation of  $b$ . For a discussion of sensitivity analysis in (real symmetric) semidefinite programming, see Goldfarb and Scheinberg [12].

# 5 OPTIONAL SETTINGS

By default, SeDuMi fills your terminal screen with some output concerning its iterative progress. This can be an annoying feature, in particular if SeDuMi is merely used as a subroutine within a larger program. To suppress the on-screen output of SeDuMi, it suffices to set an optional parameter, pars.fid, to zero.

```txt
>> load truss1  
>> pars.fid = 0;  
>> [x,y,info] = sedumi(At,b,c,K, pars);
```

The structure pars is not only used for suppressing iterative output of SeDuMi. It can contain a number of optional fields, which we will discuss in this section.

The abbreviation 'fid' in pars.fid stands for 'file identifier': the output of SeDuMi will be sent to the file whose file identifier is pars.fid. The file identifier for the null-device is 0, which is useful for suppressing output, and for the terminal screen it is 1. Output can also be redirected to a file, e.g.

```txt
>> pars.fid = fopen('truss1.out', 'w');  
>> [x, y, info] =SEDumi(At, b, c, K, pars);  
>> fclose pars.fid); pars.fid = 1;
```

With the above lines, the output is redirected to the file 'truss1.out', as can be checked with the command dbtype truss1.out.

SeDuMi uses a variant of the primal-dual interior point method, which is known as the centering-predictor-corrector method [23]. There are 3 variants of the centering-predictor-corrector method implemented, which can be selected with the field pars.alg. With pars.alg = 0, you select a longest-step algorithm, without any second order corrector. To enhance the algorithm with a second order corrector, you can either set pars.alg = 1 or pars.alg = 2. With pars.alg = 1, the second order corrector is derived by linearization of the so-called  $v$ -values whereas pars.alg = 2 uses linearization of the squared  $v$ -values, which is also known as  $xz$ -linearization. For linear programming,  $xz$ -linearization results in the well-known Mehrotra's corrector [16]. In all three variants, the centering step is determined by the central region parameter, pars.theta. This parameter can take any value in (0,1]. At one extreme, pars.theta = 1 results

in path-following, which typically involves relatively short step lengths. Setting pars.theta to a smaller value, such as 1/4, makes the algorithm work in the neighborhood of a full dimensional central region, and this typically allows for larger step lengths, see Sturm and Zhang [24]. The size of the neighborhood is controlled by the parameter pars.beta, which can be assigned any value in (0,1). In the output of SeDuMi on the terminal screen, there is a column labeled 'delta', which lists the actual distance to the central region in each iteration. The step length will always be such that this is at most pars.beta. The ratio of the actual step length and the maximal steplength to the boundary of the cone  $\kappa$  is listed in the column labeled 't/maxt'. For some iterations, an asterisk ('*') appears in front of the output line. At these iterations, the residual vector of the self-dual model has been recomputed (to avoid accumulation of numerical errors).

For research purposes, SeDuMi can produce a plot of the iterative  $v$ -values. This feature is activated by setting pars.vplot = 1. For problem truss1, this results in the plots of Figure 1. For each iteration, the first plot shows all the  $v$ -values, divided by the mean of the  $v$ -vector in that iteration. It also gives a horizontal line at value 1, representing the central path, and a horizontal line at the central region threshold, pars. theta = 1/4. Any  $v$ -values below this threshold will be corrected by the centering component in the succeeding iteration. The second plot shows the rate of linear reduction, which is simply

$$
\begin{array}{c} \text {d u a l i t y g a p i n i t e r a t i o n k} \\ \hline \text {d u a l i t y g a p i n i t e r a t i o n k - 1} \end{array} .
$$

The rate of linear reduction is also listed in the column 'rate' in the on-screen output of SeDuMi, and the iterative duality gap is listed under 'gap'. This is the duality gap in an artificial self-dual model, in which your original model is embedded by SeDuMi, using the technique of Ye, Todd and Mizuno [29]. The self-dual model gives rise to a feasibility indicator, listed in the column 'feas'. Ideally, the indicator converges to  $+1$  for feasible problems, and to  $-1$  for (primal and/or dual) infeasible problems.

Termination control is provided by the fields maxiter, numtol and eps in the pars structure. SeDuMi will terminate successfully if it finds a solution that violates feasibility and optimality requirements by no more than pars.eps. Unfortunately, SeDuMi often has to terminate prematurely, due to numerical problems. The parameter pars.namtol specifies the size of numerical errors that are tolerated, without termination. The

![](images/67961e613f1370957a8df4481a635eccd0b92c9fbbe50d37bd7fd4e599499bc6.jpg)

![](images/d7c182156e6b4621cbb38cb67a32a692dc2c99b534084aaa674f8336a537fdf7.jpg)  
FIGURE 1 Plot produced by setting pars.vplot = 1.

parameter pars.maxiter allows you to set a maximum on the number of iterations. By default, pars.eps = 1E - 9, pars.numtol = 5E - 4, and pars.maxiter = 150. A possible experiment with these parameters is to set pars.eps = 0 in the example of minimizing  $\frac{1}{x_1}$ , which was discussed in Section 3.1.

# Appendix: Calling Sequence

The primal canonical form for solving optimization problems with SeDuMi is

$$
\min  \{c ^ {\mathrm {T}} x | A x = b, x \in \mathcal {K} \},
$$

and the dual canonical form is

$$
\max  \{b ^ {\mathrm {T}} y | c - A ^ {\mathrm {T}} y \in \mathcal {K} \}.
$$

The general calling sequence for solving the above primal-dual pair is

$$
[ x, y, \text {i n f o} ] = \text {s e d u m i (A , b , c , K , p a r s)}
$$

Here,  $\mathbf{K}$  is a MATLAB structure to define the symmetric cone  $\mathcal{K}$ ; it consists of the following (optional) fields:

K.1 The number of nonnegativity constraints

K.q A list of dimensions of quadratic cone constraints

K.  $r$  A list of dimensions of rotated quadratic cone constraints

K.sA list of orders of positive semidefiniteness constraints

K.ycomplex This field is not related to  $\kappa$ . It lists the components of the  $y$ -variables that are complex valued. Equivalently, it lists the primal equality constraints  $(Ax)_i = b_i$  that have to be satisfied not only in their real parts, but also in their imaginary parts.

The structure  $\mathbf{K}$  defines  $\kappa$  to be

$$
\begin{array}{l} \mathcal {K} = \mathfrak {R} _ {+} ^ {\mathrm {K . l}} \times (\text {Q c o n e} \times \dots \times \text {Q c o n e}) \times (\text {R c o n e} \times \dots \times \text {R c o n e}) \\ \times (\text {S c o n e} \times \dots \times \text {S c o n e}), \\ \end{array}
$$

In total, the number of Qcone (Rcone, Scone) components is length (K.q) (length (K.r), length (K.s)). The  $i$ th Qcone is

$$
\operatorname {Q c o n e} _ {i} = \left\{\left(x _ {1}, x _ {2}\right) \in \Re \times \mathcal {C} ^ {\mathrm {K . q [ i ] - 1}} \mid x _ {1} \geq \| x _ {2} \| \right\},
$$

where  $\mathcal{C}^n$  denotes the space of complex  $n$ -tuples. The  $j$ th Rcone is

$$
\begin{array}{l} \operatorname {R c o n e} _ {j} = \left\{(x _ {1}, x _ {2}, x _ {3}) \in \Re \times \Re \times \mathcal {C} ^ {\mathrm {K . r [ j ] - 2}} \Bigg | x _ {1} x _ {2} \geq \frac {1}{2} \| x _ {3} \| ^ {2}, \right. \\ \left. x _ {1} + x _ {2} \geq 0 \right\}, \\ \end{array}
$$

and the  $k$ th Scone is

$\mathbf{Scone}_k = \left\{x\in \mathcal{C}^{\mathbf{K},\mathbf{s}[\mathbf{k}]^2}|\mathbf{mat}(\mathbf{x})\text{is Hermitian positive semidefinite}\right\} ,$

for primal components. For dual components  $z = c - A^{\mathrm{T}}y$ , we use a slightly milder definition of Scone, viz.

$\mathbf{Scone}_k = \left\{z\in \mathcal{C}^{\mathbf{K},s[\mathbf{k}]^2}\mid \mathbf{mat}(\mathbf{z}) + \mathbf{mat}(\mathbf{z})'\text{is positive semidefinite}\right\} .$

The length of the vector  $c$  should be

$$
\operatorname {l e n g t h} (c) = K. 1 + \operatorname {s u m} (K. q) + \operatorname {s u m} (K. r) + \operatorname {s u m} (K. s. ^ {\prime} 2)
$$

If the data  $(A, b, c)$  is real valued, then  $x$  and  $y$  will also be real valued.

The parameter pars is a MATLAB structure, consisting of the following (optional) fields:

pars.fid By default, pars.fid = 1, which tells SeDuMi to produce iterative statistics on the screen. If pars.fid = 0, then SeDuMi runs quietly, i.e. no screen output. In general, output is written to the file or device that is identified by the file handle pars.fid. A file handle is assigned to a file by the MATLAB function fopen, as in

$$
\operatorname {p a r s . f i d} = \text {f o p e n} ^ {\prime} (\text {t r u s s 1 . o u t} ^ {\prime}, ^ {\prime} w ^ {\prime}).
$$

pars.alg By default, pars.alg = 1 for nonlinear cones, and pars.alg = 2 if the problem is completely linear. If pars.alg = 0, then a first-order algorithm is used, which is not recommendable. If pars.alg = 1, then SeDuMi uses the centering-predictor-corrector algorithm with  $v$ -linearization. If pars.alg = 2 then  $xz$ -linearization is used in the corrector, similar to Mehrotra's algorithm. All 3 algorithms are special instances of the generic wide-region algorithm, as discussed in Chapter 7 of Sturm [23].

pars theta, pars.beta By default, pars.theta = 0.25 and pars. beta = 0.5. These are the wide region and neighborhood parameters. Valid choices are  $0 < \theta <= 1$  and  $0 < \beta < 1$ .

pars.vplot If this field is 1, then SeDuMi produces a fancy  $v$ -plot, for research purposes. Default: vplot = 0.

pars.eps The desired accuracy.

pars.namtol Tolerance to observed numerical problems.

pars.maxiter Maximum number of iterations, before termination.

The output parameter info is a MATLAB structure, with the following fields:

info.pinf and info.dinf The feasibility status of the primal-dual problem pair, as detected by SeDuMi. There are three cases:

1.  $\mathsf{pinf} = \mathsf{dinf} = 0$  Then  $x$  and  $y$  are (approximate) optimal solutions, i.e.  $Ax = b$ ,  $x \in \mathcal{K}$ ,  $c - A^{\mathrm{T}}y \in \mathcal{K}$ , and  $c^{\mathrm{T}}x \leq b^{\mathrm{T}}y$  (approximately).  
2.  $\mathsf{pinf} = 1$  Primal is infeasible, i.e.  $\{x\in \mathcal{K}|Ax = b\} = \emptyset$ . Then  $y$  is a Farkas-type solution, i.e.  $b^{\mathrm{T}}y > 0$  and  $-A^{\mathrm{T}}y\in \mathcal{K}$  
3.  $\mathrm{dinf} = 1$  Dual is infeasible, i.e.  $\{y|c - A^{\mathrm{T}}y\in \mathcal{K}\} = \emptyset$ . Then  $x$  is a Farkas-type solution, i.e.  $c^{\mathrm{T}}x < 0$ ,  $Ax = 0$  and  $x\in \mathcal{K}$ .

info.numerr A positive value of info.numerr means that SeDuMi-terminated without achieving the desired accuracy, because of

numerical problems. If info[numerr = 1 then the results are merely inaccurate: the solution still has two or more digits of accuracy. If info[numerr = 2 then SeDuMi failed completely.

# Acknowledgments

I thank T. Terlaky for encouraging me to write this manual, and for pointing out a bug in the first public release of SeDuMi. T. N. Davidson, V. Prodanovic and A. Ross helped to improve the software, by providing bug reports and suggestions. Two anonymous referees have contributed in improving this document.

# References

[1] Alizadeh, F., Haeberly, J. A., Nayakkankuppann, M. V., Overton, M. and Schmieta, S. (1997). SDP-Pack user's guide. New York University, New York, USA.  
[2] Borchers, B. (1997). CSDP, a C library for semidefinite programming. Technical report, New Mexico Tech Mathematics Faculty, USA.  
[3] Brixius, N. and Potra, F. A. (1998). Sdpha: A MATLAB implementation of homogeneous interior-point algorithms for semidefinite programming. Technical report, Department of Computer Science, University of Iowa, Iowa City, Iowa, USA.  
[4] Davidson, T. N., Luo, Z.-Q. and Sturm, J. F. (1998). A (primal form of the) positive real lemma for FIR systems. Technical report, Communications Research Laboratory, McMaster University, Hamilton, Canada. To appear.  
[5] Deng, S. and Hu, H. (1996). Computable error bounds for semidefinite programming. Technical report, Department of Mathematical Sciences, Northern Illinois University, DeKalb, Illinois, USA.  
[6] Dussy, S. and El Ghaoui, L. (1997). Multiobjective robust control toolbox for LMI-based control. Technical report, Laboratoire de Mathématiques Appliquées, ENSTA, Paris, France.  
[7] El Ghaoui, L. and Lebret, H. (1997). Robust solutions to least-squares problems with uncertain data, SIAM Journal on Matrix Analysis and Applications, 18(4), 1035-1064.  
[8] El Ghaoui, L., Nikoukhah, R. and Delebecque, F. (1995). LMITOOL: A front-end for LMI optimization, user's guide. Laboratoire de Mathématiques Appliquées, ENSTA, Paris, France.  
[9] Faraut, J. and Korányi, A. (1994). Analysis on Symmetric Cones, Oxford Mathematical Monographs. Oxford University Press, New York.  
[10] Fujisawa, K., Kojima, M. and Nakata, K. (1997). Exploiting sparsity in primal-dual interior-point methods for semidefinite programming, Mathematical Programming, 79, 235-253.  
[11] Fujisawa, K., Kojima, M. and Nakata, K. (1998). SDPA (semidefinite programming algorithm) user's manual — version 4.10. Technical report, Dept. of Information Sciences, Tokyo Institute of Technology, 2-12-1 Oh-Okayama, Meguro-ku, Tokyo 152, Japan.  
[12] Goldfarb, D. and Scheinberg, K. (1997). On parametric semidefinite programming. Technical report, Columbia University, Department of IEOR, New York, USA.  
[13] Lobo, M. S., Vandenberghe, L., Boyd, S. and Lebret, H. (1997). Applications of second-order cone programming. Technical report, Information Systems Lab, Stanford University. To appear in Linear Algebra and Applications.

[14] Luo, Z.-Q., Sturm, J. F. and Zhang, S. (1996). Duality and self-duality for conic convex programming. Technical Report 9620/A, Econometric Institute, Erasmus University Rotterdam, Rotterdam, The Netherlands.  
[15] Luo, Z.-Q., Sturm, J. F. and Zhang, S. (1997). Duality results for conic convex programming. Technical Report 9719/A, Econometric Institute, Erasmus University Rotterdam, Rotterdam, The Netherlands.  
[16] Mehrotra, S. (1992). On the implementation of a primal-dual interior point method, SIAM Journal on Optimization, 2, 575-601.  
[17] Mehrotra, S. and Ye, Y. (1993). Finding an interior point in the optimal face of linear programs, Mathematical Programming, 62, 497-515.  
[18] Mittelmann, H. D. (1998). Several SDP-codes on problems from SDPLIB. ftp://plato.la.asu.edu/pub/sdplib.txt.  
[19] Monteiro, R. D. C. and Mehrotra, S. (1996). A general parametric analysis approach and its implication to sensitivity analysis in interior point methods, Mathematical Programming, 72, 65-82.  
[20] Nesterov, Y. and Todd, M. J. (1997). Self-scaled barriers and interior-point methods for convex programming, Mathematics of Operations Research, 22(1), 1-42.  
[21] Roos, C., Terlaky, T. and Vial, J.-Ph. (1997). Theory and algorithms for linear optimization. An interior point approach. Series in discrete mathematics and optimization. John Wiley & Sons, New York.  
[22] Ross, A. M. (1998). Optimization over cones: SDPpack versus SeDuMi. Technical Report 1998-10-22, Department IEOR, University of California at Berkeley.  
[23] Sturm, J. F. (1997). Primal-Dual Interior Point Approach to Semidefinite Programming, volume 156 of Tinbergen Institute Research Series. Thesis Publishers, Amsterdam, The Netherlands.  
[24] Sturm, J. F. and Zhang, S. (1997). On a wide region of centers and primal-dual interior point algorithms for linear programming, Mathematics of Operations Research, 22(2), 408-431.  
[25] Todd, M. J. and Ye, Y. (1998). Approximate Farkas lemmas and stopping rules for iterative infeasible-point algorithms for linear programming, Mathematical Programming, 81, 1-21.  
[26] Toh, K. C., Todd, M. J. and Tütuncü R. H. (1996). SDPT3 — a MATLAB package for semidefinite programming. Technical report, School of Operations Research and Industrial Engineering, Cornell University, Ithaca, NY, USA.  
[27] Vandenberghe, L. and Boyd, S. (1994). SP: Software for semidefinite programming. Information Systems Laboratory, Electrical Engineering Department, Stanford University, Stanford, USA.  
[28] Wu, S., Luo, Z.-Q. and Wong, K. (1997). Direction finding for coherent sources via Toeplitz approximation. Technical report, Communications Research Laboratory, McMaster University, Hamilton, Ontario, Canada.  
[29] Ye, Y., Todd, M. J. and Mizuno S. (1994). An  $O(\sqrt{n} L)$ -iteration homogeneous and self-dual linear programming algorithm, Mathematics of Operations Research, 19, 53-67.  
[30] Zhang, Y. (1997). Solving large-scale linear programs by interior-point methods under the MATLAB environment. Technical report, Department of Computational and Applied Mathematics, Rice University, Houston, Texas, USA.