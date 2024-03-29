# -*- coding: utf-8 -*-
"""S&P-project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15W3Nmf_1cE853LBAmUf4jj-cPJOPEOyK
"""

import pandas as pd

information_technology = pd.read_csv("Information_technology.csv")
information_technology.head()

import numpy as np

def read_and_process_data(sector_name_list):
    merged_df = None
    for sector_name in sector_name_list:
        sector_df = pd.read_csv(sector_name+ '.csv')
        sector_df['date'] = pd.to_datetime(sector_df['Date'])
        sector_df[sector_name] = sector_df['Adj Close']
        sector_df.drop(columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'],
                        inplace = True)

        if merged_df is None:
            merged_df = sector_df
        else:
            merged_df = merged_df.merge(sector_df, how = 'inner', on = 'date')
    merged_df.set_index('date', inplace = True)
    merged_df.dropna(inplace = True)
    return np.round((merged_df - merged_df.mean())/merged_df.std(), 1)


df = read_and_process_data(['Information_technology'])
df.head()

print(df.describe());

states = set()
for row in df.iterrows():
    new_state = []
    for c in row[1].items():
        new_state.append(c[1])
    states.add(tuple(new_state))

index = pd.MultiIndex.from_tuples(list(states), names=["Information_technology"])
policy = pd.DataFrame(0, index = index, columns = ['buy_buy', 'buy_sell', 'sell_sell', 'sell_buy'])
policy = policy.sort_index()
policy.head()

import random

def find_action(policy, current_value):
    if policy.loc[current_value, :].sum().sum() == 0:
        return random.choice(['buy_buy', 'buy_sell', 'sell_sell', 'sell_buy'])

    return policy.columns[np.argmax(policy.loc[current_value, :].values)]

def update_policy(reward, current_state_value, action):
    LEARNING_RATE = 0.1
    MAX_REWARD = 10
    DISCOUNT_FACTOR = 0.05

    return LEARNING_RATE * (reward + DISCOUNT_FACTOR * MAX_REWARD - policy.loc[current_state_value, action])

past_state_value = (0, 0)
past_action = 'buy_buy'
total_reward = 0
rewards = []

for idx, row in df.iterrows():
    current_state_value = (row['Information_technology'])
    action = find_action(policy, current_state_value)

    if past_action == 'buy_buy':
        reward = current_state_value - past_state_value[0]
        reward += current_state_value - past_state_value[1]
    elif past_action == 'buy_sell':
        reward = current_state_value - past_state_value[0]
        reward += past_state_value[1] - current_state_value
    elif past_action == 'sell_sell':
        reward = past_state_value[0] - current_state_value
        reward += past_state_value[1] - current_state_value
    else:
        reward = past_state_value[0] - current_state_value
        reward += current_state_value - past_state_value[1]

    total_reward += float(reward)
    policy.loc[current_state_value, action] += update_policy(reward, current_state_value, action)


    rewards.append(total_reward)
    past_actions = current_state_value

import matplotlib.pyplot as plt
plt.plot(rewards)
plt.title('Reward vs Iteration')
plt.xlabel('Iteration Number in Training')
plt.ylabel('Reward');

import seaborn as sns
sns.heatmap(policy.sort_index())
plt.title('Heat Map of Rewards for Policy - Action Pairs')
plt.xlabel('Action');

positively_reinforced = policy[policy > 0]
positively_reinforced.describe()

negatively_reinforced = policy[policy < 0]
negatively_reinforced.describe()

import networkx as nx
from networkx.algorithms import bipartite

G = nx.Graph()
G.add_nodes_from(policy.index.values, bipartite=0)
G.add_nodes_from(policy.columns.values,bipartite=1)

edges = []
for i, row in policy.iterrows():
    row = row.values
    max_idx = np.argmax(row)
    amax = row[max_idx]
    if amax >= 1.4:
        edges.append((i, policy.columns[max_idx]))

G.add_edges_from(edges)
nx.draw_networkx(G, pos = nx.drawing.layout.bipartite_layout(G, policy.index.values), width = 2)

for edge in G.edges(['sell_sell']):
    print(edge)

for edge in G.edges(['sell_buy']):
    print(edge)

for edge in G.edges(['sell_buy']):
    print(edge)

for edge in G.edges(['buy_sell']):
    print(edge)

for edge in G.edges(['buy_buy']):
    print(edge)