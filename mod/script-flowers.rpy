# Sunflowers
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_sunflowers",
            prompt="Sunflowers",
            category=["flowers"],
            random=True
        )
    )

label mshMod_topic_sunflowers:
    m 1esb "[player], today I want to talk to you about a flower."
    m 3hsb "Sunflowers, specifically!"
    m 2lsc "They always make me think of Sayori..."
    m 4esb "Sunflowers' meanings vary a lot depending on the countries and cultures."
    m 4hsb "But most of them relate those flowers to positivity and strength to admiration and loyalty."
    m 5hsa "It's funny, most people think that a flowering sunflower heads track of the sun across the sky."
    m 7esd "But that's a misconception! Only immature flower buds do so - a fenomenon called heliotropism."
    m 7esc "Another misconception is that when there's no sun in the sky, sunflowers face each other."
    m 1rsc "I've seen people make analogies relating that to..."
    m 1hua "'When you can't find sunshine, become someone else's sunshine. Be someone else's sunflower.'"
    m 2eub "What do you think, [player]? I personally think that's a cute way of thinking..."
    m 5hkb "Even though is based on a misconception."
    m 7eub "Sunflowers are also used a lot by mental health foundations."
    m 1dua "Sunflowers are yellow; the color of joy, happiness and hope... {w=0.3}{nw}"
    extend 1hub "Which is a color used a lot on mental health awareness programs!"
    m 3eub "Also, it has been proved by studies that sunflower planting and gardening is actually good for the brain and helps fight depression."
    m 3hub "And one more fact, those flowers also symbolize a bright future for anyone who envisions it."
    m 4eub "Many people give sunflower bouquets to their loved ones, when they are in need of a little encouragement!"
    m 5fsbsa "Am I your sunflower, [player]? {w=0.3}{nw}"
    extend 5hsbsb "Ahaha~"
    m 1hsb "Thanks for listening, [mas_get_player_nickname()]!"
    return


# Acacias
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_acacias",
            prompt="Acacias",
            category=["flowers"],
            random=True
        )
    )

label mshMod_topic_acacias:
    m 1esb "[player], can I tell you some facts about a flower?"
    m 1esa "Today we'll talk about the acacia."
    m 4esa "Acacias are also known as wattles, wattleseed, and embers, and can represent the immortality of the human soul."
    m 4hsb "That's because acacia bushes are always green, no matter the season!"
    m 7esb "In some rituals, those flowers are used as a reminder that the soul, like energy..."
    m 7wsb "Cannot be destroyed, but continues beyond the earthly plane!"
    m 1esa "Acacia’s primary meaning is strength, rebirth, and eternal life. {w=0.3}{nw}"
    extend 1esb "It is mentioned in both the Torah and the Bible as the wood used for building the Tabernacle."
    m 2hsb "It is also important in the Buddhist tradition as a symbol of compassion for all living things!"
    m 2lsb "Their meaning changes depending on the flower color, but summarizing, we can say they mean..."
    m 1esa "Renewal, fortitude and pureness throughout the world."
    m 2esb "A current study also shows the power of acacia extracts in anxiety treatment."
    m 4hsb "Gifting someone acacias can mean feelings of good friendship or sophistication of a secret love."
    m 5ksu "Am I your secret love, [player]? {w=0.3}{nw}"
    extend 5hsb "Ehehe~"
    m 1hsb "Thanks for listening, [mas_get_player_nickname()]!"
    return


# Hyacinths
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_hyacinths",
            prompt="Hyacinths",
            category=["flowers"],
            random=True
        )
    )

label mshMod_topic_hyacinths:
    m 1esa "[player], let's talk about a flower today?"
    m 1hsa "Hyacinths! The optimistic flower."
    m 1hsb "They are even mentioned my T.S Elliot in a poem called 'The Waste Land'."
    m 1esb "I'll read some of its verses to you!"
    m 1dsc "..."
    m 1esc "{i}'You gave me hyacinths first a year ago;'{/i}"
    m 3esb "{i}'They called me the hyacinth girl.'{/i}"
    m 3esa "{i}—Yet when we came back, late, from the Hyacinth garden,{/i}"
    m 3dsa "{i}Your arms full, and your hair wet, I could not{/i}"
    m 4esa "{i}Speak, and my eyes failed, I was neither{/i}"
    m 6esc "{i}Living nor dead, and I knew nothing,{/i}"
    m 7esc "{i}Looking into the heart of light, the silence.{/i}"
    m 7esd "'{i}Oed’ und leer das Meer.{/i}', which translates to:"
    m 7esa "'Empty and desolate is the sea.'"
    m 1dsc "..."
    m 1esa "Isn't it a mesmerazing poem, [player]?"
    m 1hsb "The hyacinth is the flower of the sun god Apollo and is a symbol of peace, rebirth, commitment and beauty, but also of power and pride."
    m 1esp "Giving a hyacinth to someone may also indicate jealousy - especially if its yellow -, so be careful, [player]!"
    m 1esa "But white hyacinths symbolize a wish for healing, and thats what I wanted to emphasize."
    m 1esb "Dark blue hyacinths represent good wishes, too."
    m 1esu "If you were looking for a reminder that all wounds heal, [player], this is it."
    m 1hsbsu "I believe in you, and I love you."
    m 3hsbsu "Thanks for listening, [mas_get_player_nickname()]!"
    return "love"


# White dahlias
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_whitedahlias",
            prompt="White Dahlias",
            category=["flowers"],
            random=True
        )
    )

