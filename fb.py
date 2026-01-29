import requests

ACCESS_TOKEN = "YOUR_USER_ACCESS_TOKEN"
BASE_URL = "https://graph.facebook.com/v19.0"

def get_user_details():
    url = f"{BASE_URL}/me"
    params = {
        "fields": "id,name",
        "access_token": ACCESS_TOKEN
    }
    return requests.get(url, params=params).json()

def get_liked_pages():
    url = f"{BASE_URL}/me/likes"
    params = {
        "access_token": ACCESS_TOKEN
    }
    return requests.get(url, params=params).json()

def get_user_posts():
    url = f"{BASE_URL}/me/posts"
    params = {
        "access_token": ACCESS_TOKEN
    }
    return requests.get(url, params=params).json()

def get_post_comments(post_id):
    url = f"{BASE_URL}/{post_id}/comments"
    params = {
        "access_token": ACCESS_TOKEN
    }
    return requests.get(url, params=params).json()

# -------- MAIN EXECUTION --------
if __name__ == "__main__":

    print("\n--- USER DETAILS ---")
    user = get_user_details()
    print(user)

    print("\n--- PAGES LIKED BY USER ---")
    pages = get_liked_pages()
    print(pages)

    print("\n--- USER POSTS ---")
    posts = get_user_posts()
    print(posts)

    # Fetch comments from first post (if available)
    if "data" in posts and len(posts["data"]) > 0:
        first_post_id = posts["data"][0]["id"]
        print(f"\n--- COMMENTS ON POST {first_post_id} ---")
        comments = get_post_comments(first_post_id)
        print(comments)
    else:
        print("\nNo posts found.")
