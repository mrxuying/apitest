import pygame
from pygame.locals import *
import time
import random


class HeroPlan(object):
            def __init__(self,screen_temp):
                        self.x = 190
                        self.y = 700
                        self.image = pygame.image.load('./feiji/hero.gif')
                        self.screen = screen_temp
                        self.bullet_list = []

                        
            def display(self):
                        self.screen.blit(self.image,(self.x,self.y))
                        for bullet in self.bullet_list:
                                    bullet.display()
                                    bullet.move()
                                    if  bullet.judge():
                                                self.bullet_list.remove(bullet)

            def fire(self,x,y):
                      self.bullet_list.append(Bullet(self.screen,x,y))
                      
            def move(self):
                        for event in pygame.event.get():
                                    #判断是否点击了退出按钮
                                    if event.type == QUIT:
                                                print("exit")
                                                exit()
                                    elif event.type == KEYDOWN:
                                                if event.key == K_a or event.key == K_LEFT:
                                                            print("left")
                                                            self.x -= 5
                                                elif event.key == K_d or event.key == K_RIGHT:
                                                            print('right')
                                                            self.x += 5
                                                elif event.key == K_w or event.key == K_UP:
                                                            print('UP')
                                                            self.y -= 5
                                                elif event.key == K_s or event.key == K_DOWN:
                                                            print('down')
                                                            self.y += 5
                                                elif event.key == K_SPACE:
                                                            self.fire(self.x + 40,self.y - 20)

class Bullet(object):
            def __init__(self,screen_temp,x_temp,y_temp):
                        self.x = x_temp
                        self.y = y_temp
                        self.screen = screen_temp
                        self.image = pygame.image.load('./feiji/bullet.png')

                        
            def display(self):
                        self.screen.blit(self.image,(self.x,self.y))

            def move(self):
                        self.y -= 5

            
            def judge(self):
                        if self.y < 0:
                                    return True
                        else:
                                    return False

class EnemyPlan(object):
            def __init__(self,screen_temp):
                        self.enemy = pygame.image.load('./feiji/enemy0.png')
                        self.x = random.randint(0,431)
                        self.y = -40
                        self.screen = screen_temp
                        self.enemy_list = [self.enemy]


            def display(self):
                        for enemy in self.enemy_list:  
                                    self.screen.blit(enemy,(self.x,self.y))
                                    self.y += 2
                                    if len(self.enemy_list)<= 3:
                                                self.enemy_list.append(self.enemy)
                                                self.display()


                        
            
def main():

            #1.创建一个窗口，用来显示内容；
            screen = pygame.display.set_mode((480,852),0,32)

            #2.创建一个和窗口图片一样大小的图片，用来充当背景；
            background = pygame.image.load("./feiji/background.png")

            #创建一个飞机
            hero = HeroPlan(screen)

            #创建一个敌机
            enemy = EnemyPlan(screen)
            
            #3.把背景图片放到窗口中显示
            while True:
                        #设定需要显示的背景图
                        screen.blit(background,(0,0))
                        
                        hero.display()
                        enemy.display()

                        
                        #x += 1
                        #设定需要显示的内容
                        pygame.display.update()
                        time.sleep(0.01)
                        hero.move()
                        #获取事件；
                       



if __name__ == '__main__':
            main()
