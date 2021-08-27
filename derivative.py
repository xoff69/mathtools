# ---------------------------------
# Christophe PICHON
# analyse dimensionnelle
# ---------------------------------
# librairie pour les derivees partielles

# reconnaitre /d^a [exp1 ]\d [exp2] ^b/  =>exp1,a,exp2,b
#renvoie la liste des derivatives
def isolate_derivative(expression):
  res=[]
  debut=False
  current=""
  for i in range(len(expression)):
    if (expression[i]=='/'):
      if debut:
        debut=False
        res.append(current)
      else:
        current=""
        debut=True
    else:
      current=current+expression[i]
    
  return res
# on  a   d^a[exp1]\d[exp2]^b
# reconnaitre /d^a [exp1 ]\d [exp2] ^b/  =>a,exp1,b,exp2
def analyse_derivative(expression):
  i=expression.find("d^")+len("d^")
  suite=expression[i:]
  j=suite.find("[")
  a=suite[0:j]
  suite=suite[j:]
  j=suite.find("[")+1
  k=suite.find("]")
  exp1=suite[j:k]
  suite=suite[k+1:]

  j=suite.find("[")+1
  k=suite.find("]")
  exp2=suite[j:k]
  suite=suite[k+1:]
  
  j=suite.find("^")+1
  b=suite[j]
  return a.strip(),exp1.strip(),b.strip(),exp2.strip()
