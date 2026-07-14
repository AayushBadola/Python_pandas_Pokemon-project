# since the actual data of facts is vast we have isolated it in data directory 
# with the actual csv datas of gen 1 and gen 2 pokemon with duplicates and missing values


pokemon_facts = {
    "BULBASAUR": [
        "It is the only unevolved starter Pokémon that is dual-type.",
        "Its English name is a portmanteau of 'bulb' and 'dinosaur'.",
        "In the anime, Ash's Bulbasaur refused to evolve into Ivysaur.",
        "It can go for days without eating, sustained by the seed on its back.",
        "Bulbasaur is the first Pokémon listed in the National Pokédex."
    ],
    "IVYSAUR": [
        "The bud on its back is so heavy it forces Ivysaur's legs to grow thick and strong.",
        "It is the only Gen 1 second-stage Grass/Poison Pokémon that evolves via level up.",
        "Ivysaur is a playable character in Super Smash Bros. Brawl and Ultimate.",
        "When the bud on its back is ready to bloom, it gives off a distinct, sweet aroma.",
        "In the anime, May's Bulbasaur eventually evolved all the way into a Venusaur, passing through the Ivysaur stage off-screen."
    ],
    "VENUSAUR": [
        "The flower on its back catches the sun's rays to convert them into energy.",
        "It was the mascot of Pokémon Green and Pokémon LeafGreen.",
        "Venusaur is capable of Mega Evolution, gaining the Thick Fat ability.",
        "Female Venusaur have a seed in the center of their flower, while males do not.",
        "Its speed stat is surprisingly low despite its massive size, but it makes up for it in special attack."
    ],
    "CHARMANDER": [
        "If the flame on its tail goes out, Charmander will die.",
        "Its Japanese name, Hitokage, translates directly to 'fire lizard'.",
        "Ash obtained his Charmander after it was abandoned by a trainer named Damian.",
        "Charmander is the tallest Fire-type starter Pokémon in its base form.",
        "A Charmander's tail flame indicates its health and emotions."
    ],
    "CHARMELEON": [
        "It uses its tail to knock down opponents before tearing them with sharp claws.",
        "Charmeleon is notoriously aggressive and constantly seeks out battles.",
        "Ash's Charmeleon evolved into Charizard simply to battle an Aerodactyl.",
        "It has a crest on the back of its head which Charmander lacks.",
        "In the games, Charmeleon can learn Dragon Rage, making it deadly in early levels."
    ],
    "CHARIZARD": [
        "Despite its dragon-like appearance, it is a Fire/Flying type, not a Dragon type.",
        "Charizard has two different Mega Evolutions: Mega Charizard X and Mega Charizard Y.",
        "It is the only Pokémon besides Mewtwo to have two Mega Evolutions.",
        "Ash's Charizard originally refused to obey him, famously sleeping during battles.",
        "Its fire can burn through anything, and it will never turn its fiery breath on a weaker opponent."
    ],
    "SQUIRTLE": [
        "Squirtle is known as the 'Tiny Turtle Pokémon'.",
        "Ash's Squirtle was originally the leader of a mischievous gang called the Squirtle Squad.",
        "Its shell is not just for protection; its rounded shape minimizes water resistance.",
        "Squirtle is the most chosen starter Pokémon by speedrunners in Pokémon Red and Blue.",
        "It can shoot water from its mouth with enough force to accurately hit moving targets."
    ],
    "WARTORTLE": [
        "Its furry tail is a popular symbol of longevity in the Pokémon world.",
        "The scratches on its shell are proof of its toughness as a battler.",
        "Wartortle's ears and tail are covered in thick, furry hair that helps it swim.",
        "Old Wartortle often have algae growing on their shells.",
        "It hides in water to stalk unwary prey, popping out to surprise them."
    ],
    "BLASTOISE": [
        "The water jets from its shell cannons can punch through thick steel.",
        "It was the mascot for Pokémon Blue.",
        "Blastoise can learn the move Flash Cannon despite not being a Steel-type.",
        "Its Mega Evolution gives it a single, massive cannon on its back.",
        "It plants its feet firmly on the ground before firing to withstand the recoil."
    ],
    "CATERPIE": [
        "Caterpie was the first Pokémon Ash ever caught in the wild.",
        "It has a red antenna on its head that releases a terrible stench to repel predators.",
        "Its suction-cup feet allow it to climb nearly any surface, including glass.",
        "Caterpie shares its category, the 'Worm Pokémon', with Weedle and Wurmple.",
        "It must molt several times before it can safely enclose itself in a cocoon."
    ],
    "METAPOD": [
        "Its body is soft inside the hard shell, so it barely moves to avoid damage.",
        "The shell is as hard as an iron slab.",
        "In the anime, Ash's Metapod fought another Metapod using only the move Harden.",
        "It is preparing for evolution, conserving energy in its stationary state.",
        "Metapod is vulnerable to attacks before its shell fully hardens after evolution."
    ],
    "BUTTERFREE": [
        "It has a superior ability to search for delicious honey from flowers.",
        "Butterfree was the first Pokémon Ash released into the wild.",
        "Its wings are covered in water-repellent dust that carries toxic scales.",
        "It can spot blooming flowers from over six miles away.",
        "In Pokémon Sword and Shield, Butterfree received a Gigantamax form."
    ],
    "WEEDLE": [
        "Weedle has a highly toxic stinger on its head and another on its tail.",
        "It eats its weight in leaves every single day.",
        "Its bright colors serve as a warning to predators about its poison.",
        "Weedle has an incredibly acute sense of smell to distinguish types of leaves.",
        "It is often found in the same early-game forests as Caterpie."
    ],
    "KAKUNA": [
        "Although it appears completely still, it can extend its poison stinger when threatened.",
        "It hangs from branches using a strong, sticky thread.",
        "Inside its shell, Kakuna is extremely busy preparing for its adult form.",
        "It is almost completely incapable of moving, relying entirely on Harden.",
        "Kakuna can often be found in large clusters in forests."
    ],
    "BEEDRILL": [
        "Beedrill is highly territorial and attacks in swarms.",
        "It has three poisonous stingers: one on each arm and one on its tail.",
        "Mega Beedrill gains the Adaptability ability, making its Bug and Poison moves devastating.",
        "It flies at high speeds, attacking with rapid strikes from its twin stingers.",
        "In the anime, Beedrill swarms are a common natural hazard for trainers."
    ],
    "PIDGEY": [
        "Pidgey is extremely docile and prefers to flee from enemies rather than fight.",
        "It kicks up sand with its wings to blind opponents and hide.",
        "Its excellent sense of direction allows it to return home from anywhere.",
        "Pidgey is commonly used as a messenger Pokémon in the Pokémon world.",
        "It often hides in tall grass to forage for small insects."
    ],
    "PIDGEOTTO": [
        "It claims a vast territory and patrols it relentlessly.",
        "Pidgeotto relies on its sharp claws to carry prey over long distances.",
        "Ash's Pidgeotto was his second captured Pokémon in the anime.",
        "It has extraordinary vision, able to spot prey while flying at high altitudes.",
        "It will fiercely peck any intruder that enters its territory."
    ],
    "PIDGEOT": [
        "Pidgeot can fly at Mach 2 speed, faster than the speed of sound.",
        "Its gorgeous plumage is highly sought after by collectors.",
        "Ash left his Pidgeot to protect a flock of Pidgey and Pidgeotto in the anime.",
        "With a single flap of its wings, it can whip up a windstorm capable of bending trees.",
        "Mega Pidgeot boasts an incredible special attack stat and the No Guard ability."
    ],
    "RATTATA": [
        "Rattata can live and thrive anywhere, multiplying at an incredible rate.",
        "Its teeth grow continuously, so it constantly gnaws on hard objects.",
        "Alolan Rattata is Dark/Normal type and stands on its hind legs more often.",
        "It is known for the 'F.E.A.R.' strategy in competitive battles using a Focus Sash.",
        "Youngster Joey in Pokémon Gold and Silver is famous for bragging about his 'top percentage' Rattata."
    ],
    "RATICATE": [
        "Its hind feet are webbed, allowing it to swim proficiently.",
        "Raticate's fangs are strong enough to chew through cinder blocks and steel.",
        "Alolan Raticate stores huge amounts of food in its cheeks and becomes significantly heavier.",
        "If its whiskers are cut off, it loses its sense of balance.",
        "In Gen 1, Raticate was a notorious user of the high-damage move Hyper Fang."
    ],
    "SPEAROW": [
        "Spearow is very protective of its territory and will attack indiscriminately.",
        "It has a loud cry that can be heard up to half a mile away.",
        "A flock of Spearow famously attacked Ash and Pikachu in the first episode of the anime.",
        "Its wings are somewhat short, so it must flap them very fast to stay airborne.",
        "Spearow is known to eat small insects and occasionally target smaller Pokémon."
    ],
    "FEAROW": [
        "Fearow has existed largely unchanged in the Pokémon world since ancient times.",
        "It can stay in the air for a whole day without needing to land.",
        "Its long neck and beak allow it to pluck prey from the water or ground effortlessly.",
        "Fearow is one of the oldest fully-evolved Flying-types in the franchise.",
        "It was briefly used by Ash when he borrowed one in the anime."
    ],
    "EKANS": [
        "Its name is 'snake' spelled backward.",
        "Ekans can detach its jaw to swallow prey larger than its own head.",
        "It rests curled in a spiral, ready to strike from any direction.",
        "Jessie of Team Rocket obtained an Ekans as her primary battler early in the series.",
        "Ekans is born without poison; it relies on painful bites instead."
    ],
    "ARBOK": [
        "Its name is 'kobra' spelled backward.",
        "The pattern on its hood varies depending on the region it is found in.",
        "Arbok uses the frightening face on its hood to paralyze foes with terror.",
        "It can crush steel drums with its powerful constricting grip.",
        "Jessie's Ekans evolved into Arbok and remained her signature Pokémon for many seasons."
    ],
    "PIKACHU": [
        "Pikachu is the official mascot of the Pokémon franchise.",
        "It charges its electrical pouches while it sleeps.",
        "Pikachu is the only Pokémon allowed to say its own name in the mainline games.",
        "Ash's Pikachu famously refuses to enter a Poké Ball.",
        "It has a unique Gigantamax form that resembles its original, 'chubby' Gen 1 design."
    ],
    "RAICHU": [
        "Its long tail acts as a ground to protect it from its own high voltage.",
        "It can discharge up to 100,000 volts of electricity.",
        "Alolan Raichu is an Electric/Psychic type and surfs on its tail.",
        "Lt. Surge's Raichu brutally defeated Ash's Pikachu in their first gym battle.",
        "If its electricity builds up too much, it becomes aggressive and glowing in the dark."
    ],
    "SANDSHREW": [
        "It rolls into a tight ball to protect itself from attacks and harsh weather.",
        "Sandshrew lives in deep burrows in desert regions.",
        "Its skin is incredibly tough, allowing it to withstand great falls.",
        "Alolan Sandshrew adapted to snowy mountains, becoming an Ice/Steel type.",
        "Despite its ground type, it has an aversion to water and gets cold easily."
    ],
    "SANDSLASH": [
        "The spikes on its back are modified hairs that fall out and grow back quickly.",
        "It strikes with long claws and curls into a spiky ball in battle.",
        "Sandslash is known to climb trees, dropping down to ambush prey.",
        "Alolan Sandslash uses its ice spikes to carve through snow and glide swiftly.",
        "In the anime, AJ's Sandshrew evolved into Sandslash and had an impressive win streak."
    ],
    "NIDORAN_F": [
        "It is one of the few Pokémon species that explicitly indicates its gender in its name.",
        "Its small horn secretes a mild poison used mostly for self-defense.",
        "It has large ears that can rotate to listen in all directions.",
        "Nidoran♀ is known for its docile nature compared to its male counterpart.",
        "Despite its small size, its bite can be surprisingly painful."
    ],
    "NIDORINA": [
        "When in a group, Nidorina retract their barbs to avoid hurting each other.",
        "It becomes highly aggressive to protect its offspring.",
        "Nidorina is the only middle-stage Pokémon that completely loses the ability to breed.",
        "It uses ultrasonic waves emitted from its mouth to bewilder foes.",
        "It requires a Moon Stone to evolve into Nidoqueen."
    ],
    "NIDOQUEEN": [
        "Nidoqueen's scales are incredibly hard, protecting it from any attack.",
        "It is remarkably protective of its young and its nest.",
        "Despite being a female-only species, it is in the Undiscovered Egg Group and cannot breed.",
        "Nidoqueen's heavy tail is strong enough to easily knock down a building.",
        "It relies heavily on its physical bulk and Ground/Poison typing in battles."
    ],
    "NIDORAN_M": [
        "Its horn is larger and more toxic than that of Nidoran♀.",
        "It uses its highly developed ears to sense danger from afar.",
        "The poison on its horn is powerful enough to be life-threatening.",
        "Nidoran♂ attacks fiercely and won't back down from larger opponents.",
        "It was one of the first Pokémon to demonstrate gender differences in the franchise."
    ],
    "NIDORINO": [
        "It is quick to anger and will charge at any perceived threat.",
        "The horn on its head is harder than diamond.",
        "Nidorino famously appears battling a Gengar in the opening cinematic of Pokémon Red and Blue.",
        "Its poison spreads quickly upon piercing a foe.",
        "Like Nidorina, it requires a Moon Stone to reach its final evolution."
    ],
    "NIDOKING": [
        "Its tail is immensely powerful and can snap a telephone pole like a matchstick.",
        "Nidoking uses its thick arms, legs, and tail to crush opponents forcefully.",
        "Unlike Nidoqueen, Nidoking is capable of breeding in the Monster and Field egg groups.",
        "It often initiates combat by rushing its opponent and violently ramming them.",
        "Gary Oak used a Nidoking against Giovanni's Golem in the anime."
    ],
    "CLEFAIRY": [
        "It is said to arrive on meteors and lives in tight-knit colonies.",
        "Clefairy was originally planned to be the franchise mascot before Pikachu was chosen.",
        "It gathers in the moonlight to dance and sing, which causes its wings to glow.",
        "Clefairy's Metronome attack allows it to use nearly any move in the game unpredictably.",
        "Mt. Moon is famously known as the best place to find wild Clefairy."
    ],
    "CLEFABLE": [
        "It has excellent hearing and can hear a pin drop from half a mile away.",
        "Clefable prefers to live in secluded mountainous areas to avoid people.",
        "Its bouncy walk lets it literally walk on water.",
        "It was reclassified from Normal to pure Fairy-type in Generation VI.",
        "Clefable's Magic Guard ability makes it immune to all indirect damage."
    ],
    "VULPIX": [
        "It is born with a single white tail that eventually splits into six orange ones.",
        "Inside its body burns a flame that never goes out.",
        "Alolan Vulpix is an Ice-type and is covered in snowy white fur.",
        "Brock was given a Vulpix by Suzie, a Pokémon breeder, in the anime.",
        "Vulpix can manipulate fire, making wisps that resemble ghosts to trick foes."
    ],
    "NINETALES": [
        "It is said to live for a thousand years.",
        "Grabbing one of its tails allegedly results in a 1,000-year curse.",
        "Ninetales is highly intelligent and understands human speech.",
        "Its design is heavily inspired by the mythical kitsune of Japanese folklore.",
        "Alolan Ninetales is Ice/Fairy type and dwells on the sacred Mount Lanakila."
    ],
    "JIGGLYPUFF": [
        "Its singing puts anyone who hears it to sleep.",
        "In the anime, a recurring Jigglypuff would draw on the faces of sleeping characters with a marker.",
        "It has been a permanent roster member in every Super Smash Bros. game.",
        "Jigglypuff can adjust the wavelength of its voice to match the brain waves of someone in deep sleep.",
        "It inflates its body massively to sing longer without breathing."
    ],
    "WIGGLYTUFF": [
        "Its fur is exceptionally fine and pleasant to touch.",
        "If two Wigglytuff hug, they might not separate because their fur feels so good.",
        "It can inflate its body enormously by inhaling air, allowing it to bounce.",
        "Wigglytuff often serves as the assistant to Nurse Joy in the Kalos region.",
        "Its Guildmaster in Pokémon Mystery Dungeon: Explorers of Sky is famous for loving Perfect Apples."
    ],
    "ZUBAT": [
        "Zubat lacks eyes and relies entirely on echolocation to navigate.",
        "It is famously common in caves, irritating many players attempting to explore.",
        "It avoids sunlight because exposure causes it mild burns.",
        "Zubat stays clustered with others in dark places during the day.",
        "Brock caught a Zubat at Mt. Moon, which became a staple of his team."
    ],
    "GOLBAT": [
        "It loves to drink the blood of humans and Pokémon alike.",
        "Golbat can drink so much blood that it becomes too heavy to fly.",
        "Its fangs are hollow tubes used to suck blood quickly.",
        "Agatha of the Elite Four uses a Golbat in her Ghost/Poison team.",
        "It wasn't able to evolve further until Generation II introduced Crobat."
    ],
    "ODDISH": [
        "It buries itself in the soil during the day, looking like an ordinary weed.",
        "Oddish becomes active at night, scattering its seeds as it wanders.",
        "Its scientific name, according to the Pokédex, is Oddium Wanderus.",
        "When pulled from the ground, it screams in a high-pitched voice.",
        "It is commonly found on early routes in the Kanto region."
    ],
    "GLOOM": [
        "The stench from the fluid on its mouth can be smelled a mile away.",
        "It actually loves the foul smell and will drool more when feeling threatened.",
        "The nectar it secretes is a highly concentrated honey, not drool.",
        "Erika, the Celadon Gym Leader, uses a Gloom on her team.",
        "It can evolve into Vileplume with a Leaf Stone or Bellossom with a Sun Stone."
    ],
    "VILEPLUME": [
        "It has the largest petals of any flower in the world.",
        "Vileplume scatters toxic pollen every time it takes a step.",
        "The pollen can trigger severe allergic reactions in anyone who inhales it.",
        "Its heavy petals make it difficult for Vileplume to walk quickly.",
        "Its design is based on the real-life Rafflesia arnoldii flower."
    ],
    "PARAS": [
        "The mushrooms on its back are called tochukaso.",
        "The mushrooms command Paras to extract nutrients from tree roots.",
        "It is an early-game Bug/Grass Pokémon often found in Mt. Moon.",
        "Parasect's mushrooms are highly valued as a medicine ingredient.",
        "As Paras grows, the mushrooms on its back grow steadily larger."
    ],
    "PARASECT": [
        "The mushroom has completely taken over the bug host's brain.",
        "Parasect favors dark, damp places where the mushroom thrives.",
        "If the mushroom is removed, the host bug stops moving entirely.",
        "It scatters toxic spores from the mushroom cap.",
        "In Pokémon Legends: Arceus, an Alpha Parasect is known as a dangerous overworld boss."
    ],
    "VENONAT": [
        "Its eyes act as radar, allowing it to see clearly in total darkness.",
        "Venonat's body is covered in a stiff, toxic hair that protects it.",
        "It feeds mainly on smaller bugs drawn to light.",
        "Tracey Sketchit in the anime has a Venonat that uses its radar eyes to track Pokémon.",
        "Many fans note a striking resemblance between Venonat and Butterfree's designs."
    ],
    "VENOMOTH": [
        "It scatters highly toxic dust with every flap of its wings.",
        "The color of the dust determines the type of poison: dark dust paralyzes, light dust poisons.",
        "Venomoth is a nocturnal Pokémon that hunts small prey.",
        "Koga, the Fuchsia Gym Leader, uses a Venomoth in battle.",
        "Despite being a moth, it cannot learn the move Fly."
    ],
    "DIGLETT": [
        "It lives about one yard underground, feeding on plant roots.",
        "Its skin is very thin, so exposure to light heats up its blood rapidly.",
        "No one knows exactly what the lower half of Diglett's body looks like.",
        "Alolan Diglett has thin hairs resembling whiskers that are made of flexible steel.",
        "In Pokémon Mystery Dungeon, Diglett can be seen getting kidnapped by a Skarmory."
    ],
    "DUGTRIO": [
        "It is composed of three Diglett bodies that share a single mind.",
        "Dugtrio can dig through solid earth at speeds up to 60 mph.",
        "It is known to cause localized earthquakes while digging.",
        "Alolan Dugtrio grows lustrous, flowing hair made of spun steel.",
        "In Gen 1, Dugtrio's incredibly high speed made it a top-tier competitive Pokémon."
    ],
    "MEOWTH": [
        "Meowth loves shiny things and wanders cities at night searching for coins.",
        "The Meowth from Team Rocket taught himself to speak human language to impress a female Meowth.",
        "It has a Galarian form (Steel-type) and an Alolan form (Dark-type).",
        "It is the only Pokémon known to exclusively learn the move Pay Day by leveling up.",
        "Meowth is the only Pokémon in the anime known to have a unique Gigantamax form based purely on the anime."
    ],
    "PERSIAN": [
        "Its sleek coat has made it a popular pet among the wealthy.",
        "Persian is famously the signature Pokémon of Team Rocket boss Giovanni.",
        "It is highly temperamental and prone to scratching even those it trusts.",
        "Alolan Persian has a notably round face, which is considered a symbol of wealth in Alola.",
        "In Gen 1, Persian's high speed guaranteed that Slash almost always scored a critical hit."
    ],
    "PSYDUCK": [
        "It suffers from chronic, agonizing headaches.",
        "When its headache becomes severe, it inadvertently releases mysterious psychic powers.",
        "Misty accidentally captured a Psyduck when it dropped a Poké Ball on its own head.",
        "Despite its psychic abilities and name, it is a pure Water-type.",
        "Psyduck cannot remember using its powers after its headache subsides."
    ],
    "GOLDUCK": [
        "It swims faster than any human olympic swimmer.",
        "The gem on its forehead glows when it uses telekinetic powers.",
        "It is often mistaken for the Japanese cryptid, the Kappa.",
        "Golduck occasionally rescues people stranded at sea.",
        "Misty's Psyduck unexpectedly proved its potential, though it didn't evolve in the original series."
    ],
    "MANKEY": [
        "Mankey is incredibly quick to anger and throws uncontrollable tantrums.",
        "It is unsafe to approach Mankey, as it can attack without warning.",
        "Ash caught a Mankey after it stole his hat and evolved into Primeape.",
        "When it starts shaking and its nasal breathing turns rough, it is about to rage.",
        "It lives in large colonies in the mountains, constantly bickering with one another."
    ],
    "PRIMEAPE": [
        "Primeape will chase anyone who makes eye contact with it until they are beaten.",
        "It is only truly peaceful when it is completely alone.",
        "Ash gave away his Primeape to a P1 Grand Prix champion for specialized training.",
        "In Scarlet and Violet, it received a new evolution, Annihilape, achieved by using Rage Fist 20 times.",
        "It gets angrier the more it battles, boosting its physical power."
    ],
    "GROWLITHE": [
        "It is exceptionally loyal and will bark wildly to protect its trainer.",
        "Growlithe has a superb sense of smell used to track down outlaws.",
        "Officer Jenny heavily utilizes Growlithe in police forces across many regions.",
        "Hisuian Growlithe is a Fire/Rock type with a thick mane of insulating fur.",
        "It will stand up to foes much larger than itself without a second thought."
    ],
    "ARCANINE": [
        "It is classified as the 'Legendary Pokémon' in the Pokédex, despite not being an actual legendary.",
        "Arcanine can run over 6,200 miles in a single day and night.",
        "Its majestic beauty has captivated people since ancient times.",
        "Gary Oak notably used an Arcanine against Giovanni in the anime.",
        "Hisuian Arcanine incorporates rock-solid armor into its fiery mane."
    ],
    "POLIWAG": [
        "The spiral pattern on its belly is actually its internal organs visible through thin skin.",
        "Its skin is damp, smooth, and very slippery.",
        "Poliwag has newly grown legs, making it clumsy on land.",
        "It was the first Pokémon created by Satoshi Tajiri, according to early interviews.",
        "In the Pokémon Adventures manga, Red's first Pokémon was a Poliwag."
    ],
    "POLIWHIRL": [
        "Its body surface is continually slick with a slimy fluid.",
        "The spiral on its belly is opposite to the direction of Poliwag's spiral.",
        "Poliwhirl was prominently featured on the cover of Time magazine in 1999.",
        "It exudes a sweat that keeps its skin hydrated on land.",
        "It evolves into Poliwrath via a Water Stone or Politoed via trading with a King's Rock."
    ],
    "POLIWRATH": [
        "It is a master swimmer that excels at all known swimming strokes.",
        "Poliwrath has zero body fat, consisting entirely of dense muscle.",
        "It can briefly run on water due to its incredible leg strength.",
        "Red's Poliwhirl evolved into Poliwrath to save him from drowning in the manga.",
        "Despite its Water/Fighting typing, it boasts a remarkably high defense stat."
    ],
    "ABRA": [
        "Abra sleeps for 18 hours a day to rest its psychic powers.",
        "Even while deeply asleep, it can sense danger and Teleport away.",
        "In the original games, Teleport is the only move it learns naturally.",
        "Its name, along with Kadabra and Alakazam, relates to stage magic incantations.",
        "It frequently teleports to different locations while sleeping."
    ],
    "KADABRA": [
        "A famous rumor suggests Kadabra was originally a boy with psychic powers who transformed.",
        "It emits alpha waves that induce headaches in nearby people and machines.",
        "Kadabra holds a silver spoon which it uses to amplify its telekinetic abilities.",
        "Uri Geller famously sued Nintendo over Kadabra's design and name in Japan (Yungerer).",
        "Sabrina's Kadabra defeated Ash's Pikachu easily with its psychic prowess."
    ],
    "ALAKAZAM": [
        "Alakazam's brain continually grows, making its head too heavy for its neck.",
        "It boasts an IQ of over 5,000 and can remember everything.",
        "Alakazam uses its psychic powers to hold its head up.",
        "Mega Alakazam floats in the air, meditating with five spoons.",
        "Its muscle mass is very low; it relies entirely on psychokinesis for mobility."
    ],
    "MACHOP": [
        "Machop loves building its muscles and constantly trains by lifting heavy rocks.",
        "Its muscles never tire, no matter how much it exercises.",
        "It is small enough to be carried by a child but strong enough to throw a hundred adults.",
        "Machop is frequently employed by construction workers in the Pokémon world.",
        "In the Vermilion City gym, a puzzle features Machop stomping the ground."
    ],
    "MACHOKE": [
        "It wears a power-save belt to keep its overwhelming strength in check.",
        "Without its belt, Machoke's power is uncontrollable and dangerous.",
        "It gladly helps humans with heavy labor without asking for reward.",
        "Machoke has incredible stamina, able to work all day without rest.",
        "It evolves into Machamp exclusively when traded with another trainer."
    ],
    "MACHAMP": [
        "Machamp can throw 1,000 punches in a mere two seconds.",
        "It possesses four arms, but struggles with delicate tasks like tying its shoes.",
        "It uses its multiple arms to grapple foes in submission holds from every angle.",
        "Gigantamax Machamp has arms packed with incredibly dense, bursting energy.",
        "Bea, the Fighting-type Gym Leader in Galar, utilizes a powerful Machamp."
    ],
    "BELLSPROUT": [
        "Bellsprout roots itself in the ground to absorb moisture.",
        "Its incredibly flexible body allows it to easily dodge attacks.",
        "It attacks by spitting highly corrosive acid from its mouth.",
        "In the anime, Ash battled a remarkably agile Bellsprout in the Indigo League.",
        "Despite looking like a plant, its roots act like nervous system sensors."
    ],
    "WEEPINBELL": [
        "It uses a razor-sharp leaf to slice prey before digesting them.",
        "Weepinbell hooks its rear end on tree branches to rest.",
        "If its prey is bigger than its mouth, it slices it into pieces first.",
        "James of Team Rocket famously had a Weepinbell that evolved into Victreebel.",
        "It requires a Leaf Stone to evolve into its final form."
    ],
    "VICTREEBEL": [
        "It lures prey into its mouth with a sweet-smelling nectar.",
        "Once swallowed, prey is dissolved completely in mere hours.",
        "James's Victreebel had a running gag of trying to swallow him every time it was summoned.",
        "It collects moisture and nutrients inside its pitcher-like body.",
        "Victreebel groups are rumored to hold terrifying rituals deep in the jungle."
    ],
    "TENTACOOL": [
        "It drifts aimlessly in ocean currents, often stinging unwary swimmers.",
        "Its body is 99% water, making it nearly invisible in the ocean.",
        "Tentacool absorbs sunlight to convert it into energy.",
        "It is considered the 'Zubat of the sea' due to its incredibly high encounter rate while surfing.",
        "Its toxic tentacles break off easily but grow back rapidly."
    ],
    "TENTACRUEL": [
        "It possesses 80 tentacles that it stretches out to ensnare prey.",
        "Tentacruel can alert its peers to danger by flashing the red orbs on its head.",
        "In the anime, a giant mutated Tentacruel attacked Porta Vista.",
        "Its tentacles secrete a harsh poison that causes sharp, stabbing pain.",
        "It is remarkably fast in the water despite its bulky appearance."
    ],
    "GEODUDE": [
        "It is commonly mistaken for a rock and tripped over by hikers.",
        "Geodude climbs mountain paths using only the strength of its arms.",
        "Alolan Geodude is Rock/Electric type and contains magnetic sand.",
        "Brock's Geodude was one of his most reliable battlers in the early anime.",
        "When sleeping, it buries half its body in the ground."
    ],
    "GRAVELER": [
        "Graveler prefers rolling down mountain paths over walking.",
        "It doesn't care if pieces chip off its body while it furiously rolls.",
        "It eats a ton of rocks every day, preferring moss-covered ones.",
        "Alolan Graveler incorporates dravite crystals into its rocky body.",
        "It requires a trade to evolve into its final form, Golem."
    ],
    "GOLEM": [
        "Its rocky shell is as hard as bedrock and can withstand dynamite blasts.",
        "Golem sheds its skin once a year, growing a larger, harder shell.",
        "Alolan Golem functions as a living railgun, firing electrified rocks from its back.",
        "It retreats its head, arms, and legs to roll incredibly fast.",
        "Giovanni frequently used Golem in his gym battles against trainers."
    ],
    "PONYTA": [
        "Ponyta is capable of jumping over the Eiffel Tower with a single leap.",
        "Its hooves are 10 times harder than diamond.",
        "Galarian Ponyta is a Psychic-type resembling a unicorn with a pastel mane.",
        "Ash rode a Ponyta in a racing competition in the anime.",
        "Its fiery mane won't burn anyone who has gained its trust."
    ],
    "RAPIDASH": [
        "Rapidash can reach speeds up to 150 mph in just ten steps.",
        "The fiery mane blazes brilliantly when it races at high speed.",
        "Galarian Rapidash gains the Fairy typing and is known for its graceful pride.",
        "It instinctively chases anything that moves quickly past it.",
        "Blaine, the Cinnabar Island Gym Leader, considers Rapidash his signature Pokémon."
    ],
    "SLOWPOKE": [
        "Slowpoke feels no pain for an entire day if its tail is bitten.",
        "Its tail drips a sweet substance that makes it excellent for fishing.",
        "Team Rocket illegally harvested and sold Slowpoke Tails in Johto.",
        "Galarian Slowpoke is a pure Psychic-type with a yellow tipped tail.",
        "It takes a long time for it to realize it's in danger."
    ],
    "SLOWBRO": [
        "It evolves when a Shellder bites onto a Slowpoke's tail.",
        "If the Shellder falls off during a battle, it reverts back into a Slowpoke.",
        "Slowbro can Mega Evolve, causing the Shellder to swallow its entire body like armor.",
        "Galarian Slowbro is Poison/Psychic and uses a Shellder on its arm like a cannon.",
        "It loses its ability to feel pain entirely due to the Shellder's venom."
    ],
    "MAGNEMITE": [
        "Magnemite defies gravity using electromagnetic waves from its units.",
        "It is attracted to electrical lines and frequently causes power outages.",
        "It was purely an Electric-type in Gen 1, gaining the Steel type in Gen 2.",
        "When Magnemite runs out of electricity, it falls flat on the ground.",
        "It can emit strong radio waves that interfere with electronics."
    ],
    "MAGNETON": [
        "It is formed by three Magnemite linking together magnetically.",
        "Magneton generates a powerful magnetic field that ruins nearby electronics.",
        "Its magnetic force is strong enough to dry up all moisture in the air around it.",
        "It evolves into Magnezone when leveled up in a special magnetic field.",
        "Many towns warn citizens to keep Magneton in a Poké Ball to avoid tech damage."
    ],
    "FARFETCHD": [
        "It constantly carries a stalk of green leek, which it uses like a sword.",
        "If it eats its leek in an emergency, it will desperately search for a new one.",
        "Farfetch'd cannot survive without its stalk.",
        "Galarian Farfetch'd is a pure Fighting-type with a massive, heavy leek.",
        "It is based on a Japanese proverb about a duck offering itself along with leeks."
    ],
    "DODUO": [
        "Doduo's two heads never sleep at the same time to maintain watch.",
        "It is incredibly fast on land, running at 60 mph.",
        "Its two brains are linked telepathically, allowing perfect synchronization.",
        "Despite having no visible wings, it can learn the move Fly.",
        "It leaves large footprints in the ground when sprinting."
    ],
    "DODRIO": [
        "When Doduo evolves, one of its heads splits, giving Dodrio three heads.",
        "The three heads represent joy, sorrow, and anger.",
        "Dodrio runs extremely fast but struggles with complex coordination.",
        "Each head has a distinct personality, and they frequently squabble.",
        "It uses its three heads to rapidly peck opponents simultaneously."
    ],
    "SEEL": [
        "The horn on its head is tough enough to break through thick ice.",
        "Seel thrives in freezing environments and gets sluggish in warm water.",
        "It loves to rest on icebergs and sunbathe in freezing climates.",
        "In the anime, the Cerulean Gym keeps a Seel that later evolved.",
        "Its body is covered with light blue fur that acts as waterproofing."
    ],
    "DEWGONG": [
        "Its snow-white fur allows it to blend perfectly into snowy backgrounds.",
        "Dewgong stores thermal energy in its body, thriving in sub-zero oceans.",
        "It sleeps on icebergs and occasionally rescues stranded sailors.",
        "Lorelei of the Elite Four heavily utilizes Dewgong in battle.",
        "It is completely immune to the cold, regardless of how low temperatures drop."
    ],
    "GRIMER": [
        "Grimer was born from toxic sludge mutated by X-rays from the moon.",
        "As it moves, highly toxic sludge drips from its body, creating barren wastelands.",
        "Alolan Grimer is Poison/Dark and has crystalized toxic teeth.",
        "Ash caught a Grimer in Gringey City that frequently hugged Professor Oak.",
        "Wherever Grimer passes, no plants will ever grow again."
    ],
    "MUK": [
        "Muk's body is so toxic that just a single drop can contaminate a whole lake.",
        "It smells unbearably foul, but Muk's sense of smell is nonexistent.",
        "Alolan Muk has a brightly colored, shifting body from digesting various trash.",
        "In the anime, Ash's Muk is incredibly affectionate and loves smothering people.",
        "Its footprints remain violently toxic for years after it passes by."
    ],
    "SHELLDER": [
        "Its shell is purportedly harder than diamond and withstands enormous pressure.",
        "Shellder travels backward by clamping its shell rapidly.",
        "Its soft internal body is highly vulnerable when the shell is open.",
        "When a Shellder bites a Slowpoke's tail, it radically alters its own form.",
        "It often sticks its tongue out as a taunt to lure prey."
    ],
    "CLOYSTER": [
        "Cloyster's shell cannot be broken by any known means, not even a bomb.",
        "It fires sharp spikes from its shell to pierce enemies.",
        "When it clamps its shell shut, it is impossible for anyone to pry it open.",
        "Cloyster is a master of the move Shell Smash, dominating competitive play.",
        "Lorelei's Cloyster defeated Ash's Pikachu easily with Aurora Beam."
    ],
    "GASTLY": [
        "Gastly is made of 95% poisonous gas.",
        "It can easily be blown away by a strong gust of wind.",
        "It suffocates its victims by enveloping them in its toxic body.",
        "Gastly appeared as a talking spirit mimicking humans in 'The Ghost of Maiden's Peak'.",
        "It often hides in abandoned buildings, waiting for unwary travelers."
    ],
    "HAUNTER": [
        "Its tongue is made of gas and stealing an opponent's life force with a lick.",
        "Haunter loves to play practical jokes in the dark to frighten people.",
        "If you feel a sudden chill in the dark, a Haunter is likely near.",
        "Sabrina temporarily lost her serious demeanor because Ash's Haunter made her laugh.",
        "It can slip through solid walls to stalk its prey."
    ],
    "GENGAR": [
        "Gengar hides in the shadows of its victims, stealing their body heat.",
        "It can mega evolve, gaining a terrifying third eye.",
        "Gigantamax Gengar's mouth is said to be a direct portal to the afterlife.",
        "Ash's Gengar in Pokémon Journeys was extremely loyal but previously abandoned.",
        "It laughs gleefully as it watches its victims experience terror."
    ],
    "ONIX": [
        "Onix burrows through the earth at 50 mph, shaking the ground violently.",
        "As it grows older, its rocky body becomes smoother and rounder.",
        "Brock's Onix was his signature Pokémon in the Kanto and Johto anime arcs.",
        "It consumes large boulders, which compress inside its body to strengthen its shell.",
        "A special Crystal Onix resistant to water attacks appeared in the anime."
    ],
    "DROWZEE": [
        "It feeds on the dreams of people and Pokémon by extracting them through their noses.",
        "Drowzee prefers the dreams of children because they are tastier.",
        "Its design is based on the Baku, a tapir-like dream-eating yokai.",
        "It remembers every dream it has ever eaten.",
        "If your nose itches while you sleep, it means Drowzee is standing nearby."
    ],
    "HYPNO": [
        "Hypno carries a pendulum that it swings to induce deep sleep.",
        "There are scary rumors of Hypno hypnotizing and abducting a child.",
        "Its psychic powers are so potent it can force opponents into a slumber instantly.",
        "In the Sevii Islands, a Hypno was famously recorded kidnapping a lost girl named Lostelle.",
        "When it is very hungry, it puts humans to sleep to feast on their dreams."
    ],
    "KRABBY": [
        "If Krabby loses a pincer in battle, it quickly regenerates a new one.",
        "It creates a wall of bubbles to protect itself when feeling threatened.",
        "Ash caught a Krabby that remained at Professor Oak's lab until the Indigo League.",
        "Its pincers are remarkably strong but can easily unbalance it.",
        "It can be found on nearly any beach in the Kanto region."
    ],
    "KINGLER": [
        "One of Kingler's pincers grew disproportionately massive and heavy.",
        "The oversized pincer has 10,000 horsepower of crushing strength.",
        "Because the claw is so heavy, Kingler tires quickly during battle.",
        "Ash's Krabby evolved into Kingler during a crucial Pokémon League match and swept the opponent.",
        "It communicates with others by waving its enormous claw."
    ],
    "VOLTORB": [
        "Voltorb looks identically like a Poké Ball, often tricking item-hunters.",
        "It tends to explode without warning when startled.",
        "Hisuian Voltorb is Grass/Electric type and is made entirely of wood.",
        "It was first discovered in a Poké Ball factory.",
        "Many believe it is a Poké Ball exposed to strong energetic pulses."
    ],
    "ELECTRODE": [
        "Electrode stores so much electricity it regularly explodes from excess energy.",
        "It is known as the 'Bomb Ball' due to its volatile nature.",
        "Hisuian Electrode constantly vents electricity and seeds from a hole in its top.",
        "It was famously the fastest Pokémon in Generation 1.",
        "It consumes electricity from power plants to sustain itself."
    ],
    "EXEGGCUTE": [
        "Exeggcute consists of six egg-like seeds telepathically linked together.",
        "If one is separated, it quickly uses telepathy to reunite with the group.",
        "Despite looking like eggs, they are actually plant seeds.",
        "The shell cracks as it gets closer to evolving.",
        "They swarm enemies, rotating around them before attacking."
    ],
    "EXEGGUTOR": [
        "Each of Exeggutor's three heads has an independent brain.",
        "Alolan Exeggutor grows to over 35 feet tall, taking on a Dragon typing.",
        "If one of its heads grows too large and falls off, it becomes an Exeggcute.",
        "It is known as the 'Walking Jungle'.",
        "It frequently emits shrill psychic cries during battle."
    ],
    "CUBONE": [
        "Cubone wears the skull of its deceased mother as a helmet.",
        "Its mournful cries echo inside the skull, creating a melancholy melody.",
        "It uses a bone as a weapon to throw and strike opponents.",
        "The ghost of a Marowak mother is a famous encounter in Pokémon Tower.",
        "Cubone's true face has never been seen by any human."
    ],
    "MAROWAK": [
        "Marowak overcame its grief and became ferocious and tough.",
        "It is highly skilled at wielding its bone like a boomerang.",
        "Alolan Marowak is Fire/Ghost type and dances to honor its fallen ancestors.",
        "It actively hunts Mandibuzz to exact revenge for preying on Cubone.",
        "The bone it carries is collected from a secret graveyard."
    ],
    "HITMONLEE": [
        "Its legs can freely stretch and contract like coiled springs.",
        "Hitmonlee is known as the 'Kicking Fiend'.",
        "It has no mouth or nose visible on its body.",
        "Its name is a reference to the famous martial artist Bruce Lee.",
        "After a battle, it massages its legs to relieve fatigued muscles."
    ],
    "HITMONCHAN": [
        "Hitmonchan's punches are so fast they cut through the air, creating a sonic boom.",
        "It possesses an indomitable spirit and will never give up in a fight.",
        "It needs to take a break every three minutes while fighting.",
        "Its name is a reference to the famous martial artist Jackie Chan.",
        "It learns a variety of elemental punches, making it highly versatile."
    ],
    "LICKITUNG": [
        "Its tongue is over six feet long and covered in sticky saliva.",
        "Lickitung's saliva is paralyzing and causes an uncomfortable tingling sensation.",
        "Jessie accidentally traded her Lickitung for a Wobbuffet.",
        "It uses its tongue like a chameleon to catch prey.",
        "Its tongue is twice as long as its entire body."
    ],
    "KOFFING": [
        "Koffing's balloon-like body is filled with lighter-than-air toxic gases.",
        "When agitated, the gas expands and can cause Koffing to spontaneously explode.",
        "James obtained a Koffing as his first Pokémon in Team Rocket.",
        "It is frequently found in polluted areas and garbage dumps.",
        "Its design features a prominent skull-and-crossbones symbol."
    ],
    "WEEZING": [
        "Weezing is formed when two Koffing merge in heavily polluted environments.",
        "Galarian Weezing acts as an air purifier, breathing in smog and expelling clean air.",
        "James's Weezing was a reliable partner before he released it to protect a flock of Koffing.",
        "It continuously mixes different toxic gases to increase its toxicity.",
        "Very rarely, three Koffing can merge to form a mutant Weezing."
    ],
    "RHYHORN": [
        "Rhyhorn's brain is so small it can only focus on one thing at a time.",
        "Once it starts running, it will not stop until it hits something.",
        "Its bones are 1,000 times harder than human bones.",
        "In the Kalos region, trainers frequently ride Rhyhorn on specialized tracks.",
        "It often forgets why it started running in the first place."
    ],
    "RHYDON": [
        "Rhydon was the very first Pokémon ever designed by Game Freak.",
        "It is strong enough to topple buildings with a single swipe of its tail.",
        "Despite its rocky hide, Rhydon is highly intelligent.",
        "It can withstand the heat of magma without taking any damage.",
        "Rhydon was frequently used by Giovanni as one of his strongest Pokémon."
    ],
    "CHANSEY": [
        "Chansey lays several highly nutritious and delicious eggs every day.",
        "It is extremely rare in the wild and incredibly difficult to catch.",
        "Nurse Joys across all regions use Chansey as their medical assistants.",
        "Its eggs are highly valued as a luxury food item and healing medicine.",
        "Chansey is known for its immense HP stat but abysmally low physical defense."
    ],
    "TANGELA": [
        "Tangela's entire body is wrapped in thick, moving blue vines.",
        "If a vine is pulled off, a new one immediately grows in its place.",
        "Its true face hidden beneath the vines remains a complete mystery.",
        "Erika of Celadon Gym occasionally uses a Tangela in battles.",
        "It snaps its own vines to escape from predators when caught."
    ],
    "KANGASKHAN": [
        "Kangaskhan carries its young in its pouch until they are three years old.",
        "If it feels its baby is in danger, it becomes violently aggressive.",
        "Mega Kangaskhan's baby jumps out of the pouch to fight alongside its mother.",
        "It sleeps standing up so it doesn't crush the baby in its pouch.",
        "It has a deeply ingrained maternal instinct and will adopt lost Pokémon."
    ],
    "HORSEA": [
        "Horsea shoots ink from its mouth to blind predators and escape.",
        "It anchors itself with its tail to avoid being washed away by strong currents.",
        "Misty caught a Horsea that was struggling with injuries in the ocean.",
        "It swims backward by rapidly flapping its dorsal fin.",
        "When feeling safe, it playfully shoots water bubbles."
    ],
    "SEADRA": [
        "The spikes on Seadra's body secrete a deadly venom.",
        "It creates whirlpools by spinning its body rapidly underwater.",
        "Fishermen are cautious of Seadra because its sting causes intense pain.",
        "It swims backward to attack enemies with its venomous quills.",
        "Seadra requires a Dragon Scale and a trade to evolve into Kingdra."
    ],
    "GOLDEEN": [
        "Goldeen is called the 'Water Queen' because of its elegant, billowing fins.",
        "It will forcefully ram any intruder that enters its territory.",
        "During spawning season, they swim gracefully up rivers in large groups.",
        "Misty's Goldeen was notoriously useless when summoned on dry land.",
        "Its horn is extremely tough and can shatter glass instantly."
    ],
    "SEAKING": [
        "Seaking uses its drill-like horn to hollow out boulders in riverbeds for nests.",
        "The male and female take turns guarding their eggs.",
        "In autumn, Seaking grow significantly fatter to prepare for mating season.",
        "Its horn strikes are incredibly powerful, easily piercing steel.",
        "It is known for the meme 'F*** yeah, Seaking!' which gained massive internet popularity."
    ],
    "STARYU": [
        "Staryu's central core glows brightly like a star at night.",
        "If its appendages are severed, they rapidly regenerate as long as the core is intact.",
        "Misty consistently used a highly skilled Staryu in her gym battles.",
        "It communicates with others by blinking its red core.",
        "Staryu are often found near beaches at night, mirroring the starry sky."
    ],
    "STARMIE": [
        "Starmie's core glows in seven distinct colors during battle.",
        "Many people in the Pokémon world believe it is an extraterrestrial creature.",
        "It emits mysterious radio signals into the night sky.",
        "Misty's Starmie was her ace Pokémon in the Cerulean Gym.",
        "It uses rapid spinning movements to deliver powerful Water and Psychic attacks."
    ],
    "MR_MIME": [
        "Mr. Mime is a master of pantomime and can create invisible solid walls.",
        "If interrupted during a pantomime, it will slap the offender vigorously.",
        "Ash's mother, Delia Ketchum, has a Mr. Mime named Mimey who does chores.",
        "Galarian Mr. Mime is Ice/Psychic type and tap dances to create ice barriers.",
        "Its fingertips emit a strange force that solidifies the air."
    ],
    "SCYTHER": [
        "Scyther is incredibly fast and moves like a blur, confusing opponents.",
        "Its scythes become sharper each time it cuts through hard objects.",
        "Tracey Sketchit captured an elderly, deeply respected Scyther in the Orange Islands.",
        "It despises the color red and gets highly aggressive when seeing it.",
        "It requires a Metal Coat and a trade to evolve into Scizor."
    ],
    "JYNX": [
        "Jynx communicates using a bizarre, human-like language that sounds like chanting.",
        "Its hypnotic hip-swaying dance causes people to mimic its movements.",
        "Jynx was controversially redesigned, changing its face color from black to purple.",
        "Lorelei of the Elite Four uses a powerful Jynx.",
        "It uses psychic attacks paired with freezing ice magic."
    ],
    "ELECTABUZZ": [
        "Electabuzz feeds on electricity and causes massive blackouts near power plants.",
        "It spins its arms rapidly to generate electricity before throwing a punch.",
        "The red stripes on its body act as a lightning rod.",
        "In the anime, Paul frequently used an aggressive Electabuzz.",
        "It often quarrels with Scyther over territory in the wild."
    ],
    "MAGMAR": [
        "Magmar's body temperature approaches 2,200 degrees Fahrenheit.",
        "It heals its injuries by soaking in active volcanic magma.",
        "When it breathes deeply, heat waves emanate from its body, blurring the air.",
        "Blaine's Magmar gave Ash's Charizard an incredibly brutal and cinematic battle.",
        "It is born in the crater of a volcano."
    ],
    "PINSIR": [
        "Pinsir uses its massive horns to crush anything that gets in its way.",
        "It is highly sensitive to the cold and won't move when temperatures drop.",
        "Mega Pinsir gains the Flying typing and large wings.",
        "It is considered the natural rival to Scyther or Heracross.",
        "It sleeps high up in the trees, grasping branches with its horns."
    ],
    "TAUROS": [
        "Tauros is extremely prone to violence and charges at anything in its path.",
        "It whips itself with its three tails to build up momentum and anger.",
        "Ash famously caught 30 Tauros in the Safari Zone, a recurring gag in the anime.",
        "Paldean Tauros has three distinct regional forms: Combat, Blaze, and Aqua.",
        "Once a Tauros starts charging, it cannot stop until it hits a target."
    ],
    "MAGIKARP": [
        "Magikarp is widely considered the weakest and most pathetic Pokémon in the world.",
        "Despite its weakness, it can survive in any body of water, no matter how polluted.",
        "A Magikarp was famously bought by James from a shady salesman.",
        "It has a legendary ability to jump incredibly high, occasionally over mountains.",
        "Its Splash attack literally does absolutely nothing in battle."
    ],
    "GYARADOS": [
        "Gyarados is wildly destructive and has been known to raze entire cities.",
        "Its violent nature is said to be caused by its brain cells undergoing structural changes during evolution.",
        "Mega Gyarados becomes a Water/Dark type and becomes even more ferocious.",
        "The Red Gyarados at the Lake of Rage is one of the most famous shiny Pokémon.",
        "Its scales are harder than steel, making it nearly invulnerable."
    ],
    "LAPRAS": [
        "Lapras was driven to the brink of extinction due to overhunting.",
        "It has high intelligence and can fully understand human speech.",
        "Ash traveled across the Orange Islands on the back of a friendly Lapras.",
        "Thanks to conservation efforts, Lapras populations have vastly recovered.",
        "It sings a beautiful, mournful melody when searching for others of its kind."
    ],
    "DITTO": [
        "Ditto can perfectly rearrange its cellular structure to transform into anything.",
        "If it tries to transform from memory, it often gets details wrong.",
        "It is highly sought after by breeders because it can breed with almost any Pokémon.",
        "In the anime, a famous Ditto couldn't change its derpy face when transforming.",
        "When two Ditto meet, they will vigorously attempt to transform into each other."
    ],
    "EEVEE": [
        "Eevee possesses an irregular genetic makeup that allows it to evolve into many forms.",
        "Its evolution is triggered by its environment, stones, or friendship.",
        "It was the starter Pokémon for the rival in Pokémon Yellow.",
        "Eevee has a unique Gigantamax form resembling its heavily fluffy original design.",
        "It is one of the very few Pokémon capable of using a unique Z-Move, Extreme Evoboost."
    ],
    "VAPOREON": [
        "Vaporeon's cellular structure is similar to water molecules.",
        "It can melt away invisibly into water.",
        "It has gills that allow it to breathe underwater indefinitely.",
        "Vaporeon uses its large tail to detect incoming rain.",
        "It is celebrated for its massive HP stat in competitive battling."
    ],
    "JOLTEON": [
        "Jolteon gathers negative ions in the atmosphere to generate 10,000 volts of electricity.",
        "Its fur stands on end like sharp needles when it is angry or startled.",
        "It is capable of firing its spiked fur like a volley of darts.",
        "Jolteon was favored by Gen 1 speedrunners for its immense speed and critical hit rate.",
        "Its mood changes quickly, making it notoriously difficult to train."
    ],
    "FLAREON": [
        "Flareon fluffs out its thick collar to cool down its high body temperature.",
        "It stores thermal energy in an internal flame sac.",
        "When breathing fire, its internal temperature can reach 1,650 degrees Fahrenheit.",
        "Despite its high physical attack, it lacked a strong physical Fire move for many generations.",
        "It is incredibly soft and warm to hug, making it popular in cold regions."
    ],
    "PORYGON": [
        "Porygon was created entirely from computer programming code.",
        "It doesn't need to breathe, allowing it to function in the vacuum of space.",
        "It was the focus of a controversial anime episode that caused real-life seizures.",
        "Porygon can perfectly replicate any attack used against it using Conversion.",
        "It can move freely in cyberspace and enter computer networks."
    ],
    "OMANYTE": [
        "Omanyte is an ancient Pokémon resurrected from a Helix Fossil.",
        "It navigates the water by manipulating air trapped inside its shell.",
        "If attacked, it completely withdraws into its hard shell.",
        "It went extinct millions of years ago, but is now bred in captivity.",
        "Omanyte inspired the infamous 'Lord Helix' meme during Twitch Plays Pokémon."
    ],
    "OMASTAR": [
        "Omastar has sharp, fang-like teeth capable of cracking Shellder shells.",
        "Its shell grew so heavy it eventually struggled to hunt, contributing to its extinction.",
        "It attacks prey by wrapping them in its tentacles.",
        "Omastar was famously chosen by Red in Twitch Plays Pokémon.",
        "It is an exceptionally slow swimmer due to its unwieldy shell."
    ],
    "KABUTO": [
        "Kabuto was resurrected from the Dome Fossil.",
        "It hides on the ocean floor, blending in perfectly with the rocks.",
        "The 'eyes' on its back glow in the dark.",
        "Its true eyes are located underneath its shell.",
        "It has remained mostly unchanged for 300 million years."
    ],
    "KABUTOPS": [
        "Kabutops uses its sharp scythes to slash prey before draining their fluids.",
        "It eventually moved from the ocean to land to adapt to environmental changes.",
        "It swims extremely fast by folding its scythes close to its body.",
        "Kabutops is widely considered a relentless and vicious predator.",
        "Its body shape heavily inspired the design of the Pokémon Genesect."
    ],
    "AERODACTYL": [
        "Aerodactyl is a prehistoric predator resurrected from Old Amber.",
        "Its fangs are serrated like a saw, capable of tearing flesh and steel.",
        "Mega Aerodactyl is brutally aggressive because of the jagged rocks growing out of its body.",
        "In the anime, an Aerodactyl briefly kidnapped Ash.",
        "It ruled the ancient skies with absolute ferocity."
    ],
    "SNORLAX": [
        "Snorlax eats at least 900 pounds of food a day before going to sleep.",
        "Its stomach acids are strong enough to digest heavily spoiled or poisoned food.",
        "In the games, players typically must use a Poké Flute to wake up a sleeping Snorlax.",
        "Ash caught a Snorlax in the Orange Islands that proved to be an unexpected powerhouse.",
        "Gigantamax Snorlax has an entire ecosystem, including a park and tree, growing on its belly."
    ],
    "ARTICUNO": [
        "Articuno creates blizzards by simply flapping its majestic wings.",
        "It has been known to appear to doomed people lost in snowy mountains.",
        "Galarian Articuno is a Psychic/Flying type that emits psychic energy from its eyes.",
        "It is one of the three Legendary Birds of Kanto.",
        "Its translucent ice-like feathers are stunningly beautiful."
    ],
    "ZAPDOS": [
        "Zapdos gains immense power when struck by lightning.",
        "It causes massive thunderstorms simply by flapping its wings.",
        "Galarian Zapdos is a Fighting/Flying type resembling a grounded roadrunner.",
        "It was originally found at the Kanto Power Plant.",
        "Its loud screeches sound like snapping electricity."
    ],
    "MOLTRES": [
        "Moltres scatters blazing embers with every flap of its wings.",
        "If wounded, it heals itself by diving into the magma of an active volcano.",
        "Galarian Moltres is a Dark/Flying type that exudes a sinister aura.",
        "Its flames were traditionally used to ignite the torch for the Pokémon League.",
        "It migrates southward when spring arrives."
    ],
    "DRATINI": [
        "Dratini sheds its skin constantly as it grows larger.",
        "It was considered a mere myth until a colony was discovered underwater.",
        "It can be fished up in the Kanto Safari Zone.",
        "Dratini possesses immense life energy deep within its body.",
        "It hides behind large waterfalls to protect its soft, molting skin."
    ],
    "DRAGONAIR": [
        "Dragonair stores immense energy in the crystalline orbs on its neck and tail.",
        "It can alter the weather, summoning rain or calming storms at will.",
        "Despite having no wings, it can fly gracefully through the sky.",
        "It is often revered as a divine Pokémon in many regions.",
        "Clair, the Blackthorn Gym Leader, has a powerful Dragonair on her team."
    ],
    "DRAGONITE": [
        "Dragonite can circle the entire globe in just 16 hours.",
        "Despite its bulky appearance, it is incredibly kind and saves drowning sailors.",
        "If severely angered, it goes on an unstoppable rampage.",
        "Lance, the Champion of Johto, is famous for using three illegal-level Dragonite.",
        "Ash caught a surprisingly huggable Dragonite in Pokémon Journeys."
    ],
    "MEWTWO": [
        "Mewtwo was created by genetic manipulation from Mew's DNA.",
        "It was designed to be the ultimate battle machine, devoid of compassion.",
        "It destroyed the laboratory where it was created in a fit of rage.",
        "Mewtwo possesses two distinct Mega Evolutions, X and Y.",
        "It starred in the first Pokémon movie, questioning the purpose of its existence."
    ]
}