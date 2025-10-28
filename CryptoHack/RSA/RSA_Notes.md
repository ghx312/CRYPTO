RSA Course on CryptoHack

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



