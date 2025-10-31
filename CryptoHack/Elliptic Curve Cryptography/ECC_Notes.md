### __Introduction__

Elliptic Curves are defined by an equation, also known as the Weierstrass Equations

$y^{2} = x^{3} + ax + b$

However, in ECC, we treat valid curves as a set of points on a graph, we can define this as shown.

$E(F_{p}) = (x, y): x, y ∈ F_{p}$ satisfying $y^{2} = x^{3} + ax +b ∪ O$

This simply means that the "Elliptic Curve" that we are looking at contains points that have coordinates such that they are within the set $F_{p}$ that still satisfies the equation of the "curve" $y^{2} = x^{3} + ax + b$ + O at the point at infinity or the additive inverse.

__Reduction/Trapdoor Function__

The hardness of ECC comes from its reduction, where,

Given points $Q, P$ find $n$ such that $Q = [n]P$

__Identity Element__

The identity element of an elliptic curve is the point O, where

$P + O = P$

$P + (-P) = O$

__Point Addition Properties__

$P + O = O + P = P$

$P + (- P) = O$

$(P + Q) + R = P + (Q + R)$ (Associative)

$P + Q = Q + P$ (Commutative)

__Limitations__

All elliptic curves in ECC must fulfil this equation $4a^{3} + 27b^{2} \neq 0$, this equation shows that the elliptic curve does not have a singularity point, meaning that there are no repeated roots for this equation, for reapeated roots can compromise the security of the ECC.

### __Point Negation__

Point Negation is about calculating the inverse of a specific point on an ECC valid curve. To negate a point, we require its x and y coordinates and the modulus of the equation. We can do so using this equation:

$P(x, y) = Q(x, p - y)$ -> $P + Q = O$

### __Point Addition__

![Screenshot](../images/PointAddition.png)

