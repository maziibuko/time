import time

def stopwatch():
    input("Нажмите Enter, чтобы начать секундомер.")
    start_time = time.time()

    try:
        while True:
            elapsed_time = time.time() - start_time
            print(f"\rПрошло времени: {round(elapsed_time, 2)} сек.", end="", flush=True)
            time.sleep(0.1)  # Период обновления вывода
    except KeyboardInterrupt:
        pass  # Прерывание выполнения секундомера при нажатии Ctrl+C

    print("\nСекундомер остановлен.")

if __name__ == "__main__":
    stopwatch()
