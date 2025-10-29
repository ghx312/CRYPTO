### __RSA Revision__

Python: pow(base, exponent, modulus)

Encryption: $c = m^{e} \pmod{N} $

Euler's Totient Function: $\varphi(N) = (p - 1)(q - 1)$

Modular Multiplicative Inverse: $d \equiv e^{-1} \pmod{\varphi(N)}$

Decryption: $m = c^{d} \pmod{N}$, $N = p \cdot q$

### __RSA Signing__

Sender:

$c = m^{e_{0}} \pmod{N}$, encrypt the messagin using the your friend's public key

$H(m)$ is a function to calculate the Hash of the original message; each hash is unique for every message. We will use this to ensure that the receiver knows if the message has been tampered with.

$S = H(m)^{d_{1}} \pmod{N}$, encrypt the hash of the original message with your private key

Reciever:

$m = c^{e_{1}} \pmod{N}$, decrypt the message using your private key

$s = S^{d_{0}} \pmod{N}$, decrypt the hash of the original message with your friend's public key

If $H(m) = s$, the message is the original

### __Diffie-Hellman Key Exchange__

Diffie-Hellman Key Exchange is a method used to generate the same key for 2 individuals without even meeting up. Alice and Bob both agree on a public base $g$ and a public modulus $p$. They then each choose a private exponent, a and b

They will then both calculate this:

$g^{a} \pmod{p}$ --> Alice

$g^{b} \pmod{p}$ --> Bob

This information is then passed to the other person through a public server

When they both receive the new information, they will apply their private exponent to the received new secret key without even having to meet up

$SK = g^{ab} \pmod{p}$

This key exchange works on the fact that for every element in $F_{p}$ where p is prime, for all non-zero elements, there exists an $x$ where $x \cdot x^{-1} \equiv 1 \pmod{p}$. This allows us to easily calculate inverses when doing modulo math.


### __Generators__

Generators, $g$, are elements in $F_{p}$ such that there is a subgroup $H = {g, g^{2},...,g^{p - 1}}$

Where all the elements in $F_{p}$ can be written as $g^{n} \pmod{p}$ for some integer $n < p$

Finding Generators:

$\varphi(n) = p - 1 = \prod {q_i}^{k_n}$

$g^\frac{\varphi(n)}{q_{i}} \pmod{n}$

In simple terms, separate the totient of p into its prime factors, then check using the second algorithm below, if none of the answers are 1, $g$ is a generator of $\pmod{p}$


### __Man-In-The-Middle__

Man-in-the-Middle is when you intercept and change the information between Alice and Bob. This is how to break Diffie-Hellman using a MITM attack.

Alice will send you g, p and A where $A = g^{a} \pmod{p}$, where a is Alice’s secret exponent

You will now need to send this information to Bob, however, you can manipulate it such that you are able to disconnect the Diffie-Hellman Key between both of them and make it such that you have a secret symmetrical key between Alice, you and Bob.

Create a secret exponent m.

Calculate:

$M = g^{m} \pmod{p}$ and send g, p and M to Bob

Bob will then send you B, where $B = g^{b} \pmod{p}$ where, b is Bob’s secret exponent

You will now need to send M to Alice. Alice will think that M is B, but it’s actually not.

You now have a secret key between you and Alice, $SK_{Alice} = A^{m} \pmod{p} = g^{am} \pmod{p}$

Alice will then attempt to send a message to Bob, giving you the IV and the Encrypted message. You can plug all the values into this MITM_Decrypt.py and read the secret message.

If you wish to stay hidden, you can also encrypt the message using the key you have with Bob, taken by $SK_{Bob} = B^{m} \pmod{p} = g^{bm} \pmod{p}$, using MITM_Encrypt.py

In the unfortunate case that you are only able to manipulate a little bit of the communication, for example, the number of bits they are going to use for the Diffie-Hellman, you are able to put in vulnerabilities that allow you to brute-force.

Using: 

from sympy.ntheory.residue_ntheory import * 

a = discrete_log(p, A, g) 

This imported function helps to solve small discrete logs

This is usable for primes $< 2^{64}$ or about 20 digits


### __Baby-Step-Giant-Step__

p is prime

Algorithm:

$A = g^{x} \pmod{p} = g^{x_1 \cdot + x_2}$

$m = Ceiling(\sqrt{p})$ (Round up to nearest Integer)

$A \cdot g^{-x_2} = (g^{m})^{x_1}$

$x = x_1 + x_2$

Baby Steps:

Make a table containing the values of $g^{x_2}$ where $x_{2}∈${$0, 1, 2, 3,..., m - 1$}

Giant Steps:

Calculate the giant step multiplier: $g^{-m} \cdot g^{m} \equiv 1 \pmod{p}$

Compute $A \cdot (g^{-m})^{x_1}$, where $x_1 ∈ {0, 1, 2,..., m - 1}$

When $A \cdot (g^{-m})^{x_1} \equiv_{p} g^{x_2}$, $x = x_1 + x_2$

Efficiency:

Time Complexity: $O(\sqrt{p})$

Space Complexity: $O(\sqrt{p})$

Works efficiently for $p < 2^{50}$ or about 16 digits

### __Pollard's Rho__

The algorithm uses the equation, $x_i = g^{a_i} \cdot A^{b_i}$

There is a pseudorandom algorithm that generates values a and b such that 

$a_i, b_i, \neq a_j, b_j$ and $g^{a_j} \cdot g^{b_j} = x_j = x_i = g^{a_i} \cdot g^{b_i}$

Using this equation, $a_i + b_i \cdot x = a_j + b_j \cdot x$, we can solve for x

$x = \frac{a_j - a_i}{b_j - b_i}$

Efficiency:

Time Complexity: $O(\sqrt{p})$

Space Complexity: $O(1)$

Works efficiently for $p < 2^{60}$ ~ $2^{80}$, or about 18 to 24 digits.
