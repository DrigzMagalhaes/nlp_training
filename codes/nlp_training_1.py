import re
import nltk
import string
import heapq

orig_text = """Aquele que habita no esconderijo do Altíssimo,
a sombra do Onipotente descansará.
Direi do senhor: ele é o meu Deus, o meu refugio,
a minha forataleza, e nele confiarei.
Porque ele te livra-rá do laço do passarinheiro,
e da peste perniciosa.
Ele te cubrirá com suas penas, e de baixo de suas
asas, seguro estarás.
A sua verdade é escudo e broquel, não temerás
espanto noturno, nem seta que voe de dia, nem
peste que ande na escuridão, nem mortandade que
assole ao meio dia.
Mil cairam ao teu ledo e dez mil a tua direita
mas tú, não serás atingido.
Somente com os teus olhos olharás, e verás a
recompensa dos ímpios.
Porque tú oh Senhor, és o meu refugio,o altíssimo
é a tua habitação.
Nenhum mal te sucederá, nem praga alguma chegará
a tua tenda, porque aos seu anjos dará ordem a
teu respeito para ti guardarem, e todos os teus
caminhos.
Eles te susteram em suas mãos para que não tropesses
com o teu pé em pedra.
Pisarás o leão e a cobra, calcarás aos pé o
filho do leão e a serpente.
Porque tão encarecidamente me amou, também eu o
livrarei, poloei em retiro alto, porque conheceu
o meu nome.
Ele me invocará, e eu lhe responderei, estarei
com ele na angústia, e o glorificarei.
Farta-lo-ei com longuras de dias, e lhe mostrarei
a minha salvação."""

orig_text = re.sub(r'\s+',' ',orig_text)
print(orig_text)

def preprocessing(text):
    processed_text = text.lower()

    nltk.download('punkt')
    nltk.download('stopwords')

    stopwords = nltk.corpus.stopwords.words('portuguese')

    tokens = []
    for token in nltk.word_tokenize(processed_text):
        tokens.append(token)

    tokens = [word for word in tokens if word not in stopwords and word not in string.punctuation]

    processed_text = ' '.join([str(token) for token in tokens])
    
    return processed_text

def word_weights(text):
    words_freq = nltk.FreqDist(nltk.word_tokenize(text))
    words_freq

    max_freq = max(words_freq.values())
    print(max_freq)
    for word in words_freq.keys():
        
        words_freq[word] = (words_freq[word]/max_freq)
        
    return words_freq

def sent_value (text, words_freq):
    sent_list = nltk.sent_tokenize(text)

    sent_values = {}
    for sent in sent_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in words_freq.keys():
                if sent not in sent_values.keys():
                    sent_values[sent] = words_freq[word]
                else:
                    sent_values[sent] += words_freq[word]

    return sent_values

def summarized_txt (sent_values):

    hi_val_sent = heapq.nlargest(5,sent_values,key=sent_values.get)

    summary = ' '.join(hi_val_sent)

    return summary

processed_text = preprocessing(orig_text)

words_freq = word_weights(processed_text)

sent_values = sent_value(orig_text,words_freq)

summary = summarized_txt(sent_values)

print(summary)