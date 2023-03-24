'''
    데이터 베이스 접속후 쿼리 수행 + 파라미터 전달
'''
import pymysql as my

def select_login(uid, upw):
    connection = None
    try:    
        connection = my.connect(host        ='localhost',
                                #port        = 3306,     
                                user        ='root',     
                                password    ='12341234', 
                                database    ='ml_db',                                
                                cursorclass =my.cursors.DictCursor
                                )
        with connection.cursor() as cursor:
            # 파라미터는 %s표시로 순서대로 세팅된다 '값' => ''는 자동으로 세팅된다
            sql = '''
                SELECT 
                    `name`, uid, regdate 
                FROM 
                    users
                WHERE
                    uid=%s
                AND
                    upw=%s;
            '''
            # execute() 함수의 2번 인자가 파라미터 전달하는 자리, 튜플로 표현
            cursor.execute( sql, (uid, upw) )
            row = cursor.fetchone()        
            print( row['name'] )
            pass
    except Exception as e:
        print('접속 오류', e)
    else:
        print('접속시 문제 없었음')
    finally:    
        if connection:
            connection.close()    

if __name__ == '__main__':
    # d4 개발자의 테스트 코드
    # f5 개발자가 사용할때는 작동않함
    select_login('guest', '1234')
