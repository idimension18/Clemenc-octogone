from DATA.utilities.Base_Char import Char, Hitbox, change_left, signe
import pygame
from math import pi

##### Poissonnier

class Poissonnier(Char):
    def __init__(self,x,y,player) -> None:
        super().__init__(speed=2, dashspeed=3, airspeed=1.7, deceleration=0.78, fallspeed=1, fastfallspeed=1.8, fullhop=13, shorthop=10,
                         doublejumpheight=15,airdodgespeed=6,airdodgetime=3,dodgeduration=15)

        self.rect = pygame.Rect(100,0,48,120) # Crée le rectangle de perso
        self.jumpsound = pygame.mixer.Sound("DATA/Musics/jump.wav") # Son test
        self.name = "Poissonnier"
        self.x = x
        self.rect.y = y
        self.player = player
    
    def __str__(self) -> str:
        return "Poissonnier"

    def special(self): 
        pass

    def animation_attack(self,attack,inputs,stage,other):
        left, right, up, down, fullhop, shorthop, attack_button, special, shield, C_Left, C_Right, C_Up, C_Down, D_Left, D_Right, D_Up, D_Down = inputs # dissociation des inputs
        smash = C_Down or C_Left or C_Right or C_Up
        if attack == "UpB":
            if self.frame == 11: # Saute frame 11
                self.can_act = False # ne peut pas agir après un grounded up B
                self.vy = -20
                self.attack = None
                self.doublejump = [True for _ in self.doublejump] # Annule tout les sauts
            #if self.frame < 6 :
            #    if left : # peut reverse netre les frames 1 et 5
            #        self.look_right = False
            #    if right :
            #        self.look_right = True
            #if self.frame == 6: # Hitbox frame 6-11
            #    self.active_hitboxes.append(Hitbox(-1.5,88.5,51,48,2*pi/3,18,32,1/150,40,5,self,False))

        if attack == "NeutralB":
            if self.frame > 15: # 10 frames de lag
                self.attack = None
                self.charge = 0

        if attack == "DownB":
            if self.frame > 20 : # 15 frames de lag
                self.attack = None
                self.charge = 0

        if attack == "SideB":
            if self.frame > 80 : # 20 frames de lag
                self.attack = None

        if attack == "Jab":

            if self.frame > 22: # 10 frames de lag
                self.attack = None

        if attack == "DownTilt":
            if self.frame == 8 :
                self.active_hitboxes.append(Hitbox(50,100,84,32,pi/5,8,6.2,1/101,9,2,self,boum=7,deflect=True,modifier=0.5))

            if self.frame > 20: # 7 frames de lag
                self.attack = None

        if attack == "ForwardTilt":
            if self.frame < 3 :
                if left :
                    self.look_right = False
                if right :
                    self.look_right = True
            if self.frame == 12 :
                self.active_hitboxes.append(Hitbox(50,50,84,32,pi/10,10,11.1,1/101,11,2,self,boum=7,deflect=True,modifier=1.01))

            if self.frame > 40: # 25 frames de lag
                self.attack = None

        if attack == "UpTilt":
            if self.frame == 10 :
                self.active_hitboxes.append(Hitbox(50,50,72,32,4*pi/11,14,14.9,1/101,14,2,self,boum=7,deflect=True,modifier=1.3))
            if self.frame == 11 :
                self.active_hitboxes.append(Hitbox(30,-75,64,64,pi/2,9,9.9,1/101,12,3,self,boum=5,deflect=True,modifier=0.1))
            if self.frame > 11 and self.frame < 14 :
                if self.active_hitboxes :
                    self.active_hitboxes[-1].sizex += 30
                    if self.look_right :
                        self.active_hitboxes[-1].relativex -= 30
            if self.frame == 14 :
                self.active_hitboxes.append(Hitbox(change_left(50,72),50,72,32,7*pi/11,14,14.9,1/101,14,2,self,boum=7,deflect=True,modifier=1.3))
            if self.frame > 25: # 11 Frames de lag
                self.attack = None

        if attack == "UpAir":

            if self.frame > 25: # 10 frames de lag
                self.attack = None

            if self.grounded :
                self.attack = None
                if self.frame < 15 :
                    self.lag = self.frame-2 # Auto cancel frame 1-2 et 15+

        if attack == "ForwardAir":

            if self.frame > 50: # 29 frames de lag
                self.attack = None

            if self.grounded :
                self.attack = None
                if self.frame < 40 :
                    self.lag = self.frame-3 # Auto cancel frame 1-3 et 40+

        if attack == "BackAir":

            if self.frame > 25: # 14 frames de lag
                self.attack = None

            if self.grounded :
                self.attack = None
                if self.frame < 20 :
                    self.lag = self.frame-2 # Auto cancel frame 1-2 et 20+

        if attack == "DownAir":

            if self.frame > 25: # 10 frames de lag
                self.attack = None

            if self.grounded :
                self.attack = None
                if self.frame < 20 :
                    self.lag = self.frame-5 # Auto cancel frame 1-5 et 20+

        if attack == "NeutralAir":

            if self.frame > 40: # 17 frames de lag
                self.attack = None

            if self.grounded :
                self.attack = None
                if self.frame < 30 :
                    self.lag = self.frame-2 # Auto cancel frame 1-2 et 30+

        if attack == "ForwardSmash":
            if self.frame > 4 and self.frame < 7 and smash and self.charge < 200 : # Chargement jusqu'à 200 frames
                self.frame = 5
                self.animeframe -= 1
                self.charge = self.charge+1
            if self.frame == 24 :
                self.charge = min(self.charge,100)
                self.active_hitboxes.append(Hitbox(42,42,64,64,pi/4,28+5*(self.charge/100),24.2,1/101,27+5*(self.charge/100),3,self,boum=12))
            if self.frame > 55: # 30 frames de lag
                self.attack = None
                self.charge = 0

        if attack == "UpSmash":

            if self.frame < 5 :
                if left : # peut reverse netre les frames 1 et 5
                    self.look_right = False
                if right :
                    self.look_right = True
            if self.frame > 4 and self.frame < 8  and smash and self.charge < 200 : # Chargement jusqu'à 200 frames
                self.animeframe -= 1
                self.frame = 5
                self.charge = self.charge+1
            if self.frame == 15 :
                self.vy = -14
                self.active_hitboxes.append(Hitbox(-2,-30,52,42,pi/2,22+2*(self.charge/100),20.4,1/101,19+8*(self.charge/100),10,self,boum=3))
            if self.frame > 15 :
                self.vy += 1

            if self.frame > 50: # 25 frames de lag
                self.attack = None
                self.charge = 0

        if attack == "DownSmash":

            if self.frame < 3 :
                if left : # peut reverse netre les frames 1 et 2
                    self.look_right = False
                if right :
                    self.look_right = True
            if self.frame > 20 and self.frame < 23 and smash and self.charge < 200 : # Chargement jusqu'à 200 frames
                self.frame = 21
                self.animeframe -= 1
                self.charge = self.charge+1
            if self.frame == 30 :
                self.charge = min(self.charge,100)
                self.active_hitboxes.append(Hitbox(10,-82,32,84,pi/9,22+8*(self.charge/100),22.2,1/101,24+9*(self.charge/100),6,self,boum=11,deflect=True,modifier=1.5))
            if self.frame > 30 and self.active_hitboxes:
                self.active_hitboxes[-1].relativex += 12*signe(self.direction)
                self.active_hitboxes[-1].relativey += 24+(self.frame-30)*7
                self.active_hitboxes[-1].sizey -= 10
                self.active_hitboxes[-1].sizex += 10
                if not self.look_right :
                    self.active_hitboxes[-1].relativex -= 10
            if self.frame > 70: # 40 frames de lag
                self.attack = None
                self.charge = 0

        if attack == "DashAttack":
            if self.frame < 26 :
                self.vy = 0
                if self.grounded :
                    self.vx += self.dashspeed*signe(self.direction)
                else :
                    self.vx -= self.dashspeed*signe(self.direction)
            if self.frame > 9 and self.frame%3 == 1 and self.frame < 23:
                self.active_hitboxes.append(Hitbox(-20,5,88,88,pi/4,3,2,1/1000,4,2,self,boum=3))
            if self.frame == 25 :
                self.active_hitboxes.append(Hitbox(-20,5,88,88,pi/5,10,4,1/101,9,2,self,boum=4))
            if self.frame > 50: # 25 frames de lag
                self.attack = None

        if attack == "UpTaunt":
            
            if self.frame > 30: # Durée de 30 frames
                self.attack = None

        if attack == "DownTaunt":
            
            if self.frame > 30: # Durée de 30 frames
                self.attack = None

        if attack == "LeftTaunt":
            
            if self.frame > 30: # Durée de 30 frames
                self.attack = None

        if attack == "RightTaunt":
            
            if self.frame > 30: # Durée de 30 frames
                self.attack = None

###################          
""" Projectiles """
###################

##### Autres skins
