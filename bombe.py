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

turnover = [
  'Q',
  'E',
  'V',
  'J',
  'Z',
  'ZM',
  'ZM',
  'ZM'
  ]



def pass_through(s0, s1, s2, r0, r1, r2, rf, t0, t1, known):
    out = ''
    mv_2 = False
    for c in range(len(known)):
        given_in = known[c]
        s0 += 1
        s0 %= 26
        if s0 == t0:
            s1 += 1
            s1 %= 26
            if s1 == t1:
                mv_2 = True
        if mv_2:
            s1 += 1
            s2 += 1
            mv_2 = False

        e0 = (rotors[r0][(s0 + given_in) % 26] - s0) % 26
        e1 = (rotors[r1][(s1 + e0) % 26] - s1)%26
        e2 = (rotors[r2][(s2 + e1) % 26] - s2)%26
        # print(chr(e2+65+s2))
        r = reflectors[rf][e2 % 26]
        # print(r)
        e3 = (rotors[r2].index((s2 + r) % 26) - s2)%26
        # print(chr(e2+65-s2))
        e4 = (rotors[r1].index((s1 + e3) % 26) - s1)%26
        e5 = (rotors[r0].index((s0 + e4) % 26) - s0) % 26

        # print(chr(given_in+65), s2, s1, s0)
        # print(''.join([chr(i+65) for i in [e0, e1, e2, r, e3, e4, e5]]))
        out += chr(e5+65)
    return out




known = 'HEILKONSTANTINOVICHHELLOWORLD'
known = [ord(c) - 65 for c in known]

s2, s1, s0 = 3, 3, 18  # Starting position
r2, r1, r0 = 3, 1, 2  # Rotor choice
rf = 1  # Reflector choice
t0 = (ord(turnover[r0]) - 65 + 1) % 26 # Turnover pos
t1 = (ord(turnover[r1]) - 65) % 26

encoded = pass_through(s0, s1, s2, r0, r1, r2, rf, t0, t1, known)
print(''.join([chr(i+65) for i in known]), encoded)

encoded = [ord(c) - 65 for c in encoded]

# pass_through(s0, s1, s2, r0, r1, r2, rf, t0, t1, known, encoded)


for s0 in range(26):
    for s1 in range(26):
        for s2 in range(26):
            s00, s11, s22 = s0, s1, s2
            # Test each char
            mv_2 = False
            for c in range(len(known)):
                given_in = known[c]
                given_out = encoded[c]
                s00 += 1
                s00 %= 26
                if s00 == t0:
                    s11 += 1
                    s11 %= 26
                    if s11 == t1:
                        mv_2 = True
                if mv_2:
                    s11 += 1
                    s22 += 1
                    mv_2 = False

                e0 = (rotors[r0][(s00 + given_in) % 26] - s00) % 26
                e1 = (rotors[r1][(s11 + e0) % 26] - s11) % 26
                e2 = (rotors[r2][(s22 + e1) % 26] - s22) % 26
                # print(chr(e2+65+s2))
                r = reflectors[rf][e2 % 26]
                # print(r)
                e3 = (rotors[r2].index((s22 + r) % 26) - s22) % 26
                # print(chr(e2+65-s2))
                e4 = (rotors[r1].index((s11 + e3) % 26) - s11) % 26
                e5 = (rotors[r0].index((s00 + e4) % 26) - s00) % 26

                if given_out != e5:
                    # print(given_out, e5)
                    break
                elif c == len(known)-1:
                    print(s0, s1, s2)
                    exit()