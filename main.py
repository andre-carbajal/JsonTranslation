import os
import shutil

def main():
    all_languages = {
        'uk': 'uk_ua',
        'fr': 'fr_fr',
        'zh-CN': 'zh_cn',
        'zh-TW' : 'zh_tw',
        'ja' : 'ja_jp',
        'de' : 'de_de',
        'it' : 'it_it',
        'ko' : 'ko_kr',
        'ru': 'ru_ru',
        'pt': 'pt_br'
    }

    LangCodeList = [
        'uk',
        'fr',
        'zh-CN',
        'zh-TW',
        'ja',
        'de',
        'it',
        'ko',
        'ru',
        'pt'
    ]

    dir = 'C:/Users/andre/Documentos/aproyectos/JsonTT/input/'
    output = 'C:/Users/andre/Documentos/aproyectos/JsonTT/output/'
    for LangCode in LangCodeList:
        old_name = os.path.join(dir, LangCode + '.json')
        new_name = os.path.join(dir, all_languages[LangCode] + '.json')

        os.rename(old_name, new_name)
        print(LangCode + '.json' + ' -> ' + all_languages[LangCode] + '.json')
        shutil.move(new_name, output+all_languages[LangCode] + '.json')
        print(all_languages[LangCode] + '.json' + ' was moved')

if __name__ == '__main__':
    main()