from agent import ActionSpace

class Enviornment:
    def __init__(self, tickers, target, data, min_acc=0.485, n_features=10):
        self.tickers = tickers
        self.target = target 
        self.min_acc = min_acc
        self.n_features = n_features
        self.data = data
        self.action_space = ActionSpace()

    def reset(self):
        self.bar = self.n_features
        self.total_reward = 0
        state = self.data_.drop(columns=[self.target]).iloc[
            self.bar - self.n_features:self.bar
        ].values
        return state, {}
    
    def step(self, action):
        if action == self.data['trend'].iloc[self.bar]:
            correct = True
        else:
            correct = False
        
        reward = 1 if correct else 0
        self.total_reward += reward

        self.bar += 1
        self.acc = self.total_reward / (self.bar - self.n_features)

        if self.bar >= len(self.data):
            done = True
        elif reward == 1:
            done = False
        elif (self.acc < self.min_acc) and (self.bar > 20):
            done = True
        else:
            done = False
        
        next_state = self.data_.drop(columns=[self.target]).iloc[
            self.bar - self.n_features:self.bar
        ].values
        return next_state, reward, done, False, {}
