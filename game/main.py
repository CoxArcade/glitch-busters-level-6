import asyncio
import pygame, random, math, ast
pygame.init()
W,H=640,400
screen=pygame.display.set_mode((W,H))
pygame.display.set_caption('QUESTFORGE / GLITCH BUSTERS LEVEL 6: ECHOES OF THE VOID')
clock=pygame.time.Clock()
F=pygame.font.Font(None,21); S=pygame.font.Font(None,16); L=pygame.font.Font(None,37)
WHITE=(241,244,255); BG=(12,15,31); CYAN=(81,224,222); GOLD=(255,207,83)
PINK=(252,91,152); RED=(237,75,99); GREEN=(102,228,137); PURPLE=(173,117,249)
GRAY=(147,153,183); BLUE=(80,129,227)
AREA=pygame.Rect(25,65,590,264)
ROOMS=['THE OBSIDIAN OBSERVATORY', 'THE SHATTERED ARCHIVES', 'THE MIRROR FOUNDRY', 'THE STORM CITADEL', 'THE VOID ENGINE']
Q=[('TELESCOPE BOOT', 'Set power to 4, then increase power by 3.', ['power = 4', 'power = power - 3'], [], 0, 'Type the complete working Python program.', 'power = 4\npower = power + 3', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('STARLIGHT BATTERY', 'Set charge to 6, then subtract 2.', ['charge == 6', 'charge = charge - 2'], [], 0, 'Type the complete working Python program.', 'charge = 6\ncharge = charge - 2', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('ORBIT SIGNAL', "Set signal to 'STAR', then set ready to True.", ["signal = 'STAR'", 'ready = False'], [], 0, 'Type the complete working Python program.', "signal = 'STAR'\nready = True", 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('LENS CALIBRATION', 'Set x to 120 and y to 90.', ['x == 120', 'y = 90'], [], 0, 'Type the complete working Python program.', 'x = 120\ny = 90', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('CONSTELLATION SCORE', 'Set score to 10, then add 5 twice using two lines.', ['score = 10', 'score = score - 5', 'score = score + 5'], [], 0, 'Type the complete working Python program.', 'score = 10\nscore = score + 5\nscore = score + 5', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('REPAIR THE MAP', 'Set stars to 3, then set mapped to stars + 2.', ['stars = 3', 'mapped = stars - 2'], [], 0, 'Type the complete working Python program.', 'stars = 3\nmapped = stars + 2', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('ARCHIVE AUTHORIZATION', 'If clearance is at least 4, set door True; otherwise False.', ['if clearance >= 4:', '    door = False', 'else:', '    door = False'], [], 0, 'Type the complete working Python program.', 'if clearance >= 4:\n    door = True\nelse:\n    door = False', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('BOOK RECOVERY', 'If pages is below 5, add 3; otherwise subtract 1.', ['if pages < 5:', '    pages = pages - 3', 'else:', '    pages = pages - 1'], [], 0, 'Type the complete working Python program.', 'if pages < 5:\n    pages = pages + 3\nelse:\n    pages = pages - 1', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('MISSING FILE', 'If code equals 7, set found True; otherwise False.', ['if code == 7:', '    found = False', 'else:', '    found = False'], [], 0, 'Type the complete working Python program.', 'if code == 7:\n    found = True\nelse:\n    found = False', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('ARCHIVE ALARM', 'If danger is not 0, set alarm True; otherwise False.', ['if danger != 0:', '    alarm = False', 'else:', '    alarm = False'], [], 0, 'Type the complete working Python program.', 'if danger != 0:\n    alarm = True\nelse:\n    alarm = False', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('INDEX REBUILD', 'If records exceeds 10, set records to 10; otherwise add 1.', ['if records > 10:', '    records = 10', 'else:', '    records = records - 1'], [], 0, 'Type the complete working Python program.', 'if records > 10:\n    records = 10\nelse:\n    records = records + 1', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('ACCESS OVERRIDE', 'If key is True and level >= 3, set open True; otherwise False.', ['if key and level >= 3:', '    open = False', 'else:', '    open = False'], [], 0, 'Type the complete working Python program.', 'if key and level >= 3:\n    open = True\nelse:\n    open = False', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('MIRROR LEFT', 'If left pressed, subtract speed from x; otherwise add 1 to x.', ['if keyboard.left:', '    x = x - speed', 'else:', '    x = x - 1'], [], 0, 'Type the complete working Python program.', 'if keyboard.left:\n    x = x - speed\nelse:\n    x = x + 1', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('REFLECTION GATE', 'If x > 500 set x to 500; if x < 0 set x to 0.', ['if x > 500:', '    x == 500', 'if x < 0:', '    x = 0'], [], 0, 'Type the complete working Python program.', 'if x > 500:\n    x = 500\nif x < 0:\n    x = 0', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('PHANTOM STEP', 'If up pressed and fuel > 0, subtract 5 from y and 1 from fuel.', ['if keyboard.up and fuel > 0:', '    y == y - 5', '    fuel = fuel - 1'], [], 0, 'Type the complete working Python program.', 'if keyboard.up and fuel > 0:\n    y = y - 5\n    fuel = fuel - 1', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('MIRROR SWITCH', 'If mode equals 1, add 4 to x; otherwise subtract 4.', ['if mode == 1:', '    x = x - 4', 'else:', '    x = x - 4'], [], 0, 'Type the complete working Python program.', 'if mode == 1:\n    x = x + 4\nelse:\n    x = x - 4', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('SAFE REFLECTION', 'If y >= 300, set y to 300 and falling to False.', ['if y > 300:', '    y = 300', '    falling = False'], [], 0, 'Type the complete working Python program.', 'if y >= 300:\n    y = 300\n    falling = False', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('DOUBLE MIRROR', 'If right pressed and x < 550, increase x by speed; otherwise set blocked True.', ['if keyboard.right and x < 550:', '    x = x - speed', 'else:', '    blocked = True'], [], 0, 'Type the complete working Python program.', 'if keyboard.right and x < 550:\n    x = x + speed\nelse:\n    blocked = True', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('STORM CHARGE', 'Loop four times; add 2 to power each time, then set ready True.', ['for i in range(4):', '    power = power - 2', 'ready = True'], [], 0, 'Type the complete working Python program.', 'for i in range(4):\n    power = power + 2\nready = True', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('LIGHTNING COUNT', 'Loop three times; subtract 1 from timer and add 1 to sparks.', ['for i in range(3):', '    timer = timer - 1', '    sparks = sparks - 1'], [], 0, 'Type the complete working Python program.', 'for i in range(3):\n    timer = timer - 1\n    sparks = sparks + 1', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('TURBINE REPAIR', 'Loop five times; add 2 to charge, then set stable True.', ['for i in range(5):', '    charge = charge - 2', 'stable = True'], [], 0, 'Type the complete working Python program.', 'for i in range(5):\n    charge = charge + 2\nstable = True', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('BOLT FILTER', 'Loop four times; if heat > 0 subtract 1 from heat.', ['for i in range(4):', '    if heat > 0:', '        heat == heat - 1'], [], 0, 'Type the complete working Python program.', 'for i in range(4):\n    if heat > 0:\n        heat = heat - 1', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('POWER DIVERSION', 'Loop three times; if voltage > 8, subtract 2 from voltage.', ['for i in range(3):', '    if voltage > 8:', '        voltage == voltage - 2'], [], 0, 'Type the complete working Python program.', 'for i in range(3):\n    if voltage > 8:\n        voltage = voltage - 2', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('THUNDER RESET', 'Loop twice; add 5 to energy and subtract 1 from faults.', ['for i in range(2):', '    energy = energy - 5', '    faults = faults - 1'], [], 0, 'Type the complete working Python program.', 'for i in range(2):\n    energy = energy + 5\n    faults = faults - 1', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('VOID SHIELD', 'Write shield(power) that returns True when power >= 10, otherwise False.', ['def shield(power):', '    if power >= 10:', '        return False', '    else:', '        return False'], [], 0, 'Type the complete working Python program.', 'def shield(power):\n    if power >= 10:\n        return True\n    else:\n        return False', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('CORE RECHARGE', 'Write recharge(energy) that returns energy + 5 if below 10, otherwise energy.', ['def recharge(energy):', '    if energy < 10:', '        return energy - 5', '    else:', '        return energy'], [], 0, 'Type the complete working Python program.', 'def recharge(energy):\n    if energy < 10:\n        return energy + 5\n    else:\n        return energy', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('GATE ACCESS', 'Write access(key, level) returning True if key and level >= 5, else False.', ['def access(key, level):', '    if key and level >= 5:', '        return False', '    else:', '        return False'], [], 0, 'Type the complete working Python program.', 'def access(key, level):\n    if key and level >= 5:\n        return True\n    else:\n        return False', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('HEALING PULSE', 'Write heal(hp) returning hp + 3 if hp < 5, otherwise hp.', ['def heal(hp):', '    if hp < 5:', '        return hp - 3', '    else:', '        return hp'], [], 0, 'Type the complete working Python program.', 'def heal(hp):\n    if hp < 5:\n        return hp + 3\n    else:\n        return hp', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('VOID COUNTER', 'Write count() that loops 3 times, adding 2 to total starting at 0, then returns total.', ['def count():', '    total = 0', '    for i in range(3):', '        total = total - 2', '    return total'], [], 0, 'Type the complete working Python program.', 'def count():\n    total = 0\n    for i in range(3):\n        total = total + 2\n    return total', 'Trace each statement in order. Check the condition, colon, indentation and final value.'), ('FINAL TRANSMISSION', 'Write win(score) returning score * 2 if score >= 10, otherwise score + 1.', ['def win(score):', '    if score >= 10:', '        return score * 2', '    else:', '        return score - 1'], [], 0, 'Type the complete working Python program.', 'def win(score):\n    if score >= 10:\n        return score * 2\n    else:\n        return score + 1', 'Trace each statement in order. Check the condition, colon, indentation and final value.')]
BOSS_Q={r:[r*6+i for i in range(1,6)] for r in range(5)}
STATIONS={0:[(110,144,0)],1:[(501,145,1)],2:[(125,140,2)],3:[(482,145,3)],4:[(475,280,4)]}

NPCS={0:[(307,282,'GUIDE','The gate forks when a condition is true or false. Search the east wall for supplies.')],
1:[(310,278,'PATCH','A broken else branch can trap you. Look for hidden seams.')],
2:[(309,286,'SCOUT','Only one branch should run. The bow has been upgraded. Search the walls for hidden vaults.')],
3:[(315,278,'CIPHER','Game states decide when you win or lose. Bombs are in the east.')],
4:[(314,283,'KEEPER','Repair the final conditions and claim the relics.')]}
# Mentors reinforce accumulated Python skills across earlier levels.
MENTORS={
 'PROFESSOR PIXEL':{'room':0,'pos':(310,139),'color':(83,183,224),'intro':'The keeper of the forked gates.', 'topics':[('What is a decision?','An if condition checks whether something is true. Only then does its indented block run.','TIP: IF CHECKS A CONDITION.'),('What does == mean?','Two equals signs compare values. One equals sign assigns a value.','TIP: == COMPARES; = ASSIGNS.'),('How do I repair the gates?','Read the goal, inspect the broken code, then type the complete corrected Python snippet.','TIP: CTRL+ENTER TESTS YOUR REPAIR.')], 'gift':('potion',1)},
 'SPROCKET':{'room':1,'pos':(310,135),'color':(240,120,82),'intro':'Engineer of the truth engine.', 'topics':[('What is else?','Else runs when the if condition is false. The else line ends with a colon.','TIP: ELSE HANDLES THE OTHER CASE.'),('How do I indent?','The lines inside an if or else block need four spaces. Press Tab in the code editor.','TIP: TAB INSERTS FOUR SPACES.'),('Why does a gate stay locked?','Check >, <, >=, <=, == and !=. One wrong comparison changes the outcome.','TIP: COMPARE THE ACTUAL VALUE.')], 'gift':('potion',1)},
 'RANGER ARROW':{'room':2,'pos':(313,127),'color':(119,202,118),'intro':'The branch scout.', 'topics':[('What are branches?','If checks a condition. Else provides the other outcome. Trace each possibility.','TIP: TEST BOTH OUTCOMES.'),('Can I write more than one condition?','Yes. Use and when both conditions must be true.','TIP: AND REQUIRES BOTH.'),('Where is the bow?','Your bow is ready. Save arrows for secret bosses.','GEAR: FIND THE BOW HERE.')], 'gift':('arrows',6)},
 'ARCHIVIST':{'room':3,'pos':(313,130),'color':(179,119,232),'intro':'Archivist of game states.', 'topics':[('What is a game state?','A variable can hold playing, won, or lost. Conditions decide when it changes.','TIP: STATE = "WON".'),('How do I find the bug?','Predict which branch should run, test the comparison, then repair the code.','TIP: PREDICT, TEST, REPAIR.'),('Where are bombs?','Bombs are powerful against the secret bosses. Search every alcove.','GEAR: BOMBS IN STAGE FOUR.')], 'gift':('bombs',2)},
 'KEEPER':{'room':4,'pos':(317,135),'color':(220,188,95),'intro':'Keeper of the Void Engine.', 'topics':[('What opens the final gate?','Complete the code repairs, trace both branches, and defeat the guardian.','TIP: REPAIR ALL DECISIONS.'),('What is a win state?','When the win condition is true, set state to "won".','TIP: STATE = "WON".'),('Any final advice?','A missing colon or indentation can change whether code runs at all.','TIP: CHECK COLONS AND SPACES.')], 'gift':('potion',1)},
 'ECHO':{'room':'secret','pos':(450,253),'color':(117,217,241),'intro':'A hidden debugger.', 'topics':[('Why use if and else?','They create different outcomes for true and false conditions.','TIP: TRACE BOTH PATHS.'),('What is the most common bug?','Wrong comparisons, missing colons and indentation.','TIP: READ EVERY CHARACTER.'),('How did you find this room?','Secret chambers reward explorers who notice unusual details.','TIP: LOOK FOR SEAMS.')], 'gift':('potion',1)}}

# Five distinct, mandatory puzzle systems. Every puzzle has a retryable hint.
PUZZLE_NAMES=['STAR MAP ALIGNMENT', 'THE LIVING INDEX', 'REFLECTION ROUTING MATRIX', 'THUNDER REACTOR SEQUENCE', 'THE FIVE-LOCK VOID ENGINE']
PUZZLE_POS=[(380,284),(530,275),(530,275),(530,275),(530,275)]
puzzle_done=set(); puzzle_attempts=[0]*5; puzzle_hints=[0]*5
puzzle_step=0; puzzle_selected=0; puzzle_feedback=''; puzzle_feedback_timer=0
PUZZLE_DATA=[[('A student holds LEFT while x = 240 and speed = 5. The program uses if keyboard.left: followed by x = x - speed. What is x after one update?', ['245', '235', '240'], 1)], [('The right arrow is released. The program checks if keyboard.right: then adds 4 to x. x begins at 100. What happens?', ['x becomes 104', 'x stays 100', 'x becomes 96'], 1)], [('A hero moves left even when no key is pressed. The line x = x - speed is not indented under if keyboard.left:. What is the best diagnosis?', ['The movement runs outside the condition', 'The screen is too wide', 'The hero needs a new color'], 0)], [('A student writes if keyboard.right without a colon, then indents x = x + speed. The program will not run. What fixes the syntax?', ['Replace + with -', 'Remove indentation', 'Add : after keyboard.right'], 2)], [('The hero begins at x=300 with speed=6. LEFT is held for one update, then RIGHT for one update. Both if blocks are correctly written. What is the final x?', ['288', '300', '312'], 1)]]
PUZZLE_HINTS=['Check each comparison carefully: >= includes equality.','Follow the IF branch when true and ELSE when false.','AND is true only when both sides are true.','Trace when the state changes to won or lost.','Work through each decision in order.']

# Mandatory guided learning: three topics and a comprehension check per main-stage mentor.
MAIN_MENTORS=['PROFESSOR PIXEL','SPROCKET','RANGER ARROW','ARCHIVIST','KEEPER']
# The Keeper is a main-stage mentor; Echo remains a bonus secret contact.
MENTORS['KEEPER']={'room':4,'pos':(460,125),'color':(236,198,96),
 'intro':'Guardian of the final arcade restoration.',
 'topics':[('How do functions begin?', 'Write def draw(): with a colon. Put instructions on the next indented line.', 'TIP: def draw(): starts a function.'),
           ('What changes the game?', 'update() changes x or other variables; draw() displays objects using those values.', 'TIP: update changes values; draw displays.'),
           ('How can if help with score?', 'An if statement can check whether the player is near a coin, then add one to score.', 'TIP: SCORE INCREASES WHEN BOTH DECISIONS ARE CLOSE.')],
 'gift':('potion',1)}
LESSON_CHECKS={'PROFESSOR PIXEL': [('What does keyboard.left detect?', ['A left-arrow press', 'A mouse click', 'The player position'], 0, 'keyboard.left becomes true when the left arrow is held.'), ('What happens to x after x = x - speed?', ['It increases', 'It decreases', 'It stays the same'], 1, 'Subtracting speed decreases x and moves the player left.'), ('Why put movement under if keyboard.left?', ['It runs always', 'It changes the background', 'It runs only while LEFT is held'], 2, 'The indented movement only runs when the condition is true.')], 'SPROCKET': [('Which condition checks the right arrow?', ['if keyboard.right:', 'if keyboard.left:', 'if right:'], 0, 'keyboard.right reads the right arrow; the colon begins the block.'), ('What does x = x + speed do?', ['Moves left', 'Moves right', 'Stops movement'], 1, 'Adding speed increases x, moving the player right.'), ('What is missing in if keyboard.right?', ['A number', 'A quote', 'A colon'], 2, 'The if header must end in a colon.')], 'RANGER ARROW': [('Which value changes during horizontal movement?', ['x', 'HEIGHT', 'color'], 0, 'Horizontal movement changes the x coordinate.'), ('What if LEFT is not pressed?', ['The left block runs', 'The left block is skipped', 'The game ends'], 1, 'When the condition is false, its indented block does not run.'), ('Which line belongs under if keyboard.left:?', ['screen.fill("black")', 'WIDTH = 640', '    x = x - speed'], 2, 'Indent the movement line to make it conditional.')], 'ARCHIVIST': [('Why use a speed variable?', ['To adjust movement in one place', 'To change the screen title', 'To create a new key'], 0, 'A variable lets you adjust how far x changes each update.'), ('If x=100 and speed=4, x=x+speed gives?', ['96', '104', '100'], 1, 'Add four to 100 to get 104.'), ('If x=100 and speed=4, x=x-speed gives?', ['104', '100', '96'], 2, 'Subtract four from 100 to get 96.')], 'KEEPER': [('Which function changes movement values each frame?', ['update()', 'draw()', 'screen.fill()'], 0, 'update() changes values while draw() displays the result.'), ('Where should screen.draw.filled_circle() go?', ['Inside keyboard.left', 'Inside draw()', 'Inside HEIGHT'], 1, 'draw() is where the circle is displayed on the screen.'), ('What does a false keyboard condition do?', ['Moves twice', 'Crashes the program', 'Skips its indented block'], 2, 'If the arrow is not held, Python skips that if block.')]}
LEVEL5_TOPICS={
 'PROFESSOR PIXEL':[('How do I store a value?','Use a single equals sign to assign a number to a variable.','TIP: COINS = 5.'),('How do I change a value?','Read the old variable, add a number, then assign the result back.','TIP: COINS = COINS + 2.'),('How do I store words?','Use quotation marks around text, such as status = "READY".','TIP: QUOTE STRINGS.')],
 'SPROCKET':[('How do conditions work?','An if statement checks a comparison. Use > for greater than.','TIP: IF WATER > 10:'),('What is equality?','Double equals signs compare values, while one equals sign assigns.','TIP: == COMPARES.'),('What does at least mean?','Greater than or equal to uses >=, including the boundary.','TIP: PRESSURE >= 6.')],
 'RANGER ARROW':[('How does screen movement work?','Left subtracts from x, right adds to x, up subtracts from y, down adds to y.','TIP: UP MEANS Y DECREASES.'),('How do I detect a key?','keyboard.left, keyboard.right, keyboard.up and keyboard.down become true while held.','TIP: IF KEYBOARD.LEFT:'),('How do I keep the player on screen?','Check whether x crosses a boundary, then set it back to the limit.','TIP: IF X < 0: X = 0.')],
 'ARCHIVIST':[('What is a for loop?','for i in range(3) repeats the indented block three times.','TIP: RANGE(3) REPEATS 3 TIMES.'),('How can I count down?','Subtract from the timer on each loop iteration.','TIP: TIMER = TIMER - 1.'),('Why does indentation matter?','The lines under the for loop must be indented to repeat.','TIP: TAB ADDS FOUR SPACES.')],
 'KEEPER':[('What is a function?','A function starts with def, a name, parentheses and a colon.','TIP: DEF POWER():'),('What does return do?','return sends a value back from a function to the code that called it.','TIP: RETURN 10.'),('How do parameters work?','A parameter such as n receives a value. You can calculate and return with it.','TIP: RETURN N * 3.')]
}
for _mentor,_topics in LEVEL5_TOPICS.items():
    MENTORS[_mentor]['topics']=_topics

mentor_topics_done=set(); mentor_checks_done=set(); mentor_check_attempts={name:[0,0,0] for name in MAIN_MENTORS}
check_name=''; check_topic=0; check_selected=0; check_feedback=''
mentor_retry_locks={}
mentor_met=set(); mentor_gifts=set(); journal=[]; journal_page=0
chat_name=''; chat_selected=0; chat_page='menu'; chat_topic=0
player_name=''; player_experience=''; conversation_steps=0
CHESTS={0:(530,207,'potion'),1:(320,218,'potion'),2:(524,213,'bow'),3:(527,207,'bombs'),4:(320,215,'armor')}
ARTIFACTS={0:(94,285,'FORKED KEY'),2:(110,136,'TRUTH SHARD'),3:(94,285,'STATE CORE')}
WALLS={
0:[pygame.Rect(200,90,18,98),pygame.Rect(420,210,18,93)],
1:[pygame.Rect(180,180,130,18),pygame.Rect(350,180,120,18),pygame.Rect(310,180,18,60)],
2:[pygame.Rect(215,100,18,120),pygame.Rect(410,175,18,122),pygame.Rect(215,215,90,18)],
3:[pygame.Rect(220,92,18,145),pygame.Rect(402,152,18,145),pygame.Rect(238,235,95,18)],
4:[pygame.Rect(215,190,110,18),pygame.Rect(325,190,100,18),pygame.Rect(305,207,18,90)]}

rooms_done=set(); solved=set(); chests=set(); artifacts=set(); opened=set()
# Wall secrets are not drawn as objects. Each north/south wall has normal-looking tiles.
# Nearby NPC clues and subtle tile seams reward careful observation.
SECRETS={
 0:[(65,112,'ARTIFACT','A loose wall tile hides the GOLD CARTRIDGE.'),(557,112,'CACHE','An old cabinet contains a speed module.')],
 1:[(86,112,'CACHE','A cracked panel conceals two health potions.'),(553,305,'CACHE','A hidden drawer holds eight arrows.')],
 2:[(86,112,'ARTIFACT','Behind the wall is the PIXEL CRYSTAL.'),(557,112,'CACHE','A dusty machine contains a sword upgrade.')],
 3:[(86,306,'ARTIFACT','You uncover the GLITCH CHIP.'),(555,112,'CACHE','A hidden compartment holds three bombs.')],
 4:[(86,112,'CACHE','A vault panel hides a full heal.'),(555,112,'CACHE','A forgotten terminal holds extra arrows.')]
}
secret_found=set(); chamber_cleared=set(); secret_room=False; secret_origin=0; secret_index=0; npc_gifts=set(); boss_hacks_room={r:0 for r in range(5)}

stats={'runs':0,'gameovers':0,'lives':0,'damage':0,'kills':0,'attempts':[0]*len(Q),'wrong':0,'victories':0,'seconds':0.,'rooms':set(),'secrets':0,'chests':0,'dashes':0,'talks':0,'lessons':0,'puzzles':0}
room=0; player=pygame.Rect(75,283,19,25); facing=(0,1); frame=0
hp=5; max_hp=5; lives=3; weapon='PIXEL SWORD'; has_bow=True; bombs=0; arrows=12; potions=0
state='title'; active=0; selected=0; code_input=''; code_cursor=0; code_feedback=''; invuln=0; attack_time=0; attack_cd=0; dash_time=0; dash_cd=0; speed_upgrade=False; sword_upgrade=False; moving=False
message=''; msg_timer=0; bugs=[]; shots=[]; pickups=[]; sparks=[]; hit_fx=[]; boss=None; boss_hp=0
boss_open=0; boss_shot=0; boss_question=0; boss_hacks=0; boss_quiz=False; spawn_cd=0; copy_msg=''; waves=0; report_return='world'; reinforce_count=0; reinforce_timer=0; secret_bugs=[]; secret_chest_open=False
secret_lock_solved=set(); secret_lock_selected=0
repair_locks={}; repair_successes=0
# Overdrive and legendary challenge progress reset for each new adventure.
crystals=set(); crystal_bank=0; overdrive_charges=0; overdrive_time=0
overdrive_earned=0; overdrive_uses=0; crystal_total=0; pending_crystals=0
legendary=set(); gauntlet_room=1; gauntlet_x=45; gauntlet_y=200
gauntlet_hits=0; gauntlet_cooldown=0; gauntlet_return=(70,275)
victory_kind=''; victory_countdown=0
CRYSTAL_SPOTS={
 0:[(70,210),(352,116),(531,298),(320,190),(475,245)],
 1:[(85,190),(205,285),(404,115),(535,235),(347,290)],
 2:[(84,275),(173,296),(332,105),(465,191),(552,289)],
 3:[(89,199),(194,295),(338,111),(482,220),(546,291)],
 4:[(88,195),(195,293),(320,110),(474,197),(548,289)]
}
RESTRICTED={
 1:('PRISM SWITCHYARD','PRISM HEART',(538,110)),
 2:('SHADOW LOGIC MAZE','ECHO BLADE',(533,285)),
 3:('FRACTURED CORE','PHASE RELIC',(103,110))
}

def draw_text(t,x,y,c=WHITE,font=F): screen.blit(font.render(str(t),True,c),(int(x),int(y)))
def center(t,y,c=WHITE,font=F):
    im=font.render(str(t),True,c); screen.blit(im,((W-im.get_width())//2,int(y)))
def box(x,y,w,h,c,r=0): pygame.draw.rect(screen,c,(int(x),int(y),int(w),int(h)),border_radius=r)
def tell(t,delay=180):
    global message,msg_timer
    message=t; msg_timer=delay

def bug(x,y,kind=None):
    kind=kind or random.choice(['wander','patrol','hunter','shooter','charger'])
    return {'x':float(x),'y':float(y),'kind':kind,'hp':4 if kind=='charger' else 3,
            'phase':random.random()*7,'turn':random.uniform(-3,3),'timer':random.randrange(55,145),'speed':1.0+room*.19,'vx':random.choice([-1,1]),'shot':random.randrange(70,140),'charge':0,'tell':0,'base_x':float(x),'base_y':float(y),'max_hp':4 if kind=='charger' else 3,'flash':0,'hurt':0}

def enter_room(n):
    global room,bugs,boss,boss_hp,boss_open,boss_shot,spawn_cd,waves,shots,reinforce_count,reinforce_timer
    room=n; stats['rooms'].add(n); bugs=[]; shots=[]; pickups.clear()
    spawn_cd=150; boss=None; boss_open=0; waves=1; reinforce_count=0; reinforce_timer=140
    if n==0: positions=[(260,190),(365,210),(450,265),(185,255)]
    elif n==1: positions=[(115,220),(485,125),(448,275),(175,275),(380,275)]
    elif n==2: positions=[(130,215),(330,145),(475,145),(480,285),(320,280),(120,280)]
    elif n==3: positions=[(128,150),(315,265),(490,170),(465,290),(150,275),(345,120)]
    else: positions=[(116,170),(500,160),(120,285),(505,280)]
    if n not in rooms_done:
        for i,(x,y) in enumerate(positions): bugs.append(bug(x,y,[['patrol','wander','shooter','hunter','charger'],['shooter','patrol','charger','hunter','wander'],['hunter','charger','patrol','shooter','wander'],['charger','shooter','hunter','patrol','wander'],['hunter','shooter','charger','patrol','charger']][n][i%5]))
    else: waves=3
    player.topleft=(56,279)
    tell('AREA '+str(n+1)+': '+ROOMS[n]+'  |  FIND STATIONS, CHESTS, AND ARTIFACTS',200)

def new_game():
    global hp,max_hp,lives,weapon,has_bow,bombs,arrows,potions,state,invuln
    global secret_lock_solved,secret_lock_selected,evolution_seen,repair_locks,repair_successes,puzzle_retry_locks,mentor_retry_locks
    global rooms_done,solved,chests,artifacts,opened,boss_hacks,boss_quiz,secret_found,npc_gifts,boss_hacks_room,dash_cd,dash_time,speed_upgrade,sword_upgrade,secret_room,secret_origin,secret_index,chamber_cleared,secret_bugs,secret_chest_open,mentor_met,mentor_gifts,journal,journal_page,puzzle_done,puzzle_attempts,puzzle_hints,mentor_topics_done,mentor_checks_done,mentor_check_attempts,player_name,player_experience
    evolution_seen=0
    stats['runs']+=1; hp=5; max_hp=5; lives=3; weapon='PIXEL SWORD'; has_bow=True
    bombs=8; arrows=32; potions=3; invuln=0; boss_hacks=0; boss_quiz=False
    secret_lock_solved=set();secret_lock_selected=0;secret_boss_defeated.clear();secret_code_locks.clear();repair_locks={};repair_successes=0;puzzle_retry_locks={};mentor_retry_locks={}
    rooms_done=set(); solved=set(); chests=set(); artifacts=set(); opened=set(); secret_found=set(); chamber_cleared=set(); secret_room=False; secret_origin=0; secret_index=0; npc_gifts=set(); boss_hacks_room={r:0 for r in range(5)}; dash_cd=0; dash_time=0; speed_upgrade=False; sword_upgrade=False
    mentor_met=set(); mentor_gifts=set(); journal=[]; journal_page=0; puzzle_done=set(); puzzle_attempts=[0]*5; puzzle_hints=[0]*5; mentor_topics_done=set(); mentor_checks_done=set(); mentor_check_attempts={name:[0,0,0] for name in MAIN_MENTORS}
    player_name=''; player_experience=''
    global crystals,crystal_bank,overdrive_charges,overdrive_time,overdrive_earned,overdrive_uses,crystal_total,pending_crystals,legendary,gauntlet_hits,gauntlet_cooldown,victory_kind,victory_countdown
    crystals=set(); crystal_bank=0; overdrive_charges=0; overdrive_time=0
    overdrive_earned=0; overdrive_uses=0; crystal_total=0; pending_crystals=0; legendary=set()
    gauntlet_hits=0; gauntlet_cooldown=0; victory_kind=''; victory_countdown=0
    enter_room(0); state='world'

def heart(x,y,on):
    c=RED if on else (72,67,91)
    pygame.draw.circle(screen,c,(x+5,y+6),5)
    pygame.draw.circle(screen,c,(x+13,y+6),5)
    pygame.draw.polygon(screen,c,[(x,y+8),(x+18,y+8),(x+9,y+19)])

# Evolution is earned through repairs, completed mentor checks, and puzzle clears.
# Five forms are visual only: the original player collision rectangle stays unchanged.
EVOLUTION_NAMES = ('ROOKIE BUSTER', 'CIRCUIT INITIATE', 'CYBER GUARDIAN',
                   'MECH BUSTER', 'GLITCH TITAN')
evolution_seen = 0

def evolution_points():
    return len(solved) + len(mentor_checks_done) + 2 * len(puzzle_done)

def evolution_form():
    points = evolution_points()
    if points >= 29: return 4
    if points >= 19: return 3
    if points >= 11: return 2
    if points >= 4: return 1
    return 0

def evolution_check():
    global evolution_seen
    current = evolution_form()
    if current > evolution_seen:
        evolution_seen = current
        tell('EVOLUTION UNLOCKED: ' + EVOLUTION_NAMES[current] + '!', 250)
        play_sfx('unlock')
        journal_add('HERO EVOLVED: ' + EVOLUTION_NAMES[current])

def draw_evolved_hero(x, y, bob, form):
    # The same recognizable blue-clad hero acquires mechanical parts over time.
    # Scaling affects appearance, never hitboxes or movement through walls.
    scale = (1.0, 1.08, 1.16, 1.25, 1.34)[form]
    def rect(dx, dy, w, h, color, radius=0):
        rw=max(1,round(w*scale)); rh=max(1,round(h*scale))
        box(x+round(dx*scale), y+round(dy*scale)+bob, rw, rh, color, radius)
    metal=(119,160,193); dark=(40,67,102); glow=GOLD if overdrive_time else CYAN
    pygame.draw.ellipse(screen,(13,16,34),(x-round(14*scale),y+13,round(28*scale),8))
    # Legs progressively turn into reinforced mechanical boots.
    leg=metal if form>=2 else (43,51,91)
    rect(-8,5,7,12,leg); rect(2,5,7,12,leg)
    rect(-10,13,9,5,dark if form>=2 else (27,28,43))
    rect(2,13,9,5,dark if form>=2 else (27,28,43))
    if form>=2:
        rect(-6,8,3,3,glow); rect(4,8,3,3,glow)
    # Original blue jacket remains recognizable under armor.
    rect(-11,-6,22,17,(43,100,197),3)
    rect(-11,2,22,4,GOLD if 1 in legendary else (26,66,144))
    if form>=3:
        rect(-12,-9,24,7,metal,3)
        rect(-3,-4,6,7,glow,2)
        rect(-15,-6,4,11,dark); rect(11,-6,4,11,dark)
    # First the right arm, then both arms, become robotic.
    rect(-15,-3,5,12,metal if form>=3 else (228,171,121))
    rect(10,-3,5,12,metal if form>=1 else (228,171,121))
    if form>=1: rect(11,3,3,4,glow)
    if form>=3: rect(-14,3,3,4,glow)
    # Keep the original face and hair visible until the final evolution.
    face=metal if form==4 else (237,183,137)
    rect(-8,-19,16,16,face,4)
    if form<4:
        rect(-10,-21,20,7,(81,48,39),3)
        rect(-10,-17,4,7,(81,48,39))
    else:
        rect(-11,-22,22,7,dark,3)
        rect(-12,-16,3,12,metal); rect(9,-16,3,12,metal)
    if form>=2:
        rect(-9,-13,18,5,dark,2)
        rect(-7,-12,14,2,glow)
    elif facing[0]:
        rect(4 if facing[0]>0 else -5,-12,2,3,(26,32,53))
    elif facing[1]>0:
        rect(-5,-12,2,3,(26,32,53)); rect(3,-12,2,3,(26,32,53))
    if form>=4:
        rect(-14,-12,4,8,metal); rect(10,-12,4,8,metal)
        pygame.draw.circle(screen,glow,(x,y-1+bob),round(4*scale),2)
    if form>=1:
        pygame.draw.line(screen,glow,(x+round(11*scale),y+bob),
                         (x+round(14*scale),y+round(8*scale)+bob),2)
    if overdrive_time:
        pygame.draw.circle(screen,glow,(x,y-4),round(17*scale),2)

def human():
    x,y=player.centerx,player.centery
    if invuln and frame%8<4: return
    bob=int(moving and frame%12<6)*2
    draw_evolved_hero(x, y, bob, evolution_form())
    if attack_time:
        fx,fy=facing; sx=x+fx*12; sy=y+fy*12
        if weapon=='PUNCH':
            pygame.draw.circle(screen,(239,189,137),(sx+fx*7,sy+fy*7),5)
        else:
            ax=fx*.75-fy*.66; ay=fy*.75+fx*.66
            tip=(int(sx+ax*34),int(sy+ay*34))
            pygame.draw.line(screen,(25,34,62),(sx,sy),tip,12)
            pygame.draw.line(screen,PURPLE if 2 in legendary else (110,185,221),(sx,sy),tip,9)
            pygame.draw.line(screen,WHITE,(int(sx+ax*9),int(sy+ay*9)),tip,4)
            pygame.draw.polygon(screen,WHITE,[tip,(int(tip[0]-ax*8+ay*5),int(tip[1]-ay*8-ax*5)),(int(tip[0]-ax*8-ay*5),int(tip[1]-ay*8+ax*5))])
            pygame.draw.line(screen,GOLD,(int(sx-ay*9),int(sy+ax*9)),(int(sx+ay*9),int(sy-ax*9)),5)

def draw_mentor(name,x,y,color):
    # Distinct hair, clothes, and a small animated face; no floating question marks.
    bob=1 if frame%40<20 else 0
    pygame.draw.ellipse(screen,(14,19,32),(x-13,y+15,26,7))
    box(x-8,y+8,7,11,(36,39,62)); box(x+2,y+8,7,11,(36,39,62))
    box(x-12,y-4,24,16,color,4)
    box(x-8,y-17+bob,16,16,(238,185,138),4)
    hair=(68,52,43) if name=='PROFESSOR PIXEL' else (173,74,40) if name=='SPROCKET' else (44,41,71) if name=='ARCHIVIST' else (78,64,38) if name=='RANGER ARROW' else (157,210,231)
    box(x-9,y-20+bob,18,6,hair,2)
    if name=='PROFESSOR PIXEL':
        pygame.draw.rect(screen,WHITE,(x-7,y-11+bob,6,5),1)
        pygame.draw.rect(screen,WHITE,(x+2,y-11+bob,6,5),1)
    elif name=='SPROCKET':
        box(x-11,y-20+bob,22,4,GOLD)
    elif name=='ARCHIVIST':
        pygame.draw.polygon(screen,hair,[(x-15,y-6),(x,y-27),(x+15,y-6)])
    elif name=='RANGER ARROW':
        pygame.draw.arc(screen,GOLD,(x+7,y-5,13,23),-1.5,1.5,2)
    else:
        pygame.draw.circle(screen,CYAN,(x,y-9+bob),11,1)
    box(x-4,y-10+bob,2,2,(24,29,46)); box(x+3,y-10+bob,2,2,(24,29,46))
    short={'PROFESSOR PIXEL':'PROF. PIXEL','SPROCKET':'SPROCKET','ARCHIVIST':'ARCHIVIST','RANGER ARROW':'RANGER','ECHO':'ECHO','KEEPER':'KEEPER'}[name]
    draw_text(short,x-29,y+21,GOLD,S)

def journal_add(entry):
    if entry not in journal:
        journal.append(entry)
        stats['lessons']+=1

def wrap_lines(value,max_chars=62):
    words=value.split(); lines=[]; current=''
    for word in words:
        trial=(current+' '+word).strip()
        if len(trial)>max_chars and current:
            lines.append(current); current=word
        else: current=trial
    if current: lines.append(current)
    return lines

def hero_name():
    return player_name.strip() or 'adventurer'

def talk_to(name):
    global state,chat_name,chat_selected,chat_page,chat_topic
    chat_name=name; chat_selected=0; chat_topic=0; state='dialogue'
    if name=='PROFESSOR PIXEL' and not player_name:
        chat_page='hello'
    else:
        chat_page='hello_return' if name in mentor_met else 'hello'
    mentor_met.add(name); stats['talks']+=1
    journal_add('MET '+name+': '+MENTORS[name]['intro'])

def begin_topic(topic):
    global chat_page,chat_topic,potions,bombs,arrows
    chat_topic=topic; chat_page='story'
    title,response,note=MENTORS[chat_name]['topics'][topic]
    journal_add(note)
    mentor_topics_done.add((chat_name,topic))
    if chat_name not in mentor_gifts:
        mentor_gifts.add(chat_name)
        kind,amount=MENTORS[chat_name]['gift']
        if kind=='potion': potions+=amount
        elif kind=='bombs': bombs+=amount
        elif kind=='arrows': arrows+=amount
        journal_add('GIFT FROM '+chat_name+': '+str(amount)+' '+kind.upper())

def select_chat():
    begin_topic(chat_selected)

def dialogue_advance():
    global chat_page,chat_selected,player_experience
    if chat_page=='hello':
        chat_page='name' if chat_name=='PROFESSOR PIXEL' and not player_name else 'menu'
    elif chat_page=='hello_return': chat_page='menu'
    elif chat_page=='name':
        if player_name.strip(): chat_page='experience'
    elif chat_page=='experience':
        player_experience=['brand new to coding','tried coding before','made a game before'][chat_selected]
        journal_add('CODING EXPERIENCE: '+player_experience)
        chat_page='experience_reply'
    elif chat_page=='experience_reply': chat_page='menu'
    elif chat_page=='story': chat_page='reflection'
    elif chat_page=='reflection':
        if chat_name in MAIN_MENTORS and (chat_name,chat_topic) not in mentor_checks_done:
            start_mentor_check()
        else: chat_page='menu'
    elif chat_page=='menu': select_chat()

def dialogue_screen():
    mentor=MENTORS[chat_name]
    modal(chat_name+' // CONVERSATION','Talking with '+chat_name+'  |  '+hero_name())
    box(48,143,544,158,(27,37,59),7)
    def lines(t,y=160):
        for i,line in enumerate(wrap_lines(t,61)[:5]):
            draw_text(line,60,y+i*22,WHITE,S)
    if chat_page in ('hello','hello_return'):
        if chat_page=='hello':
            lines('Hello there! I am '+chat_name+'. '+mentor['intro']+' It is good to meet you, '+hero_name()+'!')
        else:
            lines('Welcome back, '+hero_name()+'! The arcade is still counting on us. What shall we explore next?')
    elif chat_page=='name':
        lines('Before we start, what should I call you? Type your first name or a classroom nickname. It will appear on your final Mission Report. Do not enter your full name.')
        box(65,260,485,28,(52,69,99),4)
        draw_text((player_name or 'TYPE NAME HERE')+'|',75,266,GOLD,S)
    elif chat_page=='experience':
        lines('Tell me a little about yourself, '+hero_name()+'. Have you programmed before? There is no wrong answer.')
        for i,t in enumerate(['1. I am brand new!','2. I have tried coding.','3. I have made a game.']):
            y=237+i*29
            box(60,y,516,26,(48,89,95) if i==chat_selected else (35,47,72),4)
            draw_text(t,72,y+5,WHITE,S)
    elif chat_page=='experience_reply':
        if chat_selected==0: lines('Welcome to programming, '+hero_name()+'! Every expert started by trying one little idea. We will learn by experimenting.')
        elif chat_selected==1: lines('Wonderful, '+hero_name()+'! You already know that programs can surprise us. Let us build on what you have tried.')
        else: lines('A game maker! Then you know a tiny mistake can change the whole adventure. Let us sharpen those debugging skills.')
    elif chat_page=='menu':
        done=sum((chat_name,i) in mentor_checks_done for i in range(3)) if chat_name in MAIN_MENTORS else 0
        lines('I have three things to share, '+hero_name()+'. Which should we talk about?'+(' Lessons '+str(done)+'/3.' if chat_name in MAIN_MENTORS else ''))
        for i,(title,_,_) in enumerate(mentor['topics']):
            y=213+i*29
            flag=' [DONE]' if (chat_name,i) in mentor_checks_done else ''
            box(60,y,516,26,(48,89,95) if i==chat_selected else (35,47,72),4)
            draw_text(str(i+1)+'. '+title+flag,72,y+5,WHITE,S)
    elif chat_page=='story':
        title,response,_=mentor['topics'][chat_topic]
        lines('You asked: '+title+'  '+response)
    elif chat_page=='reflection':
        title,response,_=mentor['topics'][chat_topic]
        if (chat_name,chat_topic) in mentor_checks_done:
            lines('You have already shown me you understand this, '+hero_name()+'. Excellent work. Ready for another topic?')
        elif chat_name in MAIN_MENTORS:
            lines('Now, '+hero_name()+', let us try something together. I will describe a situation from the arcade, and you tell me what you would do. Mistakes are welcome; we learn by testing.')
        else: lines('I hope that helps, '+hero_name()+'. You can come back to ask about the other secrets whenever you like.')
    box(48,306,544,29,(43,93,89),5)
    label='ENTER: CONTINUE'
    if chat_page=='name': label='TYPE NAME, THEN ENTER'
    elif chat_page in ('menu','experience'): label='UP/DOWN OR 1-3, THEN ENTER'
    elif chat_page=='reflection' and chat_name in MAIN_MENTORS and (chat_name,chat_topic) not in mentor_checks_done: label='ENTER: LET US TRY IT TOGETHER'
    draw_text(label,61,314,WHITE,S)
    draw_text('BACKSPACE: RETURN TO GAME   |   CLICK CONTINUE',50,352,GOLD,S)

MENTOR_CODE_TASKS = {'PROFESSOR PIXEL': [('Set coins to 5.', 'coins = 5', 'Use = to store five coins.'), ('Increase coins by 2.', 'coins = coins + 2', 'Add two to the current value.'), ("Store 'READY' in status.", "status = 'READY'", 'Strings need quotation marks.')], 'SPROCKET': [('When water is above 10, set gate to True.', 'if water > 10:\n    gate = True', 'Use > and indent the action.'), ('When fuel equals 0, set alarm to True.', 'if fuel == 0:\n    alarm = True', 'Use == to compare equality.'), ('When pressure is at least 6, subtract 2 from pressure.', 'if pressure >= 6:\n    pressure = pressure - 2', 'At least means >=; subtraction reduces pressure.')], 'RANGER ARROW': [('When LEFT is pressed, decrease x by speed.', 'if keyboard.left:\n    x = x - speed', 'Left subtracts from x.'), ('When DOWN is pressed, increase y by speed.', 'if keyboard.down:\n    y = y + speed', 'Down increases y.'), ('When x is less than 0, reset x to 0.', 'if x < 0:\n    x = 0', 'Clamp x at the left edge.')], 'ARCHIVIST': [('Loop three times and increase score by 1.', 'for i in range(3):\n    score = score + 1', 'range(3) loops three times.'), ('Loop twice and decrease timer by 1.', 'for i in range(2):\n    timer = timer - 1', 'Decrease once on each iteration.'), ('Loop four times and add 2 to charge.', 'for i in range(4):\n    charge = charge + 2', 'Four repetitions add eight total.')], 'KEEPER': [('Write power() to return 10.', 'def power():\n    return 10', 'return provides the result.'), ('Write triple(n) to return n * 3.', 'def triple(n):\n    return n * 3', 'The parameter n is multiplied by three.'), ('Write can_enter(level) to return level >= 5.', 'def can_enter(level):\n    return level >= 5', 'At least five includes equality.')]}
def reset_code_editor():
    global code_input,code_cursor,code_feedback
    code_input='';code_cursor=0;code_feedback=''
def start_mentor_check():
    global state,check_name,check_topic,chat_page
    if chat_name not in MAIN_MENTORS or (chat_name,chat_topic) in mentor_checks_done:
        chat_page='menu';return
    if mentor_retry_locks.get((chat_name,chat_topic),-1)>=len(mentor_checks_done)+repair_successes:
        tell('COMPLETE A DIFFERENT REPAIR OR LESSON FIRST.',180);chat_page='menu';state='world';return
    check_name=chat_name;check_topic=chat_topic;reset_code_editor();state='mentor_check'
def answer_mentor_check():
    global state,check_feedback,chat_page,repair_successes
    mentor_check_attempts[check_name][check_topic]+=1
    prompt,expected,why=MENTOR_CODE_TASKS[check_name][check_topic]
    if code_normalize(code_input)==code_normalize(expected):
        mentor_checks_done.add((check_name,check_topic));repair_successes+=1
        journal_add('CODE LESSON PASSED: '+check_name+' '+str(check_topic+1))
        check_feedback='CODE ACCEPTED! '+why;state='mentor_result';play_sfx('repair')
    else:
        stats['wrong']+=1
        mentor_retry_locks[(check_name,check_topic)]=len(mentor_checks_done)+repair_successes
        check_feedback='DEBUG NOTE: '+why+' WORKING CODE: '+expected.replace('\n',' / ')
        state='mentor_retry'
def code_task_screen(title,prompt,broken=None):
    modal(title,'WRITE PYTHON, NOT A MULTIPLE-CHOICE ANSWER.')
    for i,line in enumerate(wrap_lines(prompt,69)[:3]):draw_text(line,48,130+i*17,WHITE,S)
    if broken:
        box(48,180,544,45,(45,35,62),5)
        for i,line in enumerate(broken.split('\n')[:2]):draw_text(line,58,185+i*17,PINK,S)
    box(47,233,546,101,(18,38,48),6)
    lines=code_input.split('\n')
    for i,line in enumerate(lines[-5:]):draw_text(line[:78],58,239+i*18,GREEN,S)
    before=code_input[:code_cursor];row=before.count('\n');col=len(before.rsplit('\n',1)[-1]);offset=max(0,len(lines)-5)
    if offset<=row<offset+5 and frame%40<25:
        cx=58+S.size(lines[row][:col])[0];cy=239+(row-offset)*18
        pygame.draw.line(screen,GOLD,(cx,cy),(cx,cy+14),2)
    draw_text('TAB: INDENT   ENTER: NEW LINE   CTRL+ENTER: TEST CODE',49,347,GOLD,S)
    if code_feedback:draw_text(code_feedback[:85],49,367,PINK,S)
def mentor_check_screen():
    prompt,expected,why=MENTOR_CODE_TASKS[check_name][check_topic]
    code_task_screen(check_name+' // CODE LAB '+str(check_topic+1)+'/3',prompt)

def mentor_result_screen():
    modal('LESSON CHECK // '+('COMPLETE' if state=='mentor_result' else 'TRY AGAIN'),'Learning is part of restoring the arcade.')
    for i,line in enumerate(wrap_lines(check_feedback,57)):
        draw_text(line,50,158+i*25,GREEN if state=='mentor_result' else GOLD,F)
    done=sum((check_name,i) in mentor_checks_done for i in range(3))
    draw_text('LESSONS COMPLETED: '+str(done)+'/3',50,252,CYAN,F)
    draw_text('ENTER/SPACE: CONTINUE',50,310,GOLD,F)

def journal_screen():
    modal('FIELD JOURNAL // DISCOVERIES','Knowledge, clues, and supplies found while exploring.')
    draw_text('PEOPLE MET '+str(len(mentor_met))+'/5    ENTRIES '+str(len(journal)),52,145,CYAN,F)
    start=journal_page*6
    for i,entry in enumerate(journal[start:start+6]):
        draw_text(str(start+i+1)+'. '+entry[:75],53,177+i*24,WHITE,S)
    if not journal: draw_text('Talk to people to fill your journal.',53,193,GRAY,F)
    draw_text('LEFT/RIGHT: PAGE    J OR BACKSPACE: RETURN',52,318,GOLD,S)

def draw_game_hud(chamber=False):
    # Three separate lines, each with fixed columns and no overlapping labels.
    box(0,0,640,77,(14,17,34))
    title='GLITCH BUSTERS / SECRET CHAMBER' if chamber else 'GLITCH BUSTERS / '+ROOMS[room]
    draw_text(title,12,7,CYAN,F)
    draw_text('ART '+str(len(artifacts))+'/3' + ('' if chamber else '   FIX '+str(len(solved))+'/5'),495,10,GOLD,S)
    for i in range(max_hp): heart(18+i*20,28,i<hp)
    # Label positions are fixed so changing counts never merges adjacent fields.
    equip='SWORD' if weapon!='PUNCH' else 'PUNCH'
    for x,label in [(165,'LIVES '+str(lives)),(231,equip),(310,'ARROWS '+str(arrows if has_bow else 0)),(407,'BOMBS '+str(bombs)),(502,'POTIONS '+str(potions))]:
        draw_text(label,x,33,WHITE,S)
    draw_text('CRYSTALS '+str(crystal_bank)+'/5',17,58,CYAN,S)
    draw_text('OVERDRIVE '+('READY' if crystal_bank==5 else 'CHARGING'),185,58,GOLD if crystal_bank==5 else CYAN,S)
    draw_text('LEGENDARY '+str(len(legendary))+'/3',347,58,CYAN,S)
    draw_text('EVO '+str(evolution_form()+1)+'/5',451,58,GOLD,S)
    if not chamber:
        lessons=sum((MAIN_MENTORS[room],i) in mentor_checks_done for i in range(3))
        draw_text('LESSONS '+str(lessons)+'/3',527,58,GREEN if lessons==3 else GOLD,S)

def draw_game_footer(chamber=False):
    box(0,338,640,62,(15,18,35))
    if chamber:
        notice=message if msg_timer else 'FIND THE EXIT AFTER CLEARING THE CHAMBER'
    elif room not in puzzle_done:
        notice='EXIT LOCKED: SOLVE THE '+('INPUT LAB' if room==0 else 'PUZZLE')+' TO ADVANCE'
    else:
        notice=message if msg_timer else 'EXPLORE, REPAIR, AND DEFEAT THE GUARDIAN'
    # Fit the announcement into its own dedicated strip.
    draw_text(notice[:76],12,343,GOLD,S)
    draw_text('MOVE ARROWS   Z ATTACK   X DASH   C BOW   B BOMB   H HEAL',12,364,WHITE,S)
    draw_text('E INTERACT   V OVERDRIVE   J JOURNAL   R REPORT   M MUSIC',12,382,GRAY,S)
    if overdrive_time:
        draw_text('OD '+str((overdrive_time+59)//60)+'s',555,343,CYAN,S)

def background():
    if secret_room:
        draw_chamber(); return
    screen.fill(BG)
    palette=[(11,24,57),(51,30,48),(30,58,71),(25,35,79),(26,11,54)]
    box(23,63,594,268,palette[room],6)
    for x in range(29,610,27):
        for y in range(68,328,27):
            pygame.draw.rect(screen,(56,61,87),(x,y,25,25),1)
    # LEVEL SIX: Observatory, living library, mirror forge, storm fortress, void machine.
    pulse=math.sin(frame*.032)
    if room==0:
        # Observatory: deep sky, parallax stars, orbital instruments.
        for i in range(65):
            sx=35+(i*83)%564;sy=73+(i*47)%235
            pygame.draw.circle(screen,(115+i%4*28,147+i%3*23,205),(sx,sy),1+(i%7==0))
        for i in range(3):
            r=45+i*36;cx=317;cy=188
            pygame.draw.ellipse(screen,(70+i*24,118+i*18,182),(cx-r,cy-r//2,2*r,r),2)
            angle=frame*.012*(i+1);px=int(cx+math.cos(angle)*r);py=int(cy+math.sin(angle)*r*.5)
            pygame.draw.circle(screen,(254,214,132),(px,py),5+i)
        for x in (78,550):
            pygame.draw.line(screen,(111,158,192),(x,314),(x,111),5)
            pygame.draw.circle(screen,(131,200,238),(x,115),22,3)
    elif room==1:
        # Living archive: tall shelves, enchanted books, floating runes.
        for i in range(9):
            x=37+i*66;pygame.draw.rect(screen,(94,55,67),(x,101,51,217),4)
            for j in range(7):
                yy=118+j*27
                for k in range(4):
                    box(x+7+k*10,yy,7,18,[(133,87,147),(210,137,87),(75,166,177)][(i+j+k)%3])
        for i in range(15):
            x=47+(i*131)%540;y=93+(i*59)%205+int(5*math.sin(frame*.03+i))
            pygame.draw.circle(screen,(218,182,113),(x,y),2)
    elif room==2:
        # Mirror foundry: giant reflective slabs and molten luminous seams.
        for i in range(7):
            x=45+i*83;shift=int(4*math.sin(frame*.03+i))
            pygame.draw.polygon(screen,(66,101,139),[(x,101+shift),(x+49,90+shift),(x+55,292),(x+6,309)],0)
            pygame.draw.polygon(screen,(153,216,226),[(x+6,110+shift),(x+42,105+shift),(x+45,286),(x+12,297)],2)
            pygame.draw.line(screen,(239,136,194),(x+16,118),(x+39,283),2)
        for i in range(9):
            x=62+i*61;pygame.draw.circle(screen,(246,153,91),(x,314+int(pulse*2)),4)
    elif room==3:
        # Storm citadel: crenellations, lightning arcs and reactor pylons.
        for i in range(11):
            x=29+i*54;box(x,113+(i%3)*15,43,203,(44,63,104))
            box(x,105+(i%3)*15,15,15,(85,112,160))
        for i in range(5):
            x=85+i*111;pygame.draw.circle(screen,(110,199,249),(x,184),21,3)
            pygame.draw.line(screen,(83,189,239),(x,184),(x+int(18*math.sin(frame*.07+i)),265),2)
        if frame%65<8:
            pts=[(145,72),(166,123),(149,154),(185,203)]
            pygame.draw.lines(screen,(231,240,255),False,pts,4)
    else:
        # Void engine: rotating polygonal rings, fracture lines, gravity shards.
        cx,cy=319,197
        for r in (47,82,120):
            pts=[(int(cx+math.cos(frame*.013+i*math.tau/8)*r),int(cy+math.sin(frame*.013+i*math.tau/8)*r*.8)) for i in range(8)]
            pygame.draw.lines(screen,(129+r//3,83,201),True,pts,3)
        for i in range(17):
            ang=i*math.tau/17-frame*.014;r=116+i%4*19
            x=cx+math.cos(ang)*r;y=cy+math.sin(ang)*r*.7
            pygame.draw.polygon(screen,(86,213,232) if i%2 else (228,106,194),[(x,y-9),(x+7,y),(x,y+9),(x-7,y)],2)
        pygame.draw.circle(screen,(12,8,31),(cx,cy),31)
        pygame.draw.circle(screen,(240,111,219),(cx,cy),24,3)
    # Neon floor accents and room-specific machinery.
    for j in range(7):
        xx=57+j*82
        pygame.draw.circle(screen,(42,88,108) if room%2==0 else (76,48,112),(xx,86),2)
    for i in range(3):
        xx=43+i*264
        box(xx,74,36,32,(16,23,42),5)
        box(xx+5,79,26,19,(35,71+room*8,105),3)
        pygame.draw.line(screen,PINK,(xx+9,94),(xx+26,84),2)
        box(xx+9,101,18,3,GOLD)
    for x in range(23,618,34):
        box(x,61,31,8,(78,75,119)); box(x,324,31,7,(78,75,119))
    for w in WALLS[room]:
        box(w.x,w.y,w.w,w.h,(78,71,107),3)
        pygame.draw.rect(screen,(139,119,161),w,2)
    for x,y,idx in STATIONS[room]:
        ok=idx in solved; c=GREEN if ok else (CYAN if idx%2==0 else GOLD)
        pygame.draw.circle(screen,(22,74,70) if ok else (57,47,86),(x,y),25)
        box(x-15,y-16,30,31,(20,24,43),4)
        box(x-11,y-12,22,19,c if ok else (65,59,108),2)
        draw_text('OK' if ok else '?',x-9,y-9,(19,26,43) if ok else WHITE,S)
        draw_text('REPAIR',x-23,y+20,c,S)
    for x,y,name,clue in NPCS[room]:
        box(x-10,y-8,20,23,(103,77,164),5)
        pygame.draw.circle(screen,(243,185,134),(x,y-11),9)
        box(x-6,y-16,12,4,(84,48,35))
        draw_text(name,x-18,y+17,GOLD,S)
    for name,data in MENTORS.items():
        if data['room']==room:
            x,y=data['pos']; draw_mentor(name,x,y,data['color'])
    for n,(x,y,item) in CHESTS.items():
        if n==room and n not in chests:
            box(x-15,y-9,30,20,(127,77,42),3)
            box(x-15,y-9,30,7,(213,150,67),2)
            box(x-2,y-6,5,9,GOLD)
    # Mandatory puzzle terminals are large, distinctive and clearly labelled.
    if room not in puzzle_done:
        px,py=PUZZLE_POS[room]
        box(px-28,py-25,56,47,(27,44,64),6)
        box(px-23,py-20,46,29,(64,92,122),4)
        pygame.draw.rect(screen,GOLD,(px-28,py-25,56,47),3,border_radius=6)
        for k in range(3):
            pygame.draw.circle(screen,(98,238,172) if k==0 else CYAN,(px-14+k*14,py-10),4)
        pygame.draw.line(screen,GOLD,(px-15,py+2),(px+15,py+2),2)
        draw_text('DECISION ENGINE' if room==0 else 'PUZZLE PANEL',px-47,py+27,GOLD,S)
        if distance(px,py)<78:
            box(max(30,min(450,px-102)),py-65,204,23,(20,37,55),5)
            draw_text('E - TRACE DECISIONS' if room==0 else 'E - TRACE DECISIONS',max(36,min(456,px-96)),py-59,WHITE,S)

    # Power Crystals are collectible on the main path and in optional detours.
    for i,(cx,cy) in enumerate(CRYSTAL_SPOTS[room]):
        if (room,i) not in crystals:
            bob=math.sin(frame*.095+i)*3
            pts=[(cx,cy-10+bob),(cx+8,cy+bob),(cx,cy+10+bob),(cx-8,cy+bob)]
            pygame.draw.polygon(screen,(37,105,131),[(x+2,y+3) for x,y in pts])
            pygame.draw.polygon(screen,CYAN,pts)
            pygame.draw.line(screen,WHITE,(cx,cy-7+bob),(cx+3,cy+bob),2)
    if room in RESTRICTED and room not in legendary:
        name,reward,(gx,gy)=RESTRICTED[room]
        box(gx-24,gy-22,48,43,(29,47,73),5)
        for k in range(4):
            pygame.draw.line(screen,CYAN if frame//8%2 else PURPLE,
                (gx-20+k*13,gy-19),(gx-20+k*13,gy+17),3)
        draw_text('DANGER',gx-22,gy+25,GOLD,S)
        if distance(gx,gy)<80:
            draw_text('E: '+name[:22],max(30,gx-120),gy-43,WHITE,S)
    if 3 in legendary:
        for i,(sx,sy,kind,clue) in enumerate(SECRETS[room]):
            if (room,i) not in secret_found and distance(sx,sy)<145:
                pygame.draw.circle(screen,CYAN,(sx,sy),15+int(3*math.sin(frame*.12)),1)
    # Artifacts now live in concealed chambers, not in plain sight.
    if room<4:
        color=GREEN if ready_exit() else (85,66,100)
        box(585,255,25,48,color,4); draw_text('>',592,269,WHITE)
    if room>0:
        box(29,255,25,48,CYAN,4); draw_text('<',34,269,BG)
    # Subtle masonry: secret tiles use the same base shade as their neighbors.
    # A tiny one-pixel seam is the only visual hint. Nothing glows or has a marker.
    for i,(x,y,kind,clue) in enumerate(SECRETS[room]):
        if (room,i) not in secret_found:
            base=(78,75,119) if y<170 else (78,75,119)
            box(x-12,y-8,24,9,base)
            if i==0:
                pygame.draw.line(screen,(93,87,127),(x-4,y-6),(x+1,y-4),1)
            else:
                pygame.draw.line(screen,(91,84,125),(x+3,y-5),(x+6,y-2),1)
        else:
            box(x-13,y-9,26,13,(30,32,49))
            pygame.draw.rect(screen,(96,88,131),(x-13,y-9,26,13),1)
    for p in pickups:
        heart(int(p[0]),int(p[1]),True)
    for e in bugs:
        x,y=int(e['x']),int(e['y']); c=PINK if e['kind']=='hunter' else PURPLE if e['kind']=='patrol' else CYAN if e['kind']=='shooter' else RED if e['kind']=='charger' else GOLD
        pygame.draw.ellipse(screen,(24,25,45),(x-13,y+5,26,8))
        pygame.draw.polygon(screen,WHITE if e.get('flash',0)>0 and frame%4<3 else c,
          [(x-15,y-4),(x-10,y-14),(x,y-19),(x+11,y-14),(x+16,y-4),(x+9,y+11),(x,y+16),(x-10,y+11)])
        for a in range(4):
            theta=frame*.07+a*math.pi/2+e['phase']
            pygame.draw.line(screen,c,(x,y),(int(x+math.cos(theta)*21),int(y+math.sin(theta)*21)),2)
        pygame.draw.circle(screen,BG,(x,y),5);pygame.draw.circle(screen,GOLD,(x,y),3)
        if e['kind']=='shooter':
            pygame.draw.line(screen,CYAN,(x,y-14),(x,y-27),3)
            pygame.draw.circle(screen,WHITE,(x,y-29),4)
        elif e['kind']=='charger':
            pygame.draw.polygon(screen,RED,[(x-20,y-17),(x-12,y-7),(x-28,y-5)])
            pygame.draw.polygon(screen,RED,[(x+20,y-17),(x+12,y-7),(x+28,y-5)])
        elif e['kind']=='hunter':
            pygame.draw.line(screen,PINK,(x-10,y+8),(x-20,y+20),3)
            pygame.draw.line(screen,PINK,(x+10,y+8),(x+20,y+20),3)
        pygame.draw.circle(screen,WHITE,(x-4,y-2),3); pygame.draw.circle(screen,WHITE,(x+5,y-2),3)
        pygame.draw.circle(screen,BG,(x-4,y-2),1); pygame.draw.circle(screen,BG,(x+5,y-2),1)
        for dx in (-12,12): pygame.draw.line(screen,c,(x+dx,y+2),(x+dx*1.3,y+8),2)
        if e['kind']=='shooter':
            pygame.draw.circle(screen,WHITE,(x,y-2),4,1)
        if e['kind']=='charger' and e['tell']:
            pygame.draw.circle(screen,GOLD,(x,y),17,2)
        if e['kind']=='patrol': box(x-8,y-12,16,4,PURPLE)
        if e['hp']<e.get('max_hp',e['hp']):
            box(x-13,y-20,26,4,(75,46,68),1)
            box(x-13,y-20,26*max(0,e['hp'])/e['max_hp'],4,GREEN,1)
    for fx in hit_fx:
        x,y,life,damage_num=fx
        for k in range(6):
            a=k*math.pi/3+frame*.08; d=(15-life)*2
            pygame.draw.circle(screen,CYAN if k%2 else PINK,(int(x+math.cos(a)*d),int(y+math.sin(a)*d)),3)
        draw_text('-'+str(damage_num),x-8,y-25-(15-life),GOLD,F)
    for sh in shots:
        pygame.draw.circle(screen,GOLD if sh[4]=='arrow' else RED,(int(sh[0]),int(sh[1])),5)
    if boss:
        x,y=int(boss['x']),int(boss['y'])
        c=RED if boss_open else PURPLE
        pygame.draw.ellipse(screen,(16,15,35),(x-26,y+16,52,15))
        pygame.draw.polygon(screen,c,[(x-35,y-16),(x-22,y-35),(x,y-26),(x+22,y-35),(x+35,y-16),(x+28,y+25),(x,y+37),(x-28,y+25)])
        pygame.draw.circle(screen,(35,32,64),(x,y),16)
        pygame.draw.circle(screen,GOLD,(x,y),8)
        for a in range(6):
            angle=frame*.035+a*math.tau/6
            pygame.draw.circle(screen,CYAN,(int(x+math.cos(angle)*43),int(y+math.sin(angle)*43)),5)
        for dx in (-19,19): box(x+dx-5,y-27,10,15,c,3)
        pygame.draw.circle(screen,GOLD,(x-10,y-2),5); pygame.draw.circle(screen,GOLD,(x+10,y-2),5)
        if not boss_open: pygame.draw.ellipse(screen,CYAN,(x-30,y-26,60,57),2)
        box(235,83,170,7,(65,50,76),3)
        box(235,83,170*boss_hp/5,7,RED,3)
    human()
    if overdrive_time:
        pygame.draw.circle(screen,[CYAN,GOLD,PINK,GREEN,PURPLE][frame//4%5],player.center,22+frame%5,3)
        for i in range(5):
            a=frame*.15+i*math.tau/5
            pygame.draw.circle(screen,GOLD,(int(player.centerx+math.cos(a)*28),int(player.centery+math.sin(a)*28)),3)
    draw_game_hud()
    draw_game_footer()


def secret_chest_pos():
    return [(160,160),(470,170),(320,140),(165,250),(470,250)][secret_origin] if secret_index==0 else [(470,165),(170,240),(470,250),(325,140),(160,155)][secret_origin]
def secret_guard_positions():
    layouts=[[(270,165,'hunter'),(420,260,'shooter'),(450,120,'charger'),(300,270,'patrol')],
             [(175,210,'shooter'),(315,145,'hunter'),(480,270,'charger'),(390,245,'patrol')],
             [(210,245,'charger'),(450,165,'shooter'),(350,255,'hunter'),(150,145,'patrol')],
             [(470,220,'charger'),(300,140,'shooter'),(230,260,'hunter'),(510,120,'patrol')],
             [(210,150,'hunter'),(470,160,'shooter'),(380,260,'charger'),(155,270,'patrol')]]
    return layouts[secret_origin][::-1] if secret_index else layouts[secret_origin]

def draw_chamber():
    screen.fill(BG)
    box(26,61,588,270,(24,31,50),7)
    for x in range(35,608,27):
        for y in range(72,319,27):
            pygame.draw.rect(screen,(42,54,76),(x,y,25,25),1)
    for x in range(30,612,27):
        box(x,65,24,11,(81,79,112)); box(x,318,24,11,(81,79,112))
    for y in range(77,319,25):
        box(27,y,10,23,(81,79,112)); box(603,y,10,23,(81,79,112))
    # Secret chambers vary by origin, rather than repeating the same room.
    tone=[(52,88,116),(108,58,98),(44,108,96),(116,83,46),(75,61,124)][secret_origin]
    for i in range(7):
        x=65+i*75;y=100+int(15*math.sin(i+secret_index))
        pygame.draw.polygon(screen,tone,[(x,y-15),(x+20,y),(x,y+15),(x-20,y)],2)
    # A distinct room, with shelves, machinery, and a sealed chest.
    for i in range(3):
        px=180+i*135;py=110+((i+secret_origin)%2)*120
        pygame.draw.circle(screen,[(51,159,192),(169,88,171),(125,174,75),(208,133,74),(138,106,205)][secret_origin],(px,py),10,2)
    for x in (105,490):
        box(x,122,42,82,(43,54,78),5)
        box(x+5,129,32,10,(66,107,125)); box(x+5,148,32,10,(66,107,125))
        box(x+5,167,32,10,(66,107,125))
    cx,cy=secret_chest_pos()
    box(cx-20,cy-17,40,32,(103,65,43),4)
    box(cx-20,cy-17,40,10,(202,143,62),3)
    box(cx-2,cy-11,5,11,GOLD)
    if not secret_chest_open:
        draw_text('BOSS SEALED' if secret_bugs else 'E: CODE VAULT',cx-31,cy-37,GOLD,S)
    else: draw_text('EMPTY',cx-20,cy-37,GREEN,S)
    box(290,291,60,27,(46,122,105),4)
    draw_text('EXIT',305,297,WHITE,S)
    for e in secret_bugs:
        x,y=int(e['x']),int(e['y'])
        c=SECRET_BOSS_COLORS[e['phase']] if e['kind']=='secret_boss' else CYAN if e['kind']=='shooter' else PURPLE if e['kind']=='patrol' else GOLD
        if e['kind']=='secret_boss':
            rr=21+int(3*math.sin(frame*.13));pygame.draw.circle(screen,c,(x,y),rr,3)
            for a in range(6):
                ang=frame*.025+a*math.tau/6;pygame.draw.circle(screen,c,(int(x+math.cos(ang)*29),int(y+math.sin(ang)*29)),4)
            pygame.draw.rect(screen,(80,32,55),(x-35,y-39,70,6))
            pygame.draw.rect(screen,c,(x-35,y-39,int(70*max(0,e['hp'])/e['max_hp']),6))
            draw_text(e['name'],x-46,y-55,c,S)
            continue
        pygame.draw.ellipse(screen,c,(x-12,y-9,24,20))
        pygame.draw.circle(screen,WHITE,(x-4,y-2),3)
        pygame.draw.circle(screen,WHITE,(x+5,y-2),3)
    for fx in hit_fx:
        x,y,life,damage_num=fx
        for k in range(6):
            a=k*math.pi/3+frame*.08; d=(15-life)*2
            pygame.draw.circle(screen,CYAN if k%2 else PINK,(int(x+math.cos(a)*d),int(y+math.sin(a)*d)),3)
        draw_text('-'+str(damage_num),x-8,y-25-(15-life),GOLD,F)
    for sh in shots:
        pygame.draw.circle(screen,RED if sh[4]=='enemy' else GOLD,(int(sh[0]),int(sh[1])),5)
    if secret_origin==2 and secret_index==0:
        draw_mentor('ECHO',450,253,MENTORS['ECHO']['color'])
    human()
    if overdrive_time:
        pygame.draw.circle(screen,[CYAN,GOLD,PINK,GREEN,PURPLE][frame//4%5],player.center,22+frame%5,3)
        for i in range(5):
            a=frame*.15+i*math.tau/5
            pygame.draw.circle(screen,GOLD,(int(player.centerx+math.cos(a)*28),int(player.centery+math.sin(a)*28)),3)
    draw_game_hud(chamber=True)
    draw_game_footer(chamber=True)


def update_chamber():
    global hp
    for e in secret_bugs[:]:
        if e.get('flash',0): e['flash']-=1
        if e.get('hurt',0): e['hurt']-=1; continue
        e['timer']-=1
        if e['timer']<=0:
            e['turn']=random.uniform(-math.pi,math.pi)
            e['timer']=random.randrange(55,120)
        if e['kind']=='secret_boss':
            phase=e['phase'];theta=frame*.02*(1+phase*.07)
            dx=player.centerx-e['x'];dy=player.centery-e['y'];mag=max(1,math.hypot(dx,dy))
            e['x']+=(dx/mag)*(.6+phase*.06)+math.cos(theta)*(.5+phase*.05)
            e['y']+=(dy/mag)*(.5+phase*.05)+math.sin(theta*1.3)*.6
            e['shot']-=1
            if e['shot']<=0:
                for z in range(2+phase%3):
                    a=math.atan2(dy,dx)+(z-(1+phase%3)/2)*.25
                    shots.append([e['x'],e['y'],math.cos(a)*2.4,math.sin(a)*2.4,'enemy'])
                e['shot']=max(38,105-phase*6)
        elif e['kind']=='patrol':
            e['x']+=e['vx']*1.35
            if e['x']<170 or e['x']>470: e['vx']*=-1
        elif e['kind']=='shooter':
            e['shot']-=1
            if e['shot']<=0:
                dx=player.centerx-e['x'];dy=player.centery-e['y']; mag=max(1,math.hypot(dx,dy))
                shots.append([e['x'],e['y'],dx/mag*2.4,dy/mag*2.4,'enemy'])
                e['shot']=120
        else:
            e['x']+=math.cos(e['turn'])*1.2; e['y']+=math.sin(e['turn'])*1.2
        e['x']=max(60,min(575,e['x']));e['y']=max(115,min(280,e['y']))
        if player.collidepoint(e['x'],e['y']): damage()
    for sh in shots[:]:
        sh[0]+=sh[2];sh[1]+=sh[3]
        if not AREA.collidepoint(sh[0],sh[1]): shots.remove(sh);continue
        if sh[4]=='enemy':
            if player.collidepoint(sh[0],sh[1]): damage(); shots.remove(sh)
        else:
            for e in secret_bugs[:]:
                if math.hypot(sh[0]-e['x'],sh[1]-e['y'])<17:
                    hit_bug(e,1,True);shots.remove(sh);play_sfx('defeat')
                    break

def modal(title,subtitle):
    # A separate screen: do not draw the adventure HUD or its instructions behind menus.
    screen.fill(BG)
    box(0,0,640,53,(14,17,34))
    draw_text('GLITCH BUSTERS  /  '+hero_name(),22,17,CYAN,F)
    box(30,75,580,265,(13,19,37),9)
    pygame.draw.rect(screen,CYAN,(30,75,580,265),2,9)
    draw_text(title,48,92,GOLD,F)
    draw_text(subtitle,48,119,GRAY,S)

def code_normalize(value):
    try:
        return ast.dump(ast.parse(value.strip()),include_attributes=False)
    except (SyntaxError,IndentationError,ValueError):return None

def code_key(event):
    global code_input,code_cursor
    if event.key==pygame.K_BACKSPACE:
        if code_cursor>0:
            code_input=code_input[:code_cursor-1]+code_input[code_cursor:];code_cursor-=1
    elif event.key==pygame.K_DELETE:
        code_input=code_input[:code_cursor]+code_input[code_cursor+1:]
    elif event.key==pygame.K_LEFT:code_cursor=max(0,code_cursor-1)
    elif event.key==pygame.K_RIGHT:code_cursor=min(len(code_input),code_cursor+1)
    elif event.key==pygame.K_HOME:code_cursor=code_input.rfind('\n',0,code_cursor)+1
    elif event.key==pygame.K_END:
        end=code_input.find('\n',code_cursor);code_cursor=len(code_input) if end<0 else end
    elif event.key==pygame.K_RETURN:
        code_input=code_input[:code_cursor]+'\n'+code_input[code_cursor:];code_cursor+=1
    elif event.key==pygame.K_TAB:
        code_input=code_input[:code_cursor]+'    '+code_input[code_cursor:];code_cursor+=4
    elif event.unicode and event.unicode.isprintable() and len(code_input)<360:
        code_input=code_input[:code_cursor]+event.unicode+code_input[code_cursor:];code_cursor+=len(event.unicode)

def question_screen():
    name,desc,broken,*_=Q[active]
    modal('WRITE THE FIX // '+name,'Replace the broken code below. Write every line, including indentation.')
    for i,line in enumerate(wrap_lines(desc,75)):draw_text(line,48,125+i*15,WHITE,S)
    box(47,158,546,62,(34,36,58),5)
    for i,line in enumerate(broken[:3]):draw_text(line,58,162+i*17,PINK,S)
    box(47,228,546,106,(21,35,49),5)
    # Scroll vertically to keep the last lines visible.
    lines=code_input.split('\n');visible=lines[-5:]
    for i,line in enumerate(visible):draw_text(line[:75],59,235+i*18,GREEN,S)
    before=code_input[:code_cursor]; cursor_line=before.count('\n');cursor_col=len(before.rsplit('\n',1)[-1])
    offset=max(0,len(lines)-5)
    if offset<=cursor_line<offset+5 and frame%40<25:
        # Character cell is approximate for the built-in proportional font.
        prefix=lines[cursor_line][:cursor_col]
        cx=59+S.size(prefix)[0];cy=235+(cursor_line-offset)*18
        pygame.draw.line(screen,GOLD,(cx,cy),(cx,cy+14),2)
    draw_text('TYPE FULL CODE | TAB: 4 SPACES | ENTER: NEW LINE | CTRL+ENTER: TEST',49,346,GOLD,S)
    if code_feedback:draw_text(code_feedback[:80],49,366,PINK,S)

def lesson_screen():
    name,desc,broken,opts,ans,why,correct,explanation=Q[active]
    modal('DEBUG ASSISTANT // LEARN FROM THE GLITCH','This terminal is locked until you complete another task.')
    y=143
    for line in wrap_lines(explanation,67)[:4]:
        draw_text(line,51,y,WHITE,S);y+=19
    draw_text('WORKING REPAIR:',51,y+5,CYAN,S)
    for i,line in enumerate(correct.split('\n')):
        draw_text(line,59,y+28+i*20,GREEN,F)
    draw_text('WHY IT MATTERS: READ THE KEY, DIRECTION AND INDENTATION.',49,299,GOLD,S)
    draw_text('ENTER: RETURN TO ARCADE. COME BACK AFTER ANOTHER REPAIR.',49,321,GOLD,S)

def report_code():
    return ('GB6|R'+str(stats['runs'])+'|G'+str(stats['gameovers'])+'|D'+str(stats['damage'])+
        '|K'+str(stats['kills'])+'|W'+str(stats['wrong'])+'|Q'+'.'.join(map(str,stats['attempts']))+
        '|A'+''.join(str(i) for i in sorted(artifacts))+'|S'+''.join(str(i) for i in sorted(stats['rooms']))+
        '|V'+str(stats['victories'])+'|T'+str(int(stats['seconds']))+'|H'+str(stats['secrets'])+'|C'+str(stats['chests'])+'|DS'+str(stats['dashes'])+'|NPC'+str(stats['talks'])+'|J'+str(stats['lessons'])+'|P'+''.join(str(i) for i in sorted(puzzle_done))+'|PA'+'.'.join(map(str,puzzle_attempts))+'|ML'+''.join(str(sum((name,i) in mentor_checks_done for i in range(3))) for name in MAIN_MENTORS)+'|MA'+'.'.join(str(v) for name in MAIN_MENTORS for v in mentor_check_attempts[name])+'|NAME:'+hero_name().replace('|','').replace(' ','_')[:18]+'|EXP:'+player_experience.replace(' ','_')[:20]+
        '|PC'+str(crystal_total)+'|OD'+str(overdrive_earned)+'.'+str(overdrive_uses)+
        '|LG'+''.join(str(i) for i in sorted(legendary))+'|EVO'+str(evolution_form()+1) )

def copy_report():
    global copy_msg
    code=report_code()
    try:
        import js
        # Use the browser's native selectable text dialog as a reliable manual fallback.
        el=js.document.createElement('textarea'); el.value=code
        el.style.position='fixed'; el.style.top='0'; el.style.left='0'
        js.document.body.appendChild(el); el.focus(); el.select()
        ok=bool(js.document.execCommand('copy'))
        js.document.body.removeChild(el)
        if ok: copy_msg='COPIED! PASTE INTO THE GOOGLE FORM.'; return
        js.window.prompt('SELECT ALL (CTRL+A), COPY (CTRL+C), THEN PASTE INTO THE FORM:',code)
        copy_msg='USE CTRL+C IN THE POPUP, THEN CTRL+V IN THE FORM.'
    except Exception:
        copy_msg='BROWSER BLOCKED COPY. READ THE CODE BELOW.'

def report_screen():
    # Compact, fixed columns: the mission code is copied, not drawn over the stats.
    modal('MISSION INTELLIGENCE // LEVEL 6','Progress is information, not a penalty for mistakes.')
    box(43,137,554,120,(23,30,49),5)
    draw_text('RUNS '+str(stats['runs'])+'   GAME OVERS '+str(stats['gameovers'])+'   DAMAGE '+str(stats['damage']),53,145,WHITE,S)
    draw_text('BUGS '+str(stats['kills'])+'   ROOMS '+str(len(stats['rooms']))+'/5   ARTIFACTS '+str(len(artifacts))+'/3',53,165,WHITE,S)
    draw_text('SECRETS '+str(stats['secrets'])+'   WRONG '+str(stats['wrong'])+'   PUZZLES '+str(len(puzzle_done))+'/5',53,185,WHITE,S)
    draw_text('TIME '+str(int(stats['seconds']//60))+'m '+str(int(stats['seconds']%60))+'s   NPC '+str(stats['talks'])+'   WINS '+str(stats['victories']),53,205,WHITE,S)
    draw_text('LESSONS '+str(len(mentor_checks_done))+'/15   CRYSTALS '+str(crystal_total)+'   OVERDRIVE '+str(overdrive_uses),53,225,CYAN,S)
    draw_text('MISSION CODE FOR '+hero_name().upper()[:16],49,264,GOLD,S)
    draw_text('Use COPY CODE to submit your complete mission record.',49,285,GRAY,S)
    box(439,296,151,32,(39,107,102),5)
    draw_text('COPY CODE',462,303,WHITE,F)
    if copy_msg: draw_text(copy_msg[:43],49,309,GOLD,S)
    draw_text('R / BACKSPACE: RETURN',49,324,GRAY,S)

def distance(x,y): return math.hypot(player.centerx-x,player.centery-y)
def inspect_secret(mx=None,my=None):
    global potions,arrows,bombs,hp,speed_upgrade,sword_upgrade,secret_room,secret_origin,secret_index,secret_bugs,secret_chest_open
    for i,(x,y,kind,clue) in enumerate(SECRETS[room]):
        if (room,i) in secret_found: continue
        close=distance(x,y)<64
        clicked=mx is not None and math.hypot(mx-x,my-y)<22
        if not close or (mx is not None and not clicked): continue
        secret_found.add((room,i)); stats['secrets']+=1; play_sfx('unlock')
        secret_origin=room; secret_index=i; secret_room=True; secret_chest_open=False; shots.clear()
        secret_bugs=[bug(x,y,k) for x,y,k in secret_guard_positions()]
        boss_n=room*2+i
        elite=bug(310,165,'hunter');elite.update({'kind':'secret_boss','hp':12+boss_n*2,'max_hp':12+boss_n*2,'name':SECRET_BOSS_NAMES[boss_n],'shot':40,'phase':boss_n,'speed':1.0+boss_n*.08})
        secret_bugs.append(elite)
        player.topleft=(304,283)
        tell('SECRET BOSS DETECTED! DEFEAT IT, CODE THE VAULT, CLAIM THE PRIZE.',230)
        return True
    return False

SECRET_CODE_TASKS = [('Set vault to True.', 'vault = True', 'True unlocks the vault.'), ('Increase arrows by 6.', 'arrows = arrows + 6', 'Add ammunition.'), ('When key equals 9, set open to True.', 'if key == 9:\n    open = True', 'Equality uses ==.'), ('When hp is below 3, add 2 to hp.', 'if hp < 3:\n    hp = hp + 2', 'Heal when low.'), ('When LEFT is held, subtract 4 from x.', 'if keyboard.left:\n    x = x - 4', 'Left decreases x.'), ('When DOWN is held, add 3 to y.', 'if keyboard.down:\n    y = y + 3', 'Down increases y.'), ('Loop twice and add 4 to bombs.', 'for i in range(2):\n    bombs = bombs + 4', 'Two loops add eight bombs.'), ('Loop three times and add 1 to keys.', 'for i in range(3):\n    keys = keys + 1', 'Three repetitions.'), ('Write unlock() to return True.', 'def unlock():\n    return True', 'Return the boolean.'), ('Write refill(n) to return n + 5.', 'def refill(n):\n    return n + 5', 'Return increased energy.')]
SECRET_BOSS_NAMES=['ASTRAL SENTINEL', 'ECLIPSE BEHEMOTH', 'PAPER PHANTOM', 'THE INDEX EATER', 'SILVER DOPPELGANGER', 'GLASS WIDOW', 'THUNDER WYRM', 'TEMPEST KNIGHT', 'THE NULL ARCHON', 'OBLIVION CORE']
SECRET_BOSS_COLORS=[(83,233,249),(243,180,63),(66,133,230),(52,210,189),(130,236,96),(206,119,244),(240,172,75),(247,102,165),(178,120,250),(255,77,104)]
secret_boss_defeated=set();secret_code_locks={}
def secret_lock_screen():
    prompt,expected,why=SECRET_CODE_TASKS[secret_origin*2+secret_index]
    code_task_screen('HIDDEN VAULT // PYTHON SEAL',prompt)
def secret_lock_submit():
    global state,repair_successes
    n=secret_origin*2+secret_index;prompt,expected,why=SECRET_CODE_TASKS[n]
    if code_normalize(code_input)==code_normalize(expected):
        secret_lock_solved.add((secret_origin,secret_index));repair_successes+=1
        state='world';tell('VAULT CODE ACCEPTED! OPEN THE CHEST.',170);play_sfx('unlock')
    else:
        stats['wrong']+=1;secret_code_locks[n]=repair_successes
        global check_feedback
        check_feedback='DEBUG NOTE: '+why+' WORKING CODE: '+expected.replace('\n',' / ')
        state='secret_code_retry'
def secret_code_retry_screen():
    modal('VAULT SECURITY // DEBUG REPORT','INCORRECT CODE. REVISIT AFTER ANOTHER SUCCESS.')
    for i,line in enumerate(wrap_lines(check_feedback,66)[:6]):draw_text(line,49,155+i*23,WHITE,S)
    draw_text('ENTER: RETURN TO SECRET CHAMBER',49,327,GOLD,S)

def interact():
    global active,selected,state,code_input,code_cursor,code_feedback,weapon,has_bow,arrows,bombs,potions,max_hp,hp,secret_room,secret_chest_open,room,speed_upgrade,sword_upgrade
    if secret_room:
        if secret_origin==2 and secret_index==0 and distance(450,253)<49:
            talk_to('ECHO'); return
        if distance(*secret_chest_pos())<52 and not secret_chest_open:
            if secret_bugs:
                tell('CHEST SEALED! DEFEAT THE SECRET BOSS AND ITS GUARDS.',140); return
            if (secret_origin,secret_index) not in secret_lock_solved:
                global secret_lock_selected
                secret_lock_selected=0
                if secret_code_locks.get(secret_origin*2+secret_index,-1)>=repair_successes:
                    tell('VAULT REQUIRES ANOTHER SUCCESSFUL CODE TASK FIRST.',180);return
                reset_code_editor();state='secret_lock';return
            secret_chest_open=True; play_sfx('treasure'); chamber_cleared.add((secret_origin,secret_index))
            grant_crystal('HIDDEN CHAMBER')
            n=secret_origin
            if secret_index==0 and n in ARTIFACTS and n not in artifacts:
                artifacts.add(n); tell('HIDDEN ARTIFACT FOUND: '+ARTIFACTS[n][2],220)
            elif n==1 and secret_index==0:
                potions+=2; tell('HIDDEN TREASURE: TWO HEALTH POTIONS!',220)
            elif n==4 and secret_index==0:
                hp=max_hp; tell('HIDDEN TREASURE: FULL HEALTH RESTORED!',220)
            elif n==0:
                speed_upgrade=True; tell('SECRET SPEED MODULE! MOVE FASTER!',220)
            elif n==2:
                sword_upgrade=True; tell('SECRET BLADE UPGRADE! STRONGER ATTACKS!',220)
            elif n==3:
                bombs+=7; tell('SECRET CACHE: THREE GLITCH BOMBS!',220)
            else:
                arrows+=15; tell('SECRET CACHE: FIFTEEN ARROWS!',220)
            return
        if distance(319,301)<48:
            secret_room=False; room=secret_origin; player.topleft=(100,115)
            tell('RETURNED TO '+ROOMS[room],150); return
        tell('DEFEAT THE UNIQUE SECRET BOSS, CODE THE VAULT, THEN EXIT.',140); return
    if room in RESTRICTED and room not in legendary:
        title,reward,(gx,gy)=RESTRICTED[room]
        if distance(gx,gy)<65:
            start_gauntlet(room)
            return
    if room not in puzzle_done and distance(*PUZZLE_POS[room])<74:
        if puzzle_retry_locks.get(room,-1)>=repair_successes:
            tell('INPUT LAB LOCKED: COMPLETE A DIFFERENT REPAIR FIRST.',180);return
        begin_puzzle(); return
    for name,data in MENTORS.items():
        if data['room']==room and distance(*data['pos'])<47:
            talk_to(name); return
    if inspect_secret(): return
    for x,y,q in STATIONS[room]:
        if q not in solved and distance(x,y)<44:
            if repair_locks.get(q,-1)>=repair_successes:
                tell('TERMINAL LOCKED: COMPLETE ANOTHER REPAIR OR LESSON FIRST.',170);return
            active=q; selected=0; code_input='';code_cursor=0;code_feedback='';state='quiz'; return
    for x,y,name,clue in NPCS[room]:
        if distance(x,y)<48:
            if room not in npc_gifts:
                npc_gifts.add(room)
                if room==0: potions+=1; arrows+=8; bombs+=2; tell(name+': '+clue+' TAKE THIS POTION. LOOK FOR ODD WALL TILES.',280)
                elif room==1: potions+=1; bombs+=3; tell(name+': '+clue+' HERE IS A POTION.',260)
                elif room==2: arrows+=12; tell(name+': '+clue+' TAKE FIVE ARROWS.',260)
                elif room==3: bombs+=5; tell(name+': '+clue+' TAKE TWO BOMBS.',260)
                else: potions+=2; arrows+=10; bombs+=4; tell(name+': '+clue+' TAKE A POTION.',260)
            else: tell(name+': '+clue+' LOOK FOR CRACKS AND ODD CABINETS.',260)
            return
    x,y,item=CHESTS[room]
    if room not in chests and distance(x,y)<47:
        if item=='armor' and len(artifacts)<3:
            tell('VAULT CHEST NEEDS ALL 3 ARTIFACTS!',160); return
        chests.add(room); stats['chests']+=1; play_sfx('treasure')
        if item=='sword': weapon='PIXEL SWORD'; tell('FOUND THE PIXEL SWORD! Z NOW DEALS MORE DAMAGE.',210)
        if item=='potion': potions+=2; tell('FOUND 2 HEALTH POTIONS! PRESS H TO USE.',210)
        if item=='bow': has_bow=True; arrows+=14; tell('DEBUG BOW UNLOCKED! PRESS C TO SHOOT.',210)
        if item=='bombs': bombs+=7; tell('GLITCH BOMBS UNLOCKED! PRESS B TO BLAST.',210)
        if item=='armor': max_hp=7; hp=7; tell('LEGENDARY ARMOR! MAX HEALTH INCREASED TO 7.',210)
        return

    tell('SEARCH FOR STATIONS, CHESTS, ARTIFACTS, OR NPCS.',100)

def submit_answer():
    global state,boss_open,boss_hacks,boss_quiz,code_feedback,repair_successes
    stats['attempts'][active]+=1
    expected=Q[active][6]
    if code_normalize(code_input)==code_normalize(expected):
        repair_successes+=1
        state='world';code_feedback=''
        if boss_quiz:
            boss_quiz=False;boss_open=540;boss_hacks+=1
            tell('SHIELD DOWN! MOVE CLOSE AND PRESS Z TO STRIKE!',240);play_sfx('unlock')
        else:
            solved.add(active);hp_restore();play_sfx('repair')
            tell('PYTHON REPAIR ACCEPTED! +1 HEART. '+Q[active][0],160)
    else:
        stats['wrong']+=1;state='lesson';repair_locks[active]=repair_successes if not boss_quiz else -1;code_feedback='Review the explanation, then complete another task before retrying.'

def hp_restore():
    global hp
    hp=min(max_hp,hp+1)

SFX_NAMES=('swing','hit','hurt','defeat','pickup','crystal','treasure','heal','repair','unlock','overdrive','bomb','victory')
sfx_bank={}
sfx_channels=[]
def play_sfx(name):
    if not music_enabled: return
    try:
        if not pygame.mixer.get_init(): return
        if name not in sfx_bank:
            sfx_bank[name]=pygame.mixer.Sound('sfx_'+name+'.ogg')
            sfx_bank[name].set_volume(.45)
        sfx_bank[name].play()
    except Exception:
        pass  # Never interrupt a lesson or gameplay for an audio failure.

def damage():
    global hp,lives,invuln,state
    if invuln or overdrive_time or state!='world': return
    hp-=1; stats['damage']+=1; invuln=80; play_sfx('hurt')
    if hp<=0:
        lives-=1; stats['lives']+=1
        if lives<=0:
            stats['gameovers']+=1; state='gameover'
        else:
            hp=max_hp; player.topleft=(65,283); invuln=130
            tell('LIFE LOST! '+str(lives)+' REMAINING.',140)

def hit_bug(e,amount,secret=False):
    e['hp']-=amount*(2 if 2 in legendary and weapon!='PUNCH' else 1); e['flash']=12; e['hurt']=12; play_sfx('hit')
    e['x']=max(55,min(582,e['x']+facing[0]*15))
    e['y']=max(107,min(300,e['y']+facing[1]*15))
    hit_fx.append([e['x'],e['y'],15,amount])
    if e['hp']<=0:
        play_sfx('defeat')
        if secret:
            if e in secret_bugs: secret_bugs.remove(e); stats['kills']+=1
            if e.get('kind')=='secret_boss':
                secret_boss_defeated.add((secret_origin,secret_index));grant_crystal('SECRET BOSS');arrows_bonus=5
                journal_add('DEFEATED '+e['name']);tell(e['name']+' DEFEATED! SECRET VAULT UNSEALED.',180)
        elif e in bugs: kill_bug(e)

def attack():
    global attack_time,attack_cd,boss_hp,boss,boss_open
    if attack_cd: return
    attack_cd=23 if weapon=='PUNCH' else 17; attack_time=11; play_sfx('swing')
    fx,fy=facing; reach=23 if weapon=='PUNCH' else 40
    target=pygame.Rect(player.centerx+fx*reach-17,player.centery+fy*reach-17,34,34)
    for e in (secret_bugs if secret_room else bugs)[:]:
        if target.collidepoint(e['x'],e['y']):
            hit_bug(e,1 if weapon=='PUNCH' else 3 if sword_upgrade else 2,secret_room)
    if not secret_room and boss and boss_open and math.hypot(target.centerx-boss['x'],target.centery-boss['y'])<53:
        boss_hp-=1; boss_open=0; boss_hacks_room[room]+=1; play_sfx('hit')
        hit_fx.append([boss['x'],boss['y'],15,1])
        tell('DIRECT HIT! GUARDIAN HAS '+str(boss_hp)+' HP LEFT.',100)
        if boss_hp<=0: defeat_boss()

def kill_bug(e):
    bugs.remove(e); stats['kills']+=1
    if random.random()<.22: pickups.append([e['x'],e['y'],360])

def defeat_boss():
    play_sfx('victory')
    global boss
    boss=None; rooms_done.add(room)
    tell('GUARDIAN DEFEATED! EXIT TO THE EAST IS OPEN!',230)

def shoot_bow():
    global arrows
    if not has_bow or arrows<=0: tell('FIND THE DEBUG BOW OR MORE ARROWS.',100); return
    arrows-=1; fx,fy=facing
    shots.append([float(player.centerx),float(player.centery),fx*5.5,fy*5.5,'arrow'])

def use_bomb():
    global bombs,boss_hp
    if bombs<=0: tell('NO BOMBS! FIND THEM IN THE FACTORY.',110); return
    bombs-=1; play_sfx('bomb'); x,y=player.center
    pygame.draw.circle(screen,GOLD,(x,y),55,4)
    for e in (secret_bugs if secret_room else bugs)[:]:
        if math.hypot(x-e['x'],y-e['y'])<82:
            if secret_room: hit_bug(e,4,True)
            else: kill_bug(e)
    if not secret_room and boss and distance(boss['x'],boss['y'])<82 and boss_open:
        boss_hp-=1; boss_open=0; boss_hacks_room[room]+=1
        if boss_hp<=0: defeat_boss()
    tell('GLITCH BOMB DETONATED!',85)

def ready_exit():
    return all((MAIN_MENTORS[room],i) in mentor_checks_done for i in range(3)) and room in puzzle_done and all(q in solved for x,y,q in STATIONS[room]) and room in rooms_done and boss is None and not bugs

def update():
    global frame,invuln,attack_time,attack_cd,boss_open,boss_shot,spawn_cd,hp,state,boss,boss_hp,waves,dash_time,dash_cd,moving,reinforce_count,reinforce_timer
    frame+=1
    evolution_check()
    if state!='world': return
    stats['seconds']+=1/60
    global overdrive_time,gauntlet_cooldown,crystal_bank,overdrive_charges,overdrive_earned,crystal_total
    if invuln: invuln-=1
    if overdrive_time: overdrive_time-=1
    if gauntlet_cooldown: gauntlet_cooldown-=1
    if attack_time: attack_time-=1
    if attack_cd: attack_cd-=1
    if dash_cd: dash_cd-=1
    if dash_time: dash_time-=1
    msg_timer_update()
    keys=pygame.key.get_pressed(); dx=int(keys[pygame.K_RIGHT] or keys[pygame.K_d])-int(keys[pygame.K_LEFT] or keys[pygame.K_a]); dy=int(keys[pygame.K_DOWN] or keys[pygame.K_s])-int(keys[pygame.K_UP] or keys[pygame.K_w])
    global facing
    moving=bool(dx or dy)
    if dx or dy:
        if abs(dx)>abs(dy): facing=(1 if dx>0 else -1,0)
        else: facing=(0,1 if dy>0 else -1)
        scale=(7.4 if dash_time else 4.5 if overdrive_time else 3.25 if speed_upgrade else 2.95)/math.hypot(dx,dy)
        for axis,step in [('x',dx*scale),('y',dy*scale)]:
            old=player.copy()
            if axis=='x': player.x+=round(step)
            else: player.y+=round(step)
            if not secret_room and any(player.colliderect(w) for w in WALLS[room]): player.topleft=old.topleft
        player.clamp_ip(AREA)
    # Crystals persist after collection; returning to previous rooms is worthwhile.
    if not secret_room:
        for i,(cx,cy) in enumerate(CRYSTAL_SPOTS[room]):
            if (room,i) not in crystals and distance(cx,cy)<22 and crystal_bank<5:
                crystals.add((room,i)); grant_crystal('WORLD PICKUP')
                if crystal_bank==5:
                    tell('OVERDRIVE READY! PRESS V. OTHER CRYSTALS STAY UNTIL YOU USE IT.',190)
                else: tell('POWER CRYSTAL +1  |  '+str(crystal_bank)+'/5 TO OVERDRIVE',100)
    for fx in hit_fx[:]:
        fx[2]-=1
        if fx[2]<=0: hit_fx.remove(fx)
    if secret_room:
        update_chamber(); return
    if overdrive_time:
        for e in bugs[:]:
            if distance(e['x'],e['y'])<29:
                hit_bug(e,3)

    if room<4 and player.centerx>580 and 255<player.centery<306:
        if ready_exit():
            rooms_done.add(room); enter_room(room+1)
            return
        if frame%80==0:
            if not all((MAIN_MENTORS[room],i) in mentor_checks_done for i in range(3)):
                tell('EXIT LOCKED: TALK TO '+MAIN_MENTORS[room]+' AND PASS ALL 3 LESSON CHECKS.',140)
            else: tell('EXIT LOCKED: SOLVE THE PUZZLE, REPAIRS AND GUARDIAN.',100)
    if room>0 and player.centerx<57 and 255<player.centery<306:
        enter_room(room-1); player.topleft=(557,279); return
    for e in bugs[:]:
        if e.get('flash',0): e['flash']-=1
        if e.get('hurt',0):
            e['hurt']-=1
            continue
        e['timer']-=1
        if e['timer']<=0:
            e['turn']=random.uniform(-3.14,3.14)
            e['timer']=random.randrange(65,145)
            if e['kind']=='patrol': e['vx']*=-1
        dxp=player.centerx-e['x']; dyp=player.centery-e['y']
        angle=math.atan2(dyp,dxp)
        kind=e['kind']; speed=e['speed']
        if kind=='wander':
            angle=e['turn']; speed*=.8
        elif kind=='patrol':
            angle=0 if e['vx']>0 else math.pi; speed*=1.35
        elif kind=='hunter':
            angle+=math.sin(frame*.08+e['phase'])*.45; speed*=1.25
        elif kind=='shooter':
            # Keep distance; shoot rather than clustering around the hero.
            angle=angle+math.pi if math.hypot(dxp,dyp)<150 else e['turn']
            speed*=.65
            e['shot']-=1
            if e['shot']<=0:
                mag=max(1,math.hypot(dxp,dyp))
                shots.append([e['x'],e['y'],dxp/mag*2.7,dyp/mag*2.7,'enemy'])
                e['shot']=random.randrange(max(55,110-room*8),max(80,160-room*9))
        elif kind=='charger':
            if e['tell']>0:
                e['tell']-=1; speed=0
                if e['tell']==0: e['charge']=32; e['turn']=angle
            elif e['charge']>0:
                e['charge']-=1; angle=e['turn']; speed*=3.1
            elif math.hypot(dxp,dyp)<185 and e['timer']<40:
                e['tell']=35; speed=0
            else: angle=e['turn']; speed*=.55
        vx=math.cos(angle)*speed; vy=math.sin(angle)*speed
        for other in bugs:
            if other is e: continue
            dd=math.hypot(e['x']-other['x'],e['y']-other['y'])
            if 0<dd<54:
                vx+=(e['x']-other['x'])/dd*1.25
                vy+=(e['y']-other['y'])/dd*1.25
        e['x']=max(55,min(582,e['x']+vx)); e['y']=max(107,min(300,e['y']+vy))
        if player.collidepoint(e['x'],e['y']): damage()
    for p in pickups[:]:
        p[2]-=1
        if distance(p[0],p[1])<20:
            hp_restore(); play_sfx('pickup'); pickups.remove(p)
        elif p[2]<=0: pickups.remove(p)
    for sh in shots[:]:
        sh[0]+=sh[2]; sh[1]+=sh[3]
        if not AREA.collidepoint(sh[0],sh[1]): shots.remove(sh); continue
        if sh[4]=='enemy':
            if player.collidepoint(sh[0],sh[1]): damage(); shots.remove(sh)
        else:
            hit=False
            for e in bugs[:]:
                if math.hypot(sh[0]-e['x'],sh[1]-e['y'])<16:
                    hit_bug(e,1); hit=True
                    break
            if boss and boss_open and math.hypot(sh[0]-boss['x'],sh[1]-boss['y'])<43:
                boss_hp-=1; boss_open=0; boss_hacks_room[room]+=1; hit=True; play_sfx('hit'); hit_fx.append([boss['x'],boss['y'],15,1])
                if boss_hp<=0: defeat_boss()
            if hit: shots.remove(sh)
    if boss:
        # Guardians move in two dimensions, accelerate when wounded,
        # and summon a limited number of reinforcements after the first hit.
        if boss_hp<5 and reinforce_count<(2 if boss_hp>=3 else 5):
            reinforce_timer-=1
            if reinforce_timer<=0:
                bx,by=random.choice([(110,160),(520,170),(170,275),(460,270)])
                bugs.append(bug(bx,by,['shooter','charger','hunter','patrol'][reinforce_count%4]))
                reinforce_count+=1; reinforce_timer=180 if boss_hp==1 else 280
                tell('GUARDIAN SUMMONED REINFORCEMENTS!',110)
        boss['x']=315+math.sin(frame*.038+room)*180
        boss['y']=180+math.cos(frame*.047+room)*75
        boss_shot-=1
        if boss_shot<=0:
            vx=player.centerx-boss['x']; vy=player.centery-boss['y']; mag=max(1,math.hypot(vx,vy))
            shots.append([boss['x'],boss['y'],vx/mag*2.5,vy/mag*2.5,'enemy'])
            boss_shot=70 if boss_hp>2 else 43
        if boss_open: boss_open-=1
        if distance(boss['x'],boss['y'])<37: damage()
    # Two additional finite waves per area. Guardians arrive only afterward.
    if not bugs and waves<2:
        waves+=1
        for i in range(3+room):
            bx=random.randint(125,510); by=random.randint(120,286)
            if math.hypot(bx-player.centerx,by-player.centery)<85: bx,by=500,135
            bugs.append(bug(bx,by,['wander','patrol','hunter','shooter','charger'][(i+waves+room)%5]))
        tell('GLITCH WAVE '+str(waves)+'/2! WATCH THE ENEMY PATTERNS.',140)
    if (waves>=2 and not bugs and boss is None and room not in rooms_done
        and all(q in solved for x,y,q in STATIONS[room])):
        boss={'x':315.,'y':110.,'dir':1,'timer':100,'phase':0}
        boss_hp=5
        boss_shot=90
        tell('WARNING: GUARDIAN EMERGING! GET CLOSE AND PRESS E TO HACK.',220)

def msg_timer_update():
    global msg_timer
    if msg_timer: msg_timer-=1
    return True

def try_boss_hack():
    global boss_open,boss_hacks,boss_quiz,active,selected,state,code_input,code_cursor,code_feedback
    if not boss: return False
    if distance(boss['x'],boss['y'])<165 and not boss_open:
        # One unique hack for each boss hit, no reused station questions.
        active=BOSS_Q[room][boss_hacks_room[room]%5]; selected=0
        boss_quiz=True;code_input='';code_cursor=0;code_feedback='';state='quiz'
        return True
    return False

def puzzle_note(msg):
    global puzzle_feedback,puzzle_feedback_timer
    puzzle_feedback=msg; puzzle_feedback_timer=210

PUZZLE_CODE_TASKS = [[('Set x to 10 and speed to 4, then add speed to x.', 'x = 10\nspeed = 4\nx = x + speed', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('Set charge to 3. If charge < 5, add 2; otherwise subtract 1.', 'charge = 3\nif charge < 5:\n    charge = charge + 2\nelse:\n    charge = charge - 1', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('Set stars to 0. Loop three times and add 2 to stars.', 'stars = 0\nfor i in range(3):\n    stars = stars + 2', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('Write orbit(n) that returns n + 4 if n < 10, otherwise n.', 'def orbit(n):\n    if n < 10:\n        return n + 4\n    else:\n        return n', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.')], [('Set pages to 4. If pages >= 4, add 2; otherwise set pages to 0.', 'pages = 4\nif pages >= 4:\n    pages = pages + 2\nelse:\n    pages = 0', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('Set keys to 0. Loop three times and add 1 to keys.', 'keys = 0\nfor i in range(3):\n    keys = keys + 1', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('If key is True and clearance > 2, set access True; otherwise False.', 'if key and clearance > 2:\n    access = True\nelse:\n    access = False', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('Write index(n) returning n * 2 when n > 3, otherwise n + 1.', 'def index(n):\n    if n > 3:\n        return n * 2\n    else:\n        return n + 1', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.')], [('If keyboard.left and x > 0, subtract speed from x; otherwise set blocked True.', 'if keyboard.left and x > 0:\n    x = x - speed\nelse:\n    blocked = True', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('If y < 0 set y to 0. If y > 300 set y to 300.', 'if y < 0:\n    y = 0\nif y > 300:\n    y = 300', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('Set reflections to 0. Loop four times adding 2 to reflections.', 'reflections = 0\nfor i in range(4):\n    reflections = reflections + 2', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('Write mirror(x) returning 500 if x > 500, otherwise x.', 'def mirror(x):\n    if x > 500:\n        return 500\n    else:\n        return x', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.')], [('Set charge to 0. Loop five times and add 3 to charge.', 'charge = 0\nfor i in range(5):\n    charge = charge + 3', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('Loop four times. If heat > 0, subtract 2 from heat.', 'for i in range(4):\n    if heat > 0:\n        heat = heat - 2', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('Set bolts to 0. Loop three times adding 1 to bolts, then set ready True.', 'bolts = 0\nfor i in range(3):\n    bolts = bolts + 1\nready = True', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('Write stabilize(power) returning power + 5 when power < 10, otherwise power.', 'def stabilize(power):\n    if power < 10:\n        return power + 5\n    else:\n        return power', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.')], [('Write activate(power) returning True if power >= 10, otherwise False.', 'def activate(power):\n    if power >= 10:\n        return True\n    else:\n        return False', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('Write restore(energy) returning energy + 4 if below 8, otherwise energy.', 'def restore(energy):\n    if energy < 8:\n        return energy + 4\n    else:\n        return energy', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('Write charge() that starts total at 0, adds 3 four times, and returns total.', 'def charge():\n    total = 0\n    for i in range(4):\n        total = total + 3\n    return total', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.'), ('Write escape(key, power) returning True when key and power >= 12, otherwise False.', 'def escape(key, power):\n    if key and power >= 12:\n        return True\n    else:\n        return False', 'Break the program into smaller parts: initialize values, check conditions, follow indented blocks, and return the requested result.')]]
def begin_puzzle():
    global state,puzzle_step,puzzle_selected
    state='puzzle';puzzle_step=0;puzzle_selected=0;reset_code_editor()
def finish_puzzle():
    global state,victory_kind,victory_countdown,repair_successes
    puzzle_done.add(room);stats['puzzles']+=1;repair_successes+=1;play_sfx('victory')
    journal_add('COMPLEX PUZZLE SOLVED: '+PUZZLE_NAMES[room]);grant_crystal('PUZZLE COMPLETE')
    victory_kind='puzzle';victory_countdown=90;state='celebrate'
def puzzle_submit():
    global puzzle_step,state,repair_successes,puzzle_feedback
    prompt,expected,why=PUZZLE_CODE_TASKS[room][puzzle_step]
    puzzle_attempts[room]+=1
    if code_normalize(code_input)==code_normalize(expected):
        repair_successes+=1;puzzle_step+=1;play_sfx('repair');reset_code_editor()
        if puzzle_step>=len(PUZZLE_CODE_TASKS[room]):finish_puzzle()
    else:
        stats['wrong']+=1
        puzzle_feedback='DEBUG NOTE: '+why+' WORKING CODE: '+expected.replace('\n',' / ')
        puzzle_retry_locks[room]=repair_successes;state='puzzle_explain'
def puzzle_key(key):
    global state
    if key==pygame.K_BACKSPACE:return 'exit'
    if key==pygame.K_h:
        puzzle_hints[room]+=1
        prompt,expected,why=PUZZLE_CODE_TASKS[room][puzzle_step]
        puzzle_note('HINT: '+why)
def puzzle_explanation_screen():
    modal('CODE GAUNTLET // DEBUG REVIEW','AN INCORRECT PROGRAM IS A CHANCE TO LEARN.')
    y=142
    for line in wrap_lines(puzzle_feedback,65)[:7]:draw_text(line,48,y,WHITE,S);y+=22
    draw_text('COMPLETE A DIFFERENT TASK BEFORE RETRYING.',48,318,GOLD,S)
    draw_text('ENTER: RETURN TO ARCADE',48,345,CYAN,S)
def puzzle_update():
    global puzzle_feedback_timer
    stats['seconds']+=1/60
    if puzzle_feedback_timer:puzzle_feedback_timer-=1
def puzzle_screen():
    prompt,expected,why=PUZZLE_CODE_TASKS[room][puzzle_step]
    code_task_screen('CIRCUIT PUZZLE '+str(puzzle_step+1)+'/4 // '+ROOMS[room],prompt)
    if puzzle_feedback_timer:draw_text(puzzle_feedback[:70],48,212,GOLD,S)

def grant_crystal(reason):
    # A full meter never destroys a reward. World crystals remain on the map,
    # while one-time puzzle/chest rewards wait safely until the meter has space.
    global crystal_bank,crystal_total,pending_crystals,overdrive_earned
    if crystal_bank>=5:
        pending_crystals+=1
        journal_add('POWER CRYSTAL RESERVED: '+reason)
        tell('OVERDRIVE FULL! CRYSTAL REWARD SAVED FOR AFTER ACTIVATION.',160)
        return
    crystal_total+=1; crystal_bank+=1; play_sfx('crystal')
    journal_add('POWER CRYSTAL: '+reason)
    if crystal_bank==5:
        overdrive_earned+=1
        journal_add('OVERDRIVE READY: PRESS V TO ACTIVATE.')


def activate_overdrive():
    global overdrive_time,overdrive_uses,crystal_bank,pending_crystals
    if overdrive_time:
        tell('OVERDRIVE PROTOCOL ALREADY ACTIVE!',90)
    elif crystal_bank==5:
        crystal_bank=0; overdrive_uses+=1; play_sfx('overdrive')
        overdrive_time=(28 if 3 in legendary else 20)*60
        # Deliver reserved one-time rewards only after the full meter is spent.
        while pending_crystals and crystal_bank<5:
            pending_crystals-=1
            grant_crystal('SAVED REWARD')
        tell('OVERDRIVE ACTIVATED! '+str(crystal_bank)+'/5 CRYSTALS IN NEW METER.',190)
    else:
        tell('COLLECT FIVE POWER CRYSTALS TO CHARGE OVERDRIVE.',140)

def start_gauntlet(n):
    global state,gauntlet_room,gauntlet_x,gauntlet_y,gauntlet_hits,gauntlet_cooldown,gauntlet_return
    gauntlet_room=n; gauntlet_x=42; gauntlet_y=200; gauntlet_hits=0; gauntlet_cooldown=0
    gauntlet_return=player.topleft
    state='gauntlet'
    journal_add('RESTRICTED AREA DISCOVERED: '+RESTRICTED[n][0])

def finish_gauntlet():
    global state,max_hp,hp,sword_upgrade,overdrive_time,victory_kind,victory_countdown
    n=gauntlet_room
    if n in legendary: return
    legendary.add(n); play_sfx('victory')
    if n==1:
        max_hp+=2; hp=max_hp
    elif n==2:
        sword_upgrade=True
    elif n==3:
        # Root Access permanently lengthens Overdrive, including an active charge.
        if overdrive_time: overdrive_time+=6*60
    journal_add('OVERDRIVE RELIC: '+RESTRICTED[n][1])
    victory_kind='legendary'; victory_countdown=105; state='celebrate'

def gauntlet_update():
    global frame,gauntlet_x,gauntlet_y,gauntlet_cooldown,gauntlet_hits,overdrive_time,hp
    frame+=1; stats['seconds']+=1/60
    if overdrive_time: overdrive_time-=1
    if gauntlet_cooldown: gauntlet_cooldown-=1
    keys=pygame.key.get_pressed()
    speed=5.8 if overdrive_time else 3.0
    gauntlet_x+=speed*(int(keys[pygame.K_RIGHT] or keys[pygame.K_d])-int(keys[pygame.K_LEFT] or keys[pygame.K_a]))
    gauntlet_y+=speed*(int(keys[pygame.K_DOWN] or keys[pygame.K_s])-int(keys[pygame.K_UP] or keys[pygame.K_w]))
    gauntlet_x=max(38,min(603,gauntlet_x)); gauntlet_y=max(112,min(290,gauntlet_y))
    for i,x in enumerate((145,233,321,409,497)):
        live=((frame//(24+gauntlet_room*7)+i*(gauntlet_room+1))%4 < (2 if gauntlet_room==2 else 3))
        if live and abs(gauntlet_x-(x+int(math.sin(frame*.045+i)*14) if gauntlet_room==3 else x))<17 and not overdrive_time and not gauntlet_cooldown:
            gauntlet_hits+=1; gauntlet_cooldown=95; gauntlet_x=max(40,gauntlet_x-55)
            hp=max(1,hp-1); stats['damage']+=1
    if gauntlet_x>571: finish_gauntlet()

def gauntlet_screen():
    screen.fill(BG)
    n=gauntlet_room
    title,reward,_=RESTRICTED[n]
    center(title,21,CYAN,L)
    center('RESTRICTED ACCESS  //  REWARD: '+reward,60,GOLD,S)
    box(25,91,590,221,[(25,35,59),(39,25,61),(30,51,47),(62,33,48),(34,30,62)][n],7)
    for x in range(40,605,28):
        for y in range(104,300,28):
            pygame.draw.rect(screen,(44,57,80),(x,y,26,26),1)
    for i,x in enumerate((145,233,321,409,497)):
        live=((frame//(24+gauntlet_room*7)+i*(gauntlet_room+1))%4 < (2 if gauntlet_room==2 else 3))
        color=[CYAN,PINK,GOLD,GREEN,PURPLE][n] if live else (55,81,97)
        for j in range(6):
            yy=106+j*33
            shift=int(math.sin(frame*(.15+n*.03)+j)* (4+n*2))
            if n==3:pygame.draw.line(screen,color,(x+shift,yy),(x-shift,yy+31),5 if live else 2)
            elif n==1:pygame.draw.circle(screen,color,(x+shift,yy+14),12 if live else 5,3)
            elif n==2:pygame.draw.polygon(screen,color,[(x,yy),(x+10+shift,yy+14),(x,yy+28),(x-10-shift,yy+14)],3)
            else:pygame.draw.line(screen,color,(x+shift,yy),(x-shift,yy+31),5 if live else 2)
        draw_text('LIVE' if live else 'OFF',x-14,94,GOLD if live else GRAY,S)
    # A different visible relic waits beyond each electrical gauntlet.
    relic_color=[CYAN,PINK,GOLD,GREEN,PURPLE][n]
    if n==1:
        pygame.draw.polygon(screen,relic_color,[(580,180),(590,194),(580,208),(570,194)])
    elif n==2:
        pygame.draw.line(screen,relic_color,(580,174),(580,207),5)
        pygame.draw.line(screen,WHITE,(574,188),(586,188),4)
    else:
        pygame.draw.circle(screen,relic_color,(580,194),12,3)
        pygame.draw.circle(screen,WHITE,(580,194),4)
    pygame.draw.rect(screen,(53,144,99),(566,170,34,60),2)
    draw_text('EXIT',568,153,WHITE,S)
    hero_color=[CYAN,PINK,GOLD,GREEN,PURPLE][frame//5%5] if overdrive_time else GREEN
    pygame.draw.circle(screen,hero_color,(int(gauntlet_x),int(gauntlet_y)),12)
    if overdrive_time:pygame.draw.circle(screen,GOLD,(int(gauntlet_x),int(gauntlet_y)),20,3)
    box(20,326,600,65,(16,23,42),5)
    draw_text('ARROWS: MOVE  |  V: OVERDRIVE  |  BACKSPACE: RETURN',34,336,WHITE,S)
    draw_text('TIME THE PULSES OR USE OVERDRIVE. THE EXIT IS ON THE RIGHT.',34,356,CYAN,S)
    draw_text('HEARTS '+str(hp)+'  HITS '+str(gauntlet_hits)+'  METER '+str(crystal_bank)+'/5'+'  ACTIVE '+str((overdrive_time+59)//60)+'s',34,374,GOLD,S)

def celebration_screen():
    global victory_countdown
    screen.fill((10,18,35))
    n=room if victory_kind=='puzzle' else gauntlet_room
    pulse=(frame//6)%5
    for i in range(7):
        pygame.draw.circle(screen,[CYAN,GREEN,GOLD,PURPLE,PINK][(i+pulse)%5],
            (320,174),28+i*21,2)
    if victory_kind=='puzzle':
        center('TELEPORTER RESTORED!' if n==0 else 'PUZZLE COMPLETE!',45,GREEN,L)
        center(PUZZLE_NAMES[n],98,CYAN,F)
        center('POWER CRYSTAL EARNED!',237,GOLD,L)
        center('EXIT SYSTEM RESTORED. WELL DONE, '+hero_name().upper()[:14]+'!',282,WHITE,S)
    else:
        center('LEGENDARY UPGRADE DISCOVERED!',45,GOLD,F)
        center(RESTRICTED[n][1],102,CYAN,L)
        explanation={1:'+2 MAX HEARTS  |  BLUE CAPACITOR ARMOR',
                     2:'DOUBLE SWORD DAMAGE  |  ELECTRIC BLADE',
                     3:'ROOT SCANNER  |  OVERDRIVE LASTS 18 SECONDS'}[n]
        center(explanation,252,GREEN,F)
        if len(legendary)==3: center('ALL THREE UPGRADES! MASTER ENDING UNLOCKED.',283,GOLD,S)
    if victory_countdown>0:
        center('ENERGY SURGE IN PROGRESS...',325,GRAY,S)
    else:
        center('PRESS ENTER OR CLICK TO CONTINUE',325,WHITE,F)

def draw_title():
    screen.fill(BG)
    for i in range(13):
        x=(i*53+frame//4)%W; y=(i*39+30)%H
        box(x,y,8,8,(45,55,99))
    center('GLITCH BUSTERS',85,CYAN,L)
    center('LEVEL 6: ECHOES OF THE VOID',130,GOLD,F)
    center('EVOLVE INTO THE GLITCH TITAN',158,CYAN,S)
    center('FIVE NEW AREAS  |  INPUT PUZZLES  |  ROBOT EVOLUTION  |  SECRETS',189,WHITE,S)
    center('WEEK 3 PYTHON: IF / ELSE, COMPARISONS, INDENTATION, GAME STATES',215,GREEN,S)
    center('ENTER TO BEGIN THE ADVENTURE',265,GOLD,F)
    center('F11: FULLSCREEN   M: MUSIC ON/OFF   ESC: LEAVE FULLSCREEN',301,GRAY,S)

def draw_end(won):
    background(); box(54,103,530,194,(17,24,43),8)
    center('LEVEL 6 COMPLETE!' if won else 'GAME OVER',130,GREEN if won else RED,L)
    center('ARTIFACTS '+str(len(artifacts))+'/3   PUZZLES '+str(len(puzzle_done))+'/5',185,GOLD,F)
    if won and len(legendary)==3: center('MASTER GLITCH BUSTER ENDING UNLOCKED!',218,CYAN,F)
    center('R: MISSION REPORT     ENTER: RESTART',253,WHITE,F)


music_enabled=True
music_started=False
music_channel=None
music_tracks={}

def music_control(toggle=False):
    global music_enabled,music_started,music_channel
    if toggle: music_enabled=not music_enabled
    try:
        if not pygame.mixer.get_init(): pygame.mixer.init()
        if not music_tracks:
            for name in ('arcade','puzzle','boss','title'):
                music_tracks[name]=pygame.mixer.Sound('music_'+name+'.ogg')
        if not music_enabled:
            if music_channel: music_channel.stop()
            return
        desired='title' if state=='title' else 'puzzle' if state in ('puzzle','quiz','mentor_check','gauntlet') else 'boss' if state=='world' and boss else 'arcade'
        if not music_channel or not music_channel.get_busy() or music_started!=desired:
            if music_channel: music_channel.stop()
            music_channel=music_tracks[desired].play(loops=-1)
            if music_channel: music_channel.set_volume(.24)
            music_started=desired
    except Exception as err:
        # Some school browsers may disable audio; gameplay must still work.
        if not music_started: print('QuestForge audio unavailable')
        music_started='unavailable'

async def game_loop():
    global state, chat_page, chat_selected, check_selected, dash_cd, dash_time
    global frame, hp, invuln, journal_page, player_name, potions
    global report_return, selected, victory_countdown, secret_lock_selected, code_input,code_cursor,code_feedback
    running=True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT: running=False
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mx,my=event.pos
                if state=='world':
                    if secret_room:
                        if secret_origin==2 and secret_index==0 and math.hypot(mx-450,my-253)<28 and distance(450,253)<49:
                            talk_to('ECHO')
                        elif pygame.Rect(288,206,65,38).collidepoint(mx,my) or pygame.Rect(289,281,65,37).collidepoint(mx,my): interact()
                    else:
                        clicked_person=False
                        for name,data in MENTORS.items():
                            if data['room']==room:
                                x,y=data['pos']
                                if math.hypot(mx-x,my-y)<30 and distance(x,y)<47:
                                    talk_to(name); clicked_person=True; break
                        if not clicked_person:
                            if room not in puzzle_done and math.hypot(mx-PUZZLE_POS[room][0],my-PUZZLE_POS[room][1])<42 and distance(*PUZZLE_POS[room])<85:
                                begin_puzzle()
                            else: inspect_secret(mx,my)
                elif state=='quiz':
                    pass
                elif state=='secret_lock':
                    pass
                elif state=='celebrate' and victory_countdown<=0:
                    state='world'
                    if victory_kind=='legendary':player.topleft=gauntlet_return
                elif state=='mentor_check':
                    pass
                elif state in ('mentor_result','mentor_retry'):
                    if state=='mentor_result': state='dialogue'; chat_page='menu'
                    else: state='world'
                elif state=='dialogue':
                    if chat_page in ('menu','experience') and 213<=my<300:
                        chat_selected=max(0,min(2,(my-213)//29)); dialogue_advance()
                    elif pygame.Rect(48,303,544,29).collidepoint(mx,my): dialogue_advance()
                elif state=='lesson': state='world'
                elif state=='report' and pygame.Rect(445,301,143,30).collidepoint(mx,my): copy_report()
            if event.type!=pygame.KEYDOWN: continue
            if event.key==pygame.K_m:
                music_control(toggle=True)
                continue
            if state=='title':
                if event.key==pygame.K_RETURN: new_game(); music_control()
                elif event.key==pygame.K_r: report_return='title'; state='report'
            elif state=='world':
                if event.key==pygame.K_z: attack()
                elif event.key==pygame.K_x:
                    if not dash_cd:
                        dash_time=9; dash_cd=75; invuln=max(invuln,11); stats['dashes']+=1
                elif event.key==pygame.K_c: shoot_bow()
                elif event.key==pygame.K_b: use_bomb()
                elif event.key==pygame.K_h:
                    if potions and hp<max_hp: potions-=1; hp=min(max_hp,hp+3); play_sfx('heal'); tell('HEALTH RESTORED!')
                elif event.key==pygame.K_e:
                    if not try_boss_hack(): interact()
                elif event.key==pygame.K_r: report_return='world'; state='report'
                elif event.key==pygame.K_j: journal_page=0; state='journal'
                elif event.key==pygame.K_v: activate_overdrive()
            elif state=='puzzle':
                if event.key==pygame.K_RETURN and event.mod & pygame.KMOD_CTRL:puzzle_submit()
                elif event.key==pygame.K_ESCAPE:state='world'
                else:code_key(event)
            elif state=='puzzle_explain':
                if event.key in (pygame.K_RETURN,pygame.K_SPACE,pygame.K_BACKSPACE):state='world'
            elif state=='secret_lock':
                if event.key==pygame.K_RETURN and event.mod & pygame.KMOD_CTRL:secret_lock_submit()
                elif event.key==pygame.K_ESCAPE:state='world'
                else:code_key(event)
            elif state=='secret_code_retry':
                if event.key in (pygame.K_RETURN,pygame.K_SPACE,pygame.K_ESCAPE):state='world'
            elif state=='gauntlet':
                if event.key==pygame.K_BACKSPACE:
                    state='world'; player.topleft=gauntlet_return
                elif event.key==pygame.K_v: activate_overdrive()
            elif state=='celebrate':
                if victory_countdown<=0 and event.key in (pygame.K_RETURN,pygame.K_SPACE):
                    state='world'
                    if victory_kind=='legendary': player.topleft=gauntlet_return
            elif state=='dialogue':
                if chat_page=='name':
                    if event.key==pygame.K_RETURN: dialogue_advance()
                    elif event.key==pygame.K_BACKSPACE: player_name=player_name[:-1]
                    elif event.unicode and event.unicode.isprintable() and len(player_name)<18:
                        if event.unicode.isalpha() or event.unicode in (' ','-','_'):
                            player_name+=event.unicode
                elif event.key==pygame.K_BACKSPACE: state='world'
                elif chat_page in ('menu','experience'):
                    if event.key==pygame.K_UP: chat_selected=(chat_selected-1)%3
                    elif event.key==pygame.K_DOWN: chat_selected=(chat_selected+1)%3
                    elif event.key in (pygame.K_1,pygame.K_2,pygame.K_3):
                        chat_selected=event.key-pygame.K_1; dialogue_advance()
                    elif event.key in (pygame.K_RETURN,pygame.K_SPACE): dialogue_advance()
                elif event.key in (pygame.K_RETURN,pygame.K_SPACE): dialogue_advance()
            elif state=='mentor_check':
                if event.key==pygame.K_RETURN and event.mod & pygame.KMOD_CTRL:answer_mentor_check()
                elif event.key==pygame.K_ESCAPE:state='world'
                else:code_key(event)
            elif state in ('mentor_result','mentor_retry'):
                if event.key in (pygame.K_RETURN,pygame.K_SPACE):
                    if state=='mentor_result': state='dialogue'; chat_page='menu'
                    else: state='world'
            elif state=='journal':
                if event.key in (pygame.K_BACKSPACE,pygame.K_j): state='world'
                elif event.key in (pygame.K_RIGHT,pygame.K_DOWN): journal_page=min(max(0,(len(journal)-1)//6),journal_page+1)
                elif event.key in (pygame.K_LEFT,pygame.K_UP): journal_page=max(0,journal_page-1)
            elif state=='quiz':
                if event.key==pygame.K_RETURN and event.mod & pygame.KMOD_CTRL:submit_answer()
                else:code_key(event)
            elif state=='lesson':
                if event.key in (pygame.K_RETURN,pygame.K_SPACE,pygame.K_BACKSPACE):
                    boss_quiz=False;state='world'
            elif state=='report':
                if event.key in (pygame.K_BACKSPACE,pygame.K_r): state=report_return
                elif event.key==pygame.K_c: copy_report()
            elif state in ('gameover','victory'):
                if event.key==pygame.K_r: report_return=state; state='report'
                elif event.key==pygame.K_RETURN: new_game(); music_control()
        if state=='title': frame+=1; draw_title()
        elif state=='world':
            update()
            if room==4 and ready_exit():
                stats['victories']+=1; state='victory'
            background()
            if not secret_room and boss and distance(boss['x'],boss['y'])<110:
                draw_text('Z: STRIKE NOW!' if boss_open else 'E: WRITE SHIELD CODE',215,309,GOLD,S)
        elif state=='puzzle': puzzle_update(); puzzle_screen() if state=='puzzle' else celebration_screen()
        elif state=='puzzle_explain': puzzle_explanation_screen()
        elif state=='secret_lock': secret_lock_screen()
        elif state=='secret_code_retry': secret_code_retry_screen()
        elif state=='gauntlet': gauntlet_update(); gauntlet_screen() if state=='gauntlet' else celebration_screen()
        elif state=='celebrate':
            frame+=1
            if victory_countdown>0:victory_countdown-=1
            celebration_screen()
        elif state=='dialogue': dialogue_screen()
        elif state=='mentor_check': mentor_check_screen()
        elif state in ('mentor_result','mentor_retry'): mentor_result_screen()
        elif state=='journal': journal_screen()
        elif state=='quiz': question_screen()
        elif state=='lesson': lesson_screen()
        elif state=='report': report_screen()
        else: draw_end(state=='victory')
        if music_enabled: music_control()
        pygame.display.flip()
        await asyncio.sleep(0)
    pygame.quit()

async def main():
    # Visible startup diagnostic: errors are displayed even when the console is quiet.
    try:
        screen.fill((12,15,31))
        screen.blit(L.render('QUESTFORGE BROWSER STARTING...', True, CYAN), (35,140))
        pygame.display.flip()
        await asyncio.sleep(0.2)
        await game_loop()
    except Exception:
        import traceback
        error=traceback.format_exc()
        print('QUESTFORGE STARTUP ERROR\n'+error,flush=True)
        lines=error.strip().splitlines()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT: return
            screen.fill((22,12,28))
            screen.blit(F.render('QUESTFORGE: BROWSER ERROR',True,(255,210,100)),(16,10))
            screen.blit(S.render('Send a photo of this screen.',True,(255,255,255)),(16,36))
            for i,line in enumerate(lines[-16:]):
                screen.blit(S.render(line[:100],True,(255,160,160)),(12,64+i*19))
            pygame.display.flip()
            await asyncio.sleep(0.05)

asyncio.run(main())
