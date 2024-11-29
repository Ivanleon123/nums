def nums_que_comencen_per(llista_noms, lletra):
    """Retorna el nombre de noms que comencen per la lletra especificada."""
    comptador = sum(1 for nom in llista_noms if nom.lower().startswith(lletra.lower()))
    return comptador

# Programa principal
def main():
    # Demanar a l'usuari que introdueixi una lletra
    lletra = input("Introdueix una lletra: ")
    
    # Comprovar que l'entrada sigui una única lletra
    if len(lletra) != 1 or not lletra.isalpha():
        print("Si us plau, introdueix només una lletra.")
        return

    # Llista de noms
    noms = ["Anna", "Maria", "Albert", "Pere", "Arnau", "Joaquim"]
    
    # Comptar i mostrar els noms que comencen per la lletra donada
    resultat = nums_que_comencen_per(noms, lletra)
    print(f"Noms que comencen per '{lletra}': {resultat}")

# Executar el programa
main()