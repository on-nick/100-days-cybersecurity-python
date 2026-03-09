### What I Learned

* Token randomness can be measured using entropy.
* Low entropy often indicates predictable or weak tokens.
* Python’s `math.log2()` and `collections.Counter` make entropy calculations straightforward.
* Even simple scripts can help identify potential security weaknesses in authentication systems.

### What I Built

* A Python script that reads tokens from a file and analyzes their entropy.
* The script calculates the entropy of each token and flags tokens with low randomness.
* It classifies tokens into **alerts** (very low randomness) and **warnings** (possibly weak).

### What Failed

* Initially, some tokens caused unexpected results because empty lines were included in the analysis.
* File loading also failed when the specified token file did not exist.

### How I Fixed It

* Added filtering to remove empty lines while reading the token file.
* Implemented a try/except block to handle missing files gracefully and prevent the program from crashing.

### Security Insight

Low-entropy tokens are easier for attackers to guess or brute-force. Systems that rely on predictable tokens—such as weak session IDs or API keys—can be vulnerable to unauthorized access. Regularly analyzing token randomness can help identify weak implementations and improve overall security.
