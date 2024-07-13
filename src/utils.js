export const suits = ['?', '♦', '♣', '♥', '♠'];
export const ranks = ['?', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'];
export const getCardInfo = card => {
    return ranks[card.rank] + suits[card.suit];
}