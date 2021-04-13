__author__ = "Szilveszter Rafael Szabo"
__version__ = "1.0.0"
__email__ = "ssrofficial@gmail.com"
__neptun__ = "YTBR1C"

def encoding_string(string,shift):
    """Returns an encoded string by shifting characters from a given string.

    Keyword arguments: 
    string -- the string for encode 
    shift -- the value of character shifting
    """

    encoded_string = []
    
    #Encoding string 
    for i,j in enumerate(string):
        encoded_char = ord(string[i])+shift
        encoded_string.append(chr(encoded_char))

    return encoded_string


def decoding_string(string,shift):
    """Returns decoded string by shifting characters from the encoded string.

    Keyword arguments: 
    string -- the string for decode 
    shift -- the value of character shifting
    """
    decoded_string = []
    
    #Decoding string
    for i,j in enumerate(string):
        decoded_char = ord(string[i])-shift
        decoded_string.append(chr(decoded_char))

    return decoded_string


def main():
    #Print metadata
    print("Author: " + __author__)
    print("Neptun: " + __neptun__)
    print("Version: " + __version__)
    print("E-mail: " + __email__)

    #Input
    give_string = input("\nGive a string for encoding: ")

    #Value for shifting characters
    shift = 12

    #Encoding
    encoded_string = encoding_string(give_string,shift)
    print("\nThe encoded string is: " + str(encoded_string))

    #Decoding
    decoded_string = decoding_string(encoded_string,shift)
    print("\nThe decoded string is: " + str(decoded_string) + "\n")



if __name__ == "__main__":
    main()


