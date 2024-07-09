# exit-bot – 8出口
Simple bot to play the Steam / Unity game [The Exit 8](https://store.steampowered.com/app/2653790/The_Exit_8/), (badly).

８番出口 / The Exit 8 is a short (15-60 mins), psychological horror style walking simulator game [available on Steam](https://store.steampowered.com/app/2653790/The_Exit_8/)
If you know nothing about it (and are interested) you should stop reading this and play the game. It is good.
There may be spoilers below, and the game is best played without any prior information.

This bot will not help you beat the game, it's merely a statistical experiment to discover the simplest, dumbest strategy that could possibly beat the game with unlimited time.
Ideally before reading further you should have:
* Played the game
* Beat the game
* 100% the game (all achievements, all endings etc)

If you still want to explore what else to do with the game, this bot might be one answer....


<details>
  <summary>Motivation</summary>

## Motivation

With the naive assumption that maybe there's a 50% chance the passageway contains an anomaly / 50% not, perhaps you can get
8 non-anomaly passages in a row... suggesting that simply running forwards **might** be a winning strategy.

0.5<sup>8</sup> = 0.00390625 

= 1/256. We'd expect to walk through the passage no more than 8 * 256 = 2048 times and see a straight winning exit at some point.

Now it's possible that the developers have coded something to prevent a straight run win, but we can test that.
I don't really want to go disassembling or looking in the code, that's cheating. We should be able to figure it out.

</details>

<details>
  <summary>Goals (and non-goals)</summary>

### Goals

* Determine the simplest possible winning strategy for beating Exit 8 (confirm walking forward is viable?)
* Play Exit 8, badly, without getting stuck in corners or otherwise glitching out indefinitely (like an endless screensaver)
* Explore the Exit 8 maze statistically / probabilistically without relying on visual cues

### Non-Goals
* Making a good bot with excellent vision and anomaly detection that can reliably beat the game by playing properly -- too much like cheating (this might be a basis for that-sort-of-thing, but it doesn't really interest me)

### Possible extra features
* Exploring whether there is a way to use only audio cues to play the game *somewhat* competently
</details>

<details>
  <summary>Features</summary>

Detects, and recovers from, the following death endings:
* Wave
* False exit (walks into walls a bit before getting up the stairs, but still figures out it died)
* Running tile-creature
* Mysterious pair (I think...)

Are there more?
Recovering from the handful of death endings requires the bot to use a (currently) 5 pixels vision check. All black screen = Dead. All white screen = Win.
Deaths occur at different points in the passage and messes up any hardcoded timings.

### Unimplemented
* Anomaly guess behaviour: turn around and go the other way
  * We could guess that there is an anomaly and turn around; I'm not sure this strategy will even improve the changes of getting a win
  * If the bot turns around on a non-anomaly, it would need to recognise it made a mistake, and then turn around *again* to get back on track... otherwise it could get very lost
  * .. something to explore further? Force the bot to endlessly walk *the wrong way*?
* A mechanism for the bot to know how many correct passages it has walked would be good for collecting stats on long runs. I've seen it get to 3 pretty regularly. Knowing its best run would help determine whether there is code to prevent straight runs. If there is non-probabilistic code, this could be exploitable (and would *require* the turn around feature).
   * Naive approach: position the bot 'accurately' in front of the passage sign each time and use really rough OCR to determine the number 0–8. 
</details>





