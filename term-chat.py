from fbchat import Client
from fbchat.models import *
import getpass
import time
import thread
from blessings import Terminal

term = Terminal()


fb_logo = '''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$~           .,$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z.                 Z$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                    Z$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z                     Z$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$7                      Z$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z                       Z$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                        Z$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$               ~I7777777$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:             $$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             Z$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z                                  ~$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z                                  $$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z                                  Z$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z                                  $$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z                                 .$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z                                 +$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z                                 Z$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z                                 Z$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             $$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.............$$$$$$$$$$$$$$$$$$$$$$$$$'''

welcome = term.clear() + '''\n\n
~~~~~~~~~~~~ WELCOME TO TERMCHAT ~~~~~~~~~~~
~~~ facebook messenger for your terminal ~~~
\n\n\n\n\n\n\n'''



class FBChat(Client):

    def login(self, email, password, max_tries):

        self.onLoggingIn(email=email)

        self.email = email
        self.password = password

        login_successful, login_url = self._login()

        if not login_successful:
            print('Login not successful, please enter the correct credentials!')
        else:
            self.onLoggedIn(email=email)


    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)

        if self.uid != author_id:
            user = self.fetchUserInfo(author_id)

            print('{}: {}'.format(user[author_id].name.split()[0], message) + term.clear_eol())


    def onMessageSeen(self, seen_by=None, thread_id=None, thread_type=ThreadType.USER, seen_ts=None, ts=None, metadata=None, msg={}):
        """
        Called when the client is listening, and somebody marks a message as seen
        :param seen_by: The ID of the person who marked the message as seen
        :param thread_id: Thread ID that the action was sent to. See :ref:`intro_threads`
        :param thread_type: Type of thread that the action was sent to. See :ref:`intro_threads`
        :param seen_ts: A timestamp of when the person saw the message
        :param ts: A timestamp of the action
        :param metadata: Extra metadata about the action
        :param msg: A full set of the data recieved
        :type thread_type: models.ThreadType
        """
        # log.info("Messages seen by {} in {} ({}) at {}s".format(seen_by, thread_id, thread_type.name, seen_ts/1000))

    def onMessageDelivered(self, msg_ids=None, delivered_for=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg={}):
        """
        Called when the client is listening, and somebody marks messages as delivered
        :param msg_ids: The messages that are marked as delivered
        :param delivered_for: The person that marked the messages as delivered
        :param thread_id: Thread ID that the action was sent to. See :ref:`intro_threads`
        :param thread_type: Type of thread that the action was sent to. See :ref:`intro_threads`
        :param ts: A timestamp of the action
        :param metadata: Extra metadata about the action
        :param msg: A full set of the data recieved
        :type thread_type: models.ThreadType
        """
        # log.info("Messages {} delivered to {} in {} ({}) at {}s".format(msg_ids, delivered_for, thread_id, thread_type.name, ts/1000))

    def onInbox(self, unseen=None, unread=None, recent_unread=None, msg={}):
        """
        .. todo::
            Documenting this
        :param unseen: --
        :param unread: --
        :param recent_unread: --
        :param msg: A full set of the data recieved
        """
        # log.info('Inbox event: {}, {}, {}'.format(unseen, unread, recent_unread))


def start():

    print(welcome)
    print('Enter your login credentials to continue...')

    email = raw_input('Email: ')
    password = getpass.getpass("Password: ")

    print(term.clear())
    print(welcome)

    client = FBChat(email, password)
    return client


def search(client):

    print(term.clear())
    print(welcome)
    print('Start a conversation by searching for a user!')
    fname = raw_input('First name: ')
    lname = raw_input('Last name: ')

    results = client.searchForUsers('{} {}'.format(fname, lname))

    if len(results) < 1:
        print 'Sorry! We couldn\'t find who you were looking for.'
        return None

    return results[0]


def conversation(user, me, client):

    print(term.clear())
    print(welcome)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Starting a conversation with {}'.format(user.name))
    print('')
    print('')
    print('')

    def talk():

        while True:
    
            message = raw_input()

            client.sendMessage(message, thread_id=user.uid, thread_type=ThreadType.USER)

            try:
                print(term.move_up() + '{}: {}'.format(me.name.split()[0], message) + term.clear_eol())
            except UnicodeEncodeError:
                print(term.move_up() + '{}: emoji'.format(me.name.split()[0]) + term.clear_eol())


    try:
        thread.start_new_thread(talk, ())
        thread.start_new_thread(client.listen, ())
    except:
        print('nope')

    while 1:
        pass


def term_chat():

    print(term.blue + fb_logo + term.normal)
    raw_input('Hit enter to continue...')

    client = start()

    while not client.isLoggedIn():
        client = start()

    user = client.fetchUserInfo(client.uid)
    me = user[client.uid]

    user = None

    while user == None:
        user = search(client)

    conversation(user, me, client)


term_chat()


# class Message(Client):
#     def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
#         self.markAsDelivered(author_id, thread_id)
#         self.markAsRead(author_id)

#         print("Message from {} in {} ({}): {}".format(author_id, thread_id, thread_type.name, message))


# email = "marina@elementalmusic.net"
# password = "potatoface"
# client = Message(email, password)

# # if not client.isLoggedIn():
# #     client.login('<email>', '<password>')

# # client.logout()

# message = "hi david"
# # user = "cottrell.david"

# users = client.searchForUsers('David Cottrell')
# user = users[0]
# print("User's ID: {}".format(user.uid))
# print("User's name: {}".format(user.name))
# client.sendMessage(message, thread_id='100001439708199', thread_type=ThreadType.USER)
# client.sendMessage('<message>', thread_id='<group id>', thread_type=ThreadType.GROUP)



# client.doOneListen();