
from matplotlib import pyplot as plt

def birthday_probability(num_people, space_size):
    """
    计算生日悖论中，num_people个'生日'（或其他对象）碰撞的概率。
    
    参数:
    - num_people: 总共的输入数量（例如，字符串数量、对象数量等）
    - space_size: 总的可能值的数量（例如，哈希值的大小或输出空间）
    
    返回:
    - 碰撞的概率（在0到1之间）
    """
    if num_people > space_size:
        return 1.0  # 如果人数超过了空间大小，碰撞的概率是100%

    prob_no_collision = 1.0
    for i in range(num_people):
        prob_no_collision *= (space_size - i) / space_size

    prob_collision = 1 - prob_no_collision
    return prob_collision



list = []
num_people = 1
space_size = 65536  # 输出空间为 65536 种可能值（16 位整数）
while True:
  collision_probability = birthday_probability(num_people, space_size)
  if collision_probability > 0.5 and list[-1] < 0.5:
    print(f"当有 {num_people} 个人时，碰撞的概率超过 50%")
  if collision_probability > 0.99:
    print(f"当有 {num_people} 个人时，碰撞的概率超过 99%")
    break
  list.append(collision_probability)
  num_people += 1
  
plt.plot(range(1, num_people), list)
plt.xlabel('Times of generation')
plt.ylabel('Probability of collision')
plt.title('birthday paradox')
plt.savefig('birthday.png', dpi = 1080, bbox_inches='tight')