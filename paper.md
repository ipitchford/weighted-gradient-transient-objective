# Transient objective convergence of spectrally weighted gradient descent

Anonymous

6 November 2026

Version 0.1.0-candidate · DOI: [10.5281/zenodo.24001734](https://doi.org/10.5281/zenodo.24001734)

AI-assisted research preprint; not externally peer reviewed.

# Abstract

Spectrally weighted gradient methods can share the long-time asymptotic rate of steepest descent while having a different worst-case objective decrease over finite horizons. We study this distinction for positive definite quadratic objectives normalised by $\lambda_{\min}(A)=1$ and $\lambda_{\max}(A)=\kappa$. This normalisation is part of the statement for a general nonhomogeneous weight. For every positive, nondecreasing, unbounded spectral weight, every fixed number $K$ of iterations, and every fixed relaxation parameter $0<\omega\le1$, the worst-case objective ratio has large-condition-number expansion $1-2\omega K/\kappa+o(\kappa^{-1})$. An elementary upper bound gives one direction; two- and three-dimensional constructions give the matching lower bound. For power weights $\Psi(\lambda)=\lambda^{2\ell}$ with $\ell>0$, the unrelaxed result remains sharp for every horizon $K=o(\log\kappa)$. A quantitative three-mode estimate also produces simultaneous failures of the per-iteration Kantorovich bound over logarithmically many iterations. Exact rational examples refute the two-step bound already for the standard minimal-gradient method. Two active eigenvalues cannot produce this failure: their two-step map is scalar and always satisfies the Kantorovich bound. These results answer a strong interpretation of a recent two-step question; we also prove the weaker single-factor interpretation and distinguish both from the established fixed-matrix asymptotic theory.

# Introduction

Consider the quadratic minimisation problem $$\tag{1}
 \min_{x\in\mathbb R^n} f(x),\qquad
 f(x)=\tfrac12x^TAx-b^Tx,\qquad A=A^T\succ0.$$ Its minimiser is $x_*=A^{-1}b$. We study gradient-direction methods $$\tag{2}
 x_{j+1}=x_j-\omega\alpha_jg_j,\qquad
 g_j=Ax_j-b,\qquad
 \alpha_j=\frac{g_j^T\Psi(A)g_j}{g_j^TA\Psi(A)g_j}.$$ For $\Psi\equiv1$ and $\omega=1$, this is steepest descent with exact line search. For $\Psi(\lambda)=\lambda$, it is the minimal-gradient method, which minimises the Euclidean norm of the next gradient along the current gradient direction. The family $\Psi(\lambda)=\lambda^{2\ell}$ includes both cases and corresponds to $\ell$-minimal gradient descent in (MacDonald, Murray, and Tappenden, 2025). The notation of Pronzato, Wynn and Zhigljavsky (Pronzato, Wynn, and Zhigljavsky, 2006) corresponds to $P(\lambda)=\Psi(\lambda)/\lambda$; their $P$-gradient family imposes additional regularity conditions on the weight.

Let $$E_j=f(x_j)-f(x_*)=\tfrac12(x_j-x_*)^TA(x_j-x_*),
 \qquad \kappa=\lambda_{\max}(A)/\lambda_{\min}(A).$$ The ordinary objective gap $E_j$ is the quantity studied throughout. Results for the norm minimised by the step rule need not transfer to this objective without a condition-number factor. The mechanism is simple: a high-curvature component can carry little objective energy yet dominate the weighted choice of step. The algorithm then takes short steps while most objective error remains in a low-curvature component. Two high modes keep this imbalance alive even without relaxation.

For steepest descent, the classical Kantorovich estimate is $$\tag{3}
 E_{j+1}\le C_\kappa E_j,\qquad
 C_\kappa=\left(\frac{\kappa-1}{\kappa+1}\right)^2.$$ Pronzato et al. establish common long-time asymptotic behaviour for a broad family of $P$-gradient methods (Pronzato, Wynn, and Zhigljavsky, 2006). Huang et al. give explicit limiting ratios for odd and even subsequences (Huang, Dai, Liu, and Zhang, 2022). In particular, Corollary 11, equations (60)–(62), and Remark 12, equation (63), of their author manuscript arXiv:1908.07111v1 imply that the limiting two-step objective ratio is at most $C_\kappa^2$, under their hypotheses. Those statements first fix the matrix and starting point and then send the iteration count to infinity. For symmetric positive-definite systems, standard minimal gradient is also known as minimal residual iteration or GMRES(1). He (2025) studies its residual-norm and root-convergence factors; these differ from the ordinary-objective finite-horizon quantity considered here.

MacDonald, Murray and Tappenden (MacDonald, Murray, and Tappenden, 2025) develop nonasymptotic results for relaxed power-weighted methods. Their published Section 6, paragraph headed ``Future work'', asks whether a two-step objective decrease can attain the Kantorovich rate. The question is expressed in prose, rather than as a quantified inequality. Two interpretations must therefore be separated: $$\begin{aligned}
 E_{j+2}&\le C_\kappa^2E_j, &&\text{the per-iteration rate over two steps},\tag{4}\\
 E_{j+2}&\le C_\kappa E_j, &&\text{one Kantorovich factor over two steps}.\tag{5}
\end{aligned}$$ We disprove (4), including for the standard minimal-gradient method, and prove (5) in the unrelaxed case. We do not attribute the fully quantified statement (4) verbatim to the source.

The later flexible framework of MacDonald, Murray and Tappenden (2025b, arXiv:2505.04047v1, Definition 8 and Section 2.1, Lemma 9) permits multiple search directions and symmetric preconditioning, with comparison in a selected weighted gradient norm. Those results do not by themselves give the sharp ordinary-objective transient lower construction studied here. Our counterexamples concern the single-gradient-direction update (2), not every algorithm in that broader framework.

The main result identifies the sharp leading coefficient in the finite-horizon worst-case objective decrease. In the unrelaxed case $\omega=1$, this coefficient is $2K$ for every positive, nondecreasing, unbounded spectral weight, whereas steepest descent has coefficient $4K$. Power-weighted methods exhibit this distinction over horizons growing more slowly than $\log\kappa$, and explicit instances violate the Kantorovich bound at every horizon in an interval of length proportional to $\log\kappa$.

The methods and their conjugacy to steepest descent are established objects. Our proposed contribution is the objective-specific finite-horizon lower construction, its quantitative control, and the resulting order-of-limits distinction. No claim is made that the classical two-point dynamics or the underlying algorithm family is new.

## Reading the result: metrics and limits

| Quantity or regime | What is held fixed | What the result does—and does not—say |
|---|---|---|
| Ordinary objective $E_j$ | The displayed quadratic | This is the measured error; it is not the weighted gradient norm used to choose the step. |
| Fixed horizon (Theorem 3) | $\Psi,\omega,K$; $\kappa\to\infty$ | Worst-case deficit has coefficient $2\omega K$; the problem instance may vary with $\kappa$. |
| Sublogarithmic horizon (Theorem 7) | Power exponent $\ell>0$, $\omega=1$; $K=o(\log\kappa)$ | The sharp coefficient per step is two; the witness may depend on the chosen horizon. |
| Simultaneous interval (Corollary 8) | $\ell>0$ and admissible $\theta$ | One instance at each $\kappa$ violates the bound for every $1\le K\le\theta\log\kappa$. |
| Fixed-matrix long time | One matrix and starting point; $j\to\infty$ | This is the inherited asymptotic theory, not the limit taken in our lower construction. |

**Proof roadmap.** Proposition 1 gives an objective upper bound. Theorem 3 matches its leading deficit using a small amount of high-mode energy. Proposition 5 explains why two active eigenvalues cannot give the unrelaxed two-step failure. Lemma 6 controls the perturbation for finite parameters, giving an explicit sufficient failure test and then the growing-horizon results. Readers seeking a concrete check can first consult the exact rational examples.

# Normalisation and an objective bound

Translation by $x_*$ reduces (1) to $b=0$. We impose $$\tag{6}
 \lambda_{\min}(A)=1,\qquad \lambda_{\max}(A)=\kappa>1.$$ For power weights this loses no generality after rescaling $A$. For a general nonhomogeneous $\Psi$, the normalisation is part of the statement. A rescaling may change the function used as a spectral weight.

Unless stated otherwise, $\Psi:[1,\infty)\to(0,\infty)$ is nondecreasing, and $0<\omega\le1$. Finite-dimensional spectral calculus defines $\Psi(A)$ without continuity assumptions. Multiplying $\Psi$ by a positive scalar does not change the algorithm. When an iterate reaches the minimiser, every later iterate is defined to equal it.

**Proposition 1**. *Under these assumptions, every iterate satisfies $$\tag{7}
 E_{j+1}\le(1-\omega/\kappa)^2 E_j,
 \qquad E_K\le(1-\omega/\kappa)^{2K}E_0.$$*

*Proof.* Write $\alpha_{\rm SD}=g^Tg/(g^TAg)$. The reciprocal weighted-mean formula and monotonicity of $\Psi$ imply $$\tag{8}
 \kappa^{-1}\le\alpha\le\alpha_{\rm SD}.$$ For completeness, assign probability weights proportional to the squared components of $g$ in an eigenbasis, and let $\Lambda$ be the resulting spectral random variable. If $\Lambda'$ is an independent copy, then $$\mathbb E[\Lambda\Psi(\Lambda)]-\mathbb E[\Lambda]\mathbb E[\Psi(\Lambda)]
 =\tfrac12\mathbb E[(\Lambda-\Lambda')(\Psi(\Lambda)-\Psi(\Lambda'))]\ge0.$$ This proves the second inequality in (8); the first follows from $\Lambda\le\kappa$.

