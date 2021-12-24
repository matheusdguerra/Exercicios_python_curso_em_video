# ex046
# mostre na tela um contados regressivo para fogos de artificios
# 10 até 0 com 1 segundo entre eles

from time import sleep
from emoji import emojize   # https://www.webfx.com/tools/emoji-cheat-sheet/ | https://pypi.org/project/emoji/

for c in range(10, 0, -1):
    print(c)
    sleep(1)

print(emojize(':collision: :sparkles:    :collision: :sparkles:'))
print(emojize('   :collision: :sparkles:     :collision: :sparkles:'))
print(emojize('      :collision: :sparkles: :collision: :sparkles:'))
print(emojize(' :collision: :sparkles:   :collision: :sparkles:'))
print(emojize('    :collision: :sparkles:  :collision: :sparkles:'))
print(emojize('  :collision: :sparkles:  :collision: :sparkles:'))
print(emojize(':collision: :sparkles:  :collision: :sparkles:'))
print(emojize('    :collision: :sparkles: :collision: :sparkles:'))
