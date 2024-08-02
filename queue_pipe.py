import multiprocessing as mp

from PIL import Image  # pip install pillow


# Pipe - более простой объект чем очередь, куда нельзя помещать изображения
# Поэтому приходится сохранять изменения после первого действия и передавать только пути
# А также возвращает соединение 1 и соединение 2, а не любой объект,
# За счёт чего он более легковесный, чем очередь, но и более сложный в работе
def resize_image(image_paths, pipe: mp.Pipe, stop_event):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize(800, 600)
        image.save(image_path)
        pipe.send(image_path)
    stop_event.set()


def change_color(pipe: mp.Pipe, stop_event):
    while not stop_event.is_set():
        image_path, image = pipe.recv(timeout=5)
        image = Image.open(image_path)
        image = image.convert('L')
        image.save(image_path)


def change_color(pipe):
    if __name__ == "__main__":
        data = []
        conn1, conn2 = mp.Pipe()
        # Т.к. у pipe нет таймаута, нужно привязывать событие,
        # Чтобы остановить цикл постоянного ожидания нового элемента в очереди
        stop_event = mp.Event()

        for image in range(10, 211):
            data.append(f'./images/img_({image}).jpg')

        resize_process = mp.Process(target=resize_image, args=(data, conn1, stop_event))
        change_process = mp.Process(target=change_color, args=(conn2, stop_event))

        resize_process.start()
        change_process.start()

        resize_process.join()
        change_process.join()