The quadratic $t\mapsto f(x-tg)$ decreases for $0\le t\le\alpha_{\rm SD}$. Both $\omega/\kappa$ and $\omega\alpha$ lie in this interval, in the stated order. Hence $$f(x-\omega\alpha g)\le f(x-\omega g/\kappa).$$ In an eigenbasis, the last update multiplies the coordinate with eigenvalue $\lambda$ by $1-\omega\lambda/\kappa\in[0,1-\omega/\kappa]$. This proves the one-step estimate. Iteration proves the second. ◻

**Corollary 2**. *For $\omega=1$, every nondecreasing positive weight satisfies (5).*

*Proof.* Proposition 1 gives $E_{j+2}/E_j\le(1-1/\kappa)^4$. Moreover $$(1-1/\kappa)^4\le\left(\frac{\kappa-1}{\kappa+1}\right)^2$$ because $(\kappa-1)(\kappa+1)\le\kappa^2$. ◻

The comparison argument in Proposition 1 is elementary. It improves the Rate I bound of (MacDonald, Murray, and Tappenden, 2025; Theorem 10) in the range $0<\omega\le1$, but its independent historical priority is not needed for the lower-bound results below.

# Sharp fixed-horizon asymptotics

For an integer $K\ge1$, define $$\tag{9}
 \mathcal W_{\Psi,\omega,K}(\kappa)
 =\sup\frac{E_K}{E_0},$$ where the supremum ranges over finite dimensions, matrices satisfying (6), and starting points with $E_0>0$. Let $\mathcal W^{(n)}$ denote the same supremum restricted to dimension $n$.

