<<<<<<< HEAD
<<<<<<< HEAD
HackBulgaria
============

Hack Bulgaria's Programming 101 course tasks and projects repository


The problem definitions for each solution can be found on Hack Bulgaria's Programming 101 course repository:

https://github.com/HackBulgaria/Programming101-2



=======
money-in-the-bank
=================
>>>>>>> 3487c40c8fe9f94eac65cf8390cc301ea0f5e058
=======
# Money In The Bank

## What is this?

This is one of the bigger problems from the course Hack Bulgaria. Basicly it is a simulator of a bank.

## Main menu functionality

* You can get the commands by typing `help`
* You can `register` new users(duh). The passwords must be very strong. That means they have to be longer than __8__ symbols, they have to include at least one of the following: __a lowercase letter, an uppercase letter, a number and a special symbol__ The users' passwords will be hashed and stored in a database, as everything else is. Also while typing the password it will be hidden. That's also the case during `login`
* You can `login` a registered user. If you enter a wrong password more than 5 times the given user will be banned for 5 minutes. Once you are logged in you will be taken to the logged menu.
* You can `send-reset-password` code to your email. You get a hash code that you use for `reset-password`. But hurry as it expires after __15 minutes__!
* Of course, you can exit at any time by typing, wait for it... `exit` ! (Surprized, aren't you?)

## Logged menu functionality

* Again you can get the commands by typing `help`
* By typing in `info` you get basic information about the currently logged user.
* You can write or change a message with the command `change-message`
* You can `show-message` at any time.

#### Now for the fun part

* This is a bank simulator so guess what, you can `deposit`. You can't deposit a negative amount. You need a TAN code for __every__ transaction!
* You can also `withdraw`, again no negative amounts! If you have insufficient funds you will be prompted exactly that. (Another thing you didn't expect, I get you every time.) You need a TAN code for __every__ transaction!
* You can `display-balance` at any time to check the funds available in your account.
* The really important command here is `get-tan`. As I mentioned before, you need a TAN code for __every__ transaction! This command sends you ten __TAN codes__ to use during your transactions. If you try to send new codes before you used all ten you will be prompted that you still have remaining codes. These codes __don't__ expire after a given time.
* And lastly you can `logout`. This gets you back to the main menu.
>>>>>>> adf34c6e37a3c87bebd6d445b0e7fcafeaade8ed
