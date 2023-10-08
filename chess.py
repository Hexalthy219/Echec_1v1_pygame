import pygame
import math
import random
import socket
import pickle

NOIR    = (0, 0, 0)
BLANC   = (255, 255, 255)
GRIS    = (110, 113, 127)
ROUGE   = (255, 0, 0)
BLEU    = (10, 147, 228)
JAUNE   = (235, 235, 0)
VERT    = (75, 195, 0)
VERT_MANGE = (150, 195, 0)


FENETRE_HAUTEUR = 1000
FENETRE_LARGEUR = 800


fini = False
ensemble_pieces = []
echiquier = [[],[],[],[],[],[],[],[]]
selection = []
joueur = 0

#---Initialisation---#

def initialisation():
    initialisationEchiquier()
    initialisationPieces()

def initialisationEchiquier():
    global echiquier
    for i in range(8):
        for j in range(8):
            if i%2 and j%2 or ((not i%2) and (not j%2)):
                echiquier[i].append(nouvelleCase("noir"))
            else:
                echiquier[i].append(nouvelleCase("blanc"))

def initialisationPieces():
    global ensemble_pieces, echiquier
    image_pion_noir = pygame.image.load('pion_noir.png').convert_alpha(fenetre)
    image_pion_noir = pygame.transform.smoothscale(image_pion_noir, (100, 100))
    
    image_cavalier_noir = pygame.image.load('cavalier_noir.png').convert_alpha(fenetre)
    image_cavalier_noir = pygame.transform.smoothscale(image_cavalier_noir, (100, 100))
    
    image_fou_noir = pygame.image.load('fou_noir.png').convert_alpha(fenetre)
    image_fou_noir = pygame.transform.smoothscale(image_fou_noir, (100, 100))
    
    image_tour_noir = pygame.image.load('tour_noir.png').convert_alpha(fenetre)
    image_tour_noir = pygame.transform.smoothscale(image_tour_noir, (100, 100))
    
    image_dame_noir = pygame.image.load('dame_noir.png').convert_alpha(fenetre)
    image_dame_noir = pygame.transform.smoothscale(image_dame_noir, (100, 100))
    
    image_roi_noir = pygame.image.load('roi_noir.png').convert_alpha(fenetre)
    image_roi_noir = pygame.transform.smoothscale(image_roi_noir, (100, 100))
    
    image_pion_blanc = pygame.image.load('pion_blanc.png').convert_alpha(fenetre)
    image_pion_blanc = pygame.transform.smoothscale(image_pion_blanc, (100, 100))
    
    image_cavalier_blanc = pygame.image.load('cavalier_blanc.png').convert_alpha(fenetre)
    image_cavalier_blanc = pygame.transform.smoothscale(image_cavalier_blanc, (100, 100))
    
    image_fou_blanc = pygame.image.load('fou_blanc.png').convert_alpha(fenetre)
    image_fou_blanc = pygame.transform.smoothscale(image_fou_blanc, (100, 100))
    
    image_tour_blanc = pygame.image.load('tour_blanc.png').convert_alpha(fenetre)
    image_tour_blanc = pygame.transform.smoothscale(image_tour_blanc, (100, 100))
    
    image_dame_blanc = pygame.image.load('dame_blanc.png').convert_alpha(fenetre)
    image_dame_blanc = pygame.transform.smoothscale(image_dame_blanc, (100, 100))
    
    image_roi_blanc = pygame.image.load('roi_blanc.png').convert_alpha(fenetre)
    image_roi_blanc = pygame.transform.smoothscale(image_roi_blanc, (100, 100))
    

    #pions
    for i in range(8):
        pion = nouvellePiece(i,1,"pion", "noir")
        pion['image'] = image_pion_noir
        ensemble_pieces.append(pion)

        echiquier[i][1]['piece'] = pion
        echiquier[i][1]['vide'] = False

    #tours
    tour = nouvellePiece(0,0,"tour", "noir")
    tour['image'] = image_tour_noir
    ensemble_pieces.append(tour)

    echiquier[0][0]['piece'] = tour
    echiquier[0][0]['vide'] = False
    

    tour = nouvellePiece(7,0,"tour", "noir")
    tour['image'] = image_tour_noir
    ensemble_pieces.append(tour)

    echiquier[7][0]['piece'] = tour
    echiquier[7][0]['vide'] = False


    #cavaliers
    cavalier = nouvellePiece(1,0,"cavalier", "noir")
    cavalier['image'] = image_cavalier_noir
    ensemble_pieces.append(cavalier)

    echiquier[1][0]['piece'] = cavalier
    echiquier[1][0]['vide'] = False

    cavalier = nouvellePiece(6,0,"cavalier", "noir")
    cavalier['image'] = image_cavalier_noir
    ensemble_pieces.append(cavalier)

    echiquier[6][0]['piece'] = cavalier
    echiquier[6][0]['vide'] = False

    #fous
    fou = nouvellePiece(2,0,"fou", "noir")
    fou['image'] = image_fou_noir
    ensemble_pieces.append(fou)

    echiquier[2][0]['piece'] = fou
    echiquier[2][0]['vide'] = False

    fou = nouvellePiece(5,0,"fou", "noir")
    fou['image'] = image_fou_noir
    ensemble_pieces.append(fou)

    echiquier[5][0]['piece'] = fou
    echiquier[5][0]['vide'] = False

    #dame
    dame = nouvellePiece(3,0,"dame", "noir")
    dame['image'] = image_dame_noir
    ensemble_pieces.append(dame)

    echiquier[3][0]['piece'] = dame
    echiquier[3][0]['vide'] = False

    #roi
    roi = nouvellePiece(4,0,"roi", "noir")
    roi['image'] = image_roi_noir
    ensemble_pieces.append(roi)

    echiquier[4][0]['piece'] = roi
    echiquier[4][0]['vide'] = False


    #blanc
    #pions
    for i in range(8):
        pion = nouvellePiece(i,6,"pion", "blanc")
        pion['image'] = image_pion_blanc
        ensemble_pieces.append(pion)

        echiquier[i][6]['piece'] = pion
        echiquier[i][6]['vide'] = False

    #tours
    tour = nouvellePiece(0,7,"tour", "blanc")
    tour['image'] = image_tour_blanc
    ensemble_pieces.append(tour)

    echiquier[0][7]['piece'] = tour
    echiquier[0][7]['vide'] = False
    

    tour = nouvellePiece(7,7,"tour", "blanc")
    tour['image'] = image_tour_blanc
    ensemble_pieces.append(tour)

    echiquier[7][7]['piece'] = tour
    echiquier[7][7]['vide'] = False


    #cavaliers
    cavalier = nouvellePiece(1,7,"cavalier", "blanc")
    cavalier['image'] = image_cavalier_blanc
    ensemble_pieces.append(cavalier)

    echiquier[1][7]['piece'] = cavalier
    echiquier[1][7]['vide'] = False

    cavalier = nouvellePiece(6,7,"cavalier", "blanc")
    cavalier['image'] = image_cavalier_blanc
    ensemble_pieces.append(cavalier)

    echiquier[6][7]['piece'] = cavalier
    echiquier[6][7]['vide'] = False

    #fous
    fou = nouvellePiece(2,7,"fou", "blanc")
    fou['image'] = image_fou_blanc
    ensemble_pieces.append(fou)

    echiquier[2][7]['piece'] = fou
    echiquier[2][7]['vide'] = False

    fou = nouvellePiece(5,7,"fou", "blanc")
    fou['image'] = image_fou_blanc
    ensemble_pieces.append(fou)

    echiquier[5][7]['piece'] = fou
    echiquier[5][7]['vide'] = False

    #dame
    dame = nouvellePiece(3,7,"dame", "blanc")
    dame['image'] = image_dame_blanc
    ensemble_pieces.append(dame)

    echiquier[3][7]['piece'] = dame
    echiquier[3][7]['vide'] = False

    #roi
    roi = nouvellePiece(4,7,"roi", "blanc")
    roi['image'] = image_roi_blanc
    ensemble_pieces.append(roi)

    echiquier[4][7]['piece'] = roi
    echiquier[4][7]['vide'] = False

