> 프로그래머스 인공지능 데브코스 6기 강화학습 스터디  
[[Open AI spinning up] Introduction to RL - Part 1: Key Concepts in RL]([https://spinningup.openai.com/en/latest/spinningup/rl_intro.html](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html))

# Part 1: Key Concepts in RL


강화학습은 agent가 주어진 환경(environment)에서 어떻게 시행착오(trial and error)를 통해 학습하는지에 대한 연구이다.

## Key Concepts and Terminology

![에이전트-환경 상호작용 루프](https://spinningup.openai.com/en/latest/_images/rl_diagram_transparent_bg.png)

에이전트-환경 상호작용 루프

강화학습의 주인공은 **에이전트**(agent)와 **환경**(environment)이다. 환경은 에이전트가 살고 상호작용하는 세계이다. 에이전트는 환경으로부터 **리워드**(reward)를 받는다. 리워드란 현재의 상태가 얼마나 좋고 나쁜지를 알려주는 척도이다. 에이전트의 목표는 누적 리워드 **리턴**(return)을 최대화하는 것이다.

강화학습은 이 목표를 달성할 수 있는 행동을 배우는 방법이다. 

## Terminology

### States and Observations

- **state** *s*: world에 대한 complete description
- **observation** *o*: state에 대한 부분적인 description

→ deep RL에서는 state와 observations를 벡터, 행렬, 고차텐서로 나타낸다.

💡에이전트는 세계에 대한 부분적인 정보를 가지고 행동을 결정하기 때문에 observation를 쓰는 게 더 정확한 상황에서도 일반적으로 state라고 많이 쓴다. 따라서 여기서도 standard convention을 따라 s라고 쓰도록 하겠다.

### Action Spaces

다른 환경들은 각자 다른 종류의 가능한 action이 있다. 주어진 환경에서 가능한 action들의 집합을 **action space**라고 한다.

- discrete action spaces: Atrai, 바둑과 같이 한정된 action이 가능한 경우
- continuous action spaces: 물리적 세계의 로봇을 조종하는 것과 같이 action을 실수 벡터로 표현할 수 있는 경우

### Policies

에이전트가 action을 결정하는 rule을 **policy**라고 한다.

- deterministic (결정적/확정적) : $\mu$를 이용하여 표현
- stochastic (확률적): $\pi$를 이용하여 표현
    
    ![https://spinningup.openai.com/en/latest/_images/math/831f731859658682b2af7e217a76648697c9de46.svg](https://spinningup.openai.com/en/latest/_images/math/831f731859658682b2af7e217a76648697c9de46.svg)
    

*(→ 현재의 상황을 policy 함수에 넣으면 취해야 할 action이 나온다)*

이러한 policy는 우리가 최적화 알고리즘을 통해 동작을 변경할 수 있도록 파라미터에 의존적인 계산 가능한 함수로 다뤄진다. 

**Stochastic Policies**

stochastic policies 중 가장 일반적인 종류로는 discrete action space에서 쓰는 **categorical policies**, continuous action spaces에서 쓰는 **diagonal Gaussian policies**가 있다.

stochastic policy의 key computation 두 가지

1) policy로부터 action을 샘플링하는 것 

2) 특정 action의 log likelihood를 계산하는 것 

### Trajectories

에이전트가 거친 모든 state와 action의 궤적으로, episode, rollout이라고 불리기도 한다.

![https://spinningup.openai.com/en/latest/_images/math/8337d86159a1cd98dfcd0601993d7b6b2fbb54d9.svg](https://spinningup.openai.com/en/latest/_images/math/8337d86159a1cd98dfcd0601993d7b6b2fbb54d9.svg)

$s_0$은 start-state distribution $\rho_0$에 의해 무작위로 샘플링된다. 

![https://spinningup.openai.com/en/latest/_images/math/eef23a6502b9cec4bc399bcbce93547c3723643c.svg](https://spinningup.openai.com/en/latest/_images/math/eef23a6502b9cec4bc399bcbce93547c3723643c.svg)

t에서의 상태 $s_t$에서 t+1의 상태  $s_t+1$로의 state transition은 환경과 가장 최근의 action $a_t$에 의해 결정되며 결정적이거나 확률적으로 결정된다. 

![https://spinningup.openai.com/en/latest/_images/math/16da6346104894fb6a673473cbfc9ffeba6471fa.svg](https://spinningup.openai.com/en/latest/_images/math/16da6346104894fb6a673473cbfc9ffeba6471fa.svg)

![https://spinningup.openai.com/en/latest/_images/math/872390af4f5b2541d17e7ef2bfaecbe1e9746d94.svg](https://spinningup.openai.com/en/latest/_images/math/872390af4f5b2541d17e7ef2bfaecbe1e9746d94.svg)

이 때 에이전트의 action은 policy에 의해 결정된다.

### Reward and Return

리워드함수 R은 현재 state, 방금 한 action, 다음 state에 의존한다. (현재 행동의 보상인듯)

![https://spinningup.openai.com/en/latest/_images/math/6ed565b0911f12c8ef64d93a617d8bb30380d5d5.svg](https://spinningup.openai.com/en/latest/_images/math/6ed565b0911f12c8ef64d93a617d8bb30380d5d5.svg)

에이전트의 목적은 trajectory를 따른 누적 리워드 return을 최대화하는 것이다. return은 두 가지로 나누어진다.

1) finite-horizon undiscounted return

- 특정 기간동안 단순한 리워드의 합

![https://spinningup.openai.com/en/latest/_images/math/b2466507811fc9b9cbe2a0a51fd36034e16f2780.svg](https://spinningup.openai.com/en/latest/_images/math/b2466507811fc9b9cbe2a0a51fd36034e16f2780.svg)

2) infinite-horizon discounted return

- 모든 기간동안의 리워드의 discounted된 합(discount factor와의 가중합)
- discount의 의미는 1) 수렴을 위해 2) 현재의 가치에 더 가중치를 두기 위해

![https://spinningup.openai.com/en/latest/_images/math/bf49428c66c91a45d7b66a432450ee49a3622348.svg](https://spinningup.openai.com/en/latest/_images/math/bf49428c66c91a45d7b66a432450ee49a3622348.svg)

### The RL Problem

강화학습의 목적은 **expected return**을 최대화하는 policy를 찾는 것이다. 

환경 전이와 policy가 모두 확률적(stochastic)한 상황이라고 가정했을 때, T-step trajectory의 확률은 다음과 같이 나타낼 수 있다.

![https://spinningup.openai.com/en/latest/_images/math/69369e7fae3098a2f05a79680fbecbf48a4e7f66.svg](https://spinningup.openai.com/en/latest/_images/math/69369e7fae3098a2f05a79680fbecbf48a4e7f66.svg)

이 때의 expected return 함수는 다음과 같이 각 step에서의 리워드의 기댓값으로 나타낼 수 있다.

![https://spinningup.openai.com/en/latest/_images/math/f0d6e3879540e318df14d2c8b68af828b1b350da.svg](https://spinningup.openai.com/en/latest/_images/math/f0d6e3879540e318df14d2c8b68af828b1b350da.svg)

이 때 강화학습의 중심 최적화 문제(centralized optimization problem)는 다음과 같이 표현할 수 있다.

![https://spinningup.openai.com/en/latest/_images/math/2de61070bf8758d03104b4f15df45c8ff5a86f5a.svg](https://spinningup.openai.com/en/latest/_images/math/2de61070bf8758d03104b4f15df45c8ff5a86f5a.svg)

*(expected return을 최대화하는 policy를 찾는 것)*

이 때의 $\pi^*$를 **optimal policy**라고 한다.

### Value Function

지금 state나 state-action pair에서 시작하여 특정 policy를 따라 이동했을 때의 **expected return**을를 value라고 한다.

- On-policy Value Function
    - 특정 state s에서 어떤 정책 $\pi$를 따라서 끝까지 움직였을 때의 expected return
        
        ![https://spinningup.openai.com/en/latest/_images/math/e043709b46c9aa6811953dabd82461db6308fe19.svg](https://spinningup.openai.com/en/latest/_images/math/e043709b46c9aa6811953dabd82461db6308fe19.svg)
        
- On-Policy Action-Value Function
    - 특정 state s에서 임의의 action a를 시행하고, 그 후 어떤 정책 $\pi$를 따라 끝까지 움직였을 때의 expected return
        
        ![https://spinningup.openai.com/en/latest/_images/math/85d41c8c383a96e1ed34fc66f14abd61b132dd28.svg](https://spinningup.openai.com/en/latest/_images/math/85d41c8c383a96e1ed34fc66f14abd61b132dd28.svg)
        
- Optimal Value Function
    - 특정 state s에서 optimal policy를 따라서 끝까지 움직였을 때의 expected return
        
        ![https://spinningup.openai.com/en/latest/_images/math/01d48ea453ecb7b560ea7d42144ae24422fbd0eb.svg](https://spinningup.openai.com/en/latest/_images/math/01d48ea453ecb7b560ea7d42144ae24422fbd0eb.svg)
        
- Optimal Action-Value Function
    - 특정 state s에서 임의의 action a를 시행하고, 그 후 optimal policy를 따라 끝까지 움직였을 때의 expected return
        
        ![https://spinningup.openai.com/en/latest/_images/math/bc92e8ce1cf0aaa212e144d5ed74e3b115453cb6.svg](https://spinningup.openai.com/en/latest/_images/math/bc92e8ce1cf0aaa212e144d5ed74e3b115453cb6.svg)
        

### The Optimal Q-Function and the Optimal Action

optimal action-value function $Q^*(s,a)$은 state s에서 시작해서 임의의 행동 a를 하고 나서 optimal policy를 따랐을 때의 expected return을 알려준다. 따라서 $Q^*$를 알면 다음과 같이 optimal action $a^*(s)$를 구할 수 있다.

![https://spinningup.openai.com/en/latest/_images/math/42490c4d812c9ca1fc226684577900bc8bdd609b.svg](https://spinningup.openai.com/en/latest/_images/math/42490c4d812c9ca1fc226684577900bc8bdd609b.svg)

### Bellman Equations

벨만 방정식의 기본 아이디어는 **“시작점의 value는 현재 state에서의 리워드와 다음 state에서의 value를 합한 것과 같다”**는 것이다.

![https://spinningup.openai.com/en/latest/_images/math/7e4a2964e190104a669406ca5e1e320a5da8bae0.svg](https://spinningup.openai.com/en/latest/_images/math/7e4a2964e190104a669406ca5e1e320a5da8bae0.svg)

*($s'$는 다음 state를 뜻한다)*

*→ 위에서의 value function을 현재 상태의 리워드 + 다음 상태에서의 value로 나눈 것!*

![https://spinningup.openai.com/en/latest/_images/math/f8ab9b211bc9bb91cde189360051e3bd1f896afa.svg](https://spinningup.openai.com/en/latest/_images/math/f8ab9b211bc9bb91cde189360051e3bd1f896afa.svg)

\* Bellman backup: 벨만 방정식의 우항, 현재 리워드 + 다음 value

### Advantage Functions

강화학습에서는 어떤 action이 절대적으로 얼마나 좋은지보다, 다른 action들에 비해 상대적으로 얼마나 좋은지가 중요할 때가 있다. **advantage function**은 state s에서 policy $\pi$를 따라 특정 action a를 했을 때 $\pi(*|s)$를 따라 랜덤한 action을 했을 때 얼마나 나은지를 보여준다.

![https://spinningup.openai.com/en/latest/_images/math/3748974cc061fb4065fa46dd6271395d59f22040.svg](https://spinningup.openai.com/en/latest/_images/math/3748974cc061fb4065fa46dd6271395d59f22040.svg)

### Formalism

**Markov Decision Processes(MDP)**

MDP는 시스템이 Markov property를 따른다는 것을 뜻한다. 마르코프 속성은 transition이 이전이 아닌, 가장 최근의 state와 action에만 의존한다는 것이다. MDP는 $<S, A, R, P, \rho_0>$라는 5-튜플로 표현된다.

$S$: 가능한 모든 state의 집합

$A$: 가능한 모든 action의 집합

$R$: 리워드 함수

$P$: transition probability function

$\rho_0$: starting state distribution