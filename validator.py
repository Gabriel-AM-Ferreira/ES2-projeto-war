from constants import CORINGA

def is_valid_exchange(self, cards_to_exchange):
    if len(cards_to_exchange) != 3:
        return False
    if self.same_symbol(cards_to_exchange):
        return True
    if self.diff_symbols(cards_to_exchange):
        return True
    return False

def same_symbol(self, cards_to_exchange):
    symbols = []
    for card in cards_to_exchange:
        if card.symbol != CORINGA:
            symbols.append(card.symbol)
    if len(set(symbols)) == 1:
        return True
    return False

def diff_symbols(self, cards_to_exchange):
    num_coringas = 0
    symbols = []
    for card in cards_to_exchange:
        if card.symbol == CORINGA:
            num_coringas += 1
        else:
            symbols.append(card.symbol)
    if len(set(symbols)) + num_coringas == 3:
        return True
    return False