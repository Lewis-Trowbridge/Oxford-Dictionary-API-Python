import requests

class OxfordDictionaries():
    appid=""
    appkey=""
    Authenticated=False

    def Auth(self, appid, appkey):
        self.appid = appid
        self.appkey = appkey
        self.Authenticated=True

    def Entries(self, word_id, source_lang="en"):
        if self.Authenticated==True:
            headers={"app_id":self.appid, "app_key":self.appkey}
            results=requests.get("https://od-api.oxforddictionaries.com/api/v1/entries/"+source_lang+"/"+word_id, headers=headers)
            if results.status_code==200:
                return(results.json())
            elif results.status_code==404:
                raise Exception("No entry is found matching supplied id and source_lang")
            elif results.status_code==500:
                raise Exception("Internal Error. An error occurred while processing the data")
        else:
            raise Exception("No OXD authentication given")

    def Lemmatron(self, word_id, source_lang="en"):
        if self.Authenticated==True:
            headers={"app_id":self.appid, "app_key":self.appkey}
            results=requests.get("https://od-api.oxforddictionaries.com/api/v1/inflections/"+source_lang+"/"+word_id, headers=headers)
            if results.status_code==200:
                return(results.json())
            elif results.status_code==404:
                raise Exception("No entry is found matching supplied id and source_lang")
            elif results.status_code==500:
                raise Exception("Internal Error. An error occurred while processing the data")
        else:
            raise Exception("No OXD authentication given")

    def Search(self, q, source_lang="en", prefix="false", regions=None, limit=None, offset=None):
        if self.Authenticated==True:
            headers={"app_id":self.appid, "app_key":self.appkey}
            params={"q":q, "prefix":prefix, "regions":regions, "limit":limit, "offset":offset}
            results=requests.get("https://od-api.oxforddictionaries.com/api/v1/search/"+source_lang, headers=headers, params=params)
            if results.status_code==200:
                return(results.json())
            elif results.status_code == 404:
                raise Exception("No entry is found matching supplied id and source_lang")
            elif results.status_code == 500:
                raise Exception("Internal Error. An error occurred while processing the data")
        else:
            raise Exception("No OXD authentication given")

    def Translation(self, word_id, target_translation_language, source_translation_language="en"):
        if self.Authenticated==True:
            headers={"app_id":self.appid, "app_key":self.appkey}
            results=requests.get("https://od-api.oxforddictionaries.com/api/v1/entries/"+source_translation_language+"/"+word_id+"/translations="+target_translation_language, headers=headers)
            if results.status_code == 200:
                return (results.json())
            elif results.status_code == 404:
                raise Exception("No entry is found matching supplied id and source_lang")
            elif results.status_code == 500:
                raise Exception("Internal Error. An error occurred while processing the data")
        else:
            raise Exception("No OXD authentication given")

    def Synonyms(self, word_id, source_lang="en"):
        if self.Authenticated==True:
            headers={"app_id":self.appid, "app_key":self.appkey}
            results=requests.get("https://od-api.oxforddictionaries.com/api/v1/entries/"+source_lang+"/"+word_id+"/synonyms", headers=headers)
            if results.status_code == 200:
                return (results.json())
            elif results.status_code == 404:
                raise Exception("No entry is found matching supplied id and source_lang")
            elif results.status_code == 500:
                raise Exception("Internal Error. An error occurred while processing the data")
        else:
            raise Exception("No OXD authentication given")

    def Antonyms(self, word_id, source_lang="en"):
        if self.Authenticated==True:
            headers={"app_id":self.appid, "app_key":self.appkey}
            results=requests.get("https://od-api.oxforddictionaries.com/api/v1/entries/"+source_lang+"/"+word_id+"/synonyms", headers=headers)
            if results.status_code==200:
                return(results.json())
            elif results.status_code == 404:
                raise Exception("No entry is found matching supplied id and source_lang")
            elif results.status_code == 500:
                raise Exception("Internal Error. An error occurred while processing the data")
        else:
            raise Exception("No OXD authentication given")

    def Sentence(self, word_id, source_lang="en"):
        if self.Authenticated==True:
            headers={"app_id":self.appid, "app_key":self.appkey}
            results=requests.get("https://od-api.oxforddictionaries.com/api/v1/entries/"+source_lang+"/"+word_id+"/sentences", headers=headers)
            if results.status_code==200:
                return(results.json())
            elif results.status_code == 404:
                raise Exception("No entry is found matching supplied id and source_lang")
            elif results.status_code == 500:
                raise Exception("Internal Error. An error occurred while processing the data")
        else:
            raise Exception("No OXD authentication given")
