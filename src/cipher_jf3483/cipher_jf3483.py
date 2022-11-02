def cipher(text, shift, encrypt=True):
    """
    for decrypt or encrypt the combination of some centain alphabets

    input: 
    -------------
    text is a string, contains alphabet from aA-zZ
    shift is interger
    encryt is boolean; ture-encryt false-decrypt
    
    output:
    ------------
    the output is a string accoridng to what inputs are

    Examples
    --------
    >>> from cipher import cipher
    >>> cipher('QMSS', shift = 1)
    'RNTT'
    >>> cipher('QMSS', shift = -1)
    'PLRR'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
