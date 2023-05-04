import pandas as pd
import random

french_words = pd.read_csv("french_words.csv")

french_dict = french_words.to_dict("records")

print(french_dict[0]["French"])
print(len(french_dict))









# french_dict = [{value["French"]:value["English"]} for key, value in french_words.to_dict("index").items()]
# french_list = [value["French"] for key, value in french_words.to_dict("index").items()]
#



# def random_word():
#     random_french= french_list[random.randint(0,len(french_dict) - 1)]
#     return french_dict[random_french]
#
