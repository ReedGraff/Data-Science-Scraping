from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals


import pandas as pd
import requests
import whois
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

import time
import os











from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


























links = ['https://www.nato.int/cps/en/natohq/news_185000.htm', 'https://www.politico.com/newsletters/politico-china-watcher/2021/06/17/biden-and-eu-allies-create-tough-week-for-china-493282', 'https://www.cnn.com/2021/06/16/china/china-russia-ties-mic-intl-hnk/index.html', 'https://foreignpolicy.com/2021/06/11/biden-putin-summit-asia-india-china-japan-us-russia-detente-quad/', 'https://www.cnbc.com/2021/04/18/op-ed-china-russia-cooperation-could-be-bidens-biggest-challenge.html', 'https://www.cnn.com/2021/06/28/opinions/putin-russia-uk-navy-crimea-andelman/index.html', 'https://www.thenation.com/article/world/nato-russia-norway/', 'https://apnews.com/article/lithuania-coronavirus-pandemic-covid-19-pandemic-national-security-russia-4f643495296f645e8957594034ec0367', 'https://nationalinterest.org/blog/buzz/world-war-iii-if-russia-invaded-baltics-nato-couldnt-stop-them-180303', 'https://smallwarsjournal.com/jrnl/art/total-defense-how-the-baltic-states-are-integrating-citizenry-into-their-national-security-', 'https://nationalinterest.org/blog/reboot/how-can-baltics-defend-themselves-against-russia-189009', 'https://eurasiantimes.com/nato-kicks-off-baltic-war-games-baltops-under-russias-watchful-eyes/', 'https://www.fpri.org/article/2021/06/the-reset-of-the-us-eu-relations-and-the-baltic-states/', 'https://euvsdisinfo.eu/report/nato-troops-in-baltic-countries-and-poland-threaten-the-security-of-russia-and-belarus', 'https://www.airuniversity.af.edu/Wild-Blue-Yonder/Article-Display/Article/2659250/the-russian-antiaccessarea-denial-security-issue-over-kaliningrad-and-the-balti/', 'https://www.baltictimes.com/baltic_pms_emphasize_importance_of_allied_presence_in_run-up_to_nato_summit/', 'https://www.nato.int/cps/en/natohq/topics_132685.htm', 'https://www.wilsoncenter.org/publication/151-russian-policy-nato-expansion-the-baltics', 'https://carnegieendowment.org/2021/06/30/grand-illusions-impact-of-misperceptions-about-russia-on-u.s.-policy-pub-84845', 'https://nationalinterest.org/blog/reboot/russia-nato-war-suwalki-gap-could-decide-world-war-iii-188690']
pop_list = ["/n", "\n", "..."]

Article_names = []
Article_dates = []
Article_links = []
Names = []
Summaries = []

for link in links:
    try:
        state = "True"
        max_time = 15
        start_time = time.time()

        while (time.time() - start_time) < max_time and state == "True":
            req = requests.get(link)
            soup = BeautifulSoup(req.content, 'html.parser')

            header = soup.find('h1').get_text()

            

            p_tags = soup.find_all('p')
            p_tags_text = [tag.get_text().strip() for tag in p_tags]
            sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
            sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
            article = ' '.join(sentence_list)

            for i in pop_list:
                if i in article:
                    article.strip(i)

            data = whois.whois(link)
            
            if "creation_date" in data:
                if data["creation_date"] is not None:
                    if type(data["creation_date"]) == "string" or type(data["creation_date"]) == "tuple":
                        Article_dates.append(data["creation_date"[0]])
                    else:
                        Article_dates.append(data["creation_date"])
            elif "date" in data:
                if data["creation_date"] is not None:
                    if type(data["date"]) == "string" or type(data["creation_date"]) == "tuple":
                        Article_dates.append(data["date"[0]])
                    else:
                        Article_dates.append(data["date"])
            elif "updated_date" in data:
                if data["creation_date"] is not None:
                    if type(data["updated_date"]) == "string" or type(data["creation_date"]) == "tuple":
                        Article_dates.append(data["updated_date"[0]])
                    else:
                        Article_dates.append(data["updated_date"])
            elif "expiration_date" in data:
                if data["creation_date"] is not None:
                    if type(data["expiration_date"]) == "string" or type(data["creation_date"]) == "tuple":
                        Article_dates.append(data["expiration_date"[0]])
                    else:
                        Article_dates.append(data["expiration_date"])
            else:
                Article_dates.append("None")
            


            LANGUAGE = "english"
            SENTENCES_COUNT = 2
            stemmer = Stemmer(LANGUAGE)

            summarizer = Summarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            parser = HtmlParser.from_url(link, Tokenizer(LANGUAGE))


            Article_names.append(header)
            Article_links.append(link)
            Summaries.append(summarizer(parser.document, SENTENCES_COUNT))
            Names.append("Reed")
            state = "False"



    except:
        Article_names.append("Fail")
        Article_dates.append("Fail")
        Article_links.append("Fail")
        Summaries.append("Fail")
        Names.append("Reed")

for i in range(0, (20 - len(Article_dates))):
    Article_dates.append("None")

print(len(links))
print(len(Article_names))
print(len(Article_dates))
print(len(Article_links))
print(len(Names))
print(len(Summaries))
df = pd.DataFrame({"Article Name":Article_names,"Article Date":Article_dates,"Link":Article_links,"Student":Names,"Summary":Summaries})
print(df)

df.to_excel('Debate.xlsx', index = False)