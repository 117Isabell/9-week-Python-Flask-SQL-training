import  requests
import  json

# POST REQUEST
# new_drama ={
#     "drama_name": "The Judge from Hell",
#     "description": "The Judge from Hell is about the coexistence of good and evil, where Kang Bit-na, a demon from hell who enters the body of a judge, meets detective Han Da-on, who is more human than anyone else in a reality that is more hellish than hell, and is reborn as a true judge by punishing criminals.",
#     "poster": "./static/images/The_judge_from_hell.jpg",
#     "learn_more_link": "https://www.imdb.com/title/tt33255143/"
# }
# headers = {'content-type': 'application/json'}
# result = requests.post(
#     'http://127.0.0.1:5000/dramas', headers=headers, data=json.dumps(new_drama)
# )
# print(result)


# PUT REQUEST
# updated_drama = {
#      "new content": "test",
#      "drama_name": 'Start-up'
# }
#
# drama_name = 'Start-up'
#
# headers = {'content-type': 'application/json'}
# result = requests.put(
#     'http://127.0.0.1:5000/dramas/{}'.format(drama_name), headers=headers, data=json.dumps(updated_drama)
# )
# print(result)


# DELETE REQUEST
drama_name = 'Start-up'

headers = {'content-type': 'application/json'}
result = requests.delete(
    'http://127.0.0.1:5000/dramas/{}'.format(drama_name), headers=headers
)
print(result)