#---Fin Initialisation---#

#---Données---#

def nouvelleCase(couleur):
    return{
        'couleur':couleur,
        'vide':True,
        'piece':[]
    }

def nouvellePiece(x, y, nom, couleur):
    return{
        'position': [x, y],
        'nom':nom,
        'image':[],
        'couleur':couleur,
        'capturee':False,
        'dejaBougee':False
    }

def positionCase(x, y):
    return x*100, 100+y*100

def casePosition(x, y):
    if x<0 or x>FENETRE_LARGEUR:
        return -1,-1
    elif y<100 or y>FENETRE_HAUTEUR:
        return -1,-1
    else:
        for i in range(1,9):
            if x<i*100:
                return i-1, checkY(y)

def checkY(y):
    for i in range(1,9):
        if y<((i*100)+100):
            return i-1

#---FIN Données---#

#---Déplacements---#

def nouvelleSelection():
    return{
        'pieceSelectionne':False,
        'piece':[],
        'enEchec':False,
        'auTourDes':"blanc"
    }

def deplacements(positioncase):
    global selection
    case = echiquier[positioncase[0]][positioncase[1]]
    couleur = selection['auTourDes']
    if selection['pieceSelectionne']==False and case['vide']==False and case['piece']['couleur']==selection['auTourDes']:
        selection['pieceSelectionne']=True
        selection['piece'] = case['piece']
    elif selection['pieceSelectionne']==True:
        if not case['vide'] and case['piece']==selection['piece']:
            selection['pieceSelectionne']=False
            return
        position_piece = selection['piece']['position']
        if selection['piece']['nom']=="pion":
            if deplacementPion(positioncase):
                tourSuivant()
        elif selection['piece']['nom']=="cavalier":
            if deplacementCavalier(positioncase):
                if not case['vide']:
                    if case['piece']['couleur']!=couleur:
                        if prisePiece(echiquier[position_piece[0]][position_piece[1]], case, positioncase):
                            tourSuivant()
                else:
                    if deplacePiece(positioncase, position_piece):
                        tourSuivant()
        elif selection['piece']['nom']=='fou':
            if deplacementFou(positioncase):
                if not case['vide']:
                    if case['piece']['couleur']!=couleur:
                        if prisePiece(echiquier[position_piece[0]][position_piece[1]], case, positioncase):
                            tourSuivant()
                else:
                    if deplacePiece(positioncase, position_piece):
                        tourSuivant()
        elif selection['piece']['nom']=="tour":
            if deplacementTour(positioncase):
                if not case['vide']:
                    if case['piece']['couleur']!=couleur:
                        if prisePiece(echiquier[position_piece[0]][position_piece[1]], case, positioncase):
                            case['piece']['dejaBougee']=True
                            tourSuivant()
                else:
                    if deplacePiece(positioncase, position_piece):
                        case['piece']['dejaBougee']=True
                        tourSuivant()
        elif selection['piece']['nom']=='dame':
            if deplacementFou(positioncase) or deplacementTour(positioncase):
                if not case['vide']:
                    if case['piece']['couleur']!=couleur:
                        if prisePiece(echiquier[position_piece[0]][position_piece[1]], case, positioncase):
                            tourSuivant()
                else:
                    if deplacePiece(positioncase, position_piece):
                        tourSuivant()
        elif selection['piece']['nom']=="roi":
            if deplacementRoi(positioncase):
                if not case['vide']:
                    if case['piece']['couleur']!=couleur:
                        if prisePiece(echiquier[position_piece[0]][position_piece[1]], case, positioncase):
                            case['piece']['dejaBougee']=True
                            tourSuivant()
                else:
                    if deplacePiece(positioncase, position_piece):
                        case['piece']['dejaBougee']=True
                        tourSuivant()

