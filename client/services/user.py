from services.auth import Authentication


class User:
    
    def __init__(self, userManager, userID):
        pass


class UserManager(GenericInterface):
    
    def __init__(self, auth):
        GenericInterface.__init__(self, {
            "events": [
                "ready",
            ],
        })
        assert isinstance(auth, Authentication)
        self.auth = auth
        self.__start__()

    def __start__(self):
        self.auth.event("login").append(self.__loadCurrentUser())
        self.event("ready").trigger()

    def __loadCurrentUser(self):
        user = self.auth.getCurrentUser()

