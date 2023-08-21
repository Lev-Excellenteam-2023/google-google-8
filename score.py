
def score_completion(user_input: str, correction: str) -> int:
    """
    The function receives the input from the user and the completion that was find and scores the match.
    :param user_input: The string the user entered.
    :param correction: The completion option that was found.
    :return: The completion score.
    """
    if correction.startswith(user_input):
        return len(user_input) * 2

    i = 0
    while i < len(user_input) and i < len(correction) and user_input[i] == correction[i]:
        i += 1
    mistake_pos = i

    # Diff mistake type
    if len(user_input) == len(correction):
        return 2 * (len(user_input) - 1) - (5 - min(mistake_pos, 4))

    # Extra mistake type
    if len(user_input) > len(correction):
        return 2 * len(correction) - 2 * (5 - min(mistake_pos, 4))

    # Missing mistake type
    if len(user_input) < len(correction):
        return 2 * len(user_input) - 2 * (5 - min(mistake_pos, 4))
