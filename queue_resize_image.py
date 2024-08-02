import multiprocessing as mp
from PIL import Image # pip install pillow
from empty import Empty


def resize_image(image_paths, queue):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize(800, 600)
        queue.put(image_path, image)

def change_color(queue):
    while True:
        try:
            image_path, image = queue.get(timeout=5)
        except Empty:
            break

        image = image.convert('L')
        image.save(image_path)

def change_color(queue):
    if __name__ == "__main__":
        data = []
        queue = mp.Queue()

        for image in range(10, 211):
            data.append(f'./images/img_({image}).jpg')

    resize_process = mp.Process(target=resize_image, args=(data, queue))
    change_process = mp.Process(target=change_color, args=(queue, ))

    resize_process.start()
    change_process.start()

    resize_process.join()
    change_process.join()