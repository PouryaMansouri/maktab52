import pyscreenshot


def save_screenshot(path='', name='screen_shot', ext='png'):
    my_screen_shot = pyscreenshot.grab()
    file_name = f'{path}{name}.{ext}'
    with open(file_name, 'wb') as f:
        my_screen_shot.save(f)
    return file_name


if __name__ == '__main__':
    print(save_screenshot())
