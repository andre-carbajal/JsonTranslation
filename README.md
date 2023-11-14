# JsonTranslation 

## Description

This Python project is a multilingual translation tool that uses the Azure AI Text Translation service to translate the content of a JSON file from English to multiple other languages.

The script reads a JSON file from the 'input' directory, which contains key-value pairs in English. It then translates the values into several languages (Chinese Simplified, Chinese Traditional, French, German, Italian, Japanese, Korean, Portuguese, Russian, and Ukrainian) using Azure's translation service.

The translated content is then written to new JSON files, each named according to the language code (e.g., 'zh_cn.json' for Simplified Chinese), and saved in the 'output' directory.

The translation process is performed concurrently for each key-value pair in the JSON file, which can significantly speed up the translation process for large files.

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install azure-ai-translation-text python-dotenv
```

# Setup
Create a `.env` file in the root directory of the project, and add your Azure Text Translation service key and endpoint:
```
KEY=your_key_here
ENDPOINT=your_endpoint_here
```

## Usage
1. Create your ```input``` folder 
2. Place your English json file with the name ```en_us.sjon```.
3. Execut the main file:
    ```bash
    python3 main.py
    ```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU General Public License v3.0](LICENSE)