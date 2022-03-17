def main():
    text = 'cnn.com'
    print(get_string(text))

def get_string(text):
    if text.endswith('.com'):
        val = True
    else:
        val = False
    return val
main()