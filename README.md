# TF-IDF

This file is a implementation of TF-IDF algorithm to find out text similarity.

Words are converted into numbers.
It uses ranking system and euclidean distance to find out similarity.

Explanation of TF-IDF:

TF [Term Frequency]:
  Term frequency is the number which represents frequency of the given word in the current document.
  
  TF(word,doc) = word occurance count/ total no of words in document
  
IDF [Inverse Document Frequency]:
  Inverse document frequency means its imporatance in the corpus.
  
  IDF(word,corpus) = log(no of documents/occurance of word in corpus)
  
  IDF(word,corpus) shows that as more often the word occur it will be having less imporatance.

TD-IDF:
  TF-IDF = TF*IDF
  Here TF is multiplied by IDF that means now word has a weight(IDF) so it will generate its relevence in the current document.
  
In testing phase we have to update the corpus with new document and train the model again.
Testing doc is now also a part of the corpus. 
For each word of testing doc we have to find euclidean distance with every documents.
The resultant list will contain doument index and its ditance from the document.
Less the distance more similar the document is.


NOTE: This file is an implementation of generic algorithm it does not have functionality of stemming,lemmatization and more resolved formulas
      Also data size limit is less than size of the RAM as it uses dictionary. Happy Coding! 

