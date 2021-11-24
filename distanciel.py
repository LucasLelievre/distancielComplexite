import random
import math

# Classe représentant une instance du problème MIN-MAKESPAN
class Instance:
    def __init__(self, machines, tasks):
        self.machines = machines
        self.tasks = tasks

# Calcule la borne inférieure maximum pour une instance
def borneInfMax(instance) :
    return max(instance.tasks)
# Calcule la borne inférieure moyenne pour une instance
def borneInfMoy(instance) :
    return sum(instance.tasks)/instance.machines

# Éxecute l'algorithme List Scheduling Algorithm sur l'instance donnée
def LSA(instance):
    # initialisation des machines à 0
    machines = []
    for i in range(instance.machines) :
        machines.append(0)

    for t in instance.tasks :
        # ajout de la durée de la tâche à la première machine disponible (la machine avec le plus petit total)
        machines[machines.index(min(machines))] += t

    return max(machines)

# Éxecute l'algorithme Largest Processing Timesur l'instance donnée
def LPT(instance):
    # Tri des tâches dans l'ordre décroissant
    instance.tasks.sort(reverse = True)
    # éxecution de LSA sur la liste triée
    return LSA(instance)

# Éxecute l'algorithme Random Machine Assignment sur l'instance donnée
def RMA(instance):
    # initialisation des machines à 0
    machines = []
    for i in range(instance.machines) :
        machines.append(0)

    for t in instance.tasks :
        # Ajout de l adurée de la tâche à une machine selectionnée aléatoirement
        machines[random.randrange(0, instance.machines)] += t

    return max(machines)

# Créé une instance de type Ip
def newIp(p):
    
    # nombre de machines
    machines = p*2
    print(machines, " machines")

    # liste des tâches
    tasks = []
    for i in range(4*p):
        # 4p tâches de durée 1
        tasks.append(1)
    for i in range(2*p*(p - 1)) :
        # 2p(p-1) tâches de durée 2
        tasks.append(2)
    # 1 tâche de durée 2p
    tasks.append(2*p)
    print((2*(p*p) + 2*p + 1), "tâches : ", tasks)

    # retourne une instance
    return Instance(machines, tasks)

# Créer une instance de type Ir
def newIr(m, n, dmin, dmax):
    print(m, "machines")
    # liste des tâches
    tasks = []
    for i in range(n) :
        tasks.append(random.randrange(dmin, dmax))
    print(n, "tâches :", tasks)

    return Instance(m, tasks)

def main():
    print("Bonjour !")
    print("Voulez-vous : ")
    print("1 - Génerer un instance de type Ip")
    print("2 - Générer aléatoirement plusieurs instances")
    choixMode = int(input("Entrez votre choix (1 ou 2) : "))

    # génération de l'instance selon le choix
    if choixMode == 1 :
        p = int(input("\nVeuillez entrer le nombre p de l'instance : "))
        
        instance = newIp(p)

        print("\nRésultats : \n")
        # Calcul des bornes inférieurs
        bMax = borneInfMax(instance)
        bMoy = borneInfMoy(instance)
        B = max(bMax, bMoy)
        print("Borne inférieure ``maximum´´ =", bMax)
        print("Borne inférieure ``moyenne´´ =", bMoy)
        print()
        resLSA = LSA(instance)
        print("Résultat LSA =", resLSA)
        print("ratio LSA =", resLSA/B)
        print()
        resLPT = LPT(instance)
        print("Résultat LPT =", resLPT)
        print("ratio LPT =", resLPT/B)
        print()
        resRMA = RMA(instance)
        print("Résultat RMA =", resRMA)
        print("ratio RMA =", resRMA/B)


    elif choixMode == 2 :
        print()
        m = int(input("Veuillez entrer le nombre de machines m : "))
        n = int(input("Veuillez entrer le nombre de tâches n : "))
        k = int(input("Veuillez entrer le nombre d'instances k : "))
        dmin = int(input("Veuillez entrer la durée minimum d'une tâche : "))
        dmax = int(input("Veuillez entrer le durée maximum d'une tâche : "))

        ratioLSA = 0
        ratioLPT = 0
        ratioRMA = 0
        
        for i in range(k) :
            print("instance", i)
            instance = newIr(m, n, dmin, dmax)
            bMax = borneInfMax(instance)
            bMoy = borneInfMoy(instance)
            B = max(bMax, bMoy)
            ratioLSA += (LSA(instance)/B)/k
            ratioLPT += (LPT(instance)/B)/k
            ratioRMA += (RMA(instance)/B)/k


        print()
        print("Résultats : ")
        print("ratio moyen LSA = ", ratioLSA)
        print("ratio moyen LPT = ", ratioLPT)
        print("ratio moyen RMA = ", ratioRMA)
    
    elif choixMode == 3 :
        print("générer quel batterie de tests ?")
        print("1: LSA, 2: LPT, 3:RMA, 4:Ir")
        choixMode = int(input())

        p_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 90, 100, 100, 120, 140, 160, 180, 200, 300, 350, 400, 450, 500, 550, 600, 700, 800, 900, 1000]
        file  = open("output.txt", "w")

        if choixMode == 1 :
            file.write("p\tratio LSA\n")
            for i in p_list :
                file.write(i)
                file.write("\t")

                instance = newIp(i)
                bMax = borneInfMax(instance)
                bMoy = borneInfMoy(instance)
                B = max(bMax, bMoy)
                res = LSA(instance)/B

                file.write(res)
                file.write("\n")
        if choixMode == 2 :
            file.write("p\tratio LPT\n")
            for i in p_list :
                file.write(i)
                file.write("\t")

                instance = newIp(i)
                bMax = borneInfMax(instance)
                bMoy = borneInfMoy(instance)
                B = max(bMax, bMoy)
                res = LPT(instance)/B

                file.write(res)
                file.write("\n")

        if choixMode == 3 :
            file.write("p\tratio RMA\n")
            for i in p_list :
                file.write(i)
                file.write("\t")

                instance = newIp(i)
                bMax = borneInfMax(instance)
                bMoy = borneInfMoy(instance)
                B = max(bMax, bMoy)
                res = RMA(instance)/B

                file.write(res)
                file.write("\n")

        if choixMode == 4 :
            file.write("m\tn\tk\tdmin\tdmax\tratio moyen LSA\tratio moyen LPT\tratio moyen RMA\n")
            for m in range(5, 30, 5):
                for n in range(m*3, m*3+60, 10):
                    k = m*2
                    dmin = math.ceil(m/4)
                    dmax = m*2
                    file.write(str(m))
                    file.write("\t")
                    file.write(str(n))
                    file.write("\t")
                    file.write(str(k))
                    file.write("\t")
                    file.write(str(dmin))
                    file.write("\t")
                    file.write(str(dmax))
                    file.write("\t")
                    ratioLSA = 0
                    ratioLPT = 0
                    ratioRMA = 0
                    for i in range(k) :
                        instance = newIr(m, n, dmin, dmax)
                        bMax = borneInfMax(instance)
                        bMoy = borneInfMoy(instance)
                        B = max(bMax, bMoy)
                        ratioLSA += (LSA(instance)/B)/k
                        ratioLPT += (LPT(instance)/B)/k
                        ratioRMA += (RMA(instance)/B)/k
                    file.write(str(ratioLSA))
                    file.write("\t")
                    file.write(str(ratioLPT))
                    file.write("\t")
                    file.write(str(ratioRMA))
                    file.write("\n")
        file.close()
    else :
        print("Veuillez choisir uniquement 1 ou 2")

main()
