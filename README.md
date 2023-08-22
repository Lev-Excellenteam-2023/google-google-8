# google-google-8
google-google-8 created by GitHub Classroom

# Google auto-complete project

Implement autocomplete system.
The program receives input from user and generates options for completion.

## Algorithms & Structures

The dataset is saved twice:
- Dictionary: Keys are a unique sentence id and values are the sentences themselves and their source.
- Trie: Each word in the dataset is saved in the trie. 
Every node has a dictionary. Keys are ids of sentences where the word appears and values are the positions in the sentence in which it appears.



## Detailed Code Flow
We begin by inserting data from all the files into the trie tree and the dictionary. Afterward, we iterate through all the words in the input string and search for sentences in which all the words are found. We then verify that the words appear in consecutive positions within the sentence. The sentences that meet these conditions are considered as suggested sentences for this input. If there are fewer than 5 suggested sentences, we attempt to generate more suggestions by correction by trying to get suggestion of sentences that are similar to the input sentence. Next, we calculate a score for each suggested sentence and select the top 5 sentences with the highest scores. If there are multiple suggested sentences with equal scores, we prioritize the one that is lexicographically greater


