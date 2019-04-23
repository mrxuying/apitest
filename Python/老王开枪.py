class Person(object):
            def __init__(self,name):
                        super(Person,self).__init__()
                        self.name = name
                        self.hp = 100
                        self.gun = None
                        

            
            def add_bullet(self,bullet_temp,bullet_bag_temp):
                        bullet_bag_temp.add_bullet_in(bullet_temp)
                        
            def add_bulletbag(self,gun_temp,bulletbag_temp):
                        gun_temp.add_bulletbag(bulletbag_temp)

            def get_gun(self,gun_temp):
                        self.gun = gun_temp

            def shoot(self,enemy_temp,bullet):
                        self.gun.shoot(enemy_temp,bullet)

            def get_hurt(self,power_temp):
                        self.hp -= power_temp

            def __str__(self):
                        if self.gun and self.hp > 0:
                                    return '%s的血量是%d,有枪'%(self.name,self.hp)
                        elif self.hp <= 0:
                                    return '%s is dead!!'%(self.name)
                        else:
                                    return '%s 的血量是%d，没有枪'%(self.name,self.hp)
                        
                        
class Gun(object):
            def __init__(self,gun_type):
                        super(Gun,self).__init__()
                        self.gun_type = gun_type
                        self.bulletbag = None
                        

            def __str__(self):
                        if self.bulletbag:
                                    return '这把枪是%s,装上了弹夹'%(self.gun_type)
                        else:
                                    return '这把枪是%s,没装弹夹'%(self.gun_type)
                        
            def add_bulletbag(self,bulletbag_temp):
                        self.bulletbag = bulletbag_temp

            def shoot(self,enemy_temp,bullet):
                        self.bulletbag.shoot(enemy_temp,bullet)


class BulletBag(object):
            def __init__(self,max_num):
                        super(BulletBag,self).__init__()
                        self.max_num = max_num
                        self.bullet_list = []
                        
            def add_bullet_in(self,bullet_in):
                        self.bullet_list.append(bullet_in)

            def __str__(self):
                        if self.bullet_list:
                                    return '子弹数量：%d/%d'%(len(self.bullet_list),self.max_num)
                        else:
                                    return '没有子弹'

            def shoot(self,enemy_temp,bullet):
                        if self.bullet_list:
                                    bullet.shoot(enemy_temp)
                                    self.bullet_list.pop()
                                    

class Bullet(object):
            def __init__(self,power):
                        super(Bullet,self).__init__()
                        self.power = power

            def shoot(self,enemy_temp):
                        enemy_temp.get_hurt(self.power)

def main():
            
            '''主函数'''
            #1.创建一个老王的对象
            laowang  = Person('老王')
           
            #2.创建一个枪的对象
            ak47 =  Gun('AK47')
            
            #3.创建一个弹夹对象
            bullet_bag =  BulletBag(20)
            
            #4.创建子弹
            bullet = Bullet(20)
           
            #5.创建一个敌人
            enemy = Person('敌人')
            print(enemy)

            #6.老王把子弹安装到弹夹中
            for num in range(15):
                        laowang.add_bullet(bullet,bullet_bag)
            

            #7.老王把弹夹安装到枪中
            laowang.add_bulletbag(ak47,bullet_bag)
            print(ak47)
            #8.老王拿枪
            laowang.get_gun(ak47)
##            print(laowang)
##            print(bullet_bag)

            #9.老王拿枪打敌人
            laowang.shoot(enemy,bullet)
            print(laowang)
            print(bullet_bag)
            print(enemy)
            laowang.shoot(enemy,bullet)
            print(laowang)
            print(bullet_bag)
            print(enemy)
            laowang.shoot(enemy,bullet)
            print(laowang)
            print(bullet_bag)
            print(enemy)
            laowang.shoot(enemy,bullet)
            print(laowang)
            print(bullet_bag)
            print(enemy)
            laowang.shoot(enemy,bullet)
            print(laowang)
            print(bullet_bag)
            print(enemy)
            laowang.shoot(enemy,bullet)
            print(laowang)
            print(bullet_bag)
            print(enemy)

if __name__ == '__main__':
            main()
