
from util import Queue

import random


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
            return 0
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
            return 0
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return 1

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(i)

        # Create friendships
        for i in range(len(self.users)*(avgFriendships//2)):
            while not self.addFriendship(random.randint(1,len(self.users)), random.randint(1,len(self.users))):
                pass

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  
        q = Queue()
        visited[userID] = [userID]
        q.enqueue(userID)


        while len(q.queue) > 0:
            userID = q.dequeue()
            for friend in self.friendships[userID]:
                if friend not in visited and userID not in visited:
                        visited[friend] = [userID]
                        q.enqueue(friend)
                elif friend not in visited:
                    visited[friend] = [*visited[userID], friend]
                    q.enqueue(friend)
        
        


        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
