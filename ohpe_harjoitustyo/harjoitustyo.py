# Pääohjelma
def main():
    #Ladataan tiedostot. Jos niitä ei ole olemassa, luodaan ne.
    try:
        naytokset = open("naytokset.txt", "x")
        naytokset.close()
    except FileExistsError:
        pass

    try:
        varaukset = open("varaukset.txt", "x")
        varaukset.close()
    except FileExistsError:
        pass

    #Tulostetaan käyttöliittymä
    print("Tervetuloa elokuvateatterin varausjärjestelmään!\n")

    print("Valitse käyttöliittymä:")
    print("1) Asiakas")
    print("2) Ylläpitäjä")
    valinta = input("Valintasi: ")

    #Asiakkaan käyttöliittymä
    if valinta == "1":
        print("Olet asiakkaan käyttöliittymässä.\n")
        while True:
            print("Mitä haluat tehdä?")
            print("1) Selaa elokuvia")
            print("2) Tee varaus")
            print("0) Lopeta")
            valinta = input("Valintasi: ")

            if valinta == "1":
                selaa_elokuvia()

            elif valinta == "2":
                tee_varaus()

            elif valinta == "0":
                print("Kiitos ohjelman käytöstä!")
                exit()

            else:
                print("Virheellinen syöte.\n")
        
    #Ylläpitäjän käyttöliittymä
    elif valinta == "2":
        print("Olet ylläpitäjän käyttöliittymässä.\n")

        while True:
            print("Mitä haluat tehdä?")
            print("1) Lisää elokuva ja näytösaika")
            print("2) Selaa elokuvia ja varauksia")
            print("0) Lopeta")
            valinta = input("Valintasi: ")

            if valinta == "1":
                lisaa_elokuva()

            elif valinta == "2":
                selaa_varauksia()

            elif valinta == "0":
                print("Kiitos ohjelman käytöstä!")
                exit()

            else:
                print("Virheellinen syöte.\n")

    else:
        print("Virheellinen syöte.\n")

# Ylläpitäjän käyttöliittymä, jossa voi lisätä elokuvan
def lisaa_elokuva():
    #Lisätään elokuva ja näytösaika naytokset.txt-tiedostoon

    elokuva = input("Anna elokuvan nimi: ")
    
    print("Anna alkamisaika muodossa hh:mm")

    alkamisaika = input("Alkamisaika: ")

    naytokset = open("naytokset.txt", "a")
    naytokset.write(elokuva + " " + alkamisaika + "\n")
    naytokset.close()

    print("\nElokuva lisätty onnistuneesti.\n")

# Tulostaa elokuvat ja varaukset ylläpitäjälle
def selaa_varauksia():
    print("Elokuvat:")
    
    # Lue naytokset.txt-tiedosto ja tallenna elokuvat sanakirjaan
    naytokset = open("naytokset.txt", "r")

    sisalto = naytokset.read()
    print(sisalto)

    if not sisalto:
        print("Ei elokuvia.\n")
        naytokset.close()
    
    else:

        elokuvat = {}
        for line in naytokset:
            naytos = line.strip().split(" ")
            elokuva = naytos[0]
            aika = naytos[1]

            # Lisää elokuva sanakirjaan, jos sitä ei ole vielä
            if elokuva not in elokuvat:
                elokuvat[elokuva] = []
            elokuvat[elokuva].append(aika)
        naytokset.close()
        
        # Tulosta näytökset jokaiselle elokuvalle
        for elokuva, naytokset in elokuvat.items():
            print()
            print(f"{elokuva}:")
            for naytos in naytokset:
                print(f"  {naytos}", end=" ")
                print()

    print("Varaukset:")
    
    # Lue varaukset.txt-tiedosto ja tallenna varaukset sanakirjaan
    varaukset = open("varaukset.txt", "r")

    if not sisalto:
        print("Ei varauksia.\n")
        varaukset.close()

    else:
        # Sanakirja, jossa avaimena on elokuva ja näytös ja arvona on lista
        varaukset_dict = {}
        for line in varaukset:
            varaus = line.strip().split(" ")
            elokuva = varaus[0]
            aika = varaus[1]
            teatteri = varaus[2]
            liput = varaus[3]
            if (elokuva, aika) not in varaukset_dict:
                varaukset_dict[(elokuva, aika)] = []
            varaukset_dict[(elokuva, aika)].append((teatteri, liput))
        varaukset.close()
        
        # Tulosta varaukset jokaiselle elokuvalle
        for (elokuva, aika), teatterit in varaukset_dict.items():
            print(f"{elokuva} ({aika}):")
            for teatteri, liput in teatterit:
                print(f"  {teatteri}: {liput} lippua\n")

