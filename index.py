from googletrans import Translator

def translate_to_turkish(text):
    """
    Translates English text to Spanish.

    Parameters:
        text (str): The English text to be translated.

    Returns:
        str: The translated Spanish text.
    """
    translator = Translator()
    translation = translator.translate(text, src='en', dest='tr')
    return translation.text

# Test the translator function
english_text = "Hello my name is marvin"
turkish_text = translate_to_turkish(english_text)
print(f"English: {english_text}\nTurkish: {turkish_text}")