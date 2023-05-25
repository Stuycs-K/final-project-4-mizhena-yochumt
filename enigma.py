

rotors = [
  [*'EKMFLGDQVZNTOWYHXUSPAIBRCJ'],
  [*'AJDKSIRUXBLHWTMCQGZNPYFVOE'],
  [*'BDFHJLCPRTXVZNYEIWGAKMUSQO'],
  [*'ESOVPZJAYQUIRHXLNFTGKDCMWB'],
  [*'VZBRGITYUPSDNHLXAWMJQOFECK'],
  [*'JPGVOUMFYQBENHZRDKASXLICTW'],
  [*'NZJHGRCXMYSWBOUFAIVLPEKQDT'],
  [*'FKQHTLXOCBJSPDZRAMEWNIUYGV']
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

reflectors = [
  [*'EJMZALYXVBWFCRQUONTSPIKHGD'],
  [*'YRUHQSLDPXNGOKMIEBFZCWVJAT'],
  [*'FVPJIAOYEDRZXWGCTKUQSBNMHL']
]
# A set of plugs is represented as a string i.e. "AQ"
plugboard = ['AD']

def plugs(input, plugs):
  input = input.upper()
  out = ''
  for letter in input:
    found = False
    for plug in plugs:
      if letter in plug:
        found = True
        if plug.index(letter) == 0:
          out += plug[1]
        else:
          out += plug[0]
        break
    if not found:
      out += letter
  return out

def shift(let, offset):
  num = ord(let)
  shift = ord(offset) - ord('A')
  if num + shift > ord('Z'):
    return chr(ord('A') + ((num + shift - ord('A')) % 26))
  return chr(num + shift)

def shift_reverse(let, offset):
  num = ord(let)
  shift = ord(offset) - ord('A')
  if num - shift < ord('A'):
    return chr(num - shift + 26)
  return chr(num - shift)

def rotate(rotor, input):
  return rotors[rotor][ord(input) - ord('A')]

def rotate_reverse(rotor, input):
  return chr(rotors[rotor].index(input) + ord('A'))

def reflect(reflector, input):
  return reflectors[reflector][ord(input) - ord('A')]

def rotor(input, r1, r2, r3, setting, ref):
  out = ''
  r1 -= 1
  r2 -= 1
  r3 -= 1
  ref -= 1
  for letter in input:
    if not letter.isalpha():
      out += letter
      continue
    if (setting[2] in turnover[r3] and setting[1] in turnover[r2]):
      setting[1] = shift(setting[1], 'B')

    if (setting[1] in turnover[r2]):
      setting[0] = shift(setting[0], 'B')

    setting[2] = shift(setting[2], 'B')

    print(f'\n{setting[0]} {setting[1]} {setting[2]}')

    letter = shift(letter, setting[2])
    letter = rotate(r3, letter)
    letter = shift_reverse(letter, setting[2])
    # print(f'Wheel 3: {letter}')

    letter = shift(letter, setting[1])
    letter = rotate(r2, letter)
    letter = shift_reverse(letter, setting[1])
    # print(f'Wheel 2: {letter}')

    letter = shift(letter, setting[0])
    letter = rotate(r1, letter)
    letter = shift_reverse(letter, setting[0])
    # print(f'Wheel 1: {letter}')

    letter = reflect(ref, letter)
    # print(f'Reflector: {letter}')

    letter = shift(letter, setting[0])
    letter = rotate_reverse(r1, letter)
    letter = shift_reverse(letter, setting[0])
    # print(f'Wheel 1: {letter}')

    letter = shift(letter, setting[1])
    letter = rotate_reverse(r2, letter)
    letter = shift_reverse(letter, setting[1])
    # print(f'Wheel 2: {letter}')

    letter = shift(letter, setting[2])
    letter = rotate_reverse(r3, letter)
    letter = shift_reverse(letter, setting[2])
    # print(f'Wheel 3: {letter}')

    out += letter
  return out

setting = ['D', 'D', 'S']

message = "ABCDEFGHIJKLMNOP".upper()

# message = plugs(message, plugboard)

# for i in range(0, 26):
#     print(f'D reverse shifted by {i} = {shift_reverse("D", chr(ord("A") + i))}')
#
# for i in range(0, 26):
#     print(f'D shifted by {i} = {shift("D", chr(ord("A") + i))}')

out = rotor(message, 4,2,3, setting, 2)
print(out)

# message = plugs(message, plugboard)
