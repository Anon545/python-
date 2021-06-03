# Рассмотрим задачу о пересечении двух длительных
# по времени событий. Оба события характеризуются двумя числами
# - годами начала и конца. Необходимо определить, пересекались ли
# события во времени, при этом если одно событие началось в тот год,
# когда закончилось другое - они считаются пересекающимися.
#
# Первая идея заключается в том, чтобы рассмотреть все
# возможные варианты расположения событий и выделить следующий
# критерий пересечения: если начало или конец одного из событий
# лежит между началом и концом другого, то они пересекаются.
# В виде программы это можно записать так:

start1 = int(input())
finish1 = int(input())
start2 = int(input())
finish2 = int(input())
# isS1in2 = start2 <= start1 <= finish2 вариант 1
# isF1in2 = start2 <= finish1 <= finish2
# isS2in1 = start1 <= start2 <= finish1
# isF2in1 = start1 <= finish2 <= finish1
# answer = isS1in2 or isF1in2 or isS2in1 is isF2in1 вариант 1
#  вариант 2 - он лучше #answer = start1 <= finish2 and start2 <= finish1
print (answer)