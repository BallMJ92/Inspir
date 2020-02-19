import wikiquotes
import os.path
from random import randrange

class Quotes:

    def __init__(self):
        self.authors = []
        self.saved_quotes = []
        self.filename = ""

    def export(self, quotes, filename):
        #fname = filename
        
        if filename[-4:] == ".txt":
            filename = filename
        else:
            filename = filename+".txt"

            
        with open(filename, "w") as output:
            output.write(str(quotes))
            output.close()

    def main(self):
        
        while True:
            author = input(str("Who are your favourite quote authors? "))
            if len(author) != 0:
                self.authors.append(author)
                cont = input(str("Do you want to add any more authors (y)/(n): "))
                if cont == "n":
                    break
            else:
                print("Sorry I didn't catch that..")

        print("\nLets move onto getting some quotes..\n")
        
             
        while True:
            rand_author = self.authors[randrange(len(self.authors))]
            ret_quote = input(str("Retrieve new quote (y)/(n): "))
            if ret_quote == "y":
                quote = wikiquotes.random_quote(rand_author, "english")
                print(rand_author+" : "+quote)
                save = input(str("Save quote? (y)/(n): "))
                if save == "y":
                    self.saved_quotes.append(rand_author+" : "+quote)
                    print(self.saved_quotes)
                    export = input(str("Export saved quotes? (y)/(n): "))
                    if export == "y":
                        if self.filename == "":
                            self.filename = input(str("Enter filename: "))
                            self.export(self.saved_quotes, self.filename)
                        else:
                            self.export(self.saved_quotes, self.filename)
            elif ret_quote == "n":
                print("Exiting...")
                break
            else:
                print("I don't understand..")
            


if __name__ == "__main__":
    quote = Quotes()
    quote.main()
