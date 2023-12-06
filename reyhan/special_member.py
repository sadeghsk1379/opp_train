from member import Member


class Special_member(Member):
    def __init__(self, discount_rate, *args, **kwargs):
        self.discount_rate = discount_rate
        super().__init__(*args, **kwargs)

    def apply_discount(self, discount):
        self.discount_rate = discount
