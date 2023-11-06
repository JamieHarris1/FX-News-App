import requests
import json
from bs4 import BeautifulSoup
import openai
import os
import tiktoken
import time
from LLM_functions.url_to_summary import send
import re
import random


def get_positivity(summary, country):
    with open("secrets.txt", "r") as file:
        openai.api_key = api_key = json.load(file)['openai_key']
    prompt = f'''
	you are only to respond with a 3dp number in the range of +-1 (uniformly distributed) based on how Positive you as an expert believe the summary for increase the price of {country}'s currency, you will not respond with anything other than an 3dp number in this interval, no polite explanation,
	'''
    response = send(prompt=prompt, text_data=summary, max_tokens=100)
    try:
        result = float(response[0])
    except:
        print(response)
        try:
            result = re.findall(r'\d+(\.\d+)?', response.content)
            print(result)
        except:
            print("ERROR")
            result = 0

    return (float(result))


if __name__ == '__main__':
    example_summary = '''
	According to a note from Deutsche Bank, the Japanese yen's fundamentals are weak, making it comparable to currencies like the Turkish lira and Argentine peso. The note suggests that factors like yields and external accounts contribute to the yen's poor performance.
	'''
    print(get_positivity(example_summary, 'UK'))
