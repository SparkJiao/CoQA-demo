# CoQA-demo
model running on CoQA dataset including baseline.

The models are implemented based on allennlp, I created my own DatasetReader to read the dataset of CoQA and used the bidaf to train.   

sreader.py and bidaf.json is the simple bidaf model.  

bidaf_plus_dataset_reader.py and bidaf_plus.json is the bidaf++ w/2-ctx model.

reader.py and bidaf++.json is the bidaf++ model of allennlp running on QuAC and I have tried to modified it to run on CoQA but failed. I may try it later.

For commands and the implementation details, please search "allennlp" or "allenai" on github.  