def deplacePiece(positioncase, position_piece, piece=None):
    global selection, echiquier, client_socket
    tampon0 = position_piece[0]
    tampon1 = position_piece[1]
    if(piece == None):
        piece = selection['piece']

    case = echiquier[positioncase[0]][positioncase[1]]
    echiquier[position_piece[0]][position_piece[1]]['vide']=True
    case['vide']=False
    case['piece']=selection['piece']
    selection['piece']['position'][0]=positioncase[0]
    selection['piece']['position'][1]=positioncase[1]

    if checkEchec(selection['auTourDes']):
        piece['position'][0]=tampon0
        piece['position'][1]=tampon1
        case['vide']=True
        echiquier[tampon0][tampon1]['vide']=False
        selection['piece']=piece
        return False
    #--envoi des données à l'autre joueur
    client_socket.send(pickle.dumps(positioncase))
    client_socket.send(pickle.dumps(position_piece))
    client_socket.send(pickle.dumps(piece))
    return True

def deplacementRoi(positioncase):
    position_piece = selection['piece']['position']
    if position_piece[0]==positioncase[0]+1 or position_piece[0]==positioncase[0]-1 or position_piece[0]==positioncase[0]:
        if position_piece[1]==positioncase[1]+1 or position_piece[1]==positioncase[1]-1 or position_piece[1]==positioncase[1]:
            if not (position_piece[0]==positioncase[0] and position_piece[1]==positioncase[1]):
                return True
    # elif position_piece[0]==positioncase[0]+2 and position_piece[1]==positioncase[1] and not selection['piece']['dejaBougee']:
    #     case_tour = echiquier[7][position_piece[1]]
    #     if not case_tour['vide'] and case_tour['nom']=='tour' and not case_tour['dejaBougee']:
    # elif position_piece[0]==positioncase[0]-2 and position_piece[1]==positioncase[1] and not selection['piece']['dejaBougee']:
    #     case_tour = echiquier[0][position_piece[1]]
    #     if not case_tour['vide'] and case_tour['nom']=='tour' and not case_tour['dejaBougee']:

    return False

