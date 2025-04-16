import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan''Last week','This morning','In the year 1999','In the middle of the night','A few days ago','One sunny afternoon','One rainy day']
name=input("Enter a name:")
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England'    ,'Rome', 'Berlin', 'London', 'Dubai', 'Mexico City',
    'Tokyo', 'Cairo', 'Bangkok', 'Machu Picchu', 'Antarctica']
went = ['cinema', 'university', 'seminar', 'school', 'laundry','concert', 'museum', 'zoo', 'supermarket', 'beach',
    'mountain', 'airport', 'theme park', 'bookstore', 
    'spa', 'party', 'stadium', 'mall', 'work']
happened = ['made a lot of friends', 'ate a burger', 'found a secret key', 'solved a mystery', 'wrote a book','traveled through time', 'rescued a lost puppy', 'became a superhero', 'invented a new gadget', 'saved the day']

story = (
    random.choice(when) + ', ' +
    name + ' who lived in ' +
    random.choice(residence) + ', went to the ' +
    random.choice(went) + ' and ' +
    random.choice(happened) + '.'
)

print(story)