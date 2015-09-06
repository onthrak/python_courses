def piglatin():
    print "Pig Latin"
    print "Welcome!"
    answer = raw_input("Please type word")
    ans = answer[0:1] ## takes first letter
    ans1=answer[1::1] ## takes rest
    new_word=ans1+ans+"ay"
    print new_word
piglatin()