def enc_alphabet(txt):
    d = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
             "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
             "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
             "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
             "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
             " ": "....."}
    dec_alphabet = {v: k for k, v in d.items()}


    if '-' in txt:
        return ''.join(dec_alphabet[i] for i in txt.split())
    return ' '.join(d[i] for i in txt.upper())


print(enc_alphabet('python'))
# .--. -.-- - .... --- -.
print(enc_alphabet('.--. -.-- - .... --- -.'))
# PYTHON