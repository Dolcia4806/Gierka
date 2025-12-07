##Definicje postaci 
default player_name = "hero"
define ja = Character("[player_name]", who_color="#00ccff")
define r = Character("Radio",who_color="#1bdb8b")
define m = Character("???",who_color="#ff0000") # Potwór

## zmienne logiczne ( flagi) do śledzenia postępów
default ma_lom = False
default ma_bezpiecznik = False
default ma_karta_dostepu= False
default ma_mapa= False
default prad_wlaczony = False
default drzwi_wyjsciowe_otwarte = False
default zbrojownia_otwarta =False
default serwerownia_otwarta = False
default generator_otwarty= False

## ----TŁA---------
image bg start ="pokoj1"
image bg Korytaz ="Korytarz_no_light"
image bg stolowka ="stoufka"
image bg apteka1 ="apteka"
image bg apteka2 ="apteka2"
image bg generator_swiatlo ="generator_light"
image bg generator_no_swiatlo ="generator_no_light"
image bg serwerownia ="komputerownia"
image bg zbrojownia ="zbrojownia"
image bg drzwi_wyjsciowe ="drzwi_wyjscie"

# ----- START GRY--------
label start:
    scene bg start  
    "Budzi cię potworny ból głowy. Wokół panuje półmrok, a powietrze pachnie stęchlizną i metalem."
    "Próbujesz wstać, ale przez silne zawroty głowy, twoje ciało odmawia posłuszeństwa"
    "Przez silne zawroty wydaje ci się że słyszysz znajomy głos, ale nic ci nieprzychodzi do głowy"
    "Haloo, haloo???"
    ## play sound "audio/blablabla.ogg" #dzwięk zgaszenia światła
    show radio at right
    r "Odbiór. Raz, dwa, trzy. Czy ten kawał mięsa jeszcze funkcjonuje?"
    show hero_poczatek at left
    ja "Kto... Kto mówi? Gdzie ja jestem"
    r "Och. Wspaniale! Funkcje życiowe w normie, ale widzę usterkę w twojej pamięci..."
    r "Chyba za mocno ci wtedy przyjebałem.. No nic"
    r "Witaj w Bunkrze ... . Jestem Pan Radio. Twoim jedynym i ostatnim przyjacielem."
    label Choice:   
    menu:
        " "

        "Odpowiesz na moje pytanie?!" :
            hide hero_poczatek
            show hero_wkurw at left   
            ja "Kim jesteś! i co ja tu robie??!"
            hide hero_wkurw
            show hero_poczatek at left
            r "wyluzuuj! bo ci żyłka pęknie"
            r"Jak powiedziałem jestem i nazywam się Pan Radio"
            r"jak chcesz mogę być również Panią"
            hide radio
            show pani at right 
            r"Widzisz mam wiele wcieleń"
            r"Ha ha ha ha"
            hide pani 
            show radio at right
            
        "(Milcz)":  
            ja "Huuuh...?"
            
    #Kod tutaj wykonuje się po zakończeniu wyboru
    r "W każdym razie, cieszę się, że tu jesteś."
    r "Sytuacja jest prosta: drzwi są zamknięte, tlen się kończy a ja się nudzę. Wyjdź stąd, zanim zginiesz."
    r "A właśnie jak ci tam było?"
    $ player_name = renpy.input("Jak masz na imię? ", length=15).strip()
    if player_name == "":
        $ player_name = "hero"
    ja "Możesz na mnie mówić [player_name]"
    ja "Właśnie jak mam stąd wyjść"
    r "Eksploruj. Kombinuj. I na litość boską, nie dotykaj czerwonych przycisków......"
    hide radio    
    ja "Psia mać! muszę coś wykombinować bo oszaleje.."
    "Drzwi są zamknięte."
    hide hero_poczatek


    

   
