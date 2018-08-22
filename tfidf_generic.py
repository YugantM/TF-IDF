import nltk,operator,pandas as p
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from math import log

file = open("file.txt",'r')
inpu=[]

for i in file:
    inpu.append(i.lower())

#no of documents     
Nd = len(inpu) 


#this function removes stops words as pre processing the text
def preprocess(file):
    
    stop_words = set(stopwords.words('english')) 

    filtered_sentence = []
    
	for sent in file:
        word_tokens = word_tokenize(sent) 
        temp = [w for w in word_tokens if not w in stop_words] 
        filtered_sentence.append(temp)
        
    return filtered_sentence

	
#this function finds Term Frequency
def TF(word,sent):
    score=sent.count(word)/len(sent)
    return score  

	
#this function finds Inverse Document Frequency
def IDF(word,file):
    count = 1
    for sent in file:
        if word in sent:
            count+=1
    return log(Nd/count)

	
#this function finds TF-IDF score of the word
def tfidf(word,sent,file):
    score = TF(word,sent)*IDF(word,file)
    return score


# this function generates and returns a matrix which is a dictionary containing word as key and
# a list of document index and tfidf as values
def create_matrix(file):
    matrix = {}
    index=0
    for sent in file:
        for word in sent:
            if word not in matrix.keys():
                matrix[word]=[]
            matrix[word].append(index)
            matrix[word].append(tfidf(word,sent,file))
        index+=1
    return matrix


# train model is a combination of above functions and returns matrix
def train_model(text):
    return create_matrix(preprocess(text))
    

# this is a test model which gives us similarity between a given statement and corpus
# prints sorted list of all suggested documents
def test_model(text,statement):
    statement= statement.lower()
    text1 = text+ [statement+'\n']
    comp = train_model(text1)
    
    for k in comp:
        comp[k] = sum([[k,v] for k,v in (dict(zip(comp[k][::2],comp[k][1::2])).items())],[])
    
    
    st_dict = {}
    for word in list(statement.split(' ')):
        if word in comp.keys():
            
            if len(comp[word])>2:
                
				for i in range(int(len(comp[word])/2)-1):
                    
					if comp[word][i*2] not in st_dict.keys():
                        st_dict[comp[word][i*2]]=[]
                    
					st_dict[comp[word][i*2]].append((comp[word][-1]-comp[word][i+1])**2) 
    
	for i in st_dict.keys():
        st_dict[i]=sum(st_dict[i])
        
    st_dict = sorted(st_dict.items(), key=operator.itemgetter(1))
    
    for i in range(len(st_dict)):
        print(text[i])
     

print(test_model(inpu,"how to configure liferay portlet"))