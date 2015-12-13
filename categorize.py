File = "DataSet/output_porter.txt";
positivesFile = "DataSet/Positive.txt";
negativesFile = "DataSet/Negative.txt";

positives = open(positivesFile).readlines();
negatives = open(negativesFile).readlines();
reviews = open(File).readlines();

for x in range(len(positives)):
    positives[x] = positives[x].replace("\n","");
for x in range(len(negatives)):
    negatives[x] = negatives[x].replace("\n","");
positives = frozenset(positives);
negatives = frozenset(negatives);

pos = 0;
neg = 0;
neu = 0;
old = 0;
new = 0;

for review in reviews:
    pos_ = 0;
    neg_ = 0;
    for word in review.split():
        word = word.lower();
        if word in positives:
            pos_ += 1;
        elif word in negatives:
            neg_ += 1;
    if(neg_>pos_):
        neg += 1;
    elif(pos_>neg_):
            pos += 1;
    else:
        neu += 1;
    
print "Total No. of Positive reviews",pos;
print "Total No. of Negetive reviews",neg;
print "Total No. of Neutral reviews",neu;
raw_input();