def deplacementFou(positioncase):
    global selection, echiquier
    position_piece = selection['piece']['position']
    
    n = position_piece[0]-positioncase[0]
    if n==0:
        return False
    if position_piece[1]-n==positioncase[1]:
        if n>0:
            for i in range(1,n):
                if not echiquier[position_piece[0]-i][position_piece[1]-i]['vide']:
                    return False
        elif n<0:
            for i in range(1,-n):
                if not echiquier[position_piece[0]+i][position_piece[1]+i]['vide']:
                    return False
    elif position_piece[1]+n==positioncase[1]:
        if n>0:
            for i in range(1,n):
                if not echiquier[position_piece[0]-i][position_piece[1]+i]['vide']:
                    return False
        elif n<0:
            for i in range(1,-n):
                if not echiquier[position_piece[0]+i][position_piece[1]-i]['vide']:
                    return False
    else:
        return False
                    
    return True

def deplacementPion(positioncase):
    global selection, echiquier
    position_piece = selection['piece']['position']
    couleur = selection['auTourDes']
    case = echiquier[positioncase[0]][positioncase[1]]
    if couleur == "blanc":
        if position_piece[0]==positioncase[0]:
            if position_piece[1]-1==positioncase[1] or (position_piece[1]-2==positioncase[1] and position_piece[1]==6):
                if case['vide']==True:
                    deplacePiece(positioncase, position_piece)
                    return True
        if position_piece[0]==positioncase[0]+1 or position_piece[0]==positioncase[0]-1:
            if position_piece[1]-1==positioncase[1]:
                if not case['vide'] and case['piece']['couleur']!=couleur:
                    prisePiece(echiquier[position_piece[0]][position_piece[1]], case, positioncase)
                    return True
    else:
        if position_piece[0]==positioncase[0]:
            if position_piece[1]+1==positioncase[1] or (position_piece[1]+2==positioncase[1] and position_piece[1]==1):
                if case['vide']==True:
                    deplacePiece(positioncase, position_piece)
                    return True
        if position_piece[0]==positioncase[0]+1 or position_piece[0]==positioncase[0]-1:
            if position_piece[1]+1==positioncase[1]:
                if not case['vide'] and case['piece']['couleur']!=couleur:
                    prisePiece(echiquier[position_piece[0]][position_piece[1]], case, positioncase)
                    return True
    return False

