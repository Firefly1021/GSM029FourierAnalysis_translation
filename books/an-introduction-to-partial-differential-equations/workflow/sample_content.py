"""Sample transcription and translation, checked against PDF pages 12--14.

The English is reconstructed from the scan, NOT accepted from hidden OCR.
Bounding boxes below use 1800-pixel-high derivative image coordinates and are
converted to PDF points by the workflow. A block may span a physical page break.
"""

BLOCKS = []


def add(key, kind, regions, en, zh, label=None, title_en=None, title_zh=None):
    BLOCKS.append(dict(id=key, type=kind, regions=regions, english=en,
                       chinese=zh, label=label, title_en=title_en, title_zh=title_zh))


add('basic-mathematical-questions', 'section', [(12, 95, 145, 1040, 200)],
    'Basic Mathematical Questions', '基本数学问题', 'sec:basic-mathematical-questions')
add('existence', 'subsection', [(12, 95, 225, 1040, 280)],
    'Existence', '存在性', 'subsec:existence')
add('existence-questions', 'ordinary-paragraph', [(12, 95, 285, 1040, 495)],
    r'''Questions of existence occur naturally throughout mathematics. The question of whether a solution exists \emph{should pop into} a mathematician's head any time he or she writes an equation down. Appropriately, the problem of existence of solutions of partial differential equations occupies a large portion of this text. In this section we consider precursors of the PDE theorems to come.''',
    r'''存在性问题自然地贯穿于整个数学之中. 数学家每次写下一个方程时, 脑海中\emph{都应当浮现}这个方程是否有解的问题. 因而, 偏微分方程解的存在性问题在本书中占有很大的篇幅, 这是恰当的. 本节考察后面将要讨论的偏微分方程定理的一些先导结果.''')
add('initial-value-problems-heading', 'subsection', [(12, 95, 560, 1040, 607)],
    'Initial-value problems in ODEs', '常微分方程的初值问题')
add('existence-prototype', 'ordinary-paragraph', [(12, 95, 615, 1040, 689)],
    'The prototype existence result in differential equations is for initial-value problems in ODEs.',
    '微分方程中存在性结果的典型范例是常微分方程初值问题的存在性结果.')
add('ode-existence', 'theorem', [(12, 95, 713, 1040, 1255)],
    r'''Let $D\subseteq\mathbb{R}\times\mathbb{R}^n$ be an open set, and let $\mathbf{F}:D\to\mathbb{R}^n$ be continuous in its first variable and \textbf{uniformly Lipschitz in its second}; i.e., for $(t,\mathbf{y})\in D$, $\mathbf{F}(t,\mathbf{y})$ is continuous as a function of $t$, and there exists a constant $\gamma$ such that for any $(t,\mathbf{y}_1)$ and $(t,\mathbf{y}_2)$ in $D$ we have
\begin{equation}\label{eq:uniform-lipschitz-bound}
|\mathbf{F}(t,\mathbf{y}_1)-\mathbf{F}(t,\mathbf{y}_2)|\leq\gamma|\mathbf{y}_1-\mathbf{y}_2|.
\end{equation}
Then, for any $(t_0,\mathbf{y}_0)\in D$, there exists an interval $I:=(t^-,t^+)$ containing $t_0$ and at least one solution $\mathbf{y}\in C^1(I)$ of the initial-value problem
\begin{equation}\label{eq:ode-initial-value-dynamics}
\frac{d\mathbf{y}}{dt}(t)=\mathbf{F}(t,\mathbf{y}(t)),
\end{equation}
\begin{equation}\label{eq:ode-initial-value-data}
\mathbf{y}(t_0)=\mathbf{y}_0.
\end{equation}''',
    r'''设 $D\subseteq\mathbb{R}\times\mathbb{R}^n$ 为开集, 且 $\mathbf{F}:D\to\mathbb{R}^n$ 关于第一个变量连续, \textbf{关于第二个变量一致 Lipschitz 连续}; 即对于 $(t,\mathbf{y})\in D$, $\mathbf{F}(t,\mathbf{y})$ 作为 $t$ 的函数连续, 并且存在常数 $\gamma$, 使得对于 $D$ 中任意的 $(t,\mathbf{y}_1)$ 和 $(t,\mathbf{y}_2)$ 都有
\begin{equation}\label{eq:uniform-lipschitz-bound}
|\mathbf{F}(t,\mathbf{y}_1)-\mathbf{F}(t,\mathbf{y}_2)|\leq\gamma|\mathbf{y}_1-\mathbf{y}_2|.
\end{equation}
那么, 对于任意 $(t_0,\mathbf{y}_0)\in D$, 都存在包含 $t_0$ 的区间 $I:=(t^-,t^+)$, 使得初值问题
\begin{equation}\label{eq:ode-initial-value-dynamics}
\frac{d\mathbf{y}}{dt}(t)=\mathbf{F}(t,\mathbf{y}(t)),
\end{equation}
\begin{equation}\label{eq:ode-initial-value-data}
\mathbf{y}(t_0)=\mathbf{y}_0.
\end{equation}
至少有一个解 $\mathbf{y}\in C^1(I)$.''',
    'thm:ode-existence', 'ODE existence, Picard-Lindelöf', '常微分方程的存在性, Picard-Lindelöf')
