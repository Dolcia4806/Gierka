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
    
    "Budzi mnie potworny ból głowy. Wokół panuje półmrok, a powietrze pachnie stęchlizną i metalem."
    "Próbuję wstać, ale kręci mi się w głowie."
    ## play sound "audio/blablabla.ogg" #dzwięk zgaszenia światła
    show radio at right
    r "Odbiór. Raz, dwa, trzy. Czy ten kawał mięsa już funkcjonuje?"
    show hero_poczatek at left
    ja "Kto... Kto mówi? Gdzie ja jestem"
    r "Och. Wspaniale! Funkcje życiowe w normie. Witaj w Bunkrze ... . Jestem Pan Radio. Twoim jedynym przyjacielem."
    r "Sytuacja jest prosta: drzwi są zamknięte, tlen się kończy a ja się nudzę. Wyjdź stąd, zanim zginiesz."
    r "A właśnie jak ci tam było?"
    $ player_name = renpy.input("Jak masz na imię? ", length=15).strip()
    if player_name == "":
        $ player_name = "hero"
    ja "Możesz na mnie mówić [player_name]"
    ja "Właśnie jak mam stąd wyjść"
    r "Eksploruj. Kombinuj. I na litość boską, nie dotykaj czerwonych przycisków......"
    hide radio    
    "Drzwi od mojego pokoju są zamknięte. Co chcesz zrobić?"






JEBNAL PRONT
TŁO




































### show radio at right
###radio"Witaj w moim świecie! Zanim zaczniemy, powiedz mi, jak się nazywasz?" ## $ player_name = renpy.input("Jak masz na imię?", length=15).strip()
    ##    $ player_name = "hero"
    #show hero_poczatek at left
    #hero"Możesz na mnie mówić [player_name]."
    #radio "dobrze więc"
    #hero "milczy"
    #radio "wyglądasz na przygnębionego. Wszystko w porządku?"

    #label Choice:   
# menu:
#     "Co jej odpowiesz?"
#   "Nic mi nie jest. Po prostu się zamyśliłem.":  #            
#           hero "Nie, wszystko w porządku. Po prostu... zamyśliłem się na chwilę."
    ####Szczerze? Nie czuję się najlepiej.":
                
    #     3      hero "Jeśli mam być szczery, to nie jest to mój najlepszy dzień."
    #       3     radio "Och... Chcesz o tym porozmawiać?"

            # OPCJA 3
            ##      "(Milcz)":
            
    #          hero "..."
##
    # Kod tutaj wykonuje się po zakończeniu wyboru
    #radio "W każdym razie, cieszę się, że tu jesteś."

   
