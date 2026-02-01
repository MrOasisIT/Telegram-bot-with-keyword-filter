from aiogram.filters import BaseFilter
from aiogram.types import Message
import string
import logging

log = logging.getLogger(__name__)

class Key_words(BaseFilter):
    
    def __init__(self,key_words:list):
        if not key_words:
            self.key_words_base = []
        else:
            try:
                self.key_words_base = [word.lower() for word in key_words]
                self.key_words = [word[0:-1] for word in self.key_words_base]
                self.len_words = [len(word) for word in self.key_words]
                print("обработка завершина")
            except Exception:
                log.exception("Произошла ошибка при обработке списка с ключевыми словами")
                return False

    async def __call__(self,message:Message):
        if not message.text:
            return False
        try:
            text = message.text.lower()
            text_list = text.translate(str.maketrans("","",string.punctuation)).split()
            print(text_list,self.key_words_base,self.key_words,self.len_words)
        except Exception:
            log.exception("Произошла ошибка при обработке данных")
            return False
        for word in text_list:
            for len_word in self.len_words:
                if len(word) == len_word+1:
                    if word[:-1] in self.key_words:
                        return True
                if len(word) == len_word+2:
                    if word[:-2] in self.key_words:
                        return True
                if len(word) == len_word+3:
                    if word[:-3] in self.key_words:
                        return True

        return False