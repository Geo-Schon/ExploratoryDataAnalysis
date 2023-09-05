# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4 мяча. Какова вероятность того, что 3 мяча белые?

from Combi import combination

whiteballs = combination(5, 2)*combination(3, 0)/combination(8, 2) * combination(5, 1)*combination(7, 3) / \
             combination(12,4) + combination(5, 1)*combination(3, 1)/combination(8, 2) * combination(5, 2)\
             * combination(7, 2)/combination(12, 4) + combination(5, 0)*combination(3, 2)/combination(8, 2) \
             * combination(5, 3)*combination(7, 1)/combination(12, 4)

print(f"Вероятность того, что 3 мяча белые = {whiteballs: .4f} -> {whiteballs*100:0.2f}%")