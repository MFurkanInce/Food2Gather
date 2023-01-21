class Food2GatherAI:
    def __init__(self):
        self.name = "Food2GatherAIBot"

    def run_model(self, input, db):

        for pic in db.pics:
            if input == pic:
                return input
            else:
                return "Could not find pic"

        # Sadece olusturulan yapay sinir agi kismi alt tarafta gosterilmistir.
        # Kodlarin tamamina Food2Gather.ipynb dosyasindan erisebilirsiniz

        """
        model = Sequential([
            data_augmentation,
            layers.Rescaling(1. / 255),

            # 1. Katman
            layers.Conv2D(128, 3, padding='same', activation='relu'),
            # layers.BatchNormalization(),
            layers.MaxPooling2D(),

            # 2. Katman
            layers.Conv2D(128, 3, padding='same', activation='relu'),
            # layers.BatchNormalization(),
            layers.MaxPooling2D(),

            # 3. Katman
            layers.Conv2D(64, 3, padding='same', activation='relu'),
            # layers.BatchNormalization(),
            layers.MaxPooling2D(),

            # 4. Katman
            # layers.Conv2D(32, 3, padding='same', activation='relu'),
            # layers.BatchNormalization(),
            # layers.MaxPooling2D(),

            # 5. Katman
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            # layers.BatchNormalization(),
            layers.MaxPooling2D(),
            layers.Dropout(0.5),

            # 6. Katman
            layers.Flatten(),
            layers.Dense(17, activation='softmax'),
            layers.Dense(num_classes)
        ])
        """

        return print('Finded recipe')
