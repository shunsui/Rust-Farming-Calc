print('Posadź roślinę z obojętnie jaką pulą genów na środku dużego plantera.\n')
print('Cztery rośliny-dawcy (używaj tylko takich z max 1 czerwonym i nie w tym samym miejscu)')
print('posadź dookoła środkowej rośliny.\n')
print('Wprowadź do kalkulatora pule genów czterech roślin - dawców.')
print('Wpisując geny do kalkulatora każdy z osobna zatwierdzaj klawiszem ENTER\n')
print('Po wpisaniu czwartej puli genów, program pokaże wynik automatycznie.\n\n')

print('Podaj geny pierwszej rośliny, od lewej do prawej')
g1ros1 = input()
g2ros1 = input()
g3ros1 = input()
g4ros1 = input()
g5ros1 = input()
g6ros1 = input()
ros1 = g1ros1.upper(), g2ros1.upper(), g3ros1.upper(), g4ros1.upper(), g5ros1.upper(), g6ros1.upper()

print('Podaj geny drugiej rośliny, od lewej do prawej')
g1ros2 = input()
g2ros2 = input()
g3ros2 = input()
g4ros2 = input()
g5ros2 = input()
g6ros2 = input()
ros2 = g1ros2.upper(), g2ros2.upper(), g3ros2.upper(), g4ros2.upper(), g5ros2.upper(), g6ros2.upper()

print('Podaj geny trzeciej rośliny, od lewej do prawej')
g1ros3 = input()
g2ros3 = input()
g3ros3 = input()
g4ros3 = input()
g5ros3 = input()
g6ros3 = input()
ros3 = g1ros3.upper(), g2ros3.upper(), g3ros3.upper(), g4ros3.upper(), g5ros3.upper(), g6ros3.upper()

print('Podaj geny czwartej rośliny, od lewej do prawej')
g1ros4 = input()
g2ros4 = input()
g3ros4 = input()
g4ros4 = input()
g5ros4 = input()
g6ros4 = input()
ros4 = g1ros4.upper(), g2ros4.upper(), g3ros4.upper(), g4ros4.upper(), g5ros4.upper(), g6ros4.upper()

print(ros1)
print(ros2)
print(ros3)
print(ros4)


#kolumna 1
k1 = [g1ros1.upper(), g1ros2.upper(), g1ros3.upper(), g1ros4.upper()]
gxc1 = 0
gwc1 = 0
gyc1 = 0
ggc1 = 0
ghc1 = 0
for gx1 in k1:
    if gx1 == 'X':
        gxc1 = gxc1 + 1
for gw1 in k1:
    if gw1 == 'W':
        gwc1 = gwc1 + 1
for gy1 in k1:
    if gy1 == 'Y':
        gyc1 = gyc1 + 1
for gg1 in k1:
    if gg1 == 'G':
        ggc1 = ggc1 + 1
for gh1 in k1:
    if gh1 == 'H':
        ghc1 = ghc1 + 1
#kolumna 2
k2 = g2ros1.upper(), g2ros2.upper(), g2ros3.upper(), g2ros4.upper()
gxc2 = 0
gwc2 = 0
gyc2 = 0
ggc2 = 0
ghc2 = 0
for gx2 in k2:
    if gx2 == 'X':
        gxc2 = gxc2 + 1
for gw2 in k2:
    if gw2 == 'W':
        gwc2 = gwc2 + 1
for gy2 in k2:
    if gy2 == 'Y':
        gyc2 = gyc2 + 1
for gg2 in k2:
    if gg2 == 'G':
        ggc2 = ggc2 + 1
for gh2 in k2:
    if gh2 == 'H':
        ghc2 = ghc2 + 1
#kolumna 3
k3 = g3ros1.upper(), g3ros2.upper(), g3ros3.upper(), g3ros4.upper()
gxc3 = 0
gwc3 = 0
gyc3 = 0
ggc3 = 0
ghc3 = 0
for gx3 in k3:
    if gx3 == 'X':
        gxc3 = gxc3 + 1
for gw3 in k3:
    if gw3 == 'W':
        gwc3 = gwc3 + 1
