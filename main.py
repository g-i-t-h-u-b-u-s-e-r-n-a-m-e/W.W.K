import cv2
import numpy as np
import random

typer = "(start)"
greens = ["Greetings from the world's worst keyboard!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In congue pharetra leo, nec lobortis leo dignissim quis. Curabitur sed neque et lacus pellentesque fringilla. Praesent neque nunc, porttitor vitae dictum et, rhoncus quis eros. Etiam mattis, arcu vel maximus ultricies, enim tellus pellentesque ex, ac malesuada quam metus eget augue.", "Hi, my name is Devin. I’m in ninth grade, and like you, I had to take the diagnostic. The results of the diagnostic decide what lessons you get. The diagnostic shows what you know, and what you need to work on. I remember the last diagnostic I took. It was hard. The diagnostic will feel challenging. You may see questions you may not know how to answer because you haven’t learned them. There were some questions I knew, and some questions I didn’t know. But I didn’t give up. I tried my best and moved on. When I finished, I got lessons that were right for me. The diagnostic is not a typical test. Not all students will see the same questions. Every student should expect to get around half the questions correct. That’s okay! Some of my friends rushed, and got lessons that weren’t right for them. They asked me what I did. Here are 5 things I shared with them: 1: I didn’t give up. 2: Some of the questions may seem tricky, but I made sure to read the whole question. 3: Some of the questions I didn’t know the answer to. After thinking hard and working the problem out on a piece of paper, I took my best guess. 4: Before I hit the “Done” button, I checked my answer and made sure it was right. I changed a few of my answers that way. 5: I took my time. Once, I finished really fast but then got put in lessons that weren’t right for me. Warning! Some students rush through and guess without reading the choices. If you do this, you may get lessons that are too easy for you and will be a waste of your time. You may even have to take it again. You might wanna give up or rush. Don’t! If you try your best, you’ll get the right lessons for you.", "The Life and Death of Julius Caesar Shakespeare homepage Julius Caesar Ent sir, be not out with me: yet, if you be out, sir, I can mend you. MARULLUS What meanest thou by that? mend me, thou saucy fellow! Second Commoner Why, sir, cobble you. FLAVIUS Thou art a cobbler, art thou? Second Commoner Truly, sir, all that I live by is with the awl: I meddle with no tradesman's matters, nor women's matters, but with awl. I am, indeed, sir, a surgeon to old shoes; when they are in great danger, I recover them. As proper men as ever trod upon neat's leather have gone upon my handiwork. FLAVIUS But wherefore art not in thy shop today? Why dost thou lead these men about the streets? Second Commoner Truly, sir, to wear out their shoes, to get myself into more work. But, indeed, sir, we make holiday, to see Caesar and to rejoice in his triumph. MARULLUS Wherefore rejoice? What conquest brings he home? What tributaries follow him to Rome, To grace in captive bonds his chariot-wheels? You blocks, you stones, you worse than senseless things! O you hard hearts, you cruel men of Rome, Knew you not Pompey? Many a time and oft Have you climb'd up to walls and battlements, To towers and windows, yea, to chimney-tops, Your infants in your arms, and there have sat The livelong day, with patient expectation, To see great Pompey pass the streets of Rome: And when you saw his chariot but appear, Have you not made an universal shout, That Tiber trembled underneath her banks, To hear the replication of your sounds Made in her concave shores? And do you now put on your best attire? And do you now cull out a holiday? And do you now strew flowers in his way That comes in triumph over Pompey's blood? Be gone! Run to your houses, fall upon your knees, Pray to the gods to intermit the plague That needs must light on this ingratitude. FLAVIUS Go, go, good countrymen, and, for this fault, Assemble all the poor men of your sort; Draw them to Tiber banks, and weep your tears Into the channel, till the lowest stream Do kiss the most exalted shores of all. Exeunt all the Commoners See whether their basest metal be not moved; They vanish tongue-tied in their guiltiness. Go you down that way towards the Capitol; This way will I disrobe the images, If you do find them deck'd with ceremonies. MARULLUS May we do so? You know it is the feast of Lupercal. FLAVIUS It is no matter; let no images Be hung with Caesar's trophies. I'll about, And drive away the vulgar from the streets: So do you too, where you perceive them thick. These growing feathers pluck'd from Caesar's wing Will make him fly an ordinary pitch, Who else would soar above the view of men And keep us all in servile fearfulness. Now could I, Casca, name to thee a man Most like this dreadful night, That thunders, lightens, opens graves, and roars As doth the lion in the Capitol, A man no mightier than thyself or me In personal action, yet prodigious grown And fearful, as these strange eruptions are. CASCA 'Tis Caesar that you mean; is it not, Cassius? CASSIUS Let it be who it is: for Romans now Have thews and limbs like to their ancestors; But, woe the while! our fathers' minds are dead, And we are govern'd with our mothers' spirits; Our yoke and sufferance show us womanish. CASCA Indeed, they say the senators tomorrow Mean to establish Caesar as a king; And he shall wear his crown by sea and land, In every place, save here in Italy. CASSIUS I know where I will wear this dagger then; Cassius from bondage will deliver Cassius: Therein, ye gods, you make the weak most strong; Therein, ye gods, you tyrants do defeat: Nor stony tower, nor walls of beaten brass, Nor airless dungeon, nor strong links of iron, Can be retentive to the strength of spirit; But life, being weary of these worldly bars, Never lacks power to dismiss itself. If I know this, know all the world besides, That part of tyranny that I do bear I can shake off at pleasure. Thunder still CASCA So can I: So every bondman in his own hand bears The power to cancel his captivity. CASSIUS And why should Caesar be a tyrant then? Poor man! I know he would not be a wolf, But that he sees the Romans are but sheep: He were no lion, were not Romans hinds. Those that with haste will make a mighty fire Begin it with weak straws: what trash is Rome, What rubbish and what offal, when it serves For the base matter to illuminate So vile a thing as Caesar! But, O grief, Where hast thou led me? I perhaps speak this Before a willing bondman; then I know My answer must be made. But I am arm'd, And dangers are to me indifferent. CASCA You speak to Casca, and to such a man That is no fleering tell-tale. Hold, my hand: Be factious for redress of all these griefs, And I will set this foot of mine as far As who goes farthest. CASSIUS There's a bargain made. Now know you, Casca, I have moved already Some certain of the noblest-minded Romans To undergo with me an enterprise Of honourable-dangerous consequence; And I do know, by this, they stay for me In Pompey's porch: for now, this fearful night, There is no stir or walking in the streets; And the complexion of the element In favour's like the work we have in hand, Most bloody, fiery, and most terrible. CASCA Stand close awhile, for here comes one in haste. CASSIUS 'Tis Cinna; I do know him by his gait; He is a friend. Enter CINNA Cinna, where haste you so? CINNA To find out you. Who's that? Metellus Cimber? CASSIUS No, it is Casca; one incorporate To our attempts. Am I not stay'd for, Cinna? CINNA I am glad on 't. What a fearful night is this! There's two or three of us have seen strange sights.", "What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.", ":)", "We're no strangers to loveYou know the rules and so do IA full commitment's what I'm thinking ofYou wouldn't get this from any other guyI just wanna tell you how I'm feelingGotta make you understandNever gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt youWe've known each other for so longYour heart's been aching, but you're too shy to say itInside, we both know what's been going onWe know the game and we're gonna play itAnd if you ask me how I'm feelingDon't tell me you're too blind to seeNever gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt youNever gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt you(Ooh, give you up)(Ooh, give you up)Never gonna give, never gonna give(Give you up)Never gonna give, never gonna give(Give you up)We've known each other for so longYour heart's been aching, but you're too shy to say itInside, we both know what's been going onWe know the game and we're gonna play itI just wanna tell you how I'm feelingGotta make you understandNever gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt youNever gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt youNever gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt you"]


def detect_color(frame):
    global typer
    global greens

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    print(typer)

    # Define HSV ranges for yellow, green, and blue (BGR FORMAT!!!)
    yellow_lower = np.array([43, 140, 140])
    yellow_upper = np.array([100, 255, 255])

    green_lower = np.array([48, 187, 73])
    green_upper = np.array([80, 255, 255])

    blue_lower = np.array([109, 90, 90])
    blue_upper = np.array([135, 255, 255])

    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    green_mask = cv2.inRange(hsv, green_lower, green_upper)
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)

    yellow_count = cv2.countNonZero(yellow_mask)
    green_count = cv2.countNonZero(green_mask)
    blue_count = cv2.countNonZero(blue_mask)

    if yellow_count > green_count and yellow_count > blue_count and yellow_count > 500:
        typer += "."
        return "Yellow"
    if yellow_count > 500 and blue_count > 500:
        typer += random.choice(greens)
        return "Both"
    if blue_count > green_count and blue_count > yellow_count and blue_count > 500:
        typer += "-"
        return "Blue"
    return "None"

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Unable to open webcam")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        color = detect_color(frame)
        cv2.putText(frame, f"Detected: {color}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("W.W.K Webcam", frame)

        key = cv2.waitKey(1) & 0xFF

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()