# Tämä funktio tulostaa elokuvat ja näytökset
def selaa_elokuvia():
    print("\nNäytökset:")

    naytokset = open("naytokset.txt", "r")
    sisalto = naytokset.read()
    naytokset.close()

    if not sisalto:
        print("Ei elokuvia! Ota yhteyttä ylläpitäjään.\n")

    else:
        # Lue naytokset.txt-tiedosto ja tallenna näytökset sanakirjaan
        elokuvat = {}

        for line in sisalto.split("\n"):
            naytos = line.strip().split(" ")

            if len(naytos) >= 2:  # Tarkista, että rivillä on oikea määrä tietoja
                elokuva = naytos[0]
                aika = naytos[1]

                if elokuva not in elokuvat:
                    elokuvat[elokuva] = []
                elokuvat[elokuva].append(aika)

        # Tulosta näytökset jokaiselle elokuvalle
        for elokuva, naytokset in elokuvat.items():
            print()
            print(f"{elokuva}:")

            for naytos in naytokset:
                print(f"  {naytos}", end=" ")
            print()
        print()

# Funktio varausten tekemiseen
def tee_varaus():
    # Tarkistetaan, onko elokuvia
    naytokset = open("naytokset.txt", "r")
    sisalto = naytokset.read()
    naytokset.close()

    if not sisalto:
        print("Ei elokuvia! Ota yhteyttä ylläpitäjään.\n")
        return

    # Teatterit ja niiden kapasiteetti
    teatterit = {"Pieni": 10, "Keskikokoinen": 15, "Iso": 20}

    # Kysy käyttäjältä elokuva ja alkamisaika
    elokuva = input("Anna elokuvan nimi: ")
    alkamisaika = input("Anna alkamisaika muodossa hh:mm: ")

    # Tarkistetaan, että elokuva ja alkamisaika ovat oikein
    naytokset = open("naytokset.txt", "r")
    aika_ok = False
    for line in naytokset:
        naytos = line.strip().split(" ")
        if naytos[0] == elokuva and naytos[1] == alkamisaika:
            aika_ok = True
            break
    naytokset.close()

    if not aika_ok:
        print("Virheellinen elokuva tai alkamisaika.\n")
        return

    # Näyttää käyttäjälle teatterit ja niiden vapaiden paikkojen määrä
    print("\nValitse teatteri:")
    for teatteri, paikat in teatterit.items():
        varaukset = open("varaukset.txt", "r")
        vapaita_paikkoja = paikat

        # Vähentää vapaiden paikkojen määrää, jos teatterissa on varauksia
        for line in varaukset:
            varaus = line.strip().split(" ")
            if varaus[0] == elokuva and varaus[1] == alkamisaika and varaus[2] == teatteri:
                vapaita_paikkoja -= int(varaus[3])
        varaukset.close()
        print(f"  {teatteri} ({vapaita_paikkoja} paikkaa jäljellä)")

    # Kysy käyttäjältä teatterin valinta
    teatteri_valinta = input("Valitse teatteri: ")

    teatteri_valinta = teatteri_valinta.lower()

    # Valitaan teatteri
    if teatteri_valinta == "pieni":
        teatteri = "Pieni"
    elif teatteri_valinta == "keski":
        teatteri = "Keskikokoinen"
    elif teatteri_valinta == "iso":
        teatteri = "Iso"
    else:
        print("Virheellinen syöte.\n")
        return

    # Kysy käyttäjältä lipunmäärä
    liput = input("\nMontako lippua haluat varata: ")

    # Tarkista onko tarpeeksi vapaita paikkoja
    varaukset = open("varaukset.txt", "r")
    vapaita_paikkoja = teatterit[teatteri]
    for line in varaukset:
        varaus = line.strip().split(" ")
        if varaus[0] == elokuva and varaus[1] == alkamisaika and varaus[2] == teatteri:
            vapaita_paikkoja -= int(varaus[3])
    varaukset.close()

    if vapaita_paikkoja < int(liput):
        print("Ei tarpeeksi paikkoja saatavilla.\n")
        return

    # Tallenna varaus tiedostoon
    varaukset = open("varaukset.txt", "a")
    varaukset.write(elokuva + " " + alkamisaika + " " + teatteri + " " + liput + "\n")
    varaukset.close()

    print("Varaus tehty.\n")

# Pääohjelma kutsu
main()