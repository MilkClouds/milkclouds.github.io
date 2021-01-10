---
layout: post
title: 'DQN(Deep Q-Networks)'
author: MilkClouds
comments: true
date: 2019-05-25 0:18
tags: [python]

---


### 계기  
오늘 5월 동아리 보고서를 동아리 부원들에게서 제출받았다. 근데 모 친구가 "딥러닝과 강화학습을 이용하여 게임속에서 스스로 플레이하는 인공지능AI을 구현해보자"을 주제로 보고서를 제출했다. 원래 작년 "SVM vs FC vs CNN 모델을 이용한 사람 표정 인식"을 주제로 발표 했었기 때문에 CNN에 대해서 조잡하게나마 알고 있었고 강화 학습에 대해서는 딱히 아는 바가 많지 않았는데 강화 학습에서도 CNN을 적극적으로 활용하는 것이 신기해서 글을 쓰게 됐다. 관심을 갖게 된 계기가 되는 소스는 [뱀 게임 DQN GitHub](https://github.com/YuriyGuts/snake-ai-reinforcement)에 있다.  

이 글은 전문적으로 머신러닝에 대해 알지 못하는 학생이 쓴 글이기 때문에 사소한 표현이나 용어에 있어서 부정확한 면이 있을 수 있다. 그리고 CNN에 대한 기본적인 지식이 있어야 이해가 편할 것이다.


### 개요  
DQN이라는 개념은 DeepMind의 ["Playing Atari with Deep Reinforcement Learning"](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf)이라는 논문에서 소개되었다고 한다.  

### DQN  
DQN(Deep Q-Networks)는 Convolutional Network을 이용하여 Learning하는 방법을 말하고, 근데 이름이 왜 DQN인지는 모르겠는데 좀 궁금하다. 기본적으로 게임이 진행되는 도중 한 상태는 모니터에 표시되는 게임은 대부분 2차원 데이터로 표현할 수 있다. 그리고 2D Convolutional Layer은 2차원 데이터를 입력으로 받아 Convolution 연산이 시행된 2차원 데이터를 출력으로 뱉는다. 그리고 그 2차원 데이터를 Flatten하여 1차원 데이터로 만들고 FC Layer(Dense Layer)으로 넣어줘서 적절한 결과값을 출력할 수 있다.  

쉽게 간단하게 표현하면, 이미지 인식의 원리는 이미지를 입력으로 넣고 이미지가 뭘 말하는지 텍스트(정확히는 확률이겠지만)를 출력으로 뱉는다. 게임에 CNN을 쓰려면, 게임하다 모니터 위에 표시되는 현재 상태를 입력으로 넣고 입력해야 될 keystroke을 출력으로 뱉으면 된다.


### DQN 학습 방법  

![dqn](/files/dqn.png)   

의사 코드는 위와 같다. 예제 코드로 간략하게 설명하겠다. 다만, 의사 코드에서 state는 sequence of images and action인데 예제 코드에서는 그냥 단일 이미지다.  

[뱀 게임 DQN GitHub](https://github.com/YuriyGuts/snake-ai-reinforcement)에서, `train.py`에서 dqn model과, `snakeai\agent\dqn.py`에서 DeepQNetworkAgent의 내부 메서드인 train을 확인하면 아래와 같다. 소스 코드 전문이 아니기에 세부 내용은 확인하기 힘들 지라도 대략의 맥락은 파악할 수 있을 것이다.  

```python
def create_dqn_model(env, num_last_frames):
    """
    Build a new DQN model to be used for training.
    
    Args:
        env: an instance of Snake environment. 
        num_last_frames: the number of last frames the agent considers as state.

    Returns:
        A compiled DQN model.
    """

    model = Sequential()

    # Convolutions.
    model.add(Conv2D(
        16,
        kernel_size=(3, 3),
        strides=(1, 1),
        data_format='channels_first',
        input_shape=(num_last_frames, ) + env.observation_shape
    ))
    model.add(Activation('relu'))
    model.add(Conv2D(
        32,
        kernel_size=(3, 3),
        strides=(1, 1),
        data_format='channels_first'
    ))
    model.add(Activation('relu'))

    # Dense layers.
    model.add(Flatten())
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(Dense(env.num_actions))

    model.summary()
    model.compile(RMSprop(), 'MSE')

    return model
```
굉장히 간단하다.
Conv-(ReLU)-Conv-(ReLU)-(Flatten)-Dense-(ReLU)-Dense로 구성되어 있다.
모델은 현재 상태를 입력으로 넣으면 적절한 다음 action을 반환해줄 것이다.

```python
def train(self, env, num_episodes=1000, batch_size=50, discount_factor=0.9, checkpoint_freq=None,
              exploration_range=(1.0, 0.1), exploration_phase_size=0.5):
        """
        Train the agent to perform well in the given Snake environment.
        
        Args:
            env:
                an instance of Snake environment.
            num_episodes (int):
                the number of episodes to run during the training.
            batch_size (int):
                the size of the learning sample for experience replay.
            discount_factor (float):
                discount factor (gamma) for computing the value function.
            checkpoint_freq (int):
                the number of episodes after which a new model checkpoint will be created.
            exploration_range (tuple):
                a (max, min) range specifying how the exploration rate should decay over time. 
            exploration_phase_size (float):
                the percentage of the training process at which
                the exploration rate should reach its minimum.
        """

        # Calculate the constant exploration decay speed for each episode.
        max_exploration_rate, min_exploration_rate = exploration_range
        exploration_decay = ((max_exploration_rate - min_exploration_rate) / (num_episodes * exploration_phase_size))
        exploration_rate = max_exploration_rate

        for episode in range(num_episodes):
            # Reset the environment for the new episode.
            timestep = env.new_episode()
            self.begin_episode()
            game_over = False
            loss = 0.0

            # Observe the initial state.
            state = self.get_last_frames(timestep.observation)

            while not game_over:
                if np.random.random() < exploration_rate:
                    # Explore: take a random action.
                    action = np.random.randint(env.num_actions)
                else:
                    # Exploit: take the best known action for this state.
                    q = self.model.predict(state)
                    action = np.argmax(q[0])

                # Act on the environment.
                env.choose_action(action)
                timestep = env.timestep()

                # Remember a new piece of experience.
                reward = timestep.reward
                state_next = self.get_last_frames(timestep.observation)
                game_over = timestep.is_episode_end
                experience_item = [state, action, reward, state_next, game_over]
                self.memory.remember(*experience_item)
                state = state_next

                # Sample a random batch from experience.
                batch = self.memory.get_batch(
                    model=self.model,
                    batch_size=batch_size,
                    discount_factor=discount_factor
                )
                # Learn on the batch.
                if batch:
                    inputs, targets = batch
                    loss += float(self.model.train_on_batch(inputs, targets))

            if checkpoint_freq and (episode % checkpoint_freq) == 0:
                self.model.save(f'dqn-{episode:08d}.model')

            if exploration_rate > min_exploration_rate:
                exploration_rate -= exploration_decay

            summary = 'Episode {:5d}/{:5d} | Loss {:8.4f} | Exploration {:.2f} | ' + \
                      'Fruits {:2d} | Timesteps {:4d} | Total Reward {:4d}'
            print(summary.format(
                episode + 1, num_episodes, loss, exploration_rate,
                env.stats.fruits_eaten, env.stats.timesteps_survived, env.stats.sum_episode_rewards,
            ))

        self.model.save('dqn-final.model')
```


쉽게 설명하면, 기본적으로 게임에서, 하나의 상태에 대해, 두 가지 작업 중 하나를 한다.  
(1) 랜덤으로 다음 action을 선택한다.  
(2) 현재까지 학습된 CNN에 현재 상태를 입력으로 넣어, 나온 출력을 action으로 한다.  

가장 초기에, 모든 작업은 (1)로 진행한다. 그러다가 모델이 학습을 진행됨에 따라, 진행하면서 점점 (1)을 선택하는 확률을 줄여 나가며, (2)를 선택하는 비율을 늘려 나간다.  

구체적으로 학습을 어떻게 하는지는 솔직히 나의 이해도가 높은 편은 아니어서 설명하다가 틀린 점이 나올 것 같아서 생략하겠다. 일단 위처럼 이해만 하고 넘어가도 도움은 될 거라 생각한다.


### DQN 요약  
현재 상태에 대한 정의를 이미지 sequence만을 이용하여 해줄 수 있다. 게임  메모리를 읽어와서, 예를 들면 현재 금전의 상태라던가를 불러와서 상태로 써주는 경우 관련하여 수작업이 필요한데 그런 게 없다.  
전혀 다른 게임에 대해 똑같은 모델(입력 형식, 출력 형식만 좀 수정해서)에 똑같은 상태 정의로 학습이 가능하다. 성능은 차이나겠지만 그래도 가능하다는 점이 좀 굉장하다고 생각한다.  

### 참고  
[https://sumniya.tistory.com/18](https://sumniya.tistory.com/18)