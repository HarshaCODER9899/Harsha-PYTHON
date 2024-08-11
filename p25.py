"""In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going. A simple set of heuristic
 rules can be given as follows:
If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)

If the verb ends in ie, change ie to y and add ing

For words consisting of consonant-vowel-consonant, double the final letter before adding ing

By default just add ing

Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its present participle
 form. Test your function with words such as lie, see, move and hug. However, you must not expect such simple rules to work for all 
 cases."""

#the time complexity of make_ing_form is O(N)

# the space complexity is O(1)

def make_ing_form(v):
    v=list(v)
    consonent=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    vowels=['a','e','i','o','u']
    if v==['b','e'] or v==['s','e','e'] or v==['f','l','e','e'] or v==['k','n','e','e']:
        v.append("ing")
    elif v[-2]=="i" and v[-1]=="e":
        v[-2]="y"
        v[-1]="ing"    
    elif v[-1]=="e":
        v[-1]="ing"
    elif v[-3] in consonent and v[-2] in vowels and v[-1] in consonent:
        k=v[-1]+"ing"
        v.append(k)
    else:
        v.append("ing")
    verb=""
    for i in v:
        verb=verb+i
    return verb    

print(make_ing_form("be"))        