def deplacementCavalier(positioncase):
    position_piece = selection['piece']['position']

    if positioncase[0]==position_piece[0]+2 or positioncase[0]==position_piece[0]-2:
        if positioncase[1]==position_piece[1]+1 or positioncase[1]==position_piece[1]-1:
            return True
    elif positioncase[0]==position_piece[0]+1 or positioncase[0]==position_piece[0]-1:
        if positioncase[1]==position_piece[1]+2 or positioncase[1]==position_piece[1]-2:
            return True
    return False

def deplacementTour(positioncase):
    global echiquier
    position_piece = selection['piece']['position']
    
    if position_piece[0]==positioncase[0] and position_piece[1]!=positioncase[1]:
        n = position_piece[1] - positioncase[1]
        if n>0:
            for i in range(1,n):
                if not echiquier[position_piece[0]][position_piece[1]-i]['vide']:
                    return False
        elif n<0:
            for i in range(1,-n):
                if not echiquier[position_piece[0]][position_piece[1]+i]['vide']:
                    return False
    elif position_piece[0]!=positioncase[0] and position_piece[1]==positioncase[1]:
        n = position_piece[0] - positioncase[0]
        if n>0:
            for i in range(1,n):
                if not echiquier[position_piece[0]-i][position_piece[1]]['vide']:
                    return False
        elif n<0:
            for i in range(1,-n):
                if not echiquier[position_piece[0]+i][position_piece[1]]['vide']:
                    return False
    else:
        return False
    return True

def prisePiece(casePreneur, caseCapture, positioncase):
    piece = caseCapture['piece']
    position0 = casePreneur['piece']['position'][0]
    position1 = casePreneur['piece']['position'][1]

    casePreneur['vide']=True
    caseCapture['piece']['capturee']=True
    caseCapture['piece']=casePreneur['piece']
    caseCapture['piece']['position'][0]=positioncase[0]
    caseCapture['piece']['position'][1]=positioncase[1]

    if checkEchec(selection['auTourDes']):
        casePreneur['vide']=False
        piece['capturee']=False
        casePreneur['piece']=caseCapture['piece']
        casePreneur['piece']['position'][0] = position0
        casePreneur['piece']['position'][1] = position1
        caseCapture['piece']=piece
        selection['piece']=casePreneur['piece']
        return False
    return True

def tourSuivant():
    global selection, auTourDe
    selection['enEchec']=False
    selection['pieceSelectionne']=False
    if selection['auTourDes']=="blanc":
        selection['auTourDes']="noir"
    else:
        selection['auTourDes']="blanc"
    if checkEchec(selection['auTourDes']):
        selection['enEchec']=True
    
    if auTourDe == 1:
        auTourDe = 2
    else:
        auTourDe = 1