**Theorem 3**. *Suppose that $\Psi$ is positive, nondecreasing and unbounded. For each fixed $0<\omega\le1$ and positive integer $K$, $$\tag{10}
 \lim_{\kappa\to\infty}\kappa[1-\mathcal W_{\Psi,\omega,K}(\kappa)]
 =2\omega K.$$ The same limit holds with $\mathcal W$ replaced by $\mathcal W^{(3)}$. If $0<\omega<1$, it also holds with $\mathcal W^{(2)}$.*

*Proof.* Proposition 1 yields $$\liminf_{\kappa\to\infty}\kappa(1-\mathcal W_{\Psi,\omega,K})\ge2\omega K.$$ It remains to construct matching examples. We describe an initial point by its objective-energy weights $w_i=\lambda_i x_{0,i}^2$, so that $2E_0=\sum_iw_i$. Write $$P_j(z)=\prod_{i=0}^{j-1}(1-\omega\alpha_i z).$$ Then $2E_j=\sum_iw_iP_j(\lambda_i)^2$.

First take $0<\omega<1$, let $A_\kappa=\operatorname{diag}(1,\kappa)$, and set $$T_\kappa=\sqrt{\Psi(\kappa)},\qquad
 (w_1,w_2)=\left(1,\frac{T_\kappa}{\kappa\Psi(\kappa)}\right).$$ The high-mode weight is $o(\kappa^{-1})$. Put $H_j=P_j(1)^2$, $V_j=P_j(\kappa)^2$, $a_j=\kappa\alpha_j$, and $\varepsilon_\kappa=\Psi(1)/T_\kappa\to0$. The exact recurrence is $$a_j=\frac{\varepsilon_\kappa H_j+V_j}{\varepsilon_\kappa H_j/\kappa+V_j},
 \quad H_{j+1}=H_j(1-\omega a_j/\kappa)^2,
 \quad V_{j+1}=V_j(1-\omega a_j)^2.$$ For each fixed $j$, induction gives $a_j\to1$, $H_j\to1$, and $V_j\to(1-\omega)^{2j}>0$. Therefore $$H_K=1-\frac{2\omega K}{\kappa}+o(\kappa^{-1}),\qquad
 \frac{E_K}{E_0}=H_K+o(\kappa^{-1}),$$ which proves the matching upper limit for the scaled deficit.

