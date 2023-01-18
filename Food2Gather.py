class Food2GatherAI:
    def __init__(self):
        self.name = "Food2GatherAIBot"

    def run_model(self, input, db):

        # do something
        for pic in db.pics:
            if input == pic:
                return input
            else:
                return "Could not find pic"

        return print('Finded recipe')
