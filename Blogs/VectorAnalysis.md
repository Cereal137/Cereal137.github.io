---
title: 矢量分析
date: 2021-11-30 12:43:27
categories: 物理学习
tags:
---
## Vector Triple Product

#### 不引入坐标，试证明：$(\vec{a}\times \vec{b}) \times \vec{c}=(\vec{a} \cdot \vec{c})\vec{b}-(\vec{b} \cdot \vec{c})\vec{a}$ 

#### 证明：

​    由于$(\vec{a}\times \vec{b})\times \vec{c} \perp (\vec{a}\times \vec{b})$ ，可以得到 $(\vec{a}\times \vec{b}) \times \vec{c}$ 的结果在 $\vec{a}$ 和 $\vec{b}$ 构成的平面上，可以设:

​            $(\vec{a}\times \vec{b})\times \vec{c}=X\vec{a}+Y\vec{b}$

​    同时，$(\vec{a}\times \vec{b})\times \vec{c} \perp \vec{c}$ ，把上式左右同时点乘 $\vec{c}$ 于是得到：

​            $(X\vec{a}+Y\vec{b})\cdot \vec{c}=0$

​            $X\vec{a}\cdot \vec{c}=-Y\vec{b}\cdot \vec{c}$

​    这一步的观察比较关键，由于 $\vec{a},\vec{b},\vec{c}$ 的选择是任意的，于是两边的系数项$X$，$Y$要满足如下条件：

​            $\begin{cases}X=-C(\vec{a},\vec{b},\vec{c})\cdot(\vec{b} \cdot \vec{c})\\Y=C(\vec{a},\vec{b},\vec{c})\cdot(\vec{a} \cdot \vec{c})\end{cases}$

​    其中，$C(\vec{a},\vec{b},\vec{c})$是关于 $\vec{a},\vec{b},\vec{c}$ 的系数，对于同一组 $\vec{a},\vec{b},\vec{c}$ ，$C(\vec{a},\vec{b},\vec{c})$ 输出唯一的常数.

​    于是把结果进一步写为：

​        $(\vec{a}\times \vec{b})\times \vec{c}=-C(\vec{a},\vec{b},\vec{c})\cdot(\vec{b} \cdot \vec{c})\vec{a}+C(\vec{a},\vec{b},\vec{c})\cdot(\vec{a} \cdot \vec{c})\vec{b}=C(\vec{a},\vec{b},\vec{c})\cdot((\vec{a} \cdot \vec{c})\vec{b}-(\vec{b}\cdot\vec{c})\vec{a})$

​    那么只需要求解 $C$ 了。特殊地，先考虑 $\vec{c}=\vec{a}$ 的情形，这时：

​        $(\vec{a}\times \vec{b})\times \vec{a}=C(\vec{a},\vec{b},\vec{a})\cdot((\vec{a} \cdot \vec{a})\vec{b}-(\vec{a}\cdot\vec{b})\vec{a})$

​    这一步在上式左右两边同时点乘 $\vec{b}$ ，再利用三矢量的混合积公式，得到了：

​        $(\vec{a}\times \vec{b})\cdot(\vec{a}\times \vec{b})=C(\vec{a},\vec{b},\vec{a})\cdot((\vec{a} \cdot \vec{a})(\vec{b}\cdot\vec{b})-(\vec{a}\cdot\vec{b})(\vec{a}\cdot\vec{b}))$

​    现在可以约去两边的模方，得到 $\sin^2\theta=C(\vec{a},\vec{b},\vec{a})\cdot(1-\cos^2\theta)$ ，其中 $\theta$ 为 $\vec{a}$ 与 $\vec{b}$ 的夹角。

​    显然有 $C(\vec{a},\vec{b},\vec{a})=1$ ，先记下这个结论。

​    接下来考虑普遍的情形：

​        $((\vec{a}\times \vec{b})\times \vec{c})\cdot\vec{a}=C(\vec{a},\vec{b},\vec{c})\cdot((\vec{a} \cdot \vec{c})(\vec{b}\cdot\vec{a})-(\vec{b}\cdot\vec{c})(\vec{a}\cdot\vec{a}))$

​    再使用三矢量的混合积，有

​        $(\vec{a}\times(\vec{a}\times \vec{b}))\cdot\vec{c}=-((\vec{a}\times \vec{b})\times\vec{a})\cdot\vec{c}=-(\vec{a} \cdot \vec{a})(\vec{b}\cdot\vec{c})+(\vec{a}\cdot\vec{b})(\vec{a}\cdot\vec{c})$

​    比较两式右侧，可以得到 $C(\vec{a},\vec{b},\vec{c})=1$.

​    最后，我们就成功证明了$(\vec{a}\times \vec{b}) \times \vec{c}=(\vec{a} \cdot \vec{c})\vec{b}-(\vec{b} \cdot \vec{c})\vec{a}$ .

#### 一道练习题

#### 用上述方法证明：The Schwarz inequality $\lvert\vec{a}\cdot\vec{b} \rvert \leq \lvert \vec{a} \rvert \lvert \vec{b}\rvert$

#### 证明：

​    $\lvert{\vec{a}\times\vec{b}}\rvert^2\geq0\iff(\vec{a}\times\vec{b})\cdot(\vec{a}\times\vec{b})\geq0$

​    使用三矢量的混合积：

$(\vec{a}\times\vec{b})\cdot(\vec{a}\times\vec{b})=\vec{b}\cdot((\vec{a}\times\vec{b})\times\vec{a})=\vec{b}\cdot(\vec{b}(\vec{a}\cdot\vec{a})-\vec{a}(\vec{a}\cdot\vec{b}))=(\vec{a}\cdot\vec{a})(\vec{b}\cdot\vec{b})-(\vec{a}\cdot\vec{b})(\vec{a}\cdot\vec{b})\geq0$

​    从而有： $(\vec{a}\cdot\vec{a})(\vec{b}\cdot\vec{b})\geq(\vec{a}\cdot\vec{b})(\vec{a}\cdot\vec{b})$. 即$\lvert \vec{a}\cdot\vec{b}\rvert \leq\lvert\vec{a}\rvert \lvert \vec{b}\rvert$.
