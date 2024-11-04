# Please kindly check out the readme file for better experience

import  requests
import  json


def welcome_message():
    print("🎉 Welcome to the Favorite K-dramas Management System! 🎬")
    print("📺 You can get, add, update, or delete dramas in this database. 🤩")
    print("👉 Choose an action to perform: 💡")

def display_menu():
    print("\n📋 Menu:")
    print("1️⃣  Get all dramas")
    print("2️⃣  ➕ Add a new drama")
    print("3️⃣  ✏️  Update an existing drama")
    print("4️⃣  🗑️  Delete a drama")
    print("5️⃣  👋 Leave for now")

# GET ALL DRAMAS
def get_all_dramas():
    try:
        response = requests.get('http://127.0.0.1:5000/dramas')
        print("📡 Status Code:", response.status_code)
        if response.status_code == 200:
            dramas = response.json()
            drama_count = len(dramas)
            print("🎬 The Drama List:")
            for drama in dramas:
                print(json.dumps(drama, indent=4))
            print(f"\n🌟 A total of {drama_count} dramas found! 🌟")
        else:
            print(f"❌ Failed to retrieve dramas. Status code: {response.status_code}")
            print("💔 Error:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error during request: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

# POST REQUEST
def add_drama():
    # Feel free to add your dramas!
    new_drama = {
        "Name": "The Bridal Mask",
        "Year of release": "2012",
        "Aired Date": "May 30, 2012 - Sep 6, 2012",
        "Aired On": "Wednesday, Thursday",
        "Number of Episode": "28",
        "Network": "KBS2",
        "Duration": "1 hr. 5 min.",
        "Content Rating": "15+ - Teens 15 or older",
        "Synopsis": "Lee Kang To is an ambitious and callous Korean officer employed by the Japanese colonists. Despite his mother's disapproval of his work and his own brother's antagonistic history with the Japanese, Kang To continues to play by the colonist's rules in hopes of becoming successful and bringing his family out of poverty. However, a mysterious figure wearing a traditional Bridal Mask always seems to get in Kang To's way. The Bridal Mask appears as a Zorro-like figure who protects the people from the Japanese colonists' oppression and abuse of power. An unexpected turn of events brings Kang To to cross paths with the mysterious Bridal Mask, changing his future and the nation's history forever.",
        "Cast": "Joo Won, Jin Se Yeon, Park Ki Woong, Han Chae Ah, Shin Hyun Joon, Chun Ho Jin",
        "Genre": "Action, Historical, Romance, Political",
        "Tags": "Japanese Colonial Rule, Hidden Identity, Rebellion, Revenge, Love Triangle, Murder, First Love, Adapted From A Manhwa, Investigation, Drama",
        "Rank": "#99",
        "Rating": "8.6"
    }
    headers = {'content-type': 'application/json'}
    try:
        response = requests.post('http://127.0.0.1:5000/dramas', headers=headers, data=json.dumps(new_drama))
        print("📡 Status Code:", response.status_code)

        if response.status_code == 201:
            print("🎉 The drama above added successfully! 🎊✨")
            added_drama = response.json()
            print("➕ Added Drama:")
            print(json.dumps(added_drama, ensure_ascii=False, indent=4))
        else:
            print("❌ Failed to add the drama. Error:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error during request: {e}")
    except json.JSONDecodeError as e:
        print(f"⚠️ Error decoding JSON: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

# PUT REQUEST
def update_drama():
    updated_drama = {
        "New content": "🎉 The information has been updated successfully",
        "Rating": "9.5"
    }
    drama_name = input("✏️ Enter the name of the drama to update, e.g.'Move to Heaven': ")
    headers = {'content-type': 'application/json'}

    try:
        response = requests.put(
            'http://127.0.0.1:5000/dramas/{}'.format(drama_name),
            headers=headers,
            data=json.dumps(updated_drama)
        )
        print("📡 Status Code:", response.status_code)

        if response.status_code == 200:
            print(f"🎉 '{drama_name}' has been successfully updated! 🎊✨")
            updated_data = response.json()
            print("🔄 Updated Drama Info:")
            print(json.dumps(updated_data, ensure_ascii=False, indent=4))
        elif response.status_code == 404:
            print(f"😞 Drama '{drama_name}' not found! 🚫")
        else:
            print(f"❌ Failed to update the drama. Error: {response.status_code}, {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error during request: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

# DELETE REQUEST
def delete_drama():
    # Lets try to delete 'Weak Hero Class 1` from the db
    drama_name = input("✏️ Enter the name of the drama to delete, e.g.'Weak Hero Class 1': ")
    headers = {'content-type': 'application/json'}

    try:
        result = requests.delete(
            'http://127.0.0.1:5000/dramas/{}'.format(drama_name), headers=headers
        )
        if result.status_code == 200:
            print("🎉 Drama deleted successfully! 🎊✨")
            deleted_drama = result.json()
            print("🗑️ Deleted Drama:")
            print(json.dumps(deleted_drama, ensure_ascii=False, indent=4))
        elif result.status_code == 404:
            print("😞 Drama not found! 🚫")
        else:
            print("😞 Failed to delete drama. Error:", result.status_code, result.json())
    except requests.exceptions.RequestException as e:
        print("⚠️ Error during request:", e)
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

def run():
    welcome_message()
    while True:
        display_menu()
        try:
            choice = int(input("🎯 Enter your choice here(1-5): "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue
        except KeyboardInterrupt:
            print("\n✋ Process interrupted. Exiting... 🚪")
            break

        if choice == 1 :
            get_all_dramas()
        elif choice == 2 :
            add_drama()
        elif choice == 3 :
            update_drama()
        elif choice == 4:
            delete_drama()
        elif choice == 5:
            print("😢 Sorry to see you go. Hope you had fun! Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please try again. 🔄")



if __name__ == '__main__':
    run()