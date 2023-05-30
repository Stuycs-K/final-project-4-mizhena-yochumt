
rotors = [
  list('EKMFLGDQVZNTOWYHXUSPAIBRCJ'),
  list('AJDKSIRUXBLHWTMCQGZNPYFVOE'),
  list('BDFHJLCPRTXVZNYEIWGAKMUSQO'),
  list('ESOVPZJAYQUIRHXLNFTGKDCMWB'),
  list('VZBRGITYUPSDNHLXAWMJQOFECK'),
  list('JPGVOUMFYQBENHZRDKASXLICTW'),
  list('NZJHGRCXMYSWBOUFAIVLPEKQDT'),
  list('FKQHTLXOCBJSPDZRAMEWNIUYGV')
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
  list('EJMZALYXVBWFCRQUONTSPIKHGD'),
  list('YRUHQSLDPXNGOKMIEBFZCWVJAT'),
  list('FVPJIAOYEDRZXWGCTKUQSBNMHL')
]
# A set of plugs is represented as a string i.e. "AQ"
plugboard = []

# def plugs(input, plugs):
#   input = input.upper()
#   out = ''
#   for letter in input:
#     found = False
#     for plug in plugs:
#       if letter in plug:
#         found = True
#         if plug.index(letter) == 0:
#           out += plug[1]
#         else:
#           out += plug[0]
#         break
#     if not found:
#       out += letter
#   return out

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

def rotor(input, r1, r2, r3, setting, ref, plugs):
  steps = [""] * len(input)
  out = ''
  r1 -= 1
  r2 -= 1
  r3 -= 1
  ref -= 1
  for i in range(len(input)):
    letter = input[i]
    step = ""
    if not letter.isalpha():
      out += letter
      continue
    if (setting[2] in turnover[r3] or setting[1] in turnover[r2]):
      setting[1] = shift(setting[1], 'B')

    if (setting[1] in turnover[r2]):
      setting[0] = shift(setting[0], 'B')

    setting[2] = shift(setting[2], 'B')
    
    step += setting[0] + setting[1] + setting[2] + " "

    found = False
    for plug in plugs:
      if letter in plug:
        found = True
        if plug.index(letter) == 0:
          step += plug[1]
          letter = plug[1]
        else:
          step += plug[0]
          letter = plug[0]
        break
    if not found:
      step += letter

    letter = shift(letter, setting[2])
    letter = rotate(r3, letter)
    letter = shift_reverse(letter, setting[2])
    step += letter
    
    letter = shift(letter, setting[1])
    letter = rotate(r2, letter)
    letter = shift_reverse(letter, setting[1])
    step += letter

    letter = shift(letter, setting[0])
    letter = rotate(r1, letter)
    letter = shift_reverse(letter, setting[0])
    step += letter

    letter = reflect(ref, letter)
    step += letter

    letter = shift(letter, setting[0])
    letter = rotate_reverse(r1, letter)
    letter = shift_reverse(letter, setting[0])
    step += letter

    letter = shift(letter, setting[1])
    letter = rotate_reverse(r2, letter)
    letter = shift_reverse(letter, setting[1])
    step += letter

    letter = shift(letter, setting[2])
    letter = rotate_reverse(r3, letter)
    letter = shift_reverse(letter, setting[2])
    step += letter
    
    found = False
    for plug in plugs:
      if letter in plug:
        found = True
        if plug.index(letter) == 0:
          step += plug[1]
          letter = plug[1]
        else:
          step += plug[0]
          letter = plug[0]
        break
    if not found:
      step += letter
    
    steps[i] = step
    out += letter
  return steps

def drawRotor(num, shift, let1, let2, pos, x ,y):
    coords = []
    green = False
    rotor = rotors[num - 1]
    length = 20
    for i in range(26):
        stroke(0, 0, 255)
        fill(200)
        square(x, y + (i * length), length)
        fill(0)
        output = rotor[(i + shift) % 26]
        output_revshift = chr((ord(output) - shift - ord('A')) % 26 + ord('A'))
        text(output_revshift, x + length / 2, y + (i * length) + length / 2)
        if (output_revshift == let1 and frameCount % 10 >= (4 - pos)) or (chr(ord('A') + i) == let2 and frameCount % 10 >= (6 + pos)):
            coords.append([x, y + (i * length) + length / 2, x - 100 + length, y + (ord(output_revshift) - ord('A')) * length + length / 2])
            green = True
        else:
            stroke(128)
            line(x, y + (i * length) + length / 2, x - 100 + length, y + (ord(output_revshift) - ord('A')) * length + length / 2 )
    if green:
        stroke(0,255,0)
        strokeWeight(3)
        for coord in coords:
            line(coord[0],coord[1],coord[2],coord[3])
    stroke(128)
    strokeWeight(1)

