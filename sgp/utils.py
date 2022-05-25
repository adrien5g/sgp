import json
import os
from configparser import ConfigParser

def read_config(config_file_path = os.path.abspath(os.curdir), config_file_name = 'config.ini', required = False):
    """
    Read config.ini file
    if 'required' is true, quit program if file not found.
    """
    
    file = f'{config_file_path}/{config_file_name}'

    if os.path.isfile(file):
        config = ConfigParser()
        config.read(file)
        return config._sections
    
    if required:
        quit(f'File {file} not found')

def gen_access_token_file(content, access_token_file_path = os.path.abspath(os.curdir), access_token_file_name='.access_token'):
    """
    Gen .access_token file.
    """
    file = f'{access_token_file_path}/{access_token_file_name}'
    with open(file, 'w') as token:
        token.write(content)
    return True

def get_access_token_file(access_token_file_path = os.path.abspath(os.curdir), access_token_file_name='.access_token'):
    """
    Get .access_token file.
    """
    file = f'{access_token_file_path}/{access_token_file_name}'
    try:
        with open(file, 'r') as token:
            return token.read()
            
    except FileNotFoundError:
        return None

def output_to_file(content, output_file_path = os.path.abspath(os.curdir), output_File_name='output.json'):
    file = f'{output_file_path}/{output_File_name}'
    content = json.dumps(content)
    with open(file, 'w') as output:
        output.write(content)