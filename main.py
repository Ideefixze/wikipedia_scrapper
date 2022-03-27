import pandas as pd
import wikipedia
import datetime
from tqdm import tqdm

N = 1000
FILE = 'output.csv'

def get_wiki_row(title):
    """
    Return csv data row from single title
    :param title: title of an wikipedia article
    :return: dict: title, categories, summary, content
    """
    page = wikipedia.WikipediaPage(title)
    return {'title': title, 'category': page.categories, 'summary': page.summary, 'content': page.content}

if __name__ == '__main__':
    #wikipedia.set_rate_limiting(True, datetime.timedelta(0,0.1))
    df = pd.DataFrame(columns=['title', 'category', 'summary', 'content'])

    for i in tqdm(range(N)):
        try:
            title = wikipedia.random(1)
            row = get_wiki_row(title)
            df = df.append(row, ignore_index=True)
        except Exception as e:
            print('Error at', i, ' >> ', e)

    df.to_csv(FILE, index=False)

    df_test = pd.read_csv(FILE)


