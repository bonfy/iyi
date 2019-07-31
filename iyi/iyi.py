# coding:utf-8
import sys
import requests
import getopt
from termcolor import colored


KEYFROM = 'BONFYHOME'
KEY = '490546925'

def get_response(word):
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom={}&key={}&type=data&doctype=json&version=1.1&q={}'.format(KEYFROM,KEY,word)
    r = requests.get(url)
    return r.json()

def show(response):
    if response['errorCode'] is not 0:
        print(colored('query error,please try again', 'cyan'))
    else:
        print(colored('查询: {}'.format(response['query']), 'green'))

        print(colored('释义: '+'\t'.join(response['translation']), 'cyan'))

        if 'basic' in response.keys():
            basic = response['basic']
            print(colored('基本词典:', 'blue'))
            print(colored('\n'.join(basic['explains']), 'cyan'))
        if 'web' in response.keys():
            web = response['web']
            print(colored('网络词典:', 'blue'))
            for item in web:
                print(colored(item['key'], 'green'))
                print(colored('\t'.join(item['value']), 'cyan'))

def main():
    try:
        options, args = getopt.getopt(sys.argv[1:], ["help"])
    except getopt.GetoptError as e:
        pass

    word = " ".join(args).lower()
    root = get_response(word)
    show(root)


if __name__ == '__main__':
    main()