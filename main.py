import wikiquotes
#from random import randrange

class Quotes:

    def __init__(self):
        self.saved_quotes = []

    def export(self, quotes):
        with open("quotes.txt", "a") as output:
            output.write(str(quotes))
            output.close()

    def main(self):

        while True:
            start =input(str("Retrieve new quote (y)/(n): "))
            if start == "y":
                quote = wikiquotes.random_quote("Marcus Aurelius", "english")
                print(quote)
                save = input(str("Save quote? (y)/(n): "))
                if save == "y":
                    self.saved_quotes.append(quote)
                    print(self.saved_quotes)
                    export = input(str("Export saved quotes? (y)/(n): "))
                    if export == "y":
                        self.export(self.saved_quotes)
            elif start == "n":
                print("Exiting...")
                break
            else:
                print("I don't understand..")
            


if __name__ == "__main__":
    quote = Quotes()
    quote.main()
