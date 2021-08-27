# ---------------------------------
# Christophe PICHON
# analyse dimensionnelle
# ---------------------------------

# ---------------------------------
# git:
# git commit -am "mm"
# git push
# ---------------------------------

#------------------------------------
# format
# item item 
# # derivative: /d^a [exp1 ]\d [exp2] ^b/      =>d^a (fx)/dx^2
# ----------------------------------

# --------------------------------------
# TODO
# finir derivative
# ajouter les parentheses
# ajouter expression avec dimension : exemple S= [E][K]^-1 
# ajouter boucle+aide
# -------------------------------------

import derivative as d

# unites connues
unites={"M","L","K","T","I","N","J"}
# variables connues
#E={"M L^2 T^-2"]

allvar={}
allvar["h"]="M^1 L^2 T^-1"
allvar["hbar"]=allvar["h"]
allvar["E"]=allvar["h"]
allvar["k"]="L^-1"
allvar["c"]="L^1 T^-1"
allvar["T"]="K^1"
allvar["w"]=allvar.get("c")+" "+allvar.get("k")
allvar["Kb"]="L^2 M^1 T^-2 K^-1" #m2 kg s-2 K-1


#les fonctions
def dimension_for_variable(val):
    try:
        x=allvar[val]
    except KeyError:
        return "[UNKNOWN]"
    return x
        

# gere les facteurs 
def simplify(expression):
    #^-1^1^2
    #print("expres",expression)
    l=expression.split("^")
    res=0
    #print("l",l)
    for i in l:
        if len(i)!=0:
            res=res+int(i)
    
    return "^"+str(res)

# renvoie la chaine en entree sous forme d'une chaine en mettant à plat les parentheses et les puissances
# recursif
#ne fonctionne pas pour les derivees partielles
def isole_rec_parenthese(expression):
  idx=expression.find("(")
  if idx>-1:
    idf=idx+1
    comptefer=1  #compteur de parenthese fermante
    while idf<len(expression):
        if expression[idf]==')':
            comptefer=comptefer-1
            if comptefer==0:
                break;
        elif expression[idf]=='(':
            comptefer=comptefer+1
        idf=idf+1
    
    if comptefer!=0:
      return "### ERROR ### missing ) "+expression
    souschaine=expression[idx+1:idf]
    milieu=isole_rec_parenthese(souschaine)
    # TODO chercher les puissances et les traiter
    if idf+1<len(expression) :
          if  expression[idf+1]=='^':
            puissance=""
            idf=idf+2
    TODO gerer les puissances negatives
            while idf<len(expression):
                  if expression[idf]==' ':
                        break
                  puissance=puissance+expression[idf]
                  idf=idf+1
            if puissance=="":
                  return "### ERROR ### power missing "+expression
            power=int(puissance)
            resultat=""
            for i in range(0,power):
              resultat=resultat+" "+milieu
            milieu=resultat
    
    debut=""
    if idx>0:
      debut=expression[0:idx-1]
    return debut+" "+milieu+" "+isole_rec_parenthese(expression[idf+1:])
  else:
    #traiter les puissances simples
    # il faut splitter sur les espaces puis traiter
    r=expression.split(" ")
    resultat=""
    for i in r:
      expression=i      
      # on cherche espace ou ^
      # on n'a pas de parenthese
      u=d.isolate_derivative(i)
      print("ici ",i)
      #print(i," ID ",isolate_derivative(i))
      if u=="[]": #pas de derivative
        if i.find("^")!=-1:
                puissance=""
                orig=i.find("^")
                idf=i.find("^")+1
                isNegative=False
                while idf<len(i):
                        if i[idf]==' ':
                            break
                        if i[idf]=='-':
                            isNegative=True
                        else:
                            puissance=puissance+i[idf]
                            idf=idf+1
                if puissance=="":
                        return "### ERROR ### power missing 2 "+expression+"-"+i
                power=int(puissance)
        TODO gerer les puissances negatives
                milieu=i[0:orig]
                for i in range(0,power):
                    resultat=resultat+" "+milieu
        else:
                resultat=resultat+" "+i
    else:
        # derivative
        resultat=resultat
    return resultat


# gestion des derivees 


def interprete_derivative(expression):
    e=d.analyse_derivative(expression)
    resultat=isole_rec_parenthese(e[1])+" "+isole_rec_parenthese(e[3]+"^-"+e[2])

z="d^a[k]\d[w]^3"
print(z,"-",interprete_derivative(z))

# analyse dimensionnelle    principale
def AD(expression):
    x = isole_rec_parenthese(expression).split(" ")
    resultat=""
    for i in x:
        if i!="":
            resultat=resultat+dimension_for_variable(i.strip())+ " "
    r=resultat.split()
    #print("res=",r)
    r.sort()
    #print(r)
    #simplification 
    
    simpleres={}
    for i in r:
        clef=i[0]
        #print("clef "+clef)
        #print(simpleres.get(clef))
TODO gerer les puissances negatives
        if simpleres.get(clef):
            simpleres[clef]=simpleres.get(clef)+i[1:]
        else:
            simpleres[clef]=i[1:]
    resultat=""
    for i in simpleres.keys():
        si=simplify(simpleres[i])
        if si!="^0":
            resultat=resultat+i+ si+" "
    return resultat

#affiche les variables connues
def affiche_variable_connues():
    print("Variables connues:")
    for i in allvar.keys():
        print (i,":",allvar.get(i))
# def affiche aide
def affiche_aide():
    # les variables connues
    # les commandes
    print("Liste des commandes:")
    print("? affiche l'aide")
    print("v? affiche les variables connues")
    print("s? affiche la syntaxe des expressions")
    print("AD(expression) : effectue l'analyse dimensionnelle de l'expression, s? pour la syntaxe des expressions")
    print("DEF x=[L] [M]^5  permet de definir la variable x de dimension L M^5 ",unites)

# affiche la syntaxe pour les expressions 
def affiche_syntaxe():
    print("Syntaxe:")
    print("DERIVEES: /d^a [exp1 ]\d [exp2] ^b/  =>exp1,a,exp2,b   exemple /d^2 [v]\d [t] ^2/ donnera [L]^1 [T]^-3  ")
    # TODO


#affiche le resultat
def affiche(expression):
    print(">",expression,"=>",AD(expression))

def evalue(expression):
    affiche(expression)

# ajoute une expression  a la liste
def ajoute_var(expression):
    print("ajoute var ",expression)
    #TODO

dr="/d^2[w]\d[k]^3/"
#evalue("w k^5 Kb^3 "  )
#evalue("w k^5 Kb^3 "+dr  )
#print(dr,"=>",analyse_derivative(dr))
# programme principal
while 0: # 1 est toujours vrai -> boucle infinie
    
    lettre = input("Tapez 'Q' pour quitter, ? pour l'aide : ")
    if lettre == "Q":
        print("Fin de la boucle")
        break
    elif  lettre=="v?":
        affiche_variable_connues()
    elif  lettre=="?":
        affiche_aide()
    elif lettre=="s?":
        affiche_syntaxe()
    elif lettre.startswith("AD("):
        evalue(lettre)
    elif lettre.startswith("DEF "):
        ajoute_var(lettre)
    else:
        print("Erreur de syntaxe:",lettre)
