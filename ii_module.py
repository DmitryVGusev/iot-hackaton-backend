#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def calculate_deadline(data: dict):
    """Эсулятор ИИ, дает на выход ответ"""
    answer = data['quantity'] * random.randint(1, 4) * 0.1
    return answer


def calculate_breakout(machines: set):
    """Эмулятор ИИ, дает на выходе словарь id_станка:вероятность"""
    answer = dict()
    for machine in machines:
        random_chance = random.randint(0, 100) / 100
        answer.update({machine: random_chance})

    return answer
