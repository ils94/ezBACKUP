import threading


def multithreading(function):
    x = threading.Thread(target=function)
    x.setDaemon(True)
    x.start()
