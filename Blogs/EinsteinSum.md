# The Summation Convention爱因斯坦求和约定

爱因斯坦求和约定将 $i$ 同时出现在上标和下标时的情况约定为对 $i$ 进行求和，极大地简化了求和的和式。

​        $\boldsymbol{u}=\sum_{i=1}^n u_i\boldsymbol{g}^i=u_i\boldsymbol{g}^i$


{% asset_img Einstein.JPG Albert Einstein %}


### 内积

​    $\boldsymbol{u}=\sum_{i=1}^n u_i\boldsymbol{g}^i=u_i\boldsymbol{g}^i$

​    $\boldsymbol{v}=\sum_{j=1}^n v_j\boldsymbol{g}^j=v_j\boldsymbol{g}^j$

​    $\boldsymbol{u}\cdot\boldsymbol{v}=\sum_{i=1}^n u_i\boldsymbol{g}^i\cdot\sum_{j=1}^n v_j\boldsymbol{g}^j=\sum_{i=1}^n\sum_{j=1}^n u_iv_j\boldsymbol{g}^i\cdot\boldsymbol{g}^j=u_iv_j\boldsymbol{g}^i\cdot\boldsymbol{g}^j$

这样看来$\boldsymbol{u}\cdot\boldsymbol{v}$的结果非常复杂，$n=3$时写出来是：

$u_1v_1\boldsymbol{g}^1\cdot\boldsymbol{g}^1+u_1v_2\boldsymbol{g}^1\cdot\boldsymbol{g}^2+u_1v_3\boldsymbol{g}^1\cdot\boldsymbol{g}^3+u_2v_1\boldsymbol{g}^2\cdot\boldsymbol{g}^1+u_2v_2\boldsymbol{g}^2\cdot\boldsymbol{g}^2+u_2v_3\boldsymbol{g}^2\cdot\boldsymbol{g}^3+u_3v_1\boldsymbol{g}^3\cdot\boldsymbol{g}^1+u_3v_2\boldsymbol{g}^3\cdot\boldsymbol{g}^2+u_3v_3\boldsymbol{g}^3\cdot\boldsymbol{g}^3$

仅仅到这里并不能展现出爱因斯坦求和约定的威力，为此我们还需要引入另一组基$\boldsymbol{g}_1,\boldsymbol{g}_2,...,\boldsymbol{g}_n$。

在这组新的基下，原先的坐标用上标来表示 $\boldsymbol{u}=u^i\boldsymbol{g}_i$ .

这一组基并不是任意的，而是满足$\boldsymbol{g}_i\boldsymbol{g}^j=\delta_i^j$ ，其中 $\delta_i^j$ 是Kronecker函数，当 $i=j$ 时 $\delta_i^j=1$；当 $i\neq j $ 时， $\delta_i^j=0$ .

在给定一组基 $\boldsymbol{g}^1,\boldsymbol{g}^2,...,\boldsymbol{g}^n$ 的条件下，我们可以通过线性代数的方法求解出 $\boldsymbol{g}_1,\boldsymbol{g}_2,...,\boldsymbol{g}_n$

设 $G=\begin{bmatrix}\boldsymbol{g}^1,\boldsymbol{g}^2,...,\boldsymbol{g}^n\end{bmatrix}$，则$\boldsymbol{g}_j^TG=e_j$，故把$\boldsymbol{g}_1^T,\boldsymbol{g}_2^T,...,\boldsymbol{g}_n^T$作为矩阵的行向量，可以发现这个矩阵就是$G^{-1}$，因为$G^{-1}G=I_n$.

现在来看$\boldsymbol{u}\cdot\boldsymbol{v}$，不把$\boldsymbol{v}$写成$\boldsymbol{v}=\sum_{j=1}^n v_j\boldsymbol{g}^j=v_j\boldsymbol{g}^j$，而换成新找到的一组基$\boldsymbol{v} =v^j\boldsymbol{g}_j$

于是$\boldsymbol{u}\cdot\boldsymbol{v}=u_iv^j\boldsymbol{g}^i\boldsymbol{g}_j=u_iv^i$，内积的结果就被很简单的表达出来了。

类似地也有：$\boldsymbol{u}\cdot\boldsymbol{v}=u^iv_j\boldsymbol{g}_i\boldsymbol{g}^j=u^iv_i$

