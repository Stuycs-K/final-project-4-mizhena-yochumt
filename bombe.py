
known = 'Heil Konstantinovich'

'''
Known
* Initial message
* Letters don't self-map
* Internal configurations of the rotors

Need to crack (In order of implementation)
* Rotor position
* Plugboard position
* Which rotors used (assume 1, 2, 3)
* Reset point (assume A)
'''


# Using rotors 1-8 (4th wikipedia category)
rotors = [
    {chr(65+i): 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'[i] for i in range(26)},
    {chr(65+i): 'AJDKSIRUXBLHWTMCQGZNPYFVOE'[i] for i in range(26)},
    {chr(65+i): 'BDFHJLCPRTXVZNYEIWGAKMUSQO'[i] for i in range(26)},
    {chr(65+i): 'ESOVPZJAYQUIRHXLNFTGKDCMWB'[i] for i in range(26)},
    {chr(65+i): 'VZBRGITYUPSDNHLXAWMJQOFECK'[i] for i in range(26)},
    {chr(65+i): 'JPGVOUMFYQBENHZRDKASXLICTW'[i] for i in range(26)},
    {chr(65+i): 'NZJHGRCXMYSWBOUFAIVLPEKQDT'[i] for i in range(26)},
    {chr(65+i): 'FKQHTLXOCBJSPDZRAMEWNIUYGV'[i] for i in range(26)},
    ]

