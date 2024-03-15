## TEASolver_CA2024
Tiny Encryption Algorithm is the implementation. It's SEA, and we have the key, so in the end it is just a matter of reversing the process. I utilized ChatGPT to refactor a chunk of the code because I was feeling delicate and sickly at the time. It spun up a few errors, and it was also the first time using AI to generate code like this. Upon some further review it looks a bit bloaty (it could be reduced further), but it worked with some troubleshooting.

More details.

First step was to determine what algorithm we're looking at, and since TEA is a symmetric algorithm it simplifies decoding a bit. Since it's a White-Box situation, we have the code and know implementation for cryptographic primitives. We even have how it produces an initialization vector, a delta, how it does rounds, what sorts of block chonks it uses, and the key. Having all of these elements means that it is just a matter of iterating in order - it's not one way like DHE. Some of these features appear to be intentionally insecurely or haphazardly implemented here? Idk, I am a mere script kiddie. But I solved it.
