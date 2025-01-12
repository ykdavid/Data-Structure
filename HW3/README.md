[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/KGZWwF3Y)
# Assignment 3: UW-Euchre

## Objectives

* Implementing applied data structures
* Utilize data structure implementations
* Implement your first sort function
* Become familiar with a Python testing framework 

# Overview

In this assignment, you are going to implement some key components to a card game. 
The card game is a version of Euchre (pronounced "U-ker"). Euchre is a 4-player game 
that is modified to be a 2-player for this assignment. 
To get a sense of the game, you can play the traditional version at 
https://cardgames.io/euchre/.

There are two parts to this assignment: first, implementing data structures to support 
the game play; second, implementing the game using these data structures.

Additionally, we'll start using the unittest testing module. This time, we've 
provided some example tests to get started, but it will likely be helpful for you 
to write some tests of your own. 

# Details 

The rules of UW-Euchre are below. UW-Euchre is inspired by Euchre, but 
some of the play details are simplified to make it easier to understand and implement. 

## Basic Rules Of UW-Euchre

* UW-Euchre is a 2-player game. 
* The player with the most points after 5 rounds wins. 
* A player wins a round by "collecting the most tricks".
* A **_round_** consists of each player being dealt 5 cards, choosing a trump 
(a suit designated as the highest/most powerful for this round), 
and then each player takes turns playing cards for a "trick". 

A player wins a trick by playing the highest value card in a round.

**There are a couple of rules that must be followed for playing a card:** 
the first player can play any card, but the second player must "follow suit".  
If the second player has a card of the same suit, they must play it (but they can choose 
which card they want to play). Further, a card of the trump suit is higher 
than all other cards in the deck. For example, if Spades is trump, a 9 of Spades is 
higher than an Ace of Diamonds. 

Within a suit, including trump, the face value of the 
card is highest, with Aces being the highest value card.

In this version of the game, Player 1 (the computer) ALWAYS goes first and 
leads the first card. This makes the game less fun, but more simple to implement.

The deck used for UW-Euchre is a subset of the traditional 52-card deck. 
It includes the Ace, King, Queen, Jack, 10 & 9 of all four suits (Spades, Diamonds, 
Hearts, and Clubs).

## Provided Starter Code

* `game_structures.py` is the same starter file from A3. It's here for reference/convenience; feel free to replace it with your file. 
* `game_structures_test.py` provides some tests to ensure your A3 code works properly. 
* `game_play.py` specifies the functions you need to implement for this assignment. 
* `game_play_test.py` provides some tests to ensure your new A4 functions work properly.

## Running 

To run tests: 

In the terminal window, run: 

```bash
python3 game_play_test.py
```
or for structure tests: 

```bash
python3 game_structures_test.py
```

To run the game: 

```shell
python3 uw_euchre.py
```

# Notes

* Let the tests guide your approach to this-- run the tests, and work on one at a time until it passes. 
* Start with the game_structures-- these are your basic data structures for the game. 
* After the structures are created, work on the game_play bits-- these are the building blocks the game. 
* Once both are done, the game will play! 
* Remember: It is NOT okay to put any of this code into ChatGPT or any other AI assistant for help as part of this assignment. 
* Any updates or clarifications to the assignment will be noted here and on Piazza. 
* 