for gy3 in k3:
    if gy3 == 'Y':
        gyc3 = gyc3 + 1
for gg3 in k3:
    if gg3 == 'G':
        ggc3 = ggc3 + 1
for gh3 in k3:
    if gh3 == 'H':
        ghc3 = ghc3 + 1
#kolumna 4
k4 = g4ros1.upper(), g4ros2.upper(), g4ros3.upper(), g4ros4.upper()
gxc4 = 0
gwc4 = 0
gyc4 = 0
ggc4 = 0
ghc4 = 0
for gx4 in k4:
    if gx4 == 'X':
        gxc4 = gxc4 + 1
for gw4 in k4:
    if gw4 == 'W':
        gwc4 = gwc4 + 1
for gy4 in k4:
    if gy4 == 'Y':
        gyc4 = gyc4 + 1
for gg4 in k4:
    if gg4 == 'G':
        ggc4 = ggc4 + 1
for gh4 in k4:
    if gh4 == 'H':
        ghc4 = ghc4 + 1
#kolumna 5
k5 = g5ros1.upper(), g5ros2.upper(), g5ros3.upper(), g5ros4.upper()
gxc5 = 0
gwc5 = 0
gyc5 = 0
ggc5 = 0
ghc5 = 0
for gx5 in k5:
    if gx5 == 'X':
        gxc5 = gxc5 + 1
for gw5 in k5:
    if gw5 == 'W':
        gwc5 = gwc5 + 1
for gy5 in k5:
    if gy5 == 'Y':
        gyc5 = gyc5 + 1
for gg5 in k5:
    if gg5 == 'G':
        ggc5 = ggc5 + 1
for gh5 in k5:
    if gh5 == 'H':
        ghc5 = ghc5 + 1
#kolumna 6
k6 = g6ros1.upper(), g6ros2.upper(), g6ros3.upper(), g6ros4.upper()
gxc6 = 0
gwc6 = 0
gyc6 = 0
ggc6 = 0
ghc6 = 0
for gx6 in k6:
    if gx6 == 'X':
        gxc6 = gxc6 + 1
for gw6 in k6:
    if gw6 == 'W':
        gwc6 = gwc6 + 1
for gy6 in k6:
    if gy6 == 'Y':
        gyc6 = gyc6 + 1
for gg6 in k6:
    if gg6 == 'G':
        ggc6 = ggc6 + 1
for gh6 in k6:
    if gh6 == 'H':
        ghc6 = ghc6 + 1

#FUNKCJA KOLUMNY 1
if gxc1 >=2:
    k1o = 'X'
elif gwc1 >=2:
    k1o = 'W'
elif gyc1 >=2:
    k1o = 'Y'
elif ggc1 >=2:
    k1o = 'G'
elif ghc1 >=2:
    k1o = 'H'
else:
    k1o = 'R'

if gyc1 == ggc1 == 2: #gyc1 pary random
    k1or = 'Y/G'
elif gyc1 == ghc1 == 2:
    k1or = 'Y/H'
elif ggc1 == gyc1 == 2: #ggc1 pary random
    k1or = 'G/Y'
elif ggc1 == ghc1 == 2:
    k1or = 'G/H'
elif ghc1 == gyc1 == 2: #ghc1 pary random
    k1or = 'H/Y'
elif ghc1 == ggc1 == 2:
    k1or = 'H/G'
else:
    k1or = '--'

#FUNKCJA KOLUMNY 2
if gxc2 >=2:
    k2o = 'X'
elif gwc2 >=2:
    k2o = 'W'
elif gyc2 >=2:
    k2o = 'Y'
elif ggc2 >=2:
    k2o = 'G'
elif ghc2 >=2:
    k2o = 'H'
else:
    k2o = 'R'

if gyc2 == ggc2 == 2: #gyc2 pary random
    k2or = 'Y/G'
elif gyc2 == ghc2 == 2:
    k2or = 'Y/H'
elif ggc2 == gyc2 == 2: #ggc2 pary random
    k2or = 'G/Y'
elif ggc2 == ghc2 == 2:
    k2or = 'G/H'
