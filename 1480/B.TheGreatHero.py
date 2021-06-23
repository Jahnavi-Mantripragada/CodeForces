def GreatHeroKillsMonsters(attack_power, hero_health, n, power, health):
    health.sort(reverse=True)
    for i in range(n):
        h = health[i]
        a = power[i]
        x = 0
        if h % attack_power != 0:
            r = health[i] % attack_power
            x = (h + (attack_power - r)) // attack_power
        else:
            x = h // attack_power
        if hero_health % a != 0:
            r = hero_health % a
            x = min(x, (hero_health + (a - r)) // a)
        else:
            x = min(x, hero_health // a)
        hero_health -= x * a
        health[i] -= x * attack_power
        if hero_health <= 0 and health[i] > 0:
            return False
        if hero_health <= 0 and i != n-1:
            return False
    # print(health, hero_health)
    return all([h <= 0 for h in health])


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        A, B, n = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        if GreatHeroKillsMonsters(A, B, n, a, b):
            print("YES")
        else:
            print("NO")
