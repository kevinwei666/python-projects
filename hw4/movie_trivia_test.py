import unittest
from movie_trivia import*

class Test_MovieTrivia(unittest.TestCase):

    def test_insert_actor_info(self):
        """
        test of insert actor info function
        """
        #set the example lists
        a={'name':'zed','age':'uyg'}
        b={'name':['zed'],'age':'uyg'}
        c={'name':'zed','age':'uyg','weight':'ytr'}
        d={'name':['zed','kevin'],'age':'uyg'}
        #test if the real value equals to expectation
        insert_actor_info( 'weight', 'ytr',a)
        self.assertEqual(c,a,'should be equal')
        insert_actor_info('name','kevin',b)
        self.assertEqual(b,d,'should be equal')
        
    def test_insert_rating(self):
        """
        test of insert_rating function
        """
        #set the example lists
        a={'name':'zed','age':'uyg'}
        b={'name':['zed'],'age':'uyg'}
        c={'name':'zed','age':'uyg','weight':'ytr'}
        d={'name':['zed','kevin'],'age':'uyg'}
        #test if the real value equals to expectation
        insert_rating( 'weight', 'ytr',a)
        self.assertEqual(c,a,'should be equal')
        insert_rating('name','kevin',b)
        self.assertEqual(b,d,'should be equal')
    def test_select_where_actor_is(self):
        """
        test of select_where_actor_is function
        """
        #set the example lists
        a={'Name':['zed','kevin'],'age':['uyg']}
        select_where_actor_is('name',a)
        #test if the real value equals to expectation
        self.assertEqual(['zed','kevin'], select_where_actor_is('name',a),'should be equal')
        self.assertEqual(['uyg'], select_where_actor_is('age',a),'should be equal')
        self.assertEqual([], select_where_actor_is('ageh',a),'should be equal')
    def test_select_where_movie_is(self):
        """
        test of select_where_movie_is function
        """
        #set the example lists
        a={'name':['zed','kevin'],'age':['uyg']}
        select_where_movie_is('zed',a)
        #test if the real value equals to expectation
        self.assertEqual(['name'], select_where_movie_is('zed',a),'should be equal')
        self.assertEqual([], select_where_movie_is('zedw',a),'should be equal')
    def test_select_where_rating_is(self):
        """
        test of select_where_rating_is function
        """
        #set the example dict
        a={'Sb':['79','78'],'Dsb':['94','82'],'Chjdsb':['97','90']}
        #test if the real value equals to expectation
        self.assertEqual(['Dsb','Chjdsb'],select_where_rating_is('>',80,True,a),'should be equal')
        self.assertEqual(['Dsb'],select_where_rating_is('=',94,True,a),'should be equal')
        self.assertEqual(['Sb'],select_where_rating_is('<',85,True,a),'should be equal')
        self.assertEqual(['Dsb','Chjdsb'],select_where_rating_is('>',80,False,a),'should be equal')
        self.assertEqual(['Dsb'],select_where_rating_is('=',82,False,a),'should be equal')
        self.assertEqual(['Sb','Dsb'],select_where_rating_is('<',90,False,a),'should be equal')
        self.assertEqual([],select_where_rating_is('>',100,True,a),'should be equal')
    def test_get_co_actors(self):
        """
        test of get_co_actors function
        """
        #set the example dict
        a={'name1':['zed','marry'],'name2':['zed','kevin'],'name3':['marry'],'age':['uyg'],'name4':['zed','marry','kevin']}
        #test if the real value equals to expectation
        self.assertEqual(['name2','name4','name3'],get_co_actors('name1',a))
        self.assertEqual([],get_co_actors('age',a))
        self.assertEqual([],get_co_actors('ag',a))
        b={'name1':['zed','marry'],'name2':['zed','kevin'],'age':['uyg']}
        self.assertEqual(['name2'],get_co_actors('name1',b))

    def test_get_common_movie(self):
        """
        test of get_common_movie function
        """
        #set the example dict
        a={'name1':['zed','marry'],'name2':['zed','kevin'],'age':['uyg']}
        #test if the real value equals to expectation
        self.assertEqual(['zed'],get_common_movie('name1','name2',a))
        self.assertEqual([],get_common_movie('name1','age',a))
        self.assertEqual([],get_common_movie('nam','ae',a))
        
    def test_good_movies(self):
        """
        test of insert actor info function
        """
        #set the example dict
        a={'a':['9','99'],'b':['98','39'],'c':['85','85']}
        #test if the real value equals to expectation
        self.assertEqual({'c'},good_movies(a))
        b={'a':['99','99'],'b':['98','39'],'c':['85','85']}
        self.assertEqual({'a','c'},good_movies(b))
        c={'a':['9','90'],'b':['98','39'],'c':['85','85']}
        self.assertEqual({'c'},good_movies(c))
        
        
        
    def test_get_common_actors(self):
        """
        test of insert actor info function
        """
        #set the example dict
        a={'name1':['zed','marry','kevin'],'name2':['zed','kevin'],'age':['uyg']}
        #test if the real value equals to expectation
        self.assertEqual(['name1','name2'],get_common_actors('zed','kevin',a))
        self.assertEqual([],get_common_actors('zed','uyg',a))
        self.assertEqual([],get_common_actors('zed','ke',a))
        
    def test_avoid_duplicate(self):
        """
        avoid the duplicate in the list
        """
        #test if the real value equals to expectation
        list1=['1','2','3','3','3']
        self.assertEqual(['1','2','3'],avoid_duplicate(list1))
        list2=[1,1,1,2,3,3,3]
        self.assertEqual([1,2,3],avoid_duplicate(list2))
        
        
#execute the test        
unittest.main()
