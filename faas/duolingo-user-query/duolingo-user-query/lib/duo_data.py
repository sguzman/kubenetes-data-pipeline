import datetime
import logging
import os
import random
import time
import typing

from duo import duolingo

fr_type = typing.List[typing.Dict[str, list]]
lo_type = typing.Optional[typing.List[str]]


class DuoStuff:
    duo_sess = None

    @staticmethod
    def login() -> None:
        user = open('/var/openfaas/secrets/duolingo-user').read().replace("\n", " ")
        password = open('/var/openfaas/secrets/duolingo-pass').read().replace("\n", " ")

        lingo = duolingo.Duolingo(username=user, password=password)
        DuoStuff.duo_sess = lingo

    @staticmethod
    def set_user(user: str) -> None:
        DuoStuff.duo_sess.set_username(user)

    @staticmethod
    def user_info():
        return DuoStuff.duo_sess.get_user_info()

    @staticmethod
    def get_langs():
        return DuoStuff.duo_sess.get_languages(abbreviations=False)

    @staticmethod
    def get_friends():
        return DuoStuff.duo_sess.get_friends()

    @staticmethod
    def get_streak_info():
        return DuoStuff.duo_sess.get_streak_info()

    @staticmethod
    def get_leaderboard():
        return DuoStuff.duo_sess.get_leaderboard(unit='week', before=time.time())

    @staticmethod
    def get_calendar():
        return DuoStuff.duo_sess.get_calendar()


class User:
    user: str

    def __init__(self, user: str):
        self.user = user
        DuoStuff.login()
        DuoStuff.set_user(user)

    @staticmethod
    def user_info():
        obj = DuoStuff.user_info()
        return obj

    @staticmethod
    def langs():
        obj = DuoStuff.get_langs()
        return obj

    @staticmethod
    def friends():
        obj = DuoStuff.get_friends()
        return obj

    @staticmethod
    def streak_info():
        obj = DuoStuff.get_streak_info()
        return obj

    @staticmethod
    def leaderboard():
        obj = DuoStuff.get_leaderboard()
        return obj

    @staticmethod
    def calendar():
        obj = DuoStuff.get_calendar()
        return obj

    def all(self):
        logging.info('Starting user %s', self.user)

        return {
            'user': self.user,
            'time': datetime.datetime.now(),
            'user_info': self.user_info(),
            'langs_abrev': self.langs(),
            'friends': self.friends(),
            'streak_info': self.streak_info(),
            'leaderboard': self.leaderboard(),
            'calendar': self.calendar()
        }


def get_user(user):
    ws = User(user)
    return ws.all()