from time import time, strftime, gmtime
from os import get_terminal_size


def ft_tqdm(lst: range):
    '''
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    '''
    startTime = time()
    for i, item in enumerate(lst):
        i += 1
        ln = len(lst)
        percent = i / ln

        elapsedTime = time() - startTime
        elapsPerf = i / elapsedTime

        remTime = strftime('%M:%S', gmtime((ln - i) / elapsPerf))
        elapsTime = strftime('%M:%S', gmtime(elapsedTime))

        perfomance = f"{i}/{ln} [{elapsTime}<{remTime}, {elapsPerf:.2f}it/s]"
        
        terminalWidth = get_terminal_size().columns
        barSize = terminalWidth - len(perfomance) - 7
        barSize = 2 if barSize < 2 else barSize
        
        progress = int(i * barSize / ln)
        bar = f"\r{percent: =4.0%}|" + progress * \
            "█" + (barSize - progress) * " " + "|"
        res = bar + perfomance
        diff = terminalWidth - len(res)
        if diff < 0:
            print(res[:diff], end="", flush=True)
        else:
            print(bar, perfomance, end="", fush=True)
        yield item
