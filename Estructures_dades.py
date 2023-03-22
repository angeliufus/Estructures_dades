#!/usr/bin/env python
# coding: utf-8

# # TASCA M2 T01

# ## Exercici 1

# In[18]:


list_1T = ["Gener", "Febrer", "Març"]
list_2T = ["Abril", "Maig", "Juny"]
list_3T = ["Juliol", "Agost", "Setembre"]
list_4T = ["Octubre","Novembre","Desembre"]
ANY = [list_1T,list_2T,list_3T,list_4T]
print (ANY)


# ## Exercici 2

# In[20]:


print(list_1T[1])


# In[22]:


print(list_1T)


# In[24]:


print(list_3T[2],"i",list_4T[0])


# ## Exercici 3

# In[30]:


list_Angels = [1, 234, 35, 967, 678, 19, 23457]


# - Quants números hi ha?

# In[46]:


print("El nombre d'elements a la llista és: ",len(list_Angels))


# - Quantes vegades apareix el número 3.

# In[72]:


print("El numero 3 ha sortit:",list_Angels.count(3), "vegades")


# - Quantes vegades apareix els nombres 3 i 4

# In[80]:


print("El numero 3 i 4 hi surten:",list_Angels.count(3) or list_Angels.count(4), "vegades")


# - Quin és el número més gran?

# In[82]:


print("El nombre mes gran és el:", max(list_Angels))


# - Quins són els 3 números més petits?

# In[86]:


print("Els 3 nombres mes petits son:", sorted(list_Angels)[:3])


# - Quin és el rang d’aquesta llista?

# In[121]:


import random
random.sample(range (23458),7)


# In[123]:


print("Es una llista de nombres que he creat random i desordenat per tant en Python podriem fer aquesta formula important el modul random i per exemple amb : random.sample(range(23458), 7)")


# ## Exercici 4

# - Crea un diccionari de la següent forma i respon a les preguntes:

# In[252]:


compra = { "Pomes" : {"Qty": 5, "€": 0.42}, "Peres" : {"Qty": 3, "€": 0.66} }


# In[125]:


print(type(compra))


# - Afegeix alguna fruita més

# In[126]:


compra["Mangos"] = {"Qty": 4, "€": 2}


# In[130]:


print("Afegeixo mangos, que es una fruita tropical mes cara:", compra)


# - Quant han costat les peres en total?

# In[210]:


variables_peres = compra.get("Peres")

print(variables_peres)


# In[214]:


preu = ['€']
preu_peres = [variables_peres.get(key) for key in preu]
print("El preu de les peres és", preu_peres)


# In[215]:


quantitat = ['Qty']
quantitat_peres = [variables_peres.get(key) for key in quantitat]
print ("La quantitat de peres son", quantitat_peres)


# In[302]:


peres= compra["Peres"]
peresproduct = quantitat_peres[0] * preu_peres[0]
print("El preu total de les Peres és:", peresproduct,"€")


# - Quina és la fruita més cara?

# In[137]:


Fruita_mescara = max([int(i['€']) for i in compra.values()])


# In[138]:


print(Fruita_mescara,"€")


# In[191]:


preus_en_euros=[int(i['€']) for i in compra.values()]
print(preus_en_euros)


# In[192]:


noms_de_fruites=list(compra.keys())
print(noms_de_fruites)


# In[196]:


print("La fruita mes cara son els", noms_de_fruites[preus_en_euros.index(max(preus_en_euros))])


# In[ ]:




