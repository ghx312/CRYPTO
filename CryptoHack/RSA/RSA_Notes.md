### __Modular Arithmetic Manipulation__

$a + x \equiv b + x \pmod{n}$

$a - x \equiv b - x \pmod{n}$

$a \cdot x \equiv b \cdot x \pmod{n}$

$a^x \equiv b^x \pmod{n}$

$a + b \pmod{n} \equiv a \pmod{n} + b \pmod{n}$

$ab \pmod{n} \equiv a \pmod{n} \cdot b \pmod{n}$

$a \cdot d \pmod{n} \equiv b \cdot d \pmod{n} --> a \equiv b \pmod{\frac{n}{GCD(d, n)}}$


### __Greatest Common Divisor__

When $GCD(a, b) \equiv 1$, a and b are coprime (Relatively Prime)


### __Eucild's Algorithm__
Eucild's Algorithm is used to find the GCD between 2 positive integers

Given a and b:

$a = kb + c_{1}$, where $c_{1} < b$

$b = kc{1} + c_{2}$, where $c_{2} < c_{1}$

...

$c_{n} = c_{n + 1} + 0$

The previous non-zero remainder is GCD(a, b)  


### __Euclid's Algorithm Extended Ver.__

Euclid's Extended Algorithm says that there are integers u and v such that:

$a \cdot u + b \cdot v = GCD(a, b)$

To carry out the extended version, you will need to first find the GCD(a, b) in the original version, using the equation where the remainder is the GCD(a, b)
You can rearrange the equations such that the remainder is isolated, then by using and rearranging the previous equations, you can substitute the rearranged equations and find integers u and v for a and b that fulfil the above equation.


### __Fermat's Little Theorem__

Given a and p, where p is prime and a < p

$a^{p - 1} \equiv 1 \pmod{p}$

$a^{p - 2} \equiv a^{-1} \pmod{p}$ --> Used for finding multiplicative inverse

$a^{p} \equiv a \pmod{p}$ 

In $F_{p} \equiv {0,1,2....p - 1}$ 

$∀g∈F_{p}, ∃d$ such that $g \cdot d \equiv 1 \pmod{p}$

d is known as the multiplicative inverse of g


### __Quadratic Residue__

If $∃a∈F_{p}$ for $a^{2} \equiv y \pmod{p}$ such that $0 < y < p$

y is a Quadratic Residue; otherwise, y is a Quadratic Non-Residue.

Quadratic Residue * Quadratic Residue = Quadratic Residue

Quadratic Residue * Quadratic Non-Residue = Quadratic Non-Residue

Quadratic Non-Residue * Quadratic Non-Residue = Quadratic Residue


### __Legendre Symbol__

It is only true when p is prime

$\frac{a}{p} \equiv a^(\frac{p-1}{2})$

$\frac{a}{p} \equiv 1 \pmod{p}$ a is a Quadratic Residue where $a ≢  0 \pmod{p}$

$\frac{a}{p} \equiv -1 \pmod{p}$ a is a Quadratic Non-Residue $\pmod{p}$

$\frac{a}{p} \equiv 0 \pmod{p}, a \equiv 0 \pmod{p}$


### __Tonelli-Shanks Algorithm__

This algorithm is used to find the square of the quadratic residue only when p is an odd prime and a is a quadratic residue, which can be verified using the Legendre Symbol

Algorithm:

$p - 1 = q \cdot 2^{s}$ 

Find a z such that $\frac{z}{p} = -1$

Find the following variables:

$c = z^{q} \pmod{p}$

$r = a^{\frac{p + 1}{2}} \pmod{p}$

$t = a^{q} \pmod{p}$

$m = s$

Use the found variables to iterate until $t = 1$ and smaller integer i such that $0 < i < m$ such that $t^{2^{i}} = 1$

Iteration:

$b = c^{2m + i -1} \pmod{p}$

$r = r \cdot b \pmod{p}$

$t = t \cdot b^{2} \pmod{p}$

$c = b^{2} \pmod{p}$

$m = i$

When t = 1, r is the square root of $a \pmod{p}$

When s = 1, the algorithm condenses to:

$x \equiv a^{\frac{p - 1}{4}} \pmod{p}$

### __Chinese Remainder Theorem__

This algorithm can only be used when all linear moduli are coprime

Initial Setup:

