Models

pentru relatia 1 to 1
pet-owner am pus sa se stearga pets daca e ster ownerul
pet-species daca se sterge specia, fieldul de FK va deveni null

pentru relatia many to many intre pet si treat am mai creat un tabel intermediar


la species am folosit choices
la pet  - am adaugat constraint pentru data
        - am mai creat o metoda in PetManager - doar de test sa returneze pet cu fun_name
        - la pet am mai facut un validator care sa nu lase crearea unei instante cu numele "bob"


Serializers

majoritatea au toate campurile

La owner am mai facut unul care serializeaza doar first si last name

La pet am pus sa serializeze si ownerul si species nu doar id-ul


Urls

cu default router si register

Views 
Aici am luat pe pasi
-function views
-class views - ApiView
             -mixins
             -generics
             -modelViewSets

- pe langa crud-ul facut automat am mai facut un filter, search
-am adaugat metode pentru test cu @action
