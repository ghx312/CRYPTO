Lecture 1
Adversary: (Unbounded Computationally, Eavesdropper)
The adversary is the identity of the person who is trying to figure out your message.
It is essential to identify your adversary so that you can determine the computational power and time they have to break your encryption algorithm. (Usually, the assumption that your adversary has unbounded power, meaning that they have unlimited computational power and space)

There are 2 types of adversaries:
Adversary EVE, where the adversary can only listen in on all the information
EVE(), is a function that gives an output based off the PPT, c and m’s given
Adversary Active (Mallory), where the adversary can forge or alter messages

What does the adversary know?
Kerrcoff’s Law: The adversary knows G.E.D (Has full knowledge of the algorithm)
Ciphertext only: The adversary can only know c, which is passed through insecure channels/public channels

What does the adversary not know?
The adversary does not know the state that G() was run in (The random state that was used to get sk), they do not know sk for E() and sk for D()

Why does the adversary know?
It is safer to assume that the adversary knows and allows you to prove that your encryption algorithm is secure in the worst-case scenario. In real life, if an algorithm is safe, it would be widely implemented, thereby greatly reducing the likelihood that the adversary does not know G.E.D.

What do we want from an encryption algorithm:
The adversary should not be able to compute the plaintext from ciphertexts
The adversary should not be able to compute any partial information about the plaintext from the ciphertext.(Perfect Secrecy)
The adversary should not be able to compute relations between ciphertexts. (Perfect indistinguishability, also the vulnerability that led to the downfall of the Enigma machine)

Reduction/Reduced Algorithm:
Reduction is the act of condensing an algorithm to its mathematical problem, whether it be a computationally hard problem of factoring large integers or discrete logarithms 

The reduced algorithm is the underlying mathematical problem that needs to be solved to “crack” the algorithm

Basics: Functions of an encryption algorithm:
G(1k) - Randomised algorithm that produces the sk (Secret key) of k length (k=l)
E(sk,m)=c - Algorithm that encrypts the m (Plaintext)
D(sk, c)=m, - Algorithm that decrypts the c (Ciphertext) 
Correctness: When the ciphertext is run through the Decryption function with the sk, you will obtain the original message
Security: The ciphertext reveals nothing useful to the adversary
K = {Set of all Keys}, C = {Set of all Ciphertexts}, M = {Set of all Plaintexts}

Perfect Secrecy (Shannon’s Secrecy Definition):
C is all possible ciphertexts, M is all possible messages 
 probability distribution over M
c in C, m in M
P(M=m)=P(M=m|C=c) or P(M=m)=P(M=m|E(sk,m)=c)
If an algorithm has perfect secrecy, the chance that the adversary guesses the non-zero probability of m is equal to the chance that the adversary guesses the non-zero probability of m when they know c.

In simple terms, the ciphertext, c, does not give out any information on what the plaintext, m, is.

Perfect Indistinguishability:
m, m, in M
c in C
P(C=c|M=m)=P(C=c|M=m,)
If an algorithm has perfect indistinguishability, it means that there is an equal chance between all messages that the ciphertext, when decoded, can be.

In simple terms, when the adversary has the ciphertext, there is an equal chance that the ciphertext is m1 , and m2 
E.g c = oadbwyeifabo, m1 = hello, m2 =  你好 P(M=m1)=P(M=m2)
It does not matter which language, datatype or length of the message or ciphertext, c has an equal chance of being any of m. It does not allow the adversary to deduce any information about the contents of the message. 

If an algorithm satisfies Perfect Indistinguishability, it also satisfies Perfect Secrecy, vice versa. (In practice, OTP is the only useful algorithm that achieves this)

One-Time Pad: (Encryption System)
m1,c,sk  {0,1}l is the security parameter
(Security parameter is the possible type of input, key and output for this encryption system, in this case it is 0 and 1, which is binary, where l is the length of the message)
G(1l) chooses sk at random {0,1}l 
E(sk, m)=skm=c
D(sk, c)=skc=m

This encryption scheme achieves Perfect Secrecy as there is only 1 key to a message that matches a predetermined ciphertext, vice versa, making all messages and ciphertexts equally likely, achieving Perfect Secrecy

Proof:
Fix m, c {0,1}l 
P(C=c)=PSK(SKm=c)=PSK(SK=mc)=12l
Thus, c, m1,m2
PSK(C=c|M=m1)=PSK(C=c|M=m2) (Perfect Indistinguishability)
Since One-Time Pad G.E.D achieves Perfect Indistinguishability, Perfect Secrecy

In simple terms, m and c can only be 1 or 0, for the length of the message. The probability that any c is equivalent to a predetermined c is 12l as there are 2 possible states for each digit of sk and sk has a length of l.
Since skm=c, there is only 1 possible sk when XORed with a predetermined m gives c, hence the probability that any sk when XORed with a predetermined m gives c is the same as 12l.
Following XOR logic, we can determine that PSK(SK=mc)=12l as there is only 1 possible option of sk when predetermined m XOR c
Thus, PSK(m1SK=c)=PSK(m2SK=c), as P(SKc=m) are equal for all possible SK.
Since One-Time Pad G.E.D achieves Perfect Indistinguishability, Perfect Secrecy


Why a One-Time Pad can only be used once (Without changing sk):
Proof:
Consider the case that 2 messages of length l, each encrypted using the same sk 
Let m=m1m2 ,m,=m1,m2, ,c=c1c1 where m1=m2 and m1,m2, , since the ciphertext is made up of 2c1, due to XOR logic, we know that the first half and second half of the plaintext is the same, since we know that m1,m2, , we can deduce that PSK(m,sk=c)=0 as there is no sk that can XOR 2 different messages into the same ciphertext, while we know that PSK(msk=c)>0, as there is a sk that can XOR 2 same messages into the same ciphertext. Since Perfect Indistinguishability requires P(C=c|M=m)=P(C=c|M=m,) , and we know that PSK(msk=c)PSK(m,sk=c) this shows that if One-Time Pad is used twice (without changing sk), it will not have Perfect Indistinguishability. 
