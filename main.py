import os
import json
import concurrent.futures
from dotenv import load_dotenv
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError

load_dotenv()

key = os.getenv('KEY')
endpoint = os.getenv('ENDPOINT')
region = "global"

credential = TranslatorCredential(key, region)
text_translator = TextTranslationClient(endpoint=endpoint, credential=credential)

input = 'input/en_us.json'

languages = {
        #"source_language" : "file_name"
        'zh-CN': 'zh_cn',
        'zh-TW' : 'zh_tw',
        'fr': 'fr_fr',
        'de' : 'de_de',
        'it' : 'it_it',
        'ja' : 'ja_jp',
        'ko' : 'ko_kr',
        'pt': 'pt_br',
        'ru': 'ru_ru',
        'uk': 'uk_ua'
    }

def translate_string(lang_code, string):
    try:
        input_text_elements = [ InputTextItem(text = string) ]
        response = text_translator.translate(content = input_text_elements, to = [lang_code], from_parameter = 'en')
        translation = response[0] if response else None

        if translation:
            for translated_text in translation.translations:
                return translated_text.text

    except HttpResponseError as exception:
        print(f"Error Code: {exception.error.code}")
        print(f"Message: {exception.error.message}")
        return string  # return original string if translation fails

def translate_file(file_path):
    try:
        # Attempt to open the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = json.load(file)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # Loop over the languages
    for lang, lang_code in languages.items():
        # Create a new dictionary to hold the translated content
        translated_content = {}

        # Create a ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Loop over each key-value pair in the content
            for key, value in content.items():
                # Translate the value and add it to the translated_content dictionary
                future = executor.submit(translate_string, lang, value)
                translated_content[key] = future.result()

        # Check if output directory exists, if not, create it
        if not os.path.exists('output'):
            os.mkdir('output')

        try:
            # Write the translated content to a new file in the output folder
            with open(f'output/{lang_code}.json', 'w', encoding='utf-8') as file:
                json.dump(translated_content, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error occurred while writing file: {e}")
    
    print('Done!')

if __name__ == '__main__':
    translate_file(input)