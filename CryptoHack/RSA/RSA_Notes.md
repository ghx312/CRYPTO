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

Given a and p where p is prime and a < p

$a^{p - 1} \equiv 1 \pmod{p}$

$a^{p - 2} \equiv a^{-1} \pmod{p}$

$a^{p} \equiv a \pmod{p}$

In $F_{p} \equiv {0,1,2....p - 1}$, $ \forall g\ \in F_{p}, \exists d\ s.t g \cdot d \equiv 1 \pmod{p}$




