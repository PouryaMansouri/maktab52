import translators, sys, argparse


def translator(text, to_lang, from_lang='auto', provider='google'):
    translator_func = getattr(translators, provider)
    return translator_func(text, from_lang, to_lang)


if __name__ == '__main__':
    # file, from_lang, to_lang, provider = sys.argv[1:5]

    parser = argparse.ArgumentParser(description='translator file')

    parser.add_argument(metavar='file_name', action='store', default=None, dest='filename', nargs='?')
    parser.add_argument('-t', '--to_lang', metavar='TO_LANG:', action='store', dest='to_lang', help='to_lang')
    parser.add_argument('-f', '--fr_lang', metavar='fr_LANG:', action='store', dest='fr_lang', help='fr_lang',
                        default='auto')
    parser.add_argument('-p', '--provider', metavar='PROVIDER', default='google', choices=['google', 'bing'])
    args = parser.parse_args()
    print(args)
    if args.filename:
        with open(args.filename) as f:
            t = f.read()
        res = translator(t, args.to_lang, args.fr_lang, args.provider)
        print(res)
    else:
        flag = True
        while flag:
            try:
                t = input()
                res = translator(t, args.to_lang, args.fr_lang, args.provider)
                print(res)
            except KeyboardInterrupt:
                flag = False
