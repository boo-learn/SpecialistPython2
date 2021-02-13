def sum_points(cards):
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """
    # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)

    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков
    sum_points = 0

    for i in cards:
        sum_points += i.score

    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)

    if sum_points > 21:
        sum_points = 0
        for i in cards:
            if i.rank == 'A':
                i.score = 1
            sum_points += i.score

    # print(cards,sum_points)

    return sum_points
