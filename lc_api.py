import requests

def get_leetcode_daily_question():
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
        
    query = {
        "query": """
        query {
            activeDailyCodingChallengeQuestion {
                question {
                    questionFrontendId
                    title
                    titleSlug
                    difficulty
                }
            }
        }
        """
    }

    response = requests.post(url, json=query, headers=headers)
    
    try: 
        if response.status_code == 200:
            data = response.json()
            if "data" in data and "activeDailyCodingChallengeQuestion" in data["data"]:
                question = data["data"]["activeDailyCodingChallengeQuestion"]["question"]

                return {
                    "id": question["questionFrontendId"],
                    "title": question["title"],
                    "slug": question["titleSlug"],
                    "difficulty": question["difficulty"],
                    "link": f"https://leetcode.com/problems/{question['titleSlug']}"
                }
        
    except:
        Exception(response.status_code)
        return None

if __name__ == "__main__":
    daily_question = get_leetcode_daily_question()
    print(daily_question["id"])