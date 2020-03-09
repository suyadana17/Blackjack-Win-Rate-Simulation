# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:06:15 2015

@author: Hussam Ibrahim, Ali Rabeh, Myo Lin
Project 3 - Blackjack Simulation
"""

from pylab import *
import random
from colorama import Fore, Style

numGame = 1000000
strategy = 'Strategy 1'

win = 0
lose = 0
tie = 0
dealerShowCard = None

print(Fore.BLACK+"Game is starting!!")
print(strategy)
print("")

def draw():
    card = random.choice(deck)
    for i in range(0,13):
        if(deck[i] == card):
            if(counter[i] == 4):
                card = None
            else:
                counter[i] = counter[i] + 1
    return card

def checkCardAvail():
    card = draw()
    while(card == None):
        card = draw()
    return card

def checkJQK(incCard):
    card = incCard
    if(card == 'J' or card == 'Q' or card == 'K'):
        card = 10
    return card

def checkAceCard(incCard, total):
    card = incCard
    if(card == 'A'):
        if((total + 11) > 21):
            card = 1
        elif(total + 11 <= 21):
            card = 11
    return card                 

def dealerTurn():
    global dealerShowCard    
    
    dealerFirstCard = checkCardAvail()
    print(Fore.RED+"Dealer First Card: ", dealerFirstCard)
    dealerFirstCard = checkAceCard(dealerFirstCard, 0)
    dealerFirstCard = checkJQK(dealerFirstCard)
    dealerShowCard = dealerFirstCard    
    
    dealerSecondCard = checkCardAvail()
    print("Dealer Second Card: ", dealerSecondCard)
    dealerSecondCard = checkAceCard(dealerSecondCard, dealerFirstCard)
    dealerSecondCard = checkJQK(dealerSecondCard)
    
    dealerScore = dealerFirstCard + dealerSecondCard
    return dealerScore

def playerTurn(option, showCard):
    playerFirstCard = checkCardAvail()
    print(Fore.BLUE+"Player First Card: ", playerFirstCard)
    playerFirstCard = checkAceCard(playerFirstCard, 0)
    playerFirstCard = checkJQK(playerFirstCard)
    
    playerSecondCard = checkCardAvail()
    print("Player Second Card: ",playerSecondCard)
    playerSecondCard = checkAceCard(playerSecondCard, playerFirstCard)
    playerSecondCard = checkJQK(playerSecondCard)
    
    playerScore = playerFirstCard + playerSecondCard
    if(option == 'Strategy 1'):
        print("Player Score: ", playerScore)
        return playerScore  
    if(option == 'Strategy 2'):
        if(playerScore < 17):
            while(playerScore < 17):
                playerNextCard = checkCardAvail()
                print("Player Draws: ", playerNextCard)
                playerNextCard = checkAceCard(playerNextCard, playerScore)
                playerNextCard = checkJQK(playerNextCard)
                playerScore = playerScore + playerNextCard
            print("Player Score: ", playerScore)
            return playerScore
        else:
            return playerScore
    if(option == 'Strategy 3'):
        if(playerScore < 17):
            while(playerScore < 17):
                playerNextCard = checkCardAvail()
                print("Player Draws: ", playerNextCard)
                playerNextCard = checkAceCard(playerNextCard, playerScore)
                playerNextCard = checkJQK(playerNextCard)
                playerScore = playerScore + playerNextCard
            print("Player Score: ", playerScore)
            #return playerScore
        if(showCard == 10 and playerScore == 17):
           playerNextCard = checkCardAvail()
           print("Player Draws: ", playerNextCard)
           playerNextCard = checkAceCard(playerNextCard, playerScore)
           playerNextCard = checkJQK(playerNextCard)
           playerScore = playerScore + playerNextCard
           print("Player Score: ", playerScore)
           #return playerScore
        return playerScore
    if(option == 'Strategy 4'):
        if(playerScore < (2*dealerShowCard) and playerScore < 16):
            while(playerScore < 16):
                playerNextCard = checkCardAvail()
                print("Player Draws: ", playerNextCard)
                playerNextCard = checkAceCard(playerNextCard, playerScore)
                playerNextCard = checkJQK(playerNextCard)
                playerScore = playerScore + playerNextCard
        print("Player Score: ", playerScore)
        return playerScore

def dealerSecond(dealerTotal):
    dealerScore = dealerTotal
    while(dealerScore < 17):
        dealerNextCard = checkCardAvail()
        print(Fore.RED+"Dealer Draws: ", dealerNextCard)
        dealerNextCard = checkAceCard(dealerNextCard, dealerScore)
        dealerNextCard = checkJQK(dealerNextCard)
        dealerScore = dealerScore + dealerNextCard
    print(Fore.RED+"Dealer Score: ", dealerScore)
    return dealerScore
            
def winDrawLose(dealerScore, playerScore):
    global win
    global tie
    global lose
    
    if(dealerScore > 21):
        win = win + 1
    elif(playerScore > dealerScore):
        win = win + 1
    elif(playerScore == dealerScore):
        tie = tie + 1
    elif(dealerScore > playerScore):
        lose = lose + 1

for i in range(0, numGame):
    deck = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    counter = zeros(13)
    print(Fore.BLACK + "Game ",(i+1))
    dealer = dealerTurn()
    player = playerTurn(strategy, dealerShowCard)
    if(dealer == 21 & player == 21):
        tie = tie + 1
    elif(dealer == 21):
        lose = lose + 1
    elif(player > 21):
        lose = lose + 1
    elif(player == 21):
        win = win + 1
    else:
        dealer = dealerSecond(dealer)
        winDrawLose(dealer, player)
    print("")
    
print(Fore.GREEN+'win = ', win, ',tie = ', tie, ',lose = ', lose)
probWin = win/float(numGame)
probTie = tie/float(numGame)
probLose = lose/float(numGame)
print("Probability of Win: ", probWin)
print("Probability of Tie: ", probTie)
print("Probability of Lose: ", probLose)
