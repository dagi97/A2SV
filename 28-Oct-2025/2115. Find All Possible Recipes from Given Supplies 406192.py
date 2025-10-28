# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        from collections import defaultdict, deque
 
        graph = defaultdict(list)
        indegree = {}
        
        
        for i, recipe in enumerate(recipes):
            indegree[recipe] = len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(recipe)
         
        queue = deque(supplies)
        made = set(supplies)
        result = []
        
        while queue:
            item = queue.popleft()
            
            for recipe in graph[item]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)
                    made.add(recipe)
        
        return result

        