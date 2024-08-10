"""The third person singular verb form in English is distinguished by the suffix -s, which is added to the stem of the infinitive form:
 run -> runs. A simple set of rules can be given as follows:

If the verb ends in y, remove it and add ies

If the verb ends in o, ch, s, sh, x or z, add es

By default just add s

Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form returns its third person
 singular form. Test your function with words like try, brush, run and fix. Note however that the rules must be regarded as heuristic, 
 in the sense that you must not expect them to work for all cases. Tip: Check out the string method endswith()."""
#the time complexity of make_3sg_form is O(N)

# the space complexity is O(1)

def make_3sg_form(v):
   a=list(v)
   if a[-1]=="y":
      a[-1]="ies"
   elif a[-1]=="o" or a[-1]=="s" or a[-1]=="x" or a[-1]=="z" or a[-2]=="c" and a[-1]=="h" or a[-2]=="s" and a[-1]=="h":
      a.append("es")
   else:
      a.append("s")
   b=""
   for i in a:
      b=b+i
   return b       

print(make_3sg_form("bruch"))    