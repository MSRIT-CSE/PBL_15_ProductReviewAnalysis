tweetFile = "reviews_Automotive.json.gz2";

tweets = open(tweetFile).readlines();


out=open("output.txt","w");
string="";
flag=0;
count=123456;
for tweet in tweets:
    flag=0;
    string="";
    count=count-1;
    if count==0:
        break;
    for word in tweet.split():
        
        #word = word.lower();
        if flag==1:
            string+=" "+word;
        if word=="\"reviewerName\":" and flag==0:
            flag=1;
            string+=" "+word;
        if word[len(word)-1]==","and word[len(word)-2]=="\""and flag!=0:
            if flag!=1:
                string+=" "+word;
            flag=0;
            
            #break;            
        if flag==2:
            string+=" "+word;
        if word=="\"reviewText\":" and flag==0:
            flag=2
            string+=" "+word;
        #break;
    out.write(string+"\n");
    #print string+"\n";
print "done";
