#!/usr/bin/env python3

fo = open("writing.txt", "w")
fo.write("Uma linha.\n")
fo.write("Segunda linha.\n")
fo.write("Terceira linha" + " tem texto adicional\n")
alguma_var = 5
fo.write("Quarta linha tem " + str(alguma_var) + " palavras\n")
fo.close()
