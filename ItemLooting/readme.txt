This is the original 2232 ItemLooting.dat with armor/weapon/dungeon key drops manually restored.

Over 100 hours of work, you wont find a more accurate loot table anywhere else.

# .xlsx color coding:

Green = drop rate was added from 216.
Blue = The row has been modified to match 216 or fix a bug.

Notes:
2.1.6 table had a droprate of x5 by increasing the default count/operation count; this was accounted for and divided by 5 before adding.

# Rules for 2232 table:

1. Do not alter or change the 2232 drop rates. We only _ADD_ missing.
example; Lucky Cube already has a drop value for weapons, we will NOT overwrite that value with 216 value.

~# Master List of fixed bugs (Also acts as proof of manual import) #~

BEGIN~

NPC 00301 Digger Clan
216 Invalid item count 70 instead of 10
216 removed extra item Gold Pig item 0.005% chance

NPC 01801
Kept original 2232 value

NPC 03200
Kept original 2232 value "7301332 0 1" instead of "8063554 0 2"
216 Invalid item count 15 instead of 108

NPC 04C0B
216 Invalid item count 5 instead of 1

NPC 01106
216 Invalid item count 1 instead of 15

NPC 05807
Kept original 2232 value "171796070	0	1" instead of "1610588159	0	2	1"
216 invalid item count 119 instead of 140

NPC 03908 (ace)Naid Heller
Fixed bug from 216 drops where accretia race was missing a line of drops. Changed to match the other 2 races.

NPC 03E0A
Has a slightly lower drop chance compared to the other 2 races, 966352 instead of 1073725. Left default.

NPC 08713
216 invalid item count 45 instead of 12
Kept original 2232 values, just added the armor row.

PitBosses (Unchanged, kept 2232 values.):

0AB07	RockJaw
0AC07	Blink
0AD07	Soul Sinder
06D07	Belphegor
0AE07	Spyfus
0AF07	Taraven
0B007	Dagnue
0B107	Dagan
0B207	Dagon
05817	Calliana Queen
06D07	Belphegor

NPC 032A3
216 incorrect item count 2 instead of 3
Kept original 2232 value

NPC 04307
216 invalid item count 24 instead of 126
Kept original 2232 values

#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~
For all of the following NPC in this block:
- Added 216 droprates for 55, 53 white armor.
- Used 216 drop list for 55, 53 white armor. (216 has 33% bias towards dropping gloves by having duplicate glove items in the row)
- Fixed empty spaces in item row.

00E03
0190B
01B03
01003
0CA03
0C913
13503
04103
0D403
0D303
0D80B
16013
0290B
16113
0E10B
16203
0EB03
15703
15503
15603
15703
15803
15903
15A03
09113 - Lucky Cube - kept 2232 droprate for weapon row, (5x less for weapon compared to 216, but we don't edit 'existing 2232 values')
0A503
00903 - Also fixed bug, changed loot operation count from 2 > 0 (for row that had no items)
00903
0231B
0DC1B - Also enabled rare ore drop to match 216.
0301B
0E60B
00F0B
01503
04E13
00E13
06A13
#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~

Pitbosses (Unchanged, kept 2232):

16307	Ringleader BloodAxe
16517	Endless Flame Draco
0ED07	Izen Cracker
13A07	Black Sign

END ~ Stopped Importing at 10403 ~ END
