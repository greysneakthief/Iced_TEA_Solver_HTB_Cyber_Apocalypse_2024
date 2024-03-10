## TEASolver_CA2024
Tiny Encryption Algorithm was used in the encryption. SEA, and we have the key, so in the end it was just a matter of reversing the process. Utilized ChatGPT to refactor a large portion of the code, because I'm delicate and sickly. It spun up a few errors but it was the first time using AI to generate code like this. Upon some further review it looks a bit bloaty, but it worked with some troubleshooting and standard cryptographic modules.

Details and comments as I understood them at the time:

First step was to determine what algorithm we're looking at, and since TEA is a symmetric algorithm it simplifies decoding a bit. Being Canadian I instantly realized the hint was referring to the blocking function - igloo building is in my blood (perhaps not as 'mystical' as the description hint), so did some referencing to block ciphers and TEA matched...just like the name of the challenge.

Since it's a White-Box situation, we have the code and know implementation for cryptographic primitives. We even have how it produces an initialization vector, a static delta, how it does Feistel rounds, what sorts of blocking it does, and the key. Having all of these elements means that it is just a matter of reversing the process symmetrically for each portion. Some of these features appear to be intentionally insecurely or haphazardly implemented here? Idk, I am a mere script kiddie but a static delta seems really insecure.
