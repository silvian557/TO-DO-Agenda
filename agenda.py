print("= = = = = Agenda TO-DO List = = = = =")
print("_" * 90)
print("1. Adauga task nou")
print("2. Finalizeaza un task (Sterge)")
print("3. Iesi")
print("_" * 90)

# Aici ținem minte task-urile tale
taskuri = []

while True:
    alegere = input("\nCe varianta alegi? : ")
    
    if alegere == "1":
        task = input("Super! Ce task iti propui? : ")
        taskuri = taskuri + [task]
        print("Task-urile tale actuale sunt:", taskuri)
        
    elif alegere == "2":
        if not taskuri:
            print("Nu ai niciun task în listă pe care să-l finalizezi!")
        else:
            print("Task-urile tale sunt:", taskuri)
            de_sters = input("Scrie exact numele task-ului pe care l-ai finalizat: ")
            
            # Construim o listă nouă folosind .lower() pentru a evita problema literelor mari/mici
            lista_noua = []
            for t in taskuri:
                if t.lower() != de_sters.lower():
                    lista_noua = lista_noua + [t]
                    
            taskuri = lista_noua
            print(f"Task-ul '{de_sters}' a fost finalizat și șters din listă!")
            print("Task-urile rămase:", taskuri)
            
    elif alegere == "3":
        print("Nu este nicio problema! Sa ai o zi buna!")
        break
        
    else:
        print("Introdu un număr valid din meniu!")