def drawReflector(num, let, x, y):
    coords = []
    green = False
    reflector = reflectors[num - 1]
    drawn = [0] * 26
    length = 20
    for i in range(26):
        stroke(0, 0, 255)
        fill(200)
        square(x, y + (i * length), length)
        fill(0)
        text(reflector[i % 26], x + length / 2, y + (i * length) + length / 2)
        if (drawn[i] == 0 and drawn[ord(reflector[i]) - ord('A')] == 0):
            shift = ((ord(reflector[i]) - ord('A') - i) * length)
            drawn[i] = 1
            drawn[ord(reflector[i]) - ord('A')] = 1
            if ((reflector[i % 26] == let or chr(ord('A') + i) == let) and frameCount % 10 >= 5):
                coords = [x, y + (i * length) + length / 2 + shift / 2, 75 + shift / 8, shift, PI / 2, 3 * PI / 2]
                green = True
            else:
                stroke(128)
                noFill()
                arc(x, y + (i * length) + length / 2 + shift / 2, 75 + shift / 8, shift, PI / 2, 3 * PI / 2) 
    if green:
        stroke(0,255,0)
        strokeWeight(3)
        noFill()
        arc(coords[0],coords[1],coords[2],coords[3],coords[4],coords[5])
    stroke(128)
    strokeWeight(1)

def drawPlugs(plugs, let1, let2, x, y):
    length = 20
    coords = []
    some_green = False
    for i in range(26):
        green = False
        stroke(0, 0, 255)
        fill(200)
        square(x, y + (i * length), length)
        fill(0)
        if (let1 == chr(ord('A') + i) and frameCount % 10 >= 1) or (let2 == chr(ord('A') + i) and frameCount % 10 >= 9):
            some_green = True
            green = True
        stroke(128)
        found = False
        for plug in plugs:
            if (chr(ord('A') + i) in plug):
                if plug.index(chr(ord('A') + i)) == 0:
                    if green:
                        if chr(ord('A') + i) == let2:
                            coords.append([x, y + (i * length) + length / 2, x - 100 + length, y + (ord(plug[1]) - ord('A')) * length + length / 2])
                        else:
                            coords.append([x, y + (i * length) + length / 2, x - 100 + length, y + (ord(plug[0]) - ord('A') - i) * length + length / 2])
                        green = False
                    else:
                        line(x, y + (i * length) + length / 2, x - 100 + length, y + (ord(plug[1]) - ord('A')) * length + length / 2)
                    text(plug[1], x + length / 2, y + (i * length) + length / 2)
                else:
                    if green:
                        if chr(ord('A') + i) == let2:
                            coords.append([x, y + (i * length) + length / 2, x - 100 + length, y + (ord(plug[0]) - ord('A')) * length + length / 2])                        
                        else:
                            coords.append([x, y + (i * length) + length / 2, x - 100 + length, y + (ord(plug[1]) - ord('A') - i) * length + length / 2])
                        green = False
                    else:
                        line(x, y + (i * length) + length / 2, x - 100 + length, y + (ord(plug[0]) - ord('A')) * length + length / 2)
                    text(plug[0], x + length / 2, y + (i * length) + length / 2)
                found = True
                break
        if not found:
            text(chr(ord('A') + i), x + length / 2, y + (i * length) + length / 2)
            if green:
                coords.append([x, y + (i * length) + length / 2, x - 100 + length, y + i * length + length / 2])
                green = False
            else:
                line(x, y + (i * length) + length / 2, x - 100 + length, y + i * length + length / 2)
    if some_green:
        stroke(0,255,0)
        strokeWeight(3)
        for coord in coords:
            line(coord[0],coord[1],coord[2],coord[3])
        stroke(128)
        strokeWeight(1)

setting = ['D', 'D', 'S']
message = 'HELLOWORLD'.upper()
plug_config = ['AG', 'XY', 'CD', 'LJ']
rotor_config = [4,2,3]
reflector_config = 2
output = ""

steps = rotor(message, rotor_config[0], rotor_config[1], rotor_config[2], setting, reflector_config, plug_config)
# print(steps)
out = ""
for step in steps:
    out += step[len(step) - 1]


def setup():
    size(800, 800)
    textAlign(CENTER, CENTER)
    # strokeWeight(5)


def draw():
    stroke(0)
    background(255)
    fill(0)
    step = steps[(frameCount // 10) % len(message)]
    print(step)
    print(frameCount)
    text(frameCount, 750, 50)
    textSize(20)
    text(step[0], 310, 30) 
    text(step[1], 410, 30)
    text(step[2], 510, 30)
    textSize(10)
    drawPlugs(plug_config, step[4], step[len(step) - 1], 600, 50)
    drawRotor(rotor_config[2], ord(step[2]) - ord('A'), step[len(step) - 8], step[len(step) - 2], 2, 500, 50)
    drawRotor(rotor_config[1], ord(step[1]) - ord('A'), step[len(step) - 7], step[len(step) - 3], 1, 400, 50)
    drawRotor(rotor_config[0], ord(step[0]) - ord('A'), step[len(step) - 6], step[len(step) - 4], 0, 300, 50)
    drawReflector(reflector_config, step[len(step) - 5], 200, 50)
    textSize(50)
    text("Input: " + message, 400, 600)
    text("Output: " + out[:(frameCount + 2)//10 % len(out)], 400, 700)
    textSize(10)
    delay(300)
    if (frameCount % 10 == 0):
        delay(1500)