Now take $\omega=1$. Fix $c\in(0,1)$ and require $\kappa\ge1/c$. Set $$\tag{11}
 A_\kappa=\operatorname{diag}(1,c\kappa,\kappa),\quad
 T_\kappa=\sqrt{\Psi(c\kappa)},\quad
 (w_1,w_2,w_3)=\left(1,\frac{T_\kappa}{c\kappa\Psi(c\kappa)},
 \frac{T_\kappa}{\kappa\Psi(\kappa)}\right).$$ The total high-mode energy is at most $(1+c^{-1})/[\kappa\sqrt{\Psi(c\kappa)}]=o(\kappa^{-1})$. Its two contributions to the step numerator initially equal $T_\kappa$. Put $U_j=P_j(c\kappa)^2$, $V_j=P_j(\kappa)^2$, $H_j=P_j(1)^2$, $a_j=\kappa\alpha_j$, and $\varepsilon_\kappa=\Psi(1)/T_\kappa$. Then $$\begin{aligned}
 a_j&=\frac{U_j+V_j+\varepsilon_\kappa H_j}
 {cU_j+V_j+\varepsilon_\kappa H_j/\kappa},\tag{12}\\
 H_{j+1}&=H_j(1-a_j/\kappa)^2,\quad
 U_{j+1}=U_j(1-ca_j)^2,\quad
 V_{j+1}=V_j(1-a_j)^2.\notag
\end{aligned}$$ Let $d=(1-c)/(1+c)$. Since $\varepsilon_\kappa\to0$, induction for each fixed $j$ gives $$\tag{13}
 a_j\longrightarrow\frac2{1+c},\qquad H_j\longrightarrow1,
 \qquad U_j,V_j\longrightarrow d^{2j}>0.$$ The induction is valid because every limiting denominator is positive. At equal high-mode weights the limiting step is $2/(1+c)$, and both high-mode squared multipliers equal $d^2$.

Expanding the finite product for $H_K$ and using the negligible high-mode energy gives $$\tag{14}
 \frac{E_K}{E_0}=1-\frac{4K}{(1+c)\kappa}+o(\kappa^{-1}).$$ Thus $\limsup\kappa(1-\mathcal W^{(3)})\le4K/(1+c)$ for each $c<1$. Letting $c\uparrow1$ proves (10). The two-dimensional construction for $\omega<1$ embeds in dimension three by adjoining a zero initial coordinate at an existing eigenvalue. ◻

**Corollary 4**. *Fix an unbounded positive nondecreasing $\Psi$, $0<\omega\le1$, and an integer $K\ge1$. The inequality $$\tag{15}
 E_K\le\left(1-\omega(2-\omega)\frac{4\kappa}{(1+\kappa)^2}\right)^K E_0$$ does not hold uniformly over positive definite quadratic problems.*

*Proof.* The factor on the right has expansion $1-4\omega(2-\omega)K/\kappa+O(\kappa^{-2})$. Its leading deficit exceeds $2\omega K$, because $0<\omega\le1$. Theorem 3 gives examples with a strictly larger objective ratio for all sufficiently large condition numbers. ◻

For $\Psi(\lambda)=\lambda^{2\ell}$, every fixed $\ell>0$ satisfies Theorem 3. At $\ell=0$, the unrelaxed exact worst-case factor is $C_\kappa^K$, whose leading deficit is $4K/\kappa$. Hence the limit $\ell\downarrow0$ is not uniform in $\kappa$. This statement concerns the worst objective ratio; it does not assert a discontinuity of individual iterates at fixed $A$.

# Why three spectral modes are necessary

The two-point dynamics explain both the limiting construction and why two-dimensional tests can miss the obstruction. The following identity is a direct form of the classical two-point recurrence underlying (Pronzato, Wynn, and Zhigljavsky, 2006; Huang, Dai, Liu, and Zhang, 2022); see also He (2025, Theorem 9 and Lemma 10) for minimal residual iteration. We include its proof to make the dimensional boundary explicit.

**Proposition 5**. *Suppose $\omega=1$, $\Psi$ is positive, and the initial error has components in at most two distinct eigenspaces of $A$. Then $$\tag{16}
 E_{j+2}\le C_\kappa^2 E_j$$ for every $j$, and every even block satisfies $E_{j+2m}\le C_\kappa^{2m}E_j$.*

*Proof.* If only one active eigenvalue remains, one step reaches the minimiser. Otherwise let $a$ be the lower active eigenvalue and let the upper active eigenvalue be $a\rho$, where $1<\rho\le\kappa$. Rescale the matrix to $A/a$ and define the rescaled weight $\widetilde\Psi(t)=\Psi(at)$. The gradient is divided by $a$ and the stepsize is multiplied by $a$, leaving the iterate update unchanged. At a given iterate define $$R=\frac{\widetilde\Psi(\rho)g_{\rho}^2}{\widetilde\Psi(1)g_1^2}>0,$$ where $g_1^2$ and $g_\rho^2$ denote squared Euclidean norms of the eigenspace projections of the rescaled gradient. The rescaled stepsize is $\widetilde\alpha=(1+R)/(1+\rho R)$. Its multipliers on the low and high components are respectively $$\frac{R(\rho-1)}{1+\rho R},\qquad
 -\frac{\rho-1}{1+\rho R}.$$ Consequently the next weighted ratio is $R^{-1}$. After two steps, both error components are multiplied by the same positive scalar $$\gamma(R)=\frac{(\rho-1)^2R}{(1+\rho R)(\rho+R)}
 =\frac{(\rho-1)^2}{\rho(R+R^{-1})+\rho^2+1}
 \le\left(\frac{\rho-1}{\rho+1}\right)^2.$$ The energy ratio over these two steps is $\gamma(R)^2$. Since $\rho\le\kappa$, this proves (16); iteration proves the even-block estimate. ◻

