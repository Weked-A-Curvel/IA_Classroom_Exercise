import random

class Logic(object):

    def update(self, sensors, actuators):
        
        if sensors.vision is not None:

            campoDeVisao = sensors.vision.see()

            '''lista=[campoDeVisao[0][1]/0,campoDeVisao[1][0]/1,campoDeVisao[2][1]/2,campoDeVisao[1][2]/3]
            ''negando esta diretriz o agente se moveu melhor, pq?'''
            up = campoDeVisao[2][1]
            down = campoDeVisao[0][1]
            left = campoDeVisao[1][0]
            right = campoDeVisao[1][2]

            if (up == '0' or (left != '0' and down != '0' and right != '0') or (down == 'x' and right == 'x') or (left == 'x' and down == 'x')):
                actuators.locomotor.moveUp()
            elif (left == '0' or (up != '0' and down != '0' and right != '0') or (down == 'x' and right == 'x') or (up == 'x' and right == 'x')):
                actuators.locomotor.moveLeft()
            elif (down == '0' or (up != '0' and left != '0' and right != '0') or (up == 'x' and left == 'x') or (up == 'x' and right == 'x')):
                actuators.locomotor.moveDown()
            elif (right == '0' or (up != '0' and left != '0' and down != '0') or (left == 'x' and down == 'x') or (up == 'x' and left == 'x')):
                actuators.locomotor.moveRight()
            
            '''
            if lista[2] == '0' or :
                actuators.locomotor.moveUp()
            if lista[1] == '0':
                actuators.locomotor.moveLeft()
            if lista[0] == '0':
                actuators.locomotor.moveDown()
            if lista[3] == '0':
                actuators.locomotor.moveRight()
            '''

                
        print(campoDeVisao)
        '''print(lista)'''


                
                
