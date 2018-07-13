from util.interface import GenericInterface


class Authentication(GenericInterface):

    def __init__(self):
        GenericInterface.__init__(self, {
            "events": [
                "login",    # when user signs in
                "logout",   # when user signs out
            ],
        })
        self.__start__()

    def getCurrentUser(self):
        return firebase.auth().currentUser

    def __onAuthStateChanged(self):
        user = self.getCurrentUser()
        if user:
            self.event("login").trigger(user)
        else:
            self.event("logout").trigger()

    def __start__(self):
        firebase.auth().onAuthStateChanged(self.__onAuthStateChanged)

    async def login(self):
        provider = __new__(firebase.auth.GoogleAuthProvider())
        try:
            result = await firebase.auth().signInWithPopup(provider)
        except:
            pass

    async def logout(self):
        firebase.auth().signOut()
