def count_dict(mystring):
    d = {}
# count occurances of character
    for w in mystring: 
        d[w] = mystring.count(w)
# print the result
    for k in sorted(d):
        print (k + ': ' + str(d[k]))
    print max(d, key=d.get)
    #print max(d.index())
    
mystring='blablab'
count_dict(mystring)