init python:
    # 1. Definicja samego przedmiotu (statystyki + wygląd)
    class Item:
        def __init__(self, name, idle_img, hover_img):
            self.name = name
            self.idle_img = idle_img   # Obrazek normalny
            self.hover_img = hover_img # Obrazek po najechaniu myszką

    # 2. Pomocnicza klasa dla przedmiotu leżącego w plecaku (Przedmiot + Pozycja)
    class InventorySlot:
        def __init__(self, item, x, y):
            self.item = item
            self.x = x
            self.y = y

    # 3. Zarządzanie ekwipunkiem
    class Inventory:
        def __init__(self):
            self.slots = [] # Lista przedmiotów wraz z ich pozycjami

        # Metoda dodawania wymaga teraz podania pozycji X i Y
        def add(self, item, x, y):
            new_slot = InventorySlot(item, x, y)
            self.slots.append(new_slot)
            renpy.notify(f"Znaleziono: {item.name}")

        def remove(self, slot):
            if slot in self.slots:
                self.slots.remove(slot)

---------------------- INVENTORY---------------------------------------

screen messy_inventory():
    modal True
    
    # Półprzezroczyste tło
    add Solid("#5bc4adaa")

    # Obszar plecaka (np. grafika otwartej torby)
    frame:
        align (0.5, 0.5)
        xsize 800
        ysize 600
        background Solid("#333333") # Tu wstawisz tło np. "bag_bg.png"

        text "Mój Bałagan" xalign 0.5 yalign 0.05 color "#FFF"

        # Kontener 'fixed' pozwala na swobodne rozmieszczanie dzieci
        fixed:
            # Iterujemy przez wszystkie przedmioty w plecaku
            for slot in backpack.slots:
                
                imagebutton:
                    # Wygląd
                    idle slot.item.idle_img
                    hover slot.item.hover_img
                    
                    # Pozycja (bierzemy z obiektu InventorySlot)
                    pos (slot.x, slot.y)
                    
                    # Dźwięk po najechaniu (opcjonalnie)
                    hover_sound "audio/click.ogg" 
                    
                    # Akcja po kliknięciu (np. usunięcie lub opis)
                    action Return(slot.item.name) 
                    
                    # Tooltip (dymek z nazwą po najechaniu)
                    tooltip slot.item.name

            # Obsługa tooltipa (wyświetla nazwę przedmiotu, na który najechałeś)
            $ tooltip = GetTooltip()
            if tooltip:
                text "[tooltip]":
                    color "#FFF"
                    outlines [(2, "#000", 0, 0)]
                    pos (renpy.get_mouse_pos()) # Tekst podąża za myszką
                    yoffset -30

    # Przycisk wyjścia
    textbutton "Zamknij":
        align (0.9, 0.1)
        action Hide("messy_inventory")