add('equivalent-integral-equation', 'ordinary-paragraph', [(12, 95, 1282, 1040, 1545)],
    r'''The proof of this can be found in almost any text on ODEs. We make note of one version of the proof that is the source of many techniques in PDEs: the construction of an equivalent integral equation. In this proof, one shows that there is a continuous function $\mathbf{y}$ that satisfies
\begin{equation}\label{eq:ode-integral-equation}
\mathbf{y}(t)=\mathbf{y}_0+\int_{t_0}^t\mathbf{F}(s,\mathbf{y}(s))\,ds.
\end{equation}''',
    r'''几乎任何一本常微分方程教材中都能找到这一结果的证明. 我们要指出其中一种证明, 它是偏微分方程中许多技巧的来源: 构造一个等价的积分方程. 在这一证明中, 先证明存在连续函数 $\mathbf{y}$ 满足
\begin{equation}\label{eq:ode-integral-equation}
\mathbf{y}(t)=\mathbf{y}_0+\int_{t_0}^t\mathbf{F}(s,\mathbf{y}(s))\,ds.
\end{equation}''')
add('picard-iteration', 'ordinary-paragraph', [(12, 95, 1555, 1040, 1705), (13, 90, 164, 1040, 447)],
    r'''Then the fundamental theorem of calculus implies that $\mathbf{y}$ is differentiable and satisfies \eqref{eq:ode-initial-value-dynamics}, \eqref{eq:ode-initial-value-data} (cf. the results on smoothness below). The solution of \eqref{eq:ode-integral-equation} is obtained from an iterative procedure; i.e., we begin with an initial guess for the solution (usually the constant function $\mathbf{y}_0$) and proceed to calculate
\begin{equation}\label{eq:picard-iteration}
\begin{aligned}
\mathbf{y}_1(t)&=\mathbf{y}_0+\textstyle\int_{t_0}^t\mathbf{F}(s,\mathbf{y}_0)\,ds,\\
\mathbf{y}_2(t)&=\mathbf{y}_0+\textstyle\int_{t_0}^t\mathbf{F}(s,\mathbf{y}_1(s))\,ds,\\
&\ \vdots\\
\mathbf{y}_{k+1}(t)&=\mathbf{y}_0+\textstyle\int_{t_0}^t\mathbf{F}(s,\mathbf{y}_k(s))\,ds,\\
&\ \vdots
\end{aligned}
\end{equation}''',
    r'''于是微积分基本定理表明, $\mathbf{y}$ 可微并满足 \eqref{eq:ode-initial-value-dynamics}, \eqref{eq:ode-initial-value-data} (参见下文关于光滑性的结果). 方程 \eqref{eq:ode-integral-equation} 的解由迭代过程得到; 即从解的一个初始猜测 (通常取常值函数 $\mathbf{y}_0$) 出发, 依次计算
\begin{equation}\label{eq:picard-iteration}
\begin{aligned}
\mathbf{y}_1(t)&=\mathbf{y}_0+\textstyle\int_{t_0}^t\mathbf{F}(s,\mathbf{y}_0)\,ds,\\
\mathbf{y}_2(t)&=\mathbf{y}_0+\textstyle\int_{t_0}^t\mathbf{F}(s,\mathbf{y}_1(s))\,ds,\\
&\ \vdots\\
\mathbf{y}_{k+1}(t)&=\mathbf{y}_0+\textstyle\int_{t_0}^t\mathbf{F}(s,\mathbf{y}_k(s))\,ds,\\
&\ \vdots
\end{aligned}
\end{equation}''')
add('iteration-convergence', 'ordinary-paragraph', [(13, 90, 458, 1040, 532)],
    'Of course, to complete the proof one must show that this sequence converges to a solution.',
    '当然, 要完成证明, 还必须证明这个序列收敛到一个解.')