Three active eigenvalues are therefore the smallest possible support of an unrelaxed two-step counterexample. This is a statement about the active spectrum, so repeated eigenvalues or additional zero coordinates do not alter it.

# Quantitative control and growing horizons

We now take $\Psi(\lambda)=\lambda^{2\ell}$ with fixed $\ell>0$, and $\omega=1$. Write $\mathcal W_{\ell,K}$ for the corresponding worst-case ratio. The finite-horizon construction can be controlled while $K$ grows with $\kappa$.

Fix $$\tag{17}
 \kappa\ge4,\quad \tfrac12\le c<1,\quad
 \delta=1-c,\quad d=\frac{1-c}{1+c},\quad
 0<\nu<2\ell,\quad\mu=2\ell-\nu.$$ Use the three-mode matrix and starting point $$\tag{18}
 A_\kappa=\operatorname{diag}(1,c\kappa,\kappa),\qquad
 x_0=\left(1,c^{-(\ell+1)}\kappa^{-(\nu+2)/2},
 \kappa^{-(\nu+2)/2}\right).$$ Its energy weights are $(1,c^{-(2\ell+1)}\kappa^{-1-\nu},\kappa^{-1-\nu})$. Set $$\beta_j=\kappa^{-\mu}d^{-2j},\qquad C_0=1+c^{-(2\ell+1)}.$$

**Lemma 6**. *If $K\ge1$ and $\beta_K\le\delta/64$, then the construction (18) satisfies $$\tag{19}
 \left|\kappa\left(1-\frac{E_K}{E_0}\right)-\frac{4K}{1+c}\right|
 \le\beta_K+C_0\kappa^{-\nu}+\frac{9K^2}{2\kappa}.$$*

*Proof.* The recurrence (12) holds with $\varepsilon_\kappa=\kappa^{-\mu}$. Whenever the high-mode multipliers are nonzero, define $$r_j=\log(U_j/V_j),\qquad s_j=\log(V_j/d^{2j}),\qquad
 \epsilon_j=\kappa^{-\mu}H_j/V_j=\beta_jH_je^{-s_j}.$$ The variables $r_j$ and $s_j$ measure, respectively, the high-mode imbalance and departure from their common limiting decay. Since $\alpha_j$ is the reciprocal of a weighted mean of eigenvalues at least one, $0<\alpha_j\le1$ and hence $0\le H_j\le1$. We prove simultaneously that $$\tag{20}
 |r_j|,|s_j|\le4\beta_j/\delta,\qquad\epsilon_j\le2\beta_j
 \quad(0\le j\le K).$$ At $j=0$ the bounds hold. Under the stated hypothesis, the claimed logarithmic bounds do not exceed $1/16$.

Put $A_c=(c-1/\kappa)/\delta$ and $B_c=(1-1/\kappa)/\delta$. Both are nonnegative and at most $1/\delta$. In terms of $r_j,\epsilon_j$, $$\tag{21}
 a_j=\frac{e^{r_j}+1+\epsilon_j}{ce^{r_j}+1+\epsilon_j/\kappa}.$$ Direct algebra gives $$1-ca_j=\frac{\delta-(c-1/\kappa)\epsilon_j}
 {ce^{r_j}+1+\epsilon_j/\kappa},\quad
 1-a_j=-\frac{\delta e^{r_j}+(1-1/\kappa)\epsilon_j}
 {ce^{r_j}+1+\epsilon_j/\kappa}.$$ The first numerator remains positive because $A_c\epsilon_j\le1/32$; the second is strictly positive before its minus sign. Thus neither high mode vanishes at the next step. Their logarithmic recurrences are $$\begin{aligned}
 r_{j+1}&=-r_j+2\log(1-A_c\epsilon_j)
 -2\log(1+B_c\epsilon_je^{-r_j}),\tag{22}\\
 s_{j+1}-s_j&=2r_j-2\log\frac{ce^{r_j}+1}{1+c}
 +2\log(1+B_c\epsilon_je^{-r_j})\notag\\
 &\hspace{13mm}-2\log\left(1+\frac{\epsilon_j}{\kappa(ce^{r_j}+1)}\right).
 \tag{23}
