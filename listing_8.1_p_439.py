#program chect, if letter 't' appers in entered text
def main():
    count = 0
    sent = input('Enter the sentence.')
    for ch in sent:
        if ch == 't' or ch == 'T':
            count += 1
    print('Letter "t" occures', count,'times in the entered text.')

main()