add('iteration-later-chapters', 'ordinary-paragraph', [(13, 90, 534, 1040, 600)],
    'We will see generalizations of this procedure used to solve PDEs in later chapters.',
    '在后面的章节中, 我们将看到这一过程的推广被用于求解偏微分方程.')
add('calculus-existence-heading', 'subsection', [(13, 90, 625, 1040, 674)],
    'Existence theorems of advanced calculus', '高等微积分中的存在性定理')
add('inverse-function-introduction', 'ordinary-paragraph', [(13, 90, 683, 1040, 783)],
    r'''The following theorems from advanced calculus give information on the solution of algebraic equations. The first, the inverse function theorem, considers the problem of $n$ equations in $n$ unknowns.''',
    r'''下面这些高等微积分中的定理给出了代数方程解的有关信息. 第一个定理是反函数定理, 它考察由 $n$ 个方程和 $n$ 个未知量构成的问题.''')
add('inverse-function', 'theorem', [(13, 90, 799, 1040, 1407)],
    r'''Suppose the function
\[
\mathbf{F}:\mathbb{R}^n\ni\mathbf{x}:=(x_1,\ldots,x_n)\mapsto\mathbf{F}(\mathbf{x}):=(F_1(\mathbf{x}),\ldots,F_n(\mathbf{x}))\in\mathbb{R}^n
\]
is $C^1$ in a neighborhood of a point $\mathbf{x}_0$. Further assume that
\[
\mathbf{F}(\mathbf{x}_0)=\mathbf{p}_0
\]
and
\[
\frac{\partial\mathbf{F}}{\partial\mathbf{x}}(\mathbf{x}_0):=
\begin{pmatrix}
\frac{\partial F_1}{\partial x_1}(\mathbf{x}_0)&\cdots&\frac{\partial F_1}{\partial x_n}(\mathbf{x}_0)\\
\vdots&\ddots&\vdots\\
\frac{\partial F_n}{\partial x_1}(\mathbf{x}_0)&\cdots&\frac{\partial F_n}{\partial x_n}(\mathbf{x}_0)
\end{pmatrix}
\]
is nonsingular. Then there is a neighborhood $N_x$ of $\mathbf{x}_0$ and a neighborhood $N_p$ of $\mathbf{p}_0$ such that $\mathbf{F}:N_x\to N_p$ is one-to-one and onto; i.e., for every $\mathbf{p}\in N_p$ the equation
\[
\mathbf{F}(\mathbf{x})=\mathbf{p}
\]
has a unique solution in $N_x$.''',
    r'''设函数
\[
\mathbf{F}:\mathbb{R}^n\ni\mathbf{x}:=(x_1,\ldots,x_n)\mapsto\mathbf{F}(\mathbf{x}):=(F_1(\mathbf{x}),\ldots,F_n(\mathbf{x}))\in\mathbb{R}^n
\]
在点 $\mathbf{x}_0$ 的某个邻域内为 $C^1$ 的. 进一步假设
\[
\mathbf{F}(\mathbf{x}_0)=\mathbf{p}_0
\]
且
\[
\frac{\partial\mathbf{F}}{\partial\mathbf{x}}(\mathbf{x}_0):=
\begin{pmatrix}
\frac{\partial F_1}{\partial x_1}(\mathbf{x}_0)&\cdots&\frac{\partial F_1}{\partial x_n}(\mathbf{x}_0)\\
\vdots&\ddots&\vdots\\
\frac{\partial F_n}{\partial x_1}(\mathbf{x}_0)&\cdots&\frac{\partial F_n}{\partial x_n}(\mathbf{x}_0)
\end{pmatrix}
\]
非奇异. 那么, 存在 $\mathbf{x}_0$ 的邻域 $N_x$ 和 $\mathbf{p}_0$ 的邻域 $N_p$, 使得 $\mathbf{F}:N_x\to N_p$ 为一一映射且为满射; 即对于每个 $\mathbf{p}\in N_p$, 方程
\[
\mathbf{F}(\mathbf{x})=\mathbf{p}
\]
在 $N_x$ 中有唯一解.''',
    'thm:inverse-function', 'Inverse function theorem', '反函数定理')
