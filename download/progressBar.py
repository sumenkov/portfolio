import sys


def updt(total, progress):
    """
    Отображает индикатор выполнения в консоли.
    """
    if total == 0:
        total = progress
    barLength, status = 100, ""
    progress = float(progress) / float(total)
    if progress >= 1:
        progress, status = 1, "\r"
    block = int(round(barLength * progress))
    text = "\r[{}] {:.0f}% {}".format(
        "#" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()