\end{aligned}$$ For $0\le u\le1/32$, $-\log(1-u)\le4u/3$; for $v\ge0$, $\log(1+v)\le v$. Using $e^{1/16}\le16/15$ also makes these numerical constant comparisons rational. Hence $$\tag{24}
 |r_{j+1}+r_j|<5\epsilon_j/\delta\le10\beta_j/\delta.$$ The derivative of $2r-2\log[(ce^r+1)/(1+c)]$ is $2/(ce^r+1)\le2$. The remaining terms in (23) have total absolute value at most $$2e^{1/16}\epsilon_j/\delta+2\epsilon_j/\kappa
 \le(2e^{1/16}+1/4)\epsilon_j/\delta<3\epsilon_j/\delta.$$ Therefore $$\tag{25}
 |s_{j+1}-s_j|\le2|r_j|+3\epsilon_j/\delta
 \le14\beta_j/\delta.$$ As $d\le1/3$, $$\tag{26}
 \sum_{i=0}^{j-1}\beta_i
 =\beta_j\frac{d^2(1-d^{2j})}{1-d^2}\le\beta_j/8.$$ Summing (24) in absolute value and (25) gives respectively $|r_j|\le5\beta_j/(4\delta)$ and $|s_j|\le7\beta_j/(4\delta)$, strictly within (20). Finally $\epsilon_j\le e^{1/16}\beta_j<2\beta_j$. This closes the induction, including nonvanishing of the high modes.

Compare first $\epsilon_j$ to zero at fixed $r_j$, along the nonnegative $\epsilon$ interval, and then compare $r_j$ to zero at $\epsilon=0$. The bootstrap keeps $|r|\le1/16$ on this path. At $\epsilon=0$, the absolute derivative in $r$ of the map in (21) equals $\delta e^r/(ce^r+1)^2\le\delta/(4c)\le\delta/2$. Its derivative in $\epsilon$ is nonnegative and at most one, because $$0\le\frac{ce^r+1-(e^r+1)/\kappa}
 {(ce^r+1+\epsilon/\kappa)^2}\le1.$$ It follows that $$|a_j-2/(1+c)|\le4\beta_j,\qquad
 2\sum_{j<K}|a_j-2/(1+c)|\le\beta_K.$$ Also $a_j\le4/3+1/32<3/2$. Put $z=\sum_{j<K}a_j/\kappa$. The elementary product and exponential bounds imply $$1-2z\le H_K=\prod_{j<K}(1-a_j/\kappa)^2
 \le e^{-2z}\le1-2z+2z^2.$$ Consequently $$\left|\kappa(1-H_K)-\frac{4K}{1+c}\right|
 \le\beta_K+\frac{9K^2}{2\kappa}.$$ For $K\ge1$, the bootstrap gives $V_K\le e^{1/16}d^{2K}<1$ and $U_K\le e^{1/8}d^{2K}<1$. The exact objective ratio is $$\frac{E_K}{E_0}
 =\frac{H_K+\kappa^{-1-\nu}[c^{-(2\ell+1)}U_K+V_K]}
 {1+C_0\kappa^{-1-\nu}},$$ so $\kappa|E_K/E_0-H_K|\le C_0\kappa^{-\nu}$. Combining the last two estimates proves (19). ◻

## A finite-parameter applicability and failure test

Lemma 6 can be used without sending $\kappa$ to infinity. Retain all parameters and the initial point in (17)–(18), and put
$B_K=\kappa^{-\mu}d^{-2K}+C_0\kappa^{-\nu}+\frac{9K^2}{2\kappa}.$
Its hypothesis on the integer horizon is exactly
$1\le K\le\left\lfloor
\frac{\mu\log\kappa+\log(\delta/64)}{2\log(1/d)}
\right\rfloor.$
If the upper endpoint is less than one, this test certifies no positive horizon. For any admitted $K$, the strict inequality
$\frac{4K}{1+c}+B_K
<\kappa\left[1-C_\kappa^K\right]$
is sufficient to certify $E_K/E_0>C_\kappa^K$ for that specific initial point.

*Derivation.* Taking logarithms of $\kappa^{-\mu}d^{-2K}\le\delta/64$ and using $\log(1/d)>0$ gives the horizon condition. Lemma 6 gives $E_K/E_0\ge1-[4K/(1+c)+B_K]/\kappa$, which proves the strict failure conclusion. This is an elementary consequence of the lemma, not an optimal horizon formula or a necessary condition for failure. Numerical evaluation of nonrational powers or logarithms requires certified enclosures if it is to count as a certificate; decimal evaluation alone is not an exact test. The exact rational counterexamples below establish failure directly and need not satisfy this sufficient test.

**Theorem 7**. *Fix $\ell>0$. For every integer-valued horizon $K=K(\kappa)\ge1$ with $K=o(\log\kappa)$, $$\tag{27}
 \lim_{\kappa\to\infty}\frac{\kappa}{K(\kappa)}
 [1-\mathcal W_{\ell,K(\kappa)}(\kappa)]=2.$$ The same statement holds when the supremum is restricted to dimension three.*

