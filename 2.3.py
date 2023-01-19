def zigzag(sentence, k):
    z = ""
    down = True
    for build_level in range(0, k):
        level = 0
        for c in sentence:
            # Use character if it belongs on this level, otherwise space
            if build_level == level:
                z += c
            else:
                z += " "
            # Set new level and direction
            if down:
                if level < k-1:
                    level+=1
                else:
                    down = False
                    level-=1
            else:
                if level > 0:
                    level-=1
                else:
                    down = True
                    level+=1
        z += "\n"
    return z

s = "thisisazigzag"
k = 4
print(zigzag(s, k))