### 外积

三维空间中，可以选取一组基$\boldsymbol{g}^1,\boldsymbol{g}^2,\boldsymbol{g}^3$.

​    $\boldsymbol{u}\times\boldsymbol{v}=(\boldsymbol{u}\times\boldsymbol{v})_k\boldsymbol{g}^k$ 其中，$(\boldsymbol{u}\times\boldsymbol{v})_k$指的是在基$\boldsymbol{g}^k$下的坐标。

代入$\boldsymbol{u}=u_i\boldsymbol{g}^i，\boldsymbol{v}=v_j\boldsymbol{g}^j$ 后，

​    $\boldsymbol{u}\times\boldsymbol{v}=(\boldsymbol{u}\times\boldsymbol{v})_k\boldsymbol{g}^k=u_iv_j(\boldsymbol{g}^i\times\boldsymbol{g}^j)\cdot\boldsymbol{g}^k$ 

定义Jacobian行列式为$(\boldsymbol{g}^1\times\boldsymbol{g}^2)\cdot\boldsymbol{g}^3=J$

和Levi-Civita符号$\epsilon_{ijk}=J(-1)^{\tau(ijk)}$

可以发现$\epsilon_{ijk}=(\boldsymbol{g}^i \times\boldsymbol{g}^j)\cdot\boldsymbol{g}^k$

于是$(\boldsymbol{u}\times\boldsymbol{v})_k=u_iv_j\epsilon_{ijk}$ ，可以得到由此三维矢量的外积公式。

### 三重积

三维情形下的Levi-Civita符号有如下关系：

​    $\epsilon_{pqr}\epsilon^{ijk}=\begin{vmatrix}\delta_p^i&\delta_q^i&\delta_r^i\\ \delta_p^j&\delta_q^j&\delta_r^j\\ \delta_p^k&\delta_q^k&\delta_r^k\end{vmatrix}$

当取定 $r=k$ 时，上式变为$\epsilon_{pqk}\epsilon^{ijk}=\delta_p^i\delta_q^j-\delta_p^j\delta_q^i$

对于三重积 $(\boldsymbol{u}\times\boldsymbol{v})\times\boldsymbol{w}=\boldsymbol{v}(\boldsymbol{u}\cdot\boldsymbol{w})-\boldsymbol{u}(\boldsymbol{v}\cdot\boldsymbol{w})$ ，只需要求解在上指标或者下指标下的坐标就可以证明。

为此，先计算$(\boldsymbol{u}\times\boldsymbol{v})^{k}$，再计算$((\boldsymbol{u}\times\boldsymbol{v})\times\boldsymbol{w})_p$ 令 $r=k$ 就能得出结论了。

​    $(\boldsymbol{u}\times\boldsymbol{v})^{k}=(\boldsymbol{u}\times\boldsymbol{v})\cdot\boldsymbol{g}^k=u_iv_j\epsilon^{ijk}$

​    $\begin{aligned}((\boldsymbol{u}\times\boldsymbol{v})\times\boldsymbol{w})_p&=((\boldsymbol{u}\times\boldsymbol{v})\times\boldsymbol{w})\cdot \boldsymbol{g}_p\\&=(\boldsymbol{u}\times\boldsymbol{v})^rw^q\cdot(\boldsymbol{g}_r\times\boldsymbol{g}_q)\cdot\boldsymbol{g}_p\\&=(\boldsymbol{u}\times\boldsymbol{v})^rw^q\cdot\epsilon_{rqp}\\&=u_iv_j\epsilon^{ijk}w^q\epsilon_{kqp}-u_iv_j\epsilon^{ijk}w^q\epsilon_{pqk}\\&=-u_iv_jw^q(\delta_p^i\delta_q^j-\delta_q^i\delta_p^j)\\&=u_iv_jw^q\delta_q^i\delta_p^j-u_iv_jw^q\delta_p^i\delta_q^j\\&=u_iw^iv_p-u_pv_iw^i\end{aligned}$

这样我们就得到了$(\boldsymbol{u}\times\boldsymbol{v})\times\boldsymbol{w}=\boldsymbol{v}(\boldsymbol{u}\cdot\boldsymbol{w})-\boldsymbol{u}(\boldsymbol{v}\cdot\boldsymbol{w})$