*Proof.* Proposition 1 gives the lower limit two for the scaled deficit, since $K=o(\kappa)$. For a matching example, take $\nu=\ell$ in Lemma 6, write $h=\log\kappa$, and choose $$d=\exp[-\sqrt{h/K}],\qquad c=(1-d)/(1+d).$$ Then $d\to0$, $c\to1$, and eventually $c\ge1/2$. Since $\delta=2d/(1+d)\ge d$, $$\frac{\beta_K}{\delta}
 \le\exp[-\ell h+2\sqrt{Kh}+\sqrt{h/K}]\longrightarrow0.$$ The exponent tends to minus infinity because $K/h\to0$ and $K\ge1$. Thus Lemma 6 applies eventually. Its error divided by $K$ tends to zero, whereas $4/(1+c)=2(1+d)\to2$. One admissible three-dimensional instance lower-bounds the worst-case ratio and gives the required upper limit for its deficit. ◻

**Corollary 8**. *Fix $\ell>0$ and $0<\theta<2\ell/\log9$. There exists a three-dimensional family such that, for all sufficiently large $\kappa$, $$\tag{28}
 \frac{E_K}{E_0}>C_\kappa^K
 \qquad\text{for every integer }1\le K\le\theta\log\kappa.$$ The same instance at each $\kappa$ works simultaneously for every indicated horizon.*

*Proof.* Take $c=1/2$, so $d=1/3$, and choose $0<\nu<2\ell-\theta\log9$. Then $\mu=2\ell-\nu>\theta\log9$, and $\beta_K\le\kappa^{-\mu+\theta\log9}\to0$ uniformly on the stated range. Lemma 6 yields $$\kappa(1-E_K/E_0)=\frac{8K}{3}+o(1)$$ uniformly on that range. In contrast, $$\kappa(1-C_\kappa^K)=4K+O(K^2/\kappa+K/\kappa),$$ with a uniform error tending to zero. The positive leading difference $4K/3$ proves (28). ◻

*Remark 9*. Neither Theorem 7 nor Corollary 8 fixes one matrix and then sends $K$ to infinity. The matrix and starting point vary with $\kappa$; in Theorem 7, their high-mode separation also depends on the chosen horizon. The results therefore coexist with the fixed-matrix long-time asymptotic theory in (Pronzato, Wynn, and Zhigljavsky, 2006; Huang, Dai, Liu, and Zhang, 2022). No sharp worst-case formula is asserted here for arbitrary horizons comparable to or larger than $\log\kappa$.

# Exact rational counterexamples

The limiting arguments do not depend on numerical optimisation. Small exact instances also establish the two-step failure directly.

## Standard minimal gradient

Take $\ell=1/2$, $\omega=1$, and $$\tag{29}
 A=\operatorname{diag}(1,60,100),\qquad x_0=(1,1/100,1/250)^T.$$ Direct rational arithmetic gives $$\alpha_0=\frac{193}{14485},\qquad
 \alpha_1=\frac{7013813}{446629608},$$ and $$\tag{30}
 \frac{E_2}{E_0}
 =\frac{830774224427957654527687}{887449697831729589460572}
 \approx0.9361366919812527.$$ The Kantorovich two-step value is $(99/101)^4\approx0.9231138845986189$. Their exact difference is positive: $$\frac{E_2}{E_0}-\left(\frac{99}{101}\right)^4
 =\frac{1202635053150759637694223270715}
 {92348371423698611602832496009372}>0.$$ This example uses the classical minimal-gradient method itself.

## A smaller-condition-number example

For $\ell=1$ and $\omega=1$, take $$A=\operatorname{diag}(1,6,10),\qquad x_0=(1,1/10,1/25)^T.$$ Then $$\alpha_0=\frac{749}{5969},\qquad
 \alpha_1=\frac{285369}{1748690},\qquad
 \frac{E_2}{E_0}=\frac{145981491016797622500}{293076563677580674949}
 \approx0.4981001864666148.$$ Here $(9/11)^4\approx0.4481251280650229$, and $$\frac{E_2}{E_0}-\left(\frac9{11}\right)^4
 =\frac{214439675688327182682111}{4290933968803458661928309}>0.$$

## A rational family for arbitrary fixed horizons

In the unrelaxed power construction take $\ell=1/2$, $c=1/4$, $\nu=1/2$, and $\kappa=N^4$ for an integer $N\ge2$. This gives $$\tag{31}
 A_N=\operatorname{diag}(1,N^4/4,N^4),\qquad
 x_0=(1,8/N^5,1/N^5)^T.$$ Every entry is rational, and $A_N$ has integer entries when $N$ is even. The fixed-step induction in Theorem 3, with the power-specific energy weights, gives $$\tag{32}
 \lim_{N\to\infty}N^4\left(1-\frac{E_K}{E_0}\right)=\frac{16K}{5}
 \qquad(K\text{ fixed}).$$ For example, $N=4$ gives $\kappa=256$ and $E_2/E_0\approx0.9711072425654474>(255/257)^4\approx0.9692330804194722$. The rational family supplies explicit finite instances for every fixed block length, although the existence theorem does not assert a small sufficient $N$ uniformly in $K$.

