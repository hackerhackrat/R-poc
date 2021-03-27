import threading
import time


def exception_handled_function(thread_function, args=()):
    try:
        thread_function(*args)
    except KeyboardInterrupt:
        raise
    except Exception as ex:
        print("thread {0}: {1}".format(threading.currentThread().getName(), str(ex)))


def run_threads(num_threads, thread_function, args: tuple = ()):
    threads = []

    # 启动多个线程
    for num_threads in range(num_threads):
        thread = threading.Thread(target=exception_handled_function, name=str(num_threads),
                                  args=(thread_function, args))
        thread.setDaemon(True)
        try:
            thread.start()
        except Exception as ex:
            err_msg = "error occurred while starting new thread ('{0}')".format(str(ex))
            print(err_msg)
            break

        threads.append(thread)

    # 等待所有线程完毕
    alive = True
    while alive:
        alive = False
        for thread in threads:
            if thread.isAlive():
                alive = True
                time.sleep(0.1)