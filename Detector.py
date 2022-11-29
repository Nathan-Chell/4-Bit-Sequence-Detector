#4bit sequence detector to identify a given sequence from an input string
#Detect 1011
#Input string 1010 1011 0011 0110
#Output string 0000 0001 0000 0010

def Detector(input_str):

    for i in range(len(input_str)):
        



def main():
    input_str = "1010101100110110"

    output = Detector(input_str)

    print("{}".format(output))

if __name__ == '__main__':
    main()
