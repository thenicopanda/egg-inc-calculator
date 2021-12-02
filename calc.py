def human_format(number):
    units = ['', 'k', 'm', 'b', 'T', 'q', 'Q', 's', 'S', 'o', 'N', 'd', 'U', 'D', 'Td', 'qd', 'Qd', 'sd', 'Sd', 'Od', 'Nd', 'V', 'uV', 'dV', 'tV', 'qV', 'sV', 'SV', 'OV', 'NV', 'tT']
    k = Decimal(1000.0)
    magnitude = int(floor(log(number, k)))
    return '%.3f%s' % (number / k**magnitude, units[magnitude])

def calculateEB(soulEggs: str, prophecyEggs: Decimal, prophecyBonus: Decimal, soulFood: Decimal, human: bool):
    if soulEggs.endswith("k"):
        soulEggs = (soulEggs[:-1]) 
        soulEggs = soulEggs * 1000    
    elif soulEggs.endswith("m"):
        soulEggs = Decimal(soulEggs[:-1]) 
        soulEggs = soulEggs * 1000000
    elif soulEggs.endswith("b"):
        soulEggs = Decimal(soulEggs[:-1]) 
        soulEggs = soulEggs * 1000000000
    elif soulEggs.endswith('t'):
        soulEggs = Decimal(soulEggs[:-1]) 
        soulEggs = soulEggs * 1000000000000
    elif soulEggs.endswith('q'):
        soulEggs = Decimal(soulEggs[:-1]) 
        soulEggs = soulEggs * 1000000000000000
    elif soulEggs.endswith('Q'):
        soulEggs = Decimal(soulEggs[:-1]) 
        soulEggs = soulEggs * 1000000000000000000
    elif soulEggs.endswith('s'):
        soulEggs = Decimal(soulEggs[:-1]) 
        soulEggs = soulEggs * 1000000000000000000000
    elif soulEggs.endswith('S'):
        soulEggs = Decimal(soulEggs[:-1]) 
        soulEggs = soulEggs * 1000000000000000000000000        
    else:
        soulEggs = Decimal(soulEggs)
    try:
        prophecyEggBonus = (1 + 0.05 + (0.01 * prophecyBonus))**prophecyEggs * (10 + soulFood)
        EB = Decimal(prophecyEggBonus) * soulEggs
        if human == True:
            EB = human_format(EB)
        return EB
    except:
        return False
