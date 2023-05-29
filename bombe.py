
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


turn1 = ord('Q')-65
turn2 = ord('E')-65


turn1 = ord('Q')-65
turn2 = ord('E')-65
s0, s1, s2 = 0, 0, 0
for c in range(len(known)):
    given_in = known[c]
    given_out = encoded[c]
    s0 += 1
    s0 %= 26
    if s0 == turn1:
        s1 += 1
        s1 %= 26
        if s1 == turn2:
            s2 += 1
            s2 %= 26

    e0 = rotors[2][(s0 + given_in) % 26] - s0
    e1 = rotors[1][(s1 + e0) % 26] - s1
    e2 = rotors[0][(s2 + e1) % 26] - s2
    r = reflectors[1][e2 % 26]
    e3 = rotors[0][(s2 + r) % 26] - s2
    e4 = rotors[1][(s1 + e3) % 26] - s1
    e5 = (rotors[2][(s0 + e4) % 26] - s0) % 26
    print(chr(e5+65), chr(65+given_out))

# for s1 in range(26):
#     for s2 in range(26):
#         for s3 in range(26):
#             # Test each char
#             for c in range(len(known)):
#                 given_in = known[c]
#                 given_out = encoded[c]
#                 s1 += 1
#                 s1 %= 26
#                 if s1 == turn1:
#                     s2 += 1
#                     if s2 == turn2:
#                         s3 += 1
#
#                 e0 = rotors[2][(s1 + given_in) % 26]-s1
#                 e1 = rotors[1][(s2 + e0) % 26]-s2
#                 e2 = rotors[0][(s3 + e1) % 26]-s3
#                 r = reflectors[0][e2]
#                 e3 = rotors[0][(s3 + r) % 26] - s3
#                 e4 = rotors[1][(s2 + e3) % 26] - s2
#                 e5 = rotors[2][(s1 + e4) % 26] - s1
#
#                 if given_out != e5:
#                     break
#                 elif c == len(known)-1:
#                     print(s1, s2, s3)
#                     exit()