# Interpretation and limits

The construction separates the spectrum that controls the step from the spectrum that carries most of the objective. A small amount of objective energy at large eigenvalues dominates the weighted step numerator. Two nearby high modes then maintain a short step for many iterations. Meanwhile the low mode carries almost all the ordinary objective and decreases at the rate associated with a step near $1/\kappa$.

For power weights, the change of variables $y=A^\ell(x-x_*)$ transforms the iteration into steepest descent for $\tfrac12y^TAy$. The measured objective becomes $\tfrac12y^TA^{1-2\ell}y$. This conjugacy explains why familiar weighted-norm convergence and the slower finite-time objective decrease can occur together. It does not alone establish the sharp finite-horizon coefficient or the quantitative interval of failure; those require the energy-specific construction.

The two-step issue has a precise boundary. One Kantorovich factor over two unrelaxed steps is always valid under the monotone-weight assumption. Two factors over the same steps fail with three active spectral modes, including for standard minimal gradient. No fixed block length repairs the per-iteration rate uniformly over condition number. For power weights, the sharp coefficient remains two throughout every sublogarithmic horizon, and one instance can violate the claimed per-iteration bound throughout a logarithmic interval.

The results do not give an exact finite-$\kappa$ formula for $\mathcal W_{\Psi,\omega,K}$, a sharp transition at horizons of order $\log\kappa$, or a complexity lower bound for arbitrary algorithms. They cover $0<\omega\le1$ for the fixed-horizon theorem and $\omega=1$ for the moving-horizon result. The case $1<\omega<2$ requires a separate comparison argument. The one-step upper estimate and the two-point identity are supporting ingredients whose novelty is not asserted. In particular, the factor-two difference in the leading transient decrement is not a claim that twice as many iterations are required for a fixed accuracy: the studied relative decrease tends to zero, and a fixed-fraction reduction lies outside these horizon regimes.

# Verification and research status

This is an AI-assisted research preprint, not external independent peer review. The mathematical claims rest on the proofs above. The displayed rational counterexamples can be checked with exact integer fractions; finite numerical grids do not prove the universal estimates. No proof-assistant formalisation or independent external reproduction is claimed. The accompanying verification record distinguishes current executable checks from historical provenance. The bounded prior-art comparison includes the originating question, the flexible-framework follow-up, the cited P-gradient and two-point asymptotic results, and equivalent names for minimal-gradient iteration. It did not identify the same objective-specific transient theorem, but does not establish exhaustive historical priority.

# Declarations

**Data and code.** The mathematical data are the explicit matrices, initial points and formulas in this paper. Accompanying checker sources and verification records document executable assurance separately.

**Authorship and AI assistance.** Anonymous scholarly attribution. AI systems assisted drafting, mathematical analysis, revision and internal review; this does not constitute external peer review.

**Ethics.** No human participants, personal data or animal research are involved.

**Funding and competing interests.** No funding or competing-interest declaration was supplied with the research bundle.

# References

L. MacDonald, R. Murray, and R. Tappenden, On a family of relaxed gradient descent methods for strictly convex quadratic minimization, *Computational Optimization and Applications* **91** (2025), 173–200. [doi:10.1007/s10589-025-00670-3](https://doi.org/10.1007/s10589-025-00670-3).

L. Pronzato, H. P. Wynn, and A. A. Zhigljavsky, Asymptotic behaviour of a family of gradient algorithms in $\mathbb R^d$ and Hilbert spaces, *Mathematical Programming* **107** (2006), 409–438. [doi:10.1007/s10107-005-0602-7](https://doi.org/10.1007/s10107-005-0602-7). Author manuscript: <https://arxiv.org/abs/0802.4382v1>.

Y. Huang, Y.-H. Dai, X.-W. Liu, and H. Zhang, On the asymptotic convergence and acceleration of gradient methods, *Journal of Scientific Computing* **90** (2022), article 7. [doi:10.1007/s10915-021-01685-8](https://doi.org/10.1007/s10915-021-01685-8). Author manuscript: <https://arxiv.org/abs/1908.07111v1>.

Y. He, The worst-case root-convergence factor of GMRES(1), 2025 preprint. <https://arxiv.org/abs/2501.10248v1>.


L. MacDonald, R. Murray, and R. Tappenden (2025b), *A Flexible Algorithmic Framework for Strictly Convex Quadratic Minimization*. arXiv:2505.04047v1. <https://arxiv.org/abs/2505.04047v1>.

