from dlpf.base_utils import *
import gym
from dlpf.agents import DqnAgent, RandomAgent
from dlpf.io import *

logger = init_log(out_file = 'import.log', stderr = False)
import_tasks_from_xml_to_compact('data/sample/raw/', 'data/sample/imported/')

logger = init_log(out_file = 'testbed.log', stderr = False)


env = gym.make('PathFindingByPixel-v1')
env.configure(tasks_dir = os.path.abspath('data/sample/imported/'), monitor_scale = 10, map_shape = (10, 10))
env.monitor.start('data/sample/results/basic_dqn', force=True, seed=0)
agent = DqnAgent(state_size = env.observation_space.shape,
                 number_of_actions = env.action_space.n,
                 save_name = env.__class__.__name__)
agent.build_model()

episode_count = 15000
max_steps = 100

for _ in xrange(episode_count):
    observation = env.reset()
    agent.new_episode()
    for __ in range(max_steps):
        action, values = agent.act(observation, env.cur_position_discrete, epsilon=0.05+0.95*0.999**(_))
        observation, reward, done, info = env.step(action)
        agent.observe(reward, action, env.cur_position_discrete)
        if done:
            break
    if _ % 100 == 99:
        print 'iteration:', _ + 1
        agent.plot_layers(to_save='iteration'+str(_+1))
    if _ % 10 == 9:
        agent.train_with_full_experience(_ - 999)