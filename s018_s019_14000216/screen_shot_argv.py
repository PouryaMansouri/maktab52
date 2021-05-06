import pyscreenshot, argparse


def save_screenshot(path, name, ext):
    my_screen_shot = pyscreenshot.grab()
    file_name = f'{path}{name}.{ext}'
    with open(file_name, 'wb') as f:
        my_screen_shot.save(f)
    return file_name


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take screenshot example')
    parser.add_argument('-p', '--path', action='store', metavar='DIR_PATH', default='',
                        help='directory path for save')
    parser.add_argument('-n', '--name', action='store', metavar='NAME', default='screen_shot',
                        help='file name for save')
    parser.add_argument('-e', '--ext', action='store', metavar='EXT', choices=['png', 'jpg', 'jpeg'], default='png',
                        help='extension of image file')
    args = parser.parse_args()
    print(args)
    file_path = save_screenshot(args.path
                                , args.name, args.ext)
    print('File path:', file_path)