def checkEchec(couleur_roi):
    global selection
    for piece in ensemble_pieces:
        if piece['nom']=='roi' and piece['couleur']==couleur_roi:
            roi = piece
    positioncase = roi['position']
    
    for piece in ensemble_pieces:
        selection['piece'] = piece
        if not piece['capturee'] and piece['couleur']!=couleur_roi:
            position_piece = piece['position']
            if piece['nom']=="pion":
                if piece['couleur']=='blanc':
                    if position_piece[0]==positioncase[0]+1 or position_piece[0]==positioncase[0]-1:
                        if position_piece[1]-1==positioncase[1]:
                            return True
                elif piece['couleur']=='noir':
                    if position_piece[0]==positioncase[0]+1 or position_piece[0]==positioncase[0]-1:
                        if position_piece[1]+1==positioncase[1]:
                            return True
            elif piece['nom']=="cavalier"  and deplacementCavalier(positioncase):
                return True
            elif piece['nom']=="tour"  and deplacementTour(positioncase):
                return True
            elif piece['nom']=="dame"  and (deplacementFou(positioncase) or deplacementTour(positioncase)):
                return True
            elif piece['nom']=="fou"  and deplacementFou(positioncase):
                return True
    
    return False
                    
#---FIN Déplacements---#

#---Affichage---#

def affichageEchec():
    if selection['enEchec']:
        for piece in ensemble_pieces:
            if piece['nom']=='roi' and piece['couleur']==selection['auTourDes']:
                roi = piece
        case = roi['position']
        position = positionCase(case[0], case[1])
        pygame.draw.rect(fenetre,ROUGE, (position[0], position[1], 100, 100))
    return 

def affichageGrille():
    fenetre.fill(BLANC)
    pygame.draw.rect(fenetre, NOIR, (0,0,800,100))
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(fenetre, GRIS,(100+i*200, 200+j*200, 100, 100))

    for i in range(4):
        for j in range(4):
            pygame.draw.rect(fenetre, GRIS,(i*200, 100+j*200, 100, 100))
    affichageEchec()
    affichageCaseSelectionnne()

def affichagePieces():
    for pion in ensemble_pieces:
        if not pion['capturee']:
            fenetre.blit(pion['image'],positionCase(pion['position'][0],pion['position'][1]))

def affichageCaseSelectionnne():
    if selection['pieceSelectionne']==True:
        case = selection['piece']['position']
        position = positionCase(case[0], case[1])
        pygame.draw.rect(fenetre, VERT, (position[0], position[1], 100, 100))

def affichage():
    affichageGrille()
    affichagePieces()

#---FIN Affichage---#

#---Inputs---#

def gestionEntree():
    global fini
    for evenement in pygame.event.get():
        if evenement.type==pygame.QUIT:
            fini=True
        elif evenement.type==pygame.KEYDOWN:
            # gestionDirection(evenement)
            if evenement.key==pygame.K_ESCAPE:
                print("bonjour")
        elif evenement.type==pygame.MOUSEBUTTONDOWN:
            gestionClick(evenement)

def gestionClick(evenement):
    if evenement.button==1:
        case = casePosition(position_souris[0], position_souris[1])
        deplacements(case)
    elif evenement.button==3:
        selection['pieceSelectionne']=False

#---FIN Inputs---#

#---Connexion au server---#
host = socket.gethostname()  # as both code is running on same pc
port = 1300  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

joueur = int(client_socket.recv(256).decode())
auTourDe = 1
print("Vous êtes le joueur "+str(joueur))

#---main---#

pygame.init()

temps = pygame.time.Clock()

fenetre_taille = [FENETRE_LARGEUR, FENETRE_HAUTEUR]
fenetre = pygame.display.set_mode(fenetre_taille)
pygame.display.set_caption('Chess')

initialisation()
selection = nouvelleSelection()


while not fini:
    affichage()
    if auTourDe == joueur:
        position_souris = pygame.mouse.get_pos()
        gestionEntree()
    else:
        case = pickle.loads(client_socket.recv(256))
        print(type(case))
        pos_piece = pickle.loads(client_socket.recv(256))
        print(type(pos_piece))
        piece = pickle.loads(client_socket.recv(256))
        print(type(piece))
        deplacePiece(case, pos_piece, piece)
    pygame.display.flip()
    temps.tick(30)
    
pygame.display.quit()
pygame.quit()
exit()