class BasicUser:
    def __init__(self, login, gecos, uid):
        self._login = login
        self._gecos = gecos
        self._uid = uid

    def login(self):
        return self._login

    def gecos(self):
        return self._gecos

    def uid(self):
        return self._uid

    def kind(self):
        assert self._uid >= 0 and self._uid < 65536
        if self._uid < 500:
            return "System"
        elif self._uid < 1000:
            return "Normal"
        else:
            return "Web-Only"

    def __str__(self):
        return ":".join([self._login, str(self._uid), self._gecos])


class ShellUser(BasicUser):
    def __init__(self, login, gecos, uid, shell):
        super().__init__(login, gecos, uid)
        self._shell = shell

    def shell(self):
        return self._shell

    def is_locked(self):
        assert self._uid >= 0 and self._uid < 65536
        if self._uid < 500:
            return False
        elif self._uid < 1000 and self._shell == "/bin/false":
            return True
        else:
            return False

    def __str__(self):
        return ":".join([self._login, str(self._uid), self._gecos, self._shell])

class UserDatabase:
    def __init__(self):
        self._users = list()
        self._logins = {"Bash":[], "C shell":[], "Web":[]}

    def open(self, filename):
        f = open(filename, "r")
        line = f.readline()
        while line != "":
            tokens = line.strip().split(":")
            if len(tokens) == 4:
                user = ShellUser(tokens[0], tokens[2], int(tokens[1]), tokens[3])
            else:
                user = BasicUser(tokens[0], tokens[2], int(tokens[1]))
            self.add(user)
            line = f.readline()
        f.close()

    def add(self, user):
        self._users.append(user)

    def bash_users(self):
        for user in self._users:
            if type(user) == ShellUser:
                shell = user.shell()
                if len(shell) >= 4 and shell[-4:] == "bash":
                    self._logins["Bash"].append(user)

    def csh_users(self):
        for user in self._users:
            if type(user) == ShellUser:
                shell = user.shell()
                if len(shell) > 3 and shell[-3:] == "csh":
                    self._logins["C shell"].append(user)

    def web_users(self):
        for user in self._users:
            if user.kind() == "Web-Only":
                self._logins["Web"].append(user)

    def save_database(self, filename):
        f = open(filename, "w")
        f.write("[Bash]\n")
        for user in self._logins["Bash"]:
            f.write(user.login() + "\n")
        f.write("\n")
        f.write("[C shell]\n")
        for user in self._logins["C shell"]:
            f.write(user.login() + "\n")
        f.write("\n")
        f.write("[Web]\n")
        for user in self._logins["Web"]:
            f.write(user.login() + "\n")
        f.close()
