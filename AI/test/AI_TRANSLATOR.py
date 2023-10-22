# from google_trans_new import google_translator
#
# translator = google_translator()
# translate_text = translator.translate('สวัสดีจีน',lang_tgt='en')
# print(translate_text)
from googletrans import Translator

translater = Translator()

out = translater.translate('guten Tag', dest='en')

print(out.text)
