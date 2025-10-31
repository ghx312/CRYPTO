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

![Screenshot](./images/Point_Addition.png)

When we add 2 Points of a curve together $P + Q$ , we draw a line through Points P and Q intersecting the curve again at Point R. We then take the new point R prime such that it has the same coordinates as point R, however it has the coordinates $R(x, -y)$, where Point R prime is point R flipped along the x axis. We can say that $P + Q = R$ prime.

If the 2 points are the same, $P + P$, we take the tangenet of the point, if the tangent intersects the curve again, we will do the same thing as with 2 different points. Call that point R and fliping it along the x axis. 

If the line does not intersect with the curve again, we say that it intersects with point O, which is a point located at the end of every line.

### __Point Addition Formula__

Let there be $P(x_1, y_1)$ and $Q(x_2, y_2)$ and we want to calculate $P + Q$

$-> If P = O, P + Q = Q$

$-> If Q = O, P + Q = P$

$If x_1 = x_2, y_1 = -y_2, P + Q = O$

$If P \neq Q: \lambda = \frac{y_2 - y_1}{x_2 - x_1}$

$If P = Q: \lambda = \frac{{3y^{2}}_{1} + a}{2y_1}$

$x_3 = \lambda^2 - x_1 - x_2$

$y_3 = \lambda(x_1 - x_3) - y_1$

return $(x_3, y_3)$

### __Scalar Multiplication__

Scalar Multiplication is the repeated addition of the same point n times; this is also the trapdoor function used for ECC. We are to find $n$ given $Q = [n]P$

Input: $P()$


