import wikiquotes
import os.path
#from random import randrange

class Quotes:

    def __init__(self):
        self.saved_quotes = []
        self.filename = ""

    def export(self, quotes, filename):
        #fname = filename
        
        if filename[-4:] == ".txt":
            filename = filename
        else:
            filename = filename+".txt"
        
        if os.path.isfile(filename) == True:
            with open(filename, "a") as output:
                output.write(str(quotes))
                output.close()
        elif os.path.isfile(filename) == False:
            with open(filename, "w") as output:
                output.write(str(quotes))
                output.close()
        else:
            return False

    def main(self):

        while True:
            start = input(str("Retrieve new quote (y)/(n): "))
            if start == "y":
                quote = wikiquotes.random_quote("Marcus Aurelius", "english")
                print(quote)
                save = input(str("Save quote? (y)/(n): "))
                if save == "y":
                    self.saved_quotes.append(quote)
                    print(self.saved_quotes)
                    export = input(str("Export saved quotes? (y)/(n): "))
                    if export == "y":
                        if self.filename == "":
                            self.filename = input(str("Enter filename: "))
                            self.export(self.saved_quotes, self.filename)
                        else:
                            self.export(self.saved_quotes, self.filename)
            elif start == "n":
                print("Exiting...")
                break
            else:
                print("I don't understand..")
            


if __name__ == "__main__":
    quote = Quotes()
    quote.main()