$x \equiv y_{1} \pmod{a}$

$x \equiv y_{2} \pmod{b}$

$x \equiv y_{3} \pmod{c}$

If $GCD(a, b, c) = 1$

$x \equiv b \cdot c \cdot d_{1} + a \cdot c \cdot d_{1} + b \cdot a \cdot d_{1} \pmod{a \cdot b \cdot c}$

If $x ≢  b \cdot c \pmod{a}$

Multiply $b \cdot c$ by an integer $d_{1}$ such that $x \equiv b \cdot c \cdot d_{1} \pmod{a}$

If $x ≢  a \cdot c \pmod{b}$

Multiply $a \cdot c$ by an integer $d_{2}$ such that $x \equiv a \cdot c \cdot d_{2} \pmod{a}$

If $x ≢  b \cdot a \pmod{c}$

Multiply $b \cdot a$ by an integer $d_{3}$ such that $x \equiv b \cdot a \cdot d_{3} \pmod{a}$

If x is congruent to each corresponding part, then $d_{n} = 1$

### __Euler's Totient Function__

$\varphi(p) =$ Number of x in $F_{p}$ where $GCD(p ,x) = 1$

$b^{\varphi(m)} \equiv 1 \pmod{m}$, where $GCD(b, m) = 1$

$\varphi(pq) = (p - 1)(q - 1)$

### __Binomial Expansion__

Given $N = p \cdot q$ and $(p + q)^{e} \pmod{N}$

$(p + q)^{e} \equiv p^{e} + q^{e} \pmod{N}$

### __RSA Explained__

Choose 2 large primes p and q that are about the same length

$N = p \cdot q$

Choose a Public exponent e such that:

$1 < e < \varphi(N), GCD[e, \varphi(N)] = 1$

Calculate Private exponent, d:

$d \cdot d \equiv 1 \pmod{\varphi(N)}$

### __RSA's G.E.D__

G: e, d <-- $1 < e < \varphi(N), GCD[e, \varphi(N)] = 1, d \cdot e \equiv 1 \pmod{\varphi(N)}$

E: C <-- $C \equiv M^{E} \pmod{N}, 0 <= M < N$

D: M <-- $M \equiv C^{d} \pmod{N}$

To solve RSA, we need to find $\varphi(N)$ which can be derived from p and q as $\varphi(N) = (p - 1)(q - 1)$

### __Quadratic Equations__

$\varphi(N) = (p - 1)(q - 1) = pq - (p + q) - 1 = N - (p + q) + 1$

Hence, $p + q = N - \varphi(N) + 1$

Let us consider the quadratic equation where p and q are its roots:

$(x - p)(x - q) = 0$

We get the following equation:

$x^{2} - (p + q)x + pq = 0$

$x^{2} - (N - \varphi(N) + 1)x + N = 0$

If the value of $\varphi(N)$ is correct, the results of the final equation would be a whole number, giving us the factors of N.

### __Simple Continued Fraction/Wiener's Attack__

$\varphi(N) = (p - 1)(q - 1) = N - (p + q) + 1$ which can be estimated as N as $p + q$'s value is very small when compared to $p \cdot q$

Since we know that $∃k>0, k∈ℤ$ for $e \cdot d = k \cdot \varphi(N) + 1, hence

$\frac{e}{\varphi(N)} - \frac{k}{d} = \frac{1}{d \cdot \varphi(N)}$ since the value of $d \cdot \varphi(N)$ is large, the value of $\frac{1}{d \cdot \varphi(N)}$ can be estimated as 0

This allows us to estimate $\frac{e}{N} = \frac{k}{d}$

We know that $e \cdot d \equiv 1 \pmod(\varphi(N))$, $\varphi(N) \equiv 0 \pmod(0)$ and $d \equiv 1 \pmod(\varphi(N))$. 

We will skip the verification process for all values of d that are even

Since $\varphi(N)$ is a whole number, if $\frac{e \cdot d - 1}{k}$ is not a whole number, we will also skip that value

We can use Euclid's Algorithm to find cases for which all of these are true. We will then use Quadratic Equations to verify that $\varphi(N)$ has integer solutions

Wiener's Attack will be successful if:

$q < p < 2q$ and $d <= \frac{1}{3} \sqrt[4]{N}$

May be successful if:

$d > \frac{1}{3} \sqrt[4]{N}$















