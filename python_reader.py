import pdfplumber
from gtts import gTTS


with pdfplumber.open("sample_pdf.pdf") as pdf:
    full_text = ""
    
    for page in pdf.pages:
        text = page.extract_text()
        if text :
            full_text += text + "\n"
            
print(full_text)

tts = gTTS(text=full_text, lang='en', slow=False)
tts.save("audiobook.mp3")
