def kelly_criterion(win_prob, win_loss_ratio):
    return (win_prob * (win_loss_ratio + 1) - 1) / win_loss_ratio
