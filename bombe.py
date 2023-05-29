
known = 'HEILKONSTANTINOVICHHELLOWORLD'
# For testing encoded with initial AAA, rotors 1, 2, 3, turnover
encoded = 'ILGDVKRFHTEERSNOYYJQYBSABVSON'

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

known = [ord(c) - 65 for c in known]
encoded = [ord(c) - 65 for c in encoded]
# print(reflectors[1])

t1 = (ord('V') - 65 + 1) % 26
t2 = (ord('E') - 65) % 26



s0, s1, s2 = 0, 0, 0 # Starting position
r0, r1, r2 = 2, 1, 0 #
rf = 1

t1 = turnover[r0]
t2 = turnover[r1]

mv_2 = False
for c in range(len(known)):
    given_in = known[c]
    given_out = encoded[c]
    s0 += 1
    s0 %= 26
    if s0 == t1:
        s1 += 1
        s1 %= 26
        if s1 == t2:
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
    print(chr(e5+65), chr(given_out+65))



# for s1 in range(26):
#     for s2 in range(26):
#         for s3 in range(26):
#             # Test each char
#             for c in range(len(known)):
#                 given_in = known[c]
#                 given_out = encoded[c]
#                 s1 += 1
#                 s1 %= 26
#                 if s1 == t1:
#                     s2 += 1
#                     if s2 == t2:
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