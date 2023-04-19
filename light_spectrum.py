# Программа для построения спектра света
# на основе длины волны

import matplotlib.pyplot as plt


def plot_spectrum(wavelengths):
    """
    Функция для построения спектра света
    на основе длины волны.

    Аргументы:
    wavelengths -- список длин волн (в нанометрах)
    """
    colors = []
    for wavelength in wavelengths:
        colors.append(determine_color(wavelength))
    plt.bar(wavelengths, [1] * len(wavelengths), color=colors, width=5)
    plt.xlabel("Длина волны, нм")
    plt.ylabel("Интенсив
