# # from googletrans import Translator
# # translator = Translator()
# # translator = Translator(service_urls=['translate.googleapis.com'])
# # translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
# # translator.raise_exception()
# # print(translator)
#
from translate import Translator
translator= Translator(to_lang='uz',target_language='en')
translation = translator.translate("hello")
#     text_to_translate = "hello"
# translated_text = translate_text(text_to_translate, target_language='en')
# print("Original text:", text_to_translate)
# print("Translated text:", translated_text)
print(translation)
#
# if __name__ == "__main__":
#     text_to_translate = "hello"
#     translated_text = translate_text(text_to_translate, target_language='en')
#     print("Original text:", text_to_translate)
#     print("Translated text:", translated_text)