from util.interface import GenericInterface


class Authentication(GenericInterface):

    def __init__(self):
        GenericInterface.__init__(self, {
            "events": [
                "ready",    # when service is loaded
                "login",    # when user signs in
                "logout",   # when user signs out
            ],
        })
        self.__start__()

    def getCurrentUser(self):
        return firebase.auth().currentUser

    def __onAuthStateChanged(self):
        if self.getCurrentUser():
            self.event("login").trigger()
        else:
            self.event("logout").trigger()

    def __start__(self):
        firebase.auth().onAuthStateChanged(self.__onAuthStateChanged)
        self.event("ready").trigger()

    async def logout(self):
        firebase.auth().signOut()