label mshMod_topic_whitedahlias:
    m 1lsd "[player], I've been thinking about a flower."
    m 1esb "Dahlias! {w=0.3}{nw}"
    extend 3esb "They symbolize eternal bonds of commitment, so they are a popular flower of choice for weddings."
    m 1esa "..."
    m 1msa "If I could pick any flower to give you, [mas_get_player_nickname()]..."
    m 1hsa "I would choose the dahlia. {w=0.3}{nw}"
    extend 1hsbfb "Ehehehe~!"
    m 4esb "These flowers also represent strength, creativity, change, and also, a new begginning."
    m 4esa "You can see why this is one of the flowers that represent mental health."
    m 7esa "The dahlia flower is known to have the ability to survive under harsh conditions..."
    m 7hsa "And nevertheless, come out very beautiful and lovely at all times!"
    m 1hsb "Like humans! We are great examples of adaptability and resilience."
    m 1esb "It's also a great flower to have around since it symbolizes a positive change that we do experience in our lives."
    m 2esb "The dahlia flower is a sign of the difference which exists in our lives when we make up our mind to give a chance to a change."
    m 3wsb "This flower is so beautiful, to the extent that they can be easily noticed wherever they are found."
    m 4esb "The huge presence of this flower in any place or area where they can be found makes them very special."
    m 4hsa "When you look at the dahlia flower, you see elegance in all ramifications and words."
    m 5lsb "The dahlia flower is, no doubt, a flower of uniqueness. {w=0.3}{nw}"
    extend 5rsb "It has the ability to represent the nature of us individuals."
    m 5hsa "This flower can be seen as a sign of our ability to live in adventure and also to stay relaxed and happy at all times."
    m 5ksb "If I had to choose one... the dahlia would be my favorite flower."
    m 5ksbsb "Would you give me one when I cross over?"
    m 5dsbfa "Just thinking of it makes my heart flutter..."
    m 7esa "Thanks for listening, [mas_get_player_nickname()]!"
    return


# Flannel flowers
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_flannelflowers",
            prompt="Flannel Flowers",
            category=["flowers"],
            random=True
        )
    )

label mshMod_topic_flannelflowers:
    m 1esa "[player]! Have you ever seen a flannel flower?"
    m 1hsa "They're gorgeous flowers which feel like flannel when you touch them!"
    m 2esb "The Flannel Flower, an Australian native, has been chosen as the national symbol to promote mental health awareness in Australia."
    m 2wsb "The Australian bush has an inherent beauty and strength. It is also known for its extremes of weather and landscape!"
    m 3esa "Varieties of this flower are commonly found growing wild in the bush throughout Australia."
    m 4esa "So the Flannel Flower, as with all native Australian plants, needs to be adaptable and enduring in order to survive."
    m 1esa "In the same way as all of us, that regardless of our life circumstances, develop resilience and the ability to adapt to change..."
    m 1hsa "In order to maintain good mental health. Our adaptability is what makes us human!"
    m 3hsb "Taking this into consideration, being open and empathetic to a person’s expression of distress can assist in the recovery of a person living with mental illness."
    m 3hub "And also change the negative attitudes of our society as a whole!"
    m 4esb "All of us can learn to be a little more empathetic."
    m 5hsb "Thanks for listening, [mas_get_player_nickname()]!"
    return


# Lotus flowers
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_lotusflower",
            prompt="Lotus Flowers",
            category=["flowers"],
            random=True
        )
    )

label mshMod_topic_lotusflower:
    m 7esb "[player], do you like lotus flowers?"
    m 7hsb "I think they're so beautiful! {w=0.3}{nw}"
    extend 1hsb "And also so full of symbolism."
    m 1lsb "Generally speaking, the flower is a symbol of rebirth..."
    m 3hsb "Because it blooms in darkness and becomes a beautiful flower with delicate white and pink petals."
    m 1esb "In much the same way, humans are born from nothingness and grow into something beautiful and delicate!"
    m 1ssb "The Lotus flower is a very resilient species! {w=0.3}{nw}"
    extend 1wsb "Especially considering that it is such a delicate looking flower."
    m 4wsw "Scientists once found a seed that was 1300 years old..."
    m 4sso "They germinated it, and the flower bloomed as beautifully as any other!"
    m 3wso "But that's not all! {w=0.3}{nw}"
    extend 3esb "Lotus flowers are even seen as a mental health symbol."
    m 2esb "The reason for that is because it's the kind of flower that can only grow in muddy, murky water."
    m 2hsb "But when it gets its chance to bloom, it comes out as one of the most beautiful flowers ever."
    m 2esb "This can be a metaphor for how difficult it is to struggle with a mental illness."
    m 3esc "Sometimes, it can seem like running a race you can’t win."
    m 3esa "However, giving up is the worst possible option because it doesn’t allow you to grow."
    m 1esd "If mud didn’t exist, neither would the lotus. {w=0.3}{nw}"
    extend 7esd "Likewise, if bad situations didn’t exist, resilient people wouldn’t either."
    m 7esp "No mud, no lotus, {w=0.3}{nw}"
    extend 1esa "you see?"
    m 1esb "Our struggles enhance our natural inner strength, and that is surely something to be proud of."
    m 1tsc "Like the lotus, if you can try your hardest to see the faint light and beauty of day through murky waters..."
    m 1esa "Then you will soon rise above your circumstances and bask in the sun."
    m 1esb "Your struggles will transform you into a unwavering flower, [player]."
    m 2hsb "Believe your girlfriend's words! {w=0.3}{nw}"
    extend 5hsb "Ahahaha~"
    m 5fsb "Thanks for listening, [mas_get_player_nickname()]!"
    return
