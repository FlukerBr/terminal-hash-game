from os import system
from random import randint

class game:
    def __init__(self) -> None:
        self.symbols = ['X', 'O']
        self.playerturn = randint(1, 2)
        self.slots = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ']
        self.won = False

    def show_hash(self):
        print(
        f"""

         1    |2    |3     
           {self.slots[0]}  |  {self.slots[1]}  |  {self.slots[2]}   
              |     |      
         -----|-----|----- 
         4    |5    |6     
           {self.slots[3]}  |  {self.slots[4]}  |  {self.slots[5]}   
              |     |      
         -----|-----|----- 
         7    |8    |9     
           {self.slots[6]}  |  {self.slots[7]}  |  {self.slots[8]}   
              |     |      

        """)

    def win_checker(self) -> bool:
        for s in self.symbols:
            if (self.slots[0], self.slots[1], self.slots[2]) == (s, s, s
            ) or (self.slots[3], self.slots[4], self.slots[5]) == (s, s, s
            ) or (self.slots[6], self.slots[7], self.slots[8]) == (s, s, s
            ) or (self.slots[0], self.slots[4], self.slots[8]) == (s, s, s
            ) or (self.slots[2], self.slots[4], self.slots[6]) == (s, s, s
            ) or (self.slots[0], self.slots[3], self.slots[6]) == (s, s, s
            ) or (self.slots[1], self.slots[4], self.slots[7]) == (s, s, s
            ) or (self.slots[2], self.slots[5], self.slots[8]) == (s, s, s):
                return True
        return False
system('cls')

while True:
    Game = game()
    input('Pressione qualquer tecla para continuar... ')
    system('cls')
    for _ in range(9):
        Game.show_hash()
        print(f'Jogador : {Game.symbols[Game.playerturn-1]}')
        slot = None

        while slot == None:
            try:
                slot = int(input('Escolha o lugar: '))
            except (ValueError, TypeError):
                print(f'Caractere inválido!')
                continue
            if slot < 10 and slot > 0:
                if Game.slots[slot-1] != ' ':
                    print('Área já está preenchida!')
                    slot = None
            else:
                print('Digite um número entre 1 e 9!')
                slot = None
        Game.slots[slot-1] = Game.symbols[Game.playerturn-1]
        system('cls')
        if Game.win_checker():
            print(f'Jogador {Game.symbols[Game.playerturn-1]} ganhou!!!')
            break
        Game.playerturn = 1 if Game.playerturn == 2 else 2