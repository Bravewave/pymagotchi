# Pymagotchi
A Tamagotchi-style game in Python
by Bravewave

This started as a school Computer Science project, but I liked it and decided to continue it.
The game currently has 2 main options - wait and feed. There are other features in the code, but are not implemented as of yet.

I have sprites that I plan to add in future (probably using Tkinter) but are not yet ready. I'm working on base code first before working on moving it over to a GUI based system.

The game rules are as follows:
1. Your Tamagotchi has 100% health and 0% hunger to start with. Hunger level will go up by 10% each turn
2. When your Tamagotchi's hunger level reaches 80%, they will begin to lose 5% health per turn, until the hunger level drops below 80% again
3. Every turn, you can choose to feed your Tamagotchi, or to wait another turn. Feeding drops your Tamagotchi's hunger level by a certain amount, depending on what you fed them
4. You have a certain amount of stock in your inventory. Go to the shop to buy more!
5. As your Tamagotchi levels up, their maximum health will go up, as will their skill
6. If your Tamagotchi's health reaches 0%, it will die and it's game over!
7. Your Tamagotchi's health cannot go above 100%, nor can its hunger go below 0%

Enjoy the game!
