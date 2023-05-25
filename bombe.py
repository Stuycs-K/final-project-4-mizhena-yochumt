
known = 'HEILKONSTANTINOVICH'
# For testing encoded with initial AAA, rotors 1, 2, 3, turnover
encoded = 'ILGDVKRFHTEERSNOYYJ'

'''
Known
* Initial message
* Letters don't self-map
* Internal configurations of the rotors

Need to crack (In order of implementation)
* Rotor position
* Plugboard position
* Which rotors used (assume 1, 2, 3)
* Reset point (assume Z)
'''


# Using rotors 1-8 (4th wikipedia category)
rotors = [
  [ord(c) - 65 for c in 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'],
  [ord(c) - 65 for c in 'AJDKSIRUXBLHWTMCQGZNPYFVOE'],
  [ord(c) - 65 for c in 'BDFHJLCPRTXVZNYEIWGAKMUSQO'],
  [ord(c) - 65 for c in 'ESOVPZJAYQUIRHXLNFTGKDCMWB'],
  [ord(c) - 65 for c in 'VZBRGITYUPSDNHLXAWMJQOFECK'],
  [ord(c) - 65 for c in 'JPGVOUMFYQBENHZRDKASXLICTW'],
  [ord(c) - 65 for c in 'NZJHGRCXMYSWBOUFAIVLPEKQDT'],
  [ord(c) - 65 for c in 'FKQHTLXOCBJSPDZRAMEWNIUYGV']
  ]

reflectors = [
  [ord(c) - 65 for c in 'EJMZALYXVBWFCRQUONTSPIKHGD'],
  [ord(c) - 65 for c in 'YRUHQSLDPXNGOKMIEBFZCWVJAT'],
  [ord(c) - 65 for c in 'FVPJIAOYEDRZXWGCTKUQSBNMHL']
]


known = [ord(c) - 65 for c in known]
encoded = [ord(c) - 65 for c in encoded]

for s1 in range(26):
    for s2 in range(26):
        for s3 in range(26):

            # Plugboard guess
            for p in range(26):
                used_plugs = set()
                # Test each char
                for c in range(len(known)):
                    given_in = known[c]
                    given_out = encoded[c]
                    used_plugs.add((p, given_in))
                    s1 += 1
                    s1 %= 26
                    if s1 == 25:
                        s2 += 1
                        if s2 == 25:
                            s3 += 1

                    e0 = rotors[0][(s1 + p) % 26]
                    e1 = rotors[1][(s2 + e0) % 26]
                    e2 = rotors[2][(s3 + e1) % 26]
                    r = reflectors[0][e2]
                    e3 = rotors[2][(s3 + r) % 26]
                    e4 = rotors[1][(s2 + e3) % 26]
                    e5 = rotors[0][(s1 + e4) % 26]
                    # out now maps to known character in encoded text via plugboard
                    if (e5, given_out) not in used_plugs and (given_out, e5) not in used_plugs:
                        used_plugs.add((e5, given_out))
                    else:
                        # Contradiction, try new initial plug
                        break
