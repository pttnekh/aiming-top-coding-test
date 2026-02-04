def solution(bandage, health, attacks):
    
    t,x,y = bandage
    max_hp = health
    hp = health
    streak = 0
    
    damage_at = {at: dmg for at, dmg in attacks}
    last = attacks[-1][0]
    
    for time in range(1, last + 1):
        if time in damage_at:
            hp -= damage_at[time]
            streak = 0 
            if hp <= 0:
                return -1
            
            continue
            
        hp = min(max_hp, hp + x)
        streak += 1
        
        if streak == t:
            hp = min(max_hp, hp + y)
            streak = 0

    return hp