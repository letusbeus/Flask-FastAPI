import time


def total_img(start, end):
    print(f'The image was loaded in {end - start:.02f} seconds.')


def total(start, end):
    print(f'Total program execution time: {end - start:.02f} seconds')


def usual_execute():
    print('To execute the application from the command line, run the following command:\n'
          'python app_threading.py url1 url2\nwhere url1, url2 etc. are image links.')
    time.sleep(0.5)
    print(f'The program will be executed with the given data.')
    time.sleep(0.5)


def commandline_execute():
    print('Processing data...')
    time.sleep(0.5)
