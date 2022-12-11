def get_winners(results):
    results_dict = {}
    
    for winner_result in enumerate(results): 
        results_dict[winner_result[0]+1]  = winner_result[1]
   
    sorted_results_dict = sorted(results_dict, key=results_dict.get)
    return (list(reversed(sorted_results_dict))[:3])
   
#result = get_winners([115, 352, 0, 310, 500])
result = get_winners([110, 450, 600, 310, 500])
print(result)
