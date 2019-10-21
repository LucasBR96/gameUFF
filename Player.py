import PPlay
from PPlay.Sprite import *
from Constantes import *

class Player( PPlay.sprite.Sprite ):

     def __init__( self , img_file , pos ):

          PPlay.sprite.Sprite.__init__(self , image_file = img_file ) #inicializando classe mãe
          
          #variaveis de movimento
          self.x = pos[0]
          self.y = pos[1]
          self.vx_andar = VELANDARPLAYER
          self.vx_correr = VELCORRERPLAYER
          self.vx = 0
          self.vy = 0
          self.caindo = False 

          #variaveis de vitalidade
          #variaveis de item
          
     ################################################################################################################
                                                  #METODOS DE MOVIMENTO#
     ################################################################################################################

     def pular( self ):
          self.vy = VELPLAYERPULO
          self.caindo = True #Pular é cair pra cima 
     
     def update_vy( self , dt ):
          '''
          Como o mineirinho não voa, serve tanto pra quando ele estiver pulando ou caindo
          Gravidade constante , então usa MUV 
          '''
          self.move_y( self.vy*dt )
          self.vy = self.vy + G*dt

     def update_movimentos( self , mov_escolhido , direc , dt ):
          '''
          este metodo é o unico do bloco de movimentos que deve ser chamado durante o game loop
          é chamdo a cada ciclo, e as chaves ão definidas no gameloop, pelo teclado. por exemplo:

          if teclado.key_pressed( 'space' ):
               mov_escolhido = PUL
               direc = None 
          
          elif teclado.key_pressed( 'left' ):
               direc = ESQ
               if teclado.key_pressed( 'shift' ):
                    mov_escolhido = CORR
               else
                    mov_escolhido = AND

          elif teclado.key_pressed( 'right' ):
               direc = DIR
               if teclado.key_pressed( 'shift' ):
                    mov_escolhido = CORR
               else
                    mov_escolhido = AND

          player.update_movimentos( mov_escolhido , direc , dt  )         
          '''

          self.move_x( self.vx*dt )
          if self.caindo:
               self.update_vy( dt )
          elif mov_escolhido == None:
               self.vx = 0
          elif mov_escolhido == CORR:
               self.vx = self.vx_correr*direc
          elif mov_escolhido == AND:
               self.vx = self.vx_andar*direc

     ################################################################################################################
                                                  #METODOS DE COLISAO#
     ################################################################################################################
     

     def checar_colisao_plataforma( self , plataforma_list ):

          result = None
          for p in plataforma_list:
               if self.collided_perfect( p ):
                    result = p
          return result     
     
     def checar_colisao_monstro( self , monstro_list ):

          result = None
          for m in monstro_list:
               if self.collided_perfect( m ):
                    result = m
          return result

     def checar_colisao_proj( self , proj_list ):
          
          result = None
          for m in proj_list:
               if self.collided_perfect( m ):
                    result = m
          return result
          
     
     def definir_colisao( self ,  outro ):
          '''
          este metodo só pode ser chamado quando tem-se a certeza da colisão com outro objeto
          seja ele inimigo , plataforma ou projetil

          '''

          centro_x = ( self.x + self.width )//2
          centro_y = ( self.y + self.height )//2
          pos1 = outro.x
          pos2 = outro.x + outro.width

          a = ( centro_x >= pos1 )
          b = ( pos2 >= centro_x )
          c = ( outro.y > centro_y )

          if a and b and c:
               result = DECIMA
          
          elif a and b:
               result = DEBAIXO

          elif not a:
               result = DAESQ
          
          elif not b:
               result = DADIR
          
          return result
          
     def lidar_colisao_plat( self , plataforma , flag ):

          if flag == DECIMA:
               self.y = plataforma.y - self.height
               self.vy = 0
               self.caindo = False

          elif flag == DEBAIXO:
               self.y = plataforma.y + plataforma.height
               self.vy = 0
          
          elif flag == DADIR:
               self.x = plataforma.x + plataforma.width
               self.vx = 0
          
          elif flag == DAESQ:
               self.x = plataforma.x - self.width
               self.vx = 0

     def lidar_colisao_inimigo( self , monstro , flag ):
          pass

     def lidar_colisao_projetil( self , proj , flag ):
          pass

     def update_colisoes( self , monstros, plataformas , projeteis ):

          plat = self.checar_colisao_plataforma( plataformas )
          if plat == None:
               self.caindo = True
          else:
               col = self.definir_colisao( plat )
               self.lidar_colisao_plat( plat , col )
          
          monstro = self.checar_colisao_monstro( monstros )
          if monstro != None:
               col = self.definir_colisao( monstro )
               self.lidar_colisao_inimigo( monstro , col )
          
          proj = self.checar_colisao_proj( projeteis )
          if proj != None:
               col = self.definir_colisao( proj )
               self.lidar_colisao_projetil( proj , col )