elif ghc2 == gyc2 == 2: #ghc2 pary random
    k2or = 'H/Y'
elif ghc2 == ggc2 == 2:
    k2or = 'H/G'
else:
    k2or = '--'

#FUNKCJA KOLUMNY 3
if gxc3 >=2:
    k3o = 'X'
elif gwc3 >=2:
    k3o = 'W'
elif gyc3 >=2:
    k3o = 'Y'
elif ggc3 >=2:
    k3o = 'G'
elif ghc3 >=2:
    k3o = 'H'
else:
    k3o = 'R'

if gyc3 == ggc3 == 2: #gyc1 pary random
    k3or = 'Y/G'
elif gyc3 == ghc3 == 2:
    k3or = 'Y/H'
elif ggc3 == gyc3 == 2: #ggc1 pary random
    k3or = 'G/Y'
elif ggc3 == ghc3 == 2:
    k3or = 'G/H'
elif ghc3 == gyc3 == 2: #ghc1 pary random
    k3or = 'H/Y'
elif ghc3 == ggc3 == 2:
    k3or = 'H/G'
else:
    k3or = '--'

#FUNKCJA KOLUMNY 4
if gxc4 >=2:
    k4o = 'X'
elif gwc4 >=2:
    k4o = 'W'
elif gyc4 >=2:
    k4o = 'Y'
elif ggc4 >=2:
    k4o = 'G'
elif ghc4 >=2:
    k4o = 'H'
else:
    k4o = 'R'

if gyc4 == ggc4 == 2: #gyc4 pary random
    k4or = 'Y/G'
elif gyc4 == ghc4 == 2:
    k4or = 'Y/H'
elif ggc4 == gyc4 == 2: #ggc4 pary random
    k4or = 'G/Y'
elif ggc4 == ghc4 == 2:
    k4or = 'G/H'
elif ghc4 == gyc4 == 2: #ghc4 pary random
    k4or = 'H/Y'
elif ghc4 == ggc4 == 2:
    k4or = 'H/G'
else:
    k4or = '--'

#FUNKCJA KOLUMNY 5
if gxc5 >=2:
    k5o = 'X'
elif gwc5 >=2:
    k5o = 'W'
elif gyc5 >=2:
    k5o = 'Y'
elif ggc5 >=2:
    k5o = 'G'
elif ghc5 >=2:
    k5o = 'H'

if gyc5 == ggc5 == 2: #gyc5 pary random
    k5or = 'Y/G'
elif gyc5 == ghc5 == 2:
    k5or = 'Y/H'
elif ggc5 == gyc5 == 2: #ggc5 pary random
    k5or = 'G/Y'
elif ggc5 == ghc5 == 2:
    k5or = 'G/H'
elif ghc5 == gyc5 == 2: #ghc5 pary random
    k5or = 'H/Y'
elif ghc5 == ggc5 == 2:
    k5or = 'H/G'
else:
    k5or = '--'

#FUNKCJA KOLUMNY 6
if gxc6 >=2:
    k6o = 'X'
elif gwc6 >=2:
    k6o = 'W'
elif gyc6 >=2:
    k6o = 'Y'
elif ggc6 >=2:
    k6o = 'G'
elif ghc6 >=2:
    k6o = 'H'
else:
    k6o = 'R'


if gyc6 == ggc6 == 2: #gyc6 pary random
    k6or = 'Y/G'
elif gyc6 == ghc6 == 2:
    k6or = 'Y/H'
elif ggc6 == gyc6 == 2: #ggc6 pary random
    k6or = 'G/Y'
elif ggc6 == ghc6 == 2:
    k6or = 'G/H'
elif ghc6 == gyc6 == 2: #ghc6 pary random
    k6or = 'H/Y'
elif ghc6 == ggc6 == 2:
    k6or = 'H/G'
else:
    k6or = '--'


print('Roślina na środku odziedziczy geny:\n',k1o,' ',k2o,' ',k3o,' ',k4o,' ',k5o,' ',k6o)
print(k1or, k2or, k3or, k4or, k5or, k6or)

print('Aby zakończyć, wciśnij dowolny klawisz')
input()