add('implicit-function-introduction', 'ordinary-paragraph', [(13, 90, 1418, 1040, 1490)],
    r'''Our second result, the implicit function theorem, concerns solving a system of $p$ equations in $q+p$ unknowns.''',
    r'''第二个结果是隐函数定理, 它涉及求解由 $p$ 个方程和 $q+p$ 个未知量构成的方程组.''')
add('implicit-function', 'theorem', [(13, 90, 1500, 1040, 1710), (14, 95, 163, 1045, 608)],
    r'''Suppose the function
\[
\mathbf{F}:\mathbb{R}^q\times\mathbb{R}^p\ni(\mathbf{x},\mathbf{y})\mapsto\mathbf{F}(\mathbf{x},\mathbf{y})\in\mathbb{R}^p
\]
is $C^1$ in a neighborhood of a point $(\mathbf{x}_0,\mathbf{y}_0)$. Further assume that
\[
\mathbf{F}(\mathbf{x}_0,\mathbf{y}_0)=0,
\]
and that the $p\times p$ matrix
\[
\frac{\partial\mathbf{F}}{\partial\mathbf{y}}(\mathbf{x}_0,\mathbf{y}_0):=
\begin{pmatrix}
\frac{\partial F_1}{\partial y_1}(\mathbf{x}_0,\mathbf{y}_0)&\cdots&\frac{\partial F_1}{\partial y_p}(\mathbf{x}_0,\mathbf{y}_0)\\
\vdots&\ddots&\vdots\\
\frac{\partial F_p}{\partial y_1}(\mathbf{x}_0,\mathbf{y}_0)&\cdots&\frac{\partial F_p}{\partial y_p}(\mathbf{x}_0,\mathbf{y}_0)
\end{pmatrix}
\]
is nonsingular. Then there is a neighborhood $N_x\subset\mathbb{R}^q$ of $\mathbf{x}_0$ and a function $\hat{\mathbf{y}}:N_x\to\mathbb{R}^p$ such that
\[
\hat{\mathbf{y}}(\mathbf{x}_0)=\mathbf{y}_0,
\]
and for every $\mathbf{x}\in N_x$
\[
\mathbf{F}(\mathbf{x},\hat{\mathbf{y}}(\mathbf{x}))=0.
\]''',
    r'''设函数
\[
\mathbf{F}:\mathbb{R}^q\times\mathbb{R}^p\ni(\mathbf{x},\mathbf{y})\mapsto\mathbf{F}(\mathbf{x},\mathbf{y})\in\mathbb{R}^p
\]
在点 $(\mathbf{x}_0,\mathbf{y}_0)$ 的某个邻域内为 $C^1$ 的. 进一步假设
\[
\mathbf{F}(\mathbf{x}_0,\mathbf{y}_0)=0,
\]
且 $p\times p$ 矩阵
\[
\frac{\partial\mathbf{F}}{\partial\mathbf{y}}(\mathbf{x}_0,\mathbf{y}_0):=
\begin{pmatrix}
\frac{\partial F_1}{\partial y_1}(\mathbf{x}_0,\mathbf{y}_0)&\cdots&\frac{\partial F_1}{\partial y_p}(\mathbf{x}_0,\mathbf{y}_0)\\
\vdots&\ddots&\vdots\\
\frac{\partial F_p}{\partial y_1}(\mathbf{x}_0,\mathbf{y}_0)&\cdots&\frac{\partial F_p}{\partial y_p}(\mathbf{x}_0,\mathbf{y}_0)
\end{pmatrix}
\]
非奇异. 那么, 存在 $\mathbf{x}_0$ 的邻域 $N_x\subset\mathbb{R}^q$ 及函数 $\hat{\mathbf{y}}:N_x\to\mathbb{R}^p$, 使得
\[
\hat{\mathbf{y}}(\mathbf{x}_0)=\mathbf{y}_0,
\]
且对于每个 $\mathbf{x}\in N_x$ 都有
\[
\mathbf{F}(\mathbf{x},\hat{\mathbf{y}}(\mathbf{x}))=0.
\]''',
    'thm:implicit-function', 'Implicit function theorem', '隐函数定理')
add('linearization-comment', 'ordinary-paragraph', [(14, 95, 624, 1045, 768)],
    'The two theorems illustrate the idea that a nonlinear system of equations behaves essentially like its linearization as long as the linear terms dominate the nonlinear ones. Results of this nature are of considerable importance in differential equations.',
    '这两个定理说明了这样一种思想: 只要线性项占优于非线性项, 非线性方程组的表现就基本上与其线性化相同. 这类结果在微分方程中具有相当重要的意义.')
add('multiplicity', 'subsection', [(14, 95, 824, 1045, 874)],
    'Multiplicity', '多解性', 'subsec:multiplicity')
add('multiplicity-question', 'ordinary-paragraph', [(14, 95, 882, 1045, 989)],
    'Once we have asked the question of whether a solution to a given problem exists, it is natural to consider the question of how many solutions there are.',
    '一旦提出给定问题是否有解的问题, 自然就会进一步考察它有多少个解.')
add('uniqueness-heading', 'subsection', [(14, 95, 1024, 1045, 1066)],
    'Uniqueness for initial-value problems in ODEs', '常微分方程初值问题的唯一性')
add('uniqueness-prototype', 'ordinary-paragraph', [(14, 95, 1075, 1045, 1120)],
    'The prototype for uniqueness results is for initial-value problems in ODEs.',
    '唯一性结果的典型范例来自常微分方程的初值问题.')
add('ode-uniqueness', 'theorem', [(14, 95, 1130, 1045, 1239)],
    r'''Let the function $\mathbf{F}$ satisfy the hypotheses of Theorem~\ref{thm:ode-existence}. Then the initial-value problem \eqref{eq:ode-initial-value-dynamics}, \eqref{eq:ode-initial-value-data} has at most one solution.''',
    r'''设函数 $\mathbf{F}$ 满足 Theorem~\ref{thm:ode-existence} 的假设. 那么, 初值问题 \eqref{eq:ode-initial-value-dynamics}, \eqref{eq:ode-initial-value-data} 至多有一个解.''',
    'thm:ode-uniqueness', 'ODE uniqueness', '常微分方程的唯一性')
add('gronwall-proof-pointer', 'ordinary-paragraph', [(14, 95, 1250, 1045, 1297)],
    r'''A proof of this based on Gronwall's inequality is given below.''',
    r'''下文将给出一个基于 Gronwall 不等式的证明.''')
add('nonunique-example', 'ordinary-paragraph', [(14, 95, 1304, 1045, 1518)],
    r'''It should be noted that although this result covers a very wide range of initial-value problems, there are some standard, simple examples for which uniqueness fails. For instance, the problem
\[
\begin{aligned}
\frac{dy}{dt}&=y^{1/3},\\
y(0)&=0
\end{aligned}
\]''',
    r'''应当注意, 尽管这一结果适用于范围非常广泛的初值问题, 仍有一些标准的简单例子不具有唯一性. 例如, 问题
\[
\begin{aligned}
\frac{dy}{dt}&=y^{1/3},\\
y(0)&=0
\end{aligned}
\]''')
add('nonunique-family', 'ordinary-paragraph', [(14, 95, 1533, 1045, 1703)],
    r'''has an entire family of solutions parameterized by $\gamma\in[0,1]$:
\[
y_\gamma(t):=\begin{cases}
0,&0<t\leq\gamma,\\
\left[\frac{2}{3}(t-\gamma)\right]^{3/2},&\gamma<t\leq1.
\end{cases}
\]''',
    r'''有一整族以 $\gamma\in[0,1]$ 为参数的解:
\[
y_\gamma(t):=\begin{cases}
0,&0<t\leq\gamma,\\
\left[\frac{2}{3}(t-\gamma)\right]^{3/2},&\gamma<t\leq1.
\end{cases}